import os
import json
import csv

# === author imports / helpers ===
import csv, math, json, os


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
    return {'spec': spec, 'output_dir': outputs_dir}


# === block: score_0 (check id='check_nucleation') ===
def score_0(artifact, step, ctx):
    row = artifact[0]
    r = float(row['r_crit_m'])
    u = float(row['undercooling_K'])

    # Accept any critical radius in the typical nucleation range (0.1 nm to 100 nm)
    r_ok = 1.0 if 1e-10 <= r <= 1e-7 else 0.0
    # Accept undercooling within the range the paper associates with stable droplet formation (1–10 K)
    u_ok = 1.0 if 1.0 <= u <= 10.0 else 0.0

    score = 0.5 * r_ok + 0.5 * u_ok
    return score


# === block: score_1 (check id='check_heat_transfer') ===
def score_1(artifact, step, ctx):
    # read agent's undercooling from nucleation.csv
    nuc_path = os.path.join(ctx['output_dir'], 'nucleation.csv')
    with open(nuc_path, newline='') as f:
        reader = csv.DictReader(f)
        nuc_row = next(reader)
        undercooling = float(nuc_row['undercooling_K'])

    # model parameters from step
    p = step['params']
    f = p['f']
    f1phi = p['f_one_minus_phi']
    H = p['H']
    K_raw = p['K_mh_per_kcal']
    T = p['T_K']
    P = p['P_Pa']
    s = p['s_J_per_kg']
    R_v = p['R_J_per_kgK']

    alpha_p = f * s * s * P / ( (2*math.pi)**0.5 * (R_v*T)**1.5 * T )
    one_minus_phi = f1phi / f
    alpha = alpha_p * one_minus_phi
    K_SI = K_raw / 1.163  # convert m·h/kcal -> m·K/W (1 kcal/h = 1.163 W)

    pointwise_ok = 0
    total_points = 0
    peak_alpha = -1.0
    peak_delta = None
    tol = step['tolerance_rel_pointwise']

    for row in artifact:
        dT = float(row['Delta_T_K'])
        am = float(row['alpha_m_W_m2K'])
        if dT < undercooling - 1e-12:
            expected_am = 0.0
        else:
            factor = 1.0 - K_SI * H * alpha_p * dT
            if factor < 0.0:
                factor = 0.0
            expected_am = alpha * factor
        denom = max(expected_am, 1e-9)
        rel_err = abs(am - expected_am) / denom
        if rel_err <= tol:
            pointwise_ok += 1
        total_points += 1
        if dT >= undercooling - 1e-12 and am > peak_alpha:
            peak_alpha = am
            peak_delta = dT

    pct = pointwise_ok / total_points if total_points > 0 else 0.0
    peak_score = 0.0
    if peak_delta is not None:
        lo, hi = step['peak_delta_T_range_K']
        if lo <= peak_delta <= hi:
            peak_score = 1.0
    w_pt = step['scoring']['pointwise_weight']
    w_peak = step['scoring']['peak_weight']
    score = w_pt * pct + w_peak * peak_score
    return score


_SCORERS = {
    'check_nucleation': score_0,
    'check_heat_transfer': score_1,
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
