---
name: jh-two-years
description: "13learns Job haters video \"Two Years, Max\" (\"Year 12.\"). A young figure sticks \"2 years, max\" on his monitor and sits down. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawDesk, drawNote, drawLine2)."
---

# Two Years, Max: "Year 12." (13learns Job haters)

- **Project:** `videos/the-two-years/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 13s, seamless loop, no VO)
- **Script:** `SCRIPTS-4.md` §4
- **Delivered:** `renders/13learns-two-years-max.mp4` (rendered)
- **Old A/B file:** `renders/13learns-two-years-max-alt.mp4`. It predates the one-version rule. Don't make new `-alt` renders.
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Two Years, Max: a young figure sticks "2 years, max" on his monitor and sits down. The years tick by: the desk fills up, he greys and hunches, the note curls but never comes down. At Year 12 a translucent blue copy of his young self walks in and taps it. He peels the note off, leaves it on the desk, and walks out beside his young self; they merge and he turns blue. Lights off.

## The script (as written)

**Pattern used:** you vs you ("the one who sets the alarms is never the one who has to get up"); a hidden counter revealed
**Frame line (top):** "2 YEARS, MAX." (in quotes, like a promise; line 2 at the payoff: IT'S NOT TOO LATE TO MEAN IT.)
**A/B line 2:** HOW MANY YEARS WAS YOURS?
**Labels:** the young self (blue, slightly translucent): Year 1 you · the desk self (grey): Year 12 you
**Ticker:** Year 1 → 12 on a desk calendar
**Props:** one desk with a monitor; a sticky note on the monitor that says "2 years, max"; the desk slowly clutters (mugs, a lanyard, a plant that grows, a stack of "Employee of the month" frames)
**Length:** 13s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.5s | Hook: the promise | A young, upright figure sticks the note on the monitor and points at it, nodding. | "2 YEARS, MAX." · Year 1 | sticky-note slap, pop |
| 1.5–6.0s | The years | Year ticks 2 → 12. The figure greys and hunches; the desk fills up; the note curls and fades but never comes down. At Year 2 he glances at the note and looks away. At Year 5 a "Promoted!" chip, at Year 8 a mortgage chip. | Year 2 → 12 · Promoted! · Mortgage | calendar flips, typing bed, pops for each chip |
| 6.0–7.5s | The turn: Year 1 you | At Year 12 a translucent blue copy of his young self walks in, stands beside the chair and taps the note. | Year 1 you / Year 12 you | whoosh, tap |
| 7.5–10.5s | He means it | The grey figure looks at the note for a long beat, peels it off, stands, and walks out next to his young self. As they walk they merge, and he turns solid blue. The desk lights go off. | Year 12 (blue) | chair back, steps, merge shimmer, chime |
| 10.5–13s | Payoff | Line 2 types in. The note sits alone on the empty desk. Dip, loop. | "2 YEARS, MAX." / IT'S NOT TOO LATE TO MEAN IT. | typing, sparkle |

**Post caption:** Everyone has a "2 years, max" job. Year 1 you made a promise. Year 12 you still gets to keep it. How many years was yours?
**Loop point:** the empty desk, the young figure reaching in with the note.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "“2 years, max.”"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#promoted` "Promoted!" (light), `#mortgage` "Mortgage" (light), `#lbl-young` "Year 1 you" (light), `#lbl-old` "Year 12 you" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "It’s not too late to mean it."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 13;
const SEAT_X = -0.75;
const DESK_X = SEAT_X + 0.86;
const DESK_TOP = FLOOR_Y + 0.86;
const FIG_Z = -0.2;
const DESK = { w: 0.78, d: 1.2, z: -0.2 };
const MON = { x: DESK_X + 0.26, z: -0.25, yaw: 0.6 };
const STICK_AT = { x: -0.32, z: 0.2 }; // where he stands to stick the note
const EXIT_X = -3.0;
const STICK = 0.32;
const SIT = [1.0, 1.45];
const YEAR_STEP = 0.44;
const GLANCE = [1.85, 2.4];
const PROMOTED = yearAt(5);
const MORTGAGE = yearAt(8);
const COPY_IN = [6.0, 6.8];
const TAP = [6.95, 7.35];
const COPY_TURN = [7.4, 7.7];
const LOOK = [7.35, 8.1];
const PEEL = [8.1, 8.4];
const SET_DOWN = [8.4, 8.7];
const STAND_UP = [8.7, 9.05];
const WALK = [9.15, 10.5];
const MERGE = [9.5, 10.0];
const LIGHTS_OFF = 10.05;
const LABELS = [6.55, 9.3];
const TYPE_LINE_AT = 10.6;
const YEARS = [[0, 1]];
const TYPE = { ...CHAIR_SIT, lean: 0.22, head: 0.3, shL: 0.85, elL: 0.95, shR: 0.85, elR: 0.95 };
const STICK_P = { ...STAND, lean: 0.05, head: -0.15, shR: 1.75, elR: 0.15, shL: 0.1, elL: 0.2 };
const POINT = { ...STAND, head: -0.1, shR: 1.6, elR: 0.05, shL: 0.1, elL: 0.2 };
const LOOK_UP = { ...CHAIR_SIT, lean: 0.12, head: -0.3, shL: 0.6, elL: 0.9, shR: 0.55, elR: 0.9 };
const PEEL_P = { ...CHAIR_SIT, lean: 0.15, head: -0.25, shR: 1.85, elR: 0.2, shL: 0.5, elL: 0.9 };
const SET_P = { ...CHAIR_SIT, lean: 0.35, head: 0.35, shR: 1.1, elR: 0.4, shL: 0.5, elL: 0.9 };
const COME = { ...STAND, head: 0.1, shR: 1.0, elR: 0.6, shL: 0.1, elL: 0.2 };
const LINE2 = "It’s not too late to mean it.";
const TYPE_SECS = 0.041 * LINE2.length;
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · the desk · the years pile up on the desk · figures · HTML · frame.

Functions:
- `add(m, x, y, z)`
- `makeGlow(size, color)`
- `item(mesh, year, x, z, yOff = 0)`
- `drawDesk(t)`
- `poseMe(t)`
- `poseGhost(t)`
- `drawNote(t)`
- `pin(id, v, opacity, scale = 1)`
- `popFor(t, at, life = 0.8)`
- `drawChips(t)`
- `drawLine2(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Two Years, Max as one premixed, motion-synced track. Timing mirrors scene.js: the note slapped onto the monitor, sitting down, the typing bed, a calendar flip per year, each thing that lands on the desk (mugs, the lanyard, the plant, the frames, the papers), "Promoted!" and "Mortgage", Year 12, the young self walking in and tapping the note, the peel, the chair, the walk out, the merge, and the lights going off. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `counter_blip`, `floor_step`, `glass_tink`, `hand_clap`, `rung_tick`, `soft_thud`, `stone_crackle`, `wheel_rumble`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `ping`, `pop`, `rumble-wheel-loop`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-short`.
It still has an `--alt` flag from the old A/B end line. Leave it off, since the rule is one version only.

Rebuild: `cd videos/the-two-years && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-two-years/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/two-years
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-two-years && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-two-years   # run in the background
```
`render.sh` writes `renders/13learns-two-years.mp4`. The file already delivered is `renders/13learns-two-years-max.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
