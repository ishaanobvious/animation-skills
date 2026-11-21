---
name: jh-balloon
description: "13learns Job haters video \"The Balloon\" (\"The fast way up can't hold you.\"). A tower with a lit ledge at the top, \"YOUR OWN INCOME\". Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawCrates, drawBalloons, drawLine2)."
---

# The Balloon: "The fast way up can't hold you." (13learns Job haters)

- **Project:** `videos/the-balloon/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-6.md` §1
- **Delivered:** `renders/Posted/13learns-the-balloon.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Balloon: a tower with a lit ledge at the top, "YOUR OWN INCOME". Grey grabs a bunch of balloons tagged GET RICH QUICK and shoots up beside it, way ahead, reaching for the edge; then the balloons pop one by one under his weight and he drops back to the floor. Blue builds a crate scaffold, standing on the last crate to place the next, and climbs, uneven but steady, onto the ledge. He points down at his scaffold; grey lets go of his last limp balloon and takes the first crate.

## The script (as written)

**Pattern used:** the fast route fails under load (#27, "The grind / Shortcuts")
**Frame line (top):** THE FAST WAY UP CAN'T HOLD YOU. (line 2 at the payoff, in blue: BUILD ONE THAT CAN.)
**Labels:** left: Quick money · right: Real skills
**Props:** a glowing ledge high above the floor marked "YOUR OWN INCOME". Grey grabs a bunch of pale balloons tagged "GET RICH QUICK". Blue builds a scaffold of crates, each on a thin post, zig-zagging up and standing on the last one to place the next.
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.5s | Hook: lift-off | Grey is already rising on his balloons at 0.0s. Blue sets down crate one and steps onto it. | THE FAST WAY UP CAN'T HOLD YOU. · Quick money / Real skills | balloon squeak, whoosh, crate thud |
| 1.5–4.5s | Way ahead | Grey shoots up to just under the ledge and reaches for its edge. Blue is a few crates up, placing one per beat. | YOUR OWN INCOME | crate thuds, rising whoosh |
| 4.5–6.0s | The weight | The balloons pop one by one under his weight. He sinks, then drops to the floor. | (no new text) | pop, pop, pop, fall whoosh, thud |
| 6.0–8.5s | The climb | Blue keeps building and climbing, uneven but steady, and steps onto the ledge. It lights up blue. | (no new text) | thuds speeding up, chime |
| 8.5–12s | Kind payoff | Grey sits on the floor holding one limp balloon. Blue points down at his scaffold. Grey drops the balloon, walks over and steps onto the first crate. Line 2 types in. Dip, loop. | THE FAST WAY UP CAN'T HOLD YOU. / BUILD ONE THAT CAN. | steps, crate creak, typing, sparkle |

**Post caption:** Quick money looks faster right up until it has to carry your weight. Skills are slower, and they hold. Which one are you climbing?
**Loop point:** grey grabbing the balloons, blue's first crate.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "The fast way up can’t hold you."
- Label `#lbl-emp` (`index.html`): "Quick money"
- Label `#lbl-own` (`index.html`): "Real skills"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#ledge-sign` "YOUR OWN INCOME" (light), `#tag` "GET RICH QUICK" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Build one that can."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const LEDGE = { x0: -0.9, x1: 0.9, y: FLOOR_Y + 3.4, z0: -1.25, z1: 0.35 };
const G_START = { x: -1.85, z: 0.25 };
const G_REACH = { x: -1.35, y: 1.85 }; // root height above the floor at his highest
const RISE = 0.485;
const CRATES = Array.from({ length: 7 }, (_, k) => ({ x: k % 2 === 0 ? 1.15 : 1.6, top: FLOOR_Y + RISE * (k + 1), z: 0.2 }));
const N = CRATES.length;
const B_START = { x: 1.95, z: 0.2 };
const T_CRATE = CRATES.map((_, k) => (k === 0 ? 0.1 : 1.0 + 0.95 * (k - 1) + 0.12 * Math.sin(k * 2.3)));
const UP = [0.0, 3.0];
const HOVER = [3.0, 4.5];
const POPS = [4.55, 4.85, 5.1, 5.3];
const FALL = [5.32, 5.82];
const TO_LEDGE = [T_CRATE[N - 1] + 0.45, T_CRATE[N - 1] + 0.95];
const LIT = TO_LEDGE[1];
const POINT = [9.3, 9.8];
const G_UP = [9.9, 10.35];
const G_WALK = [10.4, 11.25];
const G_FOOT = [11.3, 11.6];
const TYPE_LINE_AT = 10.3;
const BALLOONS = [[0, 0.95, 0], [-0.26, 0.82, 0.05], [0.26, 0.84, -0.04], [-0.12, 1.2, -0.06], [0.16, 1.18, 0.06]];
const LIMP = 0; // the one he keeps
const REACH_EDGE = { ...HANG, head: 0.35, shL: 1.9, elL: 0.1, thL: 0.5, knL: -0.6 };
const SIT_LOOK = { ...SIT, head: -0.3, shR: 0.9, elR: 0.9 };
const PLACE = { ...STAND, lean: 0.35, head: 0.25, shL: 1.9, elL: 0.15, shR: 1.85, elR: 0.2 };
const POINT_P = { ...STAND, lean: 0.25, head: -0.5, shR: 0.9, elR: 0.05, shL: 0.1, elL: 0.2 };
const INVITE = { ...STAND, head: -0.4, shR: 1.0, elR: 0.6, shL: 0.1, elL: 0.2 };
const FOOT_UP = { ...STAND, lean: 0.1, head: 0.2, thR: 0.95, knR: -1.0, shL: 0.25, elL: 0.3, shR: -0.2, elR: 0.3 };
const LINE2 = "Build one that can.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials & helpers · the tower and its ledge · blue's scaffold · grey's balloons · figures · HTML · frame.

Functions:
- `add(m, x, y, z)`
- `makeGlow(size, color)`
- `drawCrates(t)`
- `greyLift(t)`
- `poseGrey(t)`
- `drawBalloons(t)`
- `standOn(k)`: blue: lays a crate, steps onto it, lays the next
- `poseBlue(t)`
- `pin(el, v, opacity)`
- `drawHud(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Balloon as one premixed, motion-synced track. Timing mirrors scene.js: grey's lift-off and rise on the balloons, the near-miss at the ledge, four pops, the fall and the thud on the floor; blue setting down each crate (a thud and a rising blip) and stepping up onto it, stepping onto the ledge as it lights, pointing grey up; grey letting the last balloon go, walking over and taking the first crate. Grey sits left in the stereo field, blue right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `air_whoosh`, `counter_blip`, `floor_step`, `soft_thud`.
`sfx-library/` sounds: `body-fall`, `chime`, `pop`, `riser`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-deep`, `whoosh-short`.

Rebuild: `cd videos/the-balloon && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-balloon/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/balloon
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-balloon && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-balloon   # run in the background
```
`render.sh` writes `renders/13learns-balloon.mp4`. The file already delivered is `renders/Posted/13learns-the-balloon.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
