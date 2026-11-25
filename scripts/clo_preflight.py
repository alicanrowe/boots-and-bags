#!/usr/bin/env python3
"""Pre-flight for a CLO batch: run on the job folder BEFORE sending anything to the tower.
Catches the failure classes from rounds 1-3 (see references/clo3d-preflight.md) so a 35-minute tower run is not
spent finding them.  usage: python3 clo_preflight.py <jobs_dir> [<forms_dir>]   exit 1 if anything fails.

Checks
  jobs (*.json, kind != boot): every pattern has >= 3 points and a leather; every seam points at a real pattern and
    line; pieces with no seam at all (they fall to the floor) unless named *_under and dropped by the builder;
    marks lie inside their piece; tiny closed shapes that CLO cannot remesh (area < 400 mm2 or a corner < 15 deg).
  forms (pair_XX_parts/*.obj): one boundary loop, valid UV outline, no zero-area UV triangles, UVs start at 0,0.
"""
import collections, glob, json, math, os, sys

FAIL = []


def bad(*a):
    FAIL.append(" ".join(str(x) for x in a))


def poly_area(P):
    return 0.5 * sum(P[k][0] * P[(k + 1) % len(P)][1] - P[(k + 1) % len(P)][0] * P[k][1] for k in range(len(P)))


def min_corner(P):
    best = 180.0
    n = len(P)
    for k in range(n):
        a, b, c = P[k - 1], P[k], P[(k + 1) % n]
        u = (a[0] - b[0], a[1] - b[1]); v = (c[0] - b[0], c[1] - b[1])
        nu, nv = math.hypot(*u), math.hypot(*v)
        if nu < 1e-6 or nv < 1e-6:
            continue
        best = min(best, math.degrees(math.acos(max(-1, min(1, (u[0] * v[0] + u[1] * v[1]) / (nu * nv))))))
    return best


def inside(pt, P):
    x, y = pt; c = False
    for k in range(len(P)):
        (x1, y1), (x2, y2) = P[k][:2], P[k - 1][:2]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


def check_job(path):
    J = json.load(open(path))
    if J.get("kind") == "boot":
        return
    pats = J["patterns"]; name = os.path.basename(path)
    sewn = collections.Counter()
    for s in J["seams"]:
        for side in "ab":
            i = s[side]
            if not (0 <= i < len(pats)):
                bad(name, "seam points at missing pattern", i); continue
            if not (0 <= s["l" + side] < pats[i]["n_lines"]):
                bad(name, pats[i]["name"], "seam line", s["l" + side], "of", pats[i]["n_lines"])
            sewn[i] += 1
    for i, p in enumerate(pats):
        P = [q[:2] for q in p["points"]]
        if len(P) < 3:
            bad(name, p["name"], "has", len(P), "points (single-point pieces vanish)")
        if not p.get("leather"):
            bad(name, p["name"], "no leather (renders as CLO default fabric)")
        if not sewn[i] and not p["name"].rsplit("_", 1)[0].endswith("_under"):
            bad(name, p["name"], "has no seams: it will fall to the floor")
        for m in p.get("marks", []):
            mp = m["pts"]
            probe = [((mp[k][0] + mp[k + 1][0]) / 2, (mp[k][1] + mp[k + 1][1]) / 2) for k in range(len(mp) - 1)]
            if not all(inside(q, P) for q in probe[::max(1, len(probe) // 6)]):
                bad(name, p["name"], m["kind"], "mark leaves the piece")
            if m["kind"] == "pierce":
                a = abs(poly_area(m["pts"]))
                if a < 400 or min_corner(m["pts"][:-1]) < 15:
                    bad(name, p["name"], "pierce cell %.0f mm2 / corner %.0f deg: CLO cannot remesh it (modal dialog)"
                        % (a, min_corner(m["pts"][:-1])))


def check_part(path):
    T = []; F = []
    for l in open(path):
        if l.startswith("vt "):
            T.append(tuple(map(float, l.split()[1:3])))
        elif l.startswith("f "):
            F.append([tuple(int(x) - 1 for x in t.split("/")[:2]) for t in l.split()[1:]])
    E = collections.Counter(); zero = 0
    for f in F:
        for k in range(1, len(f) - 1):
            a, b, c = (T[f[j][1]] for j in (0, k, k + 1))
            if abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) < 1e-9:
                zero += 1
        for k in range(len(f)):
            E[tuple(sorted((f[k][0], f[(k + 1) % len(f)][0])))] += 1
    bd = [e for e, n in E.items() if n == 1]
    adj = collections.defaultdict(set)
    for a, b in bd:
        adj[a].add(b); adj[b].add(a)
    seen = set(); loops = 0
    for s in adj:
        if s in seen:
            continue
        loops += 1; st = [s]
        while st:
            x = st.pop()
            if x not in seen:
                seen.add(x); st += adj[x]
    nm = os.path.relpath(path)
    if any(len(v) != 2 for v in adj.values()):
        bad(nm, "boundary is pinched (a vertex on two boundary runs)")
    if zero:
        bad(nm, zero, "zero-area UV triangles")
    if loops != 1 and "wall" not in nm:
        bad(nm, loops, "boundary loops (expect 1)")
    if T and (min(u for u, _ in T) < -0.01 or min(v for _, v in T) < -0.01):
        bad(nm, "UVs do not start at 0,0")


if __name__ == "__main__":
    for p in sorted(glob.glob(os.path.join(sys.argv[1], "*.json"))):
        check_job(p)
    if len(sys.argv) > 2:
        for p in sorted(glob.glob(os.path.join(sys.argv[2], "pair_*_parts", "*.obj"))):
            check_part(p)
    print("\n".join(FAIL) if FAIL else "preflight OK")
    print(len(FAIL), "problems")
    sys.exit(1 if FAIL else 0)
