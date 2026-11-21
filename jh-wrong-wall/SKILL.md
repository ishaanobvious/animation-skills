---
name: jh-wrong-wall
description: "13learns Job haters video \"The Wrong Wall\" (\"He reached the top. Of someone else's wall.\"). Grey races up a ladder of job titles on a huge grey wall. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawMine, drawCamera, drawYear, drawTitles)."
---

# The Wrong Wall: "He reached the top. Of someone else's wall." (13learns Job haters)

- **Project:** `videos/the-wrong-wall/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 11s, seamless loop, no VO)
- **Script:** `SCRIPTS-3.md` §6
- **Delivered:** `renders/13learns-the-wrong-wall.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Wrong Wall: grey races up a ladder of job titles on a huge grey wall. At the top he looks over, and the camera rises with him: the wall was hiding someone else's mansion. Blue, meanwhile, builds a short wall of his own, climbs it, and his own small house lights up behind it.

## The script (as written)

**Pattern used:** a familiar idiom drawn literally (the ladder against the wrong wall); early leader loses
**Frame line (top):** HE REACHED THE TOP. (line 2 at the reveal: OF SOMEONE ELSE'S WALL.)
**Labels:** Climbing / Building
**Small ticker:** Title: Intern → VP (grey); blue's says "Year 1 → 10"
**Props:** a very tall grey wall with a fast ladder for grey, rungs labelled with job titles; blue builds his own short wall from bricks and puts his own small ladder against it
**Length:** 11s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.0s | Hook: the fast climb | Grey races up a tall ladder. Each rung pops a title: Intern, Analyst, Manager, Director. Blue lays bricks on the ground: his wall is knee-high. | Intern → Director · Year 1 → 4 | rung clanks speeding up, brick taps |
| 3.0–6.0s | Way ahead | Grey is near the top, waving down. Blue's wall is shoulder-high now; he leans his own short ladder on it. | VP · Year 5 → 8 | rung clanks, wind |
| 6.0–7.5s | The turn | Grey reaches the top and looks over the wall: on the other side is a huge glowing mansion with a sign "OWNER". The camera follows his gaze. | HE REACHED THE TOP. | arrival ping, reveal whoosh |
| 7.5–9.0s | The reveal | Line 2 types in. The owner waves up at grey from his pool. Grey's ladder creaks. | OF SOMEONE ELSE'S WALL. | key presses, ladder creak |
| 9.0–11s | Payoff | Blue tops his own small wall, steps onto it, and a little blue house lights up behind it, his name on the sign. Dip, loop. | Year 10 (blue) | chime, sparkle |

**Post caption:** A fast climb is only good news if you checked whose wall it was.
**Loop point:** grey at the foot of the ladder, blue with one brick.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "He reached the top."
- Label `#lbl-emp` (`index.html`): "Climbing"
- Label `#lbl-own` (`index.html`): "Building"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Of someone else's wall."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 11;
const WALL_X = [-4.6, 0.2];
const WALL_H = 3.6;
const WALL_TOP = FLOOR_Y + WALL_H;
const LADDER_X = -2.2;
const LADDER_Z = [1.1, 0.32]; // bottom, top
const BRICK = { w: 0.26, h: 0.2, d: 0.32 };
const ROWS = 8;
const COLS = 5;
const MY_WALL_X = 1.6;
const MY_WALL_TOP = FLOOR_Y + ROWS * BRICK.h;
const BLUE_X = 1.28;
const WAVE = [4.2, 4.8];
const OVER_TOP = [5.7, 6.1];
const CAM_UP = [6.3, 7.2];
const CAM_DOWN = [8.6, 9.25];
const OWNER_WAVE = [7.8, 8.6];
const CREAK = 8.05;
const SIT_DOWN = [8.2, 8.7];
const TYPE_LINE_AT = 7.4;
const MY_LADDER_AT = 5.0;
const CLIMB_MINE = [9.3, 9.9];
const HOUSE_UP = 9.7;
const HOUSE_LIT = 10.0;
const SHADES_AT = 10.35;
const TITLES = [["Intern", 0.4], ["Analyst", 1.0], ["Manager", 1.6], ["Director", 2.2], ["VP", 2.9]];
const YEARS = [[0, 1], [1.0, 2], [2.0, 3], [3.0, 4], [4.0, 5], [5.0, 6], [6.0, 7], [7.0, 8], [8.4, 9], [9.8, 10, true]];
const BRICK_T = (i) => 0.25 + (i * (8.6 - 0.25)) / (ROWS * COLS);
const MY_WALL_RIGHT = MY_WALL_X + BRICK.w * (COLS + 0.5);
const PLACE_HIGH = { ...STAND, lean: 0.08, head: -0.2, shL: 1.95, elL: 0.3, shR: 1.75, elR: 0.4 };
const LINE2 = "Of someone else's wall.";
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · ground (real geometry, so the camera can rise over it) · the tall wall and its ladder · what the wall hides · blue's own wall, ladder and house · figures · camera: rise over the wall with grey, then come back down · HTML · frame.

Functions:
- `climbH(t)`: grey's height up the ladder (feet above the floor)
- `makeGlow(size, color)`
- `poseOwner(t)`
- `drawMine(t)`
- `climbPose(h)`
- `poseGrey(t)`
- `poseBlue(t)`
- `reveal(t)`
- `drawCamera(t)`
- `drawYear(t)`
- `drawTitles(t, k)`
- `drawSigns(t, k)`
- `placeTagAt(id, x, dy, k)`
- `drawLine2(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Wrong Wall as one premixed, motion-synced track. Timing mirrors scene.js (a clank per rung grey climbs, a rising note per job title, blue's brick taps, the camera rise and the reveal, the owner, the ladder creak, blue climbing his own wall and his house lighting up), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `counter_blip`, `floor_step`, `glass_tink`, `mesh_step`, `metal_creak`, `pipe_clunk`, `soft_thud`.
`sfx-library/` sounds: `chime`, `click-soft`, `ping`, `pop`, `sparkle`, `typing`, `whoosh`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-wrong-wall && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-wrong-wall/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/wrong-wall
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-wrong-wall && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-wrong-wall   # run in the background
```
`render.sh` writes `renders/13learns-wrong-wall.mp4`. The file already delivered is `renders/13learns-the-wrong-wall.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
