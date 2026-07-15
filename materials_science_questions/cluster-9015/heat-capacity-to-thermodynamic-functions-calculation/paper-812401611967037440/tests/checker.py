import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os

def load_json(path):
    with open(path) as f:
        return json.load(f)
def load_csv_dict(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


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
    return {
        'k_B': 1.380649e-23,
        'b_geo': 16.0 * math.pi / 3.0,
        'f_min': 0.1,
        'f_max': 0.9,
        'T_upper': 1490.0,
        'ref_rate': 20.0
    }


# === block: score_0 (check id='kinetic_params') ===
def score_0(artifact, step, ctx):
    import math
    ref = step.get('reference', {})
    tol = step.get('relative_tolerances', {})
    fields = [('ln_A3', 'ln_A3'), ('Q_over_k', 'Q_over_k'), ('b_sigma3_f_over_4k', 'b_sigma3_f_over_4k')]
    field_scores = []
    for key, fname in fields:
        val = artifact.get(fname)
        if val is None:
            field_scores.append(0.0)
            continue
        ref_val = ref.get(key)
        if ref_val is None or ref_val == 0:
            field_scores.append(0.0)
            continue
        rel_err = abs(val - ref_val) / abs(ref_val)
        t = tol.get(key, 0.1)
        if rel_err <= t:
            field_scores.append(1.0)
        else:
            field_scores.append(max(0.0, 1.0 - (rel_err - t) / t))
    return sum(field_scores) / len(field_scores) if field_scores else 0.0


# === block: score_1 (check id='interfacial_energy') ===
def score_1(artifact, step, ctx):
    import math
    kin_path = '/app/outputs/kinetic_parameters.json'
    if not os.path.exists(kin_path):
        return 0.0
    try:
        kin = load_json(kin_path)
    except Exception:
        return 0.0
    term = kin.get('b_sigma3_f_over_4k')
    if term is None or term <= 0:
        return 0.0
    k_B = ctx['k_B']
    b_geo = ctx['b_geo']
    f_min = ctx['f_min']
    f_max = ctx['f_max']
    factor = 4.0 * k_B * term
    sigma_min_exp = (factor / (b_geo * f_max)) ** (1.0/3.0)
    sigma_max_exp = (factor / (b_geo * f_min)) ** (1.0/3.0)
    sigma_min_agent = artifact.get('sigma_min')
    sigma_max_agent = artifact.get('sigma_max')
    if sigma_min_agent is None or sigma_max_agent is None:
        return 0.0
    tol_rel = step.get('relative_tolerance', 0.05)
    def field_score(agent_val, exp_val):
        if exp_val == 0:
            return 1.0 if agent_val == 0 else 0.0
        rel_err = abs(agent_val - exp_val) / exp_val
        if rel_err <= tol_rel:
            return 1.0
        return max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)
    s_min = field_score(sigma_min_agent, sigma_min_exp)
    s_max = field_score(sigma_max_agent, sigma_max_exp)
    return (s_min + s_max) / 2.0


# === block: score_2 (check id='critical_cooling_rate') ===
def score_2(artifact, step, ctx):
    ttt_path = '/app/outputs/ttt_curve.csv'
    if not os.path.exists(ttt_path):
        return 0.0
    try:
        rows = load_csv_dict(ttt_path)
    except Exception:
        return 0.0
    if len(rows) < 2:
        return 0.0
    try:
        pairs = []
        for row in rows:
            T = float(row.get('T', math.nan))
            t = float(row.get('t', math.nan))
            if not math.isnan(T) and not math.isnan(t) and t > 0:
                pairs.append((T, t))
    except Exception:
        return 0.0
    if not pairs:
        return 0.0
    # Find nose (minimum time)
    min_pair = min(pairs, key=lambda x: x[1])
    T_nose, t_nose = min_pair
    T_upper = ctx['T_upper']
    R_c = (T_upper - T_nose) / t_nose
    ref_rate = step.get('reference_rate', ctx['ref_rate'])
    if R_c >= ref_rate:
        return 1.0
    else:
        return max(0.0, 1.0 - (ref_rate - R_c) / ref_rate)


_SCORERS = {
    'kinetic_params': score_0,
    'interfacial_energy': score_1,
    'critical_cooling_rate': score_2,
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
