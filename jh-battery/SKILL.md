---
name: jh-battery
description: "13learns Job haters video \"The Battery\" (\"Same 40 hours.\"). Two desks, back to back. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawCable, drawProps, drawBattery, drawLine2)."
---

# The Battery: "Same 40 hours." (13learns Job haters)

- **Project:** `videos/the-battery/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-5.md` §2
- **Delivered:** `renders/13learns-the-battery.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Battery: two desks, back to back. Grey types at "work you dread" and a phone-style battery over his head drains every week, recharging a little less each weekend ("Battery health" 100% → 61%). Blue types at "work you chose" and his battery charges while he works. Week 52, Wednesday: grey hits 1%, a Low Battery alert pops and his head drops onto the desk. Blue stands, pulls the blue cable from his own desk, walks over and holds out the plug. Grey takes it and charges.

## The script (as written)

**Pattern used:** two labels, side by side; a phone-literate joke ("battery health")
**Frame line (top):** SAME 40 HOURS. (line 2 at the payoff: ONE DRAINS YOU. ONE CHARGES YOU.)
**Labels:** left: Work you dread · right: Work you chose
**Ticker:** Mon → Fri, Week 1 → 52, with a phone-style battery icon over each head and "Battery health" under grey's
**Props:** two desks side by side, each with a monitor and chair. Grey's monitor is cold white and blue's glows blue.
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.5s | Hook: Monday | Both sit down and start typing at 0.0s. Grey's battery drops fast: 100 → 80. Blue's shows a charging bolt and ticks up. | SAME 40 HOURS. · Mon · Week 1 | chair, typing, a low-battery blip |
| 1.5–6.0s | The weeks | The week flips Mon→Fri over and over, faster each time. Every Friday grey hits ~10% and slumps; each weekend he only charges back to 90, 80, 70… "Battery health 100% → 61%". Blue types upright and his battery stays high. | Week 1 → 40 · Battery health 61% | typing bed, a blip each Friday, ticks |
| 6.0–7.0s | The turn | Week 52, Wednesday: grey's battery hits 1% and a "Low Battery" alert pops over him. He drops his head onto the desk. | Low Battery · 1% remaining | error tone, bass hit |
| 7.0–9.5s | The plug | Blue stands, takes a blue cable from his own desk, walks over and holds out the plug. | (no new text) | steps, cable whip |
| 9.5–12s | Kind payoff | Grey takes it and plugs in. His icon shows a blue bolt and climbs: 1 → 20%. He sits up. Line 2 types in. Dip, loop. | SAME 40 HOURS. / ONE DRAINS YOU. ONE CHARGES YOU. | plug click, charging chime, typing, sparkle |

**Post caption:** Same 40 hours either way. Some work drains you and some charges you. What's your battery health right now?
**Loop point:** both figures sitting down to type on Monday.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same 40 hours."
- Label `#lbl-emp` (`index.html`): "Work you dread"
- Label `#lbl-own` (`index.html`): "Work you chose"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "One drains you. One charges you."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const DESK_H = 0.77;
const SEAT_H = 0.44;
const G_SEAT = { x: -1.15, z: 0 };
const B_SEAT = { x: 1.15, z: 0 };
const G_YAW = Math.PI - 0.35;
const B_YAW = 0.35;
const B_STAND_AT = { x: 1.4, z: 0.2 };
const B_GIVE_AT = { x: -1.72, z: 0.72 };
const G_TO_BLUE = Math.atan2(-(B_GIVE_AT.z - G_SEAT.z), B_GIVE_AT.x - G_SEAT.x) + 2 * Math.PI; // swivels the short way
const B_TO_GREY = Math.atan2(-(G_SEAT.z - B_GIVE_AT.z), G_SEAT.x - B_GIVE_AT.x);
const CYCLES = [
const WORK = 0.7; // fraction of each cycle that is Mon–Fri
const FRI_LOW = 9;
const LAST_WEEK = 5.0; // Week 52 starts
const DAY_LEN = 0.43;
const EMPTY = 6.3; // 1%, the alert
const HEAD_DOWN = [6.35, 6.75];
const B_GLANCE = [6.45, 6.85];
const B_UP = [7.0, 7.3];
const B_GRAB = [7.22, 7.48];
const B_WALK = [7.5, 8.8];
const B_TURN = [8.8, 9.05];
const B_OFFER = [9.05, 9.35];
const G_LIFT = [9.35, 9.75];
const G_TAKE = [9.7, 9.95];
const HANDOFF = 9.95;
const CHARGE = [10.05, 11.2];
const TYPE_LINE_AT = 10.0;
const DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"];
const LEGS = { thL: 1.57, knL: -1.57, thR: 1.5, knR: -1.5 };
const REACH_DESK = { ...STAND, lean: 0.55, head: -0.2, shR: 1.4, elR: 0.1, shL: 0.2, elL: 0.3 };
const OFFER = { ...STAND, lean: 0.12, head: -0.15, shR: 1.3, elR: 0.12, shL: 0.1, elL: 0.25 };
const LINE2 = "One drains you. One charges you.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: layout · the weeks · materials & helpers · figures · HTML · frame.

Functions:
- `cycleAt(t)`
- `greyAt(t)`: grey's battery, health and day at time t
- `makeGlow(size, color)`
- `screenTex(draw)`: a monitor screen drawn once onto a canvas
- `makeStation(seat, yaw, tex, glowColor)`: one desk, its monitor and its swivel chair for a seat that faces `yaw`
- `drawCable(end, visible)`
- `typing(pose, amp, t, seed = 0)`: typing jitter: two hands, slightly different speeds
- `poseGrey(t, g)`
- `poseBlue(t)`
- `drawProps(t, g)`
- `drawBattery(el, pct, { bolt = 0, low = false, opacity = 1 })`
- `pinAbove(el, fig, y, dx = 0)`
- `drawHud(t, g)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Battery as one premixed, motion-synced track. Timing mirrors scene.js: both figures typing, a low-battery blip each time grey's week bottoms out on Friday, a tick for each new week, the 1% alert and grey's head on the desk; blue's chair, the cable off his desk, his walk across, the plug changing hands and grey's battery charging. Grey sits left in the stereo field, blue right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `counter_blip`, `floor_step`, `rung_tick`, `soft_thud`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `error`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-short`.

Rebuild: `cd videos/the-battery && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-battery/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/battery
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-battery && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-battery   # run in the background
```
`render.sh` writes `renders/13learns-battery.mp4`. The file already delivered is `renders/13learns-the-battery.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
