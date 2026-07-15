import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    step = spec['steps'][0]
    alloys = step['alloys']
    nu = step['nu']
    alpha = step['alpha']
    T_room = step['T_room']
    T_700 = step['T_700']
    E_coeff = step['elastic_modulus_coeff']
    expected = {}
    for a in alloys:
        ag = a['a_gamma_rt']
        am = a['a_m23c6_rt']
        for T_C, T_K in [(25, T_room), (700, T_700)]:
            ag_T = ag * (1 + alpha * (T_K - T_room))
            am_T = am * (1 + alpha * (T_K - T_room))
            E_mod = E_coeff[0] + E_coeff[1] * T_K
            delta = abs(am_T - 3*ag_T) / am_T
            if delta == 0:
                sigma = 0.0
            else:
                term1 = 2.0 / (1 + 1.0/(4*delta**2))
                term2 = math.log(2*delta)
                f = delta * (term1 - term2)
                denom = 4 * math.sqrt(2) * (1 - nu**2)
                sigma_MPa_A = (E_mod * ag_T) / denom * f
                sigma = sigma_MPa_A * 1e-4
            expected[(a['name'], T_C)] = sigma
    return {
        'expected': expected,
        'tolerance': step['tolerance_abs'],
        'numeric_weight': step.get('numeric_weight', 0.8),
        'ordering_weight': step.get('ordering_weight', 0.2),
        'alloy_names': [a['name'] for a in alloys]
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    expected = ctx['expected']
    tolerance = ctx['tolerance']
    numeric_w = ctx['numeric_weight']
    ordering_w = ctx['ordering_weight']
    alloy_names = ctx['alloy_names']
    matches = 0
    valid_rows = 0
    sigma_by_alloy_temp = {}
    for row in artifact:
        alloy = row.get('alloy', '').strip()
        temp_str = row.get('temperature_C', '')
        try:
            temp_C = int(temp_str)
        except:
            continue
        key = (alloy, temp_C)
        if key not in expected:
            continue
        valid_rows += 1
        sigma_agent = float(row.get('sigma', 0))
        sigma_exp = expected[key]
        if abs(sigma_agent - sigma_exp) <= tolerance:
            matches += 1
        sigma_by_alloy_temp.setdefault(temp_C, {})[alloy] = sigma_agent
    numeric_score = matches / 4.0 if valid_rows == 4 else 0.0
    ordering_ok = 0
    for temp in [25, 700]:
        val25 = sigma_by_alloy_temp.get(temp, {}).get('25Cr-20Ni-Nb-N')
        val22 = sigma_by_alloy_temp.get(temp, {}).get('22Cr-25Ni-Mo-Nb-N')
        if val25 is not None and val22 is not None and val25 > val22:
            ordering_ok += 1
    ordering_score = ordering_ok / 2.0
    score = numeric_w * numeric_score + ordering_w * ordering_score
    return max(0.0, min(1.0, score))


_SCORERS = {
    'step_01': score_0,
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
