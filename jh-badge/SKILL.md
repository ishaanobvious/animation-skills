---
name: jh-badge
description: "13learns Job haters video \"The Badge\" (\"The badge was never yours.\"). Grey taps his badge on an office turnstile, faster and faster, ten years of blue \"granted\" lights, the flap swinging open every time. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawDoor, drawBox, drawGate)."
---

# The Badge: "The badge was never yours." (13learns Job haters)

- **Project:** `videos/the-badge/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-7.md` §3
- **Delivered:** `renders/13learns-badge.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Badge: grey taps his badge on an office turnstile, faster and faster, ten years of blue "granted" lights, the flap swinging open every time. On the right, blue builds a door of his own: posts, lintel, door, lock. Then one tap is denied, and again, and a box of desk things drops into grey's arms. Blue turns his key, his door swings open on blue light, and he holds it for grey, who walks over with his box and goes in.

## The script (as written)

**Pattern used:** visible vs hidden (#6): ten years of green lights, then one red one. A familiar object (#7)
**Frame line (top):** THE BADGE WAS NEVER YOURS. (line 2 at the payoff, in blue: THE DOOR CAN BE.)
**Labels:** left: Their building · right: His own door
**Stats:** a "Year 1 → Year 10" chip over grey, then "ACCESS DENIED"
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–6.0s | Ten years of green | Grey taps his badge on a turnstile reader, faster and faster. Green light, beep, the flap opens; the year ticks up. Blue builds a door frame on the right: posts, lintel, door. | THE BADGE WAS NEVER YOURS. · Year 1 → Year 10 | beeps, flap swish, hammer clunks |
| 6.0–7.4s | Denied | One tap: red. The flap stays shut. He taps again: red. A box of desk things drops into his arms. | ACCESS DENIED | error buzz ×2, thud |
| 7.4–9.0s | His own key | Blue turns a key in his door. It swings open and blue light pours out. | (no new text) | click, creak, swell |
| 9–12s | Kind payoff | Blue holds the door and waves. Grey walks over with his box and goes in. Line 2 types in. Dip, loop. | THE BADGE WAS NEVER YOURS. / THE DOOR CAN BE. | steps, typing, sparkle |

**Post caption:** Ten years of green lights, and one morning it's red. The badge was always theirs. Build a door you hold the key to.
**Loop point:** grey's first tap, green.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "The badge was never yours."
- Label `#lbl-emp` (`index.html`): "Their building"
- Label `#lbl-own` (`index.html`): "His own door"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#year` "Year 1" (numbers), `#denied` "ACCESS DENIED" (dark negative)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "The door can be."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const G_AT = [-2.0, 0];
const READER = { x: -1.62, h: 1.12 };
const GATE = { x: -1.3, z: -0.42 };
const DOOR = { x0: 1.1, x1: 1.9, h: 1.85, z: -0.1 };
const B_AT = [0.72, 0.05];
const TAPS = [0.15];
const DENIED = [6.2, 6.75];
const BOX_DROP = [7.05, 7.35];
const PARTS = { postL: 0.6, postR: 1.6, lintel: 2.7, door: 4.0, lock: 5.2 };
const KEY = [7.35, 7.75];
const OPEN = [7.75, 8.35];
const WAVE = [8.4, 9.2];
const G_WALK = [8.85, 10.95];
const TYPE_LINE_AT = 10.0;
const TAP = { ...STAND, lean: 0.08, head: -0.1, shR: 1.15, elR: 0.25, shL: 0.1 };
const CARRY = { ...STAND, lean: 0.12, head: -0.2, shL: 0.75, elL: 0.95, shR: 0.75, elR: 0.95 };
const HAMMER = (t) => ({ ...STAND, lean: 0.12, shR: 1.4 + 0.7 * Math.max(0, Math.sin(t * 16)), elR: 0.5, shL: 0.9, elL: 0.4 });
const WAVE_P = (t) => ({ ...STAND, shR: 2.1 + 0.35 * Math.sin(t * 11), elR: 0.6 + 0.3 * Math.sin(t * 11), shL: 0.1 });
```

## How `scene.js` is built

Sections, in order: layout · story beats · the turnstile and reader · blue's door · the box of desk things · figures · HTML · frame.

Functions:
- `build(m, t, at)`
- `drawDoor(t)`
- `poseGrey(t)`
- `poseBlue(t)`
- `drawBox(t)`
- `drawGate(t)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Badge as one premixed, motion-synced track. Timing mirrors scene.js: a bright "granted" beep and a flap swish on every badge tap (eighteen of them, speeding up across ten years), blue's hammering and a clunk as each piece of his door goes up, then two flat "denied" tones, the box of desk things landing in grey's arms, blue's key turning, the door creaking open on a swell of light, the wave, grey's steps over with the box, and the payoff. Grey sits left in the stereo field, blue right. Owned synths and ../../sfx-library sounds only.

Owned synths: `air_whoosh`, `counter_blip`, `floor_step`, `metal_creak`, `pipe_clunk`, `rung_tick`, `soft_thud`.
`sfx-library/` sounds: `chime`, `click`, `error`, `glass-tink-01`, `impact-bass-1`, `sparkle`, `typing`, `whoosh-cinematic`.

Rebuild: `cd videos/the-badge && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-badge/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/badge
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-badge && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-badge   # run in the background
```
`render.sh` writes `renders/13learns-badge.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
