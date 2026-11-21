#!/usr/bin/env bash
# Render Job haters projects one after another and deliver them to renders/.
#
#   bash .claude/skills/job-haters/scripts/render.sh the-cactus the-badge ...
#
# For each project: hyperframes render (pinned version from its package.json), copy the newest MP4 to
# renders/13learns-<short>.mp4 (<short> = name without a leading "the-"), print size, duration,
# resolution, fps, whether there's an audio stream and integrated loudness, and write a 4-frame strip
# (1s, 5s, 8s, 10.7s) to renders/.strips/<short>.png for a last look.
set -u
ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
mkdir -p "$ROOT/renders/.strips"
status=0
for name in "$@"; do
  dir="$ROOT/videos/$name"
  short="${name#the-}"
  if [ ! -f "$dir/index.html" ]; then echo "$name: no project at $dir"; status=1; continue; fi
  ver=$(sed -n 's/.*hyperframes@\([0-9.]*\).*/\1/p' "$dir/package.json" | head -1)
  log="$dir/renders/render.log"
  mkdir -p "$dir/renders"
  before=$(ls -t "$dir"/renders/*.mp4 2>/dev/null | head -1)
  (cd "$dir" && npx --yes "hyperframes@${ver:-latest}" render >"$log" 2>&1)
  out=$(ls -t "$dir"/renders/*.mp4 2>/dev/null | head -1)
  if [ -z "$out" ] || [ "$out" = "$before" ]; then
    echo "$name: RENDER FAILED (see $log)"; tail -5 "$log"; status=1; continue
  fi
  dest="$ROOT/renders/13learns-$short.mp4"
  cp "$out" "$dest"
  info=$(ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate:format=duration -of default=nw=1 "$dest" | tr '\n' ' ')
  lufs=$(ffmpeg -nostats -i "$dest" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | tr -s ' ')
  size=$(du -h "$dest" | cut -f1)
  ffmpeg -v error -y -i "$dest" -vf "select='eq(n\,30)+eq(n\,150)+eq(n\,240)+eq(n\,320)',scale=270:480,tile=4x1" -frames:v 1 "$ROOT/renders/.strips/$short.png"
  echo "$name -> renders/13learns-$short.mp4  [$size] $info|$lufs"
done
exit $status
