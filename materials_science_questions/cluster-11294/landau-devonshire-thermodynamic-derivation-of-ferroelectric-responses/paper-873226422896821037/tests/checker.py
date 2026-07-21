import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    ctx = {}
    ctx['b'] = 0.0254
    ctx['h0'] = 100e-6
    ctx['rho'] = 1000
    ctx['rho_e'] = 1010
    ctx['t_elec'] = 25e-6
    ctx['C10'] = 180.7e3
    ctx['C20'] = -16.7e3
    ctx['C30'] = 6.6e3
    ctx['q0'] = 20e-6 * 10**(80/20)  # 0.2 Pa
    ctx['eps0'] = 8.854187817e-12

    def sigma0(lam):
        I1 = 2*lam**2 + 1.0/lam**4
        S = ctx['C10'] + 2*ctx['C20']*(I1-3) + 3*ctx['C30']*(I1-3)**2
        return 2*(lam**2 - 1/lam**4)*S

    ctx['sigma0_115'] = sigma0(1.15)
    ctx['sigma0_138'] = sigma0(1.38)

    # pre‑compute gold mode shape for λ=1.38
    lam_mode = 1.38
    h = ctx['h0'] / lam_mode**2
    sig = sigma0(lam_mode)
    b = ctx['b']
    q0 = ctx['q0']
    x_gold = np.linspace(0, 1, 200)

    def disp_hat(x, y):
        total = 0.0
        for m in range(1, 52, 2):
            for n in range(1, 52, 2):
                total += np.sin(m*np.pi*x) * np.sin(n*np.pi*y) / (m*n*(m**2 + n**2))
        return total

    y_gold_raw = np.array([disp_hat(x, 0.5) for x in x_gold])
    ctx['mode_x_gold'] = x_gold
    ctx['mode_y_gold'] = y_gold_raw / np.max(y_gold_raw)
    return ctx


# === block: score_0 (check id='center_displacement') ===
def score_0(artifact, step, ctx):
    import math
    tol = 0.05
    scores = []
    for row in artifact:
        lam = float(row['prestretch'])
        agent_disp = float(row['displacement_nm'])
        # recompute expected displacement
        I1 = 2*lam**2 + 1.0/lam**4
        S = ctx['C10'] + 2*ctx['C20']*(I1-3) + 3*ctx['C30']*(I1-3)**2
        sigma0_val = 2*(lam**2 - 1/lam**4)*S
        h = ctx['h0'] / lam**2
        total = 0.0
        for m in range(1, 52, 2):
            for n in range(1, 52, 2):
                total += 1.0/(m*n*(m**2 + n**2))
        prefactor = 16.0 / np.pi**4 * ctx['q0'] * ctx['b']**2 / (sigma0_val * h)
        expected = prefactor * total * 1e9
        rel_err = abs(agent_disp - expected) / expected
        scores.append(1.0 if rel_err <= tol else 0.0)
    if len(scores) == 0:
        return 0.0
    return float(sum(scores)) / len(scores)


# === block: score_1 (check id='mode_shape') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    x_agent = np.array([float(r['x_norm']) for r in artifact])
    y_agent = np.array([float(r['displacement_norm']) for r in artifact])
    if np.any(x_agent < 0) or np.any(x_agent > 1):
        return 0.0
    idx = np.argsort(x_agent)
    x_agent = x_agent[idx]
    y_agent = y_agent[idx]
    y_interp = np.interp(ctx['mode_x_gold'], x_agent, y_agent)
    rmse = np.sqrt(np.mean((y_interp - ctx['mode_y_gold'])**2))
    return 1.0 if rmse <= 0.1 else 0.0


# === block: score_2 (check id='resonance_frequencies') ===
def score_2(artifact, step, ctx):
    import math
    tol = 0.02
    scores = []
    for row in artifact:
        lam = float(row['prestretch'])
        with_elec = str(row['with_electrode']).strip().lower() in ('true','1','yes')
        agent_freq = float(row['frequency_Hz'])
        I1 = 2*lam**2 + 1.0/lam**4
        S = ctx['C10'] + 2*ctx['C20']*(I1-3) + 3*ctx['C30']*(I1-3)**2
        sigma0_val = 2*(lam**2 - 1/lam**4)*S
        h = ctx['h0'] / lam**2
        M_aM = 1.3785 * ctx['rho'] * h / ctx['b']**2
        C_aM = 0.0351 * ctx['b']**4 / (sigma0_val * h)
        M_aRad = 1.486 * ctx['b'] * ctx['rho'] / (2 * ctx['b']**2)
        M_aE = 0.0
        if with_elec:
            M_aE = 1.3785 * ctx['rho_e'] * ctx['t_elec'] / ctx['b']**2
        total_mass = M_aM + M_aRad + M_aE
        expected = 1.0 / (2*math.pi * math.sqrt(total_mass * C_aM))
        rel_err = abs(agent_freq - expected) / expected
        scores.append(1.0 if rel_err <= tol else 0.0)
    if len(scores) == 0:
        return 0.0
    return float(sum(scores)) / len(scores)


# === block: score_3 (check id='voltage_dependence') ===
def score_3(artifact, step, ctx):
    import math
    tol = 0.05
    scores = []
    for row in artifact:
        lam = float(row['prestretch'])
        V_kV = float(row['voltage_kV'])
        agent_norm = float(row['normalized_frequency'])
        I1 = 2*lam**2 + 1.0/lam**4
        S = ctx['C10'] + 2*ctx['C20']*(I1-3) + 3*ctx['C30']*(I1-3)**2
        sigma0_val = 2*(lam**2 - 1/lam**4)*S
        epsr = -0.28 * lam + 2.76
        V = V_kV * 1000
        sigma_V = sigma0_val - ctx['eps0'] * epsr * (lam**2 * V / ctx['h0'])**2
        if sigma_V <= 0:
            expected = 0.0
        else:
            expected = math.sqrt(sigma_V / sigma0_val)
        scores.append(1.0 if abs(agent_norm - expected) <= tol else 0.0)
    if len(scores) == 0:
        return 0.0
    return float(sum(scores)) / len(scores)


_SCORERS = {
    'center_displacement': score_0,
    'mode_shape': score_1,
    'resonance_frequencies': score_2,
    'voltage_dependence': score_3,
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
