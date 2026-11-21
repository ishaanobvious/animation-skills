# The SFX layer (audio/build_sfx.py)

One premixed track, `assets/audio/sfx-mix.wav`, played by the `<audio id="sfx">` in index.html. It is
built by a per-video script that **mirrors scene.js's timing constants exactly** (copy them across
and keep them in sync when you retime a beat).

```python
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent.parent / "sfx-library"))
from mixer import Mix, smooth
from synth import floor_step, soft_thud, pipe_clunk, ...
rng = np.random.default_rng(<seed>)
m = Mix(ROOT.name, dur=12.0)
m.place(sound, t, db, pan, "label")          # one-shot; pan -1 left .. +1 right
m.bed(loop, t0, t1, db, pan, "label", fade=0.3, gain=lambda t: ...)   # tiled bed
m.lib("chime")  /  m.lib("riser", 6.0, 10.0)  # a library file (optionally a slice)
m.uses("pipe-clunk-01", ...)                   # record synth families used, for library.json
m.finish(ROOT)                                 # master chain, loudnorm -20 LUFS, cues.json, usage
```

Conventions: grey panned ≈ -0.45, blue ≈ +0.45, shared moments near 0. Typical levels: key hits
-15…-18 dB, actions -19…-23, footsteps -22…-25, beds -24…-36. Always end with
`m.lib("typing", 0.0, TYPE_SECS)` at the line-2 time (`TYPE_SECS = min(1.0, 0.041 * len(LINE2))`) and
a `sparkle` just after it.

## What's available

Search first: `python3 sfx-library/sfx.py search <words>`; audition in `sfx-library/browse.html`.

- **Synths (`synth.py`)**: `floor_step`, `mesh_step`, `rung_tick`, `coin_clink`, `coin_cascade`,
  `wheel_rumble` (loopable bed), `soft_thud(freq)`, `air_whoosh(seconds, lo, hi)` (also scrapes,
  wind, sanding), `counter_blip(freq)`, `water_*`, `pipe_clunk(pitch)`, `valve_squeak`, `glass_tink`,
  `glass_crack`, `glass_shatter`, `stone_crash`, `stone_crackle`, `quake_rumble`, `metal_creak`,
  `post_snap`, `bucket_clatter`, `hand_clap`, `applause`, plus `band`/`lowp`/`highp` filters and `SR`.
- **Library ids**: chime, click, click-soft, error, key-press, notification, ping, pop, sparkle,
  typing, whoosh, whoosh-short, whoosh-deep, whoosh-air-01/02, whoosh-cinematic, riser,
  impact-bass-1/2, body-fall, glitch-1/2/3, plus the rendered synth variants (coin-clink-04 …).
- **Writing a new sound** inside build_sfx.py is fine when nothing fits (it's owned): see the
  music-box loop in `videos/the-musical-chairs/audio/build_sfx.py` and the saw whine and servo in
  `videos/the-bottom-rung/audio/build_sfx.py`. Keep melodies original. If it's reusable, add it
  to `synth.py` and `generate.py` so the library grows.

Never add sounds that need attribution, and never take audio from the reference reels.
