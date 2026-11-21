---
name: jh-gap
description: "13learns Job haters video \"The Gap\" (\"It never gets smaller.\"). Both figures start on the \"Job\" cliff. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeCliff, drawCliffs, drawHut, drawPlank)."
---

# The Gap: "It never gets smaller." (13learns Job haters)

- **Project:** `videos/the-gap/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-2.md` §6
- **Delivered:** `renders/Posted/13learns-the-gap.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Gap: both figures start on the "Job" cliff. Blue jumps the small gap and starts building; grey stays, an excuse pops up each year and the cliffs grind further apart. When grey finally runs for it the gap is huge. Blue drops a plank across and holds his end.

## The script (as written)

**Pattern used:** the doer jumps while the overthinker waits on the edge (39.9M), told as quitting to start something
**Frame line (top):** THE GAP NEVER GETS SMALLER.
**Labels:** Waiting / Started
**Small ticker under grey:** Year 1 → 8
**Props:** two cliffs with a gap between them. The left cliff is "Job" and the right cliff glows faintly blue ("Your thing"). Excuse signs pop up beside grey: "After my bonus", "When I have savings", "Bad economy", "Next year".
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: the edge | Both figures stand at the edge of "Job". Blue backs up two steps, runs and jumps the gap, landing on one knee. Grey peers over. | THE GAP NEVER GETS SMALLER. · Year 1 | run footsteps, jump whoosh, landing thud |
| 2.0–6.0s | Excuses | An excuse sign pops up beside grey each beat. Each time, the cliffs drift apart and the gap widens. Across the gap, blue builds a small hut, then a bigger one. | "After my bonus" · "When I have savings" · "Bad economy" · "Next year" · Year 2 → 6 | sign pop per beat, rock grind as the gap widens |
| 6.0–8.0s | The turn | Grey finally backs up to jump. The gap is now enormous and he skids to a stop at the edge. | Year 7 | skid scrape |
| 8.0–12s | Kind payoff | Blue throws a plank across the gap and holds his end. "It's still not too late" appears small under the top line. Grey looks at the plank. Dip, loop. | Year 8 · "It's still not too late" | plank clunk, sparkle |

**Post caption:** "When the time is right" is the only deadline that keeps moving away from you.
**Loop point:** cliffs close together, both figures on the "Job" edge.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "The gap nevergets smaller."
- Label `#lbl-emp` (`index.html`): "Waiting"
- Label `#lbl-own` (`index.html`): "Started"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const BACK_UP = [0.0, 0.5]; // blue backs up two steps
const RUN = [0.5, 1.0];
const JUMP = [1.0, 1.45];
const KNEEL_END = 1.85;
const UP_END = 2.15;
const TO_HUT = [2.15, 2.45];
const HAMMER = [2.45, 5.75];
const EXCUSES = [
const DRIFT = [0.25, 0.25, 0.3, 0.3]; // each excuse pushes each cliff this far out
const DRIFT_DUR = 0.45;
const G_BACK = [6.0, 6.6]; // grey finally backs up
const G_RUN = [6.6, 7.25];
const G_SKID = [7.25, 7.6];
const PLANK_UP = 7.9;
const PLANK_FALL = [8.15, 8.6];
const LATE_AT = 8.75;
const G_LOOK_UP = 10.4;
const G_STEP = [10.9, 11.5];
const EDGE0 = 0.3; // half the starting gap
const EL = (t) => -EDGE0 - edgeShift(t); // left cliff's edge x
const ER = (t) => EDGE0 + edgeShift(t); // right cliff's edge x
const CLIFF_W = 8;
const CLIFF_H = 7;
const CLIFF_Z0 = -1.6;
const CLIFF_Z1 = 1.0;
const STRIKES = [2.6, 2.9, 3.2, 3.5, 3.8, 4.4, 4.7, 5.0, 5.3, 5.6];
const HUT_PARTS = [
const PLANK_L = finalGap + 0.3;
const G_Z = 0.35;
const B_Z = -0.25;
const HOLD = { ...KNEEL, lean: 0.45, head: -0.25, shL: 0.95, elL: 0.25, shR: 0.95, elR: 0.25 };
const SHRUG = { ...STAND, head: 0.12, shL: 0.25, elL: 1.35, shR: 0.25, elR: 1.35, ab: 0.4, eab: -0.35 };
const LOOK_DOWN = { ...STAND, lean: 0.2, head: 0.5, shL: 0.05, elL: 0.1, shR: 0.02, elR: 0.1 };
const HAMMER_UP = { ...STAND, lean: 0.2, head: 0.25, thL: 0.2, knL: -0.25, thR: -0.15, knR: -0.1, shL: 0.9, elL: 0.5, shR: 2.5, elR: 0.6 };
const HAMMER_DOWN = { ...HAMMER_UP, lean: 0.32, shR: 1.15, elR: 0.15 };
const STEP = 0.5;
const YEARS = [[0, 1], [2.3, 2], [3.2, 3], [4.1, 4], [5.0, 5], [5.6, 6], [G_BACK[0], 7], [PLANK_FALL[1], 8, true]];
```

## How `scene.js` is built

Sections, in order: story beats · the cliffs · blue's hut, built one strike at a time · the plank: stands up at blue's edge, then falls across like a drawbridge · figures · HTML: year ticker, excuse chips, labels · frame.

Functions:
- `edgeShift(t)`
- `makeCliff(top, edgeColor, emissive)`
- `makeGlow(size, color)`
- `drawCliffs(t)`
- `roof(w, h, d, mat)`
- `drawHut(t)`
- `drawPlank(t)`
- `poseBlue(t)`
- `poseGrey(t)`
- `drawYear(t)`
- `drawChips(t)`
- `placeTagAt(id, x, dy)`
- `drawTags(t)`
- `drawLate(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Gap as one premixed, motion-synced track. Timing mirrors scene.js (back-up, run, jump, landing, excuse chips + cliff grind, hammer strikes, grey's run and skid, the plank drawbridge, the step), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `floor_step`, `pipe_clunk`, `quake_rumble`, `soft_thud`, `stone_crackle`.
`sfx-library/` sounds: `chime`, `click-soft`, `ping`, `pop`, `sparkle`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-gap && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-gap/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/gap
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-gap && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-gap   # run in the background
```
`render.sh` writes `renders/13learns-gap.mp4`. The file already delivered is `renders/Posted/13learns-the-gap.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
