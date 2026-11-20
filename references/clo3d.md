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

## What CLO is for in this skill
Fit and collision of a boot on the avatar can be checked in the cloud kit. CLO earns its place once there are flat patterns: import the DXF, sew, drape the leather on the last or avatar, and read the strain map.
