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
    ctx = {}
    for step in spec.get('steps', []):
        if step['id'] == 'step_output_freq':
            ctx['gold_frequencies'] = step['gold_frequencies']
            ctx['tolerance_freq_cm'] = float(step['tolerance_freq_cm'])
            ctx['range_threshold_cm'] = float(step['max_min_range_threshold_cm'])
        elif step['id'] == 'step_output_gamma':
            ctx['gold_gruneisen'] = float(step['gold_gruneisen'])
            ctx['tolerance_gruneisen'] = float(step['tolerance_gruneisen'])
    return ctx


# === block: score_0 (check id='step_output_freq') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_frequencies']
    tol = ctx['tolerance_freq_cm']
    range_th = ctx['range_threshold_cm']
    freq = {}
    for row in artifact:
        sys = str(row.get('system', '')).strip()
        try:
            val = float(row.get('frequency_cm1'))
        except (ValueError, TypeError):
            val = None
        if sys and val is not None:
            freq[sys] = val
    scores = []
    for sys, g in gold.items():
        if sys in freq:
            dev = abs(freq[sys] - g)
            s = max(0.0, 1.0 - dev / tol)
            scores.append(s)
        else:
            scores.append(0.0)
    per_sys_avg = sum(scores) / len(scores) if scores else 0.0
    vals = [v for v in freq.values()]
    if len(vals) < 2:
        range_score = 0.0
    else:
        range_val = max(vals) - min(vals)
        if range_val <= range_th:
            range_score = 1.0
        else:
            range_score = max(0.0, 1.0 - (range_val - range_th) / range_th)
    score = 0.7 * per_sys_avg + 0.3 * range_score
    return score


# === block: score_1 (check id='step_output_gamma') ===
def score_1(artifact, step, ctx):
    s = str(artifact).strip().splitlines()[0].strip()
    try:
        val = float(s)
    except (ValueError, TypeError):
        return 0.0
    gold = ctx['gold_gruneisen']
    tol = ctx['tolerance_gruneisen']
    dev = abs(val - gold)
    score = max(0.0, 1.0 - dev / tol)
    return score


_SCORERS = {
    'step_output_freq': score_0,
    'step_output_gamma': score_1,
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
