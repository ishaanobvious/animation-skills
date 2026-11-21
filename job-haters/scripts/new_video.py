#!/usr/bin/env python3
"""Scaffold a new Job haters video project from a batch-7 project.

    python3 .claude/skills/job-haters/scripts/new_video.py the-musical-chairs \
        --line "They keep taking chairs." --line2 "Bring your own." \
        --left "Waiting for a seat" --right "Built his own" \
        --chip round:n:Round 1 --chip b1:b:First client

Chip spec: id:Text (light grey), id:b:Text (blue), id:n:Text (tabular numbers),
id:r:Text (dark "negative" chip; no red, the brand has no warm tones).

Copies vendor/, fonts, logo, rig.js, frame.md and the HyperFrames docs from --from (default
videos/the-commute), then writes package.json, meta.json, index.html, a runnable scene.js skeleton,
audio/build_sfx.py (typing + sparkle only, so check and render work at once) and BRIEF.md.
Refuses to overwrite an existing project.
"""

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # .claude/skills/job-haters/scripts → project root


def parse_chip(spec):
    parts = spec.split(":", 2)
    if len(parts) == 2:
        cid, text, kind = parts[0], parts[1], ""
    elif len(parts) == 3 and parts[1] in ("b", "n", "r", ""):
        cid, kind, text = parts
    else:
        cid, text, kind = parts[0], ":".join(parts[1:]), ""
    if not re.fullmatch(r"[a-z][a-z0-9-]*", cid):
        sys.exit(f"bad chip id {cid!r}: use lowercase letters, digits, dashes")
    return cid, kind, text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name", help="project folder name, e.g. the-cactus")
    ap.add_argument("--line", required=True, help="frame line (top), sentence case")
    ap.add_argument("--line2", default="", help="blue payoff line 2 (pre-filled in the scene.js skeleton)")
    ap.add_argument("--left", required=True, help="grey label under the floor")
    ap.add_argument("--right", required=True, help="blue label under the floor")
    ap.add_argument("--chip", action="append", default=[], help="id:Text, id:b:Text, id:n:Text or id:r:Text")
    ap.add_argument("--from", dest="src", default="videos/the-commute", help="batch-7 project to copy rig and assets from")
    ap.add_argument("--videos", default="videos", help="where new projects go (relative to the project root)")
    a = ap.parse_args()

    src = (ROOT / a.src).resolve()
    dst = (ROOT / a.videos / a.name).resolve()
    if dst.exists():
        sys.exit(f"{dst} already exists; not overwriting")
    if not (src / "rig.js").exists() or "batch-7 helpers" not in (src / "rig.js").read_text():
        sys.exit(f"{src} has no batch-7 rig.js")

    dst.mkdir(parents=True)
    for d in ("vendor",):
        shutil.copytree(src / d, dst / d)
    (dst / "assets/audio").mkdir(parents=True)
    shutil.copytree(src / "assets/fonts", dst / "assets/fonts")
    shutil.copy2(src / "assets/logo.png", dst / "assets/logo.png")
    for f in ("rig.js", "frame.md", "AGENTS.md", "CLAUDE.md", "hyperframes.json"):
        shutil.copy2(src / f, dst / f)
    (dst / "audio").mkdir()
    (dst / "renders").mkdir()

    pkg = json.loads((src / "package.json").read_text())
    pkg["name"] = a.name
    (dst / "package.json").write_text(json.dumps(pkg, indent=2) + "\n")
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    (dst / "meta.json").write_text(json.dumps({"id": a.name, "name": a.name, "createdAt": now}, indent=2) + "\n")

    # index.html: the source's page with this video's frame line, chips and labels
    page = (src / "index.html").read_text()
    chips = [parse_chip(c) for c in a.chip]
    chip_html = "\n".join(f'        <div id="{i}" class="chip {k}" data-layout-allow-occlusion>{html.escape(t)}</div>' for i, k, t in chips)
    page, n1 = re.subn(r'<div id="frame-line">.*?</div>', f'<div id="frame-line">{html.escape(a.line)}</div>', page, count=1)
    page, n2 = re.subn(r'(<div id="chips" data-layout-allow-overlap>\n).*?(\n      </div>\n      <div id="lbl-emp")', lambda m: m.group(1) + chip_html + m.group(2), page, count=1, flags=re.S)
    page, n3 = re.subn(r'<div id="lbl-emp" class="tag">.*?</div>', f'<div id="lbl-emp" class="tag">{html.escape(a.left)}</div>', page, count=1)
    page, n4 = re.subn(r'<div id="lbl-own" class="tag">.*?</div>', f'<div id="lbl-own" class="tag">{html.escape(a.right)}</div>', page, count=1)
    if (n1, n2, n3, n4) != (1, 1, 1, 1):
        shutil.rmtree(dst)
        sys.exit(f"index.html template in {src} didn't match (frame-line {n1}, chips {n2}, labels {n3}/{n4})")
    (dst / "index.html").write_text(page)

    line2 = a.line2.replace('"', '\\"') or "Line 2."
    chip_ids = ", ".join(f'"{i}"' for i, _, _ in chips)
    (dst / "scene.js").write_text(f'''// {a.name}: TODO one-paragraph summary of the beats (see ../../SCRIPTS-N.md).
// Skeleton from .claude/skills/job-haters: two figures standing, chips stacked in the middle, line 2
// typing at the payoff. Read .claude/skills/job-haters/references/scene-guide.md before filling it in.
import {{
  THREE, scene, renderer, camera, FLOOR_Y, mats, clamp, lerp, smooth, backOut,
  makeFigure, applyPose, mixPose, walkPose, hipHeight, POSES, GREY_START, GREY_END,
  updateMotes, placeCamera, box, add, std, makeGlow, popIn, pin, placeTagAt, makeTyper, walkBetween, yawToward,
}} from "./rig.js";

const {{ STAND }} = POSES;
const DUR = 12;

// ---------- layout ----------
const G_AT = [-1.6, 0];
const B_AT = [1.6, 0];

// ---------- story beats ----------
const TYPE_LINE_AT = 10.2;

// ---------- props ----------

// ---------- figures ----------
const blue = makeFigure(mats.blue, mats.blueLeg);
const grey = makeFigure(mats.grey, mats.greyLeg);
scene.add(blue.root, grey.root);
function poseGrey(t) {{
  applyPose(grey, STAND, G_AT[0], FLOOR_Y, G_AT[1], 0, 0);
}}
function poseBlue(t) {{
  applyPose(blue, STAND, B_AT[0], FLOOR_Y, B_AT[1], 0, Math.PI);
}}

// ---------- HTML ----------
const chipEls = [{chip_ids}].map((id) => document.getElementById(id));
function drawHud(t) {{
  chipEls.forEach((el, i) => pin(el, new THREE.Vector3(0, FLOOR_Y + 2.0 + 0.4 * i, 0), smooth((t - 0.5 * i) / 0.2), popIn(t, 0.5 * i)));
}}
const typeLine = makeTyper("{line2}", TYPE_LINE_AT);

// ---------- frame ----------
function renderAt(t) {{
  t = clamp(t, 0, DUR);
  placeCamera(t, new THREE.Vector3(), DUR);
  camera.updateMatrixWorld();
  mats.grey.color.copy(GREY_START).lerp(GREY_END, smooth(t / 8) * (1 - 0.45 * smooth((t - TYPE_LINE_AT) / 1.0)));
  poseGrey(t);
  poseBlue(t);
  updateMotes(t);
  drawHud(t);
  placeTagAt("lbl-emp", G_AT[0], 56);
  placeTagAt("lbl-own", B_AT[0], 56);
  typeLine(t);
  renderer.render(scene, camera);
}}

window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
renderAt(window.__hfThreeTime || 0);
''')

    (dst / "audio/build_sfx.py").write_text(f'''"""Build the SFX layer for {a.name} as one premixed, motion-synced track.

TODO: one paragraph on what you hear and when, mirroring scene.js. Grey sits left in the stereo
field, blue right. Owned synths and ../../sfx-library sounds only: nothing needs attribution.
See .claude/skills/job-haters/references/sfx-guide.md.

    python3 audio/build_sfx.py            # writes assets/audio/sfx-mix.wav (+ audio/cues.json)
"""

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent.parent / "sfx-library"))
from mixer import Mix  # noqa: E402
from synth import floor_step, soft_thud  # noqa: E402,F401

rng = np.random.default_rng({sum(map(ord, a.name)) % 1000})
DUR = 12.0
m = Mix(ROOT.name, dur=DUR)

# ---------- timing model (mirrors scene.js) ----------
TYPE_LINE_AT = 10.2
LINE2 = "{line2}"
TYPE_SECS = min(1.0, 0.041 * len(LINE2))
G = -0.45
B = 0.45

# ---------- TODO: the beats ----------

# ---------- payoff ----------
m.place(m.lib("typing", 0.0, TYPE_SECS), TYPE_LINE_AT, -20, 0, "type-line")
m.place(m.lib("sparkle"), TYPE_LINE_AT + TYPE_SECS + 0.05, -16, B, "payoff")

m.finish(ROOT)
''')

    message = json.dumps(f"{a.line} {a.line2}".strip(), ensure_ascii=False)
    (dst / "BRIEF.md").write_text(f'''---
workflow: general-video
flow: automation
storyboard: no
message: {message}
destination: reels-shorts
aspect: 1080x1920
language: en
length: 12s
angle: metaphor-loop
recipe: clearlyy-metaphor-loop
---

## Intent

Script N in ../../SCRIPTS-N.md. TODO: the beats in one paragraph (who does what, the test, the kind payoff).

## Assets

- assets/logo.png — 13learns logo, bottom-centre. Masters in ../../brand/.
- frame.md — design spec (blue/white/black, Space Grotesk); copy of ../../brand/frame.md.
- rig.js — batch-7 rig (camera z 42, target y -0.4) plus shared helpers.

## Customizations

- HyperFrames + Three.js, rendered 1080×1920 30fps, 12s. One version only.
- Music: rendered with SFX only; trending audio added in-app when posting.
- SFX layer: audio/build_sfx.py → assets/audio/sfx-mix.wav, owned synths and library sounds only, cues mirror scene.js.
- Post caption: TODO
''')

    # a first mix so check/render work straight away
    r = subprocess.run([sys.executable, str(dst / "audio/build_sfx.py")], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
    print(f"created {dst.relative_to(ROOT)}  (chips: {', '.join(i for i, _, _ in chips) or 'none'})")


if __name__ == "__main__":
    main()
