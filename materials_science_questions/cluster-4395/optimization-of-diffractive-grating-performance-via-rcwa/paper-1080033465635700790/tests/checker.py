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


# === block: score_0 (check id='s02_sim_power_ratio') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    with_ref = []
    without_ref = []
    for row in artifact:
        try:
            w = float(row.get('power_ratio_with_reflector', ''))
            wo = float(row.get('power_ratio_without_reflector', ''))
            with_ref.append(w)
            without_ref.append(wo)
        except:
            continue
    if not with_ref or not without_ref:
        return 0.0
    max_ref = max(with_ref)
    max_no_ref = max(without_ref)
    th = step.get('thresholds', {})
    with_min = th.get('with_reflector_min', 0.9)
    without_min = th.get('without_reflector_min', 0.3)
    without_max = th.get('without_reflector_max', 0.5)
    if max_ref >= with_min and without_min <= max_no_ref <= without_max:
        return 1.0
    return 0.0


# === block: score_1 (check id='s03_efficiency') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    tm_data = artifact.get('TM')
    te_data = artifact.get('TE')
    if not isinstance(tm_data, dict) or not isinstance(te_data, dict):
        return 0.0
    tm_eff = float(tm_data.get('peak_efficiency', -1))
    te_eff = float(te_data.get('peak_efficiency', -1))
    if tm_eff < 0 or te_eff < 0:
        return 0.0
    # misalignment tolerance width
    try:
        tol_um = float(artifact.get('tolerance_3dB_um', -1))
    except (ValueError, TypeError):
        tol_um = -1.0

    # efficiency scores
    targets = step.get('targets', {})
    tm_target = targets.get('TM', 0.70)
    te_target = targets.get('TE', 0.78)
    tol_rel = targets.get('tolerance_relative', 0.15)

    tm_thresh = tm_target * (1 - tol_rel)
    te_thresh = te_target * (1 - tol_rel)
    score_tm = min(1.0, tm_eff / tm_thresh) if tm_thresh > 0 else 1.0
    score_te = min(1.0, te_eff / te_thresh) if te_thresh > 0 else 1.0

    # misalignment tolerance score (higher is better, threshold_or_better)
    mis_target = targets.get('misalignment_target_um', 8.0)
    mis_tol = targets.get('misalignment_tolerance_relative', 0.2)
    mis_thresh = mis_target * (1 - mis_tol)
    if tol_um < 0 or mis_thresh <= 0:
        score_mis = 0.0
    else:
        score_mis = min(1.0, tol_um / mis_thresh)

    return (score_tm + score_te + score_mis) / 3.0


# === block: score_2 (check id='s04_overlap_bound') ===
def score_2(artifact, step, ctx):
    txt = artifact
    if not isinstance(txt, str):
        return 0.0
    try:
        val = float(txt.strip())
    except:
        return 0.0
    target = step.get('target', 0.80)
    tol = step.get('tolerance_abs', 0.05)
    if abs(val - target) <= tol:
        return 1.0
    return 0.0


_SCORERS = {
    's02_sim_power_ratio': score_0,
    's03_efficiency': score_1,
    's04_overlap_bound': score_2,
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
