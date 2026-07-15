import os
import json
import csv

# === author imports / helpers ===
import csv
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
    return {}


# === block: score_0 (check id='step_0') ===
def score_0(artifact, step, ctx):
    artifact_rows = {row['element']: row for row in artifact}
    ref = step['reference']
    cols = ref['columns']
    tolerances = ref['tolerances']
    expected_rows = ref['rows']
    num_checks = 0
    passed = 0
    for elem, exp_row in expected_rows.items():
        agent_row = artifact_rows.get(elem)
        if agent_row is None:
            continue
        for col in cols:
            num_checks += 1
            a_val = float(agent_row[col])
            e_val = exp_row[col]
            tol = tolerances[col]
            if e_val == 0:
                if abs(a_val) < 1e-6:
                    passed += 1
            else:
                if abs((a_val - e_val) / e_val) <= tol:
                    passed += 1
    if num_checks == 0:
        return 0.0
    return passed / num_checks


# === block: score_1 (check id='step_1') ===
def score_1(artifact, step, ctx):
    # Hardcoded reference values (Paper's Ω0 case)
    gold_rows = {
        0:   {'Av':0.6278, 'Omega0_au':129.05, 'eta1':0.4387, 'eta2':0.0,    'resistivity_uohm_cm':20.0,  'c_m_s':4359, 'beta_inv_Pa':None},
        20:  {'Av':0.9751, 'Omega0_au':130.98, 'eta1':0.3136, 'eta2':0.1566, 'resistivity_uohm_cm':30.0,  'c_m_s':4466, 'beta_inv_Pa':None},
        40:  {'Av':1.3224, 'Omega0_au':133.84, 'eta1':0.1921, 'eta2':0.3406, 'resistivity_uohm_cm':50.0,  'c_m_s':4264, 'beta_inv_Pa':None},
        60:  {'Av':1.6696, 'Omega0_au':138.47, 'eta1':0.1025, 'eta2':0.4452, 'resistivity_uohm_cm':100.0, 'c_m_s':4608, 'beta_inv_Pa':None},
        80:  {'Av':2.0169, 'Omega0_au':147.30, 'eta1':0.0396, 'eta2':0.4777, 'resistivity_uohm_cm':220.0, 'c_m_s':5838, 'beta_inv_Pa':None},
        100: {'Av':2.2976, 'Omega0_au':170.79, 'eta1':0.0,    'eta2':0.3994, 'resistivity_uohm_cm':25.0,  'c_m_s':9112, 'beta_inv_Pa':None},
    }
    # Compute beta_inv_Pa from additive density and c (Paper's Table 3 sound velocity)
    rho_Al = 2342.97  # kg/m³, from paper V. E. Zinov'ev
    rho_Li = 455.27
    for perc, vals in gold_rows.items():
        c = vals['c_m_s']
        C2 = perc / 100.0
        rho = (1-C2)*rho_Al + C2*rho_Li
        vals['beta_inv_Pa'] = 1.0 / (rho * c * c)

    tolerances = {
        'Av': 0.05,
        'Omega0_au': 0.05,
        'eta1': 0.05,
        'eta2': 0.05,
        'resistivity_uohm_cm': 0.10,
        'c_m_s': 0.05,
        'beta_inv_Pa': 0.10,
    }

    rows = {str(int(float(row['Li_at_percent']))): row for row in artifact}

    num_val_checks = 0
    passed_val = 0
    for perc_str, gold in gold_rows.items():
        agent_row = rows.get(perc_str)
        if agent_row is None:
            continue
        for col in ['Av','Omega0_au','eta1','eta2','resistivity_uohm_cm','c_m_s','beta_inv_Pa']:
            num_val_checks += 1
            a_val = float(agent_row[col])
            e_val = gold[col]
            tol = tolerances[col]
            if e_val == 0:
                if abs(a_val) < 1e-6:
                    passed_val += 1
            else:
                if abs((a_val - e_val) / e_val) <= tol:
                    passed_val += 1

    # Trend check (resistivity at 80 at% >= 2 * resistivity at 0 at%)
    trend_passed = 0
    trend_total = 0
    if '80' in rows and '0' in rows:
        trend_total = 1
        res80 = float(rows['80']['resistivity_uohm_cm'])
        res0 = float(rows['0']['resistivity_uohm_cm'])
        if res80 >= 2 * res0:
            trend_passed = 1

    total_checks = num_val_checks + trend_total
    passed_total = passed_val + trend_passed
    if total_checks == 0:
        return 0.0
    return passed_total / total_checks


_SCORERS = {
    'step_0': score_0,
    'step_1': score_1,
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
