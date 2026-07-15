import os
import json
import csv

# === author imports / helpers ===
import math
from collections import Counter

def count_zero_crossings(data, ctx):
    clamped_cell = ctx['clamped_cell_idx']
    num_cells_window = ctx['N_cells_W_half']
    window_start = max(0, clamped_cell - num_cells_window + 1)
    window_end = clamped_cell
    # Build m -> list of (n, deltaZ) inside window
    m_to_dz = {}
    for row in data:
        m = int(row['m'])
        n = int(row['n'])
        if window_start <= n <= window_end:
            dz = float(row['deltaZ'])
            m_to_dz.setdefault(m, []).append((n, dz))
    # For each m, sort by n and count zero-crossings
    counts = []
    for m, entries in m_to_dz.items():
        entries.sort(key=lambda x: x[0])
        dz_vals = [e[1] for e in entries]
        crossings = 0
        prev_sign = None
        for dz in dz_vals:
            sign = 1 if dz > 1e-9 else (-1 if dz < -1e-9 else 0)
            if sign != 0:
                if prev_sign is not None and sign != prev_sign:
                    crossings += 1
                prev_sign = sign
        counts.append(crossings)
    if not counts:
        return None
    counter = Counter(counts)
    return counter.most_common(1)[0][0]


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
    rho0 = 0.1418  # nm
    import math
    M = 104
    N = 700
    eps_xx = -0.08
    eps_yy = 0.10
    a0 = math.sqrt(3) * rho0
    b0 = 3 * rho0
    a = a0 * (1 + eps_xx)
    b = b0 * (1 + eps_yy)
    W = a * M
    N_cells_W_half = max(1, int((W / 2) / b))
    clamped_cell_idx = N - 1  # last cell index
    return {
        'M': M,
        'N': N,
        'clamped_cell_idx': clamped_cell_idx,
        'N_cells_W_half': N_cells_W_half
    }


# === block: score_0 (check id='results_json') ===
def score_0(artifact, step, ctx):
    systems = artifact.get('systems', [])
    if not systems:
        return 0.0
    by_cond = {}
    for s in systems:
        cond = str(s.get('initial_condition', '')).lower().replace(' ', '')
        by_cond[cond] = s
    exp_cond_12 = 'lambda1_to_lambda1_2'
    exp_cond_13 = 'lambda1_to_lambda1_3'
    s12 = by_cond.get(exp_cond_12)
    s13 = by_cond.get(exp_cond_13)
    if s12 is None or s13 is None:
        return 0.0

    # Energy check
    ref12 = 0.82391
    ref13 = 0.82552
    tol_rel = 0.01
    ok12e = abs(s12['energy_E'] - ref12) / ref12 <= tol_rel
    ok13e = abs(s13['energy_E'] - ref13) / ref13 <= tol_rel
    order_ok = s12['energy_E'] < s13['energy_E']
    e_score = (ok12e + ok13e + order_ok) / 3.0

    # Zero-crossing counts
    z12 = s12['num_zero_crossings_within_W']
    z13 = s13['num_zero_crossings_within_W']
    z_ok12 = int(z12) == 5
    z_ok13 = int(z13) == 1
    z_score = (z_ok12 + z_ok13) / 2.0

    # max_deltaZ
    lo, hi = 1.3, 1.5
    in_range = lambda x: lo <= x <= hi
    dz12 = s12['max_deltaZ']
    dz13 = s13['max_deltaZ']
    d_score = (in_range(dz12) + in_range(dz13)) / 2.0

    w_e, w_z, w_d = 0.5, 0.3, 0.2
    return w_e * e_score + w_z * z_score + w_d * d_score


# === block: score_1 (check id='deltaz_l12') ===
def score_1(artifact, step, ctx):
    target = 5
    crossings = count_zero_crossings(artifact, ctx)
    if crossings is None:
        return 0.0
    return 1.0 if crossings == target else 0.0


# === block: score_2 (check id='deltaz_l13') ===
def score_2(artifact, step, ctx):
    target = 1
    crossings = count_zero_crossings(artifact, ctx)
    if crossings is None:
        return 0.0
    return 1.0 if crossings == target else 0.0


_SCORERS = {
    'results_json': score_0,
    'deltaz_l12': score_1,
    'deltaz_l13': score_2,
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
