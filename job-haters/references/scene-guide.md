# Writing scene.js

scene.js draws one frame for any time `t` (seconds, 0–12). index.html handles the fade-in and the dip
to black over the last 0.28s, and its GSAP timeline only pulses the floor glow. Everything else (3D,
chips, labels, line 2) is driven from `renderAt(t)` on `hf-seek`.

## Coordinates (batch-7 camera: fov 17, z 42, target y -0.4)

| World | Screen (1080×1920) |
| --- | --- |
| floor `FLOOR_Y = -2.0` | y ≈ 1160px (labels sit 56px below it) |
| 1 world unit | ≈ 153px |
| x | px ≈ 540 + 153·x; visible x ≈ -3.5 … 3.5 at z 0 |
| y | px ≈ 1160 − 153·(y + 2) |
| frame line / line 2 | 132–290px ⇒ keep props and chips below world **y ≈ 3.2** |
| logo | top 1515px, bottom-centre (in index.html) |

z points at the camera. Use z ≈ -1 … 0.9: put a figure that must pass a prop at a different z
(e.g. walk "round the front" at z 0.6–0.75), and set backdrops (walls, windows) at z ≈ -1.

A typical layout: grey's world on the left (x ≈ -3 … -0.5), blue's on the right (x ≈ 0.5 … 2.8),
labels placed under each column with `placeTagAt("lbl-emp", x)` / `placeTagAt("lbl-own", x)`.

## Figures

```js
const blue = makeFigure(mats.blue, mats.blueLeg);
const grey = makeFigure(mats.grey, mats.greyLeg);
scene.add(blue.root, grey.root);
applyPose(fig, pose, x, groundY, z, lift = 0, yaw = 0, roll = 0);
```

- Size: head top ≈ floor + 1.85, hip ≈ 0.97, shoulder ≈ 1.57; standing reach with arms up ≈ 2.3.
- `applyPose` puts the hips at `groundY + hipHeight(pose) + lift`, so feet land on `groundY`.
  **Sitting on something:** pass `groundY = seatY - hipHeight(pose)` so the hips sit at `seatY`.
- Pose keys: `lean head thL knL thR knR shL elL shR elR ab eab` (radians).
  - `lean` + leans forward; `head` + looks up; `th` + swings the leg forward; `kn` negative bends.
  - `sh` + raises the arm forward (π/2 ≈ straight ahead, ~2.9 straight up); `el` + folds the forearm
    forward; `ab` swings arms out sideways, `eab` folds forearms back in (hands on hips, a hug).
- Built-ins (`POSES`): STAND, CROUCH, TUCK, PROUD, HUNCH, SIT (on the floor, knees up), REACH (arms up),
  BALANCE; `walkPose(phase, amp)`, `runPose(phase, amp, lean)`; `mixPose(a, b, u)` blends.
- Poses that worked in batch 7 (copy them): chair sit `{ lean: 0.05, thL: 1.5, knL: -1.5, thR: 1.45,
  knR: -1.45, shL: 0.55, elL: 0.55, shR: 0.5, elR: 0.6 }`; hug `{ shL: 1.25, elL: 1.05, shR: 1.3, elR:
  1.0, ab: 0.45, eab: -0.9 }`; hammering `shR: 1.4 + 0.7·max(0, sin(16t))`; holding a box
  `shL/shR 0.75, elL/elR 0.95`; offering a hand `shR: 1.45, elR: 0.1`; wave `shR: 2.1 + 0.35·sin(11t)`.
- Walk phase: about `distance × 1.6` steps; keep walks under ~2.3 world units/s or they skate.

### Yaw

The figure faces **+x at yaw 0**, -x at yaw π, away from camera at π/2, toward camera at -π/2.
`yawToward(dx, dz)` turns +x toward a direction. To turn round, lerp 0 → **-π** (through facing the
camera), not 0 → π. Pass yaw around explicitly: `applyPose` does a `rotateZ`, so
`root.rotation.y` can read back wrong. Keep seated and working figures in profile; poses facing the
camera foreshorten badly.

### Grey's colour

`mats.grey.color.copy(GREY_START).lerp(GREY_END, smooth(t / 8) * (1 - 0.45 * smooth((t - payoff) / 1)))`
greys him out over the struggle and brightens him once blue helps.

## Helpers in rig.js (batch-7 block at the bottom)

| Helper | Use |
| --- | --- |
| `box(w, h, d, mat)` / `add(mesh, x, y, z)` / `std(color, rough, metal)` | quick props |
| `makeGlow(size, color)` | additive sprite for lights, screens, sparks (set `.material.opacity`) |
| `glassMat(op)` / `waterMat()` | glass panes, water |
| `popIn(t, at, dur)` | 0 → 1 with overshoot, for parts and chip scale |
| `pin(el, worldVec, opacity, scale)` | pins an HTML chip over a world point |
| `placeTagAt(id, x, dy)` | puts a label under the floor at world x |
| `makeTyper(text, at)` | returns `(t) => …` that types line 2 with a caret (keep ≤ ~24 chars) |
| `walkBetween(t, t0, t1, [x, z], [x, z])` | `{ x, z, w, u }`, `w` is the walk-pose blend |
| `yawToward(dx, dz)`, `smooth`, `easeInOut`, `backOut`, `clamp`, `lerp`, `mulberry32(seed)` | maths |
| `handWorld(fig, "R", out)`, `headTop(fig)`, `fig.torso.localToWorld(v)` | attach props to a figure |
| `updateMotes(t)`, `placeCamera(t, shake, DUR)` | call every frame |

## Chips, labels, line 2

Chips are `<div class="chip …">` elements in `#chips` (created by `new_video.py`); they start
invisible and `pin()` sets position, opacity and scale every frame. Change `textContent` for tickers
(Year 1 → 10, Day 1 → 240). Extra decorative ones (♪ notes) can be created in JS and appended to
`#chips`. Keep them from overlapping: stack vertically ≥ 0.38 units apart and offset x for long ones.

## Beat timing that works

- Motion from frame 0: someone is already doing the thing at 0.0s.
- 0–6s: the two paths (grey repeats, blue builds); chips pop one per beat.
- 6–8s: the test or the failure (denied, yanked, chair pulled, misses the rung).
- 8.5–12s: the kind payoff; line 2 types at ~10.0–10.3s; the dip handles the loop.

## Gotchas already hit

- **State must be a pure function of t.** A cached "where it dropped" value made the-leash draw
  different frames depending on seek order. Compute fixed positions instead.
- Tall props (ladders, cables) crossing the frame line: cap them below y ≈ 3.2 and hide anything
  hauled upward once it passes that height.
- Chips overlapping each other or a prop: check every snapshot with chips on screen.
- Geometry rebuilt per frame (tubes, ropes) must `scene.remove` + `geometry.dispose()` the old one.
- No `Math.random()`/`Date.now()`: use `mulberry32(seed)` once at build time.
- Brand: no red/orange/gold even for "error" states.

## Skeleton

```js
import { THREE, scene, renderer, camera, FLOOR_Y, mats, clamp, lerp, smooth, makeFigure, applyPose,
  mixPose, walkPose, hipHeight, POSES, GREY_START, GREY_END, updateMotes, placeCamera, box, add, std,
  makeGlow, popIn, pin, placeTagAt, makeTyper, walkBetween, yawToward } from "./rig.js";
const DUR = 12;
// layout constants, story beats (one const per beat, in seconds), props, figures, pose functions
function renderAt(t) {
  t = clamp(t, 0, DUR);
  placeCamera(t, new THREE.Vector3(), DUR);
  camera.updateMatrixWorld();
  // props(t); poseGrey(t); poseBlue(t); updateMotes(t); drawHud(t);
  placeTagAt("lbl-emp", -1.6); placeTagAt("lbl-own", 1.6);
  typeLine(t);
  renderer.render(scene, camera);
}
window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
renderAt(window.__hfThreeTime || 0);
```
