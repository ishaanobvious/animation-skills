---
name: jh-lunch-hour
description: "13learns Job haters video \"The Lunch Hour\" (\"Same 1 hour. Different life.\"). Two identical desks, one wall clock stuck on 1:00. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawDoor, makeBadge, drawBlueBadge, drawDay)."
---

# The Lunch Hour: "Same 1 hour. Different life." (13learns Job haters)

- **Project:** `videos/the-lunch-hour/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-2.md` §1
- **Delivered:** `renders/13learns-the-lunch-hour.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Lunch Hour: two identical desks, one wall clock stuck on 1:00. Grey scrolls his phone every lunch break; blue opens his laptop and builds. Days fly by, blue's $0/mo finally jumps, and he leaves his badge on the desk and walks out through a glowing door. Grey keeps scrolling.

## The script (as written)

**Pattern used:** "same X" constraint, small daily habit compounds (the 34M "Same 5 minutes" reel)
**Frame line (top):** SAME 1 HOUR. / DIFFERENT LIFE. (the second line lands at the payoff)
**Labels:** Scrolling / Building
**Small ticker under each label:** Day 1 → 365 · blue's "$0/mo" ticker
**Props:** two identical office desks side by side, a wall clock reading 1:00, a phone (grey), a laptop (blue)
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.0s | Hook: same break | The clock hits 1:00. Both figures push back from identical desks. Grey slumps and thumb-scrolls his phone, and its glow lights his face. Blue opens a laptop and types fast. The clock snaps back to 1:00 with each day. | SAME 1 HOUR. · Day 1 → 60 · $0/mo | clock tick, scroll flicks, keyboard clatter |
| 3.0–5.5s | The grind | Days flip faster. Grey's posture sinks lower. Blue's ticker sits at $0, then $0, then $12. Nothing visible happens yet, and that's the tension. | Day 61 → 180 · $0 → $12/mo | faster ticks, one small coin clink at $12 |
| 5.5–7.0s | The turn | The ticker jumps: $300 → $1,100 → $4,800. Blue's desk lamp turns brand blue. | Day 240 · $4,800/mo (blue) | coin ladder, whoosh |
| 7.0–9.5s | The exit | Blue closes the laptop, stands, sets his ID badge on the desk and walks out of a door that appears at the right edge. Grey is still scrolling. | Day 300 → 365 | badge set down, door open |
| 9.5–12s | Payoff | "DIFFERENT LIFE." types in under the top line. Grey alone, scrolling, clock at 1:00. Dip, loop. | SAME 1 HOUR. / DIFFERENT LIFE. | soft sparkle, door click shut |

**Post caption:** Your lunch break is 250 hours a year. That's a business, a skill, or 250 hours of other people's highlights.
**Loop point:** clock at 1:00, both at their desks, blue's badge back on his chest.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same 1 hour."
- Label `#lbl-emp` (`index.html`): "Scrolling"
- Label `#lbl-own` (`index.html`): "Building"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Different life."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const SEATS = { grey: { x: -2.0, dir: 1 }, blue: { x: 2.0, dir: -1 } };
const DESK_OFF = 0.86; // desk centre, in front of the hip
const DESK_TOP = FLOOR_Y + 0.86;
const DOOR_X = 3.4;
const DOOR_Z = -0.4;
const TURN_AT = 5.6; // income jumps, blue's lamp turns blue
const CLOSE_AT = 6.95; // blue closes the laptop
const STAND_AT = 7.25;
const BADGE_AT = 7.68;
const TURN_AWAY_AT = 8.05;
const WALK_AT = 8.3;
const AT_DOOR = 9.05;
const ENTER_END = 9.55;
const DOOR_UP = 7.6;
const DOOR_OPEN = 8.55;
const DOOR_SHUT = 9.55;
const TYPE_LINE_AT = 9.6;
const CLOCK_R = 0.42;
const DOOR_W = 0.86;
const DOOR_H = 2.12;
const REST = { ...CHAIR_SIT, lean: 0.12, shL: 0.75, elL: 0.75, shR: 0.7, elR: 0.8 };
const TYPE = { ...CHAIR_SIT, lean: 0.24, head: 0.28, shL: 0.85, elL: 0.95, shR: 0.85, elR: 0.95 };
const PHONE = { ...CHAIR_SIT, lean: 0.16, head: 0.42, shL: 0.38, elL: 2.05, shR: 0.44, elR: 2.0 };
const TO_CHEST = { ...STAND, lean: 0.06, shR: 0.35, elR: 2.25 };
const DROP = { ...STAND, lean: 0.32, head: 0.35, shR: 1.15, elR: 0.25 };
const FLICK = 0.42;
const LEN_A = 1.56;
const LEN_B = P2.distanceTo(P3);
const STEP = 0.5; // ground covered per step
const YAW_START = Math.atan2(-(P1.z - P0.z), P1.x - P0.x) + 2 * Math.PI;
const DAYS = [
const MONEY = [[0, "$0"], [4.75, "$12"], [TURN_AT, "$300"], [5.95, "$1,100"], [6.35, "$4,800", true]];
const LINE2 = "Different life.";
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · desk, chair, laptop, lamp (one set per seat) · phone · wall clock, stuck on lunch · the door that appears behind blue · ID badges · figures · counters · lights that tell the story · frame.

Functions:
- `makeGlow(size)`
- `makeStation({ x, dir })`: desk, chair, laptop, lamp (one set per seat)
- `setLid(st, open)`
- `clockHand(len, w, z)`
- `drawDoor(t)`
- `makeBadge()`: ID badges
- `poseGrey(t)`
- `walkState(t)`
- `poseBlue(t)`
- `drawBlueBadge(t)`
- `drawDay(t)`
- `drawMoney(t)`
- `drawClock(t)`: the clock sweeps one lunch hour per day shown, then snaps back to 1:00
- `drawFrameLine(t)`
- `drawStations(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Lunch Hour as one premixed, motion-synced track. Timing mirrors scene.js (day steps, phone flicks, laptop lid, typing, income jumps, badge, walk, door), so every tick, key and coin lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `coin_clink`, `counter_blip`, `floor_step`, `rung_tick`, `soft_thud`, `valve_squeak`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `coin-cascade-01`, `coin-cascade-02`, `key-press`, `ping`, `pop`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-lunch-hour && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-lunch-hour/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/lunch-hour
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-lunch-hour && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-lunch-hour   # run in the background
```
`render.sh` writes `renders/13learns-lunch-hour.mp4`. The file already delivered is `renders/13learns-the-lunch-hour.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
