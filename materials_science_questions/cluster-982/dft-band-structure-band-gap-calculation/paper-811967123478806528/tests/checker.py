import os
import json
import csv

# === author imports / helpers ===
import csv, os, json


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
    return spec


# === block: score_0 (check id='band_gaps_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    systems = {row['system'].strip(): row for row in rows}
    required = ['La','Y','Sc']
    if not all(s in systems for s in required):
        return 0.0
    targets = step['target_values']
    tol_energy = step.get('energy_tolerance', 0.1)
    tol_optical = step.get('optical_tolerance', 0.1)
    value_score = 0.0
    for s in required:
        rep = systems[s]
        try:
            v_eg = float(rep['energy_band_gap_eV'])
            v_og = float(rep['optical_band_gap_eV'])
        except (ValueError, KeyError):
            return 0.0
        t_eg = targets[s]['energy_band_gap_eV']
        t_og = targets[s]['optical_band_gap_eV']
        eg_score = max(0.0, 1.0 - abs(v_eg - t_eg) / tol_energy)
        og_score = max(0.0, 1.0 - abs(v_og - t_og) / tol_optical)
        value_score += eg_score + og_score
    value_score /= 6.0
    # trend check: increasing order La < Y < Sc
    trend_ok = True
    eg_vals = []
    og_vals = []
    for s in ['La','Y','Sc']:
        eg_vals.append(float(systems[s]['energy_band_gap_eV']))
        og_vals.append(float(systems[s]['optical_band_gap_eV']))
    if not (eg_vals[0] < eg_vals[1] < eg_vals[2]):
        trend_ok = False
    if not (og_vals[0] < og_vals[1] < og_vals[2]):
        trend_ok = False
    trend_score = 1.0 if trend_ok else 0.0
    final = 0.6 * value_score + 0.4 * trend_score
    return final


# === block: score_1 (check id='bond_angles_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    systems = {row['system'].strip(): row for row in rows}
    required = ['La','Y','Sc']
    if not all(s in systems for s in required):
        return 0.0
    targets = step['target_values']
    tol = step.get('tolerance', 1.0)
    value_score = 0.0
    for s in required:
        try:
            v = float(systems[s]['Ti_O_Ti_angle_deg'])
        except (ValueError, KeyError):
            return 0.0
        t = targets[s]
        score = max(0.0, 1.0 - abs(v - t) / tol)
        value_score += score
    value_score /= 3.0
    # trend check: decreasing La > Y > Sc
    angle_vals = []
    for s in ['La','Y','Sc']:
        angle_vals.append(float(systems[s]['Ti_O_Ti_angle_deg']))
    trend_ok = (angle_vals[0] > angle_vals[1] > angle_vals[2])
    trend_score = 1.0 if trend_ok else 0.0
    final = 0.6 * value_score + 0.4 * trend_score
    return final


# === block: score_2 (check id='formation_energies_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    systems = {row['system'].strip(): row for row in rows}
    required = ['La','Y','Sc']
    if not all(s in systems for s in required):
        return 0.0
    targets = step['target_values']
    tol = step.get('tolerance', 0.05)
    value_score = 0.0
    for s in required:
        try:
            v = float(systems[s]['O_vacancy_formation_energy_eV'])
        except (ValueError, KeyError):
            return 0.0
        t = targets[s]
        score = max(0.0, 1.0 - abs(v - t) / tol)
        value_score += score
    value_score /= 3.0
    return value_score


_SCORERS = {
    'band_gaps_check': score_0,
    'bond_angles_check': score_1,
    'formation_energies_check': score_2,
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
