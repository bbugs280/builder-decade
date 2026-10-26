---
title: "Painting 3D Prints: Where a Plastic Toy Becomes an Object People Keep"
translationKey: "painting-finishing-3d-prints"
date: 2026-10-26T07:00:00+08:00
lastmod: 2026-10-26T18:00:00+08:00
draft: false
tags: ["3d printing", "painting 3d prints", "finishing 3d prints", "primer", "sanding", "airbrush", "resin safety", "hardware", "solo builder", "art"]
description: "The printer is a roughing tool. Everything that makes a printed object worth owning happens in the twenty minutes after it comes off the plate."
cover:
  image: "cover-painting-finishing-3d-prints.png"
  alt: "A finished painted 3D print on a workbench beside paint pots, brushes and a primed grey figure"
---

There is a moment every person who buys a 3D printer goes through. The first print finishes, you lift it off the plate, and it is *fine*. It's the shape you wanted. It works. And it looks exactly like what it is: extruded plastic, with visible layer lines and a matte flatness that reads as "prototype" no matter what the object is.

Most people stop there. The printer goes on a shelf, and the machine gets filed under "neat, but I don't have a use for it."

That's a finishing problem, not a printing problem. And it's the single biggest gap between a solo builder who owns a printer and one who can actually ship a physical product.

Here's the useful reframe: **your printer is a roughing tool.** It gets you the geometry. Everything that makes a printed object something a person wants to hold — or pay for — happens in the twenty minutes after it comes off the plate.

## The line that actually matters

Every FDM print reveals its layer height. At 0.2 mm you get visible stair-stepping on any curved surface; at 0.12 mm it's finer but still there. You cannot print your way out of this. Lowering layer height costs you time quadratically and never reaches smooth.

So you sand. And this is where most people quit, because sanding a print feels like doing it wrong — you're abrading the thing you just carefully manufactured.

It isn't wrong. It's the process. The layer lines are a *manufacturing artifact*, and finishing is how you remove them:

```
80–120 grit    knock down major layer lines and layer shifts
220            clear the scratches the rough grit left
400            pre-primer smoothing — switch to wet sanding here
800            post-primer de-nibbing
1000–1500      final flat before paint
```

Two things that make this bearable rather than miserable:

**Wet sand from 400 up.** Less dust, and the paper doesn't clog. Dry-sanding fine grits on plastic is how you spend an evening being annoyed.

**Primer is a diagnostic, not a coat.** A flat grey filler primer does something a sanded surface can't: it makes every remaining defect visible under raking light. You're not painting yet. You're *inspecting*. Prime, look, sand again, prime again. Formlabs makes the same point — the flat finish is the whole value, because it shows you what your fingers can't feel. Two to three light coats, and only after the surface is already as good as you can get it.

## Working from finished pieces rather than theory

I want to show this concretely rather than describe it abstractly, because the difference between a generic finishing guide and a useful one is whether you can point at the object at the end.

I make finished pieces under [@vincenty3d](https://www.instagram.com/vincenty3d/) — mostly pop-culture subjects built on sculpted and printed forms, then painted. Two of them illustrate the two different problems finishing actually solves.

**Worldbreaker** ([see the post](https://www.instagram.com/p/DIEHecZyPX1/)) is a sculpture carrying an argument. The subject is a political one, and the piece only works if the sculpture reads as deliberate — a heavy, finished object making a statement. If the surface still shows layer lines and a flat plastic sheen, the viewer reads "someone's hobby project" instead of "a work about policy." The finishing is doing the persuasive work. A rough print would have killed the message before anyone read it.

**Vader Poppy** ([see the post](https://www.instagram.com/p/DLNPwXpBEVz/)) is the opposite test. It's a Pop Mart doll crossed with Darth Vader — deliberately cute, deliberately absurd, and meant to be *liked* at a glance. Toy-adjacent pieces are the ones where finishing discipline shows up most brutally, because the audience already knows what a good collectible feels like in the hand. A collector has held a real figure. The gloss level, the crispness of the edges, the depth in the dark parts — that's the entire comparison, and it happens in about two seconds. There is no version of that piece where "good enough" reads as good.

The practical point from both: **the finishing brief changes with the audience, not with the printer.** Same machine, same plastic, same sandpaper sequence. A sculpture aimed at an argument needs a matte, unified, gallery-ish surface. A toy aimed at desire needs gloss and depth and clean separations. If you finish everything the same way, you'll be wrong on at least one of them.

## The step where it becomes a product

Here's the part that separates a painted print from a *good* painted print, and it's the one hobbyists skip because it feels like a detour.

**Paint is translucent.** Everything under it shows through, subtly. Which means your base coat doesn't sit on a neutral surface — it sits on whatever colour the plastic and primer happen to be. Print in black, prime in grey, and every colour you apply afterwards is fighting a different starting point than the one in your head.

The fix is boring and it changes the result completely: **prime in a neutral grey, then establish a consistent base coat before you do anything expressive.** Only then does layering behave the way you expect.

The other half is that gloss and matte do different jobs. A matte varnish unifies; a gloss clear deepens. On a display piece, the difference between "painted model" and "collectible" is almost always the final clear coat, not the paint underneath it.

## The safety part I'm not going to soften

If you're working in resin rather than FDM, there is a hazard in this hobby that is genuinely serious and routinely underplayed by enthusiastic YouTubers.

**Uncured photopolymer resin is a sensitizer.** Not just an irritant — repeated exposure can cause you to develop a permanent allergic reaction that gets *worse* with each exposure, not better. It is one of the few things in this hobby where "I've done it for years and I'm fine" is not evidence of safety. Your body can be silently building the reaction right now.

NIOSH's 2025 guidance for desktop resin printing is specific and worth reading in full:

- Uncured resin contains **acrylates** that can cause **asthma or dermatitis** (allergic or irritant)
- **Let the printer air out for a few minutes before opening the cover** — printing releases uncured resin particles and gases that may not be contained
- **Curing** (UV + heat) generates particles and gases you should not breathe — ventilate
- **Sanding cured resin generates dust containing both cured and uncured particles**
- Use gloves rated to protect against **acrylates and IPA**, and change them frequently

Note that last point carefully. Thin disposable gloves are not automatically adequate — uncured resin can permeate thin gloves within roughly half an hour, which is exactly how long a wash-and-clean session takes. The glove you wore for the whole job may have been doing nothing for the last twenty minutes of it.

**The good news inside the bad news:** NIOSH notes that once curing is complete, resin on the surface of parts is usually fully cured, and *the risk of allergic dermatitis is reduced significantly*. Post-cure properly and the finished part is safe to handle. The hazard lives in the liquid, the wash, and the dust — not the object.

Which is also an argument for a specific discipline: **finish your parts completely, every time.** A half-cleaned, half-cured print sitting on a shelf is an uncured-resin object pretending to be a finished one.

## What this means if you're building solo

Two things, and they're both about money rather than craftsmanship.

**1. The printer isn't the cost centre — the finishing is.** A finished piece takes a printer that costs a few hundred, plus consumables in sandpaper, primer, paint, and clear coat. The consumables are cheap individually and add up fast. If you're costing a product, the finishing line is the one people forget to include, and it's usually the difference between a margin and no margin.

**2. Finishing is where the perceived value is created, so it's where your time should go.** Two identical prints straight off the plate are worth the same. Two identical prints with different finishing are not close in perceived value. The labour is identical in both directions — the only variable is whether you spent it.

That's the argument for treating art × hardware as a real lane rather than a hobby: **the skill isn't in the machine, and the margin isn't either.**

If you want the other half of this — building the physical object and the electronics inside it — that's [the hardware post](/posts/building-hardware-solo/). This one is specifically about the last twenty minutes.

## Sources

- **NIOSH (2025).** *Safe Desktop Vat Photopolymerization 3-D Printing.* CDC / National Institute for Occupational Safety and Health. — Uncured resin contains acrylates that can cause asthma or dermatitis; printing releases particles and gases not contained by the cover; curing generates inhalable particles and gases; sanding generates dust containing cured and uncured resin particles; use gloves rated against acrylates and isopropyl alcohol and change them frequently; once curing is complete, surface resin is usually fully cured and dermatitis risk is significantly reduced.
- **Formlabs.** *How to Prime and Paint 3D Printed Parts.* — Primer's flat neutral grey is used to highlight surface imperfections before painting; FDM layer lines may require sanding the whole model; fine-grit (>600) reworking after priming.

*Honest note on this post: the grit sequence is the standard workshop practice described in the sources cited, not a measured comparison of outcomes. The two pieces named above are my own finished work and are cited as examples of the finishing brief, not as controlled tests of any technique. The resin safety section is drawn from NIOSH guidance and is the one part of this post you should treat as a hard requirement rather than a suggestion.*
