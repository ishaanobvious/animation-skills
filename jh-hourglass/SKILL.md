---
name: jh-hourglass
description: "13learns Job haters video \"The Hourglass\" (\"Every salary is paid in hours.\"). Each figure holds an hourglass of pale sand, the hours of his life. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeHourglass, makeStream, drawStream, makeCoins)."
---

# The Hourglass: "Every salary is paid in hours." (13learns Job haters)

- **Project:** `videos/the-hourglass/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-5.md` §3
- **Delivered:** `renders/13learns-the-hourglass.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Hourglass: each figure holds an hourglass of pale sand, the hours of his life. Grey tips his into the tray of a PAYROLL window, pour after pour, and one coin slides back each time. Blue tips his into the funnel of a small machine marked MY THING and gets nothing back, for years. At Age 33 the machine clunks on, its gear spins and coins pour out of its chute on their own; blue sets his hourglass down with plenty of sand left. Grey keeps pouring until his is nearly empty. Then blue brings a small blue funnel over and sets it on grey's tray, and grey's next pour goes into it.

## The script (as written)

**Pattern used:** visible vs hidden; same counter, different stat
**Frame line (top):** EVERY SALARY IS PAID IN HOURS. (line 2: BUILD SOMETHING THAT ISN'T.)
**Labels:** left: Sells hours · right: Builds once
**Shared counter:** Age 25 → 45, with a stat under each side: "Hours sold: 0 → 40,000" / "Hours sold: 0 → 6,000"
**Props:** each figure holds a big glass hourglass of pale sand. Grey stands at a small "PAYROLL" window: each time he tips sand into the tray, one coin slides back. Blue pours sand into the funnel on top of a small machine ("MY THING"). For a while nothing comes out, and then it starts dropping coins on its own.
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: pour, coin | Grey is already tipping sand into the tray at 0.0s and a coin clinks back. Blue pours into his machine's funnel and gets no coin. | EVERY SALARY IS PAID IN HOURS. · Age 25 | sand hiss, coin clink, machine whir |
| 2.0–5.5s | The years | Age 26 → 32. Grey's rhythm is steady: pour, coin, pour, coin, and his top bulb drops. Blue keeps pouring and the machine stays quiet. Grey is clearly ahead on coins. | Age 26 → 32 · stats climb | sand + clink loop, whir |
| 5.5–6.5s | The turn | Age 33: blue's machine clunks, its gear spins, and coins start dropping from its chute, faster than grey's. Blue stops pouring and sets his hourglass upright. | Age 33 (blue) | clunk, gear spin, coin cascade |
| 6.5–9.5s | Two paths | Age 34 → 45. Grey keeps pouring and his top bulb is nearly empty. Blue's machine keeps dropping coins while his own hourglass holds plenty of sand. | Age 45 · 40,000 / 6,000 | slower sand for grey, steady coin flow |
| 9.5–12s | Kind payoff | Blue walks over with a small blue funnel and sets it on grey's tray. Grey's next pour goes into the funnel instead. Line 2 types in. Dip, loop. | EVERY SALARY IS PAID IN HOURS. / BUILD SOMETHING THAT ISN'T. | funnel clink, sand, typing, sparkle |

**Post caption:** A salary is the price of your hours, and hours don't refill. Spend some of them building something that pays without them.
**Loop point:** both figures at Age 25 with full top bulbs, mid-pour.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Every salary is paid in hours."
- Label `#lbl-emp` (`index.html`): "Sells hours"
- Label `#lbl-own` (`index.html`): "Builds once"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#payroll` "PAYROLL" (light), `#mything` "MY THING" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Build something that isn't."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const G_AT = { x: -0.72, z: 0.05 };
const B_AT = { x: 0.72, z: 0.05 };
const BOOTH = { x0: -2.65, x1: -1.75, h: 2.0, z: 0.0, d: 0.5 };
const TRAY = { x: -1.5, y: FLOOR_Y + 0.98, z: 0.05, w: 0.5, d: 0.5 };
const MACH = { x: 1.95, w: 0.9, h: 0.95, d: 0.6, z: 0.0 };
const G_PILE = { x: -1.12, z: 0.55 };
const B_PILE = { x: 1.5, z: 0.82 };
const B_GIVE_AT = { x: -1.55, z: 0.8 };
const TURN = 5.5; // Age 33: the machine starts
const AGE_END = 9.0; // Age 45
const B_SET_DOWN = [5.75, 6.35];
const B_GRAB = [9.0, 9.3];
const B_WALK = [9.35, 10.15];
const B_PLACE = [10.25, 10.55];
const B_STEP_BACK = [10.6, 11.15];
const FUNNEL_POUR = 10.95;
const TYPE_LINE_AT = 10.0;
const G_POURS = [];
const B_POURS = G_POURS.filter((t) => t < TURN - 0.3);
const MACH_COINS = [];
const HG_H = 0.6;
const NECK_Y = 0;
const B_SLOTS = [];
const HOLD = { ...STAND, head: -0.1, shL: 0.6, elL: 1.25, shR: 0.55, elR: 1.3 };
const POUR = { ...HOLD, lean: 0.25, head: -0.2, shL: 1.05, elL: 0.95, shR: 1.0, elR: 1.0 };
const CARRY = { ...STAND, shR: 0.9, elR: 1.2, shL: 0.1, elL: 0.2 };
const PLACE = { ...STAND, lean: 0.3, head: -0.2, shR: 1.35, elR: 0.25, shL: 0.1, elL: 0.2 };
const INVITE = { ...STAND, head: 0.1, shR: 0.8, elR: 0.35, shL: 0.1, elL: 0.2 };
const LINE2 = "Build something that isn't.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials & helpers · hourglasses · the payroll window · the machine · coins · figures · HTML · frame.

Functions:
- `add(m, x, y, z)`
- `makeGlow(size, color)`
- `makeHourglass()`
- `setSand(hg, s)`
- `holdHourglass(hg, fig, yaw, tilt)`: (yaw is passed in: after applyPose's rotateZ, root.rotation.y can read back as 0 for a yaw of π)
- `mouthOf(hg)`
- `makeStream()`
- `drawStream(m, from, toY, on)`
- `makeCoins(n)`
- `drawGreyCoins(t)`
- `drawBlueCoins(t)`
- `poseGrey(t)`
- `poseBlue(t)`
- `drawProps(t, gEnv)`
- `ageSince(t)`: seconds since the age last ticked over
- `drawHud(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Hourglass as one premixed, motion-synced track. Timing mirrors scene.js: every pour (a hiss of sand) and, for grey, the coin that slides back out of the payroll window and clinks onto his stack; blue's pours into a machine that only hums, then the clunk at Age 33, the gear and a trickle of coins that keeps speeding up; blue setting his hourglass down, fetching the spare funnel and walking it over; grey's last pour into it. Grey sits left in the stereo field, blue right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `air_whoosh`, `coin_clink`, `floor_step`, `pipe_clunk`, `rung_tick`, `soft_thud`, `wheel_rumble`.
`sfx-library/` sounds: `chime`, `click-soft`, `glass-tink-01`, `ping`, `rumble-wheel-loop`, `sparkle`, `typing`.

Rebuild: `cd videos/the-hourglass && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-hourglass/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/hourglass
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-hourglass && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-hourglass   # run in the background
```
`render.sh` writes `renders/13learns-hourglass.mp4`. The file already delivered is `renders/13learns-the-hourglass.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
