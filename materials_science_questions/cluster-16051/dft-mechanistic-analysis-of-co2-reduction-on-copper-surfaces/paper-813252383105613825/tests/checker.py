import os
import json
import csv

# === author imports / helpers ===
import json, math

KB = 8.617333262145e-5
T = 300.0
KT = KB * T


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
    import os
    barriers_path = os.path.join(outputs_dir, 'step_01_barriers.json')
    with open(barriers_path) as f:
        barriers = json.load(f)

    paper_ref = {
        'barriers': {
            'CH3O_to_CH3OH': 0.15,
            'CH3O_to_CH4': 1.21,
            'CO_to_CHO': 0.39,
            'CO_to_COH': 0.21
        },
        'ratio_pathI': 6e17,
        'ratio_CO': 2000.0
    }

    return {'barriers': barriers, 'paper_ref': paper_ref}


# === block: score_0 (check id='barriers_check') ===
def score_0(artifact, step, ctx):
    paper = ctx['paper_ref']['barriers']
    tol = 0.2
    keys = ['CH3O_to_CH3OH', 'CH3O_to_CH4', 'CO_to_CHO', 'CO_to_COH']
    barrier_scores = []
    for k in keys:
        v = artifact.get(k)
        if v is None:
            barrier_scores.append(0.0)
            continue
        if abs(v - paper[k]) <= tol:
            barrier_scores.append(1.0)
        else:
            barrier_scores.append(0.0)
    barrier_avg = sum(barrier_scores) / len(keys) if keys else 0.0

    # Ordering check
    ordering_ok = True
    if artifact.get('CH3O_to_CH3OH') is not None and artifact.get('CH3O_to_CH4') is not None:
        if artifact['CH3O_to_CH3OH'] >= artifact['CH3O_to_CH4']:
            ordering_ok = False
    if artifact.get('CO_to_COH') is not None and artifact.get('CO_to_CHO') is not None:
        if artifact['CO_to_COH'] >= artifact['CO_to_CHO']:
            ordering_ok = False
    order_score = 1.0 if ordering_ok else 0.0

    return barrier_avg * 0.8 + order_score * 0.2


# === block: score_1 (check id='selectivity_check') ===
def score_1(artifact, step, ctx):
    barriers = ctx['barriers']
    paper = ctx['paper_ref']
    # recompute differences and ratios from step_01 barriers
    diff_pathI = barriers.get('CH3O_to_CH4', 0.0) - barriers.get('CH3O_to_CH3OH', 0.0)
    ratio_pathI = math.exp(diff_pathI / KT)
    diff_CO = barriers.get('CO_to_CHO', 0.0) - barriers.get('CO_to_COH', 0.0)
    ratio_CO = math.exp(diff_CO / KT)

    # 1. self-consistency: compare reported values to recomputed
    fuzz = 1e-5
    consistency = 0.0
    n_checks = 0
    if artifact.get('barrier_difference_pathI') is not None:
        if abs(artifact['barrier_difference_pathI'] - diff_pathI) <= fuzz:
            consistency += 1.0
        n_checks += 1
    if artifact.get('selectivity_ratio_pathI') is not None:
        if abs(artifact['selectivity_ratio_pathI'] - ratio_pathI) <= fuzz * ratio_pathI:
            consistency += 1.0
        n_checks += 1
    if artifact.get('barrier_difference_CO_reduction') is not None:
        if abs(artifact['barrier_difference_CO_reduction'] - diff_CO) <= fuzz:
            consistency += 1.0
        n_checks += 1
    if artifact.get('selectivity_pathII_over_I') is not None:
        if abs(artifact['selectivity_pathII_over_I'] - ratio_CO) <= fuzz * ratio_CO:
            consistency += 1.0
        n_checks += 1
    consistency_score = consistency / max(n_checks, 1)

    # 2. accuracy: compare recomputed ratios to paper gold within factor 10
    factor = 10.0
    accuracy_score = 1.0
    if paper['ratio_pathI'] > 0:
        if not (paper['ratio_pathI'] / factor <= ratio_pathI <= paper['ratio_pathI'] * factor):
            accuracy_score = 0.0
    if paper['ratio_CO'] > 0:
        if not (paper['ratio_CO'] / factor <= ratio_CO <= paper['ratio_CO'] * factor):
            accuracy_score = 0.0

    return 0.4 * consistency_score + 0.6 * accuracy_score


_SCORERS = {
    'barriers_check': score_0,
    'selectivity_check': score_1,
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
