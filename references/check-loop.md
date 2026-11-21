# The make-and-check loop

Render, compare against the named references, list what's off, fix, repeat until it holds up. Show the client only results that passed.

## Checks before every render (any fail stops the render)
1. **Clipping.** No part passes into another: hardware through leather, leather through the last or form, laces through eyelet walls, straps through buckles, lining through the upper.
2. **Stack.** At every hardware point, the post or setting fits the modelled leather stack.
3. **Stretch.** Every flattened panel is under 3 percent stretch.
4. **Seams.** Each pair of joined edges matches in length to 1 mm.
5. **Wear.** For boots, flex the forefoot 30 degrees and recheck clipping. For bags, load the straps and check the anchors.

## Each pass
1. Open the render next to two or three reference images per lead influence.
2. Write what reads off, specifically and by place ("shaft top edge: dead straight, the references cut it on a curve"; "buckle: reads stock, not sculpted").
3. Decide if it's this piece or the shared setup (materials, lighting, a helper), and fix it once at the source.
4. Re-render and check again. Stop when the list is empty or holds only taste calls for the client.

## Report format (one per piece)
```
<piece>: clipping 0, max stretch X.X %, seams OK, stack OK
Passes: what matches the references
Off: 1) ... 2) ... 3) ...
Changed since last round: ...
```

## Lessons from the first three boots
- Toe room is checked on both edges of the toe box, not only length: a pointed or offset toe can be long enough and still pinch the big toe on the inside edge. The last is never narrower than the foot plus 1.8 mm per side, or lower than the foot plus 4 mm, anywhere ahead of the waist.
- Toe height room is measured over the top of the toes only; the tread resting on the insole is not a fit failure.
- A short boot still gets the entry and ankle-ease checks, measured from 30 mm below its topline.
- Square and chisel toes need a true distance field at the toe end. A lofted section field leaves the toe face open (you see nested rings through the front in the hero view). Check the hero view for this before anything else.
- Drop zero-area sliver pieces after meshing; smoothing them throws spikes beyond the toe.
- Hardware has to read at sheet size. If a part is under about 3 mm across and hugs the leather, nobody sees it: make it one structural part (a guard, a cage) rather than thin strokes.
- Render the top view without the floor shadow, and keep black leather black (exposure down, roughness about 0.5), or it reads as grey plastic.

## Round 2 lessons (client: round 1 "all suck and feel unrealised")
- A boot model reads as a blob until it has what every made boot has: lapped panels with a real edge step, stitch rows 1.5-2.5 mm in from every panel edge (3-4 mm pitch), a welt with stitching, a sole/welt split line, stacked heel lifts with a darker top lift, and a finished topline (binding or turned edge) with a pull aid or closure. Build these into the kit, never leave them for "later".
- Benchmark every design before showing it: put the side view next to a photo of a classic boot of the same type and score proportions (toe extension 14-35 mm, toe height 15 mm behind the tip, toe spring 9-15 mm, heel height, shaft height for the type, ankle ease, welt 2.5-6 mm, at least 3 panels, stitch rows). The scorecard lives with the collection (round2/bench/SCORECARD.md).
- Interpolate last tables with a smooth monotone curve, and fair the final profile (Gaussian along the length, re-clamped to the foot envelope). Piecewise-linear tables and hard max() envelopes show up as creases across the vamp.
- Short boots look wrong when the shaft hugs the leg: the instep must ramp into a shaft that stands slightly off the front of the ankle (blend radius ~26 mm, front-back aspect ~1.2).
- Pull-on tall boots (engineer, western) need an ankle girth that clears the heel-instep diagonal (~340 mm for a size 11), so the shaft stands off the ankle by 80-100 mm. That is correct, not a fault.
- Straps defined as infinite bands must be clipped to the region a real strap occupies (below the topline, in front of the heel or around the ankle only), or they show as flaps and diagonal stripes.
- Stitch rows must split where the surface projection misses, or a dash bridges the gap as a long needle.
- Each design carries a buyable bill of materials (upper leather and thickness, lining, counter, toe puff, insole, welt, sole, heel, thread, hardware cast or bought, construction). Leather is chosen per design.

## Jacket lessons (round 3, THORN)
- Space repeated edge features (crown points, scallops, teeth) by arc length along the edge, not by angle round the neck: a neckline is an oval, and equal angles bunch the back points to half the width of the front ones.
- Grow a stand collar with the radial direction as the edge normal so it stands up; projecting "up" onto a near-flat shoulder normal lays it outward like a brim.
- A seam cut along exactly x = 0 on a symmetric mesh lands on vertices and comes out wavy; offset the isoline by under a millimetre.
- Stitch-only motifs (vines, ticks) vanish at full-garment scale on black leather. Couch a 3 mm tonal leather cord and stitch over it, so the line shows as relief; where two cords cross, lift the top one into a bridge so they weave instead of passing through each other.
- Many seams compete with a surface motif. When the motif carries the line work, drop the princess seams and keep a centre back seam as its spine.

## Round 3 lessons (client: round 2 "super ugly and unoriginal")
- Benchmarking against classic boot types makes classic-looking boots. Benchmark for fit and makeability only; take the look from the brief (here: armour, coats, crowns, corsets, feathers, horns) and give every design one silhouette idea you can see in the side view: a shaped topline, a sculpted or structural heel, layered panels, a flare.
- Ornament has to read at page size or it reads as noise: a small floating ring behind the heel looked like a stray pin; making the heel itself the hoop worked. Raised ridges on a toe guard read as broken chrome; a plain guard reads as made.
- Leather that renders glossy grey looks like rubber. Matte calf (roughness about 0.55, light coat, fine grain bump) and a darker print curve for black views make it read as leather. Keep the curve off highlights so steel and silver stay bright.
- A pull-on shaft wider than the build grid is cut flat at the grid edge and sends the topline binding out in a spike. Widen the grid (x0) for wide shafts and filter topline rays that miss.
- Zip pulls drawn at the topline stick out as hooks; leave them tucked in the seam.
- "Remote" helper agents in this setup ran on the same 4-core machine and the same /tmp folder, so they don't add CPUs and parallel mesh builds can run out of memory. Check `nproc` and the hostname before splitting work, give each job its own WORK folder, and run at most 2 to 3 builds at once.
- Page crops: fade only the pale floor shadow toward the frame edge, never the boot, and leave about 9% padding so tall boots aren't clipped.
