---
name: jh-lift
description: "13learns Job haters video \"The Lift\" (\"Take the stairs.\"). A cutaway building. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawSteps, drawProps, drawCount, drawLine2)."
---

# The Lift: "Take the stairs." (13learns Job haters)

- **Project:** `videos/the-lift/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-4.md` §3
- **Delivered:** `renders/13learns-the-lift.mp4` (rendered)
- **Old A/B file:** `renders/13learns-the-lift-alt.mp4`. It predates the one-version rule. Don't make new `-alt` renders.
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Lift: a cutaway building. Grey waits at a lift whose call button says "WHEN I'M READY"; blue lays one glowing step a day and climbs a switchback stair to a door marked MY BUSINESS. At Day 365 the lift reads OUT OF ORDER. Blue opens his door, then flicks a switch that lights every step down to the ground floor next to grey, who picks up his suitcase and takes the first one.

## The script (as written)

**Pattern used:** same counter, different stat ("Nobody builds a house in a day", tested 4 times); the hook is grey jabbing the button
**Frame line (top):** THE LIFT ISN'T COMING. (line 2 at the payoff, in blue: TAKE THE STAIRS.)
**A/B line 2:** THE STAIRS WERE OPEN THE WHOLE TIME.
**Labels:** left: One step a day · right: Waiting for the lift
**Shared counter (top-centre):** Day 1 → 365, with a stat under each side: "365 steps" / "0 floors"
**Props:** a cutaway building. Left: an open stairwell where blue lays one glowing step per beat, climbing toward a lit door at the top marked "MY BUSINESS". Right: a lift door with a floor display stuck on "G" and a call button labelled "WHEN I'M READY".
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.5s | Hook: the button | Grey is jabbing the call button over and over at 0.0s. Blue sets down step one and stands on it. | Day 1 · 1 step / 0 floors | button clicks ×4, soft thud |
| 1.5–6.0s | The year | The counter races to 300. Blue adds a step each beat and climbs; the camera rises with him. Grey checks his watch, sits on a suitcase, scrolls, presses the button again. The lift display flickers "G… G… G". | Day 2 → 300 · steps count up / 0 floors | step thuds speeding up, occasional button click, ding that never comes |
| 6.0–7.0s | The turn | Day 365. The lift display changes to "OUT OF ORDER". Grey's arm drops. | Day 365 · OUT OF ORDER | error tone, bass hit |
| 7.0–9.5s | The top | Blue lays the last step, opens the lit door and the floor fills with blue light. | 365 steps (blue) | last thud, door pop, chime |
| 9.5–12s | Kind payoff | Blue flicks a switch by his door: every step he built lights up down to the ground floor, right next to grey. Grey looks at the stairs, picks up his suitcase and puts a foot on step one. Line 2 types in. Dip, loop. | THE LIFT ISN'T COMING. / TAKE THE STAIRS. | switch click, light cascade (sparkle run), typing |

**Post caption:** There's no lift to your own business. There's one step today and another one tomorrow. What's your step today?
**Loop point:** grey's foot on step one becomes blue's step one at Day 1.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "The lift isn’t coming."
- Label `#lbl-own` (`index.html`): "One step a day"
- Label `#lbl-emp` (`index.html`): "Waiting for the lift"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#display` "G" (light), `#ready` "WHEN I’M READY" (light), `#biz` "MY BUSINESS" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Take the stairs."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const RISE = 0.2;
const RUN = 0.33;
const BACK_Z = -0.9;
const TOP_H = 3.2; // the top landing, above the floor
const SHAFT = { x0: 1.0, x1: 3.3, z1: -0.3 };
const LIFT_X = 2.15;
const GREY_AT = { x: 0.75, z: 0.05 };
const CASE_AT = { x: 0.28, z: 0.22 };
const BLUE_START = { x: -0.2, z: 0.42 };
const DOOR_X = 0.02;
const PIECES = [];
const N = PIECES.length;
const T_PIECE = PIECES.map((_, k) => (k === 0 ? 0.25 : 1.3 + 5.9 * Math.pow((k - 1) / (N - 2), 0.8)));
const DAY = [1.5, 6.0];
const OUT_OF_ORDER = 6.0;
const ARM_DROP = [6.2, 6.5];
const TEASE = [3.25, 3.55]; // the display flickers to "1" and back
const TO_DOOR = [7.45, 7.9];
const DOOR_OPEN = [8.0, 8.35];
const SWITCH = 9.6;
const CASCADE = [9.75, 10.55];
const G_LOOK = 10.3;
const G_TURN = [10.55, 10.8];
const G_PICK = [10.85, 11.15];
const G_WALK = [11.15, 11.55];
const G_FOOT = [11.55, 11.75];
const TYPE_LINE_AT = 10.0;
const JABS = [0.15, 0.45, 0.75, 1.05, 4.25, 4.5, 6.05];
const DOOR_Y = FLOOR_Y + TOP_H;
const JAB = { ...STAND, lean: 0.12, head: 0.12, shR: 1.5, elR: 0.05, shL: 0.1, elL: 0.2 };
const WATCH = { ...STAND, head: 0.45, shL: 1.15, elL: 1.85, shR: 0.1, elR: 0.2 };
const WAIT = { ...STAND, head: -0.25, shL: 0.35, elL: 1.6, shR: 0.35, elR: 1.6, ab: -0.1 };
const SLUMP = mixPose(STAND, HUNCH, 0.55);
const SWITCH_P = { ...STAND, head: 0.1, shR: 1.55, elR: 0.3 };
const INVITE = { ...STAND, head: 0.35, shR: 1.1, elR: 0.25, shL: 0.15, elL: 0.2, ab: 0.3 };
const FOOT_UP = { ...STAND, lean: 0.1, head: 0.2, thR: 0.75, knR: -0.95, shL: 0.25, elL: 0.3, shR: -0.2, elR: 0.3 };
const LINE2 = "Take the stairs.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · the building · the steps · figures · HTML · frame.

Functions:
- `add(m, x, y, z)`
- `makeGlow(size, color)`
- `drawSteps(t)`: the flights' side rails, which go up with the steps
- `standPos(k)`: which piece blue is standing on, and how far through stepping onto the next one
- `poseBlue(t)`
- `poseGrey(t)`
- `drawProps(t)`
- `dayAt(t)`
- `drawCount(t)`
- `pin(el, v, opacity, dy = 0)`
- `drawChips(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Lift as one premixed, motion-synced track. Timing mirrors scene.js: every step blue sets down (a thud and a rising blip, getting faster) and every step up onto it; grey's button jabs, the watch, the suitcase, the phone scroll, the "1" that almost dings, the foot tapping, OUT OF ORDER; blue's door; the switch and the light running down every step; grey's walk to the first one. Blue sits left in the stereo field, grey right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `counter_blip`, `floor_step`, `rung_tick`, `soft_thud`, `wheel_rumble`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `error`, `pop`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-short`.
It still has an `--alt` flag from the old A/B end line. Leave it off, since the rule is one version only.

Rebuild: `cd videos/the-lift && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-lift/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/lift
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-lift && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-lift   # run in the background
```
`render.sh` writes `renders/13learns-lift.mp4`. The file already delivered is `renders/13learns-the-lift.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
