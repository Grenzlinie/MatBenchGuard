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


# === block: score_0 (check id='step_06') ===
def score_0(artifact, step, ctx):
    fields = step.get('fields', {})
    score = 0.0
    higher_better_fields = {'reducing_capacity', 'oxidizing_ability', 'electron_mobility_x', 'electron_mobility_y', 'hole_mobility_x', 'hole_mobility_y', 'absorption_coefficient_visible'}
    lower_better_fields = {'absorption_edge'}
    for field_name, cfg in fields.items():
        gold = cfg.get('gold')
        weight = cfg.get('weight', 0.0)
        if field_name == 'alignment_type':
            val = artifact.get(field_name, '')
            if isinstance(val, str) and val.strip().lower() == gold.strip().lower():
                field_score = 1.0
            else:
                field_score = 0.0
        elif field_name in higher_better_fields:
            val = artifact.get(field_name)
            if val is None or not isinstance(val, (int, float)):
                field_score = 0.0
            else:
                val = float(val)
                if 'tolerance_abs' in cfg:
                    tol = cfg['tolerance_abs']
                    if val >= gold:
                        field_score = 1.0
                    else:
                        diff = gold - val
                        if tol > 0:
                            field_score = max(0.0, 1.0 - diff / tol)
                        else:
                            field_score = 1.0 if diff == 0 else 0.0
                elif 'factor_range_low' in cfg:
                    low = cfg['factor_range_low']
                    threshold = gold * low
                    if val >= threshold:
                        field_score = 1.0
                    else:
                        field_score = 0.0 if threshold <= 0 else max(0.0, val / threshold)
                else:
                    field_score = 1.0 if val >= gold else 0.0
        elif field_name in lower_better_fields:
            val = artifact.get(field_name)
            if val is None or not isinstance(val, (int, float)):
                field_score = 0.0
            else:
                val = float(val)
                tol = cfg.get('tolerance_abs', 0)
                if val <= gold:
                    field_score = 1.0
                else:
                    diff = val - gold
                    if tol > 0:
                        field_score = max(0.0, 1.0 - diff / tol)
                    else:
                        field_score = 1.0 if diff == 0 else 0.0
        else:
            if 'tolerance_abs' in cfg:
                tol = cfg['tolerance_abs']
                val = artifact.get(field_name)
                if val is None:
                    field_score = 0.0
                else:
                    diff = abs(float(val) - gold)
                    if tol > 0:
                        field_score = max(0.0, 1.0 - diff / tol)
                    else:
                        field_score = 1.0 if diff == 0.0 else 0.0
            elif 'factor_range_low' in cfg and 'factor_range_high' in cfg:
                low = cfg['factor_range_low']
                high = cfg['factor_range_high']
                val = artifact.get(field_name)
                if val is None or gold == 0:
                    field_score = 0.0
                else:
                    ratio = float(val) / gold
                    log_ratio = math.log10(ratio) if ratio > 0 else -float('inf')
                    log_low = math.log10(low)
                    log_high = math.log10(high)
                    if log_low <= log_ratio <= log_high:
                        field_score = 1.0
                    else:
                        mid = (log_low + log_high) / 2.0
                        half_range = (log_high - log_low) / 2.0
                        dist = max(0.0, abs(log_ratio - mid) - half_range)
                        field_score = max(0.0, 1.0 - dist / half_range)
            else:
                field_score = 0.0
        score += field_score * weight
    return score


_SCORERS = {
    'step_06': score_0,
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
