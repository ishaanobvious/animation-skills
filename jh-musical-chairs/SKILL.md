---
name: jh-musical-chairs
description: "13learns Job haters video \"Musical Chairs\" (\"They keep taking chairs.\"). Three grey figures walk round two back-to-back chairs while the music plays. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeChair, drawCable)."
---

# Musical Chairs: "They keep taking chairs." (13learns Job haters)

- **Project:** `videos/the-musical-chairs/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-7.md` §1
- **Delivered:** `renders/13learns-musical-chairs.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Musical Chairs: three grey figures walk round two back-to-back chairs while the music plays. Each time it stops, someone is out, and a cable hauls a chair away; in the end it takes the last chair from under the winner too. On the right, blue builds a chair of his own, sits in it, builds a second one beside it and pats it. The last grey walks over and sits down.

## The script (as written)

**Pattern used:** a game everyone knows (#7), and the early leader losing to a test (#5): even the winner gets his chair pulled
**Frame line (top):** THEY KEEP TAKING CHAIRS. (line 2 at the payoff, in blue: BRING YOUR OWN.)
**Labels:** left: Waiting for a seat · right: Built his own
**Chip:** "Round 1" → "Round 2" over the ring
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.4s | Hook: the music | Three grey figures are already walking round two back-to-back chairs at 0.0s. On the right, blue is fitting the legs of a chair of his own. | THEY KEEP TAKING CHAIRS. · Round 1 | music-box tune, clunks |
| 2.4–3.6s | Round 1 | The music stops. Two greys scramble into the chairs; the third slumps to the floor. A cable drops and hauls one chair up out of frame. | Round 2 | tune cuts, scramble, thud, cable whoosh |
| 3.6–6.4s | Round 2 | Music again. Two greys circle one chair. Blue adds the seat and the back to his chair. It stops: one sits and the other is out. | (no new text) | tune, clunks, thud |
| 6.4–7.2s | Nobody wins | The cable takes the last chair from under the winner. He drops to the floor. Blue sits down in his own chair. | (no new text) | whoosh, body fall |
| 7.2–12s | Kind payoff | Blue builds a second chair beside his and pats it. The last grey gets up, walks over and sits. Line 2 types in. Dip, loop. | THEY KEEP TAKING CHAIRS. / BRING YOUR OWN. | clunks, steps, typing, sparkle |

**Post caption:** Every round of layoffs is a round of musical chairs. You can keep circling, or build a seat nobody can pull out from under you. Which round are you on?
**Loop point:** the greys walking round the chairs, music playing.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "They keep taking chairs."
- Label `#lbl-emp` (`index.html`): "Waiting for a seat"
- Label `#lbl-own` (`index.html`): "Built his own"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#round` "Round 1" (numbers)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Bring your own."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const C = { x: -1.45, z: 0.1 };
const RX = 1.05;
const RZ = 0.62;
const OMEGA = 1.1;
const SEAT_H = 0.46;
const A = { x: C.x + 0.3, z: C.z, yaw: 0 }; // faces +x
const B = { x: C.x - 0.3, z: C.z, yaw: Math.PI }; // faces -x
const MINE = { x: 2.35, z: 0.1, yaw: Math.PI };
const SPARE = { x: 1.5, z: 0.5, yaw: Math.PI };
const OUT1 = [-3.05, 0.8];
const OUT2 = [-2.2, -0.85];
const BLUE_AT = [1.72, 0.1];
const MUSIC = [[0, 2.4], [3.3, 5.6]];
const STOP1 = 2.4;
const BACK_UP = 3.3;
const STOP2 = 5.6;
const YANK_B = 3.4;
const YANK_A = 6.55;
const DROP = [6.72, 6.95];
const MY_PARTS = { legs: [0.55, 0.85, 1.15, 1.45], seat: 4.0, back: 4.9 };
const B_SIT = [6.4, 7.0];
const SPARE_PARTS = { legs: [7.45, 7.55, 7.65, 7.75], seat: 7.95, back: 8.25 };
const PAT = [8.5, 9.0];
const G_UP = [8.8, 9.2];
const G_WALK = [9.2, 10.35];
const G_SIT = [10.35, 10.8];
const TYPE_LINE_AT = 10.3;
const TOP = 3.4; // the cable stops short of the frame line
const SMUG = { ...CHAIR_SIT, lean: -0.12, head: 0.15 };
const FLOOR_SIT = { ...SIT, lean: 0.4, head: -0.45 };
const LOOK = { ...STAND, head: 0.25, shL: 0.35, elL: 0.6, shR: 0.3, elR: 0.6 };
const HAMMER = (t, crouch) => ({ ...mixPose(STAND, POSES.CROUCH, crouch), shR: 1.4 + 0.7 * Math.max(0, Math.sin(t * 16)), elR: 0.5, shL: 0.9, elL: ...
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials & chairs · the cable that takes chairs · figures · HTML · frame.

Functions:
- `makeChair(mat)`
- `build(part, t, at)`: a part drops a little and pops in at `at`
- `drawCable(k, ch, c, at, t)`: returns how far the chair has been lifted
- `between(a, b, t, t0, t1, run = false)`: blends two states over [t0, t1]; `run` makes the move a scramble instead of a walk
- `place(fig, st)`
- `stateG2(t)`: g2: out in round 1. g0: wins round 1, out in round 2. g1: wins twice and still loses the chair.
- `stateG0(t)`
- `stateG1(t)`
- `stateBlue(t)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Musical Chairs as one premixed, motion-synced track. Timing mirrors scene.js: an original music-box loop (synthesised here) that cuts dead at each stop, the scramble for the seats, the one who's out sitting down hard, the cable creaking down and hauling a chair away, the last winner dropping to the floor, blue's chair clunking together piece by piece, the spare chair, the pat, grey's steps over and the payoff. Grey sits left in the stereo field, blue right. All sounds are owned synths or come from ../../sfx-library: no attribution.

Owned synths: `SR`, `floor_step`, `metal_creak`, `pipe_clunk`, `soft_thud`.
`sfx-library/` sounds: `body-fall`, `chime`, `click-soft`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-musical-chairs && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-musical-chairs/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/musical-chairs
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-musical-chairs && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-musical-chairs   # run in the background
```
`render.sh` writes `renders/13learns-musical-chairs.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
