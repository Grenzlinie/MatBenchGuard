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


# === block: score_0 (check id='step_simulate') ===
def score_0(artifact, step, ctx):
        def check_monotonic(values, tol):
            if len(values) < 2:
                return 0.0
            passed = 0
            for i in range(len(values)-1):
                if values[i+1] >= values[i] - tol:
                    passed += 1
            return passed / (len(values) - 1)

        def check_diminishing_returns(values, tol):
            # Check that increments are decreasing: (v[i+2]-v[i+1]) - (v[i+1]-v[i]) <= tol
            n = len(values)
            if n < 3:
                return 0.0
            passed = 0
            for i in range(n-2):
                d1 = values[i+1] - values[i]
                d2 = values[i+2] - values[i+1]
                if d2 - d1 <= tol:
                    passed += 1
            return passed / (n - 2)

        def check_overall_increase(values, min_inc):
            if len(values) < 2:
                return 0.0
            return 1.0 if (values[-1] - values[0]) >= min_inc else 0.0

        def check_range(values, low, high):
            if not values:
                return 0.0
            inside = sum(1 for v in values if low <= v <= high)
            return inside / len(values)

        cmmi = artifact.get('cmmi_trend', [])
        risk = artifact.get('risk_input_trend', [])

        tols = step.get('tolerances', {})
        mono_tol = tols.get('mono_tol', 0.02)
        convex_tol = tols.get('convex_tol', 0.02)
        min_inc = tols.get('min_increase', 0.05)
        rng = tols.get('value_range', [-1.0, 1.0])

        if not cmmi or not risk:
            return 0.0

        # Extract trustworthiness values
        cmmi_values = [d['avg_trustworthiness'] for d in sorted(cmmi, key=lambda x: x.get('cmmi_level', 0)) if 'avg_trustworthiness' in d]
        risk_values = [d['avg_trustworthiness'] for d in sorted(risk, key=lambda x: x.get('schedule_time', 0.0)) if 'avg_trustworthiness' in d]

        if len(cmmi_values) != 5 or len(risk_values) != 6:
            return 0.0

        # Sub-scores
        s_cmmi_mono = check_monotonic(cmmi_values, mono_tol)
        s_cmmi_inc = check_overall_increase(cmmi_values, min_inc)
        s_cmmi_range = check_range(cmmi_values, rng[0], rng[1])

        s_risk_mono = check_monotonic(risk_values, mono_tol)
        s_risk_dim = check_diminishing_returns(risk_values, convex_tol)
        s_risk_range = check_range(risk_values, rng[0], rng[1])

        # Weighted combination (weights sum to 1.0)
        score = (0.25 * s_cmmi_mono + 0.1 * s_cmmi_inc + 0.05 * s_cmmi_range +
                 0.3 * s_risk_mono + 0.25 * s_risk_dim + 0.05 * s_risk_range)
        return max(0.0, min(1.0, score))
    


_SCORERS = {
    'step_simulate': score_0,
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
