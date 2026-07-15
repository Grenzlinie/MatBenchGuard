import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='check_mechanical_properties') ===
def score_0(artifact, step, ctx):
    gold_moduli = step.get('gold_moduli', {})
    gold_strengths = step.get('gold_strengths', {})
    tol_modulus = step.get('tol_modulus', 0.30)
    tol_strength = step.get('tol_strength', 0.20)

    configs = ['PG', 'GV_all', 'GV_half']
    rows_by_config = {c: [] for c in configs}

    for row in artifact:
        cfg = row.get('config', '').strip()
        try:
            strain_val = float(row['strain'])
            stress_val = float(row['stress'])
        except (ValueError, KeyError, TypeError):
            continue
        if cfg in rows_by_config:
            rows_by_config[cfg].append((strain_val, stress_val))


    def compute_modulus(points):
        filtered = [(s, t) for s, t in points if 0.01 <= s <= 0.03]
        n = len(filtered)
        if n < 5:
            return None
        sum_x = sum(p[0] for p in filtered)
        sum_y = sum(p[1] for p in filtered)
        sum_xx = sum(p[0] * p[0] for p in filtered)
        sum_xy = sum(p[0] * p[1] for p in filtered)
        denom = n * sum_xx - sum_x * sum_x
        if abs(denom) < 1e-20:
            return None
        slope = (n * sum_xy - sum_x * sum_y) / denom
        return slope


    def compute_strength(points):
        stresses = [p[1] for p in points]
        if not stresses:
            return None
        return max(stresses)


    moduli = {}
    strengths = {}
    for cfg in configs:
        pts = rows_by_config[cfg]
        moduli[cfg] = compute_modulus(pts)
        strengths[cfg] = compute_strength(pts)

    score = 0.0
    total_weight = 0.0
    config_weight = 0.16

    for cfg in configs:
        m_gold = gold_moduli.get(cfg)
        s_gold = gold_strengths.get(cfg)
        m = moduli[cfg]
        s = strengths[cfg]
        if m is not None and m_gold is not None and m_gold > 0:
            rel_diff = abs(m - m_gold) / m_gold
            if rel_diff <= tol_modulus:
                score += config_weight
            else:
                decay = max(0.0, 1.0 - (rel_diff - tol_modulus) / tol_modulus)
                score += config_weight * decay
        total_weight += config_weight

        if s is not None and s_gold is not None and s_gold > 0:
            rel_diff = abs(s - s_gold) / s_gold
            if rel_diff <= tol_strength:
                score += config_weight
            else:
                decay = max(0.0, 1.0 - (rel_diff - tol_strength) / tol_strength)
                score += config_weight * decay
        total_weight += config_weight

    m_all = moduli.get('GV_all')
    m_half = moduli.get('GV_half')
    m_pg = moduli.get('PG')
    if None not in (m_all, m_half, m_pg):
        if m_all > m_half and m_half > m_pg:
            score += 0.02
        total_weight += 0.02

    s_all = strengths.get('GV_all')
    s_half = strengths.get('GV_half')
    s_pg = strengths.get('PG')
    if None not in (s_all, s_half, s_pg):
        if s_half > s_all and s_all > s_pg:
            score += 0.02
        total_weight += 0.02

    if total_weight > 0:
        normalized_score = score / total_weight
    else:
        normalized_score = 0.0

    return float(normalized_score)


_SCORERS = {
    'check_mechanical_properties': score_0,
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
