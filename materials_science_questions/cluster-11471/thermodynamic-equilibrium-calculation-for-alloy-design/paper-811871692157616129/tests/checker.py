import os
import json
import csv

# === author imports / helpers ===
import csv
import os


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
    return {}  # gold values are embedded in the step config, no shared preprocessing needed


# === block: score_0 (check id='check_alloy') ===
def score_0(artifact, step, ctx):
    # artifact is a list of dicts loaded from CSV
    if not artifact or not isinstance(artifact, list):
        return 0.0
    cfg = step.get('scoring', {})
    gold_dict = cfg.get('gold', {})
    id_col = cfg.get('identifier_column', '')
    val_col = cfg.get('value_column', '')
    tol = float(cfg.get('tolerance_abs', 0.2))

    # 1. magnitude score (reference match)
    row_scores_mag = []
    for row in artifact:
        key = row.get(id_col, '').strip()
        gold = gold_dict.get(key, None)
        if gold is None:
            row_scores_mag.append(0.0)
            continue
        try:
            agent_val = float(row.get(val_col, ''))
        except (ValueError, TypeError):
            row_scores_mag.append(0.0)
            continue
        diff = abs(agent_val - gold)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        row_scores_mag.append(score)
    mag_score = sum(row_scores_mag) / len(row_scores_mag) if row_scores_mag else 0.0

    # 2. trend score (qualitative ordering)
    agent_vals = {}
    for row in artifact:
        key = row.get(id_col, '').strip()
        try:
            agent_vals[key] = float(row.get(val_col, ''))
        except (ValueError, TypeError):
            agent_vals[key] = None

    # Expected inequalities: (lower, higher) pairs reflecting Al/Cr/Mo < Cu/Mn/Ni and P > all
    inequalities = [
        ('Cr', 'Cu'),
        ('Mo', 'Ni'),
        ('Al', 'Mn'),
        ('Mo', 'Mn'),
        ('Cr', 'Mn'),
        ('Al', 'Ni'),
        ('P', 'Si'),
        ('P', 'Cu'),
        ('P', 'Mn'),
        ('P', 'Ni'),
        ('P', 'Al'),
        ('P', 'Cr'),
        ('P', 'Mo'),
    ]
    satisfied = 0
    total_checks = len(inequalities)
    for low, high in inequalities:
        v_low = agent_vals.get(low)
        v_high = agent_vals.get(high)
        if v_low is not None and v_high is not None and v_low < v_high:
            satisfied += 1

    # Si should be close to Cu/Mn/Ni
    base_vals = [agent_vals.get(x) for x in ('Cu', 'Mn', 'Ni')]
    base_vals = [v for v in base_vals if v is not None]
    if base_vals and agent_vals.get('Si') is not None:
        avg_base = sum(base_vals) / len(base_vals)
        if abs(agent_vals['Si'] - avg_base) <= 0.1:
            satisfied += 1
        total_checks += 1

    trend_score = satisfied / total_checks if total_checks > 0 else 0.0

    # combine: 0.6 magnitude + 0.4 trend (adjust weights as needed)
    final = 0.6 * mag_score + 0.4 * trend_score
    return final


# === block: score_1 (check id='check_trip') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    cfg = step.get('scoring', {})
    sub_weights = {}
    sub_golds = {}
    sub_tols = {}
    sub_id_col = None
    sub_val_cols = {}
    # parse sub‑checks
    for sub_key, sub_cfg in cfg.items():
        if not isinstance(sub_cfg, dict):
            continue
        sub_golds[sub_key] = sub_cfg.get('gold', {})
        sub_tols[sub_key] = float(sub_cfg.get('tolerance_abs', 0.2))
        sub_weights[sub_key] = float(sub_cfg.get('weight', 0.0))
        if sub_id_col is None:
            sub_id_col = sub_cfg.get('identifier_column', '')
        sub_val_cols[sub_key] = sub_cfg.get('value_column', '')
    total_weight = sum(sub_weights.values())
    if total_weight == 0:
        return 0.0
    # compute per‑sub score
    sub_scores = {}
    for sub_key, gold_dict in sub_golds.items():
        val_col = sub_val_cols.get(sub_key, '')
        tol = sub_tols[sub_key]
        row_scores = []
        for row in artifact:
            key = row.get(sub_id_col, '').strip()
            gold = gold_dict.get(key, None)
            if gold is None:
                row_scores.append(0.0)
                continue
            try:
                agent_val = float(row.get(val_col, ''))
            except (ValueError, TypeError):
                row_scores.append(0.0)
                continue
            diff = abs(agent_val - gold)
            score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
            row_scores.append(score)
        if row_scores:
            sub_scores[sub_key] = sum(row_scores) / len(row_scores)
        else:
            sub_scores[sub_key] = 0.0
    # weighted combination
    final = 0.0
    for sub_key, w in sub_weights.items():
        final += w * sub_scores.get(sub_key, 0.0)
    return final / total_weight


_SCORERS = {
    'check_alloy': score_0,
    'check_trip': score_1,
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
