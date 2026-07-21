import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


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
    gold = spec.get('gold', {}) if isinstance(spec, dict) else {}
    g = gold.get('g', 0.02)
    expected_T_U = gold.get('expected_T_U', 3.0)
    T_U_tol_frac = gold.get('T_U_tol_frac', 0.5)
    expected_C_o = gold.get('expected_C_o', 0.002)
    C_o_tol = gold.get('C_o_tol', 0.001)
    return {'g': g, 'expected_T_U': expected_T_U, 'T_U_tol_frac': T_U_tol_frac, 'expected_C_o': expected_C_o, 'C_o_tol': C_o_tol}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    cols = rows[0].keys()
    if 'energy_K' not in cols or 'density' not in cols:
        return 0.0
    try:
        energies = [float(r['energy_K']) for r in rows]
        densities = [float(r['density']) for r in rows]
    except Exception:
        return 0.0
    if any(d < 0 for d in densities):
        return 0.0
    low_thresh = 0.2
    high_thresh = 10.0
    low_dens = [d for e,d in zip(energies, densities) if e <= low_thresh]
    high_dens = [d for e,d in zip(energies, densities) if e >= high_thresh]
    if not high_dens:
        return 0.3
    avg_high = sum(high_dens)/len(high_dens)
    if not low_dens or avg_high == 0:
        return 0.5
    avg_low = sum(low_dens)/len(low_dens)
    ratio = avg_low / avg_high
    if 0.5 <= ratio <= 1.2:
        return 1.0
    else:
        return 0.5


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    cols = rows[0].keys()
    if 'energy_K' not in cols or 'density' not in cols:
        return 0.0
    try:
        energies = [float(r['energy_K']) for r in rows]
        densities = [float(r['density']) for r in rows]
    except Exception:
        return 0.0
    if any(d < 0 for d in densities):
        return 0.0
    # use two reference points: near 10 K and near 1 K
    low_idx = None; high_idx = None
    for i, e in enumerate(energies):
        if e >= 9.5 and e <= 10.5:
            high_idx = i
        if e >= 0.8 and e <= 1.2:
            low_idx = i
    if high_idx is None or low_idx is None:
        return 0.0
    d_high = densities[high_idx]
    d_low = densities[low_idx]
    if d_high == 0:
        return 0.0
    ratio = d_high / d_low if d_low != 0 else float('inf')
    if ratio > 10.0:
        return 1.0
    elif ratio > 5.0:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    g = ctx.get('g', 0.02)
    expected_T_U = ctx.get('expected_T_U', 3.0)
    T_U_tol_frac = ctx.get('T_U_tol_frac', 0.5)
    expected_C_o = ctx.get('expected_C_o', 0.002)
    C_o_tol = ctx.get('C_o_tol', 0.001)
    tau_path = '/app/outputs/dos_tau.csv'
    s_path = '/app/outputs/dos_s.csv'
    if not os.path.exists(tau_path) or not os.path.exists(s_path):
        return 0.0
    def load_dos(path):
        with open(path) as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        e = [float(r['energy_K']) for r in rows]
        d = [float(r['density']) for r in rows]
        idx = sorted(range(len(e)), key=lambda i: e[i])
        e_sorted = [e[i] for i in idx]
        d_sorted = [d[i] for i in idx]
        return e_sorted, d_sorted
    e_tau, d_tau = load_dos(tau_path)
    e_s, d_s = load_dos(s_path)
    def interp(x, xp, fp):
        if x <= xp[0]: return fp[0]
        if x >= xp[-1]: return fp[-1]
        for i in range(len(xp)-1):
            if xp[i] <= x <= xp[i+1]:
                t = (x - xp[i]) / (xp[i+1] - xp[i])
                return fp[i] + t*(fp[i+1] - fp[i])
        return 0.0
    f_vals = []
    for i, e in enumerate(e_tau):
        dt = d_tau[i]
        ds_interp = interp(e, e_s, d_s)
        f = ds_interp - (g**2) * dt
        f_vals.append((e, f))
    T_U_cross = None
    for i in range(len(f_vals)-1):
        if f_vals[i][1] * f_vals[i+1][1] <= 0:
            e1, f1 = f_vals[i]
            e2, f2 = f_vals[i+1]
            if abs(f2 - f1) < 1e-12:
                T_U_cross = e1
            else:
                t = -f1 / (f2 - f1)
                T_U_cross = e1 + t*(e2 - e1)
            break
    if T_U_cross is None:
        if all(f < 0 for _, f in f_vals):
            T_U_cross = e_tau[-1]
        else:
            T_U_cross = e_tau[0]
    if expected_T_U > 0:
        rel_diff = abs(T_U_cross - expected_T_U) / expected_T_U
    else:
        rel_diff = 1.0
    if rel_diff <= T_U_tol_frac:
        score_TU = 1.0
    elif rel_diff <= 1.0:
        score_TU = 0.5
    else:
        score_TU = 0.0
    agent_TU = artifact.get('T_U_K', None) if isinstance(artifact, dict) else None
    if agent_TU is not None and isinstance(agent_TU, (int, float)):
        if expected_T_U > 0:
            rel_diff_agent = abs(agent_TU - expected_T_U) / expected_T_U
        else:
            rel_diff_agent = 1.0
        if rel_diff_agent <= T_U_tol_frac:
            score_agent_TU = 1.0
        elif rel_diff_agent <= 1.0:
            score_agent_TU = 0.5
        else:
            score_agent_TU = 0.0
    else:
        score_agent_TU = 0.0
    agent_Co = artifact.get('C_o', None) if isinstance(artifact, dict) else None
    if agent_Co is not None and isinstance(agent_Co, (int, float)):
        diff = abs(agent_Co - expected_C_o)
        if diff <= C_o_tol:
            score_Co = 1.0
        elif diff <= 2*C_o_tol:
            score_Co = 0.5
        else:
            score_Co = 0.0
    else:
        score_Co = 0.0
    score = 0.4 * score_TU + 0.2 * score_agent_TU + 0.4 * score_Co
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
