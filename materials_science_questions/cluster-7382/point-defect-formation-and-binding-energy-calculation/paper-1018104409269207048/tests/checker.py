import os
import json
import csv

# === author imports / helpers ===
import math


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
    diff_params = {}
    diff_tol = {}
    mono_check = False
    mixed_check = False
    mixed_tol_log10 = 0.5
    act_gold = {}
    for step in spec.get('steps', []):
        if step['id'] == 'step_01_diffusion':
            diff_params = step.get('model_params', {})
            diff_tol = step.get('tolerance', {'D_gt_1e-7': {'relative': 0.50}, 'D_le_1e-7': {'log10_abs': 0.5}})
            mono_check = step.get('monotonicity_check', False)
            mixed_check = step.get('mixed_oxide_equivalence_check', False)
            mixed_tol_log10 = step.get('mixed_oxide_tolerance_log10', 0.5)
        elif step['id'] == 'step_02_activation':
            act_gold = step
    return {'diff_params': diff_params, 'diff_tol': diff_tol, 'mono_check': mono_check,
            'mixed_check': mixed_check, 'mixed_tol_log10': mixed_tol_log10, 'act_gold': act_gold}


# === block: score_0 (check id='step_01_diffusion') ===
def score_0(artifact, step, ctx):
    k_B = 8.617333262145e-5

    def expected_D(comp_params, T):
        E_II = comp_params['E_II']
        D0_II = comp_params['D0_II']
        E_I = comp_params['E_I']
        D0_I = comp_params['D0_I']
        E_sup = comp_params['E_sup']
        D0_sup = comp_params['D0_sup']
        T_II_I = comp_params['T_II_I']
        T_I_sup = comp_params['T_I_sup']
        if T <= T_II_I:
            return D0_II * math.exp(-E_II/(k_B*T))
        elif T <= T_I_sup:
            return D0_I * math.exp(-E_I/(k_B*T))
        else:
            return D0_sup * math.exp(-E_sup/(k_B*T))

    params = ctx['diff_params']
    tol = ctx['diff_tol']
    mono_check = ctx['mono_check']
    mixed_check = ctx['mixed_check']
    mixed_tol_log10 = ctx['mixed_tol_log10']

    rows = [r for r in artifact if r.get('composition') in params]
    if not rows:
        return 0.0

    pass_cnt = 0
    total = len(rows)
    for row in rows:
        comp = row['composition']
        T = float(row['temperature_K'])
        D = float(row['D_cm2_per_s'])
        expected = expected_D(params[comp], T)
        if expected <= 1e-7:
            dif = abs(math.log10(max(D,1e-15)) - math.log10(expected))
            if dif <= tol['D_le_1e-7']['log10_abs']:
                pass_cnt += 1
        else:
            if expected > 0:
                rel = abs((D - expected) / expected)
                if rel <= tol['D_gt_1e-7']['relative']:
                    pass_cnt += 1

    d_score = pass_cnt / total if total else 0.0

    # structural checks
    mono_score = 0.0
    if mono_check:
        data_by_T = {}
        for row in rows:
            T = float(row['temperature_K'])
            comp = row['composition']
            data_by_T.setdefault(T, {})[comp] = float(row['D_cm2_per_s'])
        mono_violations = 0
        for T, d in data_by_T.items():
            if 'PuO2' in d and 'ThO2' in d:
                if d['PuO2'] <= d['ThO2']:
                    mono_violations += 1
        if mono_violations == 0:
            mono_score = 1.0
        else:
            mono_score = 0.0

    mixed_score = 0.0
    if mixed_check:
        data_by_T_mixed = {}
        for row in rows:
            comp = row['composition']
            if comp in ['PuO2', '(Pu0.5Th0.5)O2']:
                T = float(row['temperature_K'])
                data_by_T_mixed.setdefault(T, {})[comp] = float(row['D_cm2_per_s'])
        mixed_violations = 0
        mixed_cnt = 0
        for T, d in data_by_T_mixed.items():
            if 'PuO2' in d and '(Pu0.5Th0.5)O2' in d:
                mixed_cnt += 1
                if d['PuO2'] > 0 and d['(Pu0.5Th0.5)O2'] > 0:
                    diff_log = abs(math.log10(d['(Pu0.5Th0.5)O2']) - math.log10(d['PuO2']))
                    if diff_log > mixed_tol_log10:
                        mixed_violations += 1
                else:
                    if d['(Pu0.5Th0.5)O2'] != d['PuO2']:
                        mixed_violations += 1
        if mixed_cnt == 0:
            mixed_score = 0.5   # cannot evaluate, partial credit
        elif mixed_violations == 0:
            mixed_score = 1.0
        else:
            mixed_score = 0.0

    weight_D = 0.4
    weight_mono = 0.3
    weight_mixed = 0.3
    return d_score * weight_D + mono_score * weight_mono + mixed_score * weight_mixed


# === block: score_1 (check id='step_02_activation') ===
def score_1(artifact, step, ctx):
    act_step = ctx['act_gold']
    gold_energies = act_step.get('activation_gold', {})
    tol = act_step.get('tolerance_eV', 0.5)
    ratio_range = act_step.get('ratio_range', [1.2, 1.8])
    puo2_T_gold = act_step.get('puo2_transition_T_gold', 1700)
    puo2_T_tol = act_step.get('puo2_transition_T_tolerance_K', 200)

    rows = artifact
    if not rows:
        return 0.0

    # check E_D values
    correct = 0
    total_exp = 0
    for row in rows:
        comp = row.get('composition')
        region = row.get('region')
        val = float(row.get('E_D_eV', 0))
        if comp in gold_energies and region in gold_energies[comp]:
            total_exp += 1
            if abs(val - gold_energies[comp][region]) <= tol:
                correct += 1

    E_score = correct / total_exp if total_exp > 0 else 0.0

    # PuO2 transition temperature check
    puo2_T_ok = 0.0
    for row in rows:
        if row.get('composition') == 'PuO2' and row.get('region') == 'Region_I':
            trange = row.get('temperature_range_K', '')
            parts = trange.split('-')
            if len(parts) == 2:
                try:
                    T_low = float(parts[0].strip())
                    if abs(T_low - puo2_T_gold) <= puo2_T_tol:
                        puo2_T_ok = 1.0
                except:
                    pass
            break

    # ratio check
    ratio_ok = 0.0
    E_D_tho = None
    E_D_pu = None
    for row in rows:
        if row.get('composition') == 'ThO2' and row.get('region') == 'Region_I':
            E_D_tho = float(row.get('E_D_eV', 0))
        if row.get('composition') == 'PuO2' and row.get('region') == 'Region_I':
            E_D_pu = float(row.get('E_D_eV', 0))
    if E_D_tho is not None and E_D_pu is not None and E_D_pu > 0:
        ratio = E_D_tho / E_D_pu
        if ratio_range[0] <= ratio <= ratio_range[1]:
            ratio_ok = 1.0

    return E_score * 0.5 + puo2_T_ok * 0.25 + ratio_ok * 0.25


_SCORERS = {
    'step_01_diffusion': score_0,
    'step_02_activation': score_1,
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
