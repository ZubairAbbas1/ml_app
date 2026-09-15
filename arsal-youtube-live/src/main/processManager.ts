import { ChildProcessWithoutNullStreams, spawn } from 'child_process';
import { EventEmitter } from 'events';
import type { AppConfig, MediaInfo, OutputConfig, StreamStats, Encoder } from '../shared/types';
import { buildStreamArgs, ffmpegPath } from './ffmpeg';

type K = 'horizontal' | 'vertical';

export class StreamProcessManager extends EventEmitter {
  private p = new Map<K, ChildProcessWithoutNullStreams>();
  private stopSet = new Set<K>();
  private retries = new Map<K, number>();
  private lastMetricEmit = new Map<K, number>();
  stats: Record<K, StreamStats> = {
    horizontal: { state: 'offline', fps: 0, bitrateKbps: 0, speed: '0x', frames: 0, elapsed: 0, reconnects: 0 },
    vertical: { state: 'offline', fps: 0, bitrateKbps: 0, speed: '0x', frames: 0, elapsed: 0, reconnects: 0 },
  };

  constructor(private media: MediaInfo, private cfg: AppConfig, private encoder: Encoder) { super(); }
  start(k: K, o: OutputConfig) { if (this.p.has(k)) return; this.stopSet.delete(k); this.launch(k, o); }
  private launch(k: K, o: OutputConfig) {
    this.set(k, { state: 'connecting' }, true);
    const cp = spawn(ffmpegPath(), buildStreamArgs(this.media, o, this.cfg, this.encoder), { windowsHide: true });
    this.p.set(k, cp);
    let streaming = false;
    cp.stderr.setEncoding('utf8');
    cp.stderr.on('data', (s: string) => {
      if (!streaming && /frame=|Output #0/i.test(s)) { streaming = true; this.retries.set(k, 0); this.set(k, { state: 'streaming', lastError: undefined }, true); }
      const fm = s.match(/frame=\s*(\d+)/), fps = s.match(/fps=\s*([\d.]+)/), br = s.match(/bitrate=\s*([\d.]+)kbits\/s/), sp = s.match(/speed=\s*([^\s]+)/), tm = s.match(/time=(\d+):(\d+):(\d+(?:\.\d+)?)/);
      const patch: Partial<StreamStats> = {};
      if (fm) patch.frames = +fm[1]; if (fps) patch.fps = +fps[1]; if (br) patch.bitrateKbps = +br[1]; if (sp) patch.speed = sp[1]; if (tm) patch.elapsed = (+tm[1]) * 3600 + (+tm[2]) * 60 + (+tm[3]);
      if (Object.keys(patch).length) this.set(k, patch, false);
    });
    cp.on('error', e => this.set(k, { state: 'error', lastError: e.message }, true));
    cp.on('exit', () => {
      this.p.delete(k);
      if (this.stopSet.has(k)) { this.set(k, { state: 'offline' }, true); return; }
      if (this.cfg.autoReconnect) {
        const n = (this.retries.get(k) || 0) + 1; this.retries.set(k, n); this.set(k, { state: 'reconnecting', reconnects: n, lastError: 'Encoder exited; reconnecting' }, true);
        const delays = [2000, 5000, 10000, 15000, 30000]; setTimeout(() => { if (!this.stopSet.has(k)) this.launch(k, o); }, delays[Math.min(n - 1, delays.length - 1)]);
      } else this.set(k, { state: 'error', lastError: 'Encoder exited' }, true);
    });
  }
  private set(k: K, patch: Partial<StreamStats>, forceEmit = false) {
    this.stats[k] = { ...this.stats[k], ...patch };
    const now = Date.now(), last = this.lastMetricEmit.get(k) || 0;
    if (!forceEmit && now - last < 500) return;
    this.lastMetricEmit.set(k, now);
    this.emit('stats', { key: k, stats: this.stats[k] });
  }
  stop(k: K) {
    this.stopSet.add(k); const cp = this.p.get(k);
    if (!cp) { this.set(k, { state: 'offline' }, true); return; }
    this.set(k, { state: 'stopping' }, true); cp.stdin.write('q\n'); setTimeout(() => { if (!cp.killed) cp.kill(); }, 3000);
  }
  stopAll() { this.stop('horizontal'); this.stop('vertical'); }
}
