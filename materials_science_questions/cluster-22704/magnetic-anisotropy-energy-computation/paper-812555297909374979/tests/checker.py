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


# === block: score_0 (check id='mae_structural') ===
def score_0(artifact, step, ctx):
    data = artifact
    checks = []
    checks.append(data.get('cubic_AF_MAE', 0) > 0)
    ea_af = str(data.get('cubic_AF_easy_axis', ''))
    checks.append('110' in ea_af and '100' not in ea_af)
    checks.append(data.get('cubic_FM_MAE', 0) < 0)
    ea_fm = str(data.get('cubic_FM_easy_axis', ''))
    checks.append('100' in ea_fm and '110' not in ea_fm)
    checks.append(data.get('strained_AF_MAE', 0) > 0)
    ea_saf = str(data.get('strained_AF_easy_axis', ''))
    checks.append('110' in ea_saf and '100' not in ea_saf)
    checks.append(data.get('strained_FM_MAE', 0) < 0)
    ea_sfm = str(data.get('strained_FM_easy_axis', ''))
    checks.append('100' in ea_sfm and '110' not in ea_sfm)
    checks.append(abs(data.get('strained_AF_MAE', 0)) > abs(data.get('cubic_AF_MAE', 0)))
    checks.append(abs(data.get('strained_FM_MAE', 0)) < abs(data.get('cubic_FM_MAE', 0)))
    score = sum(checks) / 10.0
    return score


# === block: score_1 (check id='mc_structural') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 360:
        return 0.0
    try:
        phi_rad = [math.radians(float(row['phi_deg'])) for row in rows]
        hc_af = [float(row['Hc_SM_AF_bilayer']) for row in rows]
        hc_fm = [float(row['Hc_SM_FM_bilayer']) for row in rows]
    except (KeyError, ValueError):
        return 0.0
    cos4 = [math.cos(4.0 * p) for p in phi_rad]
    sin4 = [math.sin(4.0 * p) for p in phi_rad]
    n = len(hc_af)
    mean_af = sum(hc_af) / n
    den_a2 = sum((h - mean_af) ** 2 for h in hc_af)
    if den_a2 == 0:
        return 0.0
    num_af_c = sum((h - mean_af) * c for h, c in zip(hc_af, cos4))
    num_af_s = sum((h - mean_af) * s for h, s in zip(hc_af, sin4))
    den_c2 = sum(c ** 2 for c in cos4)
    den_s2 = sum(s ** 2 for s in sin4)
    corr_af_c = num_af_c / math.sqrt(den_a2 * den_c2) if den_c2 != 0 else 0.0
    corr_af_s = num_af_s / math.sqrt(den_a2 * den_s2) if den_s2 != 0 else 0.0
    mean_fm = sum(hc_fm) / n
    den_fm2 = sum((h - mean_fm) ** 2 for h in hc_fm)
    if den_fm2 == 0:
        return 0.0
    num_fm_c = sum((h - mean_fm) * c for h, c in zip(hc_fm, cos4))
    num_fm_s = sum((h - mean_fm) * s for h, s in zip(hc_fm, sin4))
    corr_fm_c = num_fm_c / math.sqrt(den_fm2 * den_c2) if den_fm2 != 0 and den_c2 != 0 else 0.0
    corr_fm_s = num_fm_s / math.sqrt(den_fm2 * den_s2) if den_fm2 != 0 and den_s2 != 0 else 0.0
    score = 0.0
    if corr_af_c > 0.7 and abs(corr_af_s) < 0.3:
        score += 0.5
    if corr_fm_c < -0.7 and abs(corr_fm_s) < 0.3:
        score += 0.5
    return score


_SCORERS = {
    'mae_structural': score_0,
    'mc_structural': score_1,
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
