---
name: jh-plane
description: "13learns Job haters video \"The Plane\" (\"It doesn't have to be perfect. It has to fly.\"). A cliff on the left. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawPlane, drawBench, drawLine2)."
---

# The Plane: "It doesn't have to be perfect. It has to fly." (13learns Job haters)

- **Project:** `videos/the-plane/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-6.md` §2
- **Delivered:** `renders/13learns-the-plane.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Plane: a cliff on the left. Grey stands at a workbench on top, sanding one flawless wing ("Plan: 99% ready", forever). Blue has already jumped off the edge at 0.0s, and a plane builds itself around him as he falls: body, wings (one crooked), tail, propeller. He pulls up just over the floor and loops the frame, and every lap the plane gets better (v1 → v9): the wing straightens, the body turns blue. Then he hovers beside the cliff and holds out a hand; grey sets his perfect wing down and climbs into the back seat.

## The script (as written)

**Pattern used:** build the next piece while standing on the last one (#28, "Perfectionist / Action Taker"), drawn as the idiom "jump off the cliff and build the plane on the way down"
**Frame line (top):** IT DOESN'T HAVE TO BE PERFECT. (line 2 at the payoff, in blue: IT HAS TO FLY.)
**Labels:** left: Perfect plan · right: Started anyway
**Stats:** grey's workbench "Plan: 99% ready" (never changes) · blue's plane "v1 → v9"
**Props:** a cliff on the left. Grey stands at a workbench sanding one flawless wing with a spirit level. Blue jumps off the edge, and plane parts fly in and snap on around him as he falls: body, crooked wings, tail, propeller.
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.0s | Hook: the jump | Blue is already off the edge at 0.0s. Grey is sanding. | IT DOESN'T HAVE TO BE PERFECT. · Perfect plan / Started anyway | whoosh, sanding |
| 1.0–3.0s | Build on the way down | As blue falls, a body snaps under him, then wings (one crooked), a tail, a propeller. Just above the floor he pulls up. | v1 | clunk ×4, propeller whirr |
| 3.0–8.5s | Fix it in the air | The plane loops round the frame. Each lap it improves (wing straightens, second propeller, blue trim) and the version ticks up. Grey sands, checks the level and sands again. | v2 → v9 · Plan: 99% ready | engine, a clunk per fix, sanding |
| 8.5–10s | The offer | Blue flies level with the cliff and stops beside grey, holding out a hand. | (no new text) | engine idles |
| 10–12s | Kind payoff | Grey looks at his perfect wing, sets it on the bench and climbs into the back seat. Line 2 types in. Dip, loop. | IT DOESN'T HAVE TO BE PERFECT. / IT HAS TO FLY. | step, seat thunk, typing, sparkle |

**Post caption:** Nobody's first version flies well. It flies, and then you fix it in the air. What are you still sanding?
**Loop point:** blue stepping off the cliff edge.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "It doesn’t have to be perfect."
- Label `#lbl-emp` (`index.html`): "Perfect plan"
- Label `#lbl-own` (`index.html`): "Started anyway"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#plan` "Plan: 99% ready" (light), `#ver` "v1" (light)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "It has to fly."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const CLIFF = { x0: -3.9, x1: -1.2, top: FLOOR_Y + 3.0, z0: -1.2, z1: 0.9 };
const BENCH = { x: -2.05, z: 0.15, h: 0.85 };
const G_AT = { x: -2.7, z: 0.15 };
const FLY_END = 9.15;
const PARTS = { body: 0.75, wingL: 1.15, wingR: 1.3, tail: 1.7, prop: 2.1 };
const VERS = Array.from({ length: 8 }, (_, k) => 3.4 + 0.62 * k); // v2 … v9
const TURN_ROUND = [9.1, 9.6];
const OFFER = [9.6, 10.0];
const G_STOP = 9.45;
const G_LOOK = [9.6, 10.0];
const G_SET = [10.0, 10.3];
const G_WALK = [10.3, 10.85];
const G_HOP = [10.85, 11.2];
const LEAVE = [11.3, 12.0];
const TYPE_LINE_AT = 10.3;
const S = 1.45;
const TARGETS = {
const OFFER_P = { ...PILOT, lean: -0.1, head: 0.2, shR: 1.4, elR: 0.1 };
const PASSENGER = { ...PILOT, head: 0.25, shL: 0.6, elL: 0.9, shR: 2.5, elR: 0.2 }; // a little wave as they go
const SAND = { ...STAND, lean: 0.35, head: -0.35, shL: 1.15, elL: 0.35, shR: 1.1, elR: 0.4 };
const CHECK = { ...SAND, lean: 0.55, head: -0.6 };
const SET_DOWN = { ...SAND, lean: 0.4, head: -0.5, shL: 0.95, shR: 0.95 };
const LINE2 = "It has to fly.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials & helpers · the cliff and grey's workbench · the plane (local: forward +x, up +y) · figures · HTML · frame.

Functions:
- `add(m, x, y, z)`
- `makeGlow(size, color)`
- `planePose(t)`
- `drawPlane(t)`
- `seatIn(fig, pose, lx, yaw, pitch)`
- `poseBlue(t, yaw, pitch)`
- `poseGrey(t, yaw, pitch)`
- `drawBench(t)`
- `pin(el, v, opacity, scale = 1)`
- `drawHud(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Plane as one premixed, motion-synced track. Timing mirrors scene.js: grey's sanding the whole time (with a level set down now and then), blue's jump off the edge, a clunk for each part that snaps onto the plane as he falls, the propeller catching and the engine through the loops, a bright click for every new version, the hover, the hand held out, grey's wing set down, his steps to the edge and the hop into the back seat. Grey sits left in the stereo field, blue moves with the plane. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `air_whoosh`, `counter_blip`, `floor_step`, `pipe_clunk`, `soft_thud`, `wheel_rumble`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `riser`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-cinematic`, `whoosh-deep`, `whoosh-short`.

Rebuild: `cd videos/the-plane && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-plane/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/plane
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-plane && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-plane   # run in the background
```
`render.sh` writes `renders/13learns-plane.mp4`. The file already delivered is `renders/13learns-the-plane.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
