import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os, bisect


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
    return {"spec": spec}


# === block: score_0 (check id='step_01_undoped_dos') ===
def score_0(artifact, step, ctx):
    # Load DOS CSV
    rows = artifact  # already list of dicts with Energy_Ry, Total_DOS_states_per_Ry_cell
    energies = [float(r['Energy_Ry']) for r in rows]
    dos = [float(r['Total_DOS_states_per_Ry_cell']) for r in rows]
    # Find index closest to E=0
    idx = min(range(len(energies)), key=lambda i: abs(energies[i]-0.0))
    n_ef = dos[idx]
    gold = step['gold_N_EF']
    tol = step['tolerance_rel']
    rel_err = abs(n_ef - gold) / gold if gold != 0 else abs(n_ef)
    score_nef = max(0.0, min(1.0, 1.0 - (rel_err - tol) / tol)) if rel_err > tol else 1.0
    # Shoulder check: average slope in (0, +0.005 Ry) should be positive and larger than slope on ( -0.005, 0)
    pos_indices = [i for i, e in enumerate(energies) if 0.0 < e < 0.005]
    neg_indices = [i for i, e in enumerate(energies) if -0.005 < e < 0.0]
    def slope(indices):
        if len(indices) < 2: return 0.0
        x = [energies[i] for i in indices]
        y = [dos[i] for i in indices]
        n = len(x)
        sx = sy = sxx = sxy = 0.0
        for xi, yi in zip(x, y):
            sx += xi; sy += yi; sxx += xi*xi; sxy += xi*yi
        denom = n*sxx - sx*sx
        if denom == 0: return 0.0
        return (n*sxy - sx*sy) / denom
    slope_pos = slope(pos_indices)
    slope_neg = slope(neg_indices)
    shoulder_ok = 1.0 if (slope_pos > 0 and slope_pos > slope_neg) else 0.0
    # Combine: weight 0.7 for N_EF, 0.3 for shoulder
    score = 0.7 * score_nef + 0.3 * shoulder_ok
    return score


# === block: score_1 (check id='step_02_doped_dos_a670') ===
def score_1(artifact, step, ctx):
    rows = artifact
    energies = [float(r['Energy_Ry']) for r in rows]
    dos = [float(r['Total_DOS_states_per_Ry_cell']) for r in rows]
    idx = min(range(len(energies)), key=lambda i: abs(energies[i]-0.0))
    n_ef = dos[idx]
    gold = step['gold_N_EF']
    tol = step['tolerance_rel']
    rel_err = abs(n_ef - gold) / gold if gold != 0 else abs(n_ef)
    if rel_err <= tol: return 1.0
    return max(0.0, 1.0 - (rel_err - tol) / tol)


# === block: score_2 (check id='step_03_doped_dos_a667') ===
def score_2(artifact, step, ctx):
    rows = artifact
    energies = [float(r['Energy_Ry']) for r in rows]
    dos = [float(r['Total_DOS_states_per_Ry_cell']) for r in rows]
    idx = min(range(len(energies)), key=lambda i: abs(energies[i]-0.0))
    n_ef = dos[idx]
    gold = step['gold_N_EF']
    tol = step['tolerance_rel']
    rel_err = abs(n_ef - gold) / gold if gold != 0 else abs(n_ef)
    if rel_err <= tol: return 1.0
    return max(0.0, 1.0 - (rel_err - tol) / tol)


# === block: score_3 (check id='step_04_doped_dos_a653') ===
def score_3(artifact, step, ctx):
    rows = artifact
    energies = [float(r['Energy_Ry']) for r in rows]
    dos = [float(r['Total_DOS_states_per_Ry_cell']) for r in rows]
    idx = min(range(len(energies)), key=lambda i: abs(energies[i]-0.0))
    n_ef = dos[idx]
    gold = step['gold_N_EF']
    tol = step['tolerance_rel']
    rel_err = abs(n_ef - gold) / gold if gold != 0 else abs(n_ef)
    if rel_err <= tol: return 1.0
    return max(0.0, 1.0 - (rel_err - tol) / tol)


# === block: score_4 (check id='step_05_projected_dos') ===
def score_4(artifact, step, ctx):
    rows = artifact
    gold_rows = step['gold_rows']
    tol = step['tolerance_rel']
    scores = []
    for gold in gold_rows:
        a0 = gold['a0']
        site = gold['site']
        target = gold['N_EF_states_per_Ry_atom']
        # Find matching row in artifact
        match = None
        for row in rows:
            try:
                if float(row['a0']) == a0 and row['site'] == site:
                    match = row
                    break
            except:
                continue
        if match is None:
            scores.append(0.0)
            continue
        try:
            val = float(match['N_EF_states_per_Ry_atom'])
        except:
            scores.append(0.0)
            continue
        rel_err = abs(val - target) / target if target != 0 else abs(val)
        if rel_err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (rel_err - tol) / tol))
    if not scores: return 0.0
    return sum(scores) / len(scores)


# === block: score_5 (check id='step_06_derived_properties') ===
def score_5(artifact, step, ctx):
    rows = artifact
    gold_rows = step['gold_rows']
    tolerances = step['tolerances']
    mu = step.get('mu_star', 0.13)
    internal_weight = step.get('internal_consistency_weight', 0.1)
    scores = []
    for gold in gold_rows:
        a0 = gold['a0']
        match = None
        for row in rows:
            try:
                if abs(float(row['a0']) - a0) < 0.001:
                    match = row
                    break
            except:
                continue
        if match is None:
            scores.append(0.0)
            continue
        sub_scores = []
        # check lambda
        try:
            lam = float(match['lambda'])
        except:
            lam = None
        if lam is not None and gold['lambda'] != 0:
            rel = abs(lam - gold['lambda']) / gold['lambda']
            tol = tolerances['lambda_rel']
            sub = 1.0 if rel <= tol else max(0.0, 1.0 - (rel - tol) / tol)
            sub_scores.append(sub)
        else:
            sub_scores.append(0.0)
        # check Tc
        try:
            tc = float(match['Tc_K'])
        except:
            tc = None
        if tc is not None:
            if gold['Tc_K'] == 0.0:
                sub = 1.0 if abs(tc) < tolerances['Tc_abs_min'] else max(0.0, 1.0 - abs(tc) / tolerances['Tc_abs_min'])
            else:
                rel = abs(tc - gold['Tc_K']) / gold['Tc_K']
                tol = tolerances['Tc_rel']
                sub = 1.0 if rel <= tol else max(0.0, 1.0 - (rel - tol) / tol)
            sub_scores.append(sub)
        else:
            sub_scores.append(0.0)
        # check Stoner
        try:
            s = float(match['Stoner_S'])
        except:
            s = None
        if s is not None and gold['Stoner_S'] != 0:
            rel = abs(s - gold['Stoner_S']) / gold['Stoner_S']
            tol = tolerances['Stoner_rel']
            sub = 1.0 if rel <= tol else max(0.0, 1.0 - (rel - tol) / tol)
            sub_scores.append(sub)
        else:
            sub_scores.append(0.0)
        # check gamma
        try:
            gamma = float(match['gamma_mJ_per_mol_K2'])
        except:
            gamma = None
        if gamma is not None and gold['gamma_mJ_per_mol_K2'] != 0:
            rel = abs(gamma - gold['gamma_mJ_per_mol_K2']) / gold['gamma_mJ_per_mol_K2']
            tol = tolerances['gamma_rel']
            sub = 1.0 if rel <= tol else max(0.0, 1.0 - (rel - tol) / tol)
            sub_scores.append(sub)
        else:
            sub_scores.append(0.0)
        # check N_EF_total
        try:
            nef = float(match['N_EF_total_states_per_Ry_cell'])
        except:
            nef = None
        if nef is not None and gold['N_EF_total_states_per_Ry_cell'] != 0:
            rel = abs(nef - gold['N_EF_total_states_per_Ry_cell']) / gold['N_EF_total_states_per_Ry_cell']
            tol = tolerances['N_EF_rel']
            sub = 1.0 if rel <= tol else max(0.0, 1.0 - (rel - tol) / tol)
            sub_scores.append(sub)
        else:
            sub_scores.append(0.0)
        # internal consistency: compute Tc from lambda and theta_D
        if lam is not None and gold.get('theta_D') is not None:
            theta = gold['theta_D']
            try:
                exp_arg = -1.04 * (1+lam) / (lam - mu*(1+0.62*lam))
                tc_pred = (theta / 1.45) * math.exp(exp_arg)
                tc_report = float(match['Tc_K']) if tc is not None else None
                if tc_report is not None:
                    # generous tolerance on derived Tc: allow 10 K or 100% relative
                    if gold['Tc_K'] == 0:
                        sub_int = 1.0 if abs(tc_report - tc_pred) < 2.0 else max(0.0, 1.0 - abs(tc_report - tc_pred)/4.0)
                    else:
                        diff = abs(tc_report - tc_pred)
                        sub_int = 1.0 if diff < max(2.0, 0.5*gold['Tc_K']) else max(0.0, 1.0 - diff/(4*max(1.0,gold['Tc_K'])))
                else:
                    sub_int = 0.0
            except:
                sub_int = 0.0
        else:
            sub_int = 0.0
        sub_scores_avg = sum(sub_scores) / len(sub_scores) if sub_scores else 0.0
        combined = (1.0 - internal_weight) * sub_scores_avg + internal_weight * sub_int
        scores.append(combined)
    if not scores: return 0.0
    return sum(scores) / len(scores)


# === block: score_6 (check id='step_07_trends') ===
def score_6(artifact, step, ctx):
    # Load derived table and a653 DOS curve
    outdir = os.path.join('/app','outputs')
    def load_csv(fname):
        path = os.path.join(outdir, fname)
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    rows_derived = load_csv('derived_properties_table.csv')
    rows_a653 = load_csv('total_dos_doped_a653.csv')
    # Parse derived rows into dict by a0
    data = {}
    for r in rows_derived:
        try:
            a = float(r['a0'])
        except:
            continue
        data[a] = {
            'lambda': float(r.get('lambda', 0)),
            'Tc_K': float(r.get('Tc_K', 0)),
            'Stoner_S': float(r.get('Stoner_S', 0)),
            'gamma': float(r.get('gamma_mJ_per_mol_K2', 0)),
            'N_EF': float(r.get('N_EF_total_states_per_Ry_cell', 0))
        }
    required_a = [6.7, 6.67, 6.53]
    def monotonic_decreasing(values):
        # return 1.0 if strictly decreasing, else 0.0
        for i in range(len(values)-1):
            if values[i] <= values[i+1]: return 0.0
        return 1.0
    score_trends = 0.0
    count = 0
    for key in ['N_EF', 'lambda', 'Tc_K', 'Stoner_S', 'gamma']:
        vals = []
        for a in required_a:
            if a in data:
                vals.append(data[a][key])
        if len(vals) == 3:
            score_trends += monotonic_decreasing(vals)
            count += 1
    if count:
        score_trends /= count
    # Check peak position for a653: DOS max should be at E > 0
    energies_653 = [float(r['Energy_Ry']) for r in rows_a653]
    dos_653 = [float(r['Total_DOS_states_per_Ry_cell']) for r in rows_a653]
    max_idx = max(range(len(dos_653)), key=lambda i: dos_653[i])
    peak_e = energies_653[max_idx]
    peak_above_ef = 1.0 if peak_e > 0.0 else 0.0
    # Combine trend and peak check
    return 0.7 * score_trends + 0.3 * peak_above_ef


_SCORERS = {
    'step_01_undoped_dos': score_0,
    'step_02_doped_dos_a670': score_1,
    'step_03_doped_dos_a667': score_2,
    'step_04_doped_dos_a653': score_3,
    'step_05_projected_dos': score_4,
    'step_06_derived_properties': score_5,
    'step_07_trends': score_6,
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
