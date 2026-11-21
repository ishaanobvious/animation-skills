---
name: jh-lifeboat
description: "13learns Job haters video \"The Lifeboat\" (\"Build it before you need it.\"). On the deck of THE COMPANY, grey lounges and laughs while blue hammers a little boat together. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawShip, drawBoat, drawStorm, drawChair)."
---

# The Lifeboat: "Build it before you need it." (13learns Job haters)

- **Project:** `videos/the-lifeboat/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-3.md` §1
- **Delivered:** `renders/Posted/13learns-the-lifeboat.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Lifeboat: on the deck of THE COMPANY, grey lounges and laughs while blue hammers a little boat together. A LAYOFFS storm sinks the ship; blue's boat floats free, grey clings to his deck chair. Blue rows over, holds out an oar and pulls him in.

## The script (as written)

**Pattern used:** mockery then the season flips (umbrella reel, 3.2M); the idiom drawn literally
**Frame line (top):** THEY LAUGHED WHILE THE SEA WAS CALM. (line 2 at the payoff, in blue: BUILD IT BEFORE YOU NEED IT.)
**Labels:** Relaxing / Building
**Small ticker:** Year 1 → 6
**Props:** a big grey cruise-style ship labelled "The Company" on calm dark water; a deck chair; a small blue lifeboat blue builds plank by plank on the deck; a storm cloud
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.0s | Hook: calm sea | Grey lounges in a deck chair with a drink. Blue hammers planks into a little boat beside him. "HA" bubbles float up from grey every time blue hits a nail. | Year 1 → 3 · "HA" ×4 | gentle waves, hammer taps, "HA" pops |
| 3.0–5.0s | The boat's done | Blue fits the last plank and paints a blue stripe. Grey toasts him sarcastically. | Year 4 | brush swipe, glass clink |
| 5.0–6.5s | The turn | A storm cloud rolls over a "LAYOFFS" headline banner. The ship lists, water floods the deck, the deck chair slides. | Year 5 · "LAYOFFS" | thunder, wave crash, metal groan |
| 6.5–9.0s | Two paths | Blue's boat floats free and rides the swell. Grey clings to his floating deck chair, soaked, fading. | Year 5 → 6 | splash, rain bed |
| 9.0–12s | Kind payoff | Blue rows over and holds an oar out. Grey grabs it and gets pulled into the boat. The second line types in. Dip, loop. | BUILD IT BEFORE YOU NEED IT. | oar thunk, sparkle |

**Post caption:** The best time to build your own thing is while your job still feels safe.
**Loop point:** calm sea, grey in the deck chair, blue holding the first plank.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "They laughed whilethe sea was calm."
- Label `#lbl-emp` (`index.html`): "Relaxing"
- Label `#lbl-own` (`index.html`): "Building"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Build it before you need it."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const WATER_Y = FLOOR_Y - 0.9;
const CHAIR_X = -2.0; // on the deck (ship-local)
const BOAT_X = 2.05;
const BLUE_DECK_X = 1.3;
const CHOCK = 0.12;
const DRAFT = 0.16;
const RESCUE_X = -0.55; // where blue rows to
const STRIKES = [0.45, 1.05, 1.65, 2.25, 2.85]; // four planks, then the bench and oar
const PAINT = [3.25, 3.85];
const TOAST = [3.9, 4.5];
const CLIMB_IN = [4.05, 4.65];
const STORM_IN = [4.8, 5.4];
const ALARM = 5.05;
const LIGHTNING = [5.25, 6.15, 7.45];
const ROW = [9.0, 10.0];
const OAR_OUT = [10.0, 10.4];
const GRAB = 10.6;
const PULL = [10.6, 11.3];
const LIFT = [11.3, 11.8];
const TYPE_LINE_AT = 10.2;
const YEARS = [[0, 1], [0.9, 2], [1.9, 3], [3.3, 4], [ALARM, 5], [ROW[0], 6, true]];
const T_BOAT = firstTime((t) => carry(BOAT_X, CHOCK, t).y <= WATER_Y - DRAFT);
const T_CHAIR = firstTime((t) => carry(CHAIR_X - chairSlide(t), 0, t).y <= WATER_Y + 0.02);
const BANDS = 4;
const BOAT_H = 0.44;
const LAUGH = { ...RECLINE, lean: -0.78, head: -0.45, shL: 0.6, elL: 1.2 };
const TOAST_P = { ...RECLINE, shR: 2.3, elR: 0.35, head: -0.1 };
const BRACE = { ...SIT_BOAT, lean: 0.25, head: -0.15, shL: 0.5, elL: 0.2, shR: 0.5, elR: 0.2, ab: 0.55 };
const HAMMER_UP = { ...STAND, lean: 0.2, head: 0.25, thL: 0.2, knL: -0.25, thR: -0.15, knR: -0.1, shL: 0.9, elL: 0.5, shR: 2.5, elR: 0.6 };
const HAMMER_DOWN = { ...HAMMER_UP, lean: 0.32, shR: 1.15, elR: 0.15 };
const PULL_BACK = { ...KNEEL_OUT, lean: 0.15, shL: 1.05, elL: 0.9, shR: 1.0, elR: 0.95 };
const LINE2 = "Build it before you need it.";
```

## How `scene.js` is built

Sections, in order: layout · story beats · the ship's motion · materials · sea · the ship · grey's deck chair · blue's boat: four plank bands, then a bench and an oar · storm · figures · HTML · frame.

Functions:
- `carry(lx, ly, t)`
- `firstTime(pred)`
- `drawShip(t)`
- `boatXform(t)`
- `boatPoint(lx, ly, out = new THREE.Vector3()`
- `drawBoat(t)`
- `drawStorm(t)`
- `strikeSwing(t)`
- `poseBlue(t)`
- `chairXform(t)`
- `drawChair(t)`
- `poseGrey(t)`
- `drawOar(t)`
- `drawYear(t)`
- `drawHas(t)`
- `drawCompany(t)`
- `drawLine2(t)`
- `placeTagAt(id, x, dy)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Lifeboat as one premixed, motion-synced track. Timing mirrors scene.js (hammer strikes and the "HA"s, painting, the toast, the storm and its lightning, the ship groaning and flooding, the chair and the boat hitting the water, rowing, the oar, the rescue), so every sound lands on its frame. The moments the chair and the boat float free are recomputed from the same sink curve the scene uses. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `glass_tink`, `metal_creak`, `pipe_clunk`, `quake_rumble`, `soft_thud`, `water_flow`, `water_splash`.
`sfx-library/` sounds: `click`, `click-soft`, `ping`, `pop`, `sparkle`, `typing`, `water-splash-01`, `water-splash-02`, `water-trickle-01`, `whoosh-air-01`, `whoosh-short`.

Rebuild: `cd videos/the-lifeboat && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-lifeboat/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/lifeboat
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-lifeboat && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-lifeboat   # run in the background
```
`render.sh` writes `renders/13learns-lifeboat.mp4`. The file already delivered is `renders/Posted/13learns-the-lifeboat.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
