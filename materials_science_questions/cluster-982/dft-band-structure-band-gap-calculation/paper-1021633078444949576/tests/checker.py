import os
import json
import csv

# === author imports / helpers ===
import json, math, os


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
    gold = spec.get('hidden_gold', {})
    return {'gold': gold}


# === block: score_0 (check id='optimized_zt') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    artifact = artifact   # the loaded dict
    def zt_score(agent_zt, paper_zt):
        threshold = 0.85 * paper_zt
        if agent_zt >= threshold:
            return 1.0
        lower = 0.5 * paper_zt
        if agent_zt <= lower:
            return 0.0
        return (agent_zt - lower) / (threshold - lower)
    def other_score(agent_val, gold_val):
        if gold_val == 0:
            return 1.0 if agent_val == 0 else 0.0
        rel_err = abs(agent_val - gold_val) / abs(gold_val)
        if rel_err <= 0.2:
            return 1.0
        if rel_err >= 0.5:
            return 0.0
        return 1.0 - (rel_err - 0.2) / 0.3
    scores = []
    weights_cond = {'ZT': 0.6, 'other': 0.4}
    for mat in gold:
        for doping in gold[mat]:
            for temp in gold[mat][doping]:
                g = gold[mat][doping][temp]
                a = artifact.get(mat, {}).get(doping, {}).get(temp, None)
                if a is None:
                    scores.append(0.0)
                    continue
                zt_s = zt_score(a.get('ZT', 0), g['ZT'])
                s_s = other_score(abs(a.get('Seebeck_coeff_muV_K', 0)), g['S'])
                sigma_s = other_score(a.get('electrical_cond_Ohm_m', 0), g['sigma'])
                pf_s = other_score(a.get('power_factor_W_mK2_e-3', 0), g['PF'])
                ke_s = other_score(a.get('electronic_thermal_cond_W_mK', 0), g['kappa_e'])
                kl_s = other_score(a.get('lattice_thermal_cond_W_mK', 0), g['kappa_l'])
                n_s = other_score(a.get('carrier_concentration_cm2', 0), g['n'])
                other_sum = s_s + sigma_s + pf_s + ke_s + kl_s + n_s
                other_avg = other_sum / 6.0
                cond_score = 0.6 * zt_s + 0.4 * other_avg
                scores.append(cond_score)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'optimized_zt': score_0,
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
