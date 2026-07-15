import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math


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
    steps = spec.get('steps', [])
    ctx = {}
    for s in steps:
        s_id = s.get('id','')
        if 'gold' in s:
            ctx[s_id + '_gold'] = s['gold']
        if 'expected_sign' in s:
            ctx[s_id + '_sign'] = s['expected_sign']
        if 'tolerance_kcal_mol' in s:
            ctx[s_id + '_tol'] = s['tolerance_kcal_mol']
        if 'ref_C_N' in s:
            ctx[s_id + '_ref'] = {
                'C_N': s['ref_C_N'],
                'C_O': s['ref_C_O'],
                'O_H': s['ref_O_H'],
                'Fe_LS': s['ref_Fe_LS_C_N'],
                'Fe_HS': s['ref_Fe_HS_C_N'],
                'pct': s['percent_tolerance']
            }
        if 'min_M_N' in s:
            ctx[s_id + '_geom'] = {
                'min_M_N': s['min_M_N'],
                'max_M_N': s['max_M_N'],
                'max_delta': s['max_delta_axial']
            }
        if 'expected_complexes' in s:
            ctx[s_id + '_exp_comps'] = s['expected_complexes']
            ctx[s_id + '_lhe_tol'] = s.get('lhe_tolerance', 0.01)
    return ctx


# === block: score_0 (check id='step_03_relative_energies') ===
def score_0(artifact, step, ctx):
    gold = ctx.get(step['id'] + '_gold', {})
    tol = ctx.get(step['id'] + '_tol', 1.5)
    rows = artifact
    ok = 0
    total = 0
    for r in rows:
        c = r.get('complex','').strip()
        if c in gold and r.get('functional','').strip().upper() == 'B3LYP':
            val = float(r.get('relative_energy_kcal_mol', 'inf'))
            if abs(val - gold[c]) <= tol:
                ok += 1
            total += 1
    return ok / total if total > 0 else 0.0


# === block: score_1 (check id='step_04_deltae_hs_ls') ===
def score_1(artifact, step, ctx):
    sign_map = ctx.get(step['id'] + '_sign', {})
    rows = artifact
    ok = 0
    total = 0
    for r in rows:
        c = r.get('complex','').strip()
        if c in sign_map and r.get('functional','').strip().upper() == 'B3LYP':
            try:
                val = float(r.get('deltae_hs_ls_kcal_mol','inf'))
                expected = sign_map[c]
                if (expected == 'positive' and val > 0) or (expected == 'negative' and val < 0):
                    ok += 1
                total += 1
            except:
                total += 1
    return ok / total if total > 0 else 0.0


# === block: score_2 (check id='step_05_harmonic_frequencies') ===
def score_2(artifact, step, ctx):
    ref = ctx.get(step['id'] + '_ref', {})
    tol = ref.get('pct', 5) / 100.0
    checks = []
    for r in artifact:
        c = r.get('complex','').strip()
        spin = r.get('spin','').strip().upper()
        func = r.get('functional','').strip().upper()
        if c == '1' and spin == 'LS' and func == 'B3LYP':
            try:
                cn = float(r['freq_C_N'])
                co = float(r['freq_C_O'])
                oh = float(r['freq_O_H'])
                checks.append(1.0 if abs(cn - ref['C_N'])/ref['C_N'] <= tol else 0.0)
                checks.append(1.0 if abs(co - ref['C_O'])/ref['C_O'] <= tol else 0.0)
                checks.append(1.0 if abs(oh - ref['O_H'])/ref['O_H'] <= tol else 0.0)
            except:
                pass
        elif c == '4' and func == 'B3LYP':
            try:
                cn = float(r['freq_C_N'])
                if spin == 'LS':
                    checks.append(1.0 if abs(cn - ref['Fe_LS'])/ref['Fe_LS'] <= tol else 0.0)
                    # will later compare LS > HS
                    row_ls_cn = cn
                elif spin == 'HS':
                    checks.append(1.0 if abs(cn - ref['Fe_HS'])/ref['Fe_HS'] <= tol else 0.0)
                    row_hs_cn = cn
            except:
                pass
    # trend check for complex 4: LS C-N > HS C-N
    ls_vals = [float(r['freq_C_N']) for r in artifact if r.get('complex','').strip()=='4' and r.get('spin','').strip().upper()=='LS' and r.get('functional','').strip().upper()=='B3LYP']
    hs_vals = [float(r['freq_C_N']) for r in artifact if r.get('complex','').strip()=='4' and r.get('spin','').strip().upper()=='HS' and r.get('functional','').strip().upper()=='B3LYP']
    if ls_vals and hs_vals and ls_vals[0] > hs_vals[0]:
        checks.append(1.0)
    else:
        checks.append(0.0)
    return sum(checks) / max(len(checks), 1) if checks else 0.0


# === block: score_3 (check id='step_06_geometry_bond_lengths') ===
def score_3(artifact, step, ctx):
    params = ctx.get(step['id'] + '_geom', {})
    min_mn = params.get('min_M_N', 1.8)
    max_mn = params.get('max_M_N', 2.5)
    max_delta = params.get('max_delta', 0.5)
    rows = artifact
    valid = 0
    total = 0
    for r in rows:
        try:
            mn = float(r['M_N_avg_basal'])
            e1 = float(r['M_E1'])
            e2 = float(r['M_E2'])
            if (min_mn <= mn <= max_mn) and e1 > 0 and e2 > 0 and abs(e1 - e2) <= max_delta:
                valid += 1
            total += 1
        except:
            total += 1
    return valid / total if total > 0 else 0.0


# === block: score_4 (check id='step_07_absorption_spectra') ===
def score_4(artifact, step, ctx):
    expected = ctx.get(step['id'] + '_exp_comps', [])
    lhe_tol = ctx.get(step['id'] + '_lhe_tol', 0.01)
    rows = artifact
    # group by complex
    by_cpx = {}
    for r in rows:
        c = r.get('complex','').strip()
        if c not in by_cpx:
            by_cpx[c] = []
        by_cpx[c].append(r)
    checks = []
    for c in expected:
        if c not in by_cpx:
            checks.append(0.0)
            continue
        group = by_cpx[c]
        # find row with max oscillator_strength
        max_f = -1.0
        best_row = None
        for r in group:
            try:
                f = float(r['oscillator_strength'])
                if f > max_f:
                    max_f = f
                    best_row = r
            except:
                pass
        if best_row is None or max_f <= 0:
            checks.append(0.0)
            continue
        # recompute LHE
        try:
            lhs_reported = float(best_row.get('LHE_max', -1))
            lhs_calc = 1 - 10**(-max_f)
            if lhs_reported >= 0 and abs(lhs_reported - lhs_calc) <= lhe_tol:
                checks.append(1.0)
            else:
                checks.append(0.0)
        except:
            checks.append(0.0)
    return sum(checks) / len(expected) if expected else 0.0


_SCORERS = {
    'step_03_relative_energies': score_0,
    'step_04_deltae_hs_ls': score_1,
    'step_05_harmonic_frequencies': score_2,
    'step_06_geometry_bond_lengths': score_3,
    'step_07_absorption_spectra': score_4,
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
