---
name: jh-snowball
description: "13learns Job haters video \"The Snowball\" (\"One melts. One grows.\"). Same 10 years on one snowfield. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawSnowfall, drawBlock, drawBall, drawSmall)."
---

# The Snowball: "One melts. One grows." (13learns Job haters)

- **Project:** `videos/the-snowball/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-5.md` §1
- **Delivered:** `renders/13learns-the-snowball.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Snowball: same 10 years on one snowfield. Grey starts with a big clear ice block ("Salary") and pats it proudly; every year it drips, shrinks and spreads a puddle (a "+3% raise" adds a sliver). Blue starts with a fist-sized snowball ("Skills") and never stops rolling it: it grows every year until it's twice the block's height and glows blue. Then blue breaks off a handful, packs it and rolls it to grey's feet. Grey picks it up, sets it down and starts to roll.

## The script (as written)

**Pattern used:** the early leader loses to a test; same counter, different stat
**Frame line (top):** SAME 10 YEARS. (line 2 at the payoff, in blue: ONE MELTS. ONE GROWS.)
**Labels:** left: Salary · right: Skills
**Shared counter:** Year 1 → 10, with a stat under each side: "buys 100%" → "buys 64%" / "×1" → "×12"
**Props:** a snowfield. Grey stands proudly beside a big clear ice block. Blue has a snowball the size of a fist and rolls it back and forth across his half, leaving a trail, and it grows each pass.
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.5s | Hook: the start | Grey pats his big ice block, hands on hips. Blue is already pushing a tiny snowball at 0.0s. | SAME 10 YEARS. · Year 1 · buys 100% / ×1 | snow crunch, a pat on ice |
| 1.5–6.0s | The years | Year ticks 2 → 8. Grey's block drips and shrinks and a puddle spreads under it. At Year 4 a "+3% RAISE" ice cube drops onto it: a sliver. Blue's ball grows with every pass until it's taller than the block. | Year 2 → 8 · buys 97% → 70% / ×2 → ×9 · +3% RAISE | drips, crunch passes, a tiny ice clink |
| 6.0–7.0s | The turn | Year 9: the ball passes the block's height. Grey's block slumps into a small cube in a wide puddle. | Year 9 | bass hit, slush |
| 7.0–9.5s | Year 10 | Blue's ball is huge and glows faintly blue. Grey looks down at the cube in his puddle. | Year 10 · buys 64% / ×12 (blue) | chime |
| 9.5–12s | Kind payoff | Blue breaks a handful off his ball, packs a small snowball and rolls it to grey's feet. Grey picks it up, sets it down and starts to roll. Line 2 types in. Dip, loop. | SAME 10 YEARS. / ONE MELTS. ONE GROWS. | pack crunch, roll, typing, sparkle |

**Post caption:** A salary loses a little value every year. Skills gain a little every year. Start your snowball small, but start it.
**Loop point:** grey's new little snowball → blue's tiny snowball at Year 1.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same 10 years."
- Label `#lbl-emp` (`index.html`): "Salary"
- Label `#lbl-own` (`index.html`): "Skills"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#raise` "+3% raise" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "One melts. One grows."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const BLOCK = { x: -2.12, z: -0.1, w: 1.0, h: 1.1, d: 0.8 };
const G_AT = { x: -1.3, z: 0.18 };
const BALL = { x: 1.35, z: 0.1 };
const R0 = 0.12;
const RMAX = 0.9;
const YEARS = [[0, 1], [1.5, 2], [2.15, 3], [2.8, 4], [3.45, 5], [4.1, 6], [4.75, 7], [5.4, 8], [6.0, 9], [7.0, 10]];
const BUYS = [100, 97, 93, 89, 85, 81, 77, 73, 68, 64];
const SKILL = [1, 2, 3, 4, 5, 6, 7, 9, 10, 12];
const PATS = [0, 1.4];
const RAISE = [2.8, 3.1];
const CHEER = [3.1, 3.7];
const SLUMP = 6.0;
const ROLL_STOP = [7.6, 7.95];
const GLOW = [7.1, 8.0];
const B_REACH = [8.45, 8.75];
const HANDFUL = 8.75;
const PACK = [8.8, 9.35];
const B_TURN = [8.95, 9.3];
const BOWL = [9.3, 9.5];
const RELEASE = 9.45;
const ROLL_TO = [9.45, 9.85];
const G_TURN = [9.75, 10.0];
const PICK = [10.0, 10.35];
const LOOK = [10.35, 10.6];
const SET = [10.6, 10.85];
const G_PUSH = [10.95, 11.75];
const TYPE_LINE_AT = 10.0;
const SMALL_AT = { x: -0.72, z: 0.22 };
const B_BACK = [9.6, 10.05]; // blue steps back out of grey's way
const LUMPS = Array.from({ length: 14 }, (_, i) => {
const FLAKES = 140;
const CROUCH_LEGS = { thL: 1.0, knL: -1.6, thR: 0.6, knR: -1.2 };
const PAT = { ...STAND, lean: 0.1, head: -0.15, shR: 1.15, elR: 0.35, shL: 0.1, elL: 0.2 };
const CHEER_P = { ...REACH, shL: 2.6, shR: 2.5 };
const LOOK_DOWN = { ...STAND, head: -0.45, lean: 0.12 };
const PACK_P = { ...STAND, lean: 0.1, head: -0.3, shL: 1.15, elL: 1.05, shR: 1.1, elR: 1.1 };
const HOLD_P = { ...STAND, head: -0.25, shR: 1.0, elR: 1.1, shL: 0.95, elL: 1.15 };
const INVITE = { ...STAND, head: 0.1, shR: 0.9, elR: 0.3, shL: 0.1, elL: 0.2 };
const LINE2 = "One melts. One grows.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials & helpers · the snowfield · grey's ice block, its puddle and drips · blue's snowball · figures · HTML · frame.

Functions:
- `yearAt(t)`
- `makeGlow(size, color)`
- `snowGeo(seed, bump)`: a lumpy sphere so the snow reads as packed snow, not a billiard ball
- `drawSnowfall(t)`
- `drawBlock(t)`
- `drawBall(t)`
- `pushAgainst(fig, pose, ballX, ballZ, r, facing, z)`: slide a pushing figure along x until its right hand rests on the ball's surface
- `pushPose(r, phase, amp = 0.28)`
- `blueRestX()`
- `poseBlue(t)`
- `smallAt(t)`
- `drawSmall(t)`
- `poseGrey(t)`
- `drawHud(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Snowball as one premixed, motion-synced track. Timing mirrors scene.js: blue's snowball crunching along the whole time (louder and lower as it grows), a tick for each year, grey's pats on the block, drips into a growing puddle, the "+3% raise" cube clinking on top, the block slumping at Year 9, the ball's blue glow; then the handful, the packing, the small snowball rolled to grey's feet, and grey picking it up and rolling it. Grey sits left in the stereo field, blue right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `glass_tink`, `mesh_step`, `rung_tick`, `soft_thud`, `wheel_rumble`.
`sfx-library/` sounds: `applause-small-01`, `chime`, `pop`, `sparkle`, `typing`, `water-splash-01`, `water-trickle-01`, `whoosh-air-01`, `whoosh-short`.

Rebuild: `cd videos/the-snowball && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-snowball/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/snowball
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-snowball && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-snowball   # run in the background
```
`render.sh` writes `renders/13learns-snowball.mp4`. The file already delivered is `renders/13learns-the-snowball.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
