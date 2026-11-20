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
