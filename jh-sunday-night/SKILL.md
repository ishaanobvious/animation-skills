---
name: jh-sunday-night
description: "13learns Job haters video \"Sunday Night\" (single-figure format). One grey figure on the edge of his bed. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawLaptop, drawHands, drawPhone, drawClock)."
---

# Sunday Night: "" (13learns Job haters)

- **Project:** `videos/sunday-night/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 10s, seamless loop, no VO)
- **Script:** `SCRIPTS-2.md` §7
- **Delivered:** `renders/13learns-sunday-night.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Sunday Night: one grey figure on the edge of his bed. Glowing labelled hands push in from the dark one by one as the clock races to midnight; he curls up. The Monday alarm snaps them all away and he stands, flat and grey. Then a laptop at the foot of the bed glows blue — the only blue there is.

## The script (as written)

**Pattern used:** one figure surrounded by labelled forces (the 1.2M 3 AM reel). It's our first video with one character, so we can test whether it lands without the vs.
**On-screen counter:** a clock, Sun 6:00 PM → Mon 7:00 AM
**Label:** You
**Props:** a single grey figure sitting on the edge of a bed. Glowing pointing hands slide in from the dark, one per beat, each labelled: BOSS, COMMUTE, APPRAISAL, EMI, 47 UNREAD, "Monday".
**Length:** 10s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: Sunday 6 PM | The figure is relaxed, phone in hand. The clock reads Sun 6:00 PM. The first hand slides in: BOSS. | Sun 6:00 PM | low drone, slide whoosh |
| 2.0–6.0s | The hands | One hand per beat: COMMUTE, APPRAISAL, EMI, 47 UNREAD. The hands close in, and the figure curls up and grips his head. The clock speeds up. | Sun 8 PM → 11:59 PM | whoosh per hand, drone rises, ticking speeds up |
| 6.0–7.5s | The alarm | Mon 7:00 AM: an alarm rings. All the hands snap back into the dark and the figure stands up, flat and grey. | Mon 7:00 AM | alarm, hard cut silence |
| 7.5–10s | The question | Top text: "What if Sunday felt like Friday?" A small blue light glows on a laptop at the foot of the bed, the only blue in the frame. Dip, loop. | What if Sunday felt like Friday? | soft hum, sparkle |

**Post caption:** If your Sunday night has a dread schedule, the job is costing more than 40 hours a week.
**Loop point:** Sun 6:00 PM, the figure relaxed, no hands.

## On-screen text (where it lives)

- Label `#lbl-emp` (`index.html`): "You"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 10;
const FIG_X = 0.0;
const FIG_Z = 0.05;
const BED_TOP = FLOOR_Y + 0.48;
const HANDS = [
const SLIDE = 0.35;
const ALARM = 6.0;
const SNAP = 0.25;
const STAND_UP = [6.45, 7.0];
const PHONE_DROP = 3.55;
const LAPTOP_OPEN = 7.6;
const LOOK_AT = 8.2;
const TYPE_LINE_AT = 7.75;
const CLOCK = [[0, 1080], [0.9, 1120], [2.1, 1200], [2.9, 1275], [3.7, 1350], [4.5, 1400], [5.3, 1439], [ALARM - 0.01, 1439]];
const PHONE_SIT = { ...SIT_EDGE, lean: 0.22, head: 0.45, shL: 0.45, elL: 1.85, shR: 0.5, elR: 1.8 };
const CURL = { ...SIT_EDGE, lean: 0.75, head: 0.65, shL: 2.75, elL: 2.05, shR: 2.7, elR: 2.0, ab: 0.35, eab: 0.3 };
const JOLT = { ...SIT_EDGE, lean: -0.12, head: -0.25, shL: 0.5, elL: 0.6, shR: 0.5, elR: 0.6, ab: 0.3 };
const FLAT = { ...STAND, lean: 0.12, head: 0.32, shL: 0.05, elL: 0.1, shR: 0.03, elR: 0.1 };
const YAW = -1.15; // three-quarters to camera
const LINE = "What if Sunday\nfelt like Friday?";
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · the bed · phone · the laptop at the foot of the bed · the hands · the figure · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `drawLaptop(t)`
- `handsIn(t)`
- `drawHands(t, headPos)`
- `poseYou(t)`
- `drawPhone(t)`
- `clockMinutes(t)`
- `fmt(min)`
- `drawClock(t)`
- `drawLabels(t, headPos)`
- `drawLine(t)`
- `placeTagAt(id, x, dy)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Sunday Night as one premixed, motion-synced track. Timing mirrors scene.js (each hand sliding in with a notification ping, a heartbeat and clock ticks that speed up toward midnight, the phone dropping, the Monday alarm snapping everything away, the laptop opening), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `counter_blip`, `floor_step`, `rung_tick`, `soft_thud`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `notification`, `riser`, `sparkle`, `typing`, `whoosh`, `whoosh-air-02`.

Rebuild: `cd videos/sunday-night && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/sunday-night/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2,4,6,8,9.6 --no-end --describe false -o <scratchpad>/sunday-night
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/sunday-night && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh sunday-night   # run in the background
```
`render.sh` writes `renders/13learns-sunday-night.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
