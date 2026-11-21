---
name: jh-conveyor
description: "13learns Job haters video \"The Conveyor\" (\"Everyone's on it. That doesn't mean it goes somewhere.\"). A line of identical greys rides a belt past Degree, Job, Promotion and Mortgage to 65, where it ends at a drop. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawBelt, drawSigns, drawBuild, makeCase)."
---

# The Conveyor: "Everyone's on it. That doesn't mean it goes somewhere." (13learns Job haters)

- **Project:** `videos/the-conveyor/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 13s, seamless loop, no VO)
- **Script:** `SCRIPTS-2.md` §2
- **Delivered:** `renders/13learns-the-conveyor.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Conveyor: a line of identical greys rides a belt past Degree, Job, Promotion and Mortgage to 65, where it ends at a drop. Blue steps off at Job, trips, and builds a staircase up to his own plateau. At the end he kneels at its edge and pulls the grey at the front of the line up.

## The script (as written)

**Pattern used:** the crowd walking in step (1.1M), the comfort zone break-out (5.9M)
**On-screen counter:** Age 22 → 65
**Labels:** The safe path / The other path
**Props:** a long grey conveyor belt crossing the floor, signposts along it (Degree → Job → Promotion → Mortgage → 65), a row of identical grey figures with briefcases, and a rough dirt track beside it
**Length:** 13s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.5s | Hook: in step | A line of identical grey figures rides the belt left to right. Each one hops onto it at "Degree". Blue is in the line too, same pose, same briefcase. | Age 22 → 26 | belt hum, synced footsteps |
| 2.5–4.0s | The step off | At "Job", blue looks up, hesitates and steps sideways off the belt onto the dirt. The belt keeps moving and a grey figure fills his gap at once. | Age 27 (blue) · "The other path" pops | single off-beat footstep, whoosh |
| 4.0–8.0s | Two paths | Blue stumbles, falls, gets up, and builds a short ramp out of the dirt. He's behind the crowd now. The belt carries the line past "Promotion" and "Mortgage" in perfect sync. | Age 28 → 50 | stumble thud, belt hum steady |
| 8.0–10.0s | The edge | The belt ends at the "65" sign, with a dark drop past it. The grey figures shuffle to the edge, and their briefcases fall first. Blue's ramp has climbed to a high plateau where his own small building glows. | Age 60 → 65 | briefcases falling (soft), hum stops |
| 10.0–13s | Kind payoff | Blue reaches a hand down from the plateau. One grey figure at the front looks up and takes it. Dip, loop. | Age 65 (blue) | low sparkle |

**Post caption:** School → degree → job → 65. Nobody chose the belt. They just never stepped off it.
**Loop point:** belt full and moving, blue back in line with a briefcase.

## On-screen text (where it lives)

- Label `#lbl-emp` (`index.html`): "The safe path"
- Label `#lbl-own` (`index.html`): "The other path"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 13;
const EDGE_X = 2.25; // the ground (and the belt) ends here
const BELT_X0 = -3.7;
const BELT_TOP = FLOOR_Y + 0.12;
const SPEED = 0.55; // belt speed, and the line's walking speed onto it
const SPACING = 0.45;
const BACK_Z = -1.1; // the track blue takes, behind the belt
const STEP_W = 0.34;
const STEP_RISE = 0.29;
const STEPS = 7;
const STAIR_X0 = -1.6;
const PLAT_X = [STAIR_X0 + STEPS * STEP_W - 0.02, 3.5];
const PLAT_TOP = FLOOR_Y + STEPS * STEP_RISE;
const SIGNS = [["Degree", -3.6], ["Job", -2.2], ["Promotion", -0.6], ["Mortgage", 0.9], ["65", 2.05]];
const LOOK_UP = 2.9;
const STEP_OFF = [3.5, 3.9];
const FILL = [3.7, 4.2];
const TRIP = [4.3, 4.6];
const RISE = [4.6, 5.0];
const STEP_AT = (i) => 5.1 + 0.35 * i; // each block pops up; blue hops on just after
const PLAT_AT = 7.55;
const PLAT_WALK = [7.8, 8.4];
const HOUSE_AT = 8.3;
const HOUSE_LIT = 8.6;
const KNEEL = [10.0, 10.5];
const G1_LOOK = 10.3;
const G1_REACH = 10.7;
const HOLD_AT = 11.3;
const PULL = [11.5, 12.2];
const AGES = [[0, 22], [3.5, 27], [8.0, 50], [9.3, 65]];
const BELT_L = EDGE_X - BELT_X0;
const TREAD_GAP = 0.3;
const DEPTH = 1.0;
const STAIR_Z = BACK_Z - 0.05;
const FRONT_X0 = -3.0;
const ORDER = ["G1", "G2", "G3", "BLUE", "G4", "G5", "G6"];
const QUEUE = riders.filter((r) => !r.isBlue).map((r, k) => ({ r, spot: EDGE_X - 0.2 - k * 0.36 }));
const RIDE = { ...STAND, shR: 0.04, elR: 0.06, shL: 0.1, elL: 0.12 };
const SHUFFLE = { ...STAND, lean: 0.18, head: 0.35, shL: 0.05, shR: 0.04, elR: 0.06 };
const CROUCH_HOP = { ...POSES.CROUCH, shL: -0.6, shR: -0.7 };
const STEP_OFF_X = FRONT_X0 - 3 * SPACING + SPEED * STEP_OFF[0];
const BLUE_END_X = 2.62;
const G = 9.8;
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · ground block that ends at the drop · the belt · signposts in front of the belt · blue's staircase and plateau (behind the belt) · the line · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `drawBelt(t)`
- `drawSigns()`
- `rockColumn(x0, x1, top, bottom = FLOOR_Y)`
- `drawBuild(t)`
- `makeCase()`
- `riderX(r, t)`
- `arriveTime(r)`
- `poseRider(r, t)`
- `poseBlue(t)`
- `slideAndFall(bag, x0, t0, t, z)`
- `drawBags(t)`
- `age(t)`
- `drawAge(t)`
- `placeTagAt(id, x, dy)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Conveyor as one premixed, motion-synced track. Timing mirrors scene.js (belt hum, each rider hopping on, the age ticks, blue stepping off and tripping, every staircase block and hop, the plateau and house, briefcases dropping and sliding off the lip, the hand-up), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `floor_step`, `mesh_step`, `quake_rumble`, `soft_thud`, `stone_crackle`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `ping`, `pop`, `rumble-wheel-loop`, `sparkle`, `whoosh-air-01`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-conveyor && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-conveyor/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/conveyor
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-conveyor && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-conveyor   # run in the background
```
`render.sh` writes `renders/13learns-conveyor.mp4`. The file already delivered is `renders/13learns-the-conveyor.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
