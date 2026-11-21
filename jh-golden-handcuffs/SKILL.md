---
name: jh-golden-handcuffs
description: "13learns Job haters video \"Golden Handcuffs\" (\"Every raise made it heavier.\"). Both figures are chained by the wrist to their desks, each with a key on a lanyard. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makeDesk, makeChain, drawChain, makeKey)."
---

# Golden Handcuffs: "Every raise made it heavier." (13learns Job haters)

- **Project:** `videos/golden-handcuffs/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-2.md` §4
- **Delivered:** `renders/Posted/13learns-golden-handcuffs.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

Golden Handcuffs: both figures are chained by the wrist to their desks, each with a key on a lanyard. Blue unlocks himself, trips, gets up and builds. Grey takes raise after raise; every raise snaps coin plates onto his cuff until he can't lift it. The key never left his neck.

## The script (as written)

**Pattern used:** the chain nobody came to cut (3.2M), told as raises and bonuses that make the cuff heavier
**Frame line (top):** EVERY RAISE MADE IT HEAVIER. (at the payoff, a second line types in: THE KEY WAS IN HIS POCKET.)
**Labels:** Comfortable / Free
**Small ticker under grey:** Salary $60k → $140k
**Props:** each figure cuffed by one wrist to a heavy office desk with a chain. A silver key hangs on a lanyard round each neck. Every raise adds a coin-shaped plate to grey's cuff, so it grows shinier and heavier.
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–2.5s | Hook: both chained | Both work at their cuffed desks. Blue tugs the chain and looks at the door. Grey doesn't notice his chain. | EVERY RAISE MADE IT HEAVIER. · $60k | chain rattle, typing |
| 2.5–4.5s | The raise | A coin-plate snaps onto grey's cuff ("+$15k") and he smiles. Blue lifts the key from his own neck, unlocks the cuff, and it drops with a clank. | $75k | plate snap, key turn, cuff clank |
| 4.5–7.5s | Two paths | Blue walks off, trips, gets up, and starts building a small blue frame structure. Grey gets plate after plate. He tries a step towards the door, but his arm now drags on the floor. | $90k → $140k | plate snaps (heavier each time), chain scrape |
| 7.5–9.5s | The turn | Grey tries to reach the door and the cuff is too heavy to lift. Blue's structure lights up. | $140k | heavy thud, light-on hum |
| 9.5–12s | Payoff | The camera pushes in on the key, still round grey's neck. "THE KEY WAS IN HIS POCKET." types in. Dip, loop. | EVERY RAISE MADE IT HEAVIER. / THE KEY WAS IN HIS POCKET. | soft key jingle, sparkle |

**Post caption:** Nobody locked you in. The raise just made leaving feel more expensive every year.
**Loop point:** both cuffed, grey's cuff plain again, blue's key back round his neck.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Every raisemade it heavier."
- Label `#lbl-emp` (`index.html`): "Comfortable"
- Label `#lbl-own` (`index.html`): "Free"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "He had the key the whole time."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const TAU = Math.PI * 2;
const GREY_X = -1.95;
const BLUE_X = 0.35;
const DESK_OFF = 0.67; // desk centre sits this far in front of the figure (both face -x)
const DESK_TOP = FLOOR_Y + 1.12;
const SITE_X = 2.75; // blue's workshop
const TUG = [1.0, 1.7];
const LOOK = [1.7, 2.3];
const KEY_OFF = [2.3, 2.9]; // left hand lifts the key off his chest
const KEY_TO_CUFF = [2.9, 3.5];
const UNLOCK = 3.75;
const TURN_OUT = [4.0, 4.4];
const WALK = [4.4, 5.1];
const TRIP = [5.1, 5.35];
const RISE = [5.35, 5.75];
const BUILD = [6.05, 6.3, 6.55, 6.8, 7.05, 7.3, 7.5];
const LIGHT_AT = 7.85;
const FACE_CAM = [8.0, 8.4];
const SHADES_AT = 8.5;
const RAISES = [[2.6, "+$15k", "$75k"], [4.6, "+$15k", "$90k"], [5.4, "+$15k", "$105k"], [6.2, "+$15k", "$120k"], [7.0, "+$20k", "$140k"]];
const COINS_PER_RAISE = 4;
const G_GLANCE = [5.9, 6.3];
const G_TRY1 = [6.35, 6.95];
const G_TRY2 = [7.6, 9.4];
const G_GIVE_UP = [9.4, 9.9];
const GLINT_AT = 10.2;
const LOOK_KEY = 10.9;
const TYPE_LINE_AT = 10.0;
const LINKS = 16;
const CHAIN_LEN = 1.05;
const KEY_SCALE = 1.7;
const COIN_R = 0.13;
const COIN_T = 0.05;
const POST_H = 1.3;
const SITE_PARTS = [
const TYPE = { ...STAND, lean: 0.22, head: 0.25, shL: 0.5, elL: 1.05, shR: 0.5, elR: 1.05 };
const TUG_P = { ...STAND, lean: -0.22, head: -0.1, thL: 0.25, knL: -0.2, thR: -0.2, knR: -0.1, shL: 0.4, elL: 0.5, shR: 0.75, elR: 0.05 };
const L_CHEST = { ...STAND, head: 0.3, shL: 0.35, elL: 2.25, shR: 0.55, elR: 0.6 };
const L_CUFF = { ...STAND, lean: 0.12, head: 0.45, shL: 0.85, elL: 1.15, shR: 0.95, elR: 0.6 };
const PLACE = { ...STAND, lean: 0.15, head: 0.1, shL: 1.45, elL: 0.25, shR: 1.35, elR: 0.3 };
const PLEASED = { ...TYPE, lean: 0.05, head: -0.18, shL: 0.35, elL: 0.9, shR: 0.4, elR: 0.9 };
const PULLED = { ...STAND, lean: 0.25, head: 0.0, thL: 0.35, knL: -0.3, thR: -0.25, knR: -0.15, shL: 0.6, elL: 0.4, shR: -0.55, elR: 0.1 };
const SLUMP = { ...HUNCH, shR: 0.1, elR: 0.05 };
const STEP = 0.5;
```

## How `scene.js` is built

Sections, in order: layout · story beats · materials · standing desks with an anchor ring on the near leg · chains · figures, cuffs, keys · grey's coin plates: hang from the cuff, pile up on the floor when it gets too long · blue's workshop · poses · HTML · frame.

Functions:
- `makeGlow(size, color = 0xe8eeff)`
- `makeDesk(figX)`: standing desks with an anchor ring on the near leg
- `makeChain()`
- `chainPoint(a, b, s, sag, out)`
- `drawChain(links, a, b)`
- `attachCuff(fig)`
- `makeKey()`
- `attachLanyard(fig)`
- `coinAt(i)`
- `drawCoins(t)`
- `roof(w, h, d, mat)`
- `drawSite(t)`
- `poseBlue(t)`
- `poseGrey(t)`
- `drawKeysAndCuffs(t)`
- `drawSalary(t)`
- `drawChips(t)`
- `placeTagAt(id, x, dy)`
- `drawLine2(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for Golden Handcuffs as one premixed, motion-synced track. Timing mirrors scene.js (typing, chain tugs, key, unlock, cuff drop, walk, trip, build, raises with their coin plates, grey's two attempts, the glint), so every sound lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `coin_clink`, `floor_step`, `metal_creak`, `pipe_clunk`, `rung_tick`, `soft_thud`.
`sfx-library/` sounds: `chime`, `click`, `click-soft`, `pop`, `sparkle`, `typing`, `whoosh-short`.

Rebuild: `cd videos/golden-handcuffs && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/golden-handcuffs/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/golden-handcuffs
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/golden-handcuffs && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh golden-handcuffs   # run in the background
```
`render.sh` writes `renders/13learns-golden-handcuffs.mp4`. The file already delivered is `renders/Posted/13learns-golden-handcuffs.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
