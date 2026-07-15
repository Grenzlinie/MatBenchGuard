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
    return {}


# === block: score_0 (check id='step_04') ===
def score_0(artifact, step, ctx):
    import numpy as np

    Lambda0 = 250e-6
    Dn_eff0 = 0.0062
    Delta_lambda0 = 39.6e-9
    N1 = 100
    N2 = 100
    sigma_Lambda = 0.01e-6
    sigma_Dn = 1e-6
    deltaT = 1.0

    dn_vals = [0.0, 1e-6, -1e-6, 3e-6, -3e-6]
    m_vals = list(range(-10, 11))

    wavelength_nm = np.linspace(1510, 1590, 8001)
    lambda_arr = wavelength_nm * 1e-9

    def compute_deltaI(dn, m, lambda_arr):
        dT1 = -m * deltaT
        dT2 = m * deltaT
        Lambda1 = Lambda0 + sigma_Lambda * dT1
        Lambda2 = Lambda0 + sigma_Lambda * dT2
        L1 = N1 * Lambda1
        L2 = N2 * Lambda2
        Dn1 = Dn_eff0 - dn + sigma_Dn * dT1
        Dn2 = Dn_eff0 + dn + sigma_Dn * dT2
        I_dB = np.zeros_like(lambda_arr)
        for i, lam in enumerate(lambda_arr):
            delta1 = np.pi * (Dn1 / lam - 1.0 / Lambda1)
            delta2 = np.pi * (Dn2 / lam - 1.0 / Lambda2)
            kappa1 = (Delta_lambda0 / lam**2) * Dn1
            kappa2 = (Delta_lambda0 / lam**2) * Dn2
            dbeta1 = 2.0 * np.sqrt(delta1**2 + kappa1**2)
            C1 = np.cos(dbeta1 * L1)
            S1 = np.sin(dbeta1 * L1)
            Delta1 = 2.0 * delta1 / dbeta1 if dbeta1 != 0 else 2.0
            K1 = 2.0 * kappa1 / dbeta1 if dbeta1 != 0 else 0.0
            dbeta2 = 2.0 * np.sqrt(delta2**2 + kappa2**2)
            C2 = np.cos(dbeta2 * L2)
            S2 = np.sin(dbeta2 * L2)
            Delta2 = 2.0 * delta2 / dbeta2 if dbeta2 != 0 else 2.0
            K2 = 2.0 * kappa2 / dbeta2 if dbeta2 != 0 else 0.0
            A_core = (C1 * C2 - (Delta1 * Delta2 + K1 * K2) * S1 * S2
                      + 1j * (Delta1 * S1 * C2 + Delta2 * C1 * S2))
            I = np.abs(A_core)**2
            I_dB[i] = 10.0 * np.log10(max(I, 1e-15))
        I_m = np.min(I_dB)
        return I_m

    gold = {}
    for dn in dn_vals:
        I_m0 = compute_deltaI(dn, 0, lambda_arr)
        for m in m_vals:
            I_m = compute_deltaI(dn, m, lambda_arr)
            gold[(dn, m)] = I_m - I_m0

    agent_delta = {}
    for row in artifact:
        dn = float(row["dn"])
        m = int(row["m"])
        val = float(row["DeltaI_m"])
        agent_delta[(dn, m)] = val

    tol_db = 0.5
    scores_pt = []
    for (dn, m), gold_val in gold.items():
        if (dn, m) not in agent_delta:
            scores_pt.append(0.0)
            continue
        agent_val = agent_delta[(dn, m)]
        diff = abs(agent_val - gold_val)
        if diff <= tol_db:
            s = 1.0
        elif diff <= 2 * tol_db:
            s = max(0.0, 1.0 - (diff - tol_db) / tol_db)
        else:
            s = 0.0
        scores_pt.append(s)
    pt_score = np.mean(scores_pt) if scores_pt else 0.0

    sym_scores = []
    dn0 = 0.0
    if (dn0, 0) in agent_delta:
        for m in range(1, 11):
            if (dn0, m) in agent_delta and (dn0, -m) in agent_delta:
                asym = abs(agent_delta[(dn0, m)] - agent_delta[(dn0, -m)])
                if asym <= 0.2:
                    sym_scores.append(1.0)
                elif asym <= 0.5:
                    sym_scores.append(max(0.0, 1.0 - (asym - 0.2) / 0.3))
                else:
                    sym_scores.append(0.0)
            else:
                sym_scores.append(0.0)
    sym_score = np.mean(sym_scores) if sym_scores else 0.0

    offset_scores = []
    for dn in dn_vals:
        if dn == 0.0:
            continue
        gold_curve = {m: gold[(dn, m)] for m in m_vals}
        agent_curve = {m: agent_delta.get((dn, m), None) for m in m_vals}
        try:
            m_gold = min(gold_curve, key=lambda k: gold_curve[k])
            m_agent = min(agent_curve, key=lambda k: agent_curve[k] if agent_curve[k] is not None else float('inf'))
            offset_diff = abs(m_agent - m_gold)
            off_score = max(0.0, 1.0 - offset_diff / 3.0)
        except Exception:
            off_score = 0.0
        offset_scores.append(off_score)
    offset_score = np.mean(offset_scores) if offset_scores else 0.0

    total_score = 0.7 * pt_score + 0.15 * sym_score + 0.15 * offset_score
    return total_score


_SCORERS = {
    'step_04': score_0,
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
