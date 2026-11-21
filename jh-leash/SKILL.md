---
name: jh-leash
description: "13learns Job haters video \"The Leash\" (\"Still on the leash.\"). Two desks on the left, a glowing WEEKEND door on the right. Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (drawLeash)."
---

# The Leash: "Still on the leash." (13learns Job haters)

- **Project:** `videos/the-leash/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 12s, seamless loop, no VO)
- **Script:** `SCRIPTS-7.md` §5
- **Delivered:** `renders/13learns-leash.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

The Leash: two desks on the left, a glowing WEEKEND door on the right. Both figures get up at 0.0s; blue unclips his lanyard at once and walks out into the light. Grey walks toward the door too, but his lanyard is a leash back to his laptop: it goes taut, a message pings, and it yanks him back into his chair. Saturday, then Sunday, he gets a little less far each time. Then blue walks back, unclips grey's lanyard, and they walk to the door together.

## The script (as written)

**Pattern used:** the loser loops (#9), you vs the job's reach. Burnout and always being on call
**Frame line (top):** STILL ON THE LEASH. (line 2 at the payoff, in blue: UNCLIP IT.)
**Labels:** left: Always on · right: Unclipped
**Chips:** over the laptop: "Quick question?" → "Just one thing" → "Can you hop on?"; a clock chip: "Fri 6:04 PM" → "Sat 10:12 AM" → "Sun 9:47 PM"
**Length:** 12s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–0.8s | Hook: unclipped | Both get up from their desks. Blue unclips his lanyard at once and it drops. | STILL ON THE LEASH. · Fri 6:04 PM | chair scrape, click |
| 0.8–2.6s | Snap back 1 | Grey walks toward the glowing WEEKEND door. His lanyard stretches back to the laptop, goes taut, a ping, and it yanks him back into his chair. Blue walks out into the light. | Quick question? | steps, stretch, ping, whoosh, thud |
| 2.6–8.2s | Twice more | Saturday, then Sunday: he gets a little less far each time. Grey greys. | Sat 10:12 AM · Just one thing / Sun 9:47 PM · Can you hop on? | ping, whoosh, thud ×2 |
| 8.2–12s | Kind payoff | Blue walks back, reaches over and unclips grey's lanyard. It drops. They walk to the door together. Line 2 types in. Dip, loop. | STILL ON THE LEASH. / UNCLIP IT. | steps, click, typing, sparkle |

**Post caption:** If a ping on Sunday can pull you back to your desk, you're not off. You're on a long leash. What would you do with a weekend that's actually yours?
**Loop point:** both getting up from their desks.

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Still on the leash."
- Label `#lbl-emp` (`index.html`): "Always on"
- Label `#lbl-own` (`index.html`): "Unclipped"
- Chips (`#chips` in `index.html`, pinned to 3D points by scene.js): `#clock` "Fri 6:04 PM" (numbers), `#msg` "Quick question?" (light), `#door` "WEEKEND" (blue)
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Unclip it."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 12;
const DESK_X = -2.5;
const CHAIR_X = -1.85;
const SEAT_H = 0.46;
const GZ = 0.3; // grey's desk, in front
const BZ = -0.75; // blue's desk, behind
const DOOR = { x: 2.55, z: -0.45, w: 0.9, h: 1.95 };
const SIT_X = CHAIR_X + 0.1;
const CYCLES = [0.0, 2.8, 5.6];
const REACH_X = [-0.25, -0.6, -0.95];
const CLOCK = ["Fri 6:04 PM", "Sat 10:12 AM", "Sun 9:47 PM"];
const MSG = ["Quick question?", "Just one thing", "Can you hop on?"];
const PING = 1.9; // into each cycle
const B_UNCLIP = [0.45, 0.75];
const B_OUT = [0.9, 2.5];
const B_BACK = [8.25, 9.2];
const G_TURN = [8.9, 9.3];
const UNCLIP = [9.3, 9.6];
const G_UP = [9.65, 10.0];
const GO = [10.05, 11.85];
const TYPE_LINE_AT = 10.2;
const SLUMP = { ...CHAIR_SIT, lean: 0.45, head: -0.5, shL: 0.3, elL: 0.3, shR: 0.3, elR: 0.3 };
const STRAIN = { ...STAND, lean: 0.45, head: 0.15, thL: 0.35, knL: -0.2, thR: -0.35, knR: -0.5, shL: 0.9, elL: 0.3, shR: 0.7, elR: 0.3 };
const YANKED = { ...STAND, lean: -0.35, head: -0.2, thL: 0.5, knL: -0.3, thR: 0.25, knR: -0.2, shL: 1.6, elL: 0.3, shR: 1.4, elR: 0.3 };
const STRETCH = { ...REACH, head: 0.3, lean: -0.08 };
const UNCLIP_P = { ...STAND, shR: 0.9, elR: 1.6, shL: 0.1, head: -0.3 };
const SITTING_YAW = -Math.PI;
const DROP_FROM = { blue: new THREE.Vector3(SIT_X + 0.2, FLOOR_Y + 1.5, BZ), grey: new THREE.Vector3(SIT_X + 0.15, FLOOR_Y + 1.15, GZ) };
```

## How `scene.js` is built

Sections, in order: layout · story beats · desks, chairs, laptops · the weekend door · figures · the lanyards · HTML · frame.

Functions:
- `cycleState(t, c0, xmax, k)`: one attempt at the weekend: get up, walk, strain, ping, yanked back, sit
- `stateGrey(t)`
- `stateBlue(t)`
- `place(fig, st)`
- `drawLeash(who, fig, t, clipOff, maxLen)`
- `drawHud(t)`
- `renderAt(t)`: frame

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for The Leash as one premixed, motion-synced track. Timing mirrors scene.js: both chairs scraping back at 0.0s, blue's clip coming off, his steps out to the WEEKEND door and a soft open-air bed while he stands in it; then, three times, grey's steps toward the door, the lanyard creaking taut, the message ping, the yank (a whoosh) and the thud back into his chair. Then blue's steps back, the clip on grey's lanyard, a chime, both walking out together, and the payoff. Grey sits left in the stereo field, blue right. Owned synths and ../../sfx-library only.

Owned synths: `air_whoosh`, `floor_step`, `metal_creak`, `soft_thud`.
`sfx-library/` sounds: `chime`, `click`, `notification`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-leash && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-leash/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/leash
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-leash && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-leash   # run in the background
```
`render.sh` writes `renders/13learns-leash.mp4`.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
