import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
from scipy.interpolate import interp1d


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
    import os, csv
    cs_path = os.path.join(outputs_dir, 'step_02_free_energy.csv')
    if not os.path.exists(cs_path):
        return {'tk': None, 'tc': None, 'tau_nuc_comp': None, 'tau_eq_comp': 4460.0}
    with open(cs_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    T = np.array([float(r['T']) for r in rows])
    S = np.array([float(r['S_config']) for r in rows])
    FL = np.array([float(r['F_LQ']) for r in rows])
    FR = np.array([float(r['F_CR']) for r in rows])

    # Find T_K where S_config crosses zero, linear interpolation
    idx = np.where(np.diff(np.sign(S)) != 0)[0]
    if len(idx) == 0:
        tk = None
    else:
        i = idx[0]
        if S[i] == 0:
            tk = T[i]
        else:
            slope = (S[i+1] - S[i]) / (T[i+1] - T[i])
            tk = T[i] - S[i] / slope

    # Find T_c where F_LQ == F_CR
    dF = FL - FR
    idx_c = np.where(np.diff(np.sign(dF)) != 0)[0]
    if len(idx_c) == 0:
        tc = None
    else:
        i = idx_c[0]
        if dF[i] == 0:
            tc = T[i]
        else:
            slope = (dF[i+1] - dF[i]) / (T[i+1] - T[i])
            tc = T[i] - dF[i] / slope

    ctx = {'tk': tk, 'tc': tc, 'tau_eq_comp': 20.0 * 2.23 / (3.40 - 3.39)}

    # Recompute tau_nuc(3.40) only if tk and tc are found
    if tk is not None and tc is not None and tk < 3.40 and tc > 3.40:
        deltaF350 = 0.5 * (tc - 3.50)
        deltaF340 = 0.5 * (tc - 3.40)
        T350 = 3.50
        T340 = 3.40
        # geometric constant C = 4A^3 / (27 B^2) with A=4π, B=4π/3
        C = (16.0/3.0) * math.pi
        # Back out σ^3 from τ_nuc(3.50)=1e25 (assuming τ0=1)
        E350 = math.log(1e25)
        sigma3_350 = E350 * deltaF350**2 * T350 / C
        sigma350 = sigma3_350 ** (1/3)
        # Renormalized scaling: σ ∝ (T - T_K)^{1/2}
        sigma340 = sigma350 * ((T340 - tk) / (T350 - tk)) ** 0.5
        sigma3_340 = sigma340**3
        E340 = C * sigma3_340 / (deltaF340**2 * T340)
        tau_nuc_340 = math.exp(E340)
        ctx['tau_nuc_comp'] = tau_nuc_340
    else:
        ctx['tau_nuc_comp'] = None
    return ctx


# === block: score_0 (check id='step_03_shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    if 'TK' not in artifact or 'units' not in artifact:
        return 0.0
    tk = artifact['TK']
    if not isinstance(tk, (int, float)):
        return 0.0
    return 1.0


# === block: score_1 (check id='recompute_TK') ===
def score_1(artifact, step, ctx):
    if ctx.get('tk') is None:
        return 0.0
    target = 3.18
    tol = 0.05
    error = abs(ctx['tk'] - target)
    if error <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (error - tol) / tol)  # reaches 0 at 2*tol


# === block: score_2 (check id='step_05_shape') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    if 'T' not in artifact or 'tau_nuc' not in artifact or 'units' not in artifact:
        return 0.0
    t = artifact['T']
    tau = artifact['tau_nuc']
    if not isinstance(t, (int, float)) or not isinstance(tau, (int, float)):
        return 0.0
    if abs(t - 3.40) > 0.01:
        return 0.0  # T must be 3.40
    return 1.0


# === block: score_3 (check id='recompute_tau_nuc') ===
def score_3(artifact, step, ctx):
    if ctx.get('tau_nuc_comp') is None:
        return 0.0
    ref = 4600.0
    rel_tol = 0.05
    comp = ctx['tau_nuc_comp']
    error = abs(comp - ref) / ref
    if error <= rel_tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (error - rel_tol) / (rel_tol * 2))  # reaches 0 at 3*rel_tol? let’s use decay to 0 at 0.15


# === block: score_4 (check id='step_06_shape') ===
def score_4(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    required = ['T', 'tau_eq', 'tau_nuc', 'T_sp']
    if any(k not in artifact for k in required):
        return 0.0
    t = artifact['T']
    tsp = artifact['T_sp']
    if abs(t - 3.40) > 0.01:
        return 0.0
    if abs(tsp - 3.40) > 0.01:
        return 0.0
    return 1.0


# === block: score_5 (check id='recompute_crossing') ===
def score_5(artifact, step, ctx):
    tau_eq_comp = 20.0 * 2.23 / (3.40 - 3.39)  # 4460
    if ctx.get('tau_nuc_comp') is None:
        return 0.0
    tau_nuc_comp = ctx['tau_nuc_comp']
    art = artifact
    tau_eq_art = float(art.get('tau_eq', 0))
    tau_nuc_art = float(art.get('tau_nuc', 0))
    tsp = float(art.get('T_sp', 0))

    # tau_eq score
    e_eq = abs(tau_eq_art - tau_eq_comp) / tau_eq_comp
    if e_eq <= 0.05:
        s_eq = 1.0
    else:
        s_eq = max(0.0, 1.0 - (e_eq - 0.05) / 0.10)

    # tau_nuc score
    e_nuc = abs(tau_nuc_art - tau_nuc_comp) / tau_nuc_comp
    if e_nuc <= 0.05:
        s_nuc = 1.0
    else:
        s_nuc = max(0.0, 1.0 - (e_nuc - 0.05) / 0.10)

    # T_sp must be exactly 3.40
    s_tsp = 1.0 if abs(tsp - 3.40) < 0.01 else 0.0

    return (s_eq + s_nuc + s_tsp) / 3.0


_SCORERS = {
    'step_03_shape': score_0,
    'recompute_TK': score_1,
    'step_05_shape': score_2,
    'recompute_tau_nuc': score_3,
    'step_06_shape': score_4,
    'recompute_crossing': score_5,
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
