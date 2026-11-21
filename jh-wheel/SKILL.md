---
name: jh-wheel
description: "13learns Job haters video \"The Wheel\" (\"A 9-5 keeps you running in place for 40 years\"). \"The Wheel\" — a grey \"Employee\" stick figure runs inside a hamster wheel while an \"Age 22 → 65\" counter ticks up above him. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawAge)."
---

# The Wheel: "A 9-5 keeps you running in place for 40 years" (13learns Job haters)

- **Project:** `videos/the-wheel/` (HyperFrames 0.8.181 + Three.js, 1080×1920, 30fps, 10s, seamless loop, no VO)
- **Script:** `videos/the-wheel/STORYBOARD.md` (the first video; it predates the SCRIPTS files)
- **Delivered:** `renders/13learns-the-wheel.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

"The Wheel" — a grey "Employee" stick figure runs inside a hamster wheel while an "Age 22 → 65" counter ticks up above him. At 30 a blue "Owner" figure steps off the wheel and walks away; the wheel keeps spinning empty. Seamless loop, no voiceover. Must replicate the look and quality of the reference clips (user: "Can we replicate same quality of videos?").

## The storyboard

Frames, timings and the animation rules used are in `videos/the-wheel/STORYBOARD.md`. Board images are in `videos/the-wheel/boards/`.

## On-screen text (where it lives)

- This one doesn't use the standard frame-line/label/chip layer; read `index.html` and `scene.js` for its text.

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const WHEEL_YAW = 0.55;
const WHEEL_R = 2.25;
const WHEEL_D = 1.3;
const RUNGS = 44;
const STAND_Z = -WHEEL_D / 2 - 0.4;
const STACK_X = 2.4;
const COINS = 15;
const COIN_T = 0.118;
const COIN_PITCH = 0.132;
const COIN_START = 5.55;
const COIN_EVERY = 0.2;
const GREY_LX = -0.35;
const GREY_LZ = -0.27;
const GOLD_LX = 0.3;
const GOLD_LZ = 0.3;
const MOTES = 46;
const OMEGA_PER_HZ = 1.1;
const BLUE_RGB = [74, 132, 247];
const INK_RGB = [245, 247, 250];
const RACE_START = 5.4;
const RACE_STEP = 3.2 / 35;
```

## How `scene.js` is built

Sections, in order: helpers · renderer / camera · lights · materials · stick figure rig · hamster wheel · coin stack · figures · dust motes · timing model · age counter · frame · place HTML labels from the 3D layout · skyline (seeded).

Functions:
- `mulberry32(seed)`
- `shadowed(mesh)`
- `capsule(r, len, mat, cy)`
- `makeFigure(bodyMat, legMat)`
- `mixPose(a, b, u)`
- `ankleY(th, kn)`
- `applyPose(fig, pose, x, groundY, z, lift = 0, yaw = 0)`
- `runPose(phase, amp = 0.78, lean = 0.2)`
- `walkPose(phase, amp = 0.42)`
- `layoutStack(t)`
- `integrate(fn, t, dt = 1 / 240)`
- `wheelAngle(t)`
- `poseGold(t)`
- `poseGrey(t)`
- `ageState(t)`
- `drawAge(t)`
- `renderAt(t)`: frame
- `toScreen(v)`: place HTML labels from the 3D layout

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Wheel as one premixed, motion-synced track. Timing is ported from scene.js (run cycles, wheel angle, coin schedule, jump/slump beats), so footsteps land on the frame a foot touches down and wheel clicks land as each rung passes. Generators and one-shots come from the shared library at ../../sfx-library (synth.py + library.json): synthesised coins/steps/wheel (owned), CC0 Freesound and Pixabay one-shots.

Owned synths: `SR`, `band`, `coin_clink`, `floor_step`, `load`, `lowp`, `mesh_step`, `norm`, `peak_window`, `rung_tick`.

Rebuild: `cd videos/the-wheel && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-wheel/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.181 snapshot --at 0.4,2,4,6,8,9.6 --no-end --describe false -o <scratchpad>/wheel
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-wheel && npx --yes hyperframes@0.8.181 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-wheel   # run in the background
```
`render.sh` writes `renders/13learns-wheel.mp4`. The file already delivered is `renders/13learns-the-wheel.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
