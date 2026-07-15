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
    step_list = spec.get('steps', spec.get('checks', []))
    ctx = {}
    for step in step_list:
        sid = step['id']
        hidden = step.get('hidden_gold', {}) or {}
        if 'gas_experimental' in hidden:
            ctx['gas_ref'] = {r['salt']: r for r in hidden['gas_experimental']}
            ctx['gas_salts'] = list(ctx['gas_ref'].keys())
        if 'solid_experimental_densities_kgm3' in hidden:
            ctx['solid_ref'] = {r['salt']: r['density_kgm3'] for r in hidden['solid_experimental_densities_kgm3']}
            ctx['solid_salts'] = list(ctx['solid_ref'].keys())
        if 'liquid_experimental_densities_kgm3' in hidden:
            ctx['liquid_ref'] = {r['salt']: r['density_kgm3'] for r in hidden['liquid_experimental_densities_kgm3']}
            ctx['liquid_salts'] = list(ctx['liquid_ref'].keys())
    return ctx


# === block: score_0 (check id='force_field_params_check') ===
def score_0(artifact, step, ctx):
    import math
    ff = artifact
    required = step['params']['required_keys']
    expected_rule = step['params']['combining_rule_expected']
    ranges = step['params']['ion_parameter_ranges']
    if not isinstance(ff, dict):
        return 0.0
    if not all(k in ff for k in required):
        return 0.0
    if ff.get('combining_rule') != expected_rule:
        return 0.0
    ions = ['Li+', 'Na+', 'K+', 'Cs+', 'F-', 'Cl-', 'Br-', 'I-']
    for ion in ions:
        p = ff.get(ion)
        if not isinstance(p, dict):
            return 0.0
        sigma = p.get('sigma')
        eps = p.get('epsilon')
        gamma = p.get('gamma')
        if not (isinstance(sigma, (int,float)) and isinstance(eps, (int,float)) and isinstance(gamma, (int,float))):
            return 0.0
        r = ranges['sigma_nm']
        if sigma < r['min'] or sigma > r['max']:
            return 0.0
        r = ranges['epsilon_kjmol']
        if eps < r['min'] or eps > r['max']:
            return 0.0
        r = ranges['gamma']
        if gamma < r['min'] or gamma > r['max']:
            return 0.0
    return 1.0


# === block: score_1 (check id='gas_properties_check') ===
def score_1(artifact, step, ctx):
    ref = ctx.get('gas_ref')
    if not ref:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    properties = [('re_pm', 're_pm'), ('De_kjmol', 'De_kjmol'), ('nu_cm1', 'nu_cm1'), ('mu_D', 'mu_D')]
    sum_nrmse = 0.0
    count = 0
    for col_key, ref_key in properties:
        vals = []
        ref_vals = []
        for row in artifact:
            salt = row.get('salt')
            if salt and salt in ref:
                try:
                    v = float(row[col_key])
                    rv = float(ref[salt][ref_key])
                    vals.append(v)
                    ref_vals.append(rv)
                except (ValueError, KeyError):
                    pass
        if len(vals) < 1:
            continue
        se = 0.0
        for v, rv in zip(vals, ref_vals):
            se += (v - rv) ** 2
        rmse = math.sqrt(se / len(vals))
        mean_exp = sum(ref_vals) / len(ref_vals)
        if mean_exp == 0:
            continue
        nrmse = 100.0 * rmse / abs(mean_exp)
        sum_nrmse += nrmse
        count += 1
    if count == 0:
        return 0.0
    avg_nrmse = sum_nrmse / count
    threshold = step.get('threshold', 7.0)
    if avg_nrmse <= threshold:
        return 1.0
    max_nrmse = step.get('max_nrmd_for_zero', 30.0)
    if max_nrmse <= threshold:
        return 0.0
    score = 1.0 - (avg_nrmse - threshold) / (max_nrmse - threshold)
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='solid_density_check') ===
def score_2(artifact, step, ctx):
    ref = ctx.get('solid_ref')
    if not ref:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    vals = []
    ref_vals = []
    for row in artifact:
        salt = row.get('salt')
        if salt and salt in ref:
            try:
                v = float(row['density_kgm3'])
                rv = float(ref[salt])
                vals.append(v)
                ref_vals.append(rv)
            except (ValueError, KeyError):
                pass
    if len(vals) == 0:
        return 0.0
    se = 0.0
    for v, rv in zip(vals, ref_vals):
        se += (v - rv) ** 2
    rmse = math.sqrt(se / len(vals))
    threshold = step.get('threshold', 30.0)
    if rmse <= threshold:
        return 1.0
    max_rmse = step.get('max_rmsd_for_zero', 200.0)
    if max_rmse <= threshold:
        return 0.0
    score = 1.0 - (rmse - threshold) / (max_rmse - threshold)
    return max(0.0, min(1.0, score))


# === block: score_3 (check id='liquid_density_check') ===
def score_3(artifact, step, ctx):
    ref = ctx.get('liquid_ref')
    if not ref:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    vals = []
    ref_vals = []
    for row in artifact:
        salt = row.get('salt')
        if salt and salt in ref:
            try:
                v = float(row['density_kgm3'])
                rv = float(ref[salt])
                vals.append(v)
                ref_vals.append(rv)
            except (ValueError, KeyError):
                pass
    if len(vals) == 0:
        return 0.0
    se = 0.0
    for v, rv in zip(vals, ref_vals):
        se += (v - rv) ** 2
    rmse = math.sqrt(se / len(vals))
    # threshold raised to 200 kg/m³ to align with paper's WBK performance (~176 kg/m³) and provide slack
    threshold = 200.0
    if rmse <= threshold:
        return 1.0
    max_rmse = 300.0
    score = 1.0 - (rmse - threshold) / (max_rmse - threshold)
    return max(0.0, min(1.0, score))


_SCORERS = {
    'force_field_params_check': score_0,
    'gas_properties_check': score_1,
    'solid_density_check': score_2,
    'liquid_density_check': score_3,
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
