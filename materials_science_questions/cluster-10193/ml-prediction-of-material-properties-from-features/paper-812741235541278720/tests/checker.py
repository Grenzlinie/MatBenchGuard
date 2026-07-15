import os
import json
import csv

# === author imports / helpers ===
import json
import math

def lower_score(value, gold, tol_rel=0.05):
    thresh = gold * (1 + tol_rel)
    if value <= thresh:
        return 1.0
    upper = gold * 2
    penalty = (value - thresh) / (upper - thresh) if upper > thresh else 1.0
    return max(0.0, 1.0 - penalty)

def higher_score(value, gold, tol_abs=0.05):
    thresh = gold - tol_abs
    if value >= thresh:
        return 1.0
    if thresh > 0:
        return max(0.0, min(1.0, value / thresh))
    else:
        return 0.0


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


# === block: score_0 (check id='formation_energy_main') ===
def score_0(artifact, step, ctx):
    property = 'formation_energy'
    models_data = step['gold']
    err_tol_rel = step.get('error_tol_rel', 0.05)
    r2_tol_abs = step.get('r2_tol_abs', 0.05)
    eacc_tol_abs = step.get('eacc_tol_abs', 0.02)
    try:
        agent_results = artifact[property]['model_results']
    except (KeyError, TypeError):
        return 0.0

    model_map = {m['model']: m for m in agent_results}
    scores = []
    for g in models_data:
        model = g['model']
        a = model_map.get(model)
        if a is None:
            scores.append(0.0)
            continue
        sub_scores = []
        # error metrics (lower better)
        for k in ['cv_MAE', 'cv_RMSE', 'fcv_MAE', 'fcv_RMSE']:
            v = a.get(k)
            if v is None:
                sub_scores.append(0.0)
            else:
                sub_scores.append(lower_score(v, g[k], tol_rel=err_tol_rel))
        # R² (higher better) with absolute tolerance
        for k in ['cv_R2', 'fcv_R2']:
            v = a.get(k)
            if v is None:
                sub_scores.append(0.0)
            else:
                sub_scores.append(higher_score(v, g[k], tol_abs=r2_tol_abs))
        # E_accuracy (higher better)
        v = a.get('fcv_E_accuracy')
        if v is None:
            sub_scores.append(0.0)
        else:
            sub_scores.append(higher_score(v, g['fcv_E_accuracy'], tol_abs=eacc_tol_abs))
        scores.append(sum(sub_scores) / len(sub_scores) if sub_scores else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='band_gap_main') ===
def score_1(artifact, step, ctx):
    property = 'band_gap'
    models_data = step['gold']
    err_tol_rel = step.get('error_tol_rel', 0.05)
    r2_tol_abs = step.get('r2_tol_abs', 0.05)
    eacc_tol_abs = step.get('eacc_tol_abs', 0.02)
    try:
        agent_results = artifact[property]['model_results']
    except (KeyError, TypeError):
        return 0.0

    model_map = {m['model']: m for m in agent_results}
    scores = []
    for g in models_data:
        model = g['model']
        a = model_map.get(model)
        if a is None:
            scores.append(0.0)
            continue
        sub_scores = []
        for k in ['cv_MAE', 'cv_RMSE', 'fcv_MAE', 'fcv_RMSE']:
            v = a.get(k)
            if v is None:
                sub_scores.append(0.0)
            else:
                sub_scores.append(lower_score(v, g[k], tol_rel=err_tol_rel))
        for k in ['cv_R2', 'fcv_R2']:
            v = a.get(k)
            if v is None:
                sub_scores.append(0.0)
            else:
                sub_scores.append(higher_score(v, g[k], tol_abs=r2_tol_abs))
        v = a.get('fcv_E_accuracy')
        if v is None:
            sub_scores.append(0.0)
        else:
            sub_scores.append(higher_score(v, g['fcv_E_accuracy'], tol_abs=eacc_tol_abs))
        scores.append(sum(sub_scores) / len(sub_scores) if sub_scores else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='superconducting_Tc_main') ===
def score_2(artifact, step, ctx):
    property = 'superconducting_Tc'
    models_data = step['gold']
    err_tol_rel = step.get('error_tol_rel', 0.05)
    r2_tol_abs = step.get('r2_tol_abs', 0.05)
    eacc_tol_abs = step.get('eacc_tol_abs', 0.02)
    try:
        agent_results = artifact[property]['model_results']
    except (KeyError, TypeError):
        return 0.0

    model_map = {m['model']: m for m in agent_results}
    scores = []
    for g in models_data:
        model = g['model']
        a = model_map.get(model)
        if a is None:
            scores.append(0.0)
            continue
        sub_scores = []
        for k in ['cv_MAE', 'cv_RMSE', 'fcv_MAE', 'fcv_RMSE']:
            v = a.get(k)
            if v is None:
                sub_scores.append(0.0)
            else:
                sub_scores.append(lower_score(v, g[k], tol_rel=err_tol_rel))
        for k in ['cv_R2', 'fcv_R2']:
            v = a.get(k)
            if v is None:
                sub_scores.append(0.0)
            else:
                sub_scores.append(higher_score(v, g[k], tol_abs=r2_tol_abs))
        v = a.get('fcv_E_accuracy')
        if v is None:
            sub_scores.append(0.0)
        else:
            sub_scores.append(higher_score(v, g['fcv_E_accuracy'], tol_abs=eacc_tol_abs))
        scores.append(sum(sub_scores) / len(sub_scores) if sub_scores else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='formation_energy_mstep') ===
def score_3(artifact, step, ctx):
    gold = step['gold']
    err_tol_rel = step.get('error_tol_rel', 0.05)
    eacc_tol_abs = step.get('eacc_tol_abs', 0.02)
    try:
        agent_steps = artifact['formation_energy']['m_step_results']
    except (KeyError, TypeError):
        return 0.0

    # index by (model, m)
    agent_map = {(e['model'], e['m']): e for e in agent_steps}
    scores = []
    for g in gold:
        key = (g['model'], g['m'])
        a = agent_map.get(key)
        if a is None:
            scores.append(0.0)
            continue
        sub = []
        # cv_MAE (lower)
        v = a.get('cv_MAE')
        if v is not None:
            sub.append(lower_score(v, g['cv_MAE'], tol_rel=err_tol_rel))
        else:
            sub.append(0.0)
        # fcv_MAE (lower)
        v = a.get('fcv_MAE')
        if v is not None:
            sub.append(lower_score(v, g['fcv_MAE'], tol_rel=err_tol_rel))
        else:
            sub.append(0.0)
        # fcv_E_accuracy (higher)
        v = a.get('fcv_E_accuracy')
        if v is not None:
            sub.append(higher_score(v, g['fcv_E_accuracy'], tol_abs=eacc_tol_abs))
        else:
            sub.append(0.0)
        scores.append(sum(sub) / len(sub))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_4 (check id='complete_onehot') ===
def score_4(artifact, step, ctx):
    gold_coll = step['gold']
    err_tol_rel = step.get('error_tol_rel', 0.05)
    all_scores = []
    for dataset_key, gold_list in gold_coll.items():
        agent_list = artifact.get(dataset_key)
        if not isinstance(agent_list, list):
            all_scores.append(0.0)
            continue
        agent_map = {e['model']: e for e in agent_list}
        sub = []
        for g in gold_list:
            a = agent_map.get(g['model'])
            if a is None:
                sub.append(0.0)
                continue
            pair = []
            for k in ['cv_MAE', 'fcv_MAE']:
                v = a.get(k)
                if v is not None:
                    pair.append(lower_score(v, g[k], tol_rel=err_tol_rel))
                else:
                    pair.append(0.0)
            sub.append(sum(pair) / len(pair))
        all_scores.append(sum(sub) / len(sub) if sub else 0.0)
    return sum(all_scores) / len(all_scores) if all_scores else 0.0


# === block: score_5 (check id='structural_checks') ===
def score_5(artifact, step, ctx):
    checks = []
    properties = ['formation_energy', 'band_gap', 'superconducting_Tc']
    for prop in properties:
        mr = artifact.get(prop, {}).get('model_results')
        if not mr:
            checks.append(0.0)
            continue
        for m in mr:
            # FCV MAE must be > CV MAE
            if m.get('fcv_MAE') is not None and m.get('cv_MAE') is not None:
                checks.append(1.0 if m['fcv_MAE'] > m['cv_MAE'] else 0.0)
            else:
                checks.append(0.0)
            # For 1NN-Magpie and RF-Magpie, E_accuracy must be approx 0
            if m['model'] in ('1NN-Magpie', 'RF-Magpie'):
                acc = m.get('fcv_E_accuracy')
                if acc is not None:
                    checks.append(1.0 if abs(acc) < 0.01 else 0.0)
                else:
                    checks.append(0.0)
    if checks:
        return sum(checks) / len(checks)
    return 0.0


_SCORERS = {
    'formation_energy_main': score_0,
    'band_gap_main': score_1,
    'superconducting_Tc_main': score_2,
    'formation_energy_mstep': score_3,
    'complete_onehot': score_4,
    'structural_checks': score_5,
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
