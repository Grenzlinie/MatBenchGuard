import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
from collections import defaultdict

# Parameters (same as paper)
alpha1, beta1, gamma1, delta1 = 1.0, 0.2, 0.15, 0.1
alpha2, beta2 = 1.2, 1.1
alpha3, beta3 = 0.6, 0.5
alpha4, beta4 = 0.4, 0.05
alpha, beta, gamma = 0.15, 0.02, 0.11
a, b, c = 0.09, 0.01, 0.06
p, q = 0.03, 0.01

# Force-constant matrices (the paper gives minus these matrices)
phi12 = -np.array([[alpha1, 0, 0], [0, beta1, delta1], [0, delta1, gamma1]])
phi13 = -np.array([[alpha2, beta2, beta2], [beta2, alpha2, beta2], [beta2, beta2, alpha2]])
phi14_tt = -np.array([[alpha3, beta3, beta3], [beta3, alpha3, beta3], [beta3, beta3, alpha3]])
phi34_tt = -np.array([[alpha4, 0, 0], [0, beta4, 0], [0, 0, beta4]])
phi44 = -np.array([
    [alpha, gamma, 0, 0, 0, p],
    [gamma, alpha, 0, 0, 0, p],
    [0, 0, beta, q, q, 0],
    [0, 0, q, a, c, 0],
    [0, 0, q, c, a, 0],
    [p, p, 0, 0, 0, b]
])

# Primitive cell geometry (FCC, a=1)
a1 = np.array([0.0, 1.0, 1.0]) / 2
a2 = np.array([1.0, 0.0, 1.0]) / 2
a3 = np.array([1.0, 1.0, 0.0]) / 2
basis = np.column_stack([a1, a2, a3])
inv_basis = np.linalg.inv(basis)
# Reciprocal basis: columns are b1, b2, b3 with b_i·a_j = 2π δ_ij
recip_basis = 2.0 * np.pi * inv_basis.T

# positions (fractional = cartesian for a=1)
pos = [
    np.array([0.25, 0.25, 0.25]),   # ion1 (A tetra1)
    np.array([0.75, 0.75, 0.75]),   # ion2 (A tetra2)
    np.array([0.5,  0.5,  0.5]),     # ion3 (A octa)
    np.array([0.0,  0.0,  0.0])      # C60
]

def generate_cubic_rotations():
    """48 cubic rotations (proper + improper)."""
    rots = []
    signs = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],
             [-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
    perms = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    for s in signs:
        for perm in perms:
            mat = np.zeros((3,3))
            for i,pi in enumerate(perm):
                mat[i,pi] = s[i]
            if np.linalg.det(mat) != 0:
                rots.append(mat.copy())
    return rots

cubic_rots = generate_cubic_rotations()

def reduce_vector(v):
    """Minimum image vector in primitive cell."""
    f = inv_basis @ v
    f_red = f - np.round(f)
    return basis @ f_red

def round_vec(v, decimals=6):
    return tuple(np.round(v, decimals))

block_dict = {}  # (a_type, b_type, r_min_rounded) -> block

def add_block(a,b,v_vec,block):
    v_r = reduce_vector(v_vec)
    key = (a,b,round_vec(v_r))
    block_dict[key] = block

# reference pairs (paper's explicit pairs)
ref_pairs = [
    {"a":0,"b":1,"v0":np.array([0.5,0.0,0.0]),
     "block":phi12,"type":"33"},
    {"a":0,"b":2,"v0":np.array([0.25,0.25,0.25]),
     "block":phi13,"type":"33"},
    {"a":0,"b":3,"v0":np.array([-0.25,-0.25,-0.25]),
     "block":np.hstack([phi14_tt, np.zeros((3,3))]),"type":"36"},
    {"a":2,"b":3,"v0":np.array([0.5,0.0,0.0]),
     "block":np.hstack([phi34_tt, np.zeros((3,3))]),"type":"36"},
    {"a":3,"b":3,"v0":np.array([0.5,0.5,0.0]),
     "block":phi44,"type":"66"}
]

for ref in ref_pairs:
    a = ref["a"]; b = ref["b"]; v0 = ref["v0"]
    block0 = ref["block"]; btype = ref["type"]
    for rot in cubic_rots:
        det = np.linalg.det(rot)
        v_rot = rot @ v0
        # transformed block
        if btype == "33":
            block_rot = rot @ block0 @ rot.T
        elif btype == "36":
            block_rot = np.hstack([rot @ block0[:,:3] @ rot.T, np.zeros((3,3))])
        elif btype == "66":
            P = np.zeros((6,6))
            P[:3,:3] = rot
            P[3:,3:] = det * rot
            block_rot = P @ block0 @ P.T
        else:
            block_rot = block0
        add_block(a,b,v_rot,block_rot)
        # opposite direction (b,a) using transpose
        if btype == "33":
            add_block(b,a,-v_rot,block_rot.T)
        elif btype == "36":
            add_block(b,a,-v_rot,block_rot.T)   # 3x6 -> 6x3
        elif btype == "66":
            add_block(b,a,-v_rot,block_rot.T)

# ---------- acoustic sum rule for translations ----------
# Compute on-site tt-blocks from off-diagonal sums.
on_site_tt = [np.zeros((3,3)) for _ in range(4)]
for (a,b,_), block in block_dict.items():
    if a == b:
        continue  # avoid spurious diagonal entry if any
    # extract tt part
    if block.shape[0] >= 3 and block.shape[1] >= 3:
        tt_part = block[:3,:3]
    else:
        continue  # no tt part
    on_site_tt[a] += tt_part
# on-site = - sum of off-diagonal tt contributions
for a in range(4):
    on_site_tt[a] = -on_site_tt[a]
# -------------------------------------------------------

def compute_dyn_matrix(q):
    D0 = np.zeros((15,15), dtype=complex)
    rng = [-1,0,1]
    for n1 in rng:
        for n2 in rng:
            for n3 in rng:
                n = np.array([n1,n2,n3])
                R = basis @ n
                for a in range(4):
                    for b in range(4):
                        r = pos[b] + R - pos[a]
                        r_min = reduce_vector(r)
                        key = (a,b,round_vec(r_min))
                        block = block_dict.get(key)
                        if block is None:
                            continue
                        phase = np.exp(1j * np.dot(q, r))
                        # DOF indices
                        if a < 3:
                            idx_a = a*3
                            sz_a = 3
                        else:
                            idx_a = 9
                            sz_a = 6
                        if b < 3:
                            idx_b = b*3
                            sz_b = 3
                        else:
                            idx_b = 9
                            sz_b = 6
                        if block.shape != (sz_a, sz_b):
                            continue
                        D0[idx_a:idx_a+sz_a, idx_b:idx_b+sz_b] += block * phase
    # add on-site tt blocks
    for a in range(4):
        if a < 3:
            D0[3*a:3*a+3, 3*a:3*a+3] += on_site_tt[a]
        else:
            D0[9:12, 9:12] += on_site_tt[a]
    D0 = (D0 + D0.T.conj()) / 2
    return D0

def compute_expected():
    q_vals = np.arange(0, 1.001, 0.05)
    expected = []
    # Cartesian wavevector from reduced coordinates using reciprocal basis
    for dname, qfunc in [("Delta", lambda x: recip_basis @ np.array([x,0,0])),
                          ("Sigma", lambda x: recip_basis @ np.array([x,x,0])),
                          ("Lambda",lambda x: recip_basis @ np.array([x,x,x]))]:
        for x in q_vals:
            D0 = compute_dyn_matrix(qfunc(x))
            eigvals = np.linalg.eigvalsh(D0)
            freqs = np.sqrt(np.maximum(eigvals, 0.0))
            sorted_freqs = np.sort(freqs)
            for b in range(15):
                expected.append((dname, float(x), b, float(sorted_freqs[b])))
    return expected


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    expected = compute_expected()
    return {"expected": expected}


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    if len(artifact) != 945:
        return 0.0

    expected = ctx["expected"]
    # group agent rows by (direction, q_red, branch)
    from collections import defaultdict
    agt_by_dir_q = defaultdict(lambda: defaultdict(dict))
    for row in artifact:
        d = row["direction"]
        qr = float(row["q_red"])
        br = int(row["branch"])
        fr = float(row["frequency"])
        agt_by_dir_q[d][qr][br] = fr

    matches = 0
    total = 0
    for (d, qr, br, ef) in expected:
        total += 1
        try:
            af = agt_by_dir_q[d][qr][br]
        except KeyError:
            continue
        if abs(af - ef) <= 1e-6:
            matches += 1
    score = matches / total if total > 0 else 0.0
    return score


_SCORERS = {
    'step_1': score_0,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
