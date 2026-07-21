import os
import json
import csv

# === author imports / helpers ===
from collections import defaultdict


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


# === block: score_0 (check id='structure_electronic') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerances']
    stab_req = step['stability_required']
    systems = list(gold.keys())
    total_checks = len(systems) * 3
    passed = 0
    for sys in systems:
        if sys not in artifact:
            continue
        d = artifact[sys]
        if 'lattice_constant_angstrom' in d:
            diff = abs(d['lattice_constant_angstrom'] - gold[sys]['lattice_constant_angstrom'])
            if diff <= tol['lattice_constant_angstrom']:
                passed += 1
        if 'band_gap_eV' in d and d['band_gap_eV'] is not None:
            diff = abs(d['band_gap_eV'] - gold[sys]['band_gap_eV'])
            if diff <= tol['band_gap_eV']:
                passed += 1
        if 'dynamically_stable' in d and d['dynamically_stable'] == stab_req:
            passed += 1
    return passed / total_checks


# === block: score_1 (check id='transport_properties') ===
def score_1(artifact, step, ctx):
    req = step['requirements']
    systems_list = req['systems']
    expected_temps = req['temperatures']
    data = defaultdict(list)
    for row in artifact:
        if not row:
            continue
        sys = row.get('System', '')
        try:
            T = int(row.get('Temperature_K', -1))
        except:
            continue
        sigma = float(row.get('sigma_over_tau', 0))
        kappa = float(row.get('kappa_over_tau', 0))
        see = float(row.get('Seebeck_V_per_K', 0))
        zt = float(row.get('ZT', 0))
        data[sys].append((T, sigma, kappa, see, zt))

    # 1. format & shape (0.10)
    shape_score = 0.0
    if all(sys in data for sys in systems_list):
        all_ok = True
        for sys in systems_list:
            temps_in_file = sorted([t[0] for t in data[sys]])
            if temps_in_file != expected_temps:
                all_ok = False
                break
        if all_ok:
            shape_score = 1.0

    # 2. ZT internal consistency (0.10)
    zt_cons_score = 0.0
    total_diffs = 0.0
    n_pts = 0
    for sys in systems_list:
        for (T, sigma, kappa, see, zt) in data[sys]:
            if kappa == 0:
                continue
            zt_calc = (see**2 * sigma * T) / kappa
            diff = abs(zt_calc - zt)
            total_diffs += diff
            n_pts += 1
    if n_pts > 0:
        mean_diff = total_diffs / n_pts
        if mean_diff < 1e-8:
            zt_cons_score = 1.0
        else:
            zt_cons_score = max(0.0, 1.0 - mean_diff * 1e6)

    # 3. trend checks (0.15)
    trend_score = 0.0
    see_pos = all(all(row[3] > 0 for row in data[sys]) for sys in systems_list if sys in data)
    sig_dec = True
    for sys in systems_list:
        if sys not in data:
            sig_dec = False
            break
        sig_50 = next((s for t,s,_,_,_ in data[sys] if t==50), None)
        sig_1200 = next((s for t,s,_,_,_ in data[sys] if t==1200), None)
        if sig_50 is None or sig_1200 is None or sig_50 <= sig_1200:
            sig_dec = False
            break
    kap_inc = True
    for sys in systems_list:
        if sys not in data:
            kap_inc = False
            break
        kap_50 = next((k for t,_,k,_,_ in data[sys] if t==50), None)
        kap_1200 = next((k for t,_,k,_,_ in data[sys] if t==1200), None)
        if kap_50 is None or kap_1200 is None or kap_50 >= kap_1200:
            kap_inc = False
            break
    trend_score = (1.0 if see_pos else 0.0)*0.4 + (1.0 if sig_dec else 0.0)*0.3 + (1.0 if kap_inc else 0.0)*0.3

    # 4. monolayer CaS peak (0.15)
    cas_peak_score = 0.0
    if 'CaS_monolayer' in data:
        zt_vals = [zt for (T,_,_,_,_,zt) in data['CaS_monolayer']]
        max_zt = max(zt_vals) if zt_vals else 0
        zt_1200 = None
        for (T,_,_,_,_,zt) in data['CaS_monolayer']:
            if T == 1200:
                zt_1200 = zt
                break
        if max_zt >= req['trends']['monolayer_CaS_peak_gt']:
            cas_peak_score += 0.6
        if zt_1200 is not None and max_zt > zt_1200:
            cas_peak_score += 0.4

    # 5. monolayer CaSe peak (0.15)
    case_peak_score = 0.0
    if 'CaSe_monolayer' in data:
        zt_vals = [zt for (T,_,_,_,_,zt) in data['CaSe_monolayer']]
        max_zt = max(zt_vals) if zt_vals else 0
        zt_1200 = None
        for (T,_,_,_,_,zt) in data['CaSe_monolayer']:
            if T == 1200:
                zt_1200 = zt
                break
        if max_zt >= req['trends']['monolayer_CaSe_peak_gt']:
            case_peak_score += 0.6
        if zt_1200 is not None and max_zt > zt_1200:
            case_peak_score += 0.4

    # 6. bilayer CaS ZT range 300-1200 (0.15)
    bil_zt_range_score = 0.0
    if 'CaS_bilayer' in data:
        temps_in_range = [t for t in req['temperatures'] if 300 <= t <= 1200]
        zt_pair = [(T, zt) for (T,_,_,_,_,zt) in data['CaS_bilayer'] if T in temps_in_range]
        lo, hi = req['trends']['bilayer_CaS_ZT_range_300_1200']
        in_range = sum(1 for (T,zt) in zt_pair if lo <= zt <= hi)
        total = len(zt_pair)
        if total > 0:
            bil_zt_range_score = in_range / total

    # 7. hybrid CaS/CaSe ZT range 500-1200 (0.20)
    hyb_zt_range_score = 0.0
    if 'CaS_CaSe_hybrid' in data:
        temps_in_range = [t for t in req['temperatures'] if 500 <= t <= 1200]
        zt_pair = [(T, zt) for (T,_,_,_,_,zt) in data['CaS_CaSe_hybrid'] if T in temps_in_range]
        lo, hi = req['trends']['hybrid_CaS_CaSe_ZT_range_500_1200']
        in_range = sum(1 for (T,zt) in zt_pair if lo <= zt <= hi)
        total = len(zt_pair)
        if total > 0:
            hyb_zt_range_score = in_range / total

    total = (0.10 * shape_score +
             0.10 * zt_cons_score +
             0.15 * trend_score +
             0.15 * cas_peak_score +
             0.15 * case_peak_score +
             0.15 * bil_zt_range_score +
             0.20 * hyb_zt_range_score)
    return total


_SCORERS = {
    'structure_electronic': score_0,
    'transport_properties': score_1,
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
