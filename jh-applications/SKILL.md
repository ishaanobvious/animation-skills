---
name: jh-applications
description: "13learns Job haters video \"200 Applications\" (\"Stop asking. Start offering.\", phone-screen format). Two phones side by side, the same number of taps on \"Send\". Use to rebuild, re-render or change it (text, timing, sound), or make a sequel or variant, or reuse its pieces (makePhone, drawInbox, drawTap, drawSend)."
---

# 200 Applications: "Stop asking. Start offering." (13learns Job haters)

- **Project:** `videos/the-applications/` (HyperFrames 0.8.183 + Three.js, 1080×1920, 30fps, 11s, seamless loop, no VO)
- **Script:** `SCRIPTS-5.md` §4
- **Delivered:** `renders/13learns-the-applications.mp4` (rendered)
- **Series rules:** load the `job-haters` skill first. It holds the house rules (brand, one version, no vidIQ, owned audio only) and the full build workflow; this skill only covers this one video.

## What happens

200 Applications: two phones side by side, the same number of taps on "Send". Grey sends job applications and his inbox fills with rejections and "Seen"; blue sends offers to help and his fills with "Seen" and "No thanks" too, with a blue yes every so often. Both hit Sent 200 at once: grey's last reply is another "Unfortunately", blue's is "Payment received". Blue sends one more message, which flies across into grey's inbox: "I've got more work than I can handle. Want in?" Grey taps it and his "0 offers" becomes "1 offer". Pure HTML: no 3D in this one.

## The script (as written)

**Pattern used:** a phone as the stage with an escalating list; same counter, different stat. Flat UI, so it's the quickest build.
**Frame line (top):** SAME 200 MESSAGES.
**Labels:** above the phones: Asking for a job / Offering to help
**Shared counter:** "Sent 1 → 200" on both phones, with a stat under each: "0 offers" / "7 clients"
**Props:** two phones side by side with inbox lists. Messages fly out and replies stack in. Grey's replies: "Unfortunately…", "We've moved forward…", "Seen", "Position filled", auto-replies. Blue's replies: mostly "Seen" and "No thanks", then "How much?", "Can you start Monday?", and "Payment received".
**Length:** 11s

| Time | Beat | What happens | On screen text | SFX cue |
| --- | --- | --- | --- | --- |
| 0.0–1.0s | Hook: send | Both phones send at 0.0s: grey a "Job application", blue a "Hi, I can help with your…". | SAME 200 MESSAGES. · Sent 1 | send whoosh ×2 |
| 1.0–6.0s | The flood | The Sent counters race to 200. Grey's inbox fills with grey rejections. Blue's fills with "Seen" and "No thanks" too, but every so often a blue reply pops ("How much?", "Yes, let's talk"). | Sent 2 → 199 · 0 offers / 1 → 6 clients | send whooshes speeding up, a dull blip per rejection, a ping per yes |
| 6.0–7.0s | The turn | Sent 200. Grey's last reply: "Unfortunately, we've decided…". Blue's: "Payment received". | 200 · 0 offers / 7 clients | error tone (grey), coin ching (blue) |
| 7.0–9.0s | Kind payoff | Blue's phone sends one more message, and it lands at the top of grey's inbox in blue: "I've got more work than I can handle. Want in?" Grey's thumb taps it. | (the message) | send, ping, tap |
| 9.0–11s | Payoff | Line 2 types in. Dip, loop. | SAME 200 MESSAGES. / STOP ASKING. START OFFERING. | typing, sparkle |

**Post caption:** 200 applications and 200 cold offers take the same evenings. One asks someone to pick you. The other gives someone a reason to.
**Loop point:** both inboxes empty, both thumbs on "Send".

## On-screen text (where it lives)

- Frame line: `#frame-line` in `index.html`: "Same 200 messages."
- Label `#lbl-emp` (`index.html`): "Asking for a job"
- Label `#lbl-own` (`index.html`): "Offering to help"
- Line 2 (blue, typed at the payoff) is set in `scene.js`: "Stop asking. Start offering."

## Layout and timing constants (`scene.js`)

Every beat is keyed off these. Change a time here and change the same name in `audio/build_sfx.py`, or the sound drifts off the picture.

```js
const DUR = 11;
const SENT_FULL = 6.05;
const TURN = 6.15;
const DRAFT_SWAP = 6.6;
const FRIEND_TAP = 7.0;
const FLY = [7.05, 7.7];
const FRIEND_IN = 7.75;
const GREY_TAP = 8.5;
const OFFER = 8.6;
const TYPE_LINE_AT = 9.0;
const TAPS = [];
const GREY = [
const BLUE = [
const ROW_H = 80;
const GAP = 6;
const FROM = { x: 566 + 16 + 378, y: 436 + 846 };
const TO = { x: 40 + 16 + 221, y: 436 + 140 + 62 };
const LINE2 = "Stop asking. Start offering.";
const TYPE_SECS = Math.min(1.0, 0.041 * LINE2.length);
```

## How `scene.js` is built

Sections, in order: story beats · the replies · one phone · stats under the phones · the message that flies across · line 2 · frame.

Functions:
- `sentAt(t)`
- `makePhone(id, replies)`
- `drawInbox(ph, t)`
- `drawTap(ph, x, y, at, t)`
- `drawSend(ph, t, extraTaps = [])`
- `drawStats(t)`
- `drawFly(t)`
- `drawLine2(t)`
- `renderAt(t)`

The frame is a pure function of `t` (`renderAt(t)` on `hf-seek`). Snapshots and the renderer seek out of order, so never keep state between frames.

## Sound (`audio/build_sfx.py`)

Build the SFX layer for 200 Applications as one premixed, motion-synced track. Timing mirrors scene.js: both thumbs tap Send at the same moments (a soft whoosh each, faster and faster), a dull blip for every rejection in grey's inbox, a ping for every yes in blue's, both phones hitting 200, the message that flies across, grey's tap and his first offer. Grey sits left in the stereo field, blue right. All sounds come from ../../sfx-library (owned synths, CC0, Pixabay): nothing needs attribution.

Owned synths: `air_whoosh`, `coin_clink`, `counter_blip`.
`sfx-library/` sounds: `chime`, `click`, `error`, `notification`, `ping`, `riser`, `sparkle`, `typing`, `whoosh-air-02`, `whoosh-short`.

Rebuild: `cd videos/the-applications && python3 audio/build_sfx.py` → `assets/audio/sfx-mix.wav` (+ `audio/cues.json`).

## Common jobs

All commands run from `videos/the-applications/` unless noted.

**Look at it:**
```bash
npx --yes hyperframes@0.8.183 snapshot --at 0.4,2.5,5,7.5,9.5,11.3 --no-end --describe false -o <scratchpad>/applications
```
Then read `contact-sheet.jpg`.

**Change text:** edit the element in `index.html` (or the line-2 string in `scene.js`). Keep the frame line short enough for two lines at 62px. Re-snapshot to check chips don't collide.

**Change timing:** edit the constants above, mirror them in `audio/build_sfx.py`, rebuild the SFX, then snapshot again.

**Re-render and deliver** (from the project root):
```bash
(cd videos/the-applications && npx --yes hyperframes@0.8.183 check)   # 0 errors, 0 warnings
bash .claude/skills/job-haters/scripts/render.sh the-applications   # run in the background
```
`render.sh` writes `renders/13learns-applications.mp4`. The file already delivered is `renders/13learns-the-applications.mp4`. Replace that one, so there's never two copies.
Check 1080×1920, 30fps, the full length, an audio stream, about −18 to −22 LUFS, and the strip in `renders/.strips/`.

**Sequel or variant:** propose it to the user first (job-haters step 1), then scaffold a fresh project with `new_video.py` and copy the builders you need from this `scene.js`. Don't edit this project to make a different video.
