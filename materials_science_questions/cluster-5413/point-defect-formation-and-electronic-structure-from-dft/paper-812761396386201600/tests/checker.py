import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    return {'spec': spec}


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    ref = step.get('reference_values', {})
    tol_dict = step.get('tolerances', {})
    artifact_dict = {}
    for row in artifact:
        try:
            l = int(row['layer'])
            artifact_dict[l] = row
        except:
            pass
    total_fields = 0
    correct = 0
    for layer_str, expected_row in ref.items():
        layer = int(layer_str)
        row = artifact_dict.get(layer)
        if row is None:
            continue
        for field, exp_val in expected_row.items():
            total_fields += 1
            try:
                rep_val = float(row[field])
                tol = tol_dict.get(field, 0.5)
                if abs(rep_val - exp_val) <= tol:
                    correct += 1
            except:
                pass
    if total_fields == 0:
        return 0.0
    return correct / total_fields


# === block: score_1 (check id='binding_energies') ===
def score_1(artifact, step, ctx):
    ref_rows = step.get('reference_rows', [])
    tolerance = step.get('tolerance', 0.5)
    rep = {}
    for row in artifact:
        d = row['defect_type'].strip()
        try:
            l = int(row['layer'])
        except:
            continue
        s = row['species'].strip()
        try:
            val = float(row['binding_energy'])
            rep[(d, l, s)] = val
        except:
            pass
    numeric_score = 0
    for r in ref_rows:
        d, l, s, exp = r
        key = (d, l, s)
        rep_val = rep.get(key)
        if rep_val is not None and abs(rep_val - exp) <= tolerance:
            numeric_score += 1
    num_score = numeric_score / len(ref_rows) if ref_rows else 0.0

    trend_score = 0
    trend_total = 0
    for layer in [2, 3]:
        key_He = ('V', layer, 'He')
        key_H = ('V', layer, 'H')
        if key_He in rep and key_H in rep:
            trend_total += 1
            if rep[key_He] > rep[key_H]:
                trend_score += 1
        key_HeV_H = ('HeV', layer, 'H')
        key_V_H = ('V', layer, 'H')
        if key_HeV_H in rep and key_V_H in rep:
            trend_total += 1
            if rep[key_HeV_H] < rep[key_V_H]:
                trend_score += 1
    if trend_total == 0:
        tr_score = 0.0
    else:
        tr_score = trend_score / trend_total

    return 0.7 * num_score + 0.3 * tr_score


# === block: score_2 (check id='diffusion_barriers') ===
def score_2(artifact, step, ctx):
    ref = step.get('reference_values', {})
    tolerance = step.get('tolerance', 0.1)
    rep = {}
    for row in artifact:
        path = row['diffusion_path'].strip()
        try:
            val = float(row['barrier'])
            rep[path] = val
        except:
            pass
    numeric_score = 0
    for path, exp in ref.items():
        if path in rep and abs(rep[path] - exp) <= tolerance:
            numeric_score += 1
    num_score = numeric_score / len(ref) if ref else 0.0

    trend_score = 0
    if 'He_TIS_to_V' in rep and 'H_TIS_to_V' in rep:
        if rep['He_TIS_to_V'] < rep['H_TIS_to_V']:
            trend_score = 1.0

    return 0.7 * num_score + 0.3 * trend_score


# === block: score_3 (check id='desorption_barriers') ===
def score_3(artifact, step, ctx):
    ref = step.get('reference_values', {})
    tolerance = step.get('tolerance', 0.3)
    rep = {}
    for row in artifact:
        defect = row['defect'].strip()
        try:
            val = float(row['barrier_H'])
            rep[defect] = val
        except:
            pass
    numeric_score = 0
    for defect, exp in ref.items():
        if defect in rep and abs(rep[defect] - exp) <= tolerance:
            numeric_score += 1
    num_score = numeric_score / len(ref) if ref else 0.0

    trend_score = 0
    if 'HeV' in rep and 'V' in rep:
        if rep['HeV'] < rep['V']:
            trend_score = 1.0

    return 0.7 * num_score + 0.3 * trend_score


# === block: score_4 (check id='stable_site_count') ===
def score_4(artifact, step, ctx):
    ref = step.get('reference_values', {})
    rep = {}
    for row in artifact:
        defect = row['defect'].strip()
        try:
            val = int(row['num_sites'])
            rep[defect] = val
        except:
            pass
    numeric_score = 0
    for defect, exp in ref.items():
        if defect in rep and rep[defect] == exp:
            numeric_score += 1
    num_score = numeric_score / len(ref) if ref else 0.0

    trend_score = 0
    if 'HeV' in rep and 'V' in rep:
        if rep['HeV'] > rep['V']:
            trend_score = 1.0

    return 0.7 * num_score + 0.3 * trend_score


_SCORERS = {
    'formation_energies': score_0,
    'binding_energies': score_1,
    'diffusion_barriers': score_2,
    'desorption_barriers': score_3,
    'stable_site_count': score_4,
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
