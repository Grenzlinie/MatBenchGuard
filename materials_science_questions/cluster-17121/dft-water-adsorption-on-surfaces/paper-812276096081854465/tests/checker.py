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


# === block: score_0 (check id='relaxed_bulk_cell') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tols = step['tolerances']
    params = [('a', 'a_abs'), ('b', 'b_abs'), ('c', 'c_abs'), ('alpha', 'alpha_abs'), ('beta', 'beta_abs'), ('gamma', 'gamma_abs')]
    correct = 0
    for param, tol_key in params:
        if param in artifact:
            if abs(artifact[param] - gold[param]) <= tols[tol_key]:
                correct += 1
    return correct / len(params)


# === block: score_1 (check id='surface_adsorption_energies') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    se_rel = step['se_tolerance_rel']
    se_abs = step['se_small_abs']
    ae_rel = step['ae_tolerance_rel']
    ae_abs = step['ae_small_abs']
    numeric_w = step['numeric_weight']
    trend_w = step['trend_weight']
    SE_fields = ['SE_P', 'SE_W', 'SE_H', 'SE_M', 'SE_A']
    AE_fields = ['AE_W', 'AE_H', 'AE_M', 'AE_A']
    total = 0
    ok = 0
    for surf in ['100','001','102']:
        if surf not in artifact:
            continue
        g = gold.get(surf, {})
        a = artifact[surf]
        for f in SE_fields:
            total += 1
            if f in a and f in g:
                ref = g[f]
                val = a[f]
                tol = se_rel * max(abs(ref), 0.01) if abs(ref) > 0.01 else se_abs
                if abs(val - ref) <= tol:
                    ok += 1
        for f in AE_fields:
            total += 1
            if f in a and f in g:
                ref = g[f]
                val = a[f]
                tol = ae_rel * max(abs(ref), 0.1) if abs(ref) > 0.1 else ae_abs
                if abs(val - ref) <= tol:
                    ok += 1
    numeric_score = ok / max(total, 1)

    trend_score = 1.0
    try:
        se_p = {s: artifact[s]['SE_P'] for s in ['100','001','102']}
        if not (se_p['100'] < se_p['102'] < se_p['001']):
            trend_score -= 0.25
    except:
        trend_score -= 0.25
    try:
        ae_h = {(s): artifact[s]['AE_H'] for s in ['100','102']}
        ae_a_001 = artifact['001']['AE_A']
        ae_w_100 = artifact['100']['AE_W']; ae_m_100 = artifact['100']['AE_M']; ae_a_100 = artifact['100']['AE_A']
        ae_w_102 = artifact['102']['AE_W']; ae_m_102 = artifact['102']['AE_M']; ae_a_102 = artifact['102']['AE_A']
        # most negative AE on {100} and {102} should be AE_H
        if not (ae_h['100'] < ae_w_100 and ae_h['100'] < ae_m_100 and ae_h['100'] < ae_a_100):
            trend_score -= 0.25
        if not (ae_h['102'] < ae_w_102 and ae_h['102'] < ae_m_102 and ae_h['102'] < ae_a_102):
            trend_score -= 0.25
        # most negative on {001} should be AE_A
        ae_w_001 = artifact['001']['AE_W']; ae_h_001 = artifact['001']['AE_H']; ae_m_001 = artifact['001']['AE_M']
        if not (ae_a_001 < ae_w_001 and ae_a_001 < ae_h_001 and ae_a_001 < ae_m_001):
            trend_score -= 0.25
    except:
        trend_score -= 0.25
    trend_score = max(0.0, trend_score)
    return numeric_w * numeric_score + trend_w * trend_score


_SCORERS = {
    'relaxed_bulk_cell': score_0,
    'surface_adsorption_energies': score_1,
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
