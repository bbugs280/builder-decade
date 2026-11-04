---
title: "Printed Enclosure Tolerances: The Numbers Nobody Selling You a Tool Will Give"
translationKey: "printed-enclosure-tolerances"
date: 2026-11-04T09:05:00+08:00
lastmod: 2026-11-04T09:05:00+08:00
draft: false
tags: ["hardware", "3D printing", "enclosures", "DFAM", "solo builder", "maker", "tolerances"]
description: "Every guide to printed enclosures is written by someone selling the CAD package, the print service, or the design course. Here are the numbers, and where each one comes from."
cover:
  image: "cover-printed-enclosure-tolerances.png"
  alt: "A printed plastic enclosure half open on a workbench, a brass heat-set insert glowing in a soldering iron tip beside a small pile of machine screws, an unlabelled caliper resting across the part"
---

If you search for how thick to make an enclosure wall, every result on the first page is written by someone who wants to sell you something.

The design-software company says use their generative tools and the tolerances will take care of themselves. The print-on-demand service says upload your model and let them decide. The CAD course says the numbers matter less than the workflow. The advice is not necessarily wrong. It is just that none of these people have any incentive to make you able to do it without them.

So this post is the other thing: the numbers, with the reasoning that produces each one, so you can check them against your own printer and disagree with me where your machine is different.

## The wall

**2 to 3 mm for the main wall, at 4 or more perimeters.** Not because 2 mm is a magic value, but because of what the wall has to do: take a screw thread, survive being dropped, and not visibly flex when you squeeze it. A single 0.4 mm line is a cosmetic membrane. Four lines at 0.4 mm give you 1.6 mm of solid infill-free wall, and at that point the wall stops being infill-dependent.

The number that matters more is the perimeter count, not the width. A 2 mm wall printed as five full perimeters with no infill is stronger in bending than a 3 mm wall printed as two perimeters and infill, because infill bonds are the weak plane and a screw boss will split along them. Print walls as perimeters.

**Every wall dimension should be a multiple of your nozzle diameter.** At a 0.4 mm nozzle, 1.2 mm is three lines and 2.0 mm is five — both land exactly. 1.8 mm is four and a half lines, and your slicer will round it, giving you a wall thinner or thicker than your model says. If you are designing to 0.1 mm precision and printing at 0.4 mm, you are specifying more precision than the machine can deliver.

## Screw bosses

**Boss outer diameter should be about twice your insert's diameter** — the rule protects the wall of the boss around the hole, not the screw itself. A boss sized to the screw leaves too little material and it splits when the insert goes in or the screw is over-tightened.

**Never drive a machine screw straight into a printed boss for a joint that reopens.** Self-tapping into FDM works, once. The second disassembly strips it, because the thread is cut into layers and the layer bonds are the weak direction. For any joint you expect to open more than a couple of times — a battery door, a serviceable PCB mount, a lid you will be in and out of during prototyping — use a **heat-set brass insert**.

Heat-set inserts need a boss with enough wall to contain the melting plastic as the insert goes in, and enough depth that the insert sits below the surface. Too shallow and the insert protrudes and the joint won't close flush.

## Standoffs and component clearance

**3 to 5 mm of standoff height clears solder tails** on a typical through-hole PCB. This is the number that bites hardest, because it is not a design preference — it is the physical height of the solder protruding through the back of your board. Design a 2 mm standoff and the board sits on its own solder points, rocking, and your mounting holes are now carrying load they were not sized for.

**Allow 0.5 mm of component clearance** around tall components on the board so the enclosure wall does not press on them. Pressing is not just a fit problem — pressure on a component over time is a stress path and a way to crack a joint later, after the thing has been shipped.

## The printed hole problem

**A printed hole comes out smaller than you modelled it.** Not by a fixed amount — it is a function of the geometry, the material's shrink, and the direction of the curve. A hole modelled at 3.0 mm may print at 2.7 to 2.9 mm. Circular holes printed on FDM also come out slightly non-circular, because the slicer lays down straight segments.

Two ways to handle it, and both are legitimate. **Test it on your own machine** with a small hole-test coupon covering the diameters you actually use: print once, measure, and you now have a table for that printer and that material, which is worth more than any number in this post. Or **design the hole as a slot or an oversized round** when the exact fit is not structural, which removes the issue at the cost of a looser fit.

⚠️ Be honest with yourself about which one you are doing. An oversized round hole is not a tolerance decision, it is a decision that the fit does not matter. Sometimes it does not. Know that it is what you decided.

## Clearance between printed parts

For two printed parts that slide or locate against each other, **0.2 to 0.3 mm per side** is the ordinary starting point on FDM. Tighter than that and the parts bind on the extrusion bead variance. Much looser and the assembly rattles.

⚠️ This is the number most dependent on your specific machine — nozzle wear, belt tension, and filament brand all move it. It is a starting point for a test print, not a specification. The whole reason guides give ranges instead of values is that the range is honest and the single value would not be.

## Why the sources are like this

Here is the uncomfortable part. **The authoritative numbers for design-for-additive-manufacturing come from industrial DFAM guides** — the print services and the machine makers — because those are the organisations with the volume of failure data to produce them. The same organisations that sell the service.

That is not a conspiracy. It is a structural fact about who can afford to publish. But it produces an asymmetry worth being clear about: the numbers you will find are real, and they are published by people whose commercial interest is in you using their service rather than understanding the constraint.

The way out is the same as with the laser payback arithmetic: **take their numbers as the starting point and verify them against your own machine.** A tolerance coupon is a few grams of filament and twenty minutes. It converts somebody else's range into your value, and after that you are not guessing.

## Where this fits

This post is the dimensions leg of the same hardware argument the rest of this cluster makes. If the reason you have not printed an enclosure yet is that you stalled between a good model and a physical part, that stall is [its own post](/posts/digital-to-physical-pipeline/). If you are still deciding whether the machine is worth buying at all, do [the payback math](/posts/laser-payback-math/) first — it is cheaper than finding out afterwards.

And once the part is printed and dimensionally correct, the object is not finished. The difference between a functional print and one somebody keeps is the finishing, which is [its own post](/posts/painting-finishing-3d-prints/).

## Sources

- **DFAM guidebooks published by print services and CAD vendors** — the primary source of the wall-thickness, boss-ratio, and clearance ranges quoted here, including Protolabs/Hubs, dfamacademy.com, and textocad.com. These organisations sell design tools, print capacity, or courses; the numbers are quoted as theirs, and the post's argument about who publishes them is mine.
- **FDM dimensional tolerance derives from extrusion width, not from the model.** Wall dimensions land cleanly on multiples of nozzle diameter; clearance ranges of 0.2–0.3 mm per side on FDM are stated by the sources above as ranges, not values, because the value is machine-specific.

*The honest note on this one: I am not citing a study. The tolerances above are industry DFAM conventions, widely published and mutually consistent across the print services that publish them. Where I have said a number is machine-dependent, that is the part you should test rather than trust — including the numbers I have written down. A hole-test coupon costs a few grams of filament and beats any table, this one included.*
