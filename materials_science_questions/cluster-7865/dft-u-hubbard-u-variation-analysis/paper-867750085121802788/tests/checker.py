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


# === block: score_0 (check id='step_extract_coefficients') ===
def score_0(artifact, step, ctx):
    artifact_json = artifact
    expected = step["expected"]
    M_expected = expected["M"]
    intra_expected = expected["intra_site_coefficients"]
    tol_M = float(expected.get("tolerance_abs_M", 5.0))
    tol_intra = float(expected.get("tolerance_abs_intra", 5.0))
    scores = []
    for key in M_expected:
        if key not in artifact_json.get("M", {}):
            scores.append(0.0)
        else:
            val = float(artifact_json["M"][key])
            ref = float(M_expected[key])
            diff = abs(val - ref)
            s = max(0.0, 1.0 - diff / tol_M) if tol_M > 0 else (1.0 if diff == 0 else 0.0)
            scores.append(s)
    for key in intra_expected:
        if key not in artifact_json.get("intra_site_coefficients", {}):
            scores.extend([0.0]*3)
        else:
            vals = artifact_json["intra_site_coefficients"][key]
            refs = intra_expected[key]
            if not isinstance(vals, list) or len(vals) != 3:
                scores.extend([0.0]*3)
            else:
                for i in range(3):
                    diff = abs(float(vals[i]) - float(refs[i]))
                    s = max(0.0, 1.0 - diff / tol_intra) if tol_intra > 0 else (1.0 if diff == 0 else 0.0)
                    scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_total_polarization') ===
def score_1(artifact, step, ctx):
    artifact_csv = artifact
    expected = step["expected"]
    states_expected = expected["states"]
    tol_comp = float(expected.get("tolerance_abs_component", 10.0))
    direction_weight = float(expected.get("direction_weight", 0.2))
    rows = {}
    for row in artifact_csv:
        q = row.get("q_vec", "").strip()
        rows[q] = row
    comp_scores = []
    direction_scores = []
    for state_key, state_exp in states_expected.items():
        if state_key not in rows:
            comp_scores.append(0.0)
            direction_scores.append(0.0)
            continue
        row = rows[state_key]
        try:
            Px = float(row.get("Px", 0))
            Py = float(row.get("Py", 0))
            Pz = float(row.get("Pz", 0))
        except:
            comp_scores.append(0.0)
            direction_scores.append(0.0)
            continue
        exp_Px = float(state_exp["Px"])
        exp_Py = float(state_exp["Py"])
        exp_Pz = float(state_exp["Pz"])
        diff_x = abs(Px - exp_Px)
        diff_y = abs(Py - exp_Py)
        diff_z = abs(Pz - exp_Pz)
        sc_x = max(0.0, 1.0 - diff_x / tol_comp) if tol_comp > 0 else (1.0 if diff_x == 0 else 0.0)
        sc_y = max(0.0, 1.0 - diff_y / tol_comp) if tol_comp > 0 else (1.0 if diff_y == 0 else 0.0)
        sc_z = max(0.0, 1.0 - diff_z / tol_comp) if tol_comp > 0 else (1.0 if diff_z == 0 else 0.0)
        comp_scores.append((sc_x + sc_y + sc_z) / 3.0)
        if state_exp.get("dominant_axis") == "x":
            if Px <= 0:
                dir_sc = 0.0
            else:
                ratio_y = abs(Py) / (abs(Px) + 1e-9)
                ratio_z = abs(Pz) / (abs(Px) + 1e-9)
                dir_sc = max(0.0, 1.0 - max(ratio_y, ratio_z))
        else:
            if Px <= 0 or Py <= 0:
                dir_sc = 0.0
            else:
                mag = math.sqrt(Px**2 + Py**2 + Pz**2)
                if mag == 0:
                    dir_sc = 0.0
                else:
                    dot = (Px + Py) / math.sqrt(2) / mag
                    dir_sc = max(0.0, min(1.0, dot))
        direction_scores.append(dir_sc)
    avg_comp = sum(comp_scores) / len(comp_scores) if comp_scores else 0.0
    avg_dir = sum(direction_scores) / len(direction_scores) if direction_scores else 0.0
    score = (1 - direction_weight) * avg_comp + direction_weight * avg_dir
    return score


_SCORERS = {
    'step_extract_coefficients': score_0,
    'step_total_polarization': score_1,
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
