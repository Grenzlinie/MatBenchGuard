import os
import json
import csv

# === author imports / helpers ===
import os, csv, bisect, json


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


# === block: score_0 (check id='step_kcl_512_te') ===
def score_0(artifact, step, ctx):
    hidden = step['hidden_gold_te']
    tol = step['temperature_tolerance_K']
    ref_sorted = sorted(hidden, key=lambda x: x[0])
    agent_pts = [(float(r['total_energy_kJ_mol']), float(r['temperature_K'])) for r in artifact]
    if not agent_pts:
        return 0.0
    ref_e = [p[0] for p in ref_sorted]
    matched = 0
    for e, t in agent_pts:
        idx = bisect.bisect_left(ref_e, e)
        cand = []
        if idx < len(ref_sorted):
            cand.append(ref_sorted[idx])
        if idx > 0:
            cand.append(ref_sorted[idx-1])
        best = min(cand, key=lambda p: abs(p[0] - e))
        if abs(best[1] - t) <= tol:
            matched += 1
    return matched / len(agent_pts)


# === block: score_1 (check id='step_kcl_5832_te') ===
def score_1(artifact, step, ctx):
    hidden = step['hidden_gold_te']
    tol = step['temperature_tolerance_K']
    ref_sorted = sorted(hidden, key=lambda x: x[0])
    agent_pts = [(float(r['total_energy_kJ_mol']), float(r['temperature_K'])) for r in artifact]
    if not agent_pts:
        return 0.0
    ref_e = [p[0] for p in ref_sorted]
    matched = 0
    for e, t in agent_pts:
        idx = bisect.bisect_left(ref_e, e)
        cand = []
        if idx < len(ref_sorted):
            cand.append(ref_sorted[idx])
        if idx > 0:
            cand.append(ref_sorted[idx-1])
        best = min(cand, key=lambda p: abs(p[0] - e))
        if abs(best[1] - t) <= tol:
            matched += 1
    return matched / len(agent_pts)


# === block: score_2 (check id='step_kcl_5832_liq_frac') ===
def score_2(artifact, step, ctx):
    points = [(float(r['total_energy_kJ_mol']), float(r['liquid_mole_fraction'])) for r in artifact]
    if not points:
        return 0.0
    points.sort()
    energies, fracs = zip(*points)
    # structural: range and monotonicity (allow small flips)
    all_ok = all(-0.05 <= f <= 1.05 for f in fracs)
    mono = all(fracs[i] >= fracs[i-1] - 0.005 for i in range(1, len(fracs)))
    struct_score = 0.3 if (all_ok and mono) else (0.15 if all_ok or mono else 0.0)
    # linear region: fraction between 0.1 and 0.9
    linear = [(e, f) for e, f in zip(energies, fracs) if 0.1 <= f <= 0.9]
    if len(linear) < 3:
        return struct_score
    sum_e = sum(e for e, f in linear)
    sum_f = sum(f for e, f in linear)
    sum_ef = sum(e*f for e, f in linear)
    sum_e2 = sum(e*e for e, f in linear)
    n = len(linear)
    den = n*sum_e2 - sum_e*sum_e
    if abs(den) < 1e-12:
        return struct_score
    slope = (n*sum_ef - sum_e*sum_f) / den
    if slope == 0:
        return struct_score
    intercept = (sum_f - slope*sum_e)/n
    e0 = -intercept/slope
    e1 = (1 - intercept)/slope
    vacf_enthalpy = abs(e1 - e0)
    target = step['gold_vacf_enthalpy_kJ_mol']
    tol = step['vacf_enthalpy_tolerance_kJ_mol']
    if abs(vacf_enthalpy - target) <= tol:
        main_score = 1.0
    else:
        main_score = max(0.0, 1.0 - (abs(vacf_enthalpy - target) - tol) / (2*tol))
    return struct_score*0.3 + main_score*0.7


# === block: score_3 (check id='step_results_json') ===
def score_3(artifact, step, ctx):
    expected = ['melting_temperature_K', 'enthalpy_direct_kJ_mol', 'enthalpy_vacf_kJ_mol']
    if not all(k in artifact for k in expected):
        return 0.0
    # result-level gold comparison
    def score_val(val, gold, tol):
        if abs(val - gold) <= tol:
            return 1.0
        return max(0.0, 1.0 - (abs(val - gold) - tol) / (2*tol))
    s_melt_g = score_val(float(artifact['melting_temperature_K']), step['gold_melting_temperature_K'], step['melting_temp_tolerance_K'])
    s_direct_g = score_val(float(artifact['enthalpy_direct_kJ_mol']), step['gold_enthalpy_direct_kJ_mol'], step['enthalpy_direct_tolerance_kJ_mol'])
    s_vacf_g = score_val(float(artifact['enthalpy_vacf_kJ_mol']), step['gold_enthalpy_vacf_kJ_mol'], step['enthalpy_vacf_tolerance_kJ_mol'])
    # consistency: recompute melting temperature from raw TE and fraction data
    try:
        te_path = '/app/outputs/kcl_5832_te.csv'
        frac_path = '/app/outputs/kcl_5832_liq_mol_frac.csv'
        if not os.path.exists(te_path) or not os.path.exists(frac_path):
            raise Exception('missing raw data')
        with open(te_path, newline='') as f:
            te_rows = list(csv.DictReader(f))
        with open(frac_path, newline='') as f:
            frac_rows = list(csv.DictReader(f))
        te = [(float(r['total_energy_kJ_mol']), float(r['temperature_K'])) for r in te_rows]
        frac = [(float(r['total_energy_kJ_mol']), float(r['liquid_mole_fraction'])) for r in frac_rows]
        te.sort()
        frac.sort()
        # Filter energies where fraction between 0.2 and 0.8
        frac_energies = [e for e, f in frac if 0.2 <= f <= 0.8]
        if not frac_energies:
            raise Exception('no coexistence energies')
        e_min = min(frac_energies)
        e_max = max(frac_energies)
        # Temperatures from TE in that range
        temps = [t for e, t in te if e_min <= e <= e_max]
        if not temps:
            raise Exception('no te points in coexistence range')
        recomputed_melt = sum(temps)/len(temps)
        cons_melt_tol = step.get('consistency_melting_temp_tol_K', 5.0)
        cons_melt = 1.0 if abs(recomputed_melt - float(artifact['melting_temperature_K'])) <= cons_melt_tol else 0.0
        # recompute VACF enthalpy from fraction (same as previous step) -> consistency with reported
        # reuse linear fit code
        frac_pts = [(e,f) for e,f in frac]
        linear_frac = [(e,f) for e,f in frac_pts if 0.1 <= f <= 0.9]
        if len(linear_frac) >= 3:
            sum_e = sum(e for e,f in linear_frac)
            sum_f = sum(f for e,f in linear_frac)
            sum_ef = sum(e*f for e,f in linear_frac)
            sum_e2 = sum(e*e for e,f in linear_frac)
            n = len(linear_frac)
            den = n*sum_e2 - sum_e*sum_e
            if abs(den) > 1e-12:
                slope = (n*sum_ef - sum_e*sum_f)/den
                intercept = (sum_f - slope*sum_e)/n
                if slope != 0:
                    e0 = -intercept/slope
                    e1 = (1 - intercept)/slope
                    recomputed_vacf = abs(e1 - e0)
                    cons_vacf = 1.0 if abs(recomputed_vacf - float(artifact['enthalpy_vacf_kJ_mol'])) <= step.get('consistency_vacf_enthalpy_tol_kJ_mol', 2.0) else 0.0
                else:
                    cons_vacf = 0.0
            else:
                cons_vacf = 0.0
        else:
            cons_vacf = 0.0
        cons_score = cons_melt*0.5 + cons_vacf*0.5
    except Exception as e:
        cons_score = 0.0
    # combine: 0.5 gold, 0.5 consistency (if available)
    final = (s_melt_g*0.2 + s_direct_g*0.2 + s_vacf_g*0.2) + cons_score*0.4
    return min(1.0, max(0.0, final))


_SCORERS = {
    'step_kcl_512_te': score_0,
    'step_kcl_5832_te': score_1,
    'step_kcl_5832_liq_frac': score_2,
    'step_results_json': score_3,
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
