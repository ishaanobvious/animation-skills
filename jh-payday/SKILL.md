---
name: jh-payday
description: "13learns Job haters video \"Payday\" (\"A salary arrives once. The bills arrive all month.\"). One huge coin lands in grey's wallet on Day 1 and labelled hands reach in from the edge of the frame until it's gone. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeStool, makeWallet, drawBigCoin, drawHands)."
---

# Payday: "A salary arrives once. The bills arrive all month." (13learns Job haters)

- **Project:** `videos/payday/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 10s, seamless loop, no VO)
- **Script:** `SCRIPTS-2.md` §3
- **Delivered:** `renders/Posted/13learns-payday.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Payday: one huge coin lands in grey's wallet on Day 1 and labelled hands reach in from the edge of the frame until it's gone. Blue's wallet is fed by thin pipes that never stop dripping. By Day 30 grey's next coin lands with the hands already reaching; blue's wallet overflows.

## The script (as written)

**Pattern used:** the tortoise and hare (6.6M Income vs Expenses), retold as one paycheck vs many streams
**On-screen counter:** Day 1 → 30
**Labels:** Paycheck / Pipelines
**Props:** a wallet on a stool for each figure. Grey gets one big coin on Day 1, and labelled hands reach in: Rent, EMI, Tax, Subscriptions, Food. Blue has 5 thin pipes dripping small coins into his wallet nonstop.
**Length:** 10s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.0s | Hook: payday | Day 1: a huge coin drops into grey's wallet. He throws his arms up. Blue's pipes drip tiny coins and he looks unimpressed. | Day 1 · Paycheck +$4,000 · Pipelines +$40 | big coin thunk, small drips |
| 2.0–4.5s | The hands | Labelled hands slide in from the edges and each takes a chunk: RENT, EMI, TAX, SUBSCRIPTIONS. Grey's coin shrinks with every grab. | Day 2 → 6 · $4,000 → $600 | grab whooshes, coin scrape |
| 4.5–6.0s | The turn | Day 7: grey's wallet is empty and he turns it upside down. Blue's wallet is still filling, drip by drip, and the coins are now landing faster. | Day 7 · $0 (grey) · Pipelines $40 → $1,900 (blue) | empty wallet flap, coin trickle speeds up |
| 6.0–8.5s | Two paths | Grey sits on his stool and waits, watching a "Day 30" calendar that won't turn. Blue adds a 6th pipe. | Day 8 → 29 | slow clock, pipe clunk |
| 8.5–10s | Payoff | Day 30: grey's next coin drops and the hands are already reaching in. Blue's wallet overflows and glows. Dip, loop. | Day 30 · $4,000 vs $6,200 | big coin thunk, sparkle |

**Post caption:** You don't have a money problem. You have a "money arrives once a month" problem.
**Loop point:** Day 1, grey's wallet empty and waiting, blue's pipes at a slow drip.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Money in once.Out all month."
- Label `#lbl-emp` (`index.html`): "Paycheck"
- Label `#lbl-own` (`index.html`): "Pipelines"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 10;
const TAU = Math.PI * 2;
const G_STOOL = -2.2;
const GREY_X = -1.45; // faces his stool (-x)
const B_STOOL = 1.95;
const BLUE_X = 0.95;
const STOOL_TOP = FLOOR_Y + 0.62;
const WALLET_BASE = STOOL_TOP + 0.025;
const EDGE_X = -4.7; // the hands come from beyond the left edge of the frame
const DROP1 = [0.1, 0.42];
const DROP2 = [8.5, 8.82];
const PAY = 4000;
const GRABS = [
const REACH_IN = 0.28;
const HOLD = 0.08;
const PULL_OUT = 0.4;
const FLIP = [4.75, 5.8]; // grey lifts the wallet, turns it over, puts it back
const G_SIT = [5.9, 6.3];
const G_UP = [8.6, 8.95];
const HOVER = [9.05, 9.5]; // all the hands come back for the new coin
const NEW_PIPE = [6.4, 6.8];
const B_TURN = [4.6, 5.0];
const B_REACH = [6.15, 6.95];
const B_FACE = [7.0, 7.4];
const SHADES_AT = 9.0;
const OVERFLOW_AT = 8.4;
const BIG_R = 0.36;
const PIPES = [
const SMALL_R = 0.06;
const SMALL_T = 0.028;
const FALL = 0.3;
const STACK_KEYS = [[0, 0], [2, 6], [4.5, 16], [6, 36], [8.4, 72], [9.4, 104]];
const BAL_KEYS = [[0, 40], [2, 300], [4.5, 750], [6, 1900], [8.4, 4300], [9.4, 6200]];
const COLS = [-0.21, -0.07, 0.07, 0.21];
const ROWS = 18;
const LOOK_UP = { ...STAND, head: -0.35 };
const CHEER = { ...REACH, head: -0.2 };
const HOLD_W = { ...STAND, lean: 0.12, head: 0.25, shL: 1.15, elL: 0.75, shR: 1.15, elR: 0.75 };
const SIT_WAIT = { ...SIT, head: -0.2 };
const ARMS_X = { ...STAND, head: 0.05, shL: 0.3, elL: 1.45, shR: 0.35, elR: 1.4, ab: 0.3, eab: 1.25 };
const NOD = { ...STAND, head: 0.35, lean: 0.05 };
const DAYS = [[0, 1], [2.2, 2], [2.7, 3], [3.2, 4], [3.7, 5], [4.3, 6], [4.75, 7], [6.0, 8], [6.25, 10], [6.5, 13], [6.8, 16], [7.1, 19], [7.4, 22]...
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · stools and wallets · grey's paycheck: one big coin · the hands · blue's pipes · figures · HTML · frame.

Functions:
- `makeGlow(size, color)`
- `makeStool(x)`: stools and wallets
- `makeWallet()`
- `balance(t)`
- `coinScale(t)`
- `drawBigCoin(t, walletPos)`
- `placeArm(h, from, to)`
- `drawHands(t, coinPos)`
- `drawPipes(t, stackTop)`
- `drawStack(t)`
- `poseGrey(t)`
- `drawGreyWallet(t)`
- `poseBlue(t)`
- `drawDay(t)`
- `drawBalances(t)`
- `drawGrabLabels(t)`
- `drawPayChip(t)`
- `placeTagAt(id, x, dy)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Payday as one premixed, motion-synced track. Timing mirrors scene.js (both coin drops, each hand reaching in and grabbing, the empty wallet, every coin that drips out of blue's pipes, the sixth pipe, the overflow, the hands coming back), so every sound lands on its frame. The drip schedule is rebuilt with the same seeded generator the scene uses. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `coin_clink`, `counter_blip`, `floor_step`, `pipe_clunk`, `soft_thud`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `coin-cascade-02`, `error`, `ping`, `pop`, `sparkle`, `whoosh-air-01`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/payday && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/payday/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2,4,6,8,9.6 --no-end --describe false -o <scratchpad>/payday
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/payday && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh payday   # run in the background
```
`render.sh` writes `renders/13learns-payday.mp4`. The file already delivered is `renders/Posted/13learns-payday.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
