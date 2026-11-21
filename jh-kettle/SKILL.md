---
name: jh-kettle
description: "13learns Job haters video \"The Kettle\" (\"Nothing happens at 99°.\"). Two kettles on two stoves with blue flames, big temperature counters climbing at 0.0s. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeStove, drawStove, drawScan, makeCounter)."
---

# The Kettle: "Nothing happens at 99°." (13learns Job haters)

- **Project:** `videos/the-kettle/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-8.md` §3
- **Delivered:** `renders/13learns-kettle.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Kettle: two kettles on two stoves with blue flames, big temperature counters climbing at 0.0s. At 62° grey leans in, sees nothing happening and switches off; his number drops, he relights, gets to 72° and switches off again. Blue's flame stays on and his number crawls up to 99°. A scan line turns the kettles see-through: grey's water is still, bubbles are forming at the bottom of blue's. At 100° it whistles and steams. Blue walks over and turns grey's flame back on, and they watch it climb together. Line 2 types at the payoff.

## The script (as written)

**Pattern used:** one big counter as the hero (#32), the loser loops (#9), X-ray of the hidden progress (#33)
**Frame line (top):** NOTHING HAPPENS AT 99°. (line 2 at the payoff, in blue: KEEP THE FLAME ON.)
**Labels:** left: Keeps switching off · right: Kept the flame on
**Counters:** a big temperature over each kettle. Grey's climbs, drops when he switches off, and climbs again (20° → 62° → 45° → 71° → 50°). Blue's climbs steadily, crawls 97, 98, 99, then hits 100°. Grey gets a dark chip, "Nothing yet", each time he gives up
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.9s | Hook: both on the stove | Two kettles on two stoves with blue flames, and both counters are already climbing at 0.0s. At 62° grey leans in, sees nothing happening and turns his flame off. | NOTHING HAPPENS AT 99°. · 20° → 62° · Nothing yet | gas hiss, knob click, flame out |
| 2.9–6.9s | Off, on, off | Grey's number drops to 45°. He relights, gets to 71°, looks, and switches off again. Blue's flame stays on and his number crawls up to 99°. | 45° → 71° / 99° | click, whoosh, hiss, click |
| 5.6–7.4s | The scan | A scan line passes over both kettles and they turn see-through. Grey's water is still. At the bottom of blue's, bubbles are forming and growing. | (no new text) | scan sweep, bubbling builds |
| 7.4–8.3s | 100° | The counter turns blue at 100°. The kettle whistles, steam pours out and the lid rattles. | 100° | whistle, steam hiss, lid rattle |
| 8.3–12s | Kind payoff | Blue walks over to grey's stove and turns his flame back on. Grey looks at him and the two of them watch it climb. Line 2 types in. Dip, loop. | NOTHING HAPPENS AT 99°. / KEEP THE FLAME ON. | steps, click, whoosh, typing, sparkle |

**Post caption:** Water at 99° looks exactly like water at 60°. Everything changes at 100. Most people keep switching off right before the boil. How many times have you turned your flame off?
**Loop point:** both kettles heating from 20°.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Nothing happens at 99°."
- Label `#lbl-emp` (`index.html`): "Keeps switching off"
- Label `#lbl-own` (`index.html`): "Kept the flame on"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#gnot` "Nothing yet" (dark negative)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Keep the flame on."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const G_X = -1.95;
const B_X = 1.95;
const G_STOVE = -1.15;
const B_STOVE = 1.15;
const STOVE_W = 0.8;
const STOVE_H = 1.0;
const STOVE_D = 0.6;
const TOP_Y = FLOOR_Y + STOVE_H;
const KNOB_Y = TOP_Y - 0.14;
const KNOB_Z = STOVE_D / 2 + 0.03;
const B_AT_G = [-0.72, 0.58]; // where blue stands to reach grey's knob
const G_ON = [[0, 2.5], [4.0, 5.6], [9.75, 99]]; // grey's flame on
const RATE_ON = 16.8;
const RATE_OFF = 11;
const G_PEEK = [[1.95, 2.5], [5.05, 5.6]];
const G_KNOB = [[2.35, 2.75], [3.75, 4.15], [5.45, 5.85]];
const G_NOT = [[2.6, 3.8], [5.7, 7.0]];
const G_FOLD = 6.2;
const BLUE_99 = 6.4;
const BOIL = 7.4;
const SCAN = [5.6, 6.3];
const XRAY_OFF = [7.8, 8.2];
const B_WALK = [8.4, 9.45];
const B_KNOB = [9.45, 9.95];
const B_BACK = [10.0, 10.5];
const TYPE_LINE_AT = 10.2;
const WAIT = { ...STAND, head: -0.12, shL: 0.12, elL: 0.35, shR: 0.1, elR: 0.35 };
const PEEK = { ...STAND, lean: 0.55, head: -0.45, thL: 0.1, knL: -0.18, shL: 0.35, elL: 0.5, shR: 0.4, elR: 0.5 };
const KNOB = { ...STAND, lean: 0.6, head: -0.5, thL: 0.25, knL: -0.5, thR: -0.05, knR: -0.35, shL: 0.1, elL: 0.3, shR: 0.75, elR: 0.1 };
const FOLD = { ...STAND, head: -0.2, shL: 0.75, elL: 1.6, shR: 0.7, elR: 1.6, ab: 0.15, eab: -0.75 };
const LOOK_UP = { ...STAND, lean: -0.1, head: 0.35, shL: 0.1, elL: 0.3, shR: 0.1, elR: 0.3 };
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · stove + kettle · scan line · figures · HTML · frame.

Functions:
- `greyTemp(t)`
- `makeStove(x, dir)`: stove + kettle
- `drawStove(s, flameOn, temp, t, xr, boil)`
- `drawScan(t)`
- `xray(t)`
- `poseGrey(t)`
- `poseBlue(t)`
- `makeCounter(id)`: HTML
- `drawCounter(c, temp, x, t, boilAt)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Kettle as one premixed, motion-synced track. Timing mirrors scene.js: the gas hiss under each lit burner (grey's switches on and off, blue's never does), a knob click and a whoomp at every switch, soft ticks as blue's number climbs, the scan sweep with a low hum and bubbling that builds in blue's kettle, then 100°: a hit, the whistle, a steam hiss and the lid rattling. Blue's steps over, the click and whoomp as grey's flame comes back on, line 2 and a sparkle. The whistle is an owned synth. Grey left, blue right. Nothing needs attribution.

Owned synths: `SR`, `_bubbles`, `air_whoosh`, `band`, `counter_blip`, `floor_step`, `norm`, `rung_tick`.
`sfx-library/` sounds: `click`, `impact-bass-1`, `notification`, `sparkle`, `typing`, `whoosh-air-01`.

Rebuild: `cd videos/the-kettle && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-kettle/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/kettle
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-kettle && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-kettle   # run in the background
```
`render.sh` writes `renders/13learns-kettle.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
