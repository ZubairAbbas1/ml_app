# Arsal YouTube Live Ultra Pro Max Multi-Channel — User Guide

## Fast start
1. Open YouTube Studio and create/open an encoder live stream for each YouTube channel you want to use.
2. Copy each channel's RTMPS server URL and stream key.
3. Open Arsal YouTube Live and use **Add Playlist**. Select one or many videos.
4. Paste the primary horizontal / vertical key(s). For more channels use **Additional Lives** and add a 16:9 or 9:16 destination per channel.
5. Enter your recent upload speed if known, then click **Auto Optimize**.
6. Run **Pre-flight**, then press **START LIVE**.
7. Keep YouTube Studio > Stream health open for each channel. The app shows LIVE only after FFmpeg reports real outgoing media progress.

## Multi-channel / multiple lives
- Add as many extra destinations as your connection can sustain.
- Every destination has its own channel name, format, server URL, stream key, and enabled toggle.
- Horizontal destinations share one horizontal encode. Vertical destinations share one vertical encode. This saves CPU/GPU compared with encoding every channel separately.
- Upload bandwidth still multiplies per destination. Example: a 4 Mbps vertical stream sent to three channels uses roughly 12 Mbps plus audio/protocol overhead.
- Auto Optimize includes destination count when choosing a safe quality profile.
- If one tee destination fails, FFmpeg is configured to keep other destinations running when possible.
- Stream keys are credentials. Enable **Remember keys securely** only if you want them stored using Windows encrypted storage.

## Simple vs Pro
- **Simple** keeps playlist, previews, primary destinations, multi-channel lives, Auto Optimize, Safe Mode, and Start/Stop visible.
- **Pro** adds Health & Analytics, audio processing, overlays, recording, scheduler, latency planning, diagnostics, and activity timeline.

## Smart stability
- **Adaptive Network** monitors encoder speed and reconnects. If output stays below real-time, it automatically steps down through 1080p, 720p, recovery, and emergency profiles.
- **Auto quality recovery** can test one level higher after a stable period.
- **Safe Mode** prepares a conservative 720p30 / 4 Mbps profile and reduces preview load.
- **Fix My Stream** can be pressed during a live session to force the next safer runtime profile.
- For maximum viewer buffering resilience, use **Normal latency** in YouTube Live Control Room.
- No software can guarantee smooth video when available upload is below the total bitrate required by all channels. Reduce resolution/bitrate or the number of simultaneous destinations when needed.

## Playlist
Add multiple files, drag rows to reorder, and enable **Loop full playlist**. The live encoder plays top-to-bottom and returns to the first file. Shuffle can randomize the session order.

## Live scenes
While streaming you can request **Video**, **Starting Soon**, **BRB**, or **End Screen**. In this version a scene switch performs a short controlled encoder reconnect.

## Audio
Pro mode includes volume/gain, limiter, compressor, and noise-gate controls. Limiter is enabled by default.

## Overlays
Enable a text overlay or choose a PNG/JPG/WEBP logo/watermark. Configure position and keep overlays disabled if maximum performance is required on a weak laptop.

## Recording
Enable segmented MKV local backup for crash resistance. Choose a recording folder and segment length. Optional remux converts MKV files to MP4 after streaming or on demand. Local recording adds extra encoding load, so disable it if encoder speed falls below 1.0x.

## Scheduler
The scheduler works while the app is open. Set start/stop time and active weekdays. Automatic start only works when playlist and destination keys are valid.

## Profiles
Use **Save Profile** to store non-secret configuration presets. Stream keys are intentionally excluded from profiles. Secure remembered keys remain separate.

## Diagnostics
Use **Analyze Network** to test reachability/latency to the configured ingest server. It does not pretend to measure upload bandwidth; enter a recent upload result for Auto Optimize. Use **Export diagnostics** to save a secret-redacted report.

## Recommended YouTube basics
Use RTMPS, H.264, AAC stereo, CBR, and a 2-second keyframe interval. For H.264 YouTube recommends roughly 10 Mbps for 1080p30 and 4 Mbps for 720p30, but choose a quality that your encoder and total multi-channel upload can sustain reliably.
