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


# === block: score_0 (check id='ref_match_errors') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get('gold_rows', [])
    tolerance_config = step.get('tolerance_config', {})

    if not gold_rows or not tolerance_config:
        return 0.0

    rules = tolerance_config.get('rules', [])

    def within_tolerance(observed, gold):
        # threshold_or_better: only reject if observed is WORSE than gold + tolerance margin
        if gold == 0.0:
            # for gold=0% error, accept any tiny non-negative observed (essentially the same)
            return observed <= 0.01
        for rule in rules:
            if 'if_error_lt' in rule and gold < rule['if_error_lt']:
                rel = rule['relative_tolerance']
                if rel is not None:
                    return observed <= gold * (1.0 + rel) + 1e-9
            elif 'if_error_between' in rule:
                lo, hi = rule['if_error_between']
                if lo <= gold <= hi:
                    rel = rule['relative_tolerance']
                    if rel is not None:
                        return observed <= gold * (1.0 + rel) + 1e-9
            elif 'if_error_gt' in rule and gold > rule['if_error_gt']:
                abs_tol = rule['absolute_tolerance']
                if abs_tol is not None:
                    return observed <= gold + abs_tol + 1e-9
        # fallback: observed must not be strictly larger than gold (any smaller is fine)
        return observed <= gold + 1e-9

    matched = 0
    total = len(gold_rows)
    if total == 0:
        return 0.0

    artifact_index = {}
    for row in artifact:
        try:
            key = (str(row['flow']).strip(), int(row['Reynolds']), float(row['k']))
            artifact_index[key] = float(row['error_percent'])
        except (ValueError, KeyError):
            continue

    for gold in gold_rows:
        key = (gold['flow'], gold['Reynolds'], gold['k'])
        if key in artifact_index:
            obs = artifact_index[key]
            gold_val = gold['error_percent']
            if within_tolerance(obs, gold_val):
                matched += 1

    return matched / total if total > 0 else 0.0


# === block: score_1 (check id='structural_k_conditions') ===
def score_1(artifact, step, ctx):
    thresholds = step.get('flow_k2_thresholds', {})
    if not thresholds:
        return 0.0

    # build index from artifact
    rows_by_key = {}
    for row in artifact:
        try:
            flow = str(row['flow']).strip()
            reynolds = int(row['Reynolds'])
            k = float(row['k'])
            err = float(row['error_percent'])
        except (ValueError, KeyError):
            continue
        key = (flow, reynolds)
        if key not in rows_by_key:
            rows_by_key[key] = {}
        rows_by_key[key][k] = err

    total_conditions = 0
    satisfied = 0

    for (flow, reynolds), k_dict in rows_by_key.items():
        # check k=1 > 100%
        if 1.0 in k_dict:
            total_conditions += 1
            if k_dict[1.0] > 100.0:
                satisfied += 1
        # check k=2 < threshold
        if 2.0 in k_dict and flow in thresholds:
            total_conditions += 1
            if k_dict[2.0] < thresholds[flow]:
                satisfied += 1

    return satisfied / total_conditions if total_conditions > 0 else 0.0


_SCORERS = {
    'ref_match_errors': score_0,
    'structural_k_conditions': score_1,
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
