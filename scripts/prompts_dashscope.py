"""Image prompts for Builder Decade — DashScope Wan2.6-t2i.

Style: warm editorial, cinematic, "maker / workshop / build-in-the-AI-era"
imagery with amber/copper accents. NOT the navy/crimson gym-app look — this is
a long-form human-tech reading site. Each prompt is self-contained (no text
overlays — text is rendered by Hugo/CSS).

⚠️ ETHNICITY RULE (Vincent, 2026-08): any subject who is a PERSON must be
drawn as ethnically ambiguous — plausibly Asian, Western, or mixed heritage.
The audience spans markets (EN + ZH), so no single-ethnicity read. Always
include phrasing like "mixed East Asian and Western heritage, ambiguous
ethnicity" on any human subject.

⚠️ PALETTE: warm editorial (cream/ink/amber), NOT navy/crimson. The home hero
is a STOCK PHOTO (static/images/hero.jpg), not AI art. Post covers are the
cinematic AI art generated from these prompts.
"""
PROMPTS = {
    # Home hero — broad, "build in the AI era" theme
    # (Superseded: hero is a static/images/hero.jpg stock photo. Kept for
    #  reference only — do NOT regenerate without updating palette.)
    "hero": (
        "Cinematic wide shot of a maker's workshop bench at dusk, a craftsman "
        "of mixed East Asian and Western heritage with ambiguous ethnicity in "
        "his 40s assembling a small device by warm amber lamplight, a laptop "
        "with code and circuit boards beside a coffee mug, deep shadow, "
        "volumetric light rays, moody chiaroscuro, film grain, quiet focus, "
        "photorealistic, shallow depth of field, 16:9 composition, no text, "
        "no watermark"
    ),
    # Welcome / brand anchor — the decade-long building journey
    "welcome": (
        "A long workbench receding into warm darkness, each station lit by a "
        "small pool of amber lamplight, tools and half-finished projects at "
        "intervals, symbolizing years of consistent building. Warm charcoal "
        "and copper atmosphere, cinematic perspective, faint dust in the "
        "light, moody and contemplative, photorealistic, film grain, no "
        "people, no text, no watermark"
    ),
    # "Why build for a decade" — contrast between quick hack and long game
    "decade": (
        "Dramatic split composition: on the left a tangle of cracked, "
        "discarded circuit boards and broken prototype shells falling apart "
        "mid-air, on the right a solid finished device standing on a wooden "
        "bench, its glowing amber status light steady. Deep charcoal "
        "background with copper and amber glow, high contrast, cinematic "
        "lighting, photorealistic, moody, no text, no watermark"
    ),
    # "The one-person product team is real" — a single builder dwarfed by
    # the productive glow of one workstation, no teammates
    "one-person-team": (
        "A lone figure of mixed East Asian and Western heritage, ambiguous "
        "ethnicity, seated at a single workstation in a vast dark workshop, "
        "a solitary amber desk lamp carving the only pool of light, monitors "
        "glowing with code and product prototypes, the surrounding benches "
        "empty and unlit, conveying the scale of what one person can now "
        "produce alone. Deep charcoal and copper atmosphere, cinematic "
        "chiaroscuro, volumetric light, photorealistic, moody and "
        "contemplative, shallow depth of field, no text, no watermark"
    ),
    # "Solo founders are winning" — the outcome, not the solitude: a single
    # builder stepping back to survey a shipping, growing product
    "solo-founders-winning": (
        "A single builder of mixed East Asian and Western heritage, ambiguous "
        "ethnicity, seen from behind at a distance, standing and looking at a "
        "large glowing wall of monitors in a warm dark control-room-like "
        "space, each screen showing rising revenue charts, product dashboards "
        "and delivery-truck-style shipping containers, a quiet triumphant "
        "scale. The lone silhouetted figure is small against the productive "
        "glow, conveying that one person now carries the output of a team. "
        "Deep charcoal and copper amber atmosphere, cinematic volumetric "
        "light, photorealistic, moody and assured, wide composition, no text, "
        "no watermark"
    ),
    # "The AI coding stack I actually use" — one focused workstation, a single
    # terminal-centric toolchain, deliberate rather than a drawer of tools
    "ai-coding-stack": (
        "A clean single workstation at night, a laptop showing a focused "
        "terminal with a bright code editor and a subtle AI assistant panel, "
        "one warm amber desk lamp, a small notebook and a coffee mug beside it, "
        "the desk deliberately uncluttered — exactly the tools needed and "
        "nothing more, conveying focus and intent rather than tool sprawl. No "
        "person. Deep charcoal and copper amber atmosphere, cinematic "
        "chiaroscuro, volumetric light, photorealistic, moody and calm, "
        "shallow depth of field, no text, no watermark"
    ),
    # "What AI agents still can't do" — a workbench split between the part the
    # machine touches and the part only a human hand reaches
    "what-agents-cant-do": (
        "A moody split composition across a dark workbench: on the left, a "
        "glowing laptop and monitor displaying dense code and a terminal, all "
        "precise and automated, warm amber light; on the right, a single brass "
        "drafting compass, a hand-drawn sketch and a pencil resting on paper, "
        "human and imperfect, lit by a cooler shaft of light — the reach of "
        "the machine versus the reach of the hand. Deep charcoal and copper "
        "amber atmosphere, cinematic chiaroscuro, volumetric light, "
        "photorealistic, contemplative, no people, no text, no watermark"
    ),
    # "The real cost of shipping solo" — time and attention as the currency
    "cost-of-shipping-solo": (
        "A dark warm workbench seen from above at an angle, a pair of hands of "
        "mixed East Asian and Western heritage, ambiguous ethnicity, weighing "
        "an hourglass of glowing amber sand in one hand and a small stack of "
        "coins scattered beside a laptop in the other, conveying that the real "
        "cost is time and attention, not money. Deep charcoal and copper "
        "amber atmosphere, cinematic chiaroscuro, volumetric light, "
        "photorealistic, moody and contemplative, shallow depth of field, no "
        "text, no watermark"
    ),
    # "No-code vs vibe code vs real code" — three parallel paths, one choice
    "no-code-vibe-code": (
        "Three distinct workstations in a row receding into warm darkness, "
        "each lit by its own pool of amber light: the first with colorful "
        "drag-and-drop building blocks, the second with a stream of "
        "glowing AI-generated code streaming down a monitor, the third with a "
        "hand-written page of careful code next to a coffee mug. Conveying "
        "three different ways to build, equally valid, a deliberate choice "
        "between them. Deep charcoal and copper amber atmosphere, cinematic "
        "perspective, volumetric light, photorealistic, moody, no people, no "
        "text, no watermark"
    ),
    # "Week three" — the trough, a half-finished bench going dark
    "week-three": (
        "A half-finished project abandoned on a dark workbench, tools laid "
        "down mid-task, a soldering iron still warm with a thin curl of smoke, "
        "a half-assembled device and scattered notes, the amber desk lamp "
        "flickering as if about to go out, conveying the quiet stall that hits "
        "in the messy middle. Deep charcoal and copper amber atmosphere, "
        "cinematic chiaroscuro, volumetric light, photorealistic, moody and "
        "melancholic, no people, no text, no watermark"
    ),
    # "Ship one tiny thing" — a single finished object, small and complete
    "ship-one-tiny-thing": (
        "A single small, fully-finished object sitting alone on a dark wooden "
        "workbench under one warm amber lamp — a neatly assembled little device "
        "or crafted piece, complete and quietly perfect, beside a long row of "
        "identical empty spots receding into the dark suggesting many more to "
        "come. Conveying completion and repeatable craft. Deep charcoal and "
        "copper amber atmosphere, cinematic chiaroscuro, volumetric light, "
        "photorealistic, moody and calm, shallow depth of field, no people, no "
        "text, no watermark"
    ),
    # "Building hardware solo" — a single maker's bench, physical device
    "building-hardware-solo": (
        "A solitary maker's electronics workbench at night, a single device "
        "half-assembled amid a microcontroller, wires, a multimeter and a "
        "soldering iron, a bright magnifier lamp casting warm amber light, "
        "schematic pages pinned behind, conveying the intimate focused craft "
        "of assembling a physical thing alone. Deep charcoal and copper amber "
        "atmosphere, cinematic chiaroscuro, volumetric light, photorealistic, "
        "moody, no people, no text, no watermark"
    ),
    # "Solo founder vs co-founder" — a fork in the road, a decision, not solitude
    "solo-founder-vs-cofounder": (
        "A single builder of mixed East Asian and Western heritage, ambiguous "
        "ethnicity, seen from behind, standing at a literal fork on a long dark "
        "workbench — the bench splitting into two diverging paths, the left going "
        "ahead alone into a narrow focused lane lit by one warm amber lamp, the "
        "right widening into a space of two empty chairs and a second unlit lamp, "
        "the builder paused between them weighing the choice. Conveying a "
        "deliberate decision rather than solitude or default. Deep charcoal and "
        "copper amber atmosphere, cinematic volumetric light, photorealistic, "
        "moody and contemplative, shallow depth of field, no text, no watermark"
    ),
    # "One year of building" — a long row of shipped things, a body of work
    "one-year-of-building": (
        "A long workbench receding into warm darkness, lined with many small "
        "finished objects and devices at regular intervals, each lit by its "
        "own faint pool of amber light, forming a row of completed work "
        "stretching toward the horizon, conveying the accumulation of a full "
        "year of small shipped things. Deep charcoal and copper amber "
        "atmosphere, cinematic one-point perspective, volumetric light, "
        "photorealistic, moody and contemplative, no people, no text, no "
        "watermark"
    ),
    # "How to get your first users" — quiet distribution: a single builder
    # showing a finished thing to a gathered crowd, the product speaking for
    # itself rather than the builder pitching. Show-don't-tell.
    "how-to-get-first-users-solo": (
        "A single builder of mixed East Asian and Western heritage, ambiguous "
        "ethnicity, standing quietly behind a small finished device glowing "
        "with warm amber light on a dark workbench, while a soft-focus crowd "
        "of varied faces (East Asian, South Asian, Black, Latino, Middle "
        "Eastern, Western — a genuine mix) gathers beyond the bench, drawn "
        "toward the object rather than the builder, the builder's hands resting "
        "calmly, not gesturing or pitching — the product speaking for itself, "
        "conveying quiet leverage and show-don't-tell rather than cold "
        "outreach. Deep charcoal and copper amber atmosphere, cinematic "
        "volumetric light, photorealistic, moody and assured, shallow depth "
        "of field, no text, no watermark"
    ),
    # "Reuse vs rebuild" — a fork in the road: one path you keep custody of,
    # the other path held/leased by someone else. Must show a REAL divergence,
    # not a single straight aisle.
    "reuse-vs-rebuild": (
        "A literal fork in a long dark workbench, the wood splitting into two "
        "clearly diverging paths: the left path a host of small readymade "
        "interchangeable components and identical off-the-shelf boxes arranged "
        "in neat rows, each labeled as if rented or leased, lit by a cooler "
        "pool of light suggesting someone else's ownership; the right path a "
        "single hand-crafted device glowing with warm amber light, uniquely "
        "yours, standing alone and permanent. A single builder of mixed East "
        "Asian and Western heritage, ambiguous ethnicity, seen from behind at "
        "the fork, paused weighing which path to take and which to keep. "
        "Conveying custody and ownership rather than mere cost. Deep charcoal "
        "and copper amber atmosphere, cinematic volumetric light, "
        "photorealistic, moody and contemplative, shallow depth of field, no "
        "text, no watermark"
    ),
    # "How to price a SaaS as a solo founder" — a pricing decision, weighing one
    # option against another on a scale or between two hands. Decision, not money.
    "solo-saas-pricing": (
        "Close-up of a workbench at night, a single builder of mixed East Asian "
        "and Western heritage, ambiguous ethnicity, seen only as a pair of hands, "
        "weighing two small objects in balance: in the left hand a single spent "
        "coin and a receipt, cool lit and transactional, in the right hand a small "
        "recurring glowing amber loop or an hourglass of flowing light, warm and "
        "compounding — the hands paused mid-decision between a one-time price and "
        "a recurring value. Conveying a deliberate pricing decision, not money "
        "greed. Deep charcoal and copper amber atmosphere, cinematic chiaroscuro, "
        "volumetric light, photorealistic, moody and contemplative, shallow depth "
        "of field, no text, no watermark"
    ),
    # "The one-person workweek" — six jobs, one seat: many hats hanging around a
    # single chair, the builder choosing to set most of them down. Scope-cutting.
    "one-person-workweek": (
        "A single wooden chair at an empty dark workbench under one warm amber "
        "lamp, several distinct hats — a builder's cap, a customer-service "
        "headset, a banker's visor, a marketer's cap — hanging on a row of pegs "
        "behind it, most of them shadowed and receding into darkness while one "
        "hat rests alone beside the chair in the light, conveying that a solo "
        "builder must set down five of six roles and keep only the one that "
        "matters, one lit hat resting beside it in the light. Conveying that a solo "
        "builder must set down five of six roles and keep only the one that "
        "matters. Deep charcoal and copper amber atmosphere, cinematic "
        "volumetric light, photorealistic, moody and calm, shallow depth of "
        "field, no people, no text, no watermark"
    ),
    # "Solo founder burnout" — a single lamp guttering low over an empty bench,
    # the quiet slide no one witnesses. Melancholic, not dramatic.
    "solo-founder-burnout": (
        "A single builder of mixed East Asian and Western heritage, ambiguous "
        "ethnicity, seen from behind, head bowed and hands resting flat on a dark "
        "workbench, a single amber desk lamp guttering low as if about to go out, "
        "its light just barely reaching the scattered tools and half-finished "
        "device before fading into deep shadow, the surrounding workshop empty "
        "and silent, conveying the quiet exhaustion and isolation of burning out "
        "alone with no one else to notice. Deep charcoal and copper amber "
        "atmosphere, cinematic chiaroscuro, volumetric light, photorealistic, "
        "moody and melancholic, shallow depth of field, no text, no watermark"
    ),
}
