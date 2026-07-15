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


# === block: score_0 (check id='step_melting_confirmation') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact  # list of dicts from CSV
        def get_row(temp):
            for r in rows:
                if abs(float(r['temperature']) - temp) < 0.1:
                    return r
            return None
        r1100 = get_row(1100.0)
        r1000 = get_row(1000.0)
        if r1100 is None or r1000 is None:
            return 0.0
        S_1100 = float(r1100['S_centre'])
        E_1100 = float(r1100['energy_per_atom'])
        E_1000 = float(r1000['energy_per_atom'])
        score = 0.0
        if S_1100 < step.get('S_threshold_1100K', 0.05):
            score += 0.4
        if E_1100 > E_1000 + step.get('energy_jump_min', 0.001):
            score += 0.6
        return score
    except Exception:
        return 0.0


# === block: score_1 (check id='step_density_heating_300K') ===
def score_1(artifact, step, ctx):
    try:
        max_d = 0.0
        for r in artifact:
            d = float(r['density'])
            if d > max_d:
                max_d = d
        if max_d >= step.get('min_central_peak', 0.05):
            return 1.0
        return 0.0
    except Exception:
        return 0.0


# === block: score_2 (check id='step_density_quenching_300K') ===
def score_2(artifact, step, ctx):
    try:
        quench_max = max(float(r['density']) for r in artifact)
        import csv, os
        heating_path = os.path.join('/app/outputs', 'density_profile_heating_300K.csv')
        if not os.path.exists(heating_path):
            return 0.0
        with open(heating_path, newline='') as f:
            hreader = csv.DictReader(f)
            heat_max = max(float(r['density']) for r in hreader)
        if heat_max <= 0:
            return 0.0
        if quench_max < heat_max and quench_max > 0:
            return 1.0
        return 0.0
    except Exception:
        return 0.0


# === block: score_3 (check id='step_comparison_metrics') ===
def score_3(artifact, step, ctx):
    try:
        heating_peak = float(artifact.get('heating_peak_density'))
        quenching_peak = float(artifact.get('quenching_peak_density'))
        peak_diff = float(artifact.get('peak_density_difference'))
        import csv, os
        heating_path = os.path.join('/app/outputs', 'density_profile_heating_300K.csv')
        quenching_path = os.path.join('/app/outputs', 'density_profile_quenching_300K.csv')
        if not os.path.exists(heating_path) or not os.path.exists(quenching_path):
            return 0.0
        def get_max(path):
            with open(path, newline='') as f:
                rdr = csv.DictReader(f)
                return max(float(r['density']) for r in rdr)
        heat_max_csv = get_max(heating_path)
        quench_max_csv = get_max(quenching_path)
        tol = step.get('max_peak_tolerance', 0.001)
        if (abs(heating_peak - heat_max_csv) <= tol and
            abs(quenching_peak - quench_max_csv) <= tol and
            abs(peak_diff - (heating_peak - quenching_peak)) <= tol and
            peak_diff > 0):
            return 1.0
        return 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'step_melting_confirmation': score_0,
    'step_density_heating_300K': score_1,
    'step_density_quenching_300K': score_2,
    'step_comparison_metrics': score_3,
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
