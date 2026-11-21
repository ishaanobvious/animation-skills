---
name: jh-ceiling
description: "13learns Job haters video \"The Ceiling\" (\"A salary has a ceiling. Ownership doesn't.\"). Grey's salary stack hits a glass \"salary cap\"; blue's stack smashes through it. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeStack, drawStack, makePane, drawGlass)."
---

# The Ceiling: "A salary has a ceiling. Ownership doesn't." (13learns Job haters)

- **Project:** `videos/the-ceiling/` (HyperFrames 0.8.181 + Three.js, 1080×1920, 30fps, 10s, seamless loop, no VO)
- **Script:** `SCRIPTS.md` §2
- **Delivered:** `renders/Posted/13learns-the-ceiling.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Ceiling: grey's salary stack hits a glass "salary cap"; blue's stack smashes through it.

## The script (as written)

**On-screen counter:** Age 25 → 45
**Props:** two coin stacks, a glass slab across the top of the scene tagged "Salary cap", income tickers under each label.

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.0s | Hook: the climb | Coins pop in under both figures. Grey rises steadily. Blue rises unevenly: two coins get knocked out of his stack (a setback) and he drops. Grey is ahead. | Age 25 → 31 · Employee $45k → $65k · Owner $8k → $0 → $14k | coin clinks, blue's coins clatter to the floor |
| 3.0–4.6s | The ceiling | Grey's head bonks the glass. Every new coin is a thin "+3%" one that forces him to crouch lower, palms pressed against the glass. Blue keeps climbing, faster. | Age 31 → 35 · $65k → $71k | glass "tink", strained creak |
| 4.6–5.2s | The turn | Blue reaches the glass, cracks spread from his hands, and his half shatters. "Age 35" flashes blue; "Owner" pops. | Age 35 (blue) | crack, shatter |
| 5.2–8.5s | Two paths | Blue's stack shoots up past the broken glass, coin after coin. Grey stays crouched under his intact half, fading. | Age 36 → 44 · Owner $14k → $1.2M | rapid coin ladder |
| 8.5–10s | Payoff | Age 45: blue stands tall on a tower of coins, shades on. Grey is still pressing on the glass. Dip, loop. | Age 45 (blue) · $80k vs $1.2M | final ching, sparkle |

**Post caption:** Your boss decides your ceiling. Build something where you decide.
**Loop point:** both figures on the floor with no coins; glass whole.

## On-screen text (where it lives)

- Label `#lbl-emp` (`index.html`): "Employee"
- Label `#lbl-own` (`index.html`): "Owner"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const GREY_X = -1.7;
const BLUE_X = 1.7;
const COIN_T = 0.118;
const COIN_PITCH = 0.132;
const GLASS_T = 0.08;
const GLASS_TILT = 0.2; // tipped toward camera so the pane reads as glass, not a line
const GLASS_BOTTOM = FLOOR_Y + 6 * COIN_PITCH + 1.995; // grey's head meets it on his 6th coin
const GLASS_Y = GLASS_BOTTOM + GLASS_T / 2;
const GLASS_W = 4.9;
const GLASS_D = 2.4;
const SHATTER_AT = 4.95;
const CRACKS = 14;
const COLS = 7;
const ROWS = 3;
const PRESS_A = { ...REACH, head: 0.25 };
const SQUASH = { ...CROUCH, shL: -0.5, shR: -0.6 };
const AGES = [];
```

## How `scene.js` is built

Sections, in order: layout · coin stacks · glass ceiling · figures · counters · frame.

Functions:
- `makeStack(x, defs)`
- `stackLayout(st, t)`: newest coin pushes in at the base and lifts the rest; a knocked-out coin stops counting
- `drawStack(st, t)`
- `makePane(x0, x1)`
- `drawGlass(t)`
- `figTop(fig, pose)`
- `fitUnder(fig, arms, gap)`: arms = 0 (hands down) .. 1 (palms on the glass); returns the pose that fits under `gap`
- `poseGrey(t)`
- `poseBlue(t)`
- `drawAge(t)`
- `landed(st, t)`
- `drawMoney(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Ceiling as one premixed, motion-synced track. Timing mirrors scene.js (coin schedules, knocked-out coins, bonk, cracks, shatter, shards), so each clink and crack lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `coin_clink`, `glass_crack`, `glass_shatter`, `glass_tink`, `metal_creak`, `soft_thud`.
`sfx-library/` sounds: `click-soft`, `coin-cascade-01`, `ping`, `sparkle`, `whoosh-air-01`, `whoosh-short`.

Rebuild: `cd videos/the-ceiling && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-ceiling/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.181 snapshot --at 0.4,2,4,6,8,9.6 --no-end --describe false -o <scratchpad>/ceiling
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-ceiling && npx --yes hyperframes@0.8.181 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-ceiling   # run in the background
```
`render.sh` writes `renders/13learns-ceiling.mp4`. The file already delivered is `renders/Posted/13learns-the-ceiling.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
