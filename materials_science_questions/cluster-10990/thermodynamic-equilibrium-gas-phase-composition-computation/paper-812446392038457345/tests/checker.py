import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    def compute_ratios(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                return None, None, None
            ratios = []
            reaction_to_ratio = {}
            for row in rows:
                try:
                    r = float(row['ratio'])
                    ratios.append(r)
                    reaction_to_ratio[row['reaction'].strip()] = r
                except (ValueError, KeyError):
                    return None, None, None
            if len(ratios) < 2:
                return None, None, None
            mean = sum(ratios) / len(ratios)
            variance = sum((x - mean) ** 2 for x in ratios) / (len(ratios) - 1)
            std = math.sqrt(variance)
            return mean, std, reaction_to_ratio

    gold_mean = step['gold_mean']
    gold_std = step['gold_std']
    mean_tol = step['mean_tolerance']
    std_tol = step['std_tolerance']
    rel_tol = step['per_substance_ratio_tolerance']
    gold_list = step['gold_per_substance']

    mean, std, rmap = compute_ratios('/app/outputs/ratios.csv')
    if mean is None:
        return 0.0

    # mean sub-score
    diff_mean = abs(mean - gold_mean)
    if diff_mean <= mean_tol:
        mean_score = 1.0
    else:
        mean_score = max(0.0, 1.0 - (diff_mean - mean_tol) / mean_tol)

    # std sub-score
    diff_std = abs(std - gold_std)
    if diff_std <= std_tol:
        std_score = 1.0
    else:
        std_score = max(0.0, 1.0 - (diff_std - std_tol) / std_tol)

    # per-substance match
    matched = 0
    for entry in gold_list:
        gold_ratio = entry['ratio']
        agent_ratio = rmap.get(entry['reaction'])
        if agent_ratio is not None and gold_ratio != 0:
            if abs(agent_ratio - gold_ratio) / abs(gold_ratio) <= rel_tol:
                matched += 1
    total = len(gold_list)
    match_score = matched / total if total > 0 else 0.0

    score = 0.4 * mean_score + 0.4 * std_score + 0.2 * match_score
    return score


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    summary = artifact  # dict loaded from summary.json
    if not isinstance(summary, dict) or 'mean_ratio' not in summary or 'std_ratio' not in summary:
        return 0.0
    reported_mean = summary['mean_ratio']
    reported_std = summary['std_ratio']

    # recompute from ratios.csv for consistency
    import csv, math
    with open('/app/outputs/ratios.csv', newline='') as f:
        reader = csv.DictReader(f)
        ratios = [float(row['ratio']) for row in reader]
    if len(ratios) < 2:
        return 0.0
    mean = sum(ratios) / len(ratios)
    variance = sum((x - mean) ** 2 for x in ratios) / (len(ratios) - 1)
    std = math.sqrt(variance)

    if abs(reported_mean - mean) < 1e-4 and abs(reported_std - std) < 1e-4:
        return 1.0
    return 0.0


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
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
