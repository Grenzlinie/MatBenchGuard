import os
import json
import csv

# === author imports / helpers ===
import math, csv


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


# === block: score_0 (check id='step_compute_absorption') ===
def score_0(artifact, step, ctx):
    def _check_monotonic(values, direction='decreasing', tol=1e-9):
        if len(values) < 2:
            return True
        if direction == 'decreasing':
            return all(v >= next_v - tol for v, next_v in zip(values, values[1:]))
        else:  # increasing
            return all(v <= next_v + tol for v, next_v in zip(values, values[1:]))

    def _fraction_monotonic(series_by_condition, func, threshold=0.95):
        count = 0
        total = 0
        for cond, pairs in series_by_condition.items():
            pairs_sorted = sorted(pairs, key=lambda x: x[0])
            y_vals = [y for _, y in pairs_sorted]
            if func(y_vals):
                count += 1
            total += 1
        return 1.0 if total == 0 else count / total >= threshold

    rows = artifact  # list of dicts
    cases_data = {}
    for row in rows:
        case = row['case']
        cases_data.setdefault(case, []).append(row)

    def build_series(rows_list, group_on, fixed_keys, value_key):
        series_dict = {}
        for row in rows_list:
            fixed_vals = tuple(row[k] for k in fixed_keys)
            x_val = float(row[group_on])
            y_val = float(row[value_key])
            series_dict.setdefault(fixed_vals, []).append((x_val, y_val))
        return series_dict

    trend_checks = []

    cases_checks = [
        {'case': 'DP_parallel', 'value_key': 'abs_alpha', 'temp_direction': 'increasing', 'img_nonzero': True, 'img_threshold': 0.1},
        {'case': 'DP_perpendicular', 'value_key': 'alpha_real', 'temp_direction': 'increasing', 'img_nonzero': False, 'img_threshold': 1e-6},
        {'case': 'PZ_parallel', 'value_key': 'abs_alpha', 'temp_direction': 'increasing', 'img_nonzero': True, 'img_threshold': 0.1},
        {'case': 'PZ_perpendicular', 'value_key': 'alpha_real', 'temp_direction': 'decreasing', 'img_nonzero': False, 'img_threshold': 1e-6}
    ]

    for chk in cases_checks:
        case = chk['case']
        if case not in cases_data:
            continue
        data = cases_data[case]
        # frequency decreasing
        series_freq = build_series(data, 'frequency_THz', ['thickness_um', 'temperature_K'], chk['value_key'])
        ok_freq = _fraction_monotonic(series_freq, lambda vals: _check_monotonic(vals, 'decreasing'))
        trend_checks.append(ok_freq)
        # temperature trend
        series_temp = build_series(data, 'temperature_K', ['frequency_THz', 'thickness_um'], chk['value_key'])
        ok_temp = _fraction_monotonic(series_temp, lambda vals: _check_monotonic(vals, chk['temp_direction']))
        trend_checks.append(ok_temp)
        # thickness decreasing
        series_thick = build_series(data, 'thickness_um', ['frequency_THz', 'temperature_K'], chk['value_key'])
        if case == 'PZ_perpendicular':
            # Accept an overall decreasing trend via negative slope from linear fit.
            count_negative = 0
            total_series = 0
            for cond, pairs in series_thick.items():
                pairs_sorted = sorted(pairs, key=lambda x: x[0])
                x_vals = [x for x, _ in pairs_sorted]
                y_vals = [y for _, y in pairs_sorted]
                if len(x_vals) < 2:
                    continue
                n = len(x_vals)
                sum_x = sum(x_vals)
                sum_y = sum(y_vals)
                sum_xy = sum(x*y for x,y in zip(x_vals, y_vals))
                sum_x2 = sum(x*x for x in x_vals)
                denominator = n * sum_x2 - sum_x * sum_x
                slope = (n * sum_xy - sum_x * sum_y) / denominator if denominator != 0 else 0.0
                if slope < 0:
                    count_negative += 1
                total_series += 1
            ok_thick = (count_negative / total_series >= 0.95) if total_series > 0 else True
        else:
            ok_thick = _fraction_monotonic(series_thick, lambda vals: _check_monotonic(vals, 'decreasing'))
        trend_checks.append(ok_thick)
        # imaginary part check
        imag_vals = [abs(float(row['alpha_imag'])) for row in data]
        real_vals = [abs(float(row['alpha_real'])) for row in data]
        max_imag = max(imag_vals) if imag_vals else 0.0
        max_real = max(real_vals) if real_vals else 1e-12
        ratio = max_imag / max_real if max_real > 1e-12 else 0.0
        if chk['img_nonzero']:
            trend_checks.append(ratio > chk['img_threshold'])
        else:
            trend_checks.append(ratio < chk['img_threshold'])

    score = sum(trend_checks) / len(trend_checks) if trend_checks else 0.0
    return score


_SCORERS = {
    'step_compute_absorption': score_0,
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
