---
name: jh-either-way
description: "13learns Job haters video \"Either Way\" (\"Your words build something either way.\"). Everything either figure says becomes a speech bubble that hardens into a brick with the words on it. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawBricks, drawLight, drawLine2)."
---

# Either Way: "Your words build something either way." (13learns Job haters)

- **Project:** `videos/the-either-way/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-4.md` §6
- **Delivered:** `renders/13learns-either-way.mp4` (rendered)
- **Old A/B file:** `renders/Posted/13learns-either-way-alt.mp4`. It predates the one-version rule. Don't make new `-alt` renders.
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Either Way: everything either figure says becomes a speech bubble that hardens into a brick with the words on it. Grey's excuses stack into a wall in front of him, taller than he is; blue's next steps land one step higher each time and he climbs them to a glowing door on a ledge. Then he leans back out and says "Come on": that brick lands on grey's side as a first step.

## The script (as written)

**Pattern used:** words turn into objects ("We built this wall together.", 720K); two labels, side by side
**Frame line (top):** EVERY WORD IS A BRICK. (line 2 at the payoff: BUILD STAIRS, NOT WALLS.)
**A/B line 2:** YOU'RE BUILDING EITHER WAY.
**Labels:** left: Excuses · right: Next steps
**Props:** two figures on one dark floor with a glowing doorway in the far distance marked "YOUR OWN THING". Each speech bubble drops as a brick with its words on it. Grey's bricks stack into a wall in front of him; blue's bricks stack into a staircase.
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: first words | Both speak at 0.0s. Grey's bubble "Too risky" hardens into a brick and drops at his feet. Blue's "Let's test it" drops at his. | Excuses / Next steps · Too risky · Let's test it | pop, stone thud ×2 |
| 2.0–6.0s | Building | Bubbles come faster. Grey: "No time", "Bad economy", "Next year", "What if it fails" stack up into a wall that blocks his view of the door. Blue: "Ask one client", "Post it", "Ship it", "Fix it" stack into steps that he climbs. | each brick's words | pop + thud per brick, speeding up |
| 6.0–7.0s | The turn | Grey's wall reaches above his head and casts him into shadow. Blue's top step reaches the door's height. | EVERY WORD IS A BRICK. | heavy thud, bass hit |
| 7.0–9.5s | Through the door | Blue steps through the glowing doorway and the light fills his side. | (no new text) | steps, door whoosh, chime |
| 9.5–12s | Kind payoff | Blue leans back out and says one more word: "Come on". It drops as a brick on grey's side, as the first step against his wall. Grey looks at it and steps up. Line 2 types in. Dip, loop. | EVERY WORD IS A BRICK. / BUILD STAIRS, NOT WALLS. | pop, thud, typing, sparkle |

**Post caption:** You say the same number of words either way. Some build a wall in front of you; some build the stairs. Which bricks did you lay this week?
**Loop point:** both figures with no bricks yet, opening their mouths.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Every word is a brick."
- Label `#lbl-emp` (`index.html`): "Excuses"
- Label `#lbl-own` (`index.html`): "Next steps"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Build stairs, not walls."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const BRICK = { w: 1.3, h: 0.46, d: 0.6 };
const GREY_X = -3.45;
const WALL_X = -2.0;
const BLUE_X = 3.5;
const LEDGE = { x0: -1.15, x1: 0.15, z0: -1.5, z1: 0.3, top: 5 * BRICK.h };
const DOOR = { x: -0.5, z: -1.2, w: 0.85, h: 1.9 };
const GIFT_AT = { x: -3.0, z: 0.55 }; // where "Come on" lands, in front of grey's wall
const GREY_WORDS = [["Too risky", -0.2], ["No time", 1.9], ["Bad economy", 2.8], ["Next year", 3.7], ["What if it fails", 4.6]];
const BLUE_WORDS = [["Let’s test it", -0.05], ["Ask one client", 2.2], ["Post it", 3.1], ["Ship it", 4.0], ["Fix it", 4.9]];
const HARDEN = 0.6; // bubble → brick
const FALL = 0.3;
const SHADE = [5.4, 6.2];
const TO_LEDGE = [6.95, 7.45];
const INTO_DOOR = [7.5, 8.05];
const LIGHT = [7.9, 8.7];
const LEAN_OUT = [9.45, 9.75];
const COME_ON = 9.7;
const GIFT_FLY = [COME_ON + HARDEN + 0.15, COME_ON + HARDEN + 0.15 + 0.55];
const G_LOOK = [GIFT_FLY[1] + 0.05, GIFT_FLY[1] + 0.25];
const G_STEP = [GIFT_FLY[1] + 0.3, GIFT_FLY[1] + 0.7];
const TYPE_LINE_AT = 10.2;
const GIFT = { word: "Come on", at: COME_ON, who: blue, mat: blueBrick, side: -1, slot: new THREE.Vector3(GIFT_AT.x, FLOOR_Y + BRICK.h / 2, GIFT_AT...
const SHRUG = { ...STAND, head: -0.05, shL: 0.45, elL: 1.4, shR: 0.45, elR: 1.4, ab: 0.45, eab: -0.4 };
const POINT = { ...STAND, head: -0.1, shR: 1.35, elR: 0.15, shL: 0.15, elL: 0.25 };
const LOOK_UP = { ...STAND, head: -0.45, lean: -0.05, shL: 0.1, elL: 0.2, shR: 0.1, elR: 0.2 };
const SLUMP = mixPose(STAND, POSES.HUNCH, 0.35);
const WAVE = { ...STAND, lean: 0.25, head: 0.25, shR: 2.4, elR: 0.6, shL: 0.1, elL: 0.2 };
const LINE2 = "Build stairs, not walls.";
const TYPE_SECS = 0.041 * LINE2.length;
```

## How `scene.js` is built

Sections, in order: layout · the words · story beats · materials · the ledge and the door · figures · bricks · poses · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `bubbleAnchor(b, t)`
- `pinEl(el, v, opacity, scale = 1)`
- `drawBricks(t)`
- `poseGrey(t)`
- `poseBlue(t)`
- `drawLight(t)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Either Way as one premixed, motion-synced track. Timing mirrors scene.js: every word is a bubble pop, a crackle as it hardens into a brick, and a thud as the brick lands (grey's stone ones lower and heavier, blue's brighter); blue's step up onto each new one; the wall topping out; blue's walk through the door; "Come on" flying over the wall and landing as grey's first step. Grey sits left in the stereo field, blue right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `counter_blip`, `floor_step`, `soft_thud`, `stone_crackle`, `wheel_rumble`.
`sfx-library/` sounds: `chime`, `pop`, `sparkle`, `typing`, `whoosh-air-01`, `whoosh-air-02`, `whoosh-short`.
It still has an `--alt` flag from the old A/B end line. Leave it off, since the rule is one version only.

Rebuild: `cd videos/the-either-way && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-either-way/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/either-way
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-either-way && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-either-way   # run in the background
```
`render.sh` writes `renders/13learns-either-way.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
