import os
import json
import csv

# === author imports / helpers ===
import json, math
from collections import defaultdict


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
    step = spec['steps'][0]
    return {
        'threshold_targets': step['threshold_targets'],
        'threshold_tol': step['threshold_tolerance'],
        'decay_checks': step['decay_mode_checks']
    }


# === block: score_0 (check id='fragmentation_analysis') ===
def score_0(artifact, step, ctx):
    events = artifact
    if not isinstance(events, list):
        return 0.0

    n_events = defaultdict(list)
    for e in events:
        n_events[e['N']].append((e['B_star'], e['outcomes']))

    threshold_targets = ctx['threshold_targets']
    threshold_tol = ctx['threshold_tol']
    decay_checks = ctx['decay_checks']

    def compute_threshold(n, data):
        points = []
        for b, outcomes in data:
            if not outcomes:
                continue
            mults = [len(o) for o in outcomes]
            avg = sum(mults) / len(mults)
            points.append((b, avg))
        if not points:
            return None
        points.sort(key=lambda x: x[0])
        prev = None
        for b, avg in points:
            if avg >= n - 1e-6:
                prev = (b, avg)
            else:
                if prev is not None:
                    b1, a1 = prev
                    b2, a2 = b, avg
                    if abs(a1 - a2) < 1e-12:
                        return b1
                    return b1 + (n - a1) * (b2 - b1) / (a2 - a1)
                else:
                    return None
        if prev is not None:
            return prev[0]
        return None

    threshold_scores = {}
    for n_str, target in threshold_targets.items():
        n = int(n_str)
        data = n_events.get(n, [])
        if not data:
            threshold_scores[n] = 0.0
            continue
        thresh = compute_threshold(n, data)
        if thresh is None:
            threshold_scores[n] = 0.0
        else:
            error = abs(thresh - target)
            if error <= threshold_tol:
                threshold_scores[n] = 1.0
            else:
                score = max(0.0, 1.0 - (error - threshold_tol) / (10 * threshold_tol))
                threshold_scores[n] = score

    mode_score_total = 0
    mode_checks_total = 0
    for n_str, check_info in decay_checks.items():
        n = int(n_str)
        data = n_events.get(n, [])
        all_outcomes = [tuple(sorted(outcome)) for _, outcomes in data for outcome in outcomes]
        mode_freq = defaultdict(int)
        for sig in all_outcomes:
            mode_freq[sig] += 1
        required_modes = check_info['modes']
        for mode_list in required_modes:
            sig = tuple(sorted(mode_list))
            if sig in mode_freq:
                mode_score_total += 1.0
        mode_checks_total += len(required_modes)

    decay_fraction = mode_score_total / mode_checks_total if mode_checks_total > 0 else 0.0

    threshold_weight = 0.6
    decay_weight = 0.4
    if threshold_scores:
        avg_thresh_score = sum(threshold_scores.values()) / len(threshold_scores)
    else:
        avg_thresh_score = 0.0

    final_score = threshold_weight * avg_thresh_score + decay_weight * decay_fraction
    return min(1.0, max(0.0, final_score))


_SCORERS = {
    'fragmentation_analysis': score_0,
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
