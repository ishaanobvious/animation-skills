---
name: jh-day-30
description: "13learns Job haters video \"Day 30\" (\"Same notice. Different landing.\"). Both figures hand in the same 30 days' notice. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawWeather, drawDesks, drawCalendar, drawLine2)."
---

# Day 30: "Same notice. Different landing." (13learns Job haters)

- **Project:** `videos/day-30/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 13s, seamless loop, no VO)
- **Script:** `SCRIPTS-6.md` §3
- **Delivered:** `renders/13learns-day-30.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Day 30: both figures hand in the same 30 days' notice. A tear-off calendar between their desks counts down. Grey scrolls his phone and a cloud over his head grows darker every day; blue works on his laptop and his side thing grows ("First client", "$400/mo", "$1,200/mo"). Last day: both stand with a box and get the same RESIGNED stamp. Then the desks go dark, grey's cloud bursts into rain ("Income: $0") and blue stands in the light ("Income: $1,200/mo"). Blue walks over and opens a blue umbrella over him.

## The script (as written)

**Pattern used:** same result, different cost (#29, "Procrastinator / Planner"), with a tear-off calendar and a weather cloud as the cost meter
**Frame line (top):** SAME 30 DAYS' NOTICE. (line 2 at the payoff, in blue: DIFFERENT LANDING.)
**Labels:** left: Quit first · right: Built first
**Shared prop:** a tear-off calendar between the desks: "30 days left" → "LAST DAY"
**Props:** two desks. Over grey, a small cloud grows each day. Over blue, small chips pop as his side thing grows ("First client", "$400/mo", "$1,200/mo").
**Length:** 13s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.0s | Hook: notice handed in | Both slap a letter on the desk at 0.0s. The calendar reads 30. | SAME 30 DAYS' NOTICE. · 30 days left | paper slap ×2 |
| 1.0–6.5s | The month | Pages tear off faster and faster. Grey scrolls his phone and the cloud over him grows darker. Blue works on his laptop and chips pop over him. | 29 → 2 days left · First client · $400/mo · $1,200/mo | page tears, pops, a low rumble growing |
| 6.5–8.0s | Same result | LAST DAY. Both stand with a box of desk things and a "RESIGNED" stamp lands over each. | LAST DAY · RESIGNED / RESIGNED | stamp ×2, bass hit |
| 8.0–10s | Different landing | The desks go dark. Grey's cloud bursts into rain over him: "Income: $0". Blue stands in the light: "Income: $1,200/mo". | Income: $0 / Income: $1,200/mo | thunder, rain |
| 10–13s | Kind payoff | Blue walks over and opens a blue umbrella over grey. The rain stops on it. Line 2 types in. Dip, loop. | SAME 30 DAYS' NOTICE. / DIFFERENT LANDING. | umbrella whoosh, rain on fabric, typing, sparkle |

**Post caption:** Two people hand in the same notice. One spent the month building somewhere to land. Start before you leave, not after.
**Loop point:** both slapping a notice letter on the desk.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same 30 days’ notice."
- Label `#lbl-emp` (`index.html`): "Quit first"
- Label `#lbl-own` (`index.html`): "Built first"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#chip-a` "First client" (light), `#chip-b` "$400/mo" (light), `#chip-c` "$1,200/mo" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Different landing."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 13;
const DESK_H = 0.77;
const SEAT_H = 0.44;
const G_SEAT = { x: -1.15, z: 0 };
const B_SEAT = { x: 1.15, z: 0 };
const G_YAW = Math.PI - 0.35;
const B_YAW = 0.35;
const G_STAND = { x: -1.1, z: 0.42, yaw: G_YAW + 1.62 }; // turned toward us
const B_STAND = { x: 1.1, z: 0.42, yaw: B_YAW - 1.62 };
const B_UMB_AT = { x: -0.42, z: 0.55 };
const SLAP = [0.0, 0.35];
const TEARS = Array.from({ length: 29 }, (_, k) => 1.0 + 5.3 * Math.pow((k + 1) / 29, 0.75)); // day 30 → 1
const LAST_DAY = 6.55;
const STAND_UP = [6.6, 7.05];
const STAMP = 7.15;
const DARK = 8.0;
const BURST = 8.05;
const B_DROP = [9.3, 9.6];
const B_WALK = [9.6, 10.45];
const UMB_OPEN = [10.45, 10.8];
const G_LOOK = 10.9;
const TYPE_LINE_AT = 10.6;
const CHIPS = [2.6, 4.0, 5.4];
const DROPS = 70;
const LEGS = { thL: 1.57, knL: -1.57, thR: 1.5, knR: -1.5 };
const CARRY = { ...STAND, head: -0.05, shL: 0.75, elL: 1.05, shR: 0.75, elR: 1.05 };
const CARRY_SAD = { ...HUNCH, lean: 0.45, head: -0.55, shL: 0.75, elL: 1.05, shR: 0.75, elR: 1.05 };
const HOLD_UMB = { ...STAND, lean: -0.05, head: 0.1, shR: 2.5, elR: 0.25, shL: 0.1, elL: 0.2 };
const LINE2 = "Different landing.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials & helpers · the cloud and its rain · figures, phone, boxes · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `screenTex(draw)`
- `makeStation(seat, yaw, tex, glowColor)`: one desk, its monitor and its swivel chair (as in the-battery)
- `cloudAt(t)`
- `drawWeather(t)`
- `seated(fig, st, seat, yaw, pose)`
- `standUp(fig, st, seat, yaw, to, base, t, carry)`
- `poseGrey(t)`
- `poseBlue(t)`
- `placeBox(bx, fig, seat, yaw, t, onFloor = false)`
- `drawDesks(t)`
- `setPage(el, days)`
- `drawCalendar(t)`
- `pinAt(el, v, opacity, transform)`
- `drawHud(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Day 30 as one premixed, motion-synced track. Timing mirrors scene.js: both notices slapped down at 0.0, a page tear for every day (faster and faster), grey's thumb scrolling under a growing rumble, a pop for each of blue's chips over his typing, the LAST DAY page, chairs back and two RESIGNED stamps; the desks going dark, thunder and rain over grey, blue's box set down, his walk over and the umbrella opening, rain drumming on it. Grey sits left in the stereo field, blue right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `air_whoosh`, `floor_step`, `quake_rumble`, `soft_thud`, `water_trickle`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `ping`, `pop`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/day-30 && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/day-30/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/day-30
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/day-30 && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh day-30   # run in the background
```
`render.sh` writes `renders/13learns-day-30.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
