# Arsal YouTube Live v1.2

This release focuses on two user-reported issues:

1. Proper multi-video playlist playback: videos run in order, then the playlist loops from the first item when Loop is enabled.
2. Reliable YouTube ingest status: the app no longer reports LIVE merely because FFmpeg started encoding. LIVE is shown only after FFmpeg reports real output progress after the RTMP/RTMPS output has opened.

Additional reliability work:
- Real hardware encoder capability probing instead of selecting NVENC/QSV/AMF only because FFmpeg lists the codec.
- Automatic CPU x264 fallback when requested hardware encoding is unavailable.
- Adaptive bitrate reduction across reconnect attempts when Adaptive Network is enabled.
- Clearer ingest and connection errors.
- Playlist order controls and now-playing indication.
- Safer RTMP/RTMPS URL validation and improved reconnect diagnostics.
