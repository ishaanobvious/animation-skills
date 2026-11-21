---
name: jh-attempt-7
description: "13learns Job haters video \"Attempt 7\" (\"Everyone saw number 7.\"). Blue keeps building little stalls; each one collapses into a layer of rubble and he climbs onto it. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawSign, makeStall, makeLayer, drawStalls)."
---

# Attempt 7: "Everyone saw number 7." (13learns Job haters)

- **Project:** `videos/attempt-7/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-2.md` §5
- **Delivered:** `renders/Posted/13learns-attempt-7.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Attempt 7: blue keeps building little stalls; each one collapses into a layer of rubble and he climbs onto it. #7 stands on top of the hill and gets the applause. Then the six underneath get their numbers, and blue climbs down and holds his hammer out to grey.

## The script (as written)

**Pattern used:** the success built on 47 failed tests (3.4M), plus the hidden-roots reveal (10.3M)
**On-screen counter:** Attempt #1 → #7
**Labels:** Employee / Builder
**Props:** a stage-lit plot of ground on the right. Each failed business is a small blue stall that collapses into rubble, and the rubble piles up. On the left, grey stands at a desk under a sign reading "Safe".
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: #1 falls | Blue builds stall #1 in two beats and it collapses at once. Grey at his "Safe" desk shrugs at the camera. | Attempt #1 | hammer taps, collapse crunch |
| 2.0–6.0s | Fail, fail, fail | #2, #3, #4, #5, #6: each stall goes up and falls, a little faster each time. Every collapse leaves rubble, and blue rises with the pile as it grows into a hill. | Attempt #2 → #6 | crunch per collapse, rising pitch |
| 6.0–7.5s | The turn | #7 goes up on top of the rubble hill and stays up. It lights brand blue. A crowd of small grey silhouettes appears in front and claps. | Attempt #7 (blue) · "Overnight success" tag | light-on hum, applause swell |
| 7.5–10.0s | The reveal | The camera tilts down: the hill under #7 is made of stalls #1–6, each stamped with its number. | (numbers on the rubble) | low whoosh |
| 10.0–12s | Kind payoff | Blue climbs down and offers grey a hammer. Grey looks at his "Safe" sign, then at the hammer. Dip, loop. | Attempt #7 | sparkle, single hammer tap |

**Post caption:** Everyone saw number 7. Nobody saw the six I'm standing on.
**Loop point:** empty plot, blue holding a hammer, grey at his desk.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Everyone saw #7."
- Label `#lbl-emp` (`index.html`): "Employee"
- Label `#lbl-own` (`index.html`): "Builder"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Nobody saw the six under it."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const TAU = Math.PI * 2;
const GREY_X = -2.3;
const DESK_X = GREY_X - 0.67;
const DESK_TOP = FLOOR_Y + 1.12;
const PILE_X = 1.9;
const LAYER_H = 0.22;
const STALL_X = PILE_X + 0.3;
const ATTEMPTS = [
const SQUASH = 0.3; // collapse duration; the rubble layer lands at fall + SQUASH
const HOP = [0.3, 0.55]; // blue hops onto the new layer
const LIGHT_AT = 6.45;
const CROWD = [6.5, 7.6];
const STAMP_AT = 7.8;
const STAMP_GAP = 0.25;
const TYPE_LINE_AT = 8.6;
const DOWN = [9.7, 10.35];
const WALK = [10.35, 11.15];
const OFFER_AT = 11.15;
const G_SHRUG = [1.2, 1.95];
const G_WATCH = [6.5, 7.9];
const G_TURN = [10.4, 10.8];
const G_LOOK = 11.35;
const CLAP_OPEN = { ...STAND, head: -0.35, shL: 1.25, elL: 0.55, shR: 1.25, elR: 0.55, ab: 0.45, eab: -0.2 };
const CLAP_SHUT = { ...CLAP_OPEN, ab: 0.05, eab: 0.25 };
const TYPE = { ...STAND, lean: 0.22, head: 0.25, shL: 0.5, elL: 1.05, shR: 0.5, elR: 1.05 };
const SHRUG = { ...STAND, head: 0.12, shL: 0.25, elL: 1.35, shR: 0.25, elR: 1.35, ab: 0.4, eab: -0.35 };
const HAMMER_UP = { ...STAND, lean: 0.2, head: 0.25, thL: 0.2, knL: -0.25, thR: -0.15, knR: -0.1, shL: 0.9, elL: 0.5, shR: 2.5, elR: 0.6 };
const HAMMER_DOWN = { ...HAMMER_UP, lean: 0.32, shR: 1.15, elR: 0.15 };
const CROUCH_HOP = { ...POSES.CROUCH, shL: -0.6, shR: -0.7 };
const LOOK_DOWN = { ...PROUD, head: 0.55, lean: 0.12 };
const OFFER = { ...STAND, lean: 0.12, head: 0.05, shL: 0.1, elL: 0.15, shR: 1.45, elR: 0.12 };
const COUNT = ATTEMPTS.map(([at], k) => [at, `#${k + 1}`, k === 6]);
const LINE2 = "Nobody saw the six under it.";
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · grey's desk and the SAFE sign · the stalls · the crowd that only sees #7 · figures · HTML · frame.

Functions:
- `makeGlow(size, color = 0xe8eeff)`
- `drawSign(t)`
- `makeStall(k)`: the stalls
- `makeLayer(k)`: rubble layer k: a squat slab with bits of the stall sticking out of it
- `layersDown(t)`
- `drawStalls(t)`
- `drawCrowd(t)`
- `strikeSwing(t, beats)`
- `poseBlue(t)`
- `poseGrey(t)`
- `drawCount(t)`
- `drawChip(t)`
- `drawStamps(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Attempt 7 as one premixed, motion-synced track. Timing mirrors scene.js (two hammer strikes per stall, each collapse and the rubble layer landing, blue's hops, #7 lighting up, the crowd, the stamps, the climb down and the offer), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `floor_step`, `metal_creak`, `pipe_clunk`, `soft_thud`, `stone_crash`.
`sfx-library/` sounds: `applause-small-01`, `chime`, `click`, `click-soft`, `ping`, `pop`, `sparkle`, `typing`, `whoosh-short`.

Rebuild: `cd videos/attempt-7 && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/attempt-7/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/attempt-7
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/attempt-7 && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh attempt-7   # run in the background
```
`render.sh` writes `renders/13learns-attempt-7.mp4`. The file already delivered is `renders/Posted/13learns-attempt-7.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
