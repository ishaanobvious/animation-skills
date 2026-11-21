---
name: jh-bottom-rung
description: "13learns Job haters video \"The Bottom Rung\" (\"The bottom rung is gone.\"). A robot arm (\"AI\") at the foot of a tall ladder is already sawing off the bottom rung at 0.0s, then the next, and the next: five go, each dropping with… Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawRung, drawArm, drawBlocks)."
---

# The Bottom Rung: "The bottom rung is gone." (13learns Job haters)

- **Project:** `videos/the-bottom-rung/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-7.md` §4
- **Delivered:** `renders/13learns-bottom-rung.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Bottom Rung: a robot arm ("AI") at the foot of a tall ladder is already sawing off the bottom rung at 0.0s, then the next, and the next: five go, each dropping with a spark. Grey waits under it, then jumps for the lowest rung that's left and misses by a hand, again and again. On the right, blue sets down three blocks ("Project", "Portfolio", "Proof") as steps, climbs them onto the ladder and up, then turns and points at his steps. Grey climbs them and takes the rung.

## The script (as written)

**Pattern used:** early leader loses to a test (#5), build the next step yourself (#28). AI taking entry-level jobs
**Frame line (top):** THE BOTTOM RUNG IS GONE. (line 2 at the payoff, in blue: BUILD YOUR OWN.)
**Labels:** left: Waiting to be hired · right: Built proof
**Chips:** "AI" on the robot arm; over blue's steps: "Project", "Portfolio", "Proof"
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–4.8s | Rungs go | A robot arm at the foot of a tall ladder is already cutting the bottom rung at 0.0s. Rung after rung falls with a spark. Grey waits under it. Blue starts stacking a block. | THE BOTTOM RUNG IS GONE. · AI · Project | saw, spark, clatter ×5 |
| 4.8–6.6s | Out of reach | Grey jumps for the lowest rung and misses by a hand, again and again. Blue's third block lands: three steps up to the ladder. | Portfolio · Proof | jump thuds, clunk |
| 6.6–9.0s | Built proof | Blue climbs his steps, grabs the rung and climbs the ladder. | (no new text) | mesh steps |
| 9–12s | Kind payoff | Blue looks down and points at his steps. Grey climbs them and takes the rung. Line 2 types in. Dip, loop. | THE BOTTOM RUNG IS GONE. / BUILD YOUR OWN. | steps, typing, sparkle |

**Post caption:** Entry-level postings are down by about a third. Waiting for the bottom rung isn't a plan anymore. Projects, portfolio, proof: build the steps yourself.
**Loop point:** the arm cutting the first rung.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "The bottom rung is gone."
- Label `#lbl-emp` (`index.html`): "Waiting to be hired"
- Label `#lbl-own` (`index.html`): "Built proof"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#ai` "AI" (light), `#b1` "Project" (blue), `#b2` "Portfolio" (blue), `#b3` "Proof" (blue)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Build your own."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const LX = -0.35; // ladder centre
const LZ = -0.25;
const HALF = 0.28;
const RUNG_DY = 0.45;
const RUNGS = 10;
const CUTS = 5; // rungs 0..4 go
const LOWEST = rungY(CUTS);
const L1 = 1.4;
const L2 = 1.4;
const BLOCKS = [
const G_AT = [LX - 0.62, 0.35];
const B_AT = [1.82, 0.0];
const CUT = [0.25, 1.2, 2.15, 3.1, 4.05];
const JUMPS = [4.9, 5.55, 6.2];
const B_CLIMB = [6.55, 6.85, 7.15]; // onto each block
const ON_LADDER = [7.4, 7.75];
const UP = [7.75, 8.9];
const POINT = [9.0, 9.4];
const G_WALK = [9.15, 10.05];
const G_STEPS = [10.15, 10.4, 10.65];
const G_GRAB = [10.85, 11.15];
const TYPE_LINE_AT = 10.2;
const LOOK_UP = { ...STAND, head: 0.45, lean: -0.08 };
const JUMP = { ...REACH, thL: 0.2, knL: -0.4, thR: 0.1, knR: -0.3 };
const HAMMER = (t) => ({ ...mixPose(STAND, CROUCH, 0.45), shR: 1.3 + 0.7 * Math.max(0, Math.sin(t * 16)), elR: 0.5, shL: 0.9, elL: 0.4 });
const CLIMB = (ph) => ({ lean: 0.05, head: 0.2, thL: 0.55 + 0.5 * Math.sin(ph), knL: -0.9 - 0.6 * Math.sin(ph), thR: 0.55 - 0.5 * Math.sin(ph), knR...
const HOLD = { ...CLIMB(0), thL: 0.4, knL: -0.6, thR: 0.1, knR: -0.15 };
```

## How `scene.js` is built

Sections, in order: layout · story beats · the ladder · the robot arm · blue's blocks · figures · HTML · frame.

Functions:
- `drawRung(k, t)`: a cut rung falls, spins and lands in a little heap in front of the ladder
- `segBetween(m, a, b)`
- `armTarget(t)`
- `drawArm(t)`
- `drawBlocks(t)`
- `stepUp(t, times, xs, ys, z0, z1)`: stepping up onto a block: a short hop between two foot heights
- `poseBlue(t)`
- `poseGrey(t)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Bottom Rung as one premixed, motion-synced track. Timing mirrors scene.js: the robot arm's servo whirr as it moves to each rung, a saw whine and a spark crackle on each of the five cuts, every rung clattering to the floor when it lands, grey's three jumps (and three short landings), blue's blocks thudding down, his steps up them and onto the ladder, the rungs ticking under him as he climbs, the point, grey's walk over and climb, and the payoff. Grey sits left in the stereo field, blue right. Owned synths and ../../sfx-library sounds.

Owned synths: `SR`, `band`, `floor_step`, `glass_crack`, `mesh_step`, `pipe_clunk`, `rung_tick`, `soft_thud`.
`sfx-library/` sounds: `chime`, `pop`, `sparkle`, `typing`, `whoosh-air-01`.

Rebuild: `cd videos/the-bottom-rung && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-bottom-rung/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/bottom-rung
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-bottom-rung && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-bottom-rung   # run in the background
```
`render.sh` writes `renders/13learns-bottom-rung.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
