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


# === block: score_0 (check id='raw_csv_valid') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if len(rows) != step.get("expected_rows", 7): return 0.0
    names = [r["system_name"] for r in rows]
    if set(names) != set(step["required_systems"]): return 0.0
    return 1.0


# === block: score_1 (check id='recomp_signs') ===
def score_1(artifact, step, ctx):
    energies = {r["system_name"]: float(r["total_energy_eV"]) for r in artifact}
    required = ['Fe_slab','Fe_slab_Cr_S','Fe_slab_Cr_Sm1','Fe_slab_Cr_Sm2','Fe_slab_Cr_central','Fe_bulk','Cr_bulk']
    if not all(k in energies for k in required): return 0.0
    e_fe_slab = energies['Fe_slab']
    e_fe_bulk = energies['Fe_bulk']
    e_cr_bulk = energies['Cr_bulk']
    # formula for S, S-1, S-2 (2 Cr atoms)
    def e_sol_2cr(e_slab_cr): return (e_slab_cr - 2*e_cr_bulk + 2*e_fe_bulk - e_fe_slab) / 2.0
    # formula for central (1 Cr)
    e_sol_central = energies['Fe_slab_Cr_central'] - e_cr_bulk + e_fe_bulk - e_fe_slab
    layers = {'S': energies['Fe_slab_Cr_S'], 'S-1': energies['Fe_slab_Cr_Sm1'], 'S-2': energies['Fe_slab_Cr_Sm2']}
    e_sol = {}
    for layer, e_cr_slab in layers.items():
        e_sol[layer] = e_sol_2cr(e_cr_slab)
    e_sol['central'] = e_sol_central
    e_seg = {l: e_sol[l] - e_sol['central'] for l in e_sol}
    checks = []
    checks.append(e_sol['S'] < 0)
    checks.append(e_sol['S-1'] > 0)
    checks.append(e_sol['S-2'] < 0)
    checks.append(e_sol['central'] < 0)
    checks.append(e_seg['S-1'] > 0)
    checks.append(e_seg['S-1'] > e_seg['S'])
    return sum(1 for c in checks if c) / len(checks)


# === block: score_2 (check id='recomp_Eseg_ref') ===
def score_2(artifact, step, ctx):
    energies = {r["system_name"]: float(r["total_energy_eV"]) for r in artifact}
    required = ['Fe_slab','Fe_slab_Cr_S','Fe_slab_Cr_Sm1','Fe_slab_Cr_Sm2','Fe_slab_Cr_central','Fe_bulk','Cr_bulk']
    if not all(k in energies for k in required): return 0.0
    e_fe_slab = energies['Fe_slab']
    e_fe_bulk = energies['Fe_bulk']
    e_cr_bulk = energies['Cr_bulk']
    def e_sol_2cr(e_slab_cr): return (e_slab_cr - 2*e_cr_bulk + 2*e_fe_bulk - e_fe_slab) / 2.0
    e_seg_S = e_sol_2cr(energies['Fe_slab_Cr_S']) - (energies['Fe_slab_Cr_central'] - e_cr_bulk + e_fe_bulk - e_fe_slab)
    e_seg_Sm1 = e_sol_2cr(energies['Fe_slab_Cr_Sm1']) - (energies['Fe_slab_Cr_central'] - e_cr_bulk + e_fe_bulk - e_fe_slab)
    ref = step['reference']
    tol = step['tolerance']
    score = 0.0
    if abs(e_seg_S - ref['E_seg_S']) <= tol: score += 0.5
    if abs(e_seg_Sm1 - ref['E_seg_Sm1']) <= tol: score += 0.5
    return score


# === block: score_3 (check id='sol_energy_ref') ===
def score_3(artifact, step, ctx):
    ref_layers = step['reference']
    tol = step['tolerance']
    rows_dict = {r['layer']: r for r in artifact if r['layer'] in ref_layers}
    total = 0
    count = 0
    for layer, ref_vals in ref_layers.items():
        if layer not in rows_dict: continue
        row = rows_dict[layer]
        e_seg = float(row['e_seg_eV'])
        m_cr = float(row['m_cr_muB'])
        if abs(e_seg - ref_vals['e_seg_eV']) <= tol['e_seg_eV']: total += 1
        if abs(m_cr - ref_vals['m_cr_muB']) <= tol['m_cr_muB']: total += 1
        count += 2
    if count == 0: return 0.0
    return total / count


_SCORERS = {
    'raw_csv_valid': score_0,
    'recomp_signs': score_1,
    'recomp_Eseg_ref': score_2,
    'sol_energy_ref': score_3,
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
