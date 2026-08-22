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
}
