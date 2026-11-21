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

## Jacket lessons (round 3, HARNESS)
- The jacket body field is a narrow-band distance (about 1 cm). A flat negative torso_adj larger than that leaves holes, so to loosen a waist, union the torso with a shape (a rounded-box column for a straight drop) using smin, with the shape faded out under the arms so it doesn't fuse to the sleeves.
- Strap ends round a ring or bar: build the end as a real fold, with the strap's top face wrapping the bar (inner radius = wire radius + 1.5 mm), and the return flap easing down onto the strap and riveted. Taper the strap to a tab (about half width) so a curved ring wire doesn't cut its corners, and run the last 15 to 20 mm radially into the ring. Make straps leather on both faces (no lining face), or every fold shows as a black tab on coloured leather.
- Buckle stacks: the tongue runs under the roller, rises through the frame, clears the fold of the buckle-side strap by at least 1.5 mm, and its tail lies on that strap. The prong rides the tongue's real height profile. Stop decorative top layers before the buckle.
- Paths on the body: cast rays from inside the body outward so the arms never catch them. A strap under tension bridges hollows: blend it onto the ring plane near a ring, and dilate the radius round a sleeve (taking the largest radius across the band's width) for cuff straps.
- On a bent arm, any seam or band built on the straight shoulder-to-hand axis spirals across the forearm and comes out ragged. Use a shoulder-elbow-hand frame blended at the elbow for the underarm seam, and the elbow-to-hand axis for cuff straps. Smooth the armhole field difference over the mesh (Laplacian, about 30 passes) before cutting, or the armhole seam follows the voxel steps.
- A tassel of beads and thongs on a centre-front zip clutters the zip at full-garment view and tips toward costume. A small cast ring pull in the garment's own motif reads better.

## Jacket lessons (round 4 prep, after the client rejected round 3)
- A jacket shell straight from the body field reads as one smooth moulded blob, so every panel looks flat. Pillow each cut panel up from its seams (about 5 mm over 40 mm), so the seams sit in valleys and each panel catches light on its own. Quilted channels (about 3 mm over a 24 mm pitch) on the sleeves or the waist read as made and padded, not as wrinkles.
- Free-hanging leather (tails, skirts, flaps) more than about 70 mm off the body reads as floppy. Make it structured or cut it. The kit's standoff check flags it.
- Wire-thin metal (under 2.5 mm through) reads as flimsy at full-garment scale, whether it's a halo ring, buckles or hook arms. The kit's thin_metal check flags it. Hardware is cast and chunky, or it's left off.
- One add-on motif on a plain jacket (a coil on the shoulder, horn tips) reads as a gimmick. The motif has to be the construction itself (lames, strap stacks, a structural cage), carried across the whole garment at one level of detail.

## Round 4 lessons (HORN: a cast heel that climbs the boot)
- A cast part that is the heel and also climbs the upper can't live in `st.heel` (the heel grid stops at the seat). Give
  the style an empty heel field, build sole and welt with `parts4.sole_parts` yourself, and cast the whole part with
  `B.cast`. Give any thin cast (a top lift) a grid that reaches below z = 0, or its mesh stays open and the clip check skips it.
- Cast hardware that lies on leather: build the leather first, then cut the casting with a keep-out of the last field minus
  `B.stack` (plus 0.4 mm air) and the sole block offset by the welt. It seats exactly on the moulded leather and clips 0.
- Ridges on a thick swept form: a union of spheres can't carve them (big neighbours fill every groove). Use a true tube
  field (distance to the nearest axis sample minus a radius that carries the ridges).
- Even rings round a tube read as a hose or knurling. Horn growth reads right as nested cones: each segment flares toward
  the tip and steps back in at the next ring, pitch graded about 15 mm at the root to 4 mm at the tip, step height tapering.
- A form that wraps both sides of the heel crowds the pair gap on the medial side. Flatten its section against the boot
  (oval, depth about radius / 1.5) instead of shrinking it.

## Round 4 lessons (STAY, cast busk on a corset shaft)
- A cast bar laid along the leather must not follow `stack_at` point by point: the stack is noisy along a path and
  the bar comes out with zebra-striped reflections (it reads as a zip or a ladder). Take a running max of the stack
  along the path (about 40 samples), smooth it, re-max with a short window and add 0.6 mm clearance.
- Project hardware paths with the lane held fixed (zero the y part of the gradient). Starting points far off the
  surface land on the wrong face: a spoon tip started 60 mm above the instep landed on the shaft front.
- Build hardware from swept sections with their own height and width per point (superellipse) and union the bits
  with manifold3d; SDF nearest-point tricks came out ragged where two bars lap.
- Relief laid over earlier relief telegraphs through as lumps: mask a lower panel's bones out under the next
  panel's lap.
- Bones spaced by a fraction of the panel width merge at a pinched waist: keep at least 7 mm between bone centres
  at the narrowest line (four bones, not five, on a 37 mm waist).
- The kit heel and top lift share a face and overlap about 2 mm3 after smoothing; build them with a 0.2 mm gap.
- The kit part sheet frames front hardware from inside the boot; add your own close-up cameras for the focal part.

## Round 4 lessons (COAT, kit v4.0)
- Kit v4.0 `binding` centres the edge tube at the piece's mid-thickness, so on any piece that lies on another layer the
  tube's lower half cuts into that layer (100+ mm³ of clipping per hem). Seat the tube on the piece's flesh plane
  instead (centre = edge + normal x (offset + r)), so it stands on the edge as a rolled tape.
- Bind only the edges that stay exposed. Where a later panel laps over an earlier one, end the lower panel's hem binding
  short of the lap, and stop any binding where a strap or belt will cross it; the stack map doesn't include bindings,
  so a later piece lies straight through them.
- A small strap laid with off='auto' across a lap step ripples, because it follows every bump of the stack. Lay it on a
  faired stack (dilate about 7 mm, average about 6 mm, never below the true surface) so it bridges the step like
  leather does.
- Cast parts on a shaft: a sheath or keeper built in a flat tangent frame lifts off the curved leg by s²/2R (about 20 mm
  over 46 mm). Measure height with the last's distance field, or sweep it along points projected onto the surface.
  Sweeping an oval section along projected points, with the underside riding a max-filtered and smoothed stack, gives
  a watertight one-body casting that never clips.
- Smooth-blended SDF castings leak when a scale term collapses (min(W, h) near zero lets a far region go negative);
  check `is_watertight` and the boundary edges against the box before trusting the mesh.
- A strap passing under a keeper bar reads as a cross on the boot. Keep the strap's line: a cast sheath that takes the
  strap point, in line with it, reads as hardware and avoids the cross.
- Thick padded panels on a tall shaft eat the pair gap at the topline; drop ease or flare to keep it at 10 mm.

## Round 4 lessons (SERAPH, layered feather tiers and a clasp over the crossing)
- Tiers that tuck under the next tier telegraph as a horizontal ridge through it, and tiers that run all the way to
  the topline stack too thick at the front where two wings overlap. Lap each tier about 20 mm under the next one and
  skive the lap to about 0.2 mm over its last 20 mm (thickness function of height), and trim the under wing about
  18 mm inside the over wing's edge. The ridge disappears and the crossing stays about 8 mm deep instead of 20.
- Moulded relief on a lower tier telegraphs too: fade it out over the last 10 mm before the next tier's notches.
- Feather lobes: rounded tips (sin-based lobes) read as drips, needle lancets as flames. A lancet with full convex
  sides, (1 - |x|)^0.6, and the point rounded off over about 14 % of the width reads as feathers. Grade the pitch and
  depth from root to tip so the row is never a comb, and give each feather a low dome (about 2 mm) between the creases.
- A cast plate over a lumpy stack of laps can't win either way: seated on the highest layer it floats (a gap you see in
  the side view), following the raw stack it comes out melted. Map the stack in the casting's own plane, seat the
  underside on the raw (max-filtered) map, and build the top from a heavily smoothed map plus a smoothly blurred lift
  wherever a lap rides high. The top stays fair and nothing floats.
- A frame with a bar across its window over two crossing strips reads as a cross in a circle. Close the window (a
  solid mandorla with a raised keel) or keep the strips' line.
- Fill a front V between crossing wings with a padded breast panel (about 5 mm), or the clasp bridges a hole.
- The kit's top lift and heel share a face at toplift_h; deep feather or lift cuts near it can make the clip check read
  0.5 to 0.9 mm³. A 0.3 mm seam gap at the top-lift line in the heel SDF fixes it and is a real seam anyway.
- Size a topline binding to the stack it wraps (radius = stack/2 + 0.9, max-filtered and smoothed along the loop, capped
  near 3.7 mm), or it sinks into thick layers and swells into a knob where a padded spine meets the topline.
