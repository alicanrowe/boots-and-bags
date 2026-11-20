---
name: boots-and-bags
description: Design leather boots and bags in Blender on a real last or form, flatten the panels into 1:1 cutting patterns, design cast-metal hardware, check fit and clipping, render, and run the make-and-check loop against named reference makers.
---

# Boots and bags

Use this skill to design leather footwear (boots first) and bags that a person can actually cut, sew, last and wear, with sculptural cast-metal hardware. Every design ends as three things: renders that passed the reference check, 1:1 pattern sheets, and hardware files ready for a print or casting service.

The rules that come out of real review rounds go in `references/`. Read them before designing anything. They hold every correction the client has already had to make once.

## Before you start
1. **Do what was asked, no more.** Quote the client's words for the job. "Re-render" or "same layout as X" means new views of the current model, no geometry change. Change only what the words ask for and say in the report which parts changed.
2. Read `references/construction.md`, `references/patterns.md`, `references/hardware.md`, `references/check-loop.md` and `references/client-picks.md`.
3. Find the collection's aesthetic brief (one per collection, kept with the project, not in this skill). If there is none, write one from `references/brief-template.md` with the client's words and the named reference makers. Never copy a reference: borrow its hand, not its products.
4. Reference images go in the collection's `refs/` folder with a `RESEARCH.md` that describes each maker's hand in specifics (silhouette, panel lines, edge finish, stitch, hardware, leather, colour). Write it from the images, not from memory. Instagram blocks plain cloud fetches; Composio's Firecrawl scrape returns a post's caption and maker, and its AnyAPI Instagram post and user-posts tools return every carousel image URL (download them inside the Composio workbench, then bring them over as one zip). Make a contact sheet per maker and look at it before writing.
5. Use the brand theme (fonts, colours, logo) on every sheet, pattern and caption.
6. Blender 5.0+ (`pip install bpy` for headless work), plus `numpy trimesh shapely svgwrite pillow`. The FTW Flattening Toolset add-on does the panel flattening. Blender MCP is optional for live sessions with the client.

## Workflow: boots
1. **Brief.** Boot type (engineer, chelsea, lace-up, western, jodhpur, side-zip), shaft height, size and width, construction (see `construction.md`), leads and weights (for example 50 / 30 / 20), and which hardware is cast versus bought.
2. **Last.** Model on a scan of the physical last the boot will be built on, never on a made-up foot. Record the last's size, toe shape, heel height, and back height in the brief. No last scan yet: stop and ask for one.
3. **Upper.** Offset the last surface outward by the leather plus lining thickness. Draw panel lines on it (vamp, quarters, counter, shaft, tongue, facings, pull loops). Panel lines follow the last's feature lines: the feather line, the back seam, the instep.
4. **Flatten.** Split along the panel lines and flatten each panel with the add-on. Reject any panel whose flattening stretch is over 3 percent; split it or move the seam. Add allowances from `patterns.md` per edge type.
5. **Hardware.** Model eyelets, hooks, buckles, heel plates, toe guards, pulls and zip pulls to `hardware.md`, sized to the real leather stack.
6. **Check.** Run the checks in `check-loop.md`: clipping (hardware through leather, leather through last, laces through eyelets), panel stretch, stack thickness at every hardware point, seam lengths matching on both sides of each seam.
7. **Render** on a cloud machine, never on the client's own computer. Four views (side, three-quarter front, back, top) plus a hardware close-up, on the brand theme.
8. **Loop.** Put the render beside two or three reference images per lead and list what reads off. Fix, re-render, repeat. Show the client only passing results.
9. **Deliver.** Pattern sheets (1:1 SVG and tiled PDF with a 100 mm test square on every page), a cutting list (panel, leather, thickness, grain direction, quantity), hardware STLs with a material and finish note, and the render sheet.

## Workflow: bags
Same loop, with the form in place of the last: a body form (box, cylinder, pillow, sling) modelled to the stated capacity and the client's carry (hand, shoulder, crossbody, worn on the body). Panels are body, gussets, base, flap, pockets, straps and handles. Bags are mostly developable surfaces, so flattening stretch should be near zero; a curved panel means darts, a moulded part, or a gathered edge, and the brief says which. Straps and handles are constant-thickness leather that a person could cut, fold and stitch.

## Rules that are easy to break
- Every leather part is constant-thickness sheet. No sculpted leather unless it is moulded or wet-formed, and then the brief says so.
- Everything that wraps something either opens (buckle, snap, zip, laces) or is sewn closed. No floating straps or closed loops with no way on or off.
- Hardware sits on the leather, never inside it. Rivets and posts have a real hole and a back.
- A seam is a line on both panels with matching lengths (to 1 mm) and a stated seam type.
- Panel lines follow the form. A seam across the flex point of the foot, or across the bag's fold, is wrong unless the brief asks for it.
- Public text (sheets, site copy, captions) never names the reference makers. The brief keeps the influences.

## Getting it made
`construction.md` lists the routes: by hand, with a bootmaker or small workshop, or with a sampling factory. Contacting a maker or ordering anything waits for the client's go-ahead.

## Keep this skill improving
When the client flags something, or a check misses a problem, write the rule into the matching reference file in the same session (taste remarks go in `client-picks.md` with the client's words). Then publish the skill.
