---
name: jh-who-quits-first
description: "13learns Job haters video \"Who Quits First?\" (\"The one with a reason stays.\"). Four lanes stacked like a leaderboard, each with a figure pushing a boulder up the same hill. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawBoulders, drawHouse, drawMonth, drawLabels)."
---

# Who Quits First?: "The one with a reason stays." (13learns Job haters)

- **Project:** `videos/who-quits-first/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-3.md` §2
- **Delivered:** `renders/13learns-who-quits-first.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Who Quits First?: four lanes stacked like a leaderboard, each with a figure pushing a boulder up the same hill. HYPE quits, then MOTIVATION, then MONEY (the surprise: he was winning). A REASON never stops; his boulder crests and rolls into a small blue house.

## The script (as written)

**Pattern used:** the elimination game ("Who lets go last?"), one question, a timer, archetype labels
**Frame line (top):** WHO QUITS FIRST?
**Labels:** four labels above the four figures: HYPE · MONEY · MOTIVATION · A REASON (only "A REASON" is blue)
**Ticker:** Month 1 → 36
**Props:** a long hill; four figures each pushing a boulder up their own lane side by side; the summit line glows faintly
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: all four push | Four identical figures shove four boulders up the slope in step. A timer runs. | WHO QUITS FIRST? · Month 1 → 2 | four strained grunts (thuds), stone grind |
| 2.0–3.0s | Out #1 | HYPE stops, shrugs, lets go. His boulder rolls back down and he walks off scrolling. | Month 2 · HYPE greys out | rumble down, shrug whoosh |
| 3.0–5.5s | Out #2 | MOTIVATION slows, then sits on his boulder halfway. It slides back with him on it. | Month 6 · MOTIVATION greys out | slide scrape |
| 5.5–7.5s | Out #3 (the surprise) | MONEY is furthest ahead, then his boulder grows heavier: a "$0" tag pops on it. He's crushed back down. | Month 14 · MONEY greys out | heavy thud, coin clink, rumble |
| 7.5–10.0s | The reason | A REASON (blue) keeps pushing alone, slower but never stopping. At Month 36 the boulder crests the summit and rolls down the far side into a glowing blue building. | Month 36 (blue) | final heave, crest whoosh, impact + chime |
| 10–12s | Payoff | "The one with a reason stays." types in under the frame line. Blue looks back at the three sitting at the bottom. Dip, loop. | WHO QUITS FIRST? / THE ONE WITH A REASON STAYS. | sparkle |

**Post caption:** Hype quits in a week. Motivation in a month. Money runs out. Write down your reason before you start.
**Loop point:** four boulders at the bottom, four figures in step.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Who quits first?"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "The one with a reason stays."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const S = 0.68; // figures are drawn at this scale so four lanes fit
const LANES = [
const X0 = -3.0; // where every boulder starts
const FOOT_X = -3.4; // bottom of the slope
const TOP_X = 2.2; // the crest / finish line
const FLAT_END = 2.7; // the top is flat until here, then drops away
const RISE = 0.55;
const R = 0.36; // boulder radius
const BOTTOM = -3.25; // where a boulder comes to rest after rolling back
const CREST = 9.3; // A REASON reaches the top
const HOUSE_HIT = 9.85;
const HYPE_QUIT = 2.0;
const MOT_STOP = 3.6;
const MOT_ROLL = [4.0, 4.9];
const MONEY_ZERO = 5.5;
const MONEY_ROLL = [6.0, 6.75];
const LOOK_BACK = 10.2;
const TYPE_LINE_AT = 10.2;
const MONTHS = [[0, 1], [HYPE_QUIT, 2], [MOT_STOP, 6], [MONEY_ZERO, 14], [CREST, 36]];
const DEPTH = 0.9;
const THICK = 0.42;
const SHRUG = { ...STAND, head: 0.12, shL: 0.25, elL: 1.35, shR: 0.25, elR: 1.35, ab: 0.4, eab: -0.35 };
const PHONE_WALK = { shL: 0.4, elL: 1.9, shR: 0.45, elR: 1.85, head: 0.45, lean: 0.1 };
const BALANCE_SIT = { ...SIT_TOP, head: -0.2, shL: 0.1, elL: 0.1, shR: 0.1, elR: 0.1, ab: 1.3 };
const QUIT_AT = { HYPE: HYPE_QUIT, MOTIVATION: MOT_STOP, MONEY: MONEY_ROLL[0] };
const LINE2 = "The one with a reason stays.";
```

## How `scene.js` is built

Sections, in order: lanes · story beats · materials · the hill, one slab per lane · boulders and pushers · HTML · frame.

Functions:
- `ground(lane, x)`
- `boulderX(id, t)`
- `makeGlow(size, color)`
- `moneyScale(t)`
- `drawBoulders(t)`
- `place(fig, pose, x, groundY, z = 0.05, yaw = 0, lift = 0)`: figures sit at 0.55 scale, so the hip height applyPose adds has to be scaled down too
- `pushPose(dist, rate = 1)`
- `quitFade(r, t, at)`
- `poseRow(r, t)`
- `drawHouse(t)`
- `drawMonth(t)`
- `drawLabels(t)`
- `drawZero(t)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Who Quits First? as one premixed, motion-synced track. Timing mirrors scene.js (four boulders grinding uphill, each quit with its roll-back and landing, the "$0" swell and crash, the month ticks, the crest and the house lighting up), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `counter_blip`, `metal_creak`, `quake_rumble`, `soft_thud`, `stone_crackle`, `stone_crash`.
`sfx-library/` sounds: `chime`, `click-soft`, `error`, `ping`, `pop`, `rumble-wheel-loop`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/who-quits-first && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/who-quits-first/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/who-quits-first
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/who-quits-first && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh who-quits-first   # run in the background
```
`render.sh` writes `renders/13learns-who-quits-first.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
