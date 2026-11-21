---
name: jh-pillars
description: "13learns Job haters video \"The Pillars\" (\"One income is one point of failure.\"). Grey stands on one big pillar (one income); blue on a platform of skinny posts. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawPillar, drawPosts, drawPlatform, drawYear)."
---

# The Pillars: "One income is one point of failure." (13learns Job haters)

- **Project:** `videos/the-pillars/` (HyperFrames 0.8.181 + Three.js, 1080×1920, 30fps, 10s, seamless loop, no VO)
- **Script:** `SCRIPTS.md` §3
- **Delivered:** `renders/Posted/13learns-the-pillars.mp4` (posted)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Pillars: grey stands on one big pillar (one income); blue on a platform of skinny posts. A shock topples grey's pillar; blue loses one post, wobbles, holds, and keeps adding more.

## The script (as written)

**On-screen counter:** Year 1 → 10
**Props:** grey stands on one thick stone pillar; blue on a thin platform held up by skinny blue posts. Income counts under the labels.

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–3.5s | Hook: who's safer? | Grey stands tall and steady on his big solid pillar. Blue wobbles on a platform held up by a single skinny post, arms out for balance. He adds a post every beat; the wobble settles. | Year 1 → 4 · 1 income vs 1 → 5 incomes | wobble creaks, post "thunk" per income |
| 3.5–5.0s | The shock | The whole scene shakes. Grey's pillar cracks and topples; grey falls with it and lands on the rubble. A "Laid off" tag stamps in above him. One of blue's posts snaps too: his platform dips, he wobbles, and holds. | Year 5 · "Laid off" · 1 → 0 income · 5 → 4 incomes | rumble, crack, stone crash, body fall, one post snap |
| 5.0–8.5s | Two paths | Grey sits in the rubble, fading to grey. Blue calmly adds posts: 5, 6, 7. | Year 6 → 9 · 4 → 7 incomes | post thunks |
| 8.5–10s | Payoff | Year 10: blue stands on a rock-steady platform, hands on hips, shades on. Dip, loop. | Year 10 (blue) | sparkle |

**Post caption:** "Job security" is one email away from zero. How many pillars are you standing on?
**Loop point:** pillar rebuilt, grey on top; blue back on his single post.

## On-screen text (where it lives)

- Label `#lbl-emp` (`index.html`): "Employee"
- Label `#lbl-own` (`index.html`): "Owner"

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const GREY_X = -1.75;
const BLUE_X = 1.75;
const PLAT_TOP = 0.55;
const SHOCK_AT = 3.55;
const SNAP_AT = 3.75; // blue's post breaks
const COLLAPSE_AT = 3.9; // grey's pillar gives way
const CAP_T = 0.12;
const DRUMS = 6;
const DRUM_H = (PLAT_TOP - CAP_T - 0.08 - FLOOR_Y) / DRUMS;
const R = 0.4;
const FALLS = [
const STUMP_TOP = FLOOR_Y + 0.08 + DRUM_H * 2;
const PLAT_T = 0.09;
const POST_LEN = PLAT_TOP - PLAT_T - FLOOR_Y;
const POSTS = [
const SNAP_H = 1.15; // the broken post keeps this much stump
const FLAIL = { ...TUCK, shL: 2.7, shR: 2.5, elL: 0.6, elR: 0.7, lean: -0.2, head: 0.3 };
const YEARS = [[0, 1], [0.9, 2], [1.8, 3], [2.7, 4], [SHOCK_AT, 5, true], [5.0, 6], [5.9, 7], [6.8, 8], [7.7, 9], [8.55, 10, true]];
```

## How `scene.js` is built

Sections, in order: layout · grey's pillar · blue's platform + posts · figures · counters + callout · frame.

Functions:
- `drawPillar(t)`
- `postCount(t)`
- `drawPosts(t)`
- `platTilt(t)`: platform tilt: wobbles less with every post; jolts when a post snaps
- `poseGrey(t)`
- `poseBlue(t, tilt)`
- `drawPlatform(t, tilt, kick)`
- `drawYear(t)`
- `drawIncomes(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Pillars as one premixed, motion-synced track. Timing mirrors scene.js (platform wobble, post schedule, shock, snap, pillar collapse, falls), so each creak, thunk and crash lands on its frame. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `metal_creak`, `pipe_clunk`, `post_snap`, `quake_rumble`, `soft_thud`, `stone_crackle`, `stone_crash`.
`sfx-library/` sounds: `blip-counter-01`, `blip-counter-02`, `body-fall`, `click`, `click-soft`, `ping`, `sparkle`, `whoosh-air-01`.

Rebuild: `cd videos/the-pillars && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-pillars/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.181 snapshot --at 0.4,2,4,6,8,9.6 --no-end --describe false -o <scratchpad>/pillars
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-pillars && npx --yes hyperframes@0.8.181 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-pillars   # run in the background
```
`render.sh` writes `renders/13learns-pillars.mp4`. The file already delivered is `renders/Posted/13learns-the-pillars.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
