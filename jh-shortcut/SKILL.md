---
name: jh-shortcut
description: "13learns Job haters video \"The Shortcut\" (\"Their shortcut came with a jetpack.\"). A sunglasses guru sails across a gap in one leap and lands on a pile of coins. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawCoins, drawBridge, drawJet, drawProps)."
---

# The Shortcut: "Their shortcut came with a jetpack." (13learns Job haters)

- **Project:** `videos/the-shortcut/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 11s, seamless loop, no VO)
- **Script:** `SCRIPTS-3.md` §4
- **Delivered:** `renders/Posted/13learns-the-shortcut.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Shortcut: a sunglasses guru sails across a gap in one leap and lands on a pile of coins. Grey drops his toolbox, copies the run-up and falls into the pit. The guru turns: his "backpack" is a jetpack stamped FAMILY MONEY and AD BUDGET. Blue lays planks across, then lowers a rope.

## The script (as written)

**Pattern used:** "Their way worked for them. / Don't drop yours." (copying someone else's path), retold as the get-rich-quick guru
**Frame line (top):** THEIR SHORTCUT CAME WITH A JETPACK. (appears at the reveal)
**Labels:** Copying / Building
**Small ticker:** none (the reveal is the beat)
**Props:** a wide gap; a flashy grey "guru" figure in sunglasses with a "$10K/MONTH" sign; grey and blue on the near side; blue's own plank bridge growing across
**Length:** 11s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.5s | Hook: the leap | The guru takes a run-up and sails across the gap in one leap, landing in a pile of coins and posing. A "$10K/MONTH" sign pops. | "$10K/MONTH" | whoosh, coin cascade, pop |
| 2.5–4.5s | Two reactions | Grey drops his toolbox and starts copying the guru's run-up. Blue keeps laying planks out over the gap, one per beat. | Copying / Building | toolbox clatter, plank thunks |
| 4.5–6.0s | The reveal | Grey leaps exactly like the guru and drops straight into the gap. The camera tilts to the guru: a jetpack on his back is switching off, with "Family money" and "Ad budget" stamped on it. | THEIR SHORTCUT CAME WITH A JETPACK. | fall whoosh, thud, jetpack sputter |
| 6.0–9.0s | Blue crosses | Blue's bridge reaches the other side; he walks across on his own planks. | (frame line stays) | footsteps on wood |
| 9.0–11s | Kind payoff | Blue lowers a rope into the gap to grey. The second line types in. Dip, loop. | BUILD YOUR OWN BRIDGE. | rope drop, sparkle |

**Post caption:** Every "I quit my job and made $10K in a month" story has a jetpack you can't see. Build the slow bridge.
**Loop point:** the guru on the near side, grey and blue with toolboxes.

## On-screen text (where it lives)

- Label `#lbl-emp` (`index.html`): "Copying"
- Label `#lbl-own` (`index.html`): "Building"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 11;
const EL = -0.9; // near edge
const ER = 1.4; // far edge
const PIT_Y = FLOOR_Y - 1.7;
const PLANK_W = 0.3;
const PLANKS = 8;
const GURU_LAND = 2.55;
const GREY_FALL_X = EL + 0.55;
const G_RUN = [0.15, 0.9];
const G_LEAP = [0.9, 1.75];
const TENK_AT = 2.0;
const DROP_BOX = 2.6;
const BACK_UP = [2.8, 3.45];
const RUN = [3.6, 4.5];
const LEAP = [4.5, 4.75];
const FALL = [4.75, 5.25];
const GURU_TURN = 4.6;
const SPUTTER = 4.8;
const STAMPS = [5.1, 5.45];
const FRAME_AT = 5.0;
const PLANK_T = (i) => 2.6 + 0.55 * i;
const ACROSS = PLANK_T(PLANKS - 1) + 0.15;
const CHEER = [6.7, 7.2];
const BACK_TO_MIDDLE = [7.4, 8.4];
const KNEEL_AT = 8.4;
const ROPE = [9.0, 9.6];
const GRAB = 9.85;
const PULL = [10.0, 10.8];
const TYPE_LINE_AT = 9.2;
const FLEX = { ...STAND, head: -0.1, shL: 0.4, elL: 2.2, shR: 0.4, elR: 2.2, ab: 1.3, eab: 0.2 };
const FLAIL = { ...TUCK, lean: -0.3, head: -0.4, shL: 2.8, elL: 0.4, shR: 2.6, elR: 0.5 };
const SLUMP = { ...SIT, head: 0.6, lean: 0.7 };
const GREY_X0 = -2.3;
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · cliffs and the pit · the bridge · figures · poses · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `block(x0, x1, top, mat = rockFace, topMat = rockTop)`: cliffs and the pit
- `drawCoins(t)`
- `drawBridge(t)`
- `drawJet(t)`
- `poseGuru(t)`
- `poseGrey(t)`
- `poseBlue(t)`
- `drawProps(t)`
- `drawChips(t)`
- `typed(textEl, caretEl, text, at, dur, t)`
- `placeTagAt(id, x, dy)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Shortcut as one premixed, motion-synced track. Timing mirrors scene.js (the guru's run, jet-assisted leap and coin landing, the $10K chip, grey dropping his toolbox and copying the run-up into the pit, the jetpack sputtering, the stamps, every plank, blue's walk, the rope and the pull), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `air_whoosh`, `floor_step`, `metal_creak`, `pipe_clunk`, `soft_thud`.
`sfx-library/` sounds: `body-fall`, `chime`, `click`, `click-soft`, `coin-cascade-02`, `glitch-3`, `notification`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-shortcut && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-shortcut/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/shortcut
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-shortcut && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-shortcut   # run in the background
```
`render.sh` writes `renders/13learns-shortcut.mp4`. The file already delivered is `renders/Posted/13learns-the-shortcut.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
