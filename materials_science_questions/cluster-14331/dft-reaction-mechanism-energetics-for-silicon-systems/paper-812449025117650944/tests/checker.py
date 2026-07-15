import os
import json
import csv

# === author imports / helpers ===
import json
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
    hartree_to_kcal = 627.5095
    return {
        'gold': {
            'ts2a_raw_ea': 39.0,
            'ts2b_raw_ea': 53.7,
            'ts2a_zpe_ea': 40.7,
            'ts2b_zpe_ea': 55.4,
            'SiH_bond': 83.4,
            'SiSi_bond': 68.8
        },
        'tol_raw_ea': 3.0,   # kcal/mol
        'tol_zpe_ea': 3.0,
        'tol_bond': 4.0,
        'tol_consistency_hartree': 0.001,
        'hartree_to_kcal': hartree_to_kcal
    }


# === block: score_0 (check id='consistency_raw_ea_ts2a') ===
def score_0(artifact, step, ctx):
    s = artifact.get('surface', {})
    try:
        ts2a_h = float(s['ts2a_raw_MP2_energy_hartree'])
        react_h = float(s['reactants_sum_raw_MP2_energy_hartree'])
        reported = float(s['ts2a_MP2_Ea_kcal_mol_raw'])
        computed = (ts2a_h - react_h) * ctx['hartree_to_kcal']
        return 1.0 if abs(computed - reported) < ctx['tol_consistency_hartree'] * ctx['hartree_to_kcal'] else 0.0
    except (KeyError, ValueError, TypeError):
        return 0.0


# === block: score_1 (check id='consistency_raw_ea_ts2b') ===
def score_1(artifact, step, ctx):
    s = artifact.get('surface', {})
    try:
        ts2b_h = float(s['ts2b_raw_MP2_energy_hartree'])
        react_h = float(s['reactants_sum_raw_MP2_energy_hartree'])
        reported = float(s['ts2b_MP2_Ea_kcal_mol_raw'])
        computed = (ts2b_h - react_h) * ctx['hartree_to_kcal']
        return 1.0 if abs(computed - reported) < ctx['tol_consistency_hartree'] * ctx['hartree_to_kcal'] else 0.0
    except (KeyError, ValueError, TypeError):
        return 0.0


# === block: score_2 (check id='surface_raw_ea_check') ===
def score_2(artifact, step, ctx):
    s = artifact.get('surface', {})
    try:
        ea_ts2a = float(s['ts2a_MP2_Ea_kcal_mol_raw'])
        ea_ts2b = float(s['ts2b_MP2_Ea_kcal_mol_raw'])
        ok_a = abs(ea_ts2a - ctx['gold']['ts2a_raw_ea']) <= ctx['tol_raw_ea']
        ok_b = abs(ea_ts2b - ctx['gold']['ts2b_raw_ea']) <= ctx['tol_raw_ea']
        return (ok_a + ok_b) / 2.0
    except (KeyError, ValueError, TypeError):
        return 0.0


# === block: score_3 (check id='surface_zpe_ea_check') ===
def score_3(artifact, step, ctx):
    s = artifact.get('surface', {})
    try:
        ea_zpe_ts2a = float(s['ts2a_MP2_Ea_kcal_mol_with_ZPE'])
        ea_zpe_ts2b = float(s['ts2b_MP2_Ea_kcal_mol_with_ZPE'])
        ok_a = abs(ea_zpe_ts2a - ctx['gold']['ts2a_zpe_ea']) <= ctx['tol_zpe_ea']
        ok_b = abs(ea_zpe_ts2b - ctx['gold']['ts2b_zpe_ea']) <= ctx['tol_zpe_ea']
        return (ok_a + ok_b) / 2.0
    except (KeyError, ValueError, TypeError):
        return 0.0


# === block: score_4 (check id='gas_bond_enthalpy_check') ===
def score_4(artifact, step, ctx):
    g = artifact.get('gas_phase', {})
    try:
        sih = float(g['SiH_bond_enthalpy_kcal_mol'])
        sisi = float(g['SiSi_bond_enthalpy_kcal_mol'])
        ok_sih = abs(sih - ctx['gold']['SiH_bond']) <= ctx['tol_bond']
        ok_sisi = abs(sisi - ctx['gold']['SiSi_bond']) <= ctx['tol_bond']
        return (ok_sih + ok_sisi) / 2.0
    except (KeyError, ValueError, TypeError):
        return 0.0


# === block: score_5 (check id='surface_ordering') ===
def score_5(artifact, step, ctx):
    s = artifact.get('surface', {})
    try:
        ea_zpe_ts2a = float(s['ts2a_MP2_Ea_kcal_mol_with_ZPE'])
        ea_zpe_ts2b = float(s['ts2b_MP2_Ea_kcal_mol_with_ZPE'])
        return 1.0 if ea_zpe_ts2a < ea_zpe_ts2b else 0.0
    except (KeyError, ValueError, TypeError):
        return 0.0


# === block: score_6 (check id='gas_ordering') ===
def score_6(artifact, step, ctx):
    g = artifact.get('gas_phase', {})
    try:
        sih = float(g['SiH_bond_enthalpy_kcal_mol'])
        sisi = float(g['SiSi_bond_enthalpy_kcal_mol'])
        return 1.0 if sih > sisi else 0.0
    except (KeyError, ValueError, TypeError):
        return 0.0


_SCORERS = {
    'consistency_raw_ea_ts2a': score_0,
    'consistency_raw_ea_ts2b': score_1,
    'surface_raw_ea_check': score_2,
    'surface_zpe_ea_check': score_3,
    'gas_bond_enthalpy_check': score_4,
    'surface_ordering': score_5,
    'gas_ordering': score_6,
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
