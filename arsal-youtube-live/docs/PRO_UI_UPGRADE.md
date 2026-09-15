# Arsal YouTube Live Pro UI v1.1 — Upgrade Blueprint

## Product goal
Turn the functional v1.0 streaming app into a studio-grade desktop product without making the live workflow harder. Preserve the existing FFmpeg/RTMPS behavior and prioritize clarity, safety, performance, and fast operation.

## Visual direction
- Premium dark desktop studio, not a generic web form.
- Strong hierarchy: brand/status header, workflow progress, source rail, central studio preview, destination inspector, sticky control dock.
- Subtle depth, restrained blue accents, distinct live/success/warning/error states.
- Compact typography and spacing appropriate for 1366×768 through 1920×1080 displays.

## Main layout
1. Top bar: brand, PRO marker, health, live status, stream mode.
2. Workflow strip: Source → Destinations → Pre-flight → Live.
3. Left rail: Source, Playback, Safety.
4. Center workspace: 16:9 and 9:16 previews plus Layout/Crop/Output inspector.
5. Right rail: routing, stream-key cards, encoder summary, pre-flight.
6. Lower panel: Live Stats, Pre-flight report, Activity.
7. Sticky bottom dock: session state, elapsed time, estimated output, Pre-flight, Start/Stop Live.

## UX rules
- Never auto-start a stream.
- Keep stream keys masked by default.
- Advanced information should not crowd the primary workflow.
- All live state changes need both color and text.
- Preview controls must edit the same crop/fit data consumed by FFmpeg.
- A user should understand the next required step without reading documentation.

## Performance strategy
- Use focused Zustand selectors so components subscribe only to relevant state.
- Memoize high-frequency preview and destination components.
- Throttle FFmpeg metric events to about 2 updates/second while emitting state transitions immediately.
- Use metadata-preloaded previews instead of eager full media loading.
- Keep heavy encoding in Electron main/FFmpeg processes, never in the React renderer.
- Avoid animation-heavy effects and unbounded log DOM growth.

## Acceptance criteria
- Existing horizontal, vertical and dual streaming behavior remains intact.
- v1.0.1 renderer-path fix remains intact (`base: './'`).
- 7 existing automated tests pass.
- TypeScript typecheck passes.
- Windows NSIS and portable builds complete successfully.
- UI remains usable at 1366×768 and polished at 1920×1080.
