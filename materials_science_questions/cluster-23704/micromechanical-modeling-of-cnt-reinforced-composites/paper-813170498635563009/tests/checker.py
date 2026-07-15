import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    step = spec['steps'][0]
    gold = { (r['chirality'], r['functional_group'], r['concentration']): r for r in step['gold_rows'] }
    ctx = {
        'gold': gold,
        'radius_tol': step['tolerance_radius_rel'],
        'modulus_tol': step['tolerance_modulus_rel'],
        'metal_chirality': step['metal_transition_group'],
        'metal_func': step['metal_transition_func'],
        'metal_conc': step['metal_threshold_concentration']
    }
    return ctx


# === block: score_0 (check id='overall_score') ===
def score_0(artifact, step, ctx):
    rows = artifact
    ctx_gold = ctx['gold']
    radius_tol = ctx['radius_tol']
    modulus_tol = ctx['modulus_tol']
    metal_chir = ctx['metal_chirality']
    metal_func = ctx['metal_func']
    metal_conc = ctx['metal_conc']

    agent = {}
    for r in rows:
        key = (r['chirality'], r['functional_group'], float(r['concentration']))
        agent[key] = r

    groups_trend = {}
    for key in ctx_gold:
        chir, func, conc = key
        if func == 'pristine':
            continue
        groups_trend.setdefault((chir, func), []).append(conc)

    num_conditions = len(groups_trend) * 2
    satisfied = 0
    for (chir, func), concs in groups_trend.items():
        if len(concs) < 2:
            continue
        sorted_concs = sorted(concs)
        rad_vals = []
        mod_vals = []
        valid = True
        for c in sorted_concs:
            k = (chir, func, c)
            if k not in agent:
                valid = False
                break
            rad_vals.append(float(agent[k]['radius_A']))
            mod_vals.append(float(agent[k]['young_modulus_TPa']))
        if not valid:
            continue
        if all(rad_vals[i+1] >= rad_vals[i] for i in range(len(rad_vals)-1)):
            satisfied += 1
        if all(mod_vals[i+1] <= mod_vals[i] for i in range(len(mod_vals)-1)):
            satisfied += 1
    trend_score = satisfied / max(1, num_conditions) if num_conditions > 0 else 1.0

    tot_err = 0.0
    cnt = 0
    for key, gold in ctx_gold.items():
        if key not in agent:
            continue
        arow = agent[key]
        r_err = abs(float(arow['radius_A']) - gold['radius_A']) / gold['radius_A']
        r_contrib = max(0.0, 1.0 - r_err / radius_tol)
        m_err = abs(float(arow['young_modulus_TPa']) - gold['young_modulus_TPa']) / gold['young_modulus_TPa']
        m_contrib = max(0.0, 1.0 - m_err / modulus_tol)
        tot_err += (r_contrib + m_contrib) / 2.0
        cnt += 1
    error_score = tot_err / max(1, cnt) if cnt > 0 else 0.0

    bg_score = 0.0
    metal_key = (metal_chir, metal_func, metal_conc)
    if metal_key in agent:
        gap = float(agent[metal_key]['band_gap_eV'])
        if gap <= 1e-6:
            bg_score = 1.0
    overall = 0.5 * trend_score + 0.3 * error_score + 0.2 * bg_score
    return max(0.0, min(1.0, overall))


_SCORERS = {
    'overall_score': score_0,
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
