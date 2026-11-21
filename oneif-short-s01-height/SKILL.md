---
name: oneif-short-s01-height
description: One If Short 01, "What If Your Height Doubled Every Year?" (56.6s vertical Bold Toon, standalone story, own narration). Use to re-render, re-time, fix or re-caption it, or to turn it into a full episode or reuse its growing-giant scenes (street pull-back, 4th-floor window face, above the clouds, square-cube cards).
---

# One If Short 01: "What If Your Height Doubled Every Year?"

- **Project:** `whatif/shorts/s01-height/` (HyperFrames 0.8.183, SVG, 1080×1920, 30fps, 56.6s)
- **Delivered:** `whatif/renders/shorts/one-if-short-01-height-doubles.mp4` (−14 LUFS, captions burned in)
- **Posting:** `whatif/shorts/POSTING.md` §01 (title, caption, pinned comment, facts). Post it in slot +2 days after the ep01 launch. There's no episode for it yet, so it's a candidate premise for a full film if it does well.
- **Style:** Bold Toon (`whatif/kit/STYLE.md`). Not the 13learns brand. No vidIQ.

## What happens

A standalone story with its own narration (one clip, `assets/audio/vo/height.mp3`, 943 credits; Whisper word times are in `assets/audio/words/`). Theo's height doubles every year:
- **A.** Street: the hook, then years 1–3. Theo grows and the camera pulls back.
- **B.** Year 4: a giant face at a 4th-floor window, and someone waves back.
- **C.** Year 5: heart to brain, three stories up.
- **D.** Year 6: above the clouds.
- **E.** The problem cards: ×2 height / ×8 weight / ×4 bone strength (the square-cube law).
- **F.** The legs give way (reuses the year-6 scene from "By year six").
- **G.** The real record: Robert Wadlow, 2.72 m.
- **H.** Ending: back to normal, and a question for the viewer ("Comment your year").

## How it's built

Unlike s02–s04, this one is hand-built rather than run through `runShort`. `scene.js` (222 lines) has its own `renderAt(t)`, section by section (A–H as above), with captions and fades on top.
- Cues are words, not seconds: `W(word, nth)` looks up the narration's word times. `Y[1..6]` = each "year", plus `PROB`, `LEGS`, `REC`, `END`.
- It uses `kit/vertical.js` (`verticalWrap`, `makeCaptions`, `hookTitle`, `VW/VH/FILL`) and `buildStreet` from `kit/sets.js`.
- `timeline.js` is generated, so never hand-edit it.

## Audio

`audio.json` lists the narration clip, three ep01 score cues (`cue1_wonder` at 0, `cue2_offer` at 36.2, `cue3_keepwatch` at 47.6, trimmed with `from`/`to`), and SFX from `sfx-library/` (whooshes and pops on the beats). Rebuild from the Short's folder:

```bash
python3 -I ../../kit/build_short_audio.py   # -> assets/audio/mix.wav (-14 LUFS) + timeline.js
```

## Common jobs

- **Re-render:** run `npx --yes hyperframes@0.8.183 check`, then `render` in the background. Copy the newest `renders/*.mp4` over `whatif/renders/shorts/one-if-short-01-height-doubles.mp4`. Check 1080×1920, 30fps, 56.6s and −14 LUFS.
- **Kit changes:** `bash whatif/sync-kit.sh whatif/shorts/s01-height` (from the project root).
- **Fact changes:** keep the numbers in `POSTING.md` and the on-screen cards in step.
- **Make it an episode:** write a script in ep01's structure (`WHATIFVERSE-BREAKDOWN.md` §3.3) and get it approved before any voice credits are spent.
