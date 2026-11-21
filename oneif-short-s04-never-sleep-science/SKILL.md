---
name: oneif-short-s04-never-sleep-science
description: One If Short 04, "Could a Human Never Sleep?" (35.6s vertical fact Short from episode 1's science check: the 11-day record, DEC2 gene, dolphins, frigatebirds). Use to re-render, re-time or fix facts and captions on it, or to reuse its sciCards fact-card scene for another science Short.
---

# One If Short 04: "Could a Human Never Sleep?"

- **Project:** `whatif/shorts/s04-never-sleep-science/` (HyperFrames 0.8.183, SVG, 1080×1920, 30fps, 35.6s)
- **Delivered:** `whatif/renders/shorts/one-if-short-04-never-sleep-science.mp4` (−14 LUFS, captions burned in)
- **Posting:** `whatif/shorts/POSTING.md` §04. It goes out in slot +7 days, with **Related video** set to ep01. It has a long shelf life in search.
- **Facts (keep the cards true):** Randy Gardner, 264 hours (1964); the DEC2 short-sleep gene (He et al., *Science* 2009); unihemispheric sleep in dolphins; frigatebirds sleep in flight (Rattenborg et al., 2016).
- **Source:** an ep01 cutdown with 0 new credits: `n12_science` split into two trims (`n12a`, `n12b`) around a trim of `n05_day400` (`n05r`, from 16.75 to 25.95).

## What happens

There's no hook title. The `sciCards` scene opens with "COULD A HUMAN / NEVER SLEEP?", then each card lands on a spoken word:
1. ZERO SLEEP? NOT POSSIBLE ("nobody")
2. THE RECORD (record card)
3. SOME PEOPLE NEED LESS ("but")
4. DEC2 GENE ≈ 6 HOURS A NIGHT ("dec2")
5. DOLPHINS: HALF A BRAIN AT A TIME ("dolphins")
6. FRIGATEBIRDS NAP WHILE FLYING ("frigate")

Then Theo on the rooftop (he winks on "shift"), and the end card "WOULD YOU / GIVE UP SLEEP?" with the chip "FULL FILM ON OUR CHANNEL".

## How it's built

`scene.js` is 23 lines on the shared Shorts framework (`runShort` from `kit/vshort.js`; see `oneif-short-s02-400-days`). `W(id, word)` finds a word's time inside a clip. `sciCards` takes `[time, kind, "LINE 1|LINE 2"]` entries, where kind is one of `big`, `record`, `dna`, `dolphin` or `bird`, and it can be reused for any fact Short.

## Audio

```bash
python3 -I ../../kit/build_short_audio.py   # audio.json -> assets/audio/mix.wav (-14 LUFS) + timeline.js
```

## Common jobs

- **Re-render:** run `npx --yes hyperframes@0.8.183 check`, then `render` in the background. Copy the newest `renders/*.mp4` over `whatif/renders/shorts/one-if-short-04-never-sleep-science.mp4`. Check 35.6s and −14 LUFS.
- **New fact card:** add a kind in `kit/vscenes.js` `sciCards`, run `sync-kit.sh`, and cue it on a word.
