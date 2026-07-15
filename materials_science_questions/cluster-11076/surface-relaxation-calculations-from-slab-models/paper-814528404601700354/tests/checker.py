import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math
import numpy as np

# ----- Lattice helpers -----
def build_fcc_positions(ncells):
    basis = np.array([[0.0,0.0,0.0], [0.5,0.5,0.0], [0.5,0.0,0.5], [0.0,0.5,0.5]])
    N = ncells**3 * 4
    pos = np.zeros((N, 3))
    idx = 0
    for ix in range(ncells):
        for iy in range(ncells):
            for iz in range(ncells):
                for b in range(4):
                    pos[idx] = np.array([ix, iy, iz]) + basis[b]
                    idx += 1
    return pos

def build_bcc_positions(ncells):
    basis = np.array([[0.0,0.0,0.0], [0.5,0.5,0.5]])
    N = ncells**3 * 2
    pos = np.zeros((N, 3))
    idx = 0
    for ix in range(ncells):
        for iy in range(ncells):
            for iz in range(ncells):
                for b in range(2):
                    pos[idx] = np.array([ix, iy, iz]) + basis[b]
                    idx += 1
    return pos

def compute_coordination(positions, d1, d2, tol=1e-4):
    N = positions.shape[0]
    min_ = positions.min(axis=0) - 0.5
    binsize = 1.0
    bin_dict = {}
    for i in range(N):
        pos = positions[i]
        ix = int((pos[0] - min_[0]) // binsize)
        iy = int((pos[1] - min_[1]) // binsize)
        iz = int((pos[2] - min_[2]) // binsize)
        bin_dict.setdefault((ix, iy, iz), []).append(i)
    d1_low = d1 * (1 - tol)
    d1_high = d1 * (1 + tol)
    d2_low = d2 * (1 - tol)
    d2_high = d2 * (1 + tol)
    Z1 = np.zeros(N, dtype=int)
    Z2 = np.zeros(N, dtype=int)
    for i in range(N):
        pos_i = positions[i]
        ix_i = int((pos_i[0] - min_[0]) // binsize)
        iy_i = int((pos_i[1] - min_[1]) // binsize)
        iz_i = int((pos_i[2] - min_[2]) // binsize)
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for dz in (-1,0,1):
                    key = (ix_i+dx, iy_i+dy, iz_i+dz)
                    for j in bin_dict.get(key, []):
                        if j == i:
                            continue
                        diff = positions[j] - pos_i
                        dist = np.sqrt(np.sum(diff**2))
                        if d1_low <= dist <= d1_high:
                            Z1[i] += 1
                        elif d2_low <= dist <= d2_high:
                            Z2[i] += 1
    return Z1, Z2

def compute_cluster_order(positions):
    dists = np.sqrt(np.sum(positions**2, axis=1))
    order = np.argsort(dists)
    return order

def compute_cumsum_surface(positions, Z1, Z2, a, Zb, order, max_N):
    effective_Z = Z1 + a * Z2
    surface = effective_Z < 10
    term = np.where(surface, np.sqrt(effective_Z / Zb) - 1.0, 0.0)
    term_sorted = term[order[:max_N]]
    cumsum = np.cumsum(term_sorted)
    return cumsum

def find_intersection(S_arr, C):
    max_N = S_arr.shape[0] - 1
    for N in range(1, max_N+1):
        if S_arr[N] <= C:
            if N == 1:
                return 1
            frac = (S_arr[N-1] - C) / (S_arr[N-1] - S_arr[N] + 1e-14)
            return round(N - 1 + frac)
    return max_N


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
    # Build reference S(N) curve and derive reference N_crit
    max_N = 20000
    # fcc
    fcc_pos = build_fcc_positions(25)  # ~62500 atoms
    order_f = compute_cluster_order(fcc_pos)
    d1_fcc = np.sqrt(0.5)   # 0.7071
    d2_fcc = 1.0
    Z1_f, Z2_f = compute_coordination(fcc_pos, d1_fcc, d2_fcc)
    a_fcc = 0.08; Zb_fcc = 12
    cumsum_f = compute_cumsum_surface(fcc_pos, Z1_f, Z2_f, a_fcc, Zb_fcc, order_f, max_N)
    # bcc
    bcc_pos = build_bcc_positions(30)  # ~54000 atoms, enough
    order_b = compute_cluster_order(bcc_pos)
    d1_bcc = np.sqrt(3)/2   # 0.866
    d2_bcc = 1.0
    Z1_b, Z2_b = compute_coordination(bcc_pos, d1_bcc, d2_bcc)
    a_bcc = 0.4; Zb_bcc = 8
    cumsum_b = compute_cumsum_surface(bcc_pos, Z1_b, Z2_b, a_bcc, Zb_bcc, order_b, max_N)
    # S(N) for N=1..max_N
    S_arr = np.zeros(max_N+1)
    for N in range(1, max_N+1):
        S_arr[N] = (cumsum_f[N-1] - cumsum_b[N-1]) / N
    # material constants C from paper Table I
    metals = ["V", "Cr", "Nb", "Mo", "Ta", "W"]
    C_dict = {
        "V": 0.0537,
        "Cr": 0.0925,
        "Nb": 0.0382,
        "Mo": 0.0558,
        "Ta": 0.0353,
        "W": 0.0432
    }
    N_crit_ref = {}
    for m in metals:
        N_crit_ref[m] = find_intersection(S_arr, C_dict[m])
    ctx = dict(S_arr=S_arr, N_crit_ref=N_crit_ref)
    return ctx


# === block: score_0 (check id='step_rhs_curve') ===
def score_0(artifact, step, ctx):
    # Read agent's CSV; each row must have N,S.
    agent_S = {}
    for row in artifact:
        try:
            N = int(row['N'])
            S = float(row['S'])
        except:
            continue
        if N <= 0 or N > 20000:
            continue
        agent_S[N] = S
    if not agent_S:
        return 0.0
    ref = ctx['S_arr']
    errors = []
    for N, S_agent in agent_S.items():
        S_ref = ref[N]
        rel_err = abs(S_agent - S_ref) / max(abs(S_ref), 1e-12)
        errors.append(rel_err)
    rmse_rel = math.sqrt(np.mean([e**2 for e in errors]))
    tol = float(step.get("tolerance", 0.001))
    if rmse_rel <= tol:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (rmse_rel - tol)/tol)
    return round(score, 6)


# === block: score_1 (check id='step_critical_sizes') ===
def score_1(artifact, step, ctx):
    ref_dict = ctx['N_crit_ref']
    if not isinstance(artifact, dict):
        return 0.0
    scores = []
    for metal in ["V", "Cr", "Nb", "Mo", "Ta", "W"]:
        val = artifact.get(metal)
        if not isinstance(val, (int, float)):
            scores.append(0.0)
            continue
        gold = ref_dict[metal]
        diff = abs(val - gold)
        thresh = max(0.05 * gold, 50)
        scores.append(1.0 if diff <= thresh else 0.0)
    return sum(scores) / len(scores)


_SCORERS = {
    'step_rhs_curve': score_0,
    'step_critical_sizes': score_1,
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
