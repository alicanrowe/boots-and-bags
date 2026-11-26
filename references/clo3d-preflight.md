# CLO batch pre-flight and failure log (script side)

A tower round costs about 35 minutes, and a stall costs more. Every failure class found in a round goes here as a
rule **in the same turn it is found**, with a check in `scripts/clo_preflight.py` where it can be checked
before sending. Run the pre-flight on every batch, and send nothing to the tower until it prints `preflight OK`:

    python3 scripts/clo_preflight.py <jobs_dir> [<forms_dir>]

Tower-side operation (gui.ps1 loop, watchdogs, clicking dialogs) lives in the render-farm skill. This file covers
what the build script and the job files must do.

## Modal dialogs stop the whole batch
A CLO info dialog is modal. The batch waits until someone clicks OK, and the Python API cannot dismiss it.
Prevent it instead:
- **Remesh on complex or tiny shapes** raises "The following patterns can not be remeshed due to complex
  shapes". In r3 it appeared once per call and stalled 11 minutes. It is triggered by
  `SetParticleDistanceOfPattern` on small or sharp pieces, and by re-importing an OBJ without tracing. Rules:
  - Never set particle distance on cut-out cells or pieces under 450 mm².
  - Never re-import untraced.
  - Pierce or inlay cells must be at least 450 mm² with rounded corners (the pre-flight flags this).
- Any new dialog seen on the tower becomes a rule here, naming the call that caused it.
- The build script logs a line before every slow call. A log that stops growing while CPU stays flat means a
  dialog is up. The tower watchdog checks for this (render-farm skill).

## Failure classes from rounds 1-5 (25-26 Nov 2026) and the rule for each
| Seen | Cause | Rule / check |
|---|---|---|
| Pieces vanish; `AssignFabricToPattern(x, None, ..)` errors | single-point closed outlines (one-edge pieces) | export closed outlines with corners plus spline points; pre-flight: >= 3 points |
| Lime-green sleeves and backs in turntables only | `AssignFabricToPattern(fab, pat, face)`: the 3rd arg is the face, and only face 1 was set | assign faces 0, 1 and 2 (`assign()` in build_all.py); pre-flight: every pattern has a leather |
| Black turntables | `ExportTurntableImages` writes RGBA with a transparent background; `colorHex` only affects `ExportRenderingImage` | composite the turntable PNGs onto #FFFFFF after export; for stills use `ExportStdViewImage(view, folder, colorway, w, h, True)` |
| Pieces on the floor | piece with no seam (under-layers, appliqué cups, a loose tether) | pre-flight: every piece is sewn; the builder deletes unsewn pieces before the sim and logs `DROP unsewn` |
| Boot panels lost, wrong boots paired | the whole upper in one OBJ: CLO merged or dropped UV islands | one OBJ per panel with UVs starting at 0,0 (`pair_XX_parts/`); log `PART LOST`; pre-flight checks each part's UV boundary |
| Some single-panel OBJs import False / add 0 patterns (r2-r4) | CLO's UV trace rejects an outline with an acute corner (< 45 deg); proven by probe 7 (trimmed 3 mm tips import, originals do not). A few panels fail for another, unknown reason (06 quarter_L__L, any variant) | trim UV tips < 45 deg by 3 mm before shipping; for known failures ship alternates (UV u-mirror + reversed faces, UVs in metres, 3D jitter) and the untrimmed source, tried in turn and logged as `RETRY` |
| Mottled soles | rigid core z-fights the leather shells | hide the core only when every shell landed, else log `CORE KEPT` |
| `SetRenderImageVideoProperties` TypeError | it takes an `ApiTypes.RenderImageVideoOptions` object (fields are `m_*`), not the JSON string | build the object |
| Lime backs and sleeves in viewport turntables (r3, with all faces assigned) | backs and sleeves drafted as seen from the front, so they face inside out | `FlipPatternNormal([...])` on back/arm pieces right after creation |
| Batch hung 40+ min with no log (r3, 07) | about 260 cut-and-sew cells, cut one by one | cap cells (24 per piece), time-box the loop, and write a line-by-line `live_log.txt` |
| Cut-and-sew cells (`CutPatternAlongInternalShapes`) return False in 2026.1, and the job then hangs (r4) | the API cut does not work here | show pierced or inlaid cells as a transparent PNG graphic (`ImportAsGraphic` + `AddGraphicStyleToPattern`) drawn from the cut-file cells |
| Std views and viewport turntables tint some panels lime/olive (r4) | viewport display, not the render | judge and show only render-engine images (`ExportRenderingImage`; turntable via `RenderImageVideoOptions.m_ImageVideo`) |
| `ExportStdViewImage` "Please provide filepath with extension" | it needs a full file name, not a folder | pass `views/viewN.png` |
| Main still 480x640 while turntables were 1600x2000 (r5) | `ExportRenderingImage` ran before `SetRenderImageVideoProperties` set the size | set render props first, then export the still (`_hi.png`); `SetQualityRender(True)` |
| Jackets draped half-settled, puffy (r5) | 500 + 300 sim steps (5 s) | 1500 + 800 steps; jackets still take only 2-4 min |
| Fret graphic never applied (r5): `GRAPHIC import None` | `ImportAsGraphic` was on none of pattern/utility/fabric/import_api; `GetGraphicStyleCount` returned 0, which an `or` chain skipped; `AddGraphicStyleToPattern` here takes `(pat, gi, [x, y], centre, face, z, angle)` | search every loaded `*_api` module (`api_modules()`, logged as `DISCOVER`), treat 0 as a number, use `AddGraphicStyleToPatternV2(pat, gi, x, y, w, h, face, z, angle)` or the list form + `SetGraphicStyleDimensionsOnPattern` |
| Whole sole mottled when one shell was lost (r5, 02/06/10) | core kept visible whenever any shell failed: it z-fights every shell | always hide the core; a lost shell is a `PART LOST` that fails the round anyway. Lost `__R` bottoms: ship the `__L` mesh mirrored in z with faces reversed and L's UVs (`alt4`) |
| TUCK tongue stuck out sideways (r1-r5) | a one-sided piece sewn by a symmetric seam is sewn to BOTH fronts | pre-flight flags one-sided pieces sewn to both `_L` and `_R`; the job post-process (kit/make_r6.py) drops one side and adds the cross-body seam |
| Zip closures invisible (r1-r5) | an edge-to-edge CF seam renders as a line; the 2026.1 API has no zipper creation call | sew a 9 mm metal-coloured tape strip into every zip seam (`insert_tape`), particle distance 5 mm on tapes only |
| Every jacket looked the same (r1-r5) | one 40 mm stand collar on every design | collar per design: snap tab (`tab=`), funnel (`flare=`), none; snaps via `AddButtonToPattern`; `SetPatternStrengthen` on collars, tabs, tapes |
| Site gate fails the stills (26 Nov): grey vignette background, ground plane ending in a hard rectangle | CLO's render studio backdrop | render with `m_bTransparency=True` and composite on #FFFFFF (`kit/tools/on_white.py`); the page must then pass `tools/gate.py` in the site repo |
| r6: graphics "No overlap", `AddButtonToPattern` False | CLO's 2D frame is not the frame the points were created in | place graphics by the frame-free list form `AddGraphicStyleToPattern(pat, gi, [0.5, 0.5], True, 0, 0, 0)` + `SetGraphicStyleDimensionsOnPattern`; map button points through `GetBoundingBoxOfPattern`. Styles: `utility_api.AddGraphicStyleFromImageFile` (utility_api also holds zipper, button and light-preset calls) |
| r6: FRET jacket bodies vanished | `DeletePatternPiece` on the unsewn under-layers took the bodies with them | never create pieces in CLO only to delete them; leave cut-file-only pieces out of the job |
| r6: AUGER sleeves torn open | the spiral zip tape had no arrangement, so it sat at the origin inside the body | every inserted piece copies its partner's arrangement (`arr_like`) |
| Flat, matte leather (r1-r6) | CLO's default render light | `SetLightPresetForExportRenderingImage(1)` (probe on 26 Nov: 0 pink, 2 warm, 4 green spill, 5 cold) |
| Every boot looked like the same plain sock boot (r1-r6) | straps, buckles, laces and zips existed only in the cut list, never in the CLO job | build them as thin 3D parts on the upper (plane sections of the panel meshes, lifted 1.5-2.5 mm, UVs = flat cut shape in mm), kind "trim" in parts.json (boots-jackets-v2 kit/tools/boot_hardware.py) |
| A buckle frame (closed ring) has two UV boundary loops | a hole in a traced outline | open the ring with a 1 mm slit so it traces as one outline with square corners |
| r7: graphics still not placed; `GetBoundingBoxOfPattern` gives only `{Width, Height}` | utility_api's `AddGraphicStyleToPattern` is `(pat, gi, x, y, w, h, face, z, angle)`; the x, y frame is unknown | try the piece-local origins in turn (centre, corner, y up/down) and log which sticks; same for buttons |
| r7: light preset 1 turned the white mannequin beige | warm key light | preset 5 keeps the mannequin white (house rule: plain white mannequin always) |
| r7: 3 jackets rendered fully transparent | likely two instances rendering at the same moment | if the still's PNG is under 60 KB, wait 20 s and render it again |
| Internal line leaves its piece | fold lines drawn end to end across the bounding box | clip marks to the piece; pre-flight probes segment midpoints |

## Running several CLO instances at once (the tower has the GPU for 2-4)
- Jobs must be independent: every input is read-only in the shared folder, and every output goes to `out/<job>/`.
- Claim a job with an atomic `os.mkdir(out/<job>.claim)` and skip it if that fails. Delete the `.claim` folder
  to re-run a job that crashed.
- Copy turntable frames from the paths that `ExportTurntableImages` returned, never by globbing the temp folder
  by time, because another instance's frames land there too. Per-job temp files (textures) go in `out/<job>/`.

## Before showing anything
Read the round's logs for `ERR`, `PART LOST`, `DROP`, `MISMATCH`, `SEAM FAIL` and look at every view, including
the turntables composited on white. A round with any of these is a test round. It is not shown to the owner.
