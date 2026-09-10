---
title: "Your Simulator Is Lying to You: What Shipping on Real Hardware Exposes"
translationKey: "voice-app-on-device"
date: 2026-09-10T08:00:00+08:00
draft: false
tags: ["on-device", "ios", "voice ai", "debugging", "simulator", "solo builder"]
description: "A voice app that passes every simulator test still crashed on the phone. The gap between a green test run and a bricked handset is where on-device bugs live: real-time audio threads, Bluetooth routing, app backgrounding. Why 'works on my machine' is the most dangerous sentence in mobile."
cover:
  image: "cover-voice-app-on-device.png"
  alt: "A phone lying on a workbench with a crack running across its screen, next to a glowing simulator on a laptop"
---

# Your Simulator Is Lying to You

The simulator said it worked. The phone crashed.

That gap, between a green test run and a bricked handset, is where on-device software actually gets built. And it's a gap almost nobody writes about: the people who survive it are too busy shipping to blog, and the people who blog about "I built an AI voice thing" mostly stopped at the demo that only ever ran in the simulator.

This is about the specific, physical reasons the simulator lies, and why shipping on real hardware is a different craft than passing tests.

## The first lie: a crash the simulator can't reproduce

Hooking a voice interface to a language model is fast. A WebSocket, an open protocol, some compressed audio: a weekend gets you a talking demo. On the simulator it all works, because the simulator isn't a phone. It's your laptop wearing a phone costume.

Then you put it on the handset and tap the button, and you get a thread-assertion crash: a block that expected to run on the main thread, invoked instead on a real-time audio callback. The simulator never throws this because it doesn't run a real audio engine with a real-time scheduler.

The fix is one annotation marking the closure safe for that thread. One line. But finding it meant symbolicating a device crash log and reading the backtrace down to the audio tap's internal messenger. **The fix is trivial once you know where to look; the skill is knowing how to look. And you can only look somewhere the simulator is willing to take you.**

## The second lie: nothing happening, no error

Then came the echo loop: the assistant speaks, its own output gets picked up by the mic and re-transcribed into nonsense. The fix wasn't a patch, it was architecture. The microphone and the speech playback had to share one audio engine, gated by the server's turn boundaries.

The "obvious" design, a second dedicated engine, a clean separation of concerns, was the actual bug. Two engines contending over one audio session means the reply decodes but makes no sound, and the mic stops hearing follow-ups. Together. With no crash.

The simulator doesn't reproduce this either, because it doesn't enforce real audio-session ownership the way the OS does on hardware. **The symptom was nothing happening: the hardest bug to notice, because there's no error message, just silence.**

## The third lie: it worked until it didn't

Bluetooth was next. With wireless earbuds attached, the app jittered and dropped audio; the "fix" was an audio-session mode that passed clean mic input but played speech so quietly it was nearly inaudible. A tradeoff that only exists on physical hardware with real audio routing. Then backgrounding: tap away, tap back, and the app won't listen anymore, because the OS yanks the session and suspends the socket while the app is in the background. Each one is a class of bug you only meet on a device, one teardown-and-reconnect away from being invisible in any automated run.

## What "on-device" actually means as a craft

The lesson isn't "simulators are useless." They're indispensable for the 90% of logic that's hardware-free. The lesson is that **the last 10%, the parts that touch real-time audio, Bluetooth, and the background lifecycle, cannot be tested by proxy.** They can only be found by shipping to the device, reading the crash log, and trusting what the hardware tells you over what the test suite claims.

Here's the discipline that survives contact with a real phone:

1. **Mock what's mockable, ship what isn't.** The push-to-talk state machine is unit-tested against mock sockets and microphones: a dozen tests, no real audio, no network. The audio engine itself can't be mocked, so it gets shipped and watched.
2. **Trust the device log, not the test run.** A device crash log is ground truth; a simulator pass is a hypothesis. When they disagree, the device wins every time.
3. **"Works on my machine" is the most dangerous sentence in mobile.** Your machine is the simulator. The customer's machine is the phone in their pocket with earbuds in, walking through a doorway into a dead zone.

The distinction that matters for a solo builder: a demo that only ran in the simulator is a hypothesis. A thing that survives contact with real hardware is a fact you can reason about. That's the gap, and it's wide enough to be the entire difference between a weekend project and something worth shipping.

## Sources

- **Apple Developer Documentation, real-time audio.** A tap installed on an audio engine is invoked on a real-time audio thread, not the main thread; the isolation assumption that produces a thread-assertion crash is a concurrency artifact, absent in the simulator.
- **Apple Developer Documentation, audio session categories and modes.** Session ownership is exclusive on device; a second engine starting on an already-owned session is a documented cause of silent or starved audio, and the root of "decodes but no sound."
- **Open-source voice-assistant protocol ecosystems.** Mature, MIT-licensed voice-protocol reference implementations (many with tens of thousands of GitHub stars) demonstrate both the protocol and a free client layer. The client itself carries no commercial moat; the transferable skill is the on-device hardening, not the protocol.

_This post is the on-device companion to ["Done" Is a Claim](/posts/done-is-a-claim/), which is about the verification ritual: trusting your own eyes over an agent's word. That one is about who you trust; this one is about what you trust: the hardware over the simulation._
