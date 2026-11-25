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

## Failure classes from rounds 1-3 (25 Nov 2026) and the rule for each
| Seen | Cause | Rule / check |
|---|---|---|
| Pieces vanish; `AssignFabricToPattern(x, None, ..)` errors | single-point closed outlines (one-edge pieces) | export closed outlines with corners plus spline points; pre-flight: >= 3 points |
| Lime-green sleeves and backs in turntables only | `AssignFabricToPattern(fab, pat, face)`: the 3rd arg is the face, and only face 1 was set | assign faces 0, 1 and 2 (`assign()` in build_all.py); pre-flight: every pattern has a leather |
| Black turntables | `ExportTurntableImages` writes RGBA with a transparent background; `colorHex` only affects `ExportRenderingImage` | composite the turntable PNGs onto #FFFFFF after export; for stills use `ExportStdViewImage(view, folder, colorway, w, h, True)` |
| Pieces on the floor | piece with no seam (under-layers, appliqué cups, a loose tether) | pre-flight: every piece is sewn; the builder deletes unsewn pieces before the sim and logs `DROP unsewn` |
| Boot panels lost, wrong boots paired | the whole upper in one OBJ: CLO merged or dropped UV islands | one OBJ per panel with UVs starting at 0,0 (`pair_XX_parts/`); log `PART LOST`; pre-flight checks each part's UV boundary |
| Some single-panel OBJs still not traced (r2) | unknown: clean UVs, one loop, valid outline | retry the traced import once and log `RETRY`; record the cause here once found |
| Mottled soles | rigid core z-fights the leather shells | hide the core only when every shell landed, else log `CORE KEPT` |
| `SetRenderImageVideoProperties` TypeError | it takes an `ApiTypes.RenderImageVideoOptions` object (fields are `m_*`), not the JSON string | build the object |
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
