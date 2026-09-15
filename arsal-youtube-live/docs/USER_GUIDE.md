# Arsal YouTube Live Ultra Pro Max — User Guide

## Fast start
1. Open YouTube Studio and create/open an encoder live stream.
2. Copy the RTMPS server URL and the correct stream key. If using dual horizontal + vertical encoder streaming, configure both keys.
3. Open Arsal YouTube Live and use **Add Playlist**. Select one or many videos.
4. Enter your recent upload speed if known, then click **Auto Optimize**.
5. Paste stream key(s), run **Pre-flight**, then press **START LIVE**.
6. Keep YouTube Studio > Stream health open. The app shows LIVE only after FFmpeg reports real outgoing media progress.

## Simple vs Pro
- **Simple** keeps the main playlist, previews, destinations, Auto Optimize, Safe Mode and Start/Stop controls visible.
- **Pro** adds Health & Analytics, audio processing, overlays, recording, scheduler, latency planning, diagnostics and the activity timeline.

## Smart stability
- **Adaptive Network** monitors encoder speed and reconnects. If output stays below real-time, it automatically steps down through 1080p, 720p, recovery and emergency profiles.
- **Auto quality recovery** can test one level higher after a stable period.
- **Safe Mode** prepares a conservative 720p30 / 4 Mbps profile and reduces preview load.
- **Fix My Stream** can be pressed during a live session to force the next safer runtime profile.
- For maximum viewer buffering resilience, use **Normal latency** in YouTube Live Control Room.

## Playlist
Add multiple files, drag rows to reorder, and enable **Loop full playlist**. The live encoder plays top-to-bottom and returns to the first file. Shuffle can randomize the session order.

## Live scenes
While streaming you can request **Video**, **Starting Soon**, **BRB**, or **End Screen**. In this version a scene switch performs a short controlled encoder reconnect to keep implementation reliable.

## Audio
Pro mode includes volume/gain, limiter, compressor and noise-gate controls. Limiter is enabled by default.

## Overlays
Enable a text overlay or choose a PNG/JPG/WEBP logo/watermark. Configure position and keep overlays disabled if maximum performance is required on a weak laptop.

## Recording
Enable segmented MKV local backup for crash resistance. Choose a recording folder and segment length. Optional remux converts MKV files to MP4 after streaming or on demand. Local recording adds extra encoding load, so disable it if encoder speed falls below 1.0x.

## Scheduler
The scheduler works while the app is open. Set start/stop time and active weekdays. Automatic start only works when the playlist and stream keys are valid.

## Profiles
Use **Save Profile** to store non-secret configuration presets. Stream keys are intentionally excluded from profile storage. Enable **Remember keys securely** only if you want Windows encrypted credential storage.

## Diagnostics
Use **Analyze Network** to test reachability/latency to the configured ingest server. It does not pretend to measure upload bandwidth; enter a recent upload speed result for Auto Optimize. Use **Export diagnostics** to save a secret-redacted session report.

## Recommended YouTube basics
Use RTMPS, H.264, AAC stereo, CBR and a 2-second keyframe interval. For H.264 YouTube recommends roughly 10 Mbps for 1080p30 and 4 Mbps for 720p30, but choose a quality your upload and encoder can sustain reliably.
