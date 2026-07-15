import os
import json
import csv

# === author imports / helpers ===
def _score_pressure(artifact, step):
    pressure = step.get('pressure_kbar')
    fl_temp = step.get('fl_temp')
    method = step.get('method')
    pts = [sp for sp in artifact.get('state_points', []) if abs(sp.get('pressure_kbar', 0) - pressure) < 1e-6]
    if not pts:
        return 0.0
    pts.sort(key=lambda x: x.get('temperature_K', 0))
    recomputed_T = None
    if method == 'new_peak_prominent':
        for sp in pts:
            s2 = None
            ns2 = None
            for peak in sp.get('peaks', []):
                if peak.get('peak_id') == 'second':
                    s2 = peak.get('height')
                elif peak.get('peak_id') == 'new_second':
                    ns2 = peak.get('height')
            if s2 is None or ns2 is None:
                continue
            if ns2 >= s2:
                recomputed_T = sp.get('temperature_K')
                break
    else:
        third = []
        for sp in pts:
            for peak in sp.get('peaks', []):
                if peak.get('peak_id') == 'third':
                    third.append((sp.get('temperature_K'), peak.get('position_A')))
        if third:
            recomputed_T = min(third, key=lambda x: x[1])[0]
    # get agent reported
    reported_T = None
    reported_method = None
    for cs in artifact.get('crossover_summary', []):
        if abs(cs.get('pressure_kbar', 0) - pressure) < 1e-6:
            reported_T = cs.get('crossover_temperature_K')
            reported_method = cs.get('crossover_method')
            break
    if reported_T is None:
        return 0.0
    # method correctness
    if reported_method != method:
        return 0.0
    # self-consistency score
    if recomputed_T is not None:
        diff_self = abs(reported_T - recomputed_T)
        tol_self = 5.0
        score_self = max(0.0, min(1.0, 1.0 - diff_self / tol_self))
    else:
        score_self = 0.0
    # FL match score
    diff_fl = abs(reported_T - fl_temp)
    tol_fl = max(0.15 * fl_temp, 50.0)
    score_fl = max(0.0, min(1.0, 1.0 - diff_fl / tol_fl))
    return 0.3 * score_self + 0.7 * score_fl


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


# === block: score_0 (check id='crossover_0.5kbar') ===
def score_0(artifact, step, ctx):
    return _score_pressure(artifact, step)


# === block: score_1 (check id='crossover_1.0kbar') ===
def score_1(artifact, step, ctx):
    return _score_pressure(artifact, step)


# === block: score_2 (check id='crossover_2.5kbar') ===
def score_2(artifact, step, ctx):
    return _score_pressure(artifact, step)


# === block: score_3 (check id='crossover_5.0kbar') ===
def score_3(artifact, step, ctx):
    return _score_pressure(artifact, step)


# === block: score_4 (check id='crossover_10.0kbar') ===
def score_4(artifact, step, ctx):
    return _score_pressure(artifact, step)


_SCORERS = {
    'crossover_0.5kbar': score_0,
    'crossover_1.0kbar': score_1,
    'crossover_2.5kbar': score_2,
    'crossover_5.0kbar': score_3,
    'crossover_10.0kbar': score_4,
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
