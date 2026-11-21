---
name: jh-commute
description: "13learns Job haters video \"The Commute\" (\"Same train. Same 2 hours.\"). A train carriage, city lights streaming past the windows. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawLights)."
---

# The Commute: "Same train. Same 2 hours." (13learns Job haters)

- **Project:** `videos/the-commute/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-7.md` §6
- **Delivered:** `renders/13learns-commute.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Commute: a train carriage, city lights streaming past the windows. Two seats, one behind the other, both facing the way the train goes. Grey (behind) thumbs a glowing phone; blue (in front) types on a laptop. A day counter races from "Day 1 · 2 hrs" to "Day 240 · 480 hrs" while chips pop over blue as his thing grows. Then blue turns round and holds the laptop out; grey looks up, the phone goes dark, and he leans in.

## The script (as written)

**Pattern used:** "same X" frame line (#2), same counter, different stat (#20)
**Frame line (top):** SAME TRAIN. SAME 2 HOURS. (line 2 at the payoff, in blue: BUILD SOMETHING ON IT.)
**Labels:** left: Scrolling · right: Building
**Counter chip:** "Day 1 · 2 hrs" → "Day 240 · 480 hrs". Over blue: "Landing page", "First sale", "10 customers", "$2k/mo"
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.0s | Hook | City lights already stream past the windows of a train carriage. Two seats, one behind the other: grey thumbs a glowing phone; blue types on a laptop. | SAME TRAIN. SAME 2 HOURS. · Day 1 · 2 hrs | train rumble |
| 1.0–8.5s | 240 days | The day counter races. Grey's thumb flicks endlessly and he greys and slumps. Chips pop over blue's laptop as his thing grows. | Day 240 · 480 hrs · Landing page · First sale · 10 customers · $2k/mo | rumble, a pop per chip, flicks |
| 8.5–12s | Kind payoff | Blue turns round and holds the laptop out. Grey looks up, the phone goes dark, and he leans in. Line 2 types in. Dip, loop. | SAME TRAIN. SAME 2 HOURS. / BUILD SOMETHING ON IT. | chime, typing, sparkle |

**Post caption:** Two hours a day on a train is 480 hours a year. That's twelve full work weeks. Same seat, same time; what you do with it is the only difference.
**Loop point:** both on the train, day 1.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same train. Same 2 hours."
- Label `#lbl-emp` (`index.html`): "Scrolling"
- Label `#lbl-own` (`index.html`): "Building"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#day` "Day 1 · 2 hrs" (numbers), `#b1` "Landing page" (blue), `#b2` "First sale" (blue), `#b3` "10 customers" (blue), `#b4` "$2k/mo" (blue)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Build something on it."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const SEAT_H = 0.46;
const G_SEAT = -0.85;
const B_SEAT = 0.85;
const WALL_Z = -1.0;
const WIN = { y0: FLOOR_Y + 1.15, y1: FLOOR_Y + 2.05, xs: [-2.2, 0, 2.2], w: 1.7 };
const DAYS = [0.8, 8.4];
const B_CHIPS = [2.3, 4.0, 5.7, 7.4];
const TURN = [8.7, 9.25];
const G_LOOK = [9.25, 9.6];
const PHONE_OFF = [9.4, 9.7];
const LEAN_IN = [9.7, 10.2];
const TYPE_LINE_AT = 10.2;
const LIGHTS = Array.from({ length: 22 }, () => ({ x: lightRand() * 9, y: WIN.y0 + 0.1 + lightRand() * 0.75, s: 0.5 + lightRand() * 0.9, c: lightRa...
const SCROLL = (t, slump) => ({ ...SEATED, lean: 0.2 + 0.25 * slump, head: -0.45 - 0.15 * slump, shR: 0.85, elR: 1.6, shL: 0.75, elL: 1.4, eab: 0.0...
const TYPE = (t) => ({ ...SEATED, lean: 0.15, head: -0.25, shL: 0.75 + 0.05 * Math.sin(t * 23), elL: 0.85, shR: 0.75 + 0.05 * Math.sin(t * 19 + 1),...
const HOLD_OUT = { ...SEATED, lean: 0.05, head: 0.1, shL: 1.2, elL: 0.35, shR: 1.2, elR: 0.35 };
const LEAN = { ...SEATED, lean: 0.55, head: 0.15, shL: 0.55, elL: 0.9, shR: 0.55, elR: 0.9 };
```

## How `scene.js` is built

Sections, in order: layout · story beats · the carriage · phone and laptop · figures · HTML · frame.

Functions:
- `drawLights(t)`
- `seat(fig, pose, x, yaw, t)`
- `poseGrey(t)`
- `poseBlue(t)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Commute as one premixed, motion-synced track. Timing mirrors scene.js: a steady train rumble with a clack on every rail joint (the same bumps that rock the camera), grey's thumb flicking the phone, blue's typing in bursts, the day counter ticking as it races to 240, a pop for each chip over blue, then the turn (a chime), the phone going dark, grey leaning in, and the payoff. Grey sits left in the stereo field, blue right. Owned synths and ../../sfx-library sounds only.

Owned synths: `air_whoosh`, `counter_blip`, `pipe_clunk`, `rung_tick`, `wheel_rumble`.
`sfx-library/` sounds: `chime`, `click-soft`, `ping`, `pop`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-air-02`.

Rebuild: `cd videos/the-commute && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-commute/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/commute
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-commute && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-commute   # run in the background
```
`render.sh` writes `renders/13learns-commute.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
