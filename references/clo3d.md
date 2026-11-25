# Driving CLO3D

CLO can be driven fully from its own Python editor, with no third-party plugin and no file dialogs. That is the route that works under remote control on a Mac.

## What blocks the obvious route
- File > Import opens the macOS file picker, which runs in a separate system process. A computer-use grant for CLO does not cover it, and screenshots don't show it.
- CLO's Import OBJ options window has the same problem while a picker is open.
- A full-screen Space blocks moving CLO's windows. Ask for a normal desktop first.
- The community MCP servers (as of Nov 2026): two are Windows-only DLLs, and one (a Python file-IPC listener) works on macOS but blocks CLO's UI while it listens and can exec code in dev mode. Prefer the built-in editor below; only add an MCP server after reading its code and pinning a commit.

## The route that works
1. Menu **Edit > Python Script** opens the Python Editor: a code box, a Run button (the triangle, top left) and a log console underneath.
2. Type the script into the code box (whole-field replace is fine), press Run, then read the console.
3. Keep each script short and print one tagged line per result (`print('IMP', ...)`), because the console only shows the last few lines.
4. Never walk a large folder (`os.walk` over Downloads): it blocks CLO, and the first touch of Downloads, Desktop or Documents triggers a macOS permission box that the person has to Allow. Point at exact paths instead.
5. Put the files where CLO can read them without a prompt: CLO's own asset folder (`utility_api.GetCLOAssetFolderPath()`) or a folder the person has already allowed.

## Getting files into CLO with no prompts
- Best: carry the mesh inside the script. Decimate the OBJ (about 20k faces), zlib + base64 it, paste it as a string, and have the script write it to `utility_api.GetCLOTemporaryFolderPath()` before `ImportOBJ`. CLO's own temp folder never triggers a macOS privacy prompt, and no file picker or folder grant is needed.
- Use `ApiTypes.ImportExportOption()` for the options object (`import ApiTypes`); `import_api` does not hold it. Fields include `scale`, `bSingleObject`, translation values. CLO's temp folder is `~/Library/Application Support/CLO Virtual Fashion/<app>/<build>/` and writes there work with no prompt (tested Nov 2026).
- Limit: the data has to be typed by the model, and one wrong base64 character breaks the whole file. Fine for a small test part (under about 10 KB), not for full boots. For real meshes, have the person connect a non-protected folder (one under their home, not Desktop, Documents or Downloads) to the session themselves with Add folder in the Claude app; then copy files there and point `ImportOBJ` at it. Folder-access requests from Claude can be refused by the safety layer, so ask the person to add it.
- Split anything over about 200 KB of base64 across several Run presses, each appending to the same temp file.
- Otherwise, the person grants a one-time permission that ends the prompts for good: either click Allow the first time CLO asks for Downloads, or turn on CLO under System Settings > Privacy & Security > Full Disk Access. Only the person can do this. Never try to change privacy settings yourself.

## Things that stop remote control
- A locked or sleeping screen stops every action. Ask the person to keep the Mac awake and unlocked while CLO work runs (or set Lock Screen to a longer delay themselves).
- A full-screen Space (see above).
- A macOS permission box from CLO: it is a separate process, so only the person can answer it.

## API calls used
- `import_api.ImportOBJ(path, options)` imports headless, with no dialog, when options are given. `import_api.ImportFile(path)` shows the dialog, so avoid it.
- `import_api.ImportAvatar(path)` for an avatar file; `import_api.ImportDXF(path, option)` for flat patterns.
- `export_api.ExportThumbnail3D(path)` and `export_api.ExportSnapshot3D(...)` save the 3D view to an image.
- Our OBJs are millimetres with Z up. CLO is Y up, so convert axes on import (Y takes our Z).

## Tested 20 Nov 2026 (CLO 2026.1, macOS)
- Working end to end: a connected folder under the person's home (not Desktop, Documents or Downloads), files copied in by Claude, then `import_api.ImportOBJ(path, ApiTypes.ImportExportOption())` from the Python Editor. No dialog, no prompt, returns True.
- Each `ImportOBJ` replaces the scene's object. Load one boot at a time and screenshot between loads.
- Write meshes already Y up, in mm, and leave `scale = 1.0`.
- The editor's text and console often do not repaint after a scripted replace. The code is still there; reopen the editor (Edit > Python Script) to see the console.
- A Run press can report `cannotComplete` while CLO is busy. Wait, then check before pressing again.
- Leftover Open File or Import OBJ windows from a manual try block scripts. A relaunch of CLO clears them.
- Find the editor and close buttons by element index in the window's accessibility list, not by pixel position.

## What CLO is for in this skill
Fit and collision of a boot on the avatar can be checked in the cloud kit. CLO earns its place once there are flat patterns: import the DXF, sew, drape the leather on the last or avatar, and read the strain map.

## The API can build and sew a garment with no clicks (checked 25 Nov 2026, developer.clo3d.com)
An old forum answer says the API can't sew. That's out of date. Current pattern_api has:
- `CreatePatternWithPoints([(x, y, type), ...])`: type 0 = corner (straight), 2 = spline, 3 = bezier. Lines run
  between corner points, in point order, so keep each named seam edge between two type-0 points and record its
  line index.
- `AddSeamlinePairGroup(patA, lineA, patB, lineB, dirA, dirB)` sews two lines; `AddSeamlinePairGroupPartial` sews
  sub-segments by ratio (v11); `AddSeamlineTopstitch(group, start, end, style)` adds topstitch.
- `SymmetryPatternPiece(idx, bWithSewing)`, `SetArrangement(idx, arrIdx)` with `GetArrangementList()`,
  `SetArrangementPosition`, `Simulate(steps)`, `SetSimulationQuality(q, mode)` (3 = FAST GPU),
  `AddFabric(path)` + `AssignFabricToPattern`, `ChangeFabricWithJson`, `ExportRenderingImage(path, False, 0)`,
  `ExportRenderingImageForCustomView`, `ImportZprj`, `ImportPoseW`.
- Full signature dump: boots-jackets-v2/kit/clo_api_py_signatures.txt in the project files. So the route is:
  draft patterns in the cloud, generate one CLO Python script per garment, run it in CLO's editor on the tower.

## Figure (owner rule, 25 Nov)
Render on a plain white faceless figure: a male .avt from CLO Assets/Avatar/Mannequin, or MV2.1_Luka with a flat white texture (SetAvatarTexureMap). Never the realistic avatar. build_all.py load_avatar() does this.

## Hard-won rules for scripting CLO 2026.1 (25 Nov 2026)
Sources: the open CLO MCP projects on GitHub (Lilbonner/clo3d-mcp with its clo-patterns skill, ttiimmaacc/mcp-for-clo3d
examples/workwear_jacket.py, Ubani-Studio/clo3d-mcp, marcoleder/clo3d-mcp) plus our own tower tests.
- Pattern points are mm, **Y up**, drafted **as seen from outside**, clockwise. A block drawn CB-left/CF-right is the
  body's RIGHT half: put it on the *_R arrangement points. Flipping y or guessing the side gives crumpled tubes.
- Seam directions follow the mirror principle: pieces related by rotation sew dirs equal; by a mirror (L/R halves)
  flip exactly one. Our job writer encodes this in the ratio order; check it on any new seam type.
- One-piece sleeves land rotated on arrangement points: two-piece sleeves on Arm_Front_k / Arm_Back_k place reliably.
  Body pieces: Body_*_3 points put a 64 cm body's neckline at the base of the neck (_2 puts it at the face).
- Calls that differ from the docs: ImportAvatar(path, ApiTypes.ImportExportOption()); AssignFabricToPattern(fab,
  pat, 1) (option 0 returns False); SetFabricPBRMaterialBaseColor(fab, face, r, g, b, a) floats 0-1;
  SetBackgroundColorForExportRenderingImage(r, g, b, a); AddFabric returns the index; NewProject is in utility_api;
  GetAvatarCount is in export_api; line count is nested in GetPatternInputInformation JSON.
- ExportTurntableImages(n) (one arg) works and writes output*.png to %LOCALAPPDATA%/CLO Virtual Fashion/...; copy them.
- No free 3D move: boots come in as an OBJ garment (ImportObjectType 2 + bTrace2DPatternsUVMap=True) whose UVs are
  the flat patterns in mm; one traced pattern per panel, already on the last. Type 0 = avatar (rigid: forms, soles).
- There is no undo or remove_seam via the API: save a zprj checkpoint before sewing experiments.
- Simulate in short bursts (50 steps) and render between; leather at 15 mm particle distance is fast.
- Never show a test render to the owner as a result; only stills that pass the rubric.

## Pre-flight and failure log
Before any tower batch, run `scripts/clo_preflight.py` and read `references/clo3d-preflight.md` (modal-dialog guard, the r1-r3 failure classes). Every new failure becomes a rule there in the same turn.
