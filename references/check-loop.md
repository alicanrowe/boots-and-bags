# The make-and-check loop

Render, compare against the named references, list what's off, fix, repeat until it holds up. Show the client only results that passed.

## Checks before every render (any fail stops the render)
1. **Clipping.** No part passes into another: hardware through leather, leather through the last or form, laces through eyelet walls, straps through buckles, lining through the upper, tools through the pockets that hold them. This is a measured gate at 0.5 mm, not an eyeball check (hardware.md "Clipping gate").
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

## Round 4 lessons (GAUNTLET, kit v4.0)
- Overlapping stiff lames laid with `piece(off='auto')` follow every step under them and crumple into soft, rolled cuffs ("floppy"). Lay each lame as a rigid plate instead: its flesh side is a straight incline, highest at its free edge (resting on the full-thickness part of the lame it laps) and falling evenly to its own tucked edge, with the real stack used only as a floor and faired. Never let a plate dip behind the lame it laps: that valley reads as corrugation.
- Skive every lame to about 0.6 mm where it tucks under its neighbour (10 mm lap), and keep it 2.6 to 3.5 mm with a rolled bead on the visible edge. Fewer, wider plates (about 30 mm) read as armour; six narrow rings read as a tyre.
- A large plain heel cup is a flat field. Fanning the heel lames round the ankle pivot (rays from the rondel) makes the counter part of the armour and gives the rondel a structural job.
- Where several lames converge (an ankle pivot), stop them short of the point (a 10 mm hole) and cover the hub with the cast part; otherwise narrow lames stack up and clip.
- Cast parts that sit on leather take their underside from the leather stack (KD lookup on the base stack), so they seat on stepped leather without floating or clipping. Cast a metal toe cap first and write it into the stack so the first leather lame laps over it.
- Medial hardware at the ankle costs pair clearance (pair gap needs 10 mm or more): keep the medial twin lower.
- kit v4.0 heel_fine: the heel and the top lift overlap by about 4 mm³ after smoothing and fail the clip check; clamp them apart (top lift below toplift_h - 0.2, heel above + 0.1).

## Round 4 lessons (SCALE, shingled scale courses on kit v4)
- `B.base`'s bottom boundary is not the feather line: patches of the last bottom survive the cut, so its lowest boundary loop can be a small island under the foot. Use the footprint outline (`B.fp.offset(0)`) lifted to `zb(x)` as the feather line.
- A distance-from-welt field has saddles on the vamp (the ball is wide, the waist is narrow and high), which split a course ring into islands. Weight width less than height (y x 0.4) and handle split rings; better, use the fraction f = d_welt / (d_welt + d_topline) so low courses follow the welt and high ones follow the topline, with no plain band under the binding.
- Lapped pieces laid with `off='auto'` copy every step of the edges underneath (ragged, crumpled tongues). Lay on a dilated, well-smoothed bed clamped just above the real stack, and relax each cut outline along itself before building the solid.
- Pointed tongues on a wedge's lift edges read as a row of teeth from the front; round them.

## Jacket lessons (round 4, STAY: boned channels and a cast busk)
- Relaxing a ribbed mesh folds triangles in the valleys: pinholes and dark dashes along every channel in the final. Apply
  `relief.channels` to each cut piece after `geo.relax` (before the dome), not to the shell, and use a smooth valley
  profile (sharp 2, a sin² rib); sharp under 1 leaves a kink that renders as broken dark lines.
- The 4 mm kit shell is too coarse for 20 mm channels; midpoint-subdivide it once before cutting.
- Put body seams in channel valleys (integer channels per panel) and stitch the other valleys with paired rows.
- The kit sleeve angle (`arm_coords` phi) uses a straight shoulder-to-wrist axis, so channels spin into a starburst at
  the elbow. Use an angle round the bent arm (frames carried from the upper arm to the forearm, blended at the elbow) and
  cut the underarm seam on that same angle.
- The kit sleeve ends about 7 cm above the wrist joint (the field's own end), so `base_cuts` cuff and cuff_extra never
  cut. Find the real cuff loop for bindings and fade relief by distance to it.
- A neckline detector by radius from the neck axis also matches the back hem; add a height test.
- Bindings that pass the overlay check: a C-section wrapped round the edge (mouth clears the leather by 0.75 mm and
  0.7 mm past the edge), path snapped to the real piece boundary (KD lookup, 1.2 mm) and lightly smoothed. Size the
  radius to the stack (thick/2 + 1.6 mm). Round sharp corners in the cut itself; smoothing a path round a corner pushes
  the lips into the leather.
- Hardware laid flat on the front: the check's parity test reports false hits when the +z ray grazes into a
  forward-leaning panel (waist to bust). Fill the concavity under the busk (a straight-front fill on a smooth x,z grid,
  outward only, which is what a busk does) and sit the plates 1.3 mm off the leather. Rays placing plates slip through
  seam gaps onto the far panel: despike rows against a median and nudge stud rays off gaps.
- Cast plates must wind outward (signed volume > 0) or `thin_metal` measures the wrong way and flags them.
- Let the busk plates be the front-edge finish (just inside the turned edges, over a placket); separate front-edge
  bindings fight the plates for the same 5 mm.
- Part-sheet tiles: the kit camera sits `dist` from the origin, not from the target, and the default shoulder, sleeve
  and cuff tiles aim at the left arm from the right side. Pass `info['parts']` aimed at the right arm and the real cuff.

## Round 4 lessons (BRIAR, couched-cord vines on a knee boot)
- Couched cord has to be big to read on a tall boot: 8 mm cord on a 440 mm shaft reads as piping. 15 to 17 mm at the root, tapering to about 7 mm at the topline, reads as a vine.
- Two near-vertical helices read as straps. Wind each vine most of a turn and weave them (alternate over and under along each vine) so crossings show in every view; lift the top cord by about 1.7 cord radii over a 24 mm bump.
- Make the cord the seam: cut the shaft into panels along the vine centre lines and lap each panel 1.5 mm past the line, so the cord hides both edges. A 4 mm lap shows as a second ridge beside a cord that tapers.
- Cut panels by removing base-mesh edges that cross each vine (test sides per vine, not against the nearest vine, or crossings leak). n bottom-to-top lines on a shaft give n panels plus one per crossing; one line alone does not split it.
- A branch or tendril must start buried in its parent's axis with a smaller radius; a branch that starts beside the parent shows as a cut stub (a nub).
- Aim roots at a point pushed 30 mm out from the base's bottom loop and lifted 9 mm, then project. A target on the loop is under the lasted edge and the root slides under the boot into the welt. Pick the bottom loop by length: the base has small sliver loops under the toe.
- A full-length medial zip fights a wound motif. Run a spiral zip under one vine (the cord sewn to the lapping edge) and keep that vine on top at every crossing.
- The pair-gap check counts anything medial below x = 130: keep thorns off the medial side and flatten cords there (about 60 percent) or the boots hit each other.

### Jacket lessons (round 4, STAY review)
- On a cropped jacket the arms hang below the hem, so the kit's `base_cuts` hem clip slices the forearms flat and
  the sleeve end reads as a bell. Pass a hem that returns 0 inside a forearm zone (distance to the elbow-hand axis),
  then cut the cuff yourself on a plane normal to the forearm (elbow to hand), not the straight shoulder-hand axis.
- The kit forearm is about 57 to 47 mm radius against a 37 to 23 mm body: scale the radius toward the elbow-hand
  axis (about 56 mm at the elbow to 38 mm at the wrist) for a close leather sleeve; the body check still reads 0.
- A yoke above boned panels needs its own relief: dome about 2 mm and a fan of short channels from the collar seam,
  tapered by t = dn/(dn + height above the yoke seam) so they fade before the piping on tall and short yokes alike.
- Grade equal-angle channels with theta + a(z)*sin(2*theta) (a > 0 at the waist, < 0 over the bust) and cut the
  panel seams on the same graded angle so they stay in valleys.
- Smooth the lining shell (laplace 10) before offsetting it; wrinkle noise shows as glints inside open cuffs.

## Round 4 review lessons (21 Nov 2026, boots thread across nine boots)
- Every thread's first delivery left the vamp and plain shaft as blank calf; four of nine had to go back for it. Before
  scoring, look at the vamp and the biggest panel first: each needs a bounded, moulded rest field (rays, keel, yoke,
  channels) in the boot's own motif.
- Self-scores ran 1 to 3 points high, always on Surface, Fidelity and Mood. The reviewer re-scores from the views;
  a thread's PASS stands only if the reviewer agrees.
- Many small lapped lobes (feathers, scales) drape and crinkle with piece(off='auto') and read torn or floppy. Use fewer,
  larger stiff plates on an analytic bed (GAUNTLET plate(), SCALE lay()), with the tips seated on the course below.
- Hardware under about 40 mm reads as trim on a tall boot; focal hardware wants 60 mm or more.
- The kit's heel and top lift share a face and fail clipping by 2 to 4 mm3: leave a 0.2 to 0.3 mm seam gap.
- The kit's red renders scarlet or tomato, not crimson: darken and desaturate it before the next round.
- The auto part camera lands inside the boot for parts that wrap the front: add close cameras (STAY render_close.py).

## Round 5 lessons (23 Nov 2026, BRIAR lace-up service boot)
- Lacing that reads real: each eyelet carries one strand. A diagonal comes up out of an eyelet, crosses the tongue and
  tucks under the opposite facing's inner edge (it comes up through the next eyelet from beneath). Two strands diving
  into one eyelet clip each other and look wrong.
- Model the lace's last 5 mm straight down the eyelet axis and hold those points fixed; let the free part bend above
  that, or smoothing drags the lace through the eyelet flange.
- Laces placed by pushing points off the leather, hooks and earlier laces come out wormy. Alternate a strong smooth
  with a clear pass about six times so the lace stays taut and bends only where it must.
- A speed hook that curls only outward from the facing is seen end-on from the side view and reads as a stud or
  spike. Give the curl a component down the shin (a rose prickle hooking toward the stem) so the hook shape reads in
  the lateral view, and make its base long and broad like a thorn's.
- Stacked heel lifts: keep the lift groove narrow (0.2 mm half width on a 0.28 mm grid); wider cuts read as separate
  plates with gaps.
- Ankle folds as a regular sine band read as corrugation. Use two or three individual folds, dipping toward the back,
  with uneven amplitude; one main flex break on the vamp plus a lighter one, never a ripple train.
- The look6 steer grain at boot scale reads as crackle at a 1:1 crop. Scale its cells about 3x finer and its bumps
  to about a third for boots (BRIAR's render wrapper does this with GRAIN_X and GRAIN_B).
- Style.flare must be a tuple (z_start, extra_mm); a bare number crashes the kit build.

## Round 5 lessons (HORN: side-zip boot with a moulded lame counter)
- Taubin-smoothing whole overlay pieces after the build moves the flesh side into the layer below (1 to 7 mm3 of
  clipping, worst against the welt). Smooth the grain side only, drop any inward move, and leave vertices within 4 mm of
  the welt alone; then run the clip check again on the smoothed meshes, not just at build time.
- A fan of lames cut on leg-angle curves meets at the back seam in a hard chevron, because |theta| folds there. It reads
  as a deliberate growth-ring chevron, but pillowed lames bulge and look lumpy at that seam. Keep each lame's pillow
  around 0.35 mm, and stop the backstay above the counter (lap it 10 mm under the top lame) so its edges don't show through.
- Quarter folds telegraph through a vamp lapped over them and break out as black shards along the vamp edge. Mask the
  lower piece's fold relief wherever the upper piece will lie.
- A zip line projected from a point 80 mm off the surface drifts about 0.25 rad round the leg. Place zips and hardware
  with a horizontal ray from the leg centre at a fixed angle.
- A procedural cell grain (steerhide) reads as crackle in 1:1 crops even with the bump turned down, because the cells
  sit in the colour and roughness too. Check every detail crop at 1:1 before the full set.
- Projecting points with `B.on` from far outside the last (x = leg centre - 80 mm at the back) starts outside the
  build grid (x from -30), where the field is flat: projections diverge (meshes kilometres away) and SDF casts that
  read the field come back empty. Start 50 to 55 mm off the leg centre, clamp x to the grid, and use iters=30.
- Keep cast SDF boxes tight and voxel 0.12 to 0.15 mm only on small boxes: an 80 x 80 x 50 mm box at 0.12 mm is
  ~190M samples and the build is killed for memory.
- A front zip's slider and pull must sit well under the topline (stop the teeth ~15 mm below it); a slider standing
  past the topline is the first thing a reviewer calls out.
- Product framing: fit each camera to the boots' projected bounds (move along and across the view line until the
  pair fills ~80% of a 4:5 frame) instead of fixed distances; see round5/stay/render5_stay.py `_fit`.
- A hero pair reads better with the second boot turned to show the back (HERO_ROT) when the back carries the design.
