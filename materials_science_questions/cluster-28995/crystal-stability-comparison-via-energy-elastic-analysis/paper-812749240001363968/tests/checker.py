import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    rows = []
    ca_col = 'c/a_ratio'
    e_col = 'total_energy_per_atom_eV'
    for r in artifact:
        try:
            ca = float(r[ca_col])
            e = float(r[e_col])
            rows.append((ca, e))
        except:
            continue
    if len(rows) == 0:
        return 0.0
    # global minimum
    global_min = min(rows, key=lambda x: x[1])
    global_e = global_min[1]
    # local minimum in search range
    lo, hi = step['config']['bct_ca_search_range']
    local_rows = [(ca,e) for ca,e in rows if lo <= ca <= hi]
    if not local_rows:
        return 0.0
    local_min = min(local_rows, key=lambda x: x[1])
    ca_bct = local_min[0]
    e_bct = local_min[1]
    diff = e_bct - global_e
    # energy difference subscore
    target_diff = step['config']['energy_diff_target_eV']
    tol_diff = step['config']['energy_diff_tol_eV']
    score_diff = 1.0 if abs(diff - target_diff) <= tol_diff else max(0.0, 1.0 - abs(diff - target_diff) / (2*tol_diff))
    # c/a subscore
    target_ca = step['config']['c_a_target']
    tol_ca = step['config']['c_a_tol']
    score_ca = 1.0 if abs(ca_bct - target_ca) <= tol_ca else 0.0
    # lattice parameters subscore
    V = step['config']['volume_per_atom']
    a_calc = (2*V / ca_bct) ** (1/3)
    c_calc = ca_bct * a_calc
    target_a = step['config']['a_target_A']
    target_c = step['config']['c_target_A']
    tol_latt = step['config']['lattice_tol_A']
    score_latt = 1.0 if (abs(a_calc - target_a) <= tol_latt and abs(c_calc - target_c) <= tol_latt) else 0.0
    return 0.5*score_diff + 0.25*score_ca + 0.25*score_latt


# === block: score_1 (check id='step_2') ===
def score_1(artifact, step, ctx):
    fcc = artifact.get('fcc', {})
    bct = artifact.get('bct', {})
    score = 0.0
    bct_cp = bct.get('c_prime', None)
    fcc_cp = fcc.get('c_prime', None)
    if bct_cp is not None and bct_cp < step['config']['bct_c_prime_max']:
        score += 0.6
    if fcc_cp is not None and fcc_cp > step['config']['fcc_c_prime_min']:
        score += 0.4
    return score


# === block: score_2 (check id='step_3') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    temperatures = []
    deltas = []
    for r in artifact:
        try:
            t = float(r['temperature_K'])
            d = float(r['delta_G_eV_per_atom'])
            temperatures.append(t)
            deltas.append(d)
        except:
            continue
    if len(temperatures) < 2:
        return 0.0
    score = 0.0
    if deltas[0] > 0:
        score += 0.3
    if deltas[-1] < 0:
        score += 0.3
    # sign change probe
    cross_low, cross_high = step['config']['t_cross_low'], step['config']['t_cross_high']
    cross_ok = False
    for i in range(1, len(deltas)):
        if deltas[i-1]*deltas[i] < 0:
            # linear interpolation
            if deltas[i] != deltas[i-1]:
                t_cross = temperatures[i-1] + (temperatures[i]-temperatures[i-1]) * (-deltas[i-1]/(deltas[i]-deltas[i-1]))
            else:
                t_cross = temperatures[i-1]
            if cross_low <= t_cross <= cross_high:
                cross_ok = True
            break
        elif deltas[i] == 0 and cross_low <= temperatures[i] <= cross_high:
            cross_ok = True
            break
    if cross_ok:
        score += 0.4
    return score


_SCORERS = {
    'step_1': score_0,
    'step_2': score_1,
    'step_3': score_2,
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
