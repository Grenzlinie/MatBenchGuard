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


# === block: score_0 (check id='vacancy_ordering') ===
def score_0(artifact, step, ctx):
    import math

    artifact_data = artifact  # artifact is a dict loaded from JSON
    # Read required fields
    iface_s = artifact_data.get('interface_single_vacancy_formation_energy')
    iface_d = artifact_data.get('interface_double_vacancy_formation_energy')
    bulk_s  = artifact_data.get('bulk_single_vacancy_formation_energy')
    bulk_d  = artifact_data.get('bulk_double_vacancy_formation_energy')
    # If any missing, score 0
    if any(v is None or not isinstance(v, (int,float)) for v in [iface_s, iface_d, bulk_s, bulk_d]):
        return 0.0

    # Get hidden threshold for negativity
    neg_thr = step.get('hidden', {}).get('reference_negative_threshold', 0.0)

    # HARD REQUIREMENT: at least one interface vacancy formation energy must be negative (or zero)
    min_iface = min(iface_s, iface_d)
    if min_iface > neg_thr:
        return 0.0

    # Score how much lower the most favourable interface energy is relative to its bulk counterpart
    # (full credit if the difference is at least 0.5 eV, linear ramp between 0 and 1 for [–0.5, 0])
    diff_s = iface_s - bulk_s
    diff_d = iface_d - bulk_d
    min_diff = min(diff_s, diff_d)

    if min_diff <= -0.5:
        score_val = 1.0
    elif min_diff <= 0:
        score_val = (0 - min_diff) / 0.5
    else:
        score_val = 0.0

    # Reference oracle: iface_s=-0.30, iface_d=0.22, bulk_s=0.30, bulk_d=0.50
    # min_iface = -0.30 ≤ 0   => passes negativity gate
    # min_diff  = -0.60       => full credit (1.0)

    return min(max(score_val, 0.0), 1.0)


# === block: score_1 (check id='barrier_magnitude') ===
def score_1(artifact, step, ctx):
    import math

    artifact_data = artifact
    barriers = artifact_data.get('migration_barriers_CeO2')
    if not isinstance(barriers, list) or not barriers:
        return 0.0
    if not all(isinstance(b, (int,float)) for b in barriers):
        return 0.0

    max_barrier = step.get('hidden', {}).get('max_barrier_eV', 0.2)
    tol = step.get('hidden', {}).get('tolerance_abs', 0.1)
    threshold = max_barrier + tol  # barrier up to 0.3 eV gets partial credit

    # Threshold-or-better: every barrier <= max_barrier gives full credit (1.0).
    # For barriers above 0.2, linear penalty; if any barrier > 1.0, zero.
    # More precisely: score = (number of barriers <= max_barrier) / total; we want to penalize excessively high barriers.
    fine_count = sum(1 for b in barriers if b <= max_barrier)
    penalty = sum((b - max_barrier) for b in barriers if b > max_barrier)  # total excess (eV)
    # Use penalty to reduce score: if fine_count == total, score = 1.0, else score = max(0.0, 1.0 - penalty / 0.5)
    # But ensure oracle (barriers 0.09,0.17) fine_count=2, penalty=0 -> score=1.0.
    total = len(barriers)
    if fine_count == total:
        score_val = 1.0
    else:
        # if any barrier is too high, reduce proportionally
        score_val = max(0.0, 1.0 - (penalty / 0.5))
        # also cap at fine_count/total as a baseline
        score_val = min(score_val, fine_count / total)
    return min(max(score_val, 0.0), 1.0)


_SCORERS = {
    'vacancy_ordering': score_0,
    'barrier_magnitude': score_1,
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
