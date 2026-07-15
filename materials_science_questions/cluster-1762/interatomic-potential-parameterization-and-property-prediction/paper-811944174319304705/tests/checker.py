import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os

def _interpolate_zero_crossing(rows):
    """Find temperature where Delta_F crosses zero by linear interpolation between adjacent points."""
    rows.sort(key=lambda r: float(r['Temperature_K']))
    Tvals = []
    Fvals = []
    for r in rows:
        Tvals.append(float(r['Temperature_K']))
        Fvals.append(float(r['Delta_F_eV']))
    for i in range(len(Fvals)-1):
        if Fvals[i] == 0.0:
            return Tvals[i]
        if Fvals[i]*Fvals[i+1] <= 0:
            # linear interpolation
            t1, f1 = Tvals[i], Fvals[i]
            t2, f2 = Tvals[i+1], Fvals[i+1]
            if abs(f2 - f1) < 1e-12:
                return (t1 + t2) / 2.0
            t0 = t1 - f1 * (t2 - t1) / (f2 - f1)
            return t0
    return None  # no crossing

def _is_monotonic_increasing(rows):
    rows_sorted = sorted(rows, key=lambda r: float(r['Temperature_K']))
    vals = [float(r['Delta_F_eV']) for r in rows_sorted]
    for i in range(len(vals)-1):
        if vals[i+1] + 1e-9 < vals[i]:
            return False
    return True


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
    ctx = {}
    ctx['delta_gold'] = 0.024
    ctx['delta_tol'] = 0.01
    ctx['Tc_gold'] = 300
    ctx['Tc_strict'] = 30   # full credit within this window
    ctx['Tc_decay'] = 200    # score decays linearly from strict to strict+decay
    ctx['monotonic_penalty'] = 0.5  # multiplier if not monotonic
    return ctx


# === block: score_0 (check id='step_map_e_latt') ===
def score_0(artifact, step, ctx):
    artifact = load_artifact(os.path.join('/app/outputs', 'lattice_energy_minimum_difference.json'))
    if artifact is None:
        return 0.0
    val = artifact.get('delta_E_eV_per_fu')
    if val is None:
        return 0.0
    gold = ctx['delta_gold']
    tol = ctx['delta_tol']
    if abs(val - gold) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='step_free_energy_tc') ===
def score_1(artifact, step, ctx):
    rows = load_artifact(os.path.join('/app/outputs', 'free_energy_difference.csv'))
    if rows is None or len(rows) < 10:
        return 0.0
    # Check monotonic
    monotonic = _is_monotonic_increasing(rows)
    Tc_obs = _interpolate_zero_crossing(rows)
    if Tc_obs is None:
        return 0.0  # no crossing
    Tc_gold = ctx['Tc_gold']
    Tc_strict = ctx['Tc_strict']
    Tc_decay = ctx['Tc_decay']
    derr = abs(Tc_obs - Tc_gold)
    if derr <= Tc_strict:
        Tc_score = 1.0
    else:
        Tc_score = max(0.0, 1.0 - (derr - Tc_strict) / Tc_decay)
    # Apply monotonic penalty
    if not monotonic:
        Tc_score *= ctx['monotonic_penalty']
    return Tc_score


_SCORERS = {
    'step_map_e_latt': score_0,
    'step_free_energy_tc': score_1,
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
