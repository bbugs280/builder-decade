---
title: "Choosing the Brain of a Physical Product: The Decision Every Hardware Guide Skips"
translationKey: "choosing-the-brain-of-a-physical-product"
date: 2026-11-13T08:39:00+08:00
lastmod: 2026-11-13T08:39:00+08:00
draft: false
tags: ["hardware", "microcontroller", "esp32", "solo builder", "electronics", "product design", "physical products"]
description: "Enclosure guides tell you wall thickness. Nobody tells you which chip to put inside. Here is the decision, the four candidates, and the questions that actually narrow it."
cover:
  image: "cover-choosing-the-brain-of-a-physical-product.png"
  alt: "A bare green circuit board lying flat on a scarred old wooden workbench, a few unmarked black chips on the board, a brass-rimmed magnifying glass beside it, scattered capacitors and a coiled multicoloured wire, warm light raking from a brass desk lamp at upper left, dust suspended in the beam"
---

I have written about enclosures, tolerances, cash flow, and the pipeline from digital to physical. Every one of those posts is a footnote to a decision I never named.

**What chip runs the thing.**

It is the first real commitment in any physical product, and it is the one your enclosure dimensions, your battery life, your firmware, your certification path, and your unit cost all hang off. Get it wrong and you redesign the board. Get it wrong late and you redesign the enclosure too.

Here is the decision, laid out honestly — including where the evidence is thin.

## The four candidates that cover almost everything

You do not need to survey the entire microcontroller market. For a solo builder shipping a connected product, four families cover nearly every case, and the choice between them is not close once you know which constraint binds.

| Chip | Core | Wireless | Rough unit price | The job it wins |
|---|---|---|---|---|
| **ESP32-C3** | Single RISC-V, 160 MHz | Wi-Fi + BLE built in | ~$1.50–2 | Cheapest connected sensor node |
| **ESP32-S3** | Dual Xtensa LX7, 240 MHz | Wi-Fi + BLE, native USB | ~$2.80–4.40 | Screens, camera, on-device inference |
| **RP2040** | Dual Cortex-M0+, 133 MHz | None (Pico W adds it) | ~$0.80–1.20 | Wired USB devices, unusual I/O, hard timing |
| **nRF52840** | Cortex-M4F | BLE only, no Wi-Fi | ~$4–6 | Battery products that must sip power |

Prices are indicative and they move — treat the ordering as the stable part, not the numbers. Verify before you commit a BOM.

## The three questions that actually decide it

Most chip-selection writing gives you a spec table and wishes you luck. The table is not the decision. These three questions are.

**1. Does it need a radio, and which one?**

Wi-Fi and Bluetooth are not interchangeable, and the choice is usually set by *where the device lives*, not by the spec sheet.

- **In a home with a router** → Wi-Fi. The ESP32 family has the radio inside the silicon, so it is genuinely cheaper than a bare MCU plus a separate radio module.
- **Paired to a phone, worn or carried** → BLE. Wi-Fi association is a poor experience for something that moves.
- **Both** → ESP32 covers it in one part.

If the answer is "neither," you have just eliminated three of the four candidates and the decision drops to the RP2040 versus a bare industrial MCU.

**2. Is it on a battery, and what is the duty cycle?**

This is where the most expensive mistake hides, and it is not the one people expect.

An ESP32's average current depends overwhelmingly on **how long the radio is awake**, not on the chip's headline sleep figure. A device that wakes, connects to Wi-Fi, sends a reading, and sleeps is dominated by the connect-and-transmit window. Deep-sleep current of a few microamps sounds impressive and is nearly irrelevant if the radio runs for two seconds every minute.

⚠️ The honest version: **the sleep current in the datasheet is the easiest number to find and the least useful one.** Work out your radio-on seconds per hour first. If the device transmits rarely, an ESP32-C3 can run for months. If it transmits constantly, no deep-sleep number saves you.

Where the nRF52840 genuinely wins is a device that is *connected* most of the time — a BLE peripheral maintaining a link. Its radio and stack are tuned for low-duty-cycle BLE in a way the ESP32's is not. That is the real argument for paying more, and it is worth paying for only if that is your actual pattern.

**3. Does it have to do anything hard in real time?**

The RP2040 answers this better than its price suggests. Its programmable I/O lets you implement timing-sensitive protocols in hardware rather than fighting an interrupt scheduler. If your product drives precise motor control, reads an unusual sensor protocol, or needs deterministic timing, that matters more than clock speed.

⚠️ **The ESP32's real-time performance can be affected by its own Wi-Fi stack** — this is a known property of the family, and it bites products that assume the radio and a tight control loop can coexist without care. If your product is genuinely real-time, test that assumption before you commit, because it is the one that costs a board revision.

## Where this post's evidence is weakest

I want to be clear about what I have not measured.

**I have not built a production run on all four of these.** The spec-level comparison is verifiable from vendor datasheets and I have checked it. The *feel* of each ecosystem — how much friction the toolchain adds, how often you fall into a community forum with an answer — is not something a spec table captures and it is not something I can honestly quantify from here.

That is also why most of the internet's version of this comparison is unreliable in a specific direction. The dominant search results for chip comparison are written by **component distributors and board vendors**. Their interest is in you buying a part, not in you correctly deciding you do not need one. The numbers they publish are usually right; the framing consistently points toward more capability than your product needs.

And that is the asymmetry worth naming, because in hardware it is expensive: an over-specified chip costs you on every unit, in power budget, in certification complexity, and in board area. Nobody sells you the smaller chip with the same enthusiasm as the bigger one.

## The decision, reduced

If you want the short version:

- **Cheapest connected node, mains-powered** → ESP32-C3
- **Anything with a screen, camera, or on-device model** → ESP32-S3
- **Wired, precise, or unusual I/O** → RP2040
- **Battery, connected most of the time, BLE** → nRF52840

Four rows, and every one of them is a decision you can reverse at prototype stage for the price of a board. **That is the actual insight: this decision is cheap early and expensive late.** A dev board for each candidate costs less than one hour of your time. Buy all four, spend a weekend proving the one binding constraint on the real silicon, and the spec table stops mattering.

The enclosure you print later depends on this. Print it in the wrong order and you will print it twice.
