---
name: jh-pump
description: "13learns Job haters video \"The Pump\" (\"Pump 30. Still dry.\"). Two old hand pumps. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makePump, drawStream, drawScan, drawBucket)."
---

# The Pump: "Pump 30. Still dry." (13learns Job haters)

- **Project:** `videos/the-pump/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-8.md` §1
- **Delivered:** `renders/13learns-pump.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Pump: two old hand pumps. Both figures are already pumping at 0.0s under big "PUMPS" counters. Grey stops at 5, peers at his dry spout and sits down. Blue keeps going, faster and faster, to 30. A scan line turns both pump bodies see-through: grey's pipe is 16% full, blue's is nearly full and rises with every stroke. Pump 31 gushes into blue's bucket. Blue carries it over, pours it into the top of grey's pump to prime it and sets the bucket under grey's spout; grey gets up, pumps, and on his second stroke water runs into the bucket. Line 2 types at the payoff.

## The script (as written)

**Pattern used:** one big counter as the hero (#32), an X-ray of the hidden progress (#33), one repeated action that speeds up (#35), same counter with a different stat (#20)
**Frame line (top):** PUMP 30. STILL DRY. (line 2 at the payoff, in blue: IT WAS RISING ALL ALONG.)
**Labels:** left: Stopped at 5 · right: Kept pumping
**Counters:** a big "5 PUMPS" over grey (it freezes and dims) and a big "1 → 31 PUMPS" over blue. During the scan: a fill % chip on each pump. Grey also gets a dark chip: "Must be dry"
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.0s | Hook: both pumping | Two old hand pumps. Both figures are already working the handles at 0.0s and both counters tick. After 5 pumps grey stops, peers into the spout and sits down by his pump. | PUMP 30. STILL DRY. · 5 PUMPS / 1 → 8 PUMPS · Must be dry | lever creaks, clunks per stroke |
| 3.0–5.0s | Blue keeps going | Blue pumps faster and faster, and the counter races. Nothing comes out. Grey greys. | 9 → 20 PUMPS | clunks speed up |
| 5.0–6.6s | The scan | A blue scan line sweeps down across both pumps, and their bodies turn see-through. Grey's pipe is 16% full of water. Blue's is nearly full and rises with every stroke. | 16% / 74% → 97% | scan sweep, a low hum |
| 6.6–7.9s | Pump 31 | The counter hits 31 and turns blue. Water gushes out of blue's spout into his bucket. | 31 PUMPS | big clunk, gush, splash |
| 7.9–12s | Kind payoff | Blue carries the full bucket over and pours it into the top of grey's pump to prime it. Grey gets up and pumps, and on the second stroke water runs into the bucket blue is holding. Line 2 types in. Dip, loop. | PUMP 30. STILL DRY. / IT WAS RISING ALL ALONG. | steps, pour, clunks, gush, typing, sparkle |

**Post caption:** Most people stop pumping when nothing comes out. But the water was climbing the pipe the whole time, and the next stroke was the one. Your effort is still counting even when you can't see it. How many pumps are you in?
**Loop point:** both pumping at stroke 1.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Pump 30. Still dry."
- Label `#lbl-emp` (`index.html`): "Stopped at 5"
- Label `#lbl-own` (`index.html`): "Kept pumping"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#gdry` "Must be dry" (dark negative), `#gpct` "16%" (numbers), `#bpct` "74%" (blue)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "It was rising all along."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const G_X = -2.05; // grey stands here, facing +x
const B_X = 2.05; // blue stands here, facing -x
const G_PUMP = -0.97;
const B_PUMP = 0.97;
const BODY_TOP = FLOOR_Y + 1.3;
const SPOUT_Y = FLOOR_Y + 0.95;
const SPOUT_LEN = 0.36;
const G_SPOUT = G_PUMP + SPOUT_LEN; // spout tips point at the centre
const B_SPOUT = B_PUMP - SPOUT_LEN;
const G_RATE = 1.75; // strokes per second
const G_STOP = 5 / G_RATE; // 2.86: fifth stroke done
const G_PEER = [3.0, 3.6];
const G_SIT = [3.7, 4.3];
const B_DONE = 7.2; // stroke 31 lands, the gush starts
const SCAN = [5.0, 5.7]; // scan line sweeps top to bottom
const XRAY_OFF = [7.7, 8.1];
const GUSH = [B_DONE, 8.2];
const B_WALK1 = [7.75, 8.5];
const B_PICK = [8.5, 8.85];
const B_PICK_AT = [0.1, 0.3];
const B_WALK2 = [8.85, 9.4];
const B_POUR = [9.4, 9.95]; // raise, tilt, pour
const POUR_FLOW = [9.6, 9.9];
const B_SET = [9.95, 10.35];
const G_LOOK = 9.2;
const G_UP = [9.45, 9.9];
const G_PUMP2 = 9.95; // grey pumps again
const G_RATE2 = 1.9;
const G_FLOW = G_PUMP2 + 1.5 / G_RATE2; // 10.74: on the second stroke
const COUNT_FADE = 7.9;
const TYPE_LINE_AT = 10.2;
const UP = { ...STAND, lean: 0.05, head: -0.05, shL: 1.3, elL: 0.35, shR: 1.35, elR: 0.35 };
const DOWN = { ...STAND, lean: 0.32, head: -0.2, thL: 0.12, knL: -0.22, thR: -0.06, knR: -0.12, shL: 0.75, elL: 0.25, shR: 0.78, elR: 0.25 };
const PEER = { ...STAND, lean: 0.55, head: -0.35, thL: 0.1, knL: -0.15, shL: 0.5, elL: 0.6, shR: 0.55, elR: 0.6 };
const SAT = { ...SIT, lean: 0.4, head: -0.35 };
const PICK = { ...CROUCH, shL: 0.5, elL: 0.3, shR: 0.55, elR: 0.25 };
const CARRY = { ...STAND, shR: 0.12, elR: 0.05 };
const POUR_P = { ...STAND, lean: 0.12, head: -0.15, shL: 1.55, elL: 0.3, shR: 1.6, elR: 0.25 };
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · a pump: base, body, cap, spout, pivot bracket, lever (lever drawn per frame) · blue's bucket · water streams and glows · scan line · figures · HTML · frame.

Functions:
- `makePump(x, dir, bodyMat)`: a pump: base, body, cap, spout, pivot bracket, lever (lever drawn per frame)
- `aimLever(p, hand)`
- `drawStream(m, on, x, yTop, yBottom, r, t)`: stream from (x, yTop) down to yBottom
- `drawScan(t)`
- `xray(t)`: how see-through a pump body is: from when the scan passes its top until XRAY_OFF
- `poseGrey(t)`
- `poseBlue(t)`
- `drawBucket(t)`: bucket: on the floor under blue's spout, then in blue's hand, poured, then under grey's spout
- `drawWater(t)`
- `makeCounter(id)`: HTML
- `drawCounter(c, n, since, x, blueAmt, fade, big)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Pump as one premixed, motion-synced track. Timing mirrors scene.js: a creak and a clunk on every stroke (grey's five, blue's thirty-one, speeding up), a soft blip as each counter ticks, grey sitting down, the scan sweep with a low hum, the gush and splash at pump 31, blue's steps and the bucket, the pour into grey's pump, grey's strokes and his water running, then the typed line 2 and a sparkle. Grey left, blue right. Owned synths and ../../sfx-library sounds only: nothing needs attribution.

Owned synths: `SR`, `bucket_clatter`, `counter_blip`, `floor_step`, `metal_creak`, `pipe_clunk`, `soft_thud`, `water_flow`, `water_pour`, `water_splash`.
`sfx-library/` sounds: `impact-bass-1`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-short`.

Rebuild: `cd videos/the-pump && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-pump/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/pump
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-pump && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-pump   # run in the background
```
`render.sh` writes `renders/13learns-pump.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
