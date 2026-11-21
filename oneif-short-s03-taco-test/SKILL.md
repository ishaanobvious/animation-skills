---
name: oneif-short-s03-taco-test
description: One If Short 03, "Learn Spanish in 75 Nights?" (22.2s vertical cutdown of episode 1: flashcards, then the taco-restaurant test with the waiter). Use to re-render, re-time or re-caption it, or to reuse its flashcards and restaurant vertical scenes.
---

# One If Short 03: "Learn Spanish in 75 Nights?"

- **Project:** `whatif/shorts/s03-taco-test/` (HyperFrames 0.8.183, SVG, 1080×1920, 30fps, 22.2s)
- **Delivered:** `whatif/renders/shorts/one-if-short-03-taco-test.mp4` (−14 LUFS, captions burned in)
- **Posting:** `whatif/shorts/POSTING.md` §03. It goes out in slot +4 days, with **Related video** set to ep01. Fact: the FSI rates Spanish at about 600–750 class hours (600 hours = 75 nights with no sleep).
- **Source:** an ep01 cutdown with 0 new credits. The narrator clip `n04_spanish` is trimmed with `from: 7.82, to: 19.12`, followed by Theo's Spanish (`d03`) and the waiter (`d04`, voice Eduardo).

## What happens

The hook title "LEARN SPANISH / IN 75 NIGHTS?" shows for 2.4s. Then the `flashcards` scene, where the chips "600 HOURS" and "= 75 NIGHTS" (pink) pop on those spoken words, and the `restaurant` scene: Theo orders in fluent Spanish ("Two al pastor tacos, please…") and the waiter asks "...Are you from here?". Word-pop captions run only over the narration (`captionClips: ["n04"]`); the Spanish dialogue gets English subtitles from the `subs` option instead. End card: "WHAT WOULD / YOU LEARN?" with the chip "TELL US BELOW".

## How it's built

`scene.js` is 16 lines on the shared Shorts framework: `runShort` from `kit/vshort.js`, plus the `flashcards`, `restaurant({theo, waiter, subs})` and `endCard` builders from `kit/vscenes.js`. The `oneif-short-s02-400-days` skill explains the framework. Scene starts are keyed off clip starts in the generated `timeline.js`.

## Audio

```bash
python3 -I ../../kit/build_short_audio.py   # audio.json -> assets/audio/mix.wav (-14 LUFS) + timeline.js
```

## Common jobs

- **Re-render:** run `npx --yes hyperframes@0.8.183 check`, then `render` in the background. Copy the newest `renders/*.mp4` over `whatif/renders/shorts/one-if-short-03-taco-test.mp4`. Check 22.2s and −14 LUFS.
- **Subtitles under the Spanish:** they're set in the `subs` option of the restaurant scene. Keep them in step with ep01's captions.
- **Kit changes:** `bash whatif/sync-kit.sh whatif/shorts/s03-taco-test`.
