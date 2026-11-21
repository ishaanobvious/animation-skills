---
name: pixar-ai-midterms
description: The "Tested Like an Airplane, or Launched Like an App?" 3D-feature-style storyboard animatic (5:53, 16:9, 13 scenes, 48 generated frames, ElevenLabs VO, synthesized score). Use to re-time, re-mix, regenerate frames, make the vertical cutdown or thumbnail, or follow the same storyboard-from-a-source-video pipeline for another explainer.
---

# AI midterms animatic: "Tested Like an Airplane, or Launched Like an App?"

- **Project:** `pixar-ai-midterms/`. Everything is described in `STORYBOARD.md` (style bible, cast, colour script, all 13 scenes with shots, VO and SFX, the fact check, the vertical cutdown).
- **Source:** adapted from Think School's video on the AI midterms super PACs (link in `STORYBOARD.md`). The sponsor read, the outro and the on-camera presenter were cut, and a narrator replaces the presenter.
- **Deliverables:** `animatic.mp4` (5:53, 1920×1080, 24fps, full mix at −14 LUFS), `storyboard.html` (every shot with its frame, timecode and VO line), `storyboard-overview.jpg` (all 48 frames), `thumbnail.jpg`.
- **Not 13learns, not One If:** this has its own look, a stylized 3D animated feature (soft rounded forms, subsurface skin, warm key and cool rim light, shallow depth of field).

## Hard rule: real people

The narration names real people, as the source does. On screen they are **role characters with no likeness**: "The President", "The Candidate", "The Founders". Never animate real faces or put lines in real people's mouths.

## Pipeline

1. **Frames:** 48 shots in `frames/` (`<scene>-<shot>.png`), plus cast sheets in `frames/cast/`, generated with Higgsfield GPT Image 2.5. **Append the prompt suffix from the style bible to every prompt**, and keep each scene's colour-script palette (Washington cream and navy, cash olive, Camp 1 orange, Camp 2 teal + `#1A5DE6`, Camp 3 violet, India saffron, finale night). The recurring cast: the President (with a sweat-bead gag), the living Capitol with seat-bot lanterns, the Maiden Group piggy-bank PAC, the Candidate, Spark the AI orb, and the three Founder camps.
2. **Voice:** ElevenLabs voice "Michael", `eleven_v4`, one file per scene in `vo/01-cold-open.mp3` … `13-finale.mp3`. `VO-full.mp3` is all 13 joined with 0.6s gaps.
3. **Timing:** `sound/timing.json` holds each shot's `start`/`end` against `VO-full.mp3` (`vo_end` 349.2s). The animatic cuts the frames to these times.
4. **Sound:** `sound/score.py` synthesizes the score and SFX on the shot times (plus five Pixabay-licensed hits and whooshes from the media-use library, which need no credit). `sound/mix.sh` lays the VO, the music (ducked) and the SFX (lightly ducked) under the picture and normalises to −14 LUFS. Only the input's video stream is used, so re-running is safe.

```bash
cd pixar-ai-midterms
python3 sound/score.py sound          # -> sound/music.wav + sound/sfx.wav
sound/mix.sh animatic.mp4 out.mp4     # MUSIC=0.27 SFX=0.35 by default; override via env
```

## Common jobs

- **Re-time a shot:** edit `sound/timing.json`, rebuild the picture cut, then re-run `score.py` and `mix.sh` so the cues follow.
- **Swap a frame:** regenerate it with the same prompt suffix and palette, and keep the filename.
- **Vertical 9:16:** follow the "Vertical 9:16 cutdown" notes at the end of `STORYBOARD.md`.
- **Thumbnail:** `thumbnail/` is a small HTML + `scene.js` project (fonts and vendor bundled). Render it with HyperFrames' chrome-headless-shell.
- **Before publishing:** work through the "Fact-check before publishing" list in `STORYBOARD.md`.
