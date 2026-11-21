---
name: jh-pipeline
description: "13learns Job haters video \"The Pipeline\" (\"Employees carry buckets. Owners build pipelines.\"). Grey hauls buckets one at a time; blue builds a pipe once and lets it flow. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeTank, makeStream, drawFlow, drawPieces)."
---

# The Pipeline: "Employees carry buckets. Owners build pipelines." (13learns Job haters)

- **Project:** `videos/the-pipeline/` (HyperFrames 0.8.181 + Three.js, 1080×1920, 30fps, 10s, seamless loop, no VO)
- **Script:** `SCRIPTS.md` §1
- **Delivered:** `renders/Posted/13learns-the-pipeline.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Pipeline: grey hauls buckets one at a time; blue builds a pipe once and lets it flow.

## The script (as written)

**On-screen counter:** Year 1 → 10
**Props:** a shared water reservoir in the middle, a small glass tank on the left (grey's), a big glass tank on the right (blue's), a pipe blue builds between them.

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.5s | Hook: the grind | Grey fills a bucket at the reservoir tap, carries it left, pours it into his tank: one bucket at a time, his tank inches up. Blue isn't carrying anything: he's bolting pipe sections together, one per beat, from the reservoir towards his empty tank. Grey looks like he's winning. | Year 1, 2, 3, 4 | tap trickle, footsteps, splash per pour, metal clunk per pipe |
| 3.5–5.0s | The turn | Blue fits the last elbow, turns the valve: water gushes into his tank. "Year 5" flashes blue; "Owner" pops in. | Year 5 (blue) | valve squeak, gush |
| 5.0–8.5s | Two paths | Blue steps back and does nothing; his tank fills on its own. Grey keeps hauling, slower, hunched, fading to grey; his tank barely moves. | Year 6 → 9 | steady flow, slower footsteps |
| 8.5–10s | Payoff | Year 10: grey drops the bucket and sits. Blue's tank is full and glowing; hands on hips, shades on. Dip, loop. | Year 10 (blue) | bucket clatter, sparkle |

**Post caption:** You can carry buckets for 40 years, or spend 4 building the pipe. 🪣 → 🚰
**Loop point:** grey back at the tap with an empty tank; blue at the first pipe section.

## On-screen text (where it lives)

- Label `#lbl-emp` (`index.html`): "Employee"
- Label `#lbl-own` (`index.html`): "Owner"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const SRC = { x: -1.0, r: 0.58, h: 3.3 }; // shared reservoir
const GT = { x: -3.95, r: 0.45, h: 1.35 }; // grey's tank
const BT = { x: 3.2, r: 0.78, h: 2.05 }; // blue's tank
const PIPE_Y = 0.25;
const PIPE_Z = -0.45;
const PIPE_R = 0.1;
const PIPE_X0 = SRC.x + SRC.r;
const SEGS = 6;
const SEG_LEN = (BT.x - PIPE_X0) / SEGS;
const VALVE_X = 1.75;
const GREY_Z = 0;
const BLUE_Z = 0.35;
const SEG_AT = (k) => 0.35 + 0.52 * k;
const SPOUT_AT = 3.3;
const SPOUT_BOTTOM = PIPE_Y - 0.44;
const VALVE_AT = 2.95;
const FILLP = { ...STAND, lean: 0.12, head: -0.2, shR: 0.55, elR: 0.1, shL: -0.1 };
const CARRY = { ...STAND, lean: -0.04, shR: 0.02, elR: 0.02, shL: -0.25, elL: 0.2 };
const POURP = { ...STAND, lean: 0.1, head: -0.15, shR: 2.0, elR: 0.2, shL: 1.35, elL: 0.6 };
const FILL_X = SRC.x - SRC.r - 0.82;
const TAP_X = FILL_X + handOffset(FILLP, 0);
const POUR_X = GT.x - handOffset(POURP, Math.PI);
const TAP_Y = -0.62;
const BS = 1.35; // bucket scale, so it reads on a phone
const T_STOP = 8.45;
const POUR_GAIN = 0.14;
const STOPS = [];
const FLOW_AT = 4.5;
const REST_X = 1.45;
const YEARS = [[0, 1], [0.9, 2], [1.8, 3], [2.7, 4], [3.6, 5], [FLOW_AT, 5, true], [5.4, 6], [6.2, 7], [7.0, 8], [7.8, 9], [8.6, 10, true]];
```

## How `scene.js` is built

Sections, in order: layout · tanks · pipe (blue builds it) · streams · figures · grey's bucket trips · blue: builds the pipe, opens the valve, then lets it run · blue tank fill + flow · counter · frame.

Functions:
- `makeTank({ x, r, h }, level0 = 0)`: tanks
- `makeStream(r)`
- `setStream(m, x, yTop, yBot, z, on)`
- `handOffset(pose, yaw)`
- `setBucketWater(f)`
- `tripAt(t)`
- `greyTank(t)`
- `greyTrip(u, t, tired)`: grey's pose + bucket for trip phase u
- `poseGrey(t)`
- `poseBlue(t)`
- `drawFlow(t)`
- `drawPieces(t)`
- `drawCount(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Pipeline as one premixed, motion-synced track. Timing mirrors scene.js (grey's bucket trips, blue's pipe stops, valve, flow), so steps, pours and clunks land on the frame they happen. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `bucket_clatter`, `coin_clink`, `floor_step`, `pipe_clunk`, `soft_thud`, `valve_squeak`, `water_flow`, `water_pour`, `water_splash`, `water_trickle`.
`sfx-library/` sounds: `click-soft`, `ping`, `pop`, `sparkle`, `whoosh-air-02`.

Rebuild: `cd videos/the-pipeline && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-pipeline/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.181 snapshot --at 0.4,2,4,6,8,9.6 --no-end --describe false -o <scratchpad>/pipeline
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-pipeline && npx --yes hyperframes@0.8.181 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-pipeline   # run in the background
```
`render.sh` writes `renders/13learns-pipeline.mp4`. The file already delivered is `renders/Posted/13learns-the-pipeline.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
