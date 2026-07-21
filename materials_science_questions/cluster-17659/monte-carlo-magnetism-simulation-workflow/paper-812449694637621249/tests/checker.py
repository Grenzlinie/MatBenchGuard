import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import solve_ivp


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


# === block: score_0 (check id='mc_ce') ===
def score_0(artifact, step, ctx):
    import numpy as np

    def score_mc_ce(artifact, step, ctx):
        if 'eta_T' not in artifact or artifact['eta_T'] is None:
            return 0.0
        eta_T = float(artifact['eta_T'])
        gold = float(step.get('gold_eta_T', 1.515))
        win = float(step.get('tolerance_win', 0.1))
        score_eta = max(0.0, 1.0 - abs(eta_T - gold) / win)
        fvals = artifact.get('f_values', [])
        if isinstance(fvals, list) and len(fvals) > 1:
            mono = all((fvals[i-1] >= fvals[i] - 1e-6) for i in range(1, len(fvals)))
        else:
            mono = False
        score_mono = 1.0 if mono else 0.0
        return 0.9 * score_eta + 0.1 * score_mono


# === block: score_1 (check id='mc_mce') ===
def score_1(artifact, step, ctx):
    import numpy as np

    def score_mc_mce(artifact, step, ctx):
        if 'eta_MC' not in artifact or artifact['eta_MC'] is None:
            return 0.0
        eta_MC = float(artifact['eta_MC'])
        gold = float(step.get('gold_eta_MC', 1.33))
        win = float(step.get('tolerance_win', 0.1))
        return max(0.0, 1.0 - abs(eta_MC - gold) / win)


# === block: score_2 (check id='mf_ode') ===
def score_2(artifact, step, ctx):
    import numpy as np
    from scipy.integrate import solve_ivp

    def score_mf_ode(artifact, step, ctx):
        eta_vals = np.array(artifact.get('etaR_values', []), dtype=float)
        f_agent = np.array(artifact.get('f_MF_values', []), dtype=float)
        if len(eta_vals) == 0 or len(eta_vals) != len(f_agent):
            return 0.0
        # ODE rhs for df/deta
        def ode(eta, f):
            denom = eta * (3.0*f - 1.0)
            if abs(denom) < 1e-30:
                return 0.0
            return -(3.0*f - 3.0 + eta) * f / denom
        # small-eta initial condition from series expansion
        eta0 = 1e-6
        f0 = 1.0 - eta0/5.0 - eta0**2/175.0
        gold_etaC = float(step.get('gold_etaC_R', 2.517551))
        # integrate to max(agent eta, gold etaC) but compare only up to gold etaC
        t_end = max(np.max(eta_vals), gold_etaC + 0.1)
        sol = solve_ivp(ode, [eta0, t_end], [f0], method='RK45', dense_output=True, rtol=1e-10, atol=1e-14)
        if not sol.success:
            return 0.0
        # evaluate reference at agent's eta values, mask to eta <= gold_etaC
        valid_mask = eta_vals <= gold_etaC + 1e-6
        if not np.any(valid_mask):
            return 0.0
        f_ref = sol.sol(eta_vals[valid_mask])[0]
        rmse = np.sqrt(np.mean((f_agent[valid_mask] - f_ref)**2))
        score_rmse = 1.0 if rmse < 1e-4 else max(0.0, 1.0 - rmse / 0.01)
        # check reported etaC_R
        if 'etaC_R' in artifact and artifact['etaC_R'] is not None:
            etaC_R = float(artifact['etaC_R'])
            tol_win = float(step.get('tolerance_win_etaC', 0.01))
            score_etaC = max(0.0, 1.0 - abs(etaC_R - gold_etaC) / tol_win)
        else:
            score_etaC = 0.0
        return 0.7 * score_rmse + 0.3 * score_etaC


_SCORERS = {
    'mc_ce': score_0,
    'mc_mce': score_1,
    'mf_ode': score_2,
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
