---
name: oneif-short-s02-400-days
description: One If Short 02, "You Haven't Slept in 400 Days" (31.4s vertical cutdown of episode 1: hook, the oven gag, Vance's offer). Use to re-render, re-time or re-caption it, or as the template for cutting a new vertical Short out of any episode with the runShort/vscenes framework.
---

# One If Short 02: "You Haven't Slept in 400 Days"

- **Project:** `whatif/shorts/s02-400-days/` (HyperFrames 0.8.183, SVG, 1080×1920, 30fps, 31.4s)
- **Delivered:** `whatif/renders/shorts/one-if-short-02-400-days.mp4` (−14 LUFS, captions burned in)
- **Posting:** `whatif/shorts/POSTING.md` §02. It goes out on ep01 launch day, with **Related video** set to ep01.
- **Source:** an ep01 cutdown with 0 new credits. Every voice clip and music cue is read from `../../episodes/ep01-never-sleep/assets/audio/`.

## What happens

The hook title "YOU HAVEN'T SLEPT / IN 400 DAYS" shows for 2.6s. Then:
1. Theo walks the night street (`c01`).
2. He tinkers at his desk: the robot appears, then he stretches (`c02`).
3. The kitchen oven gag with Mom (`d01`, `d02`).
4. Vance's offer in the Lumen office (`d08`).
5. End card: "WOULD YOU / SELL IT?" with the chip "FULL FILM ON OUR CHANNEL".

## How it's built (the reusable Shorts framework)

`scene.js` is 17 lines. It calls `runShort({ CLIPS, DUR, hook, scenes })` from `kit/vshort.js`:
- `scenes` is a list of `[startTime, builder, options]`, with start times taken from clip starts (`C("d01") - 0.15`) so cuts land on the voice.
- The builders come from `kit/vscenes.js`: `streetWalk`, `deskTinker({robotAt, stretchAt})`, `kitchen({mom, theo})`, `office({vance})` and `endCard({at, lines, chipText})`. Also available: `flashcards`, `restaurant`, `rooftop` and `sciCards`. They draw ep01's sets (`kit/rooms.js`) into a vertical frame.
- `runShort` adds word-pop captions (`kit/vertical.js` `makeCaptions`, 3 words max, uppercase), lip sync through `mouthFromEnvelope`, fades and the `hf-seek` hook.

To cut a new Short: copy this folder, rewrite `audio.json` (clips with `at` and an optional `from`/`to` trim, music beds, SFX), rebuild the audio, then list the scenes.

## Audio

```bash
python3 -I ../../kit/build_short_audio.py   # audio.json -> assets/audio/mix.wav (-14 LUFS) + timeline.js
```

## Common jobs

- **Re-render:** run `npx --yes hyperframes@0.8.183 check`, then `render` in the background. Copy the newest `renders/*.mp4` over `whatif/renders/shorts/one-if-short-02-400-days.mp4`. Check 1080×1920, 30fps, 31.4s and −14 LUFS.
- **Kit changes:** `bash whatif/sync-kit.sh whatif/shorts/s02-400-days` (from the project root).
