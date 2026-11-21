---
name: job-haters
description: Make 13learns "Job haters" videos, the 12s faceless 3D metaphor loops (blue doer vs grey average employee, a frame line on top, a kind payoff). Use whenever the user asks for new Job haters / 13learns videos, a new batch, more ideas or scripts for the channel, "videos like these", or to rebuild/re-render one. Covers finding ideas, confirming them with the user, writing SCRIPTS-N.md, scaffolding a HyperFrames + Three.js project, writing scene.js and the SFX mix, snapshot review, render and delivery.
---

# Job haters videos (13learns)

Vertical 1080×1920, 12s, seamless loops, no voiceover. Two stick figures act out one metaphor about
jobs vs building your own thing: **blue = the one who chose differently, white/grey = the average
path**. A short frame line sits on top, two labels sit under the floor, small chips carry the numbers,
and a blue line 2 types in at the payoff. The ending is kind: blue helps grey, never gloats.

Project root: the folder that holds `.claude/skills/` (paths below are relative to it).
Each video is its own HyperFrames project in `videos/<name>/`; finished renders go to
`renders/13learns-<short>.mp4` (`<short>` = name without a leading `the-`).

## House rules (from the user, do not break)

- **One version per video.** No A/B line 2s, no `-alt.mp4`.
- **No vidIQ**, ever, not even a balance check.
- **Brand:** blue `#1A5DE6` / `#4A84F7` on dark / figure `#2F6DF0`, white `#F5F7FA`, cool blacks, Space
  Grotesk, 13learns logo bottom-centre. **No gold, no warm tones** (a "denied"/negative state is a
  dark chip, not red). Spec: `brand/frame.md`.
- **Audio:** only owned synths or `sfx-library/` sounds (CC0/owned/Pixabay), nothing that needs credit,
  never audio lifted from reference reels. Music is added in-app at posting.
- **Borrow structure only** from reference reels, never scenes, captions, logos or audio.
- **Confirm ideas before building.** Propose a shortlist, wait for the user's pick, then build.

## Workflow

### 1. Find ideas

Read `INSPIRATION.md` (31 numbered patterns) and the latest `SCRIPTS-*.md` so nothing repeats; list
existing titles with `grep -h "^## [0-9]" SCRIPTS*.md` and `ls videos/`.

Sources, in order:
1. **Reel links the user sends**: open each in the built-in browser, close the sign-up popup, read the
   caption with `get_page_text`, play the video and zoom-screenshot the video rect every ~1.5s.
   Write the new patterns into `INSPIRATION.md` as a dated update.
2. **No links:** @mindset.therapy, @neuronvisuals and their Pinterest board need a login (checked
   2026-10-30), so don't spend long there. Search current workplace news instead (layoffs, job
   hugging, AI and entry-level jobs, burnout, RTO, cost of living) and pair each theme with a pattern
   from `INSPIRATION.md`.

A strong idea has: a known object or game that reads in one second (cactus, musical chairs, badge
reader, ladder, leash), a "same X" or label-pair frame, speed or fate contrast, a test the grey path
fails, and a kind ending where blue brings grey along.

Propose 4–8 ideas, each as a title, a frame line, a two-sentence beat summary and its pattern number.
Recommend an order, then **stop and ask** which to build.

### 2. Write the scripts

Append a new `SCRIPTS-<N>.md` in the exact shape of `SCRIPTS-7.md`: intro (date, sources), house rules
line, then per video: title + quoted line, pattern used, frame line (+ line 2 in blue), labels,
chips/stats, length, a beat table (Time | Beat | What happens | On screen text | SFX cue), post
caption, loop point. End with a build order.

### 3. Scaffold each project

```bash
python3 .claude/skills/job-haters/scripts/new_video.py the-<name> \
  --line "Frame line." --left "Grey label" --right "Blue label" \
  --chip "id:Text" --chip "b1:b:Blue chip" --chip "day:n:Day 1"
```

Chip spec: `id:Text` (light), `id:b:Text` (blue), `id:n:Text` (tabular numbers), `id:r:Text` (dark
negative chip). It copies vendor/, fonts, logo, rig.js and the docs from the newest batch-7 project,
writes package.json, meta.json, index.html, a scene.js skeleton, audio/build_sfx.py skeleton and a
BRIEF.md to fill in. Fill BRIEF.md (intent, caption) before moving on.

### 4. Write scene.js

Start from the skeleton and read `references/scene-guide.md` first: coordinates, the figure rig and
poses, yaw rules, sitting, the helper API in rig.js, chips, line 2, and the bugs already hit. Good
complete examples to copy from: `videos/the-musical-chairs` (many figures, sitting, state machine),
`the-cactus` (props + growth + chips), `the-badge` (build-a-door, walk path, held prop),
`the-bottom-rung` (2-bone IK arm, falling parts, climbing), `the-leash` (rebuilt tube geometry),
`the-commute` (interior set, streaming lights, counter chip).

**The whole frame must be a pure function of `t`.** Snapshots and the renderer seek out of order.

### 5. Review with snapshots, fix, repeat

```bash
cd videos/the-<name>
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/<name>
```

Read the `contact-sheet.jpg`. Check: nothing crosses the frame line / line 2 (keep props below world
y ≈ 3.2), chips don't overlap each other, figures don't stand inside props, the story reads with the
sound off, line 2 is fully typed by ~11.3s. Expect 1–2 rounds of fixes.

### 6. Sound

Fill `audio/build_sfx.py` (see `references/sfx-guide.md`): mirror scene.js timings exactly, grey
panned left and blue right, then `python3 audio/build_sfx.py` writes `assets/audio/sfx-mix.wav`.

### 7. Check, render, deliver

```bash
npx --yes hyperframes@0.8.183 check          # must be 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-a the-b ...   # run in the background
```

`render.sh` renders each project, copies the newest MP4 to `renders/13learns-<short>.mp4`, prints
size, duration and integrated loudness (expect ~-18 to -22 LUFS) and writes a 4-frame strip per
video to `renders/.strips/` for a last look. Verify 1080×1920, 30fps, 12.0s, an audio stream.

### 8. Close out

Tell the user which files landed in `renders/`, any brand trade-offs, and what wasn't verified (you
only see frames, not playback). Update the project memory (`clearlyy-video-brand.md` video list,
`inspiration-accounts.md` batch line) with the new batch.

Then give each new video its own skill, `.claude/skills/jh-<short>/SKILL.md`, in the same shape as the existing
ones (project, script ref, delivered file, what happens, the script, on-screen text and where it lives,
timing constants, scene.js builders, sound, common jobs). The 39 existing ones were generated from each
project's own files. Hand-write the next ones in that shape, or rerun a generator that reads
`SCRIPTS-N.md`, `BRIEF.md`, `index.html`, `scene.js` and `audio/build_sfx.py`.

## Per-video skills

Every finished video has a `jh-<short>` skill (e.g. `jh-cactus`, `jh-two-years`, `jh-wheel`) with that
video's script, text locations, timing constants, builders, sound notes and re-render commands. Load the
matching one when the user asks to change or re-render a specific video, or wants to reuse a prop from it.
