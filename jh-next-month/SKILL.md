---
name: jh-next-month
description: "13learns Job haters video \"Next Month\" (\"This month was the one.\", phone-screen format). A phone held in two white 3D hands, a calendar app on month view. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawNotes, drawCalendar, drawHands, drawLine2)."
---

# Next Month: "This month was the one." (13learns Job haters)

- **Project:** `videos/the-next-month/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 11s, seamless loop, no VO)
- **Script:** `SCRIPTS-4.md` §5
- **Delivered:** `renders/13learns-next-month.mp4` (rendered)
- **Old A/B file:** `renders/13learns-next-month-alt.mp4`. It predates the one-version rule. Don't make new `-alt` renders.
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Next Month: a phone held in two white 3D hands, a calendar app on month view. "Start my own thing" keeps getting dragged to the 1st of next month, faster and faster, each drop adding an excuse to the event card, until the calendar flips to January 2027 and the card resets. The finger hovers to drag again, stops, taps "Today" instead, drops the event on today and starts it. The phone and the app are HTML under the canvas; only the hands are 3D, so they sit on the screen.

## The script (as written)

**Pattern used:** a phone as the whole stage with an escalating list (alarm series); comment bait in the caption. Flat UI, so this is the cheapest build in the batch.
**Frame line (top):** ME, EVERY MONTH
**A/B line 2:** WHICH MONTH ARE YOU ON?
**Labels:** none; the jokes are the event notes
**Props:** two white stick hands holding a dark phone, a calendar app open on month view; a single event chip "Start my own thing" that keeps getting dragged forward
**Length:** 11s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.0s | Hook: the drag | The thumb is already dragging "Start my own thing" off January 1. | ME, EVERY MONTH · Jan · "New year, new me" | swipe whoosh |
| 1.0–6.5s | The excuses | It lands on February, then gets dragged again, faster and faster: each drop adds a note under the title. Feb "after payday", Mar "when work calms down", May "after my holiday", Jul "too hot", Sep "after the bonus", Nov "busy season", Dec "January. For real." | each month name + its note | a click per drop, speeding up |
| 6.5–7.5s | The turn | The calendar flips to the next year and the chip sits on January 1 again with the same note: "New year, new me". The thumb hovers to drag again. | 2027 · "New year, new me" | page flip, error tone |
| 7.5–9.0s | Today | The thumb stops, taps "Today" instead, and drops the chip on today's date. It turns blue and the title changes to "Started". | Today · Started (blue) | tap, pop, chime |
| 9.0–11s | Payoff | Line 2 types in above the phone. Dip, loop. | ME, EVERY MONTH / THIS MONTH WAS THE ONE. | typing, sparkle |

**Post caption:** "Next month" has been the plan since last January. Which month did you get to before you dragged it again?
**Loop point:** the year resets to January and the thumb grabs the chip.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Me, every month"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "This month was the one."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 11;
const SCREEN = { x: 248, y: 318, w: 584 };
const GRID = { x: 22, y: 210, cw: 540 / 7, ch: 80 };
const TODAY_BTN = { x: 584 - 26 - 50, y: 82 + 10 + 22 };
const EDGE_X = SCREEN.w - 10;
const NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const VIEWS = [
const THIS_MONTH = { label: "This month", year: "", offset: 2, days: 30, day: 17, today: 17 };
const DURS = [1.0, 0.95, 0.85, 0.78, 0.7, 0.62, 0.56, 1.0];
const STARTS = [];
const HOVER = [6.6, 7.3];
const TO_TODAY = [7.3, 7.65];
const TAP_TODAY = 7.72;
const JUMP = [7.8, 8.15];
const CHIP_FLY = [8.15, 8.45];
const TO_CELL = [8.15, 8.5];
const STARTED = 8.62;
const REST = [9.0, 9.5];
const TYPE_LINE_AT = 9.15;
const R = { fist: limb(0.42), finger: limb(0.13, 0.5), thumb: limb(0.12, 0.3), arm: forearmMesh(0.22, 0.27), curl: [0, 1, 2].map(() => limb(0.105, ...
const L = { fist: limb(0.42), thumb: limb(0.12, 0.4), arm: forearmMesh(0.23, 0.28), curl: [0, 1, 2].map(() => limb(0.105, 0.16)) };
const LINE2 = "This month was the one.";
const TYPE_SECS = 0.041 * LINE2.length;
```

## How `scene.js` is built

Sections, in order: layout (px, #root space) · the year of excuses · story beats · calendar DOM · the hands (3D, over the phone) · line 2 · frame.

Functions:
- `cellPos(view, day)`
- `cycleAt(t)`: which cycle we're in and how far through it
- `stateAt(t)`: the state of the whole screen at time t
- `fillPage(el, view)`
- `drawNotes(t)`
- `drawCalendar(t, s)`
- `limb(r, len, rTop = r)`
- `forearmMesh(rA, rB)`
- `aim(mesh, from, dir, len)`
- `pxToWorld(x, y, z = 0)`
- `drawHands(t, s, bob)`
- `drawLine2(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Next Month as one premixed, motion-synced track. Timing mirrors scene.js: every drag cycle (press, drag, page slide, drop with a haptic tick), speeding up month by month; the flip to 2027 with its error tone; the hesitation; the tap on "Today", the jump back to this month, the event flying onto today and the tap that starts it. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `rung_tick`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `error`, `glitch-3`, `pop`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-air-02`, `whoosh-short`.
It still has an `--alt` flag from the old A/B end line. Leave it off, since the rule is one version only.

Rebuild: `cd videos/the-next-month && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-next-month/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/next-month
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-next-month && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-next-month   # run in the background
```
`render.sh` writes `renders/13learns-next-month.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
