---
name: jh-notice
description: "13learns Job haters video \"The Notice\" (\"Same layoff. Different morning.\"). Two identical rooms, one above the other, one shared countdown to the layoffs. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeRoom, drawCups, drawRooms, drawCountdown)."
---

# The Notice: "Same layoff. Different morning." (13learns Job haters)

- **Project:** `videos/the-notice/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-3.md` §3
- **Delivered:** `renders/Posted/13learns-the-notice.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Notice: two identical rooms, one above the other, one shared countdown to the layoffs. Top (blue) gets ready the whole month; bottom (grey) watches TV until a 3 AM panic. At 0 days the same envelope slides under both doors: blue walks out through a door marked DAY 1, grey sits down.

## The script (as written)

**Pattern used:** top/bottom split with one shared countdown (doom pile, 783K; "Same deadline", 17.2M)
**Frame line (centre, between the two halves):** SAME LAYOFF.
**Labels:** top half: Ready · bottom half: Not ready
**Shared timer (centre):** "Layoffs in 30 days" counting down to 0
**Props:** two identical small apartments stacked; each has a desk, a laptop and a door; an envelope slides under each door at 0
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: the rumour | Both halves: a phone buzzes with "Layoffs soon?" Top (blue) calmly opens a laptop. Bottom (grey) shrugs and turns on the TV. | SAME LAYOFF. · 30 days | phone buzz ×2, TV click |
| 2.0–6.0s | The month | Days tick down fast. Top: blue updates a portfolio, a side-income ticker grows, he makes a call. Bottom: grey binges, then at day 5 panics, typing a CV at 3 AM, coffee cups piling up. | 30 → 1 days · top ticker $0 → $2,400/mo | timer ticks, keyboard (top steady, bottom frantic) |
| 6.0–7.0s | The turn | Day 0: an envelope slides under both doors at the same instant. | 0 days · "NOTICE" on both envelopes | envelope swish ×2, bass hit |
| 7.0–9.5s | Two mornings | Top: blue reads it, nods, and walks out through a second door that glows blue, marked "Day 1". Bottom: grey opens his envelope, sits on the floor, and the coffee-cup pile topples. | Ready · Not ready | paper rustle, cup clatter |
| 9.5–12s | Payoff | "DIFFERENT MORNING." types in under "SAME LAYOFF." Dip, loop. | SAME LAYOFF. / DIFFERENT MORNING. | key presses, sparkle |

**Post caption:** You can't control the layoff. You can control what the month before it looked like.
**Loop point:** both phones buzzing.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same layoff."
- Label `#lbl-emp` (`index.html`): "Not ready"
- Label `#lbl-own` (`index.html`): "Ready"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const TOP_F = 1.38;
const BOT_F = -3.66;
const SEAT_X = -2.05;
const DESK_X = SEAT_X + 0.86;
const DESK_TOP = 0.86; // above the room floor
const FIG_Z = -0.6;
const DOOR_X = 1.95;
const BLUE_DOOR_X = 3.25;
const WALL_Z = -1.5;
const BUZZ = [0.3, 1.4];
const LID_TOP = [0.9, 1.2];
const CALL = [4.2, 5.0];
const TV_ON = 1.2;
const PANIC = 4.5;
const LID_BOT = [4.5, 4.7];
const CUPS = [4.7, 5.9];
const ZERO = 6.0;
const ENV_SLIDE = [6.0, 6.35];
const TOP_STAND = [6.4, 6.8];
const TOP_WALK = [6.8, 7.3];
const TOP_PICK = [7.3, 7.5];
const TOP_READ = [7.5, 8.0];
const TOP_NOD = 7.85;
const BLUE_DOOR_UP = 7.3;
const TOP_EXIT = [8.0, 8.6];
const TOP_IN = [8.6, 9.0];
const BOT_STAND = [6.5, 6.9];
const BOT_WALK = [6.9, 7.4];
const BOT_PICK = [7.4, 7.6];
const BOT_READ = [7.6, 8.0];
const BOT_SIT = [8.0, 8.5];
const TOPPLE = 8.3;
const TYPE_LINE_AT = 9.6;
const REST = { ...CHAIR_SIT, lean: 0.12, shL: 0.75, elL: 0.75, shR: 0.7, elR: 0.8 };
const GLANCE = { ...REST, head: 0.55, lean: 0.25 };
const TYPE = { ...CHAIR_SIT, lean: 0.24, head: 0.28, shL: 0.85, elL: 0.95, shR: 0.85, elR: 0.95 };
const CALL_P = { ...TYPE, head: 0.05, shR: 0.35, elR: 2.6 };
const SHRUG_SIT = { ...CHAIR_SIT, head: 0.12, shL: 0.25, elL: 1.35, shR: 0.25, elR: 1.35, ab: 0.4, eab: -0.35 };
const PANIC_TYPE = { ...TYPE, lean: 0.45, head: 0.15 };
const READ = { ...STAND, head: 0.45, lean: 0.1, shL: 0.85, elL: 1.1, shR: 0.85, elR: 1.1 };
const PICK = { ...STAND, lean: 0.9, head: 0.5, thL: 0.7, knL: -0.9, thR: 0.4, knR: -0.7, shL: 1.2, elL: 0.2, shR: 1.2, elR: 0.2 };
const SLUMP = { ...SIT, head: 0.65, lean: 0.75, shL: 0.6, elL: 0.9, shR: 0.55, elR: 0.9 };
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · a room (built twice) · figures · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `makeRoom(f, wallMat)`: a room (built twice)
- `drawCups(t)`
- `setLid(r, open)`
- `buzz(r, t)`
- `envelope(r, t, pickAt, dropAt, holdFig)`
- `poseBlue(t)`
- `poseGrey(t)`
- `drawRooms(t)`
- `days(t)`
- `drawCountdown(t)`
- `pin(el, v, opacity, dy = 0, scale = 1)`
- `popIn(t, at, out)`
- `drawChips(t)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Notice as one premixed, motion-synced track. Timing mirrors scene.js (both phones buzzing, blue's calm typing and call, grey's TV and the 3 AM panic with its coffee cups, the countdown, both envelopes landing at once, the stand-ups and walks, blue's door and grey's slump with the cups toppling), so every sound lands on its frame. The countdown ticks come from the same curve the scene uses. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `floor_step`, `glass_tink`, `rung_tick`, `soft_thud`, `stone_crackle`, `water_flow`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `error`, `glitch-3`, `notification`, `pop`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-notice && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-notice/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/notice
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-notice && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-notice   # run in the background
```
`render.sh` writes `renders/13learns-notice.mp4`. The file already delivered is `renders/Posted/13learns-the-notice.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
