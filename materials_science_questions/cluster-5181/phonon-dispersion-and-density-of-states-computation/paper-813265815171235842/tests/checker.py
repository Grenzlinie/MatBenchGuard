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
    return {}


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    gold = step['parameters']['gold']
    tols = step['parameters']['relative_tolerances']
    data = {}
    for row in artifact:
        if 'material' in row:
            data[row['material']] = row
    materials = ['Si', 'Ge', 'SiGe']
    total = 0
    ok = 0
    for mat in materials:
        if mat not in data:
            continue
        for key in ['c11','c12','c44']:
            total += 1
            try:
                val = float(data[mat][key])
                g = gold[mat][key]
                tol = tols.get(key, 0.05)
                if abs(val - g) / abs(g) <= tol:
                    ok += 1
            except:
                pass
    return ok / total if total > 0 else 0.0


# === block: score_1 (check id='phonon_frequencies') ===
def score_1(artifact, step, ctx):
    def _ta_freqs(mass_u, Fphi, fphiphi):
        conv = 1e5
        m_g = mass_u * 1.66053906660e-24
        c_cm_s = 2.99792458e10
        Fphi_cgs = Fphi * conv
        fpp_cgs = fphiphi * conv
        om2_X = 12.0 * Fphi_cgs / m_g
        om2_L = 6.0 * (Fphi_cgs - fpp_cgs) / m_g
        X_cm = math.sqrt(om2_X) / (2*math.pi * c_cm_s)
        L_cm = math.sqrt(om2_L) / (2*math.pi * c_cm_s)
        return X_cm, L_cm

    gamma_gold = step['parameters']['gamma_gold']
    gamma_tol = step['parameters']['gamma_tol_abs']
    vff = step['parameters']['vff']
    ta_tol = step['parameters']['ta_rel_tol']
    data = {}
    for row in artifact:
        if 'material' in row:
            data[row['material']] = row
    total = 0
    ok = 0
    for mat in ['Si', 'Ge']:
        if mat not in data or mat not in vff:
            continue
        row = data[mat]
        # Gamma optical
        total += 1
        try:
            rep = float(row['Gamma_optic_cm-1'])
            if abs(rep - gamma_gold[mat]) <= gamma_tol:
                ok += 1
        except:
            pass
        # TA X
        exp_X, exp_L = _ta_freqs(vff[mat]['mass_u'], vff[mat]['Fphi'], vff[mat]['fphiphi'])
        total += 1
        try:
            rep_X = float(row['X_TA_cm-1'])
            if abs(rep_X - exp_X) / abs(exp_X) <= ta_tol:
                ok += 1
        except:
            pass
        total += 1
        try:
            rep_L = float(row['L_TA_cm-1'])
            if abs(rep_L - exp_L) / abs(exp_L) <= ta_tol:
                ok += 1
        except:
            pass
    return ok / total if total > 0 else 0.0


# === block: score_2 (check id='ordering_energy') ===
def score_2(artifact, step, ctx):
    params = step['parameters']
    delta_target = params['delta_e_target']
    delta_tol = params['delta_e_tol']
    c_a_target = params['c_a_rh1_target']
    c_a_tol = params['c_a_tol']
    rows = {}
    for row in artifact:
        phase = row.get('phase')
        if phase in ('RH1','random'):
            rows[phase] = row
    if 'RH1' not in rows or 'random' not in rows:
        return 0.0
    score = 0.0
    try:
        e_rh1 = float(rows['RH1']['energy_meV_per_atom'])
        e_rand = float(rows['random']['energy_meV_per_atom'])
        delta_e = abs(e_rh1 - e_rand)
        if abs(delta_e - delta_target) <= delta_tol:
            score += 0.5
    except:
        pass
    try:
        c_a = float(rows['RH1']['c_over_a'])
        if abs(c_a - c_a_target) <= c_a_tol:
            score += 0.5
    except:
        pass
    return score


_SCORERS = {
    'elastic_constants': score_0,
    'phonon_frequencies': score_1,
    'ordering_energy': score_2,
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
