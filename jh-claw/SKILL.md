---
name: jh-claw
description: "13learns Job haters video \"The Claw\" (\"Waiting to be picked.\"). A glass claw machine full of small figures waiting, arms up, to be picked for promotion. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawClaw, drawDoor, drawMachine, drawHtml)."
---

# The Claw: "Waiting to be picked." (13learns Job haters)

- **Project:** `videos/the-claw/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-4.md` §1
- **Delivered:** `renders/13learns-the-claw.mp4` (rendered)
- **Old A/B file:** `renders/13learns-the-claw-alt.mp4`. It predates the one-version rule. Don't make new `-alt` renders.
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Claw: a glass claw machine full of small figures waiting, arms up, to be picked for promotion. The claw drops empty, drops empty, lifts one and lets him slip, then finally drops one down the chute. The pale blue figure at the front stops waiting, goes down the chute himself, pushes the prize flap open from the inside and holds it open for the next one.

## The script (as written)

**Pattern used:** waiting to be rescued (chain reel, 3.2M and reposted); the elimination-style counter
**Frame line (top):** WAITING TO BE PICKED. (line 2 at the payoff, in blue: OR PICK YOURSELF.)
**A/B line 2:** NOBODY'S COMING FOR THE CLAW.
**Labels:** none on the crowd; one small label "PROMOTION" on the claw
**Ticker:** Year 1 → 8 · "Picked: 1 of 40"
**Props:** a big glass claw machine; inside, ~40 identical grey figures stand in the prize pit, arms up; a steel claw on a gantry; the prize chute in the front corner with a swing flap
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.5s | Hook: the claw drops | The claw is already falling at 0.0s. Every figure in the pit raises both arms. It closes on nobody and rises empty. The arms drop. | WAITING TO BE PICKED. · Year 1 | gantry whir, claw clack, a sigh-whoosh as the arms drop |
| 2.5–5.5s | The years | Year ticks 2 → 6. The claw drops twice more. Once it lifts a figure halfway and lets him slip back into the pit. One blue-edged figure at the front stops raising his arms and looks at the chute. | Year 2 → 6 · "Picked: 0 of 40" | whir, clack, slip-thud, ticks |
| 5.5–7.0s | The pick | Year 7: the claw finally grabs one figure and drops him down the chute. A "PROMOTED" chip pops. The other 39 cheer, then raise their arms again. | Year 7 · PROMOTED · "Picked: 1 of 40" | clack, chute whoosh, ping, small cheer |
| 7.0–9.5s | Pick yourself | The blue figure walks to the chute, pushes the flap from the inside and climbs out on his own. Outside he turns fully blue and a small blue sign lights over a door beside the machine: his own name. | Year 8 (blue) | flap creak, steps, pop, chime |
| 9.5–12s | Kind payoff | Blue holds the flap open from the outside. One grey figure lowers his arms and crawls toward it. Line 2 types in. Dip, loop. | WAITING TO BE PICKED. / OR PICK YOURSELF. | typing, sparkle |

**Post caption:** A promotion is someone else deciding you're ready. You can decide that yourself. How many years have you been waiting under the claw?
**Loop point:** the claw starting its drop, every arm going up.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Waiting to be picked."
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#promo` "PROMOTION" (light), `#promoted` "PROMOTED" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Or pick yourself."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const S = 0.5; // the figures are the prizes, so they're half size
const CX = -0.6;
const CW = 3.2;
const CD = 1.7;
const BASE_H = 1.0;
const PIT_Y = FLOOR_Y + BASE_H;
const GLASS_H = 3.0;
const TOP_Y = PIT_Y + GLASS_H;
const MARQ_H = 0.5;
const FRONT_Z = CD / 2;
const X0 = CX - CW / 2;
const X1 = CX + CW / 2;
const CHUTE = { x0: 0.25, x1: 0.95, z0: 0.1, z1: 0.8, h: 0.35 };
const CHUTE_X = (CHUTE.x0 + CHUTE.x1) / 2;
const CHUTE_Z = (CHUTE.z0 + CHUTE.z1) / 2;
const FLAP = { x: CHUTE_X, w: 0.56, y0: FLOOR_Y + 0.1, h: 0.56 };
const NICHE_D = 0.5;
const DOOR_X = 1.95;
const DOOR_Z = 0.3;
const HUB_TOP = TOP_Y - 0.5;
const SLIP_AT = 4.95;
const DROP_D = 7.2;
const PROMOTED_AT = 7.35;
const CHEER = [7.45, 8.15];
const BLUE_WALK = [7.75, 8.1];
const BLUE_HOP = [8.1, 8.55];
const FLAP_OPEN = [8.55, 8.8];
const BLUE_CRAWL = [8.65, 9.15];
const BLUE_STAND = [9.15, 9.4];
const BLUE_TURN = [9.1, 9.45];
const DOOR_UP = 9.3;
const BLUE_ASIDE = [9.45, 9.8];
const G_LOWER = [9.95, 10.25];
const G_HOP = [10.3, 10.85];
const G_CRAWL = [11.15, 11.9];
const TYPE_LINE_AT = 9.95;
const YEARS = [[0, 1], [2.2, 2], [2.9, 3], [3.6, 4], [4.3, 5], [5.0, 6], [5.7, 7, true], [DOOR_UP, 8, true]];
const FX0 = FLAP.x - FLAP.w / 2;
const FX1 = FLAP.x + FLAP.w / 2;
const FY1 = FLAP.y0 + FLAP.h;
const NZ = FRONT_Z - NICHE_D;
const BLUE_CELL = nearest(0, 0.62);
const G_CELL = nearest(0.64, 0.02);
const SLIP_CELL = nearest(-1.34, 0.02);
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · the machine · the claw · the crowd · claw keyframes: [time, x, z, hub y, open] · poses · his door · HTML · frame.

Functions:
- `slab(x0, x1, y0, y1, z0, z1, mat)`: a box from min to max corners
- `makeGlow(size, color)`
- `place(fig, pose, x, ground, z, yaw, lift = 0)`
- `clawState(t)`
- `drawClaw(t)`
- `curve(keys, t)`
- `waitPose(t, ph, up)`
- `hopIn(t, from, t0, t1)`: a figure going over a chute wall and down into it; returns {x, z, lift}
- `poseCrowd(t, claw)`
- `poseBlue(t)`
- `drawDoor(t)`
- `drawMachine(t)`
- `pin(el, v, opacity, dx = 0, dy = 0)`
- `drawHtml(t, claw)`
- `drawLine2(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Claw as one premixed, motion-synced track. Timing mirrors scene.js (the claw's keyframes, every clack when it closes, the arms going up and dropping, the slip, the pick and the chute, the cheer, blue's walk, drop and crawl out of the flap, his door, and the grey figure who follows), so every sound lands on its frame. Pan follows the claw across the machine. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `SR`, `air_whoosh`, `floor_step`, `metal_creak`, `pipe_clunk`, `soft_thud`, `wheel_rumble`.
`sfx-library/` sounds: `applause-small-01`, `blip-counter-02`, `chime`, `clap-01`, `click`, `click-soft`, `ping`, `pop`, `rumble-wheel-loop`, `sparkle`, `typing`, `whoosh-short`.
It still has an `--alt` flag from the old A/B end line. Leave it off, since the rule is one version only.

Rebuild: `cd videos/the-claw && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-claw/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/claw
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-claw && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-claw   # run in the background
```
`render.sh` writes `renders/13learns-claw.mp4`. The file already delivered is `renders/13learns-the-claw.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
