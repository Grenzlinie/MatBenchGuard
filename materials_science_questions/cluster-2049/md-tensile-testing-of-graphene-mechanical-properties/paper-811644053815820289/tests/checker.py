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


# === block: score_0 (check id='mech') ===
def score_0(artifact, step, ctx):
    rows = artifact
    Y0 = None
    for r in rows:
        dt = r.get('defect_type','').strip().lower()
        conc = float(r.get('concentration', -1))
        if dt == 'pristine' and conc == 0:
            Y0 = float(r.get('Youngs_modulus_TPa', 0))
            break
    if Y0 is None or Y0 <= 0:
        return 0.0
    refs = step.get('reference_ratios', {})
    tol_ratio = step.get('tolerance_ratio', 0.05)
    points = []
    for r in rows:
        dt = r.get('defect_type','').strip().lower()
        conc = float(r.get('concentration', -1))
        y_agent = float(r.get('Youngs_modulus_TPa', 0))
        if dt == 'pristine' and conc == 0:
            points.append(1.0)
            continue
        # Only score monatomic vacancies; Stone-Wales scoring is dropped per paper review
        if dt != 'vacancy':
            continue
        ref = refs.get('vacancy')
        if ref is None:
            continue
        try:
            expected_ratio = eval(ref['formula'], {'c': conc})
        except:
            continue
        agent_ratio = y_agent / Y0
        err = abs(agent_ratio - expected_ratio)
        if err <= tol_ratio:
            pts = 1.0
        else:
            pts = max(0.0, 1.0 - (err - tol_ratio) / tol_ratio)
        points.append(pts)
    if not points:
        return 0.0
    return sum(points) / len(points)


# === block: score_1 (check id='thermal300') ===
def score_1(artifact, step, ctx):
    rows = artifact
    kappa0 = None
    for r in rows:
        dt = r.get('defect_type','').strip().lower()
        conc = float(r.get('concentration', -1))
        if dt == 'pristine' and conc == 0:
            kappa0 = float(r.get('thermal_conductivity_WmK', 0))
            break
    if kappa0 is None or kappa0 <= 0:
        return 0.0
    refs = step.get('reference_ratios', {})
    tol_ratio = step.get('tolerance_ratio', 0.15)
    points = []
    for r in rows:
        dt = r.get('defect_type','').strip().lower()
        conc = float(r.get('concentration', -1))
        k_agent = float(r.get('thermal_conductivity_WmK', 0))
        if dt == 'pristine' and conc == 0:
            points.append(1.0)
            continue
        ref = refs.get(dt)
        if ref is None:
            continue
        try:
            expected_ratio = eval(ref['formula'], {'c': conc})
        except:
            continue
        agent_ratio = k_agent / kappa0
        err = abs(agent_ratio - expected_ratio)
        if err <= tol_ratio:
            pts = 1.0
        else:
            pts = max(0.0, 1.0 - (err - tol_ratio) / tol_ratio)
        points.append(pts)
    if not points:
        return 0.0
    return sum(points) / len(points)


# === block: score_2 (check id='thermal_t') ===
def score_2(artifact, step, ctx):
    rows = artifact
    peak_range = step['rules']['peak_temperature_range']  # [150,300]
    defect_conc = step['rules']['defect_concentration']  # 0.02
    pristine = []
    defected = []
    for r in rows:
        dt = r.get('defect_type','').strip().lower()
        conc = float(r.get('concentration', -1))
        temp = float(r.get('temperature_K', 0))
        kappa = float(r.get('thermal_conductivity_WmK', 0))
        if dt == 'pristine' and conc == 0:
            pristine.append((temp, kappa))
        elif dt == 'vacancy' and abs(conc - defect_conc) < 1e-6:
            defected.append((temp, kappa))
    if not pristine or not defected:
        return 0.0
    defected_sorted = sorted(defected, key=lambda x: x[0])
    max_idx = max(range(len(defected_sorted)), key=lambda i: defected_sorted[i][1])
    peak_temp = defected_sorted[max_idx][0]
    peak_ok = 1.0 if peak_range[0] <= peak_temp <= peak_range[1] else 0.0
    pristine_dict = dict(pristine)
    ordering_ok = 0
    for t, k_d in defected_sorted:
        k_p = pristine_dict.get(t)
        if k_p is not None and k_d < k_p:
            ordering_ok += 1
    ordering_score = ordering_ok / len(defected_sorted) if defected_sorted else 0.0
    return 0.5 * peak_ok + 0.5 * ordering_score


_SCORERS = {
    'mech': score_0,
    'thermal300': score_1,
    'thermal_t': score_2,
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
