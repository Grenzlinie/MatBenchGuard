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


# === block: score_0 (check id='step_2_conductivity_mu0') ===
def score_0(artifact, step, ctx):
    rows = artifact
    data = [(float(r['frequency_cm-1']), float(r['sigma1'])) for r in rows]
    cfg = step['config']
    f_min, f_max = cfg['frequency_range']
    range_data = [(f, s) for f, s in data if f_min <= f <= f_max]
    if len(range_data) < 3:
        return 0.0
    n = len(range_data)
    sum_x = sum(f for f,_ in range_data)
    sum_y = sum(s for _,s in range_data)
    sum_xy = sum(f*s for f,s in range_data)
    sum_x2 = sum(f*f for f,_ in range_data)
    slope = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x*sum_x) if (n*sum_x2 - sum_x*sum_x) != 0 else 0
    intercept = (sum_y - slope*sum_x) / n if n else 0
    min_slope = cfg.get('min_slope', 0.0)
    slope_ok = slope > min_slope
    int_min, int_max = cfg['intercept_range']
    intercept_ok = int_min <= intercept <= int_max
    peak_freq = cfg.get('peak_threshold_low_freq', 200.0)
    peak_rel = cfg.get('peak_relative_increase', 1.0)
    has_peak = False
    for f, s in data:
        if f <= peak_freq:
            lin = slope * f + intercept
            if lin > 0 and (s - lin) > peak_rel * lin:
                has_peak = True
                break
    peak_ok = not has_peak
    if slope_ok and intercept_ok and peak_ok:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_3_conductivity_mu30') ===
def score_1(artifact, step, ctx):
    rows = artifact
    data = [(float(r['frequency_cm-1']), float(r['sigma1'])) for r in rows]
    cfg = step['config']
    f_min, f_max = cfg['frequency_range']
    range_data = [(f, s) for f, s in data if f_min <= f <= f_max]
    if len(range_data) < 3:
        return 0.0
    n = len(range_data)
    sum_x = sum(f for f,_ in range_data)
    sum_y = sum(s for _,s in range_data)
    sum_xy = sum(f*s for f,s in range_data)
    sum_x2 = sum(f*f for f,_ in range_data)
    slope = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x*sum_x) if (n*sum_x2 - sum_x*sum_x) != 0 else 0
    intercept = (sum_y - slope*sum_x) / n if n else 0
    int_min, int_max = cfg['intercept_range']
    intercept_outside = not (int_min <= intercept <= int_max)
    peak_freq = cfg.get('peak_threshold_low_freq', 200.0)
    peak_rel = cfg.get('peak_relative_increase', 1.0)
    has_peak = False
    for f, s in data:
        if f <= peak_freq:
            lin = slope * f + intercept
            if lin > 0 and (s - lin) > peak_rel * lin:
                has_peak = True
                break
    deviation_detected = intercept_outside or has_peak
    if deviation_detected:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='step_4_summary') ===
def score_2(artifact, step, ctx):
    content = artifact.strip() if isinstance(artifact, str) else str(artifact).strip()
    expected = f"best_mu={step['config']['expected_best_mu']}"
    if content == expected:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_2_conductivity_mu0': score_0,
    'step_3_conductivity_mu30': score_1,
    'step_4_summary': score_2,
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
