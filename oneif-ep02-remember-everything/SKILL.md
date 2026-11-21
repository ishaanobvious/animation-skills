---
name: oneif-ep02-remember-everything
description: One If episode 2, "What If You Remembered 100% of Your Life?" (8:11 Bold Toon SVG film, 1920×1080, Jay + Dev). Use to re-render, re-time, fix shots, sound or captions on it, cut Shorts from it, or reuse its memory-wall, library, bus and diner builders and the audio/caption pipeline for a new episode.
---

# One If ep02: "What If You Remembered 100% of Your Life?"

- **Project:** `whatif/episodes/ep02-remember-everything/` (HyperFrames 0.8.183, SVG + GSAP, 1920×1080, 30fps, `DUR` 491.28s)
- **Delivered:** `whatif/renders/whatif-ep02-final.mp4` (with music), `whatif-ep02-thumbnail.png`, `whatif-ep02-captions-en.srt`. The approved animatic is in the project's `renders/ep02-animatic.mp4`.
- **Upload sheet:** `UPLOAD.md`. **Script:** `SCRIPT.md` (premise #5 from `WHATIFVERSE-BREAKDOWN.md`, cast, fact check, build list)
- **Style:** Bold Toon, `whatif/kit/STYLE.md`. Not the 13learns brand. Borrow only the system from Ifverse. No vidIQ.

## The story

Jay remembers every second of his life. It opens on the school bus, with Dev testing him on something said a year ago. Then comes the rule, with the forgetting curve versus a flat YOU line, and how memory works: a library run by a seahorse librarian (the hippocampus) who stops saying no. Next is the ladder: the upside-down textbook, the A+, Mom's party line, eight trivia wins and a lifetime ban, then the stolen bikes, where his plate memory (KDR 4471) closes six cases for Officer Reyes. Dr. Sato notices him. The cost: seventh-grade cringe replays, a mall of screens and the cafeteria, where he corrects Dev word for word and Dev walks off. The choice: Sato's forgetting headband, and a warm third-grade flashback of Dev sharing half a sandwich. In the resolution on Dev's porch at dusk, he remembers everything and forgives anyway, and the headband goes in a drawer. Sequel hook: a stranger in a red scarf he can't remember (NO MATCH, PART 2). Then the science check (Jill Price, HSAM, Shereshevsky) and the call to action.

Voices (`eleven_v4`, 37 takes, 6,829 credits, flow "What If - Ep02 Remember Everything - voices"): the hero rig and voice (Louie the Legend) are reused as Jay. Dev is Kai, Mom is reused from ep01, and the new voices are host Albert B. Squid, Reyes Anya, Dr. Sato Jeanne and the stranger Andrea. The manifest is in `assets/audio/VO.md`, and `takes.tsv` maps each file to its generation id.

## How it's built

Same engine as ep01 (see `oneif-ep01-never-sleep` for the details): generated `timeline.js`, `shot(...)` registration, `C`/`E`/`W(clip, word)` cues, `CUTS` / `CARD_CUTS` coverage, and `ANIMATIC = false` for the final.

Builders added for this episode, all in `scene.js` and all reusable:
- `memoryWall(root, seed, {bg, fw, fh})`: endless film frames that blur, freeze and fly (title card, cost, hook, thumbnail)
- `library(root, seed)` + `seahorse(parent)`: the brain-explainer set
- `busScenery(r, t)`: the cold-open bus interior
- `headband(parent)`, `sandwichHalf(parent)`, `filmBorder(parent)`, `blurFilter(parent)`, `icon(g, kind)`
- `rooms.js`: this episode's sets (bus, diner, police station, mall, cafeteria + flashback, porch). The ep01 sets are re-dressed.

## Audio and captions (run from the episode folder, in this order)

```bash
python3 -I assets/audio/build_timeline.py   # voice clips -> timeline.js + mix.wav
python3 -I assets/audio/build_music.py      # reuses ep01's 3 ElevenLabs cues, cut by mood (0 credits) -> music.wav
python3 -I assets/audio/build_sfx.py        # ep01 ambience loops + sfx-library one-shots, ducked -> sfx.wav + final_mix.wav
python3 -I assets/audio/build_captions.py   # word timings with Whisper mishearings fixed against the script -> captions-en.srt
```

Dialogue-heavy stretches (lockers and cafeteria, Sato's offer, the porch) have no music on purpose. Re-run music and SFX after any shot re-timing, because they key off the same cue words.

## Common jobs

- **Re-render:** run `check`, then `render` with `hyperframes@0.8.183` in the background. Copy the newest `renders/*.mp4` over `whatif/renders/whatif-ep02-final.mp4`, and check 1920×1080, 30fps, 8:11, a single audio track.
- **Thumbnail:** `thumbnail.html` (it imports `kit/rig.js`). Serve it over local http and screenshot it at 1280×720 with HyperFrames' chrome-headless-shell (see `research/style-mockups/render.sh`).
- **Shorts:** use the `kit/vscenes.js` + `kit/vshort.js` framework (see `oneif-short-s02-400-days`). VO clips can be trimmed with `from`/`to` in `audio.json`.
