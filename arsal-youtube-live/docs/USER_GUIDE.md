# Arsal YouTube Live Studio Edition v3.0 — User Guide

## Fast start
1. Open YouTube Studio and create/open an encoder live stream for every YouTube channel you want to use.
2. Copy each RTMPS server URL and stream key.
3. In **Studio**, click **Add videos** and select one or many files.
4. In **Mission Control**, paste the primary key(s) and add any extra channels.
5. Enter a recent upload-speed result and click **Auto Optimize**.
6. Run **Pre-flight**, then press **START LIVE**.
7. Keep YouTube Studio > Stream health open. Arsal Live marks individual channel relays STREAMING only after FFmpeg reports real outgoing media progress.

## Mission Control and isolated channel relays
Studio Edition v3 changes the multi-channel architecture. Each horizontal or vertical format is encoded once, then distributed to lightweight per-channel relay processes on localhost. Each relay independently connects to its RTMP/RTMPS destination.

Benefits:
- one failed channel can reconnect without stopping healthy channels;
- **Retry failed only** restarts only unhealthy destination relays;
- **Stop only this** can stop one channel while the remaining channels continue;
- each channel has its own connection state, reconnect count, bitrate/FPS telemetry, ingest host and last error;
- scene and adaptive-quality encoder restarts do not intentionally tear down all destination relays.

Encoding is shared, but upload bandwidth still multiplies per destination. A 4 Mbps output sent to three channels requires roughly 12 Mbps plus audio/protocol overhead.

## Program / Preview Studio Mode
Studio includes separate Preview and Program scene controls. Select **Video**, **Starting Soon**, **BRB**, or **End Screen** in Preview, then press **TAKE → PROGRAM**. The shared encoder changes the program source while destination relays remain isolated.

Safe operator hotkeys when enabled:
- `Ctrl+Alt+B` → BRB
- `Ctrl+Alt+V` → Video
- `Ctrl+Alt+F` → Fix My Stream

There is deliberately no one-key Start Live hotkey.

## Playlist and media QC
- Add multiple videos at once.
- Drag rows to reorder.
- Loop the full playlist or shuffle the session order.
- **Scan media health** analyzes the first 30 seconds for long black-frame sections, long silence and basic compatibility warnings.

Matching codecs/FPS/resolutions generally provide smoother playlist transitions.

## Smart stability engine
- **Adaptive Network** monitors shared-encoder real-time speed.
- If speed remains below real time, the encoder steps down through Full HD → 720p → 540p → emergency profile.
- **Auto quality recovery** can test one level higher after a stable period.
- **Safe Mode** favors stability and low preview load.
- **Fix My Stream** immediately requests a safer runtime quality profile.
- **Auto Optimize** includes the number of active destinations in its upload calculation.

No application can guarantee smooth streaming when the actual upload capacity is below the total outgoing bitrate. Reduce quality or destination count when necessary.

## Audio Mixer
Studio Edition provides:
- source volume and gain;
- limiter;
- compressor;
- noise gate;
- optional looping background-music file;
- background-music volume;
- voice ducking, which lowers the music bed while source audio is present.

## Branding
Add text and PNG/JPG/WEBP logo overlays. Disable heavy overlays and local recording if an older laptop cannot sustain encoder speed at or above 1.0x.

## Local recording
Enable segmented MKV recording for crash-resistant backups. Choose the segment duration and optionally remux MKV recordings to MP4 after Stop.

## Automation
The scheduler can start/stop a session on selected weekdays while the app is open. Automatic starts still require valid media and destination configuration. Opening the app by itself never starts a broadcast.

## Remote Operator Console
In **Automation**, enable Remote Control. By default it listens only on the same computer. Enabling LAN mode exposes the authenticated operator page to devices on the same network.

The remote URL contains a secret token. Keep it private. The remote page supports:
- Video / Starting / BRB / End Screen;
- Fix Streams;
- Retry Failed;
- Stop All;
- live status refresh.

Remote control intentionally cannot silently start a new broadcast.

## Watchdog and crash recovery
Encoder failures are monitored and retried according to the configured reconnect policy. Channel relay failures are retried independently. If the renderer/UI crashes while the main Electron process remains alive, the UI is reloaded while the streaming engine remains owned by the main process.

If the previous session ended abnormally, the next launch displays a warning. Broadcasting is never automatically resumed after a crash.

## Profiles and security
Profile export/import excludes stream keys and the remote token. When **Remember keys securely** is enabled, stream keys are stored using Electron/Windows encrypted storage. Logs and diagnostic exports should never contain complete stream keys.

## Diagnostics
Diagnostics includes:
- application/system information;
- encoder output speed/FPS/bitrate;
- per-channel state;
- ingest reachability test;
- media QC scan results;
- activity/audit trail;
- secret-redacted support export.

## Current external-service boundaries
Manual RTMPS/RTMP streaming is fully usable without a Google API project. YouTube OAuth account control, cloud guest calling, true multi-ISP bonded transport and signed automatic updates require external credentials/services/infrastructure and are not silently simulated by this desktop build.
