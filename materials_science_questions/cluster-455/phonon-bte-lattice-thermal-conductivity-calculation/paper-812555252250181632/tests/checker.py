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


# === block: score_0 (check id='tc_check') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tol_abs = step.get('tolerance_abs', 1.0)
    temp_map = {int(k): v for k, v in gold.items()}
    dirs = ['kappa_100', 'kappa_010', 'kappa_001']
    rows_by_temp = {}
    for row in artifact:
        try:
            t = int(float(row['temperature_K']))
            rows_by_temp[t] = row
        except (ValueError, KeyError):
            continue
    max_err = 0.0
    for t_expected, exp_vals in temp_map.items():
        if t_expected not in rows_by_temp:
            max_err = tol_abs + 2.0  # missing row heavily penalized
            break
        row = rows_by_temp[t_expected]
        for d in dirs:
            try:
                val = float(row[d])
            except (ValueError, KeyError):
                max_err = tol_abs + 2.0
                break
            err = abs(val - exp_vals[d])
            if err > max_err:
                max_err = err
    if max_err <= tol_abs:
        return 1.0
    else:
        return max(0.0, 1.0 - (max_err - tol_abs) / 2.0)


# === block: score_1 (check id='modal_check') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    try:
        rows = sorted(artifact, key=lambda r: float(r.get('frequency_THz', 0.0)))
    except Exception:
        return 0.0
    dirs = ['kappa_100_accumulated_W_mK', 'kappa_010_accumulated_W_mK', 'kappa_001_accumulated_W_mK']
    # monotonic check
    monotonic = True
    for d in dirs:
        prev = -float('inf')
        for row in rows:
            try:
                val = float(row[d])
            except (ValueError, KeyError):
                monotonic = False
                break
            if val < prev - 1e-12:
                monotonic = False
                break
            prev = val
        if not monotonic:
            break
    monotonic_score = 1.0 if monotonic else 0.0
    # saturation check
    gold_sat = step.get('gold_saturation', {})
    tol_frac = step.get('tolerance_relative', 0.15)
    last = rows[-1]
    sat_passed = 0
    for d in dirs:
        try:
            val = float(last[d])
        except (ValueError, KeyError):
            continue
        ref = gold_sat.get(d.replace('_accumulated', ''), None)
        if ref is None:
            continue
        if abs(val - ref) <= tol_frac * ref:
            sat_passed += 1
    if len(dirs) == 0:
        saturation_score = 0.0
    else:
        saturation_score = sat_passed / len(dirs)
    return 0.4 * monotonic_score + 0.6 * saturation_score


_SCORERS = {
    'tc_check': score_0,
    'modal_check': score_1,
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
