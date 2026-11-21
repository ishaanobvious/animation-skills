---
name: jh-deal
description: "13learns Job haters video \"The Deal\" (\"Same 9 to 5. Worse deal.\"). 1926 on top, 2026 below, one clock on the seam. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeMachine, makeLaptop, drawBook, drawOffice)."
---

# The Deal: "Same 9 to 5. Worse deal." (13learns Job haters)

- **Project:** `videos/the-deal/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 14s, seamless loop, no VO)
- **Script:** `SCRIPTS-4.md` §2
- **Delivered:** `renders/13learns-the-deal.mp4` (rendered)
- **Old A/B file:** `renders/13learns-the-deal-alt.mp4`. It predates the one-version rule. Don't make new `-alt` renders.
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Deal: 1926 on top, 2026 below, one clock on the seam. Both clock in at 9:00 AM and work the same beat until 5 PM; the clock turns into years and both grow old at it. At Year 40 the 1926 worker gets a pension and the floor claps; the 2026 worker gets a restructuring email and his chair rolls away. Then everything rewinds to 5:01 PM, Year 1: 1926 clocks out and goes home, 2026 closes the work laptop and opens his own, and turns blue.

## The script (as written)

**Pattern used:** then vs now split ("1760 / 2026", 730K day one); one shared clock on the seam
**Frame line (seam, between the halves):** SAME 9 TO 5.
**A/B line 2:** 100 YEARS LATER, STILL CLOCKING IN.
**Labels:** top corner "1926" · bottom corner "2026"
**Shared clock (seam):** 9:00 AM → 5:00 PM, then a year counter for the retirement beat
**Props:** top: a cool-grey factory floor, a punch clock, a lever machine, a foreman in a hat; bottom: a dark office desk, a laptop, a webcam light, a manager on a video tile. Both figures grey to start.
**Length:** 14s (the era-split reel held 17s, so this one can run long)

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.5s | Hook: clock in | Both clock in at the same instant: top punches a card, bottom clicks a green "Online" dot. The seam clock reads 9:00 AM. | 1926 · 2026 · 9:00 AM | punch-clock clunk, click |
| 1.5–5.0s | The same day | The clock spins to 5 PM. Top pulls a lever in a steady rhythm while the foreman watches. Bottom clicks in the same rhythm while the manager's video tile watches. Their motions match beat for beat. | SAME 9 TO 5. · 9 AM → 5 PM | lever clank / mouse click alternating, clock ticks |
| 5.0–7.0s | The years | The clock flips to a year counter, Year 1 → 40, as both figures hunch over. | Year 1 → 40 | fast ticks, riser |
| 7.0–9.0s | The turn: the deal | Year 40. Top: the foreman hands over a pension book and a house key; a small crowd claps. Bottom: an email pops: "Restructuring. Pension: N/A." His chair rolls away. | PENSION ✓ · PENSION: N/A | applause (top), error tone + bass hit (bottom) |
| 9.0–11.5s | Write a new one | Rewind to bottom at 5:01 PM, Year 1. The 2026 figure closes the work laptop and opens a second one. Its screen glows blue ("My thing"), and he turns blue. | 5:01 PM (blue) · Year 1 | rewind whoosh, lid click, chime |
| 11.5–14s | Payoff | Line 2 types in under the frame line. The top half stays cool grey; the bottom half now glows blue. Dip, loop. | SAME 9 TO 5. / WORSE DEAL. | typing, sparkle |

**Post caption:** The 9 to 5 used to come with a pension and a house. Now it comes with a laptop and a restructuring email. Same hours, worse deal, so build something that's yours after 5.
**Loop point:** both figures reaching to clock in at 9:00.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same 9 to 5."
- Label `#lbl-top` (`index.html`): "1926"
- Label `#lbl-bot` (`index.html`): "2026"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#online` "Online" (light), `#pension` "PENSION ✓" (light), `#house` "HOUSE KEY ✓" (light), `#email` "Restructuring.Pension: N/A" (light), `#live` "Manager · Live" (light), `#mything` "My thing" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Worse deal."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 14;
const TOP_F = 1.38;
const BOT_F = -3.66;
const WALL_Z = -1.5;
const CLOCK_X = -3.15;
const PUNCH_Z = -0.95;
const MACH_X = -0.5;
const WORK_X = -1.75;
const WORK_Z = -0.55;
const EXIT_X = -2.2;
const BG_MACH = [1.9, 3.4];
const BG_Z = -1.15;
const FORE0 = [0.05, 0.0];
const FORE1 = [-0.85, 0.1];
const SEAT_X = -2.05;
const DESK_X = SEAT_X + 0.86;
const DESK_TOP = 0.86;
const FIG_Z = -0.6;
const SCREEN = { x: 0.75, y: BOT_F + 1.8, w: 1.5, h: 0.86 };
const PUNCH = 0.3;
const TO_LEVER = [0.45, 1.3];
const DAY = [1.5, 5.0];
const BEAT = 0.5; // one lever pull, one click
const YEARS = [5.15, 7.0];
const FORE_WALK = [7.0, 7.45];
const HAND_OVER = [7.45, 7.8];
const PENSION_AT = 7.65;
const HOUSE_AT = 7.95;
const CLAP = [7.75, 8.85];
const EMAIL_AT = 7.2;
const CHAIR_ROLL = [7.6, 8.0];
const DROP = [7.8, 8.05];
const REWIND = [9.0, 9.7];
const BRANCH = 9.7;
const T_RELEASE = [9.75, 9.95];
const T_TO_CLOCK = [9.95, 10.6];
const PUNCH_OUT = 10.7;
const T_TO_DOOR = [10.85, 11.45];
const LIGHTS_DOWN = 11.35;
const LID_CLOSE = [9.8, 10.05];
const SWAP = [10.05, 10.4];
const LID2_OPEN = [10.4, 10.7];
const TURN_BLUE = [10.6, 11.1];
const TYPE_LINE_AT = 11.6;
const PUNCH_P = { ...STAND, lean: 0.08, head: 0.1, shR: 1.5, elR: 0.1, shL: 0.2, elL: 0.2 };
```

## How `scene.js` is built

Sections, in order: layout · story beats (story time: rewinds with the clock) · materials · 1926: the factory · 2026: the home office · figures · poses · HTML · frame.

Functions:
- `storyT(t)`
- `beat(st)`: lever down / click: 0..1 on the shared beat
- `add(m, x, y, z)`
- `makeGlow(size, color)`
- `shell(f, wallMat, floorMat)`
- `makeMachine(x, z, w = 0.9, h = 1.2, d = 0.7)`: a lever machine; returns its lever pivot
- `makeLaptop(mat, screenColor, w = 0.34, d = 0.46)`
- `addCap(fig, foreman = false)`: figures
- `leverTo(pivot, fig, grip)`
- `poseOld(t, st)`
- `oldBranch(t)`
- `greyFadeTop(st)`
- `poseBg(t, st)`
- `poseForeman(t, st)`
- `drawBook(t, st)`
- `poseNow(t, st)`
- `nowBranch(t, br)`
- `drawOffice(t, st)`
- `drawFactory(t, st)`
- `fmtTime(min)`
- `drawClock(t, st)`
- `pin(el, v, opacity, dy = 0, scale = 1)`
- `popIn(t, at, out)`
- `drawChips(t, st)`
- `drawFilm(t)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Deal as one premixed, motion-synced track. Timing mirrors scene.js: both clock-ins at 9:00, the shared beat (a lever clank in 1926 and a mouse click in 2026 on every pull), the clock and year ticks, Year 40 (the pension, the applause, the email, the chair rolling away), the rewind, and the 5:01 branch (1926 clocks out and leaves, 2026 shuts the work laptop and opens his own). Story events before the rewind use the same story clock as the scene. 1926 sits left in the stereo field, 2026 right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `SR`, `air_whoosh`, `floor_step`, `pipe_clunk`, `soft_thud`, `wheel_rumble`.
`sfx-library/` sounds: `applause-small-01`, `chime`, `clap-01`, `click`, `click-soft`, `error`, `glitch-3`, `notification`, `ping`, `pop`, `riser`, `rumble-wheel-loop`, `sparkle`, `tick-rung-01`, `typing`, `whoosh-short`.
It still has an `--alt` flag from the old A/B end line. Leave it off, since the rule is one version only.

Rebuild: `cd videos/the-deal && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-deal/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/deal
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-deal && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-deal   # run in the background
```
`render.sh` writes `renders/13learns-deal.mp4`. The file already delivered is `renders/13learns-the-deal.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
