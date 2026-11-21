---
name: jh-bamboo
description: "13learns Job haters video \"The Bamboo\" (\"Year 4. Still nothing.\"). Two planters, two watering cans, both pouring at 0.0s under one big YEAR counter. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makePlanter, drawGreyPlant, makeCulm, drawBamboo)."
---

# The Bamboo: "Year 4. Still nothing." (13learns Job haters)

- **Project:** `videos/the-bamboo/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-8.md` §2
- **Delivered:** `renders/13learns-bamboo.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Bamboo: two planters, two watering cans, both pouring at 0.0s under one big YEAR counter. Grey's planter sprouts at once and stops at knee height; blue's stays bare soil through year 4. Grey glances over and shrugs. A scan line turns the planters see-through: grey's plant has a small tuft of roots, blue's planter is packed with them. At year 5 blue's bamboo shoots up, segment by segment. Blue takes a cutting, walks over and plants it in grey's planter, and grey waters it.

## The script (as written)

**Pattern used:** a fable everyone knows (#7, the bamboo that grows roots for years first), X-ray of the hidden progress (#33), one shared counter (#32)
**Frame line (top):** YEAR 4. STILL NOTHING. (line 2 at the payoff, in blue: THE ROOTS WERE THE WORK.)
**Labels:** left: Quick results · right: Deep roots
**Counter:** a big "YEAR 1 → 5" in the middle. Chips: "Fast start" on grey's plant; during the scan, "Shallow" (dark) on grey and "4 years of roots" (blue) on blue
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.2s | Hook: both watering | Two planters, two watering cans, both pouring at 0.0s. Grey's planter sprouts at once and reaches knee height in a year. Blue's is still bare soil. | YEAR 4. STILL NOTHING. · YEAR 1 → 3 · Fast start | water trickle, a soft pop as grey's sprouts |
| 3.2–5.2s | Year 4 | Grey's plant hasn't grown since year 1. He glances over at blue's bare planter and shrugs. Blue keeps watering. | YEAR 4 | trickle, tick per year |
| 5.2–6.9s | The scan | A blue scan line sweeps down and the planters turn see-through. Grey's plant has a small tuft of roots. Blue's planter is packed with a blue root network. | Shallow / 4 years of roots | scan sweep, hum, root creaks |
| 6.9–8.3s | Year 5 | The counter turns blue at YEAR 5 and blue's bamboo shoots up, segment by segment, and its leaves pop. Blue steps back and looks up. | YEAR 5 | rising whoosh, node clicks, leaf pops |
| 8.3–12s | Kind payoff | Blue takes a cutting from the base, walks over and plants it in grey's planter. Grey waters it with him. Line 2 types in. Dip, loop. | YEAR 4. STILL NOTHING. / THE ROOTS WERE THE WORK. | steps, soil pat, trickle, typing, sparkle |

**Post caption:** For four years it looks like nothing is happening. Then it grows faster than anything around it, because it spent those years underground. The work you can't show yet is the root system. Which year are you in?
**Loop point:** both watering in year 1.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Year 4. Still nothing."
- Label `#lbl-emp` (`index.html`): "Quick results"
- Label `#lbl-own` (`index.html`): "Deep roots"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#gfast` "Fast start" (light), `#gshal` "Shallow" (dark negative), `#broots` "4 years of roots" (blue)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "The roots were the work."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const G_X = -2.3;
const B_X = 2.3;
const G_POT = -1.25;
const B_POT = 1.25;
const POT_W = 1.1;
const POT_H = 0.75;
const POT_D = 0.7;
const SOIL_Y = FLOOR_Y + POT_H - 0.05;
const YEARS = [[0, 1], [1.6, 2], [3.2, 3], [4.8, 4], [7.0, 5]];
const G_SPROUT = [0.0, 1.2];
const G_GLANCE = [3.1, 4.0];
const G_STOP_WATER = 5.0;
const SCAN = [5.2, 5.9];
const XRAY_OFF = [7.7, 8.1];
const GROW = [7.0, 8.3];
const B_STEP_BACK = [6.95, 7.35];
const B_TAKE = [8.25, 8.65];
const B_WALK = [8.7, 9.8];
const B_PLANT = [9.8, 10.3];
const G_WATER2 = [10.3, 11.6];
const COUNT_FADE = 8.4;
const TYPE_LINE_AT = 10.2;
const G_LEAVES = [[0.13, 0.42, 0.04, 0.6], [-0.12, 0.5, -0.03, 2.5], [0.1, 0.62, -0.05, 0.9], [-0.07, 0.68, 0.06, 2.2]];
const WATER = { ...STAND, lean: 0.12, head: -0.25, shL: 0.1, elL: 0.2, shR: 1.15, elR: 0.35 };
const HOLD = { ...STAND, head: -0.05, shR: 0.55, elR: 0.6 };
const SHRUG = { ...STAND, head: 0.1, shL: 0.35, elL: 1.5, shR: 0.4, elR: 1.45, ab: 0.55 };
const LOOK_UP = { ...STAND, lean: -0.12, head: 0.55, shL: 0.1, elL: 0.3, shR: 0.1, elR: 0.3 };
const REACH = { ...STAND, lean: 0.35, head: -0.2, shR: 1.3, elR: 0.25, shL: 0.2, elL: 0.3 };
const PLANT = { ...CROUCH, shR: 0.75, elR: 0.25, shL: 0.5, elL: 0.4 };
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · planters · roots (inside the planters; only seen in the scan) · grey's quick plant · blue's bamboo: two culms with node rings and leaves · the cutting: in blue's hand, then planted in grey's planter · watering cans · scan line · figures · HTML · frame.

Functions:
- `makePlanter(x, mat)`: planters
- `rootSeg(a, b, r, mat)`
- `growRoots(cx, count, maxDepth, spread, mat, seed, r)`
- `drawGreyPlant(t)`
- `makeCulm(x, z, r, height, seed)`: blue's bamboo: two culms with node rings and leaves
- `drawBamboo(t)`
- `makeCan()`: watering cans
- `drawCan(can, hand, yaw, tilt, pourOn, t, seed)`
- `drawScan(t)`
- `xray(t)`
- `drawRoots(t)`
- `poseGrey(t)`
- `poseBlue(t)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Bamboo as one premixed, motion-synced track. Timing mirrors scene.js: two watering cans trickling (grey left, blue right), soft pops as grey's plant leafs out, a tick on each new year, grey's shrug, the scan sweep with a low hum and faint root creaks, then year 5: a hit, a rising swell and a click per node as the bamboo shoots up with leaf pops. Blue's steps over, the cutting patted into the soil, grey watering it, line 2 and a sparkle. Owned synths and ../../sfx-library sounds only: nothing needs attribution.

Owned synths: `SR`, `air_whoosh`, `counter_blip`, `floor_step`, `metal_creak`, `rung_tick`, `soft_thud`, `water_trickle`.
`sfx-library/` sounds: `click-soft`, `impact-bass-1`, `ping`, `pop`, `riser`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-short`.

Rebuild: `cd videos/the-bamboo && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-bamboo/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/bamboo
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-bamboo && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-bamboo   # run in the background
```
`render.sh` writes `renders/13learns-bamboo.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
