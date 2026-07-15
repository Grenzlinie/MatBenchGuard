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
    spec = spec  # use the provided spec parameter directly
    reference_data = spec.get('reference_data', {})
    # fallback: step tolerances from spec's steps
    tolerances = {}
    for s in spec.get('steps', []):
        if s.get('id') == 'step_binding':
            tolerances['binding_energy_eV'] = s.get('tolerances', {}).get('binding_energy_eV', 0.15)
            tolerances['bond_length_A'] = s.get('tolerances', {}).get('bond_length_A', 0.03)
        if s.get('id') == 'step_migration':
            tolerances['barrier_eV'] = s.get('tolerance_barrier_eV', 0.25)
    return {'reference_data': reference_data, 'tolerances': tolerances}


# === block: score_0 (check id='step_binding') ===
def score_0(artifact, step, ctx):
    reference_binding = [
        {"system": "nanotube", "configuration": "F", "binding_energy_per_F_eV": 1.43, "C_F_bond_length_Angstrom": 1.455},
        {"system": "nanotube", "configuration": "F2(1,2)", "binding_energy_per_F_eV": 2.43, "C_F_bond_length_Angstrom": 1.408},
        {"system": "nanotube", "configuration": "F2(1,4_cis)", "binding_energy_per_F_eV": 2.38, "C_F_bond_length_Angstrom": 1.435},
        {"system": "nanotube", "configuration": "F2(1,3)", "binding_energy_per_F_eV": 1.87, "C_F_bond_length_Angstrom": 1.466},
        {"system": "nanotube", "configuration": "C4F", "binding_energy_per_F_eV": 1.75, "C_F_bond_length_Angstrom": 1.41},
        {"system": "nanotube", "configuration": "C2F", "binding_energy_per_F_eV": 1.83, "C_F_bond_length_Angstrom": 1.385},
        {"system": "graphene", "configuration": "F", "binding_energy_per_F_eV": 1.04, "C_F_bond_length_Angstrom": 1.495},
    ]
    energy_tol = 0.15
    length_tol = 0.03
    artifact = artifact if artifact is not None and isinstance(artifact, list) else []

    art_dict = {}
    for row in artifact:
        key = (row.get('system', '').strip(), row.get('configuration', '').strip())
        if key not in art_dict:
            art_dict[key] = row

    total = len(reference_binding)
    if total == 0:
        return 0.0

    numeric_score = 0.0
    found_states = {}
    for ref in reference_binding:
        sys = ref.get('system', '').strip()
        conf = ref.get('configuration', '').strip()
        key = (sys, conf)
        art_row = art_dict.get(key)
        if art_row is None:
            continue
        try:
            art_energy = float(art_row.get('binding_energy_per_F_eV', 0))
            art_length = float(art_row.get('C_F_bond_length_Angstrom', 0))
        except (ValueError, TypeError):
            continue
        ref_energy = float(ref.get('binding_energy_per_F_eV', 0))
        ref_length = float(ref.get('C_F_bond_length_Angstrom', 0))
        if math.isclose(art_energy, ref_energy, abs_tol=energy_tol) and math.isclose(art_length, ref_length, abs_tol=length_tol):
            numeric_score += 1.0
            if key not in found_states:
                found_states[key] = art_energy
    numeric_score /= total

    trend_score = 1.0
    try:
        e_isolated = float(art_dict.get(('nanotube','F'), {}).get('binding_energy_per_F_eV', None))
        e_pair_12 = float(art_dict.get(('nanotube','F2(1,2)'), {}).get('binding_energy_per_F_eV', None))
        e_pair_4cis = float(art_dict.get(('nanotube','F2(1,4_cis)'), {}).get('binding_energy_per_F_eV', None))
        e_pair_3 = float(art_dict.get(('nanotube','F2(1,3)'), {}).get('binding_energy_per_F_eV', None))
        e_c2f = float(art_dict.get(('nanotube','C2F'), {}).get('binding_energy_per_F_eV', None))
        e_c4f = float(art_dict.get(('nanotube','C4F'), {}).get('binding_energy_per_F_eV', None))
        if e_isolated is None or e_pair_4cis is None or e_c2f is None:
            trend_score = 0.0
        else:
            if not (e_isolated < e_pair_12 and e_isolated < e_pair_4cis and e_isolated < e_pair_3 and e_isolated < e_c2f):
                trend_score = 0.0
    except Exception:
        trend_score = 0.0

    return round(0.85 * numeric_score + 0.15 * trend_score, 6)


# === block: score_1 (check id='step_migration') ===
def score_1(artifact, step, ctx):
    ref_rows = ctx.get('reference_data', {}).get('migration', [])
    tols = ctx.get('tolerances', {})
    barrier_tol = float(tols.get('barrier_eV', 0.25))
    artifact = artifact if artifact is not None and isinstance(artifact, list) else []

    art_dict = {}
    for row in artifact:
        key = (row.get('system', '').strip(), row.get('transition', '').strip())
        if key not in art_dict:
            art_dict[key] = row

    total = len(ref_rows)
    if total == 0:
        return 0.0
    numeric_score = 0.0
    found_values = {}
    for ref in ref_rows:
        sys = ref.get('system', '').strip()
        tr = ref.get('transition', '').strip()
        key = (sys, tr)
        art_row = art_dict.get(key)
        if art_row is None:
            continue
        try:
            art_val = float(art_row.get('barrier_eV', 0))
        except (ValueError, TypeError):
            continue
        ref_val = float(ref.get('barrier_eV', 0))
        if math.isclose(art_val, ref_val, abs_tol=barrier_tol):
            numeric_score += 1.0
            found_values[key] = art_val
    numeric_score /= total

    trend_score = 1.0
    try:
        b12_nt = float(art_dict.get(('nanotube','(1,2)→(1,3)'), {}).get('barrier_eV', None))
        b12_gr = float(art_dict.get(('graphene','(1,2)→(1,3)'), {}).get('barrier_eV', None))
        b4_nt = float(art_dict.get(('nanotube','(1,4_cis)→(1,3)'), {}).get('barrier_eV', None))
        b4_gr = float(art_dict.get(('graphene','(1,4_cis)→(1,3)'), {}).get('barrier_eV', None))
        if None in (b12_nt, b12_gr, b4_nt, b4_gr):
            trend_score = 0.0
        elif not (b12_nt > b12_gr and b4_nt > b4_gr):
            trend_score = 0.0
    except Exception:
        trend_score = 0.0

    return round(0.85 * numeric_score + 0.15 * trend_score, 6)


_SCORERS = {
    'step_binding': score_0,
    'step_migration': score_1,
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
