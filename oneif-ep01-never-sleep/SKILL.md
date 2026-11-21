---
name: oneif-ep01-never-sleep
description: One If episode 1, "What If You Never Needed Sleep?" (5:23 Bold Toon SVG film, 1920×1080, Theo + narrator). Use to re-render, re-time, fix shots, sound or captions on it, re-cut it into Shorts, or reuse its sets (rooms.js), word-cued camera cuts, lip sync and audio pipeline for a new episode.
---

# One If ep01: "What If You Never Needed Sleep?"

- **Project:** `whatif/episodes/ep01-never-sleep/` (HyperFrames 0.8.183, SVG + GSAP, 1920×1080, 30fps, `DUR` 323.44s)
- **Delivered:** `whatif/renders/whatif-ep01-final.mp4` (5:23), `whatif-ep01-thumbnail.png` (1280×720), `whatif-ep01-captions-en.srt`; the approved animatic is `whatif-ep01-animatic.mp4`
- **Upload sheet:** `UPLOAD.md` (title, description, chapters, tags). **Script:** `SCRIPT.md` (cast, voices, shots, fact check, build list)
- **Style:** Bold Toon, `whatif/kit/STYLE.md`. This channel does **not** use the 13learns brand. Borrow only the system from Ifverse, never their scripts, twists, black-head stickmen or thumbnail layout. No vidIQ.

## The story

At 3 AM the whole city is asleep except you: Theo (17, teal hoodie) hasn't slept in 400 days. The episode covers the rule and how it works (narrator explainer cards), then the ladder of what eight free hours buy: Spanish in 75 nights and the taco test, chess, code, a robot, DAY 400, and Dr. Okafor's lab. The cost: "u up?" with no replies, an empty city, Sam's shark dream ("What does dreaming feel like again?"). The choice: Mr. Vance at "Lumen" wants to bottle it for 8 billion people ("Nobody gets eight hours back. Their bosses do."), and Okafor could reverse it. In the resolution, Zuri has a bad dream and asks him to keep watch. He says no to the pill and no to the cure. Sequel hook: DAY 1,000, someone waves back from another roof (PART 2). Then the science check (our signature segment) and the call to action.

Cast and ElevenLabs voices (model `eleven_v4`, one take per line): Narrator Brendan `hnu83udpXxIAiBp91Ci5`, Theo Louie the Legend `ataV0GNgfIus2NWdTJP0`, Zuri Boo, Mom Ms. Harris, Sam Kai, Dr. Okafor Aurora, Mr. Vance Asher 2.0, Waiter Eduardo. All 29 lines are in `assets/audio/vo/`, listed in `assets/audio/VO.md`. ElevenLabs blocks child voices, so Zuri is written about 13. Don't work around that filter.

## How it's built

- `timeline.js` is **generated** by `assets/audio/build_timeline.py`: every voice clip's start, its Whisper word times and a lip-sync envelope. Never hand-edit it.
- `scene.js`: shots are registered with `shot(id, name, start, build)`. Each builds its SVG group once, and `renderAt(t)` shows the active shot and updates it, a pure function of `t`.
  - Timing helpers: `C(clip)` = clip start, `E(clip)` = clip end, `W(clip, word, nth)` = when a word is spoken. Cut on words, not on seconds.
  - Coverage: `CUTS` (set shots: `[time, x, y, zoom]` hard cuts through `cutCam`) and `CARD_CUTS` (motion-graphic cards zoom the whole card).
  - `ANIMATIC = false` hides the review overlay (shot label + ANIMATIC tag). Set it to `true` for a review cut.
  - Builders: `actor()`, `text()`, `chip()`, `cardBg()`, `subtitle()`, `tinkerPose()`.
- `rooms.js`: this episode's finished sets (`buildRoom` with lights, beams and stars). The shared set library is `whatif/kit/rooms.js`.
- `kit/`: a copy of `whatif/kit` (rig with IK, `makeCharacter(parent, look).set(pose, face)`, `mouthFromEnvelope`, sets, util). Re-copy with `bash whatif/sync-kit.sh whatif/episodes/ep01-never-sleep` after kit changes.
- `index.html` plays `assets/audio/final_mix.wav` as a single audio track.

## Audio pipeline (run from the episode folder, in this order)

```bash
python3 -I assets/audio/build_timeline.py   # voice clips -> timeline.js + mix.wav
python3 -I assets/audio/build_music.py      # 3 ElevenLabs score cues fitted to the acts -> music.wav
python3 -I assets/audio/build_sfx.py        # ambience beds per shot + spot FX, ducked -> sfx.wav + final_mix.wav
python3 -I assets/audio/build_manifest.py   # (from assets/audio/) rebuild VO.md
```

The music and SFX scripts use the same cue words as `scene.js` (act boundaries at S18 empty city and S29 Zuri's room). **Re-run them after any shot re-timing.** ElevenLabs SFX need `duration_seconds` and `loop` set, or they come out 1–2s long.

## Common jobs

- **Look at frames:** `npx --yes hyperframes@0.8.183 snapshot --at <times> --describe false -o <scratchpad>/ep01`, picking times from `CUTS`.
- **Fix a shot:** find it by id (`S05`…`S33`) in `scene.js`, edit its build or update, and keep it seek-safe.
- **Re-render:** `npx --yes hyperframes@0.8.183 check`, then `npx --yes hyperframes@0.8.183 render` in the background. Copy the newest `renders/*.mp4` over `whatif/renders/whatif-ep01-final.mp4`, then check 1920×1080, 30fps, 5:23 and the loudness.
- **Thumbnail:** `thumbnail.html` (Theo close-up, huge awake eyes, clock at 3:07, "NEVER SLEPT.", pink "DAY 400" pill). It needs a local http server because of the module imports. Screenshot it at 1280×720 with HyperFrames' headless shell (`~/.cache/hyperframes/chrome/chrome-headless-shell/...`; the Playwright Chromium here is broken). See `research/style-mockups/render.sh`.
- **Captions:** `captions-en.srt` comes from the voice-track word timings. Spanish lines carry an English translation.
- **Shorts from it:** see `oneif-short-s02-400-days`, `oneif-short-s03-taco-test` and `oneif-short-s04-never-sleep-science`. They reuse this episode's VO clips and music cues with 0 new credits.
- **A sequel or new episode:** follow ep02's path. Write about 1,000 words to clear 8 minutes, and get the script and animatic approved before the final pass.
