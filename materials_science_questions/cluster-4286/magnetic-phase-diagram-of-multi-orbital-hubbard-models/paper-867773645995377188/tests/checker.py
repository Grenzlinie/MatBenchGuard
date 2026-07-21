import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.linalg import eigh
from itertools import combinations

def _basis_states(L, N, sz_spin2):
    N_up = (N + sz_spin2) // 2
    N_down = (N - sz_spin2) // 2
    up_combs = list(combinations(range(L), N_up))
    down_combs = list(combinations(range(L), N_down))
    up_masks = [sum(1<<i for i in c) for c in up_combs]
    down_masks = [sum(1<<i for i in c) for c in down_combs]
    masks = [(um, dm) for um in up_masks for dm in down_masks]
    state_to_idx = {m: idx for idx, m in enumerate(masks)}
    return masks, state_to_idx

def _build_H(L, BC, U, N, sz_spin2):
    masks, s2i = _basis_states(L, N, sz_spin2)
    dim = len(masks)
    is_complex = (BC == 'TBC' and L % 2 == 1)
    dtype = np.complex128 if is_complex else np.float64
    H = np.zeros((dim, dim), dtype=dtype)
    for idx, (um, dm) in enumerate(masks):
        double = bin(um & dm).count('1')
        H[idx, idx] += U * double
    t0 = 1.0
    edges = []
    if BC == 'OBC':
        for i in range(L-1):
            edges.append((i, i+1, t0))
    else:
        tau = t0 * np.exp(1j * np.pi * L / 2)
        for i in range(L-1):
            edges.append((i, i+1, t0))
        edges.append((0, L-1, tau))
    for (i, j, kappa) in edges:
        for (a, b, coeff) in [(j, i, kappa), (i, j, np.conj(kappa))]:
            for spin in [0, 1]:
                for idx, (um, dm) in enumerate(masks):
                    mask = um if spin == 0 else dm
                    if not (mask & (1 << b)): continue
                    if mask & (1 << a): continue
                    if a < b:
                        between = (mask >> (a+1)) & ((1 << (b-a-1)) - 1)
                    else:
                        between = (mask >> (b+1)) & ((1 << (a-b-1)) - 1)
                    sign = 1 if bin(between).count('1') % 2 == 0 else -1
                    new_mask = (mask ^ (1 << b)) | (1 << a)
                    if spin == 0:
                        target = s2i.get((new_mask, dm))
                    else:
                        target = s2i.get((um, new_mask))
                    if target is not None:
                        H[target, idx] += -coeff * sign
    return H

def _ground_energy(L, BC, U):
    H = _build_H(L, BC, U, L, sz_spin2=1)
    ev = eigh(H, eigvals_only=True)[0]
    return ev

def _min_energy_N(L, BC, U, N):
    min_val = None
    for N_up in range(0, min(N, L) + 1):
        N_down = N - N_up
        if N_down < 0 or N_down > L: continue
        sz = N_up - N_down
        H = _build_H(L, BC, U, N, sz)
        ev = eigh(H, eigvals_only=True)[0]
        if min_val is None or ev < min_val:
            min_val = ev
    return min_val

def _gap(L, BC, U):
    E0 = _ground_energy(L, BC, U)
    E1 = _min_energy_N(L, BC, U, L-1)
    return E1 - E0

def _magnetization_L3_OBC(U):
    L=3; BC='OBC'
    H = _build_H(L, BC, U, 3, sz_spin2=1)
    evals, evecs = eigh(H)
    v0 = evecs[:, 0]
    masks, _ = _basis_states(L, 3, 1)
    mag = np.zeros(L)
    for idx, (um, dm) in enumerate(masks):
        prob = abs(v0[idx])**2
        for site in range(L):
            up_occ = (um >> site) & 1
            down_occ = (dm >> site) & 1
            mag[site] += prob * (up_occ - down_occ)
    return mag


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
    return {}


# === block: score_0 (check id='ground_state_energy') ===
def score_0(artifact, step, ctx):
    import math
    rows = artifact
    tol = 1e-5
    combos = step["required_combinations"]
    scores = []
    for combo in combos:
        L, bc, U = combo
        row = None
        for r in rows:
            if int(r['L']) == L and str(r['BC']) == bc and abs(float(r['U']) - U) < 1e-9:
                row = r
                break
        if row is None:
            scores.append(0.0)
            continue
        reported = float(row['E_per_site'])
        expected = _ground_energy(L, bc, U) / L
        if expected == 0:
            err = abs(reported)
        else:
            err = abs(reported - expected) / abs(expected)
        score = 1.0 if err <= tol else max(0.0, 1.0 - err/(10*tol))
        scores.append(score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='energy_gap') ===
def score_1(artifact, step, ctx):
    import math
    rows = artifact
    tol = 1e-5
    combos = step["required_combinations"]
    scores = []
    for combo in combos:
        L, bc, U = combo
        row = None
        for r in rows:
            if int(r['L']) == L and str(r['BC']) == bc and abs(float(r['U']) - U) < 1e-9:
                row = r
                break
        if row is None:
            scores.append(0.0)
            continue
        reported = float(row['gap'])
        expected = _gap(L, bc, U)
        err = abs(reported - expected)
        score = 1.0 if err <= tol else max(0.0, 1.0 - err/(100*tol))
        scores.append(score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='magnetization') ===
def score_2(artifact, step, ctx):
    import math
    rows = artifact
    tol = 1e-5
    U_vals = step.get("U_vals", [])
    scores = []
    for U in U_vals:
        site_rows = [r for r in rows if abs(float(r['U'])-U) < 1e-9]
        if not site_rows:
            scores.extend([0.0]*3)
            continue
        mag_expected = _magnetization_L3_OBC(U)
        site_data = {int(r['site']): float(r['magnetization']) for r in site_rows}
        for site in [1,2,3]:
            if site not in site_data:
                scores.append(0.0)
                continue
            reported = site_data[site]
            expected = mag_expected[site-1]
            err = abs(reported - expected)
            score = 1.0 if err <= tol else max(0.0, 1.0 - err/(10*tol))
            scores.append(score)
    return sum(scores)/len(scores) if scores else 0.0


_SCORERS = {
    'ground_state_energy': score_0,
    'energy_gap': score_1,
    'magnetization': score_2,
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
