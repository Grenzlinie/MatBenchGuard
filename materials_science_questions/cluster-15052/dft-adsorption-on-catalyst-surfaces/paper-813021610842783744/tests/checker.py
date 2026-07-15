import os
import json
import csv

# === author imports / helpers ===
import os, csv, re, math


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
    out_dir = outputs_dir
    return {'out_dir': out_dir}


# === block: score_0 (check id='step3_adsorption') ===
def score_0(artifact, step, ctx):
    rows = [row for row in artifact if row.get('surface','').strip() in ['IrO2','PtO2','CrO2']]
    tol = step['parameters']['tolerances']
    exp = step['parameters']['expected']
    # map surfaces
    surf_map = {r['surface'].strip(): r for r in rows}
    numeric_hits = 0
    n_checks = 5 * 3
    for surf in exp:
        row = surf_map.get(surf)
        if row is None:
            continue
        for field in ['E_ad','CH4_charge','E_a','E_r','ICOHP']:
            col = None
            for c in row:
                if field in c:
                    col = c
                    break
            if col is None:
                continue
            try:
                val = float(row[col])
            except:
                continue
            if abs(val - exp[surf][field]) <= tol[field]:
                numeric_hits += 1
    numeric_score = numeric_hits / n_checks if n_checks else 0

    # trend checks
    trend_score = 0.0
    try:
        # E_ad magnitude: CrO2 < PtO2 < IrO2
        col_ad = [c for c in rows[0] if 'E_ad' in c][0]
        ads = {s: abs(float(surf_map[s][col_ad])) for s in exp}
        if ads['CrO2'] < ads['PtO2'] < ads['IrO2']:
            trend_score += 0.25
        # E_a: PtO2 < IrO2 < CrO2
        col_ea = [c for c in rows[0] if 'E_a' in c][0]
        ea = {s: float(surf_map[s][col_ea]) for s in exp}
        if ea['PtO2'] < ea['IrO2'] < ea['CrO2']:
            trend_score += 0.25
        # charge: CrO2 < IrO2 < PtO2
        col_ch = [c for c in rows[0] if 'CH4_charge' in c][0]
        ch = {s: float(surf_map[s][col_ch]) for s in exp}
        if ch['CrO2'] < ch['IrO2'] < ch['PtO2']:
            trend_score += 0.25
        # ICOHP (more negative stronger): PtO2 < IrO2 < CrO2
        col_ic = [c for c in rows[0] if 'ICOHP' in c][0]
        ic = {s: float(surf_map[s][col_ic]) for s in exp}
        if ic['PtO2'] < ic['IrO2'] < ic['CrO2']:
            trend_score += 0.25
    except:
        trend_score = 0.0

    return 0.5 * numeric_score + 0.5 * trend_score


# === block: score_1 (check id='step4_pcohp_curve') ===
def score_1(artifact, step, ctx):
    path = os.path.join(ctx['out_dir'], 'pCOHP_IrO2_CH.csv')
    if not os.path.exists(path):
        return 0.0
    energies = []
    neg_pcohp = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue
            try:
                energies.append(float(row[0]))
                neg_pcohp.append(float(row[1]))
            except:
                continue
    if not energies:
        return 0.0
    # structural checks
    params = step['parameters']
    occ_height_thr = params['occupied_bonding_min_height']
    unocc_height_thr = params['unoccupied_bonding_min_height']
    win_lo, win_hi = params['energy_window']
    energy_min, energy_max = params['energy_range_min'], params['energy_range_max']

    score = 0.0
    # occupied bonding peak below E_F
    occ_vals = [v for e,v in zip(energies, neg_pcohp) if e < 0]
    if occ_vals and max(occ_vals) >= occ_height_thr:
        score += 0.4
    # unoccupied bonding peak in window
    win_vals = [v for e,v in zip(energies, neg_pcohp) if win_lo <= e <= win_hi]
    if win_vals and max(win_vals) >= unocc_height_thr:
        score += 0.3
    # energy range coverage
    if min(energies) <= energy_min and max(energies) >= energy_max:
        score += 0.2
    # bonus for overall peak > 1.0
    if max(neg_pcohp) >= 1.0:
        score += 0.1
    return min(score, 1.0)


# === block: score_2 (check id='step5_pcohp_peak') ===
def score_2(artifact, step, ctx):
    text = artifact
    pattern = r'Occupied bonding peak at (-?\d+\.?\d*) eV; Unoccupied bonding peak at (-?\d+\.?\d*) eV'
    m = re.search(pattern, text)
    if not m:
        return 0.0
    occ = float(m.group(1))
    unocc = float(m.group(2))
    exp_occ = step['parameters'].get('expected_occupied')
    exp_unocc = step['parameters'].get('expected_unoccupied')
    tol = step['parameters'].get('tolerance', 0.25)
    score = 0.0
    if exp_occ is not None and abs(occ - exp_occ) <= tol:
        score += 0.5
    if exp_unocc is not None and abs(unocc - exp_unocc) <= tol:
        score += 0.5
    return score


_SCORERS = {
    'step3_adsorption': score_0,
    'step4_pcohp_curve': score_1,
    'step5_pcohp_peak': score_2,
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
