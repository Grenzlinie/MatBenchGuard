import os
import json
import csv


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


# === block: score_0 (check id='pure_cof_enthalpy') ===
def score_0(artifact, step, ctx):
    # Extract pure COF enthalpy and find angle with minimum enthalpy
    # artifact is a list of dicts with 'incline_angle' and 'enthalpy' columns
    if not artifact or len(artifact) < 4:
        return 0.0
    angles = {}
    for row in artifact:
        try:
            a = int(row['incline_angle'])
            e = float(row['enthalpy'])
            angles[a] = e
        except (ValueError, KeyError):
            return 0.0
    required = set(step.get('angles', [70,80,85,90]))
    if set(angles.keys()) != required:
        return 0.0
    min_angle = min(angles, key=angles.get)
    exp = step['expected_min_angle']
    tol = step.get('tolerance_angle', 0)
    return 1.0 if abs(min_angle - exp) <= tol else 0.0


# === block: score_1 (check id='thf_enthalpy') ===
def score_1(artifact, step, ctx):
    # Find angle with minimum enthalpy at max loading
    if not artifact:
        return 0.0
    loadings = {}
    for row in artifact:
        try:
            a = int(row['incline_angle'])
            n = int(row['n_THF'])
            e = float(row['enthalpy'])
        except (ValueError, KeyError):
            return 0.0
        loadings.setdefault(n, {})[a] = e
    max_n = step['max_loading']
    if max_n not in loadings:
        return 0.0
    min_angle = min(loadings[max_n], key=loadings[max_n].get)
    exp = step['expected_min_angle_max_loading']
    return 1.0 if min_angle == exp else 0.0


# === block: score_2 (check id='thf_interaction') ===
def score_2(artifact, step, ctx):
    # Verify interaction energy at max loading is stronger (more negative) at the check angle
    if not artifact:
        return 0.0
    max_n = step['max_loading']
    vals = {}
    for row in artifact:
        try:
            a = int(row['incline_angle'])
            n = int(row['n_THF'])
            ie = float(row['interaction_energy'])
        except (ValueError, KeyError):
            return 0.0
        if n == max_n:
            vals[a] = ie
    c1 = step['check_angle_stronger']
    c2 = step['compare_angle']
    if c1 not in vals or c2 not in vals:
        return 0.0
    return 1.0 if vals[c1] < vals[c2] else 0.0


# === block: score_3 (check id='h2o_enthalpy') ===
def score_3(artifact, step, ctx):
    # Check enthalpy minimum shifts with loading
    if not artifact:
        return 0.0
    load_map = {}
    for row in artifact:
        try:
            a = int(row['incline_angle'])
            n = int(row['n_H2O'])
            e = float(row['enthalpy'])
        except (ValueError, KeyError):
            return 0.0
        load_map.setdefault(n, {})[a] = e
    expected = step['loading_min_angle_map']  # {"628":70, "780":80, "917":85}
    cnt = 0
    score = 0.0
    for n_str, exp_angle in expected.items():
        n = int(n_str)
        if n not in load_map:
            continue
        ang = min(load_map[n], key=load_map[n].get)
        if ang == exp_angle:
            score += 1.0
        cnt += 1
    if cnt == 0:
        return 0.0
    return score / cnt


# === block: score_4 (check id='h2o_rdf_peak') ===
def score_4(artifact, step, ctx):
    # Evaluate O-O RDF peak thresholds for ordered/disordered water
    if not artifact:
        return 0.0
    lookup = {}
    for row in artifact:
        try:
            n = int(row['n_H2O'])
            a = int(row['incline_angle'])
            pos = float(row['first_peak_position'])
            hgt = float(row['first_peak_height'])
        except (ValueError, KeyError):
            continue
        lookup[(n, a)] = (pos, hgt)
    conditions = step.get('conditions', [])
    if not conditions:
        return 0.0
    score = 0.0
    total = 0
    for cond in conditions:
        key = (cond['n'], cond['a'])
        if key not in lookup:
            continue
        total += 1
        pos, hgt = lookup[key]
        if 'pos_max' in cond and 'hgt_min' in cond:
            if pos <= cond['pos_max'] and hgt >= cond['hgt_min']:
                score += 1.0
        elif 'pos_min' in cond and 'hgt_max' in cond:
            if pos >= cond['pos_min'] and hgt <= cond['hgt_max']:
                score += 1.0
    if total == 0:
        return 0.0
    return score / total


_SCORERS = {
    'pure_cof_enthalpy': score_0,
    'thf_enthalpy': score_1,
    'thf_interaction': score_2,
    'h2o_enthalpy': score_3,
    'h2o_rdf_peak': score_4,
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
