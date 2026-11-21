---
name: jh-cactus
description: "13learns Job haters video \"The Cactus\" (\"Some jobs hurt to hold.\"). Job hugging, drawn literally. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeCactus, drawTree, drawCacti)."
---

# The Cactus: "Some jobs hurt to hold." (13learns Job haters)

- **Project:** `videos/the-cactus/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-7.md` §2
- **Delivered:** `renders/13learns-cactus.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Cactus: job hugging, drawn literally. Both figures are hugging a tall cactus at 0.0s, wincing with every squeeze. Blue lets go, shakes his hands out, and his cactus sinks away; he plants a pot and a small blue tree grows. Grey hugs tighter while his cactus grows taller and pricklier, and a chip pops off it each beat ("No raise", "Overtime", ...). Then blue walks over and holds out a hand, and grey unwraps his arms and walks with him to the tree.

## The script (as written)

**Pattern used:** a known object that shows the feeling at once (#7), invisible costs made solid (#22). Job hugging, drawn literally
**Frame line (top):** SOME JOBS HURT TO HOLD. (line 2 at the payoff, in blue: YOU CAN LET GO.)
**Labels:** left: Job hugging · right: Let go
**Chips:** grey's thorns pop as chips: "No raise", "Overtime", "Layoff rumours", "Year 6". Over blue's plant: "First client", "$800/mo"
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.5s | Hook: the hug | Both figures are already hugging a tall cactus at 0.0s, wincing with each squeeze. | SOME JOBS HURT TO HOLD. · Job hugging / Let go | prickle ticks |
| 1.5–3.0s | Let go | Blue flinches, lets go, steps back and shakes out his hands. His cactus sinks away. Grey hugs tighter. | (no new text) | ow-tick, step, shake |
| 3.0–8.5s | Two paths | Grey's cactus grows taller and pricklier and a chip pops off it each beat while he greys and hunches. Blue plants a pot and a blue sapling grows into a small glowing tree. | No raise · Overtime · Layoff rumours · Year 6 / First client · $800/mo | pops, prickle, growth swells |
| 8.5–12s | Kind payoff | Blue walks over and holds out a hand. Grey looks at it, unwraps his arms and steps away from the cactus with him toward the tree. Line 2 types in. Dip, loop. | SOME JOBS HURT TO HOLD. / YOU CAN LET GO. | chime, steps, typing, sparkle |

**Post caption:** Job hugging: holding on tighter to a job that hurts, because letting go feels scarier. It doesn't get softer the longer you hold it. What would you grow with your hands free?
**Loop point:** both hugging their cactus.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Some jobs hurt to hold."
- Label `#lbl-emp` (`index.html`): "Job hugging"
- Label `#lbl-own` (`index.html`): "Let go"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#c1` "No raise" (light), `#c2` "Overtime" (light), `#c3` "Layoff rumours" (light), `#c4` "Year 6" (light), `#b1` "First client" (blue), `#b2` "$800/mo" (blue)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "You can let go."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const GC = { x: -1.2, z: 0 }; // grey's cactus
const BC = { x: 1.95, z: 0 }; // blue's cactus
const G_AT = [-1.6, 0];
const B_AT = [1.55, 0];
const B_BACK = [1.05, 0];
const B_TEND = [1.42, 0.05];
const TREE = { x: 1.0, z: 0.05 };
const B_OFFER = [-0.62, 0.05];
const SQUEEZE = 1.1; // seconds per squeeze
const B_LET_GO = [1.45, 1.85];
const B_SHAKE = [1.85, 2.5];
const B_SINK = [2.2, 3.0];
const B_TO_POT = [2.6, 3.2];
const POT_AT = 3.3;
const GROW = [3.6, 8.0];
const G_CHIPS = [3.4, 4.6, 5.8, 7.0];
const B_CHIPS = [5.3, 6.9];
const B_WALK = [8.15, 9.25];
const OFFER = [9.25, 9.6];
const G_LOOK = [9.4, 9.75];
const G_UNWRAP = [9.75, 10.15];
const G_GO = [10.15, 11.45];
const B_GO = [10.3, 11.5];
const TYPE_LINE_AT = 10.2;
const LEAVES = [[0, 0, 0, 0.36], [0.24, -0.08, 0.05, 0.26], [-0.22, -0.06, 0.04, 0.27], [0.1, 0.2, -0.05, 0.25], [-0.1, 0.16, 0.12, 0.22], [0.02, -...
const WINCE = { ...HUG, lean: 0.02, head: -0.3 };
const TIGHT = { ...HUG, lean: 0.3, head: -0.4, thL: 0.2, knL: -0.35, thR: 0.1, knR: -0.3 };
const SHAKE = (t) => ({ ...STAND, shL: 0.9 + 0.4 * Math.sin(t * 34), elL: 0.9, shR: 0.9 + 0.4 * Math.sin(t * 34 + 1.3), elR: 0.9 });
const OFFER_P = { ...STAND, shR: 1.45, elR: 0.1, head: 0.05 };
const G_SPOTS = [[-2.3, 2.1], [-0.6, 2.6], [-2.25, 3.05], [-0.45, 3.5]];
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · a cactus: trunk, two arms, white spines (group origin on the floor) · blue's pot and tree · figures · HTML · frame.

Functions:
- `makeCactus(seed)`: a cactus: trunk, two arms, white spines (group origin on the floor)
- `drawTree(t)`
- `poseBlue(t)`
- `poseGrey(t)`
- `drawCacti(t)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Cactus as one premixed, motion-synced track. Timing mirrors scene.js: a prickly tick on every squeeze (grey's run all the way to the unwrap, blue's stop when he lets go), blue's flinch and hand-shake, his cactus sinking into the floor, the pot set down, the tree growing with a pop per leaf cluster, a dull blip for each grey chip and a bright one for each blue chip, blue's walk over, the offered hand, grey letting go, both walking to the tree and the payoff. Grey sits left in the stereo field, blue right. Owned synths and ../../sfx-library sounds only: no attribution.

Owned synths: `air_whoosh`, `counter_blip`, `floor_step`, `glass_tink`, `quake_rumble`, `rung_tick`, `soft_thud`.
`sfx-library/` sounds: `chime`, `ping`, `pop`, `riser`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-short`.

Rebuild: `cd videos/the-cactus && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-cactus/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/cactus
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-cactus && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-cactus   # run in the background
```
`render.sh` writes `renders/13learns-cactus.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
