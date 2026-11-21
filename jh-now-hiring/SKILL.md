---
name: jh-now-hiring
description: "13learns Job haters video \"Now Hiring\" (\"They laughed at the first brick.\"). Coworkers on the office balcony laugh at blue's first brick. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawOffice, drawTower, drawYear, drawHas)."
---

# Now Hiring: "They laughed at the first brick." (13learns Job haters)

- **Project:** `videos/now-hiring/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-3.md` §5
- **Delivered:** `renders/Posted/13learns-now-hiring.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Now Hiring: coworkers on the office balcony laugh at blue's first brick. The bricks come faster and faster until blue has a tower; the office gets a RESTRUCTURING banner and goes dark. The coworkers walk over with a "WE ALWAYS BELIEVED IN YOU" banner, and blue holds the door open.

## The script (as written)

**Pattern used:** the crowd flips ("They laughed at every brick", "Now they're his biggest fans"), with our kind ending
**Frame line (top):** THEY LAUGHED AT THE FIRST BRICK. (line 2 at the payoff: NOW THEY'RE APPLYING.)
**Labels:** The office / The builder
**Small ticker:** Year 1 → 7
**Props:** a row of grey coworkers at an office window (a tall grey building on the left); blue's tiny brick shop on the right that grows into a tower with a glowing blue sign; a "RESTRUCTURING" banner that falls over the office
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.0s | Hook: the laughing window | Blue lays one brick on an empty lot. The office window full of coworkers points and laughs; "HA" floats up with every brick. | Year 1 → 2 · "HA" ×5 | brick tap, "HA" pops, office murmur |
| 3.0–6.0s | It grows | Bricks go up faster: a shop, then a second floor, then a tower. The laughs shrink to a couple, then stop. | Year 3 → 5 | brick taps speeding up |
| 6.0–7.5s | The turn | A "RESTRUCTURING" banner unrolls down the office building and its lights go out floor by floor. Blue's tower lights up. | Year 6 · "RESTRUCTURING" | banner unfurl, lights-off clunks, chime |
| 7.5–10.0s | The flip | The coworkers walk out to blue's tower holding a banner: "WE ALWAYS BELIEVED IN YOU". | Year 7 | footsteps, crowd murmur |
| 10–12s | Kind payoff | Blue hangs a "NOW HIRING" sign on his door and holds it open. Line 2 types in. Dip, loop. | NOW THEY'RE APPLYING. | sign clack, door creak, sparkle |

**Post caption:** The people laughing at your side project today will ask if you're hiring in five years. Hire the good ones.
**Loop point:** empty lot, full laughing window.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "They laughed atthe first brick."
- Label `#lbl-emp` (`index.html`): "The office"
- Label `#lbl-own` (`index.html`): "The builder"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Now they're applying."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const OFF = { x0: -4.6, x1: -1.3, z0: -1.2, z1: 0.4, h: 3.5 };
const FLOOR_H = OFF.h / 4;
const OFF_DOOR_X = -2.0;
const LEDGE_Y = FLOOR_Y + FLOOR_H + 0.05;
const BRICK = { w: 0.26, h: 0.2, d: 0.5 };
const ROW_SPEC = [[5, 10, 0.95], [5, 8, 1.21], [7, 6, 1.47]]; // [rows, bricks per row, left x]
const MY_DOOR_X = 2.9;
const BLUE_X0 = 0.55;
const HA_TIMES = [0.45, 1.05, 1.65, 2.25, 2.85, 3.4, 3.9];
const FAST = [3.0, 6.0];
const BANNER = [6.0, 6.5];
const LIGHTS_OUT = [6.3, 6.6, 6.9];
const TOWER_LIT = 6.5;
const BALCONY_EMPTY = 7.2;
const WALK_OUT = 7.3;
const BLUE_TO_DOOR = [7.6, 8.4];
const BANNER_UP = 9.2;
const HANG_SIGN = [9.9, 10.3];
const DOOR_OPEN = [10.4, 10.8];
const APPLY_STEP = [10.8, 11.5];
const TYPE_LINE_AT = 10.4;
const SHADES_AT = 6.8;
const YEARS = [[0, 1], [1.6, 2], [3.0, 3], [4.0, 4], [5.0, 5], [6.0, 6], [7.5, 7, true]];
const N_BRICKS = bricks.length;
const TOWER_TOP = FLOOR_Y + BRICK.h * 17;
const WALK_TARGETS = [[-0.5, 1.1], [0.0, 1.0], [0.5, 1.15], [1.0, 1.05], [1.55, 1.1]];
const LAUGH = { ...STAND, lean: -0.3, head: -0.4, shR: 1.55, elR: 0.05, shL: 0.45, elL: 1.6 };
const STARE = { ...STAND, head: 0.05, shL: 0.55, elL: 2.1, shR: 0.6, elR: 2.05, ab: -0.15, eab: 0.35 };
const HOLD_BANNER = { ...STAND, head: -0.1, shL: 1.25, elL: 0.5, shR: 1.25, elR: 0.5 };
const S_B = 0.55;
const PLACE_HIGH = { ...STAND, lean: -0.05, head: -0.45, shL: 2.4, elL: 0.3, shR: 2.25, elR: 0.35 };
const HANG = { ...STAND, head: -0.2, shL: 2.0, elL: 0.6, shR: 2.1, elR: 0.5 };
const INVITE = { ...STAND, head: 0.05, shL: 0.15, elL: 0.2, shR: 1.2, elR: 0.25, ab: 0.4 };
const LINE2 = "Now they're applying.";
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · the office · blue's tower, brick by brick · the coworkers · blue · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `drawOffice(t)`
- `drawTower(t)`
- `haPulse(t)`
- `poseCoworkers(t)`
- `poseBlue(t)`
- `drawYear(t)`
- `drawHas(t)`
- `pin(el, v, opacity)`
- `drawSigns(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Now Hiring as one premixed, motion-synced track. Timing mirrors scene.js (each "HA", every brick — slow at first, then a rattle as the tower goes up — the restructuring banner, the office lights going out floor by floor, the tower lighting up, the walk over, the sign, the door), so every sound lands on its frame. The brick schedule uses the same formula as the scene. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `floor_step`, `pipe_clunk`, `soft_thud`, `valve_squeak`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `error`, `ping`, `pop`, `sparkle`, `typing`, `whoosh-short`.

Rebuild: `cd videos/now-hiring && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/now-hiring/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/now-hiring
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/now-hiring && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh now-hiring   # run in the background
```
`render.sh` writes `renders/13learns-now-hiring.mp4`. The file already delivered is `renders/Posted/13learns-now-hiring.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
