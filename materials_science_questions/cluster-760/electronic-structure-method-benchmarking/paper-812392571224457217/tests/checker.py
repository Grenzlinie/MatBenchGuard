import os
import json
import csv

# === author imports / helpers ===
import math

def get_species_value(rows, species_name, column):
    for row in rows:
        if row.get('species') == species_name:
            val = row.get(column)
            if val is None or val == '':
                return None
            try:
                return float(val)
            except (ValueError, TypeError):
                return None
    return None


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
    return {
        'AU_TO_KCAL': 627.5095,
        'gold': {
            'DE_electronic': 8.1,
            'DE_ZPE': 8.8,
            'BDE_electronic': 39.6,
            'BDE_ZPE': 36.0,
        },
        'tolerance_kcal': 1.5,
    }


# === block: score_0 (check id='check_consistency') ===
def score_0(artifact, step, ctx):
    rows = artifact
    expected_species = {'singlet_FeCO4', 'triplet_FeCO4', 'FeCO5', 'CO'}
    species_set = set(row.get('species') for row in rows)
    if species_set != expected_species:
        return 0.0
    for row in rows:
        try:
            te = float(row['CCSD(T)/VQZ-VDZ_total_energy_Hartree'])
            zpe = float(row['B3PW91*_zero_point_energy_Hartree'])
        except (ValueError, KeyError, TypeError):
            return 0.0
        if te >= 0 or zpe < 0 or zpe > 0.2:
            return 0.0
    return 1.0


# === block: score_1 (check id='check_DE_electronic') ===
def score_1(artifact, step, ctx):
    rows = artifact
    e_s = get_species_value(rows, 'singlet_FeCO4', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    e_t = get_species_value(rows, 'triplet_FeCO4', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    if e_s is None or e_t is None:
        return 0.0
    de = e_s - e_t
    de_kcal = de * ctx['AU_TO_KCAL']
    diff = abs(de_kcal - ctx['gold']['DE_electronic'])
    return 1.0 if diff <= ctx['tolerance_kcal'] else 0.0


# === block: score_2 (check id='check_DE_ZPE') ===
def score_2(artifact, step, ctx):
    rows = artifact
    e_s = get_species_value(rows, 'singlet_FeCO4', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    e_t = get_species_value(rows, 'triplet_FeCO4', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    zpe_s = get_species_value(rows, 'singlet_FeCO4', 'B3PW91*_zero_point_energy_Hartree')
    zpe_t = get_species_value(rows, 'triplet_FeCO4', 'B3PW91*_zero_point_energy_Hartree')
    if any(v is None for v in [e_s, e_t, zpe_s, zpe_t]):
        return 0.0
    de_zpe = (e_s - e_t) + (zpe_s - zpe_t)
    de_zpe_kcal = de_zpe * ctx['AU_TO_KCAL']
    diff = abs(de_zpe_kcal - ctx['gold']['DE_ZPE'])
    return 1.0 if diff <= ctx['tolerance_kcal'] else 0.0


# === block: score_3 (check id='check_BDE_electronic') ===
def score_3(artifact, step, ctx):
    rows = artifact
    e_t = get_species_value(rows, 'triplet_FeCO4', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    e_co = get_species_value(rows, 'CO', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    e_fe5 = get_species_value(rows, 'FeCO5', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    if any(v is None for v in [e_t, e_co, e_fe5]):
        return 0.0
    bde = e_t + e_co - e_fe5
    bde_kcal = bde * ctx['AU_TO_KCAL']
    diff = abs(bde_kcal - ctx['gold']['BDE_electronic'])
    return 1.0 if diff <= ctx['tolerance_kcal'] else 0.0


# === block: score_4 (check id='check_BDE_ZPE') ===
def score_4(artifact, step, ctx):
    rows = artifact
    e_t = get_species_value(rows, 'triplet_FeCO4', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    e_co = get_species_value(rows, 'CO', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    e_fe5 = get_species_value(rows, 'FeCO5', 'CCSD(T)/VQZ-VDZ_total_energy_Hartree')
    zpe_t = get_species_value(rows, 'triplet_FeCO4', 'B3PW91*_zero_point_energy_Hartree')
    zpe_co = get_species_value(rows, 'CO', 'B3PW91*_zero_point_energy_Hartree')
    zpe_fe5 = get_species_value(rows, 'FeCO5', 'B3PW91*_zero_point_energy_Hartree')
    if any(v is None for v in [e_t, e_co, e_fe5, zpe_t, zpe_co, zpe_fe5]):
        return 0.0
    bde_zpe = (e_t + e_co - e_fe5) + (zpe_t + zpe_co - zpe_fe5)
    bde_zpe_kcal = bde_zpe * ctx['AU_TO_KCAL']
    diff = abs(bde_zpe_kcal - ctx['gold']['BDE_ZPE'])
    return 1.0 if diff <= ctx['tolerance_kcal'] else 0.0


_SCORERS = {
    'check_consistency': score_0,
    'check_DE_electronic': score_1,
    'check_DE_ZPE': score_2,
    'check_BDE_electronic': score_3,
    'check_BDE_ZPE': score_4,
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
