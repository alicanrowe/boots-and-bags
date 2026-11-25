# Patterns

Starting values. Confirm each on the paper and cheap-leather mockup, then write the confirmed value back here.

## From 3D to flat
1. Draw panel lines on the offset upper (or bag form), not on the bare last.
2. Flatten each panel (FTW Flattening Toolset: unwrap, minimize stretch, real-world scale).
3. Reject a panel whose stretch is over 3 percent. Split it, add a dart, or move the seam.
4. Check against the classic method once per new last: masking tape on the last, draw the lines, peel and lay flat. The digital panel should match within 2 mm.

## Allowances (added outside the net line, per edge)
| Edge | Allowance |
|---|---|
| Lasting (cemented) | 15 to 18 mm |
| Lasting (welted) | 18 to 22 mm |
| Stitchdown flange | 10 to 12 mm, turned outward |
| Lapped seam underlay | 8 to 10 mm |
| Closed (butted or turned) seam | 4 to 6 mm |
| Folded edge | 4 to 5 mm, skived |
| Bag turned seam | 6 to 10 mm |
| Raw edge | 0 |

Skive overlaps to about half thickness over 8 to 12 mm so seams don't ridge.

## Stitch
- Hand saddle stitch: 3.0 to 4.0 mm pitch on bags, 2.5 to 3.0 mm on boot uppers.
- Stitch line 3 to 4 mm in from the edge. Show it as a dashed line on the sheet.

## Sheet format
- 1:1 SVG plus a tiled PDF (Letter and A4) with a 100 mm test square and tile marks on every page.
- Each panel: name, quantity and side (L/R, cut 2 mirrored), leather and thickness, grain arrow, notches at every seam match point, net line solid, cut line outer, stitch line dashed.
- Seams that join must have matching lengths to 1 mm (the check prints both).

## Lessons from the v2 restart (25 Nov 2026), to confirm on the mockup
- Panels made from face labels have a triangle staircase on every edge, which runs about 30 percent long. Cut the
  mesh exactly along the label fields first (level-set split), then label faces. Both panels then share the same
  boundary vertices and seam lengths match by construction.
- Stretch limits by panel role (area-weighted 95th percentile of the per-face singular values, ignoring the band
  within 30 mm of the feather line and the toe box, which are lasted): free shaft panels 3 percent; quarters and
  fronts that are lasted or blocked over the throat up to 6 percent; crimped fronts and wet-moulded shells up to
  20 percent (the moulding takes it up). Seams in lasted areas may ease up to 4 percent; seams into a moulded or
  crimped piece up to 10 percent. The vamp-to-insole seam at the toe is gathered in lasting, so it has no length
  check.
- An open boundary is two different things: the feather line (sews to the insole) and the topline (raw or bound).
  Split them by height before naming seams.
- The xTool P3 bed is 914 x 455 mm usable. A men's 40R back is about 560 mm across, so jacket backs always need a
  centre-back seam or a yoke and gores; design that seam in, don't fight it. Straps and tethers over 890 mm need a
  skived lap join.
- The insole is a flat pattern whose outline is the feather line projected to plan, keyed run by run to the upper's
  bottom edges. That gives CLO a piece to sew the upper to (a boot can't be sewn to an OBJ).
