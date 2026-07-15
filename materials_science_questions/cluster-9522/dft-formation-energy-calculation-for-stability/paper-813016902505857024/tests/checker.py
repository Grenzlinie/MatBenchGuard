import os
import json
import csv


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


# === block: score_0 (check id='bulk_formation_energies') ===
def score_0(artifact, step, ctx):
    data = artifact
    b = data['binary_total_energies']
    t = data['ternary_total_energies']
    ef_Cs = t['CsPbBr3'] - b['CsBr'] - b['PbBr2']
    ef_MAP = t['MAPbI3'] - b['MAI'] - b['PbI2']
    p = step['params']
    tol = p['tolerance_eV']
    ok1 = abs(ef_Cs - p['target_CsPbBr3_eV']) <= tol
    ok2 = abs(ef_MAP - p['target_MAPbI3_eV']) <= tol
    return (float(ok1) + float(ok2)) / 2.0


# === block: score_1 (check id='surface_energies') ===
def score_1(artifact, step, ctx):
    b = artifact['binary_total_energies']
    t = artifact['ternary_total_energies']
    p = step['params']
    tol = p['tolerance_eV']
    targets = p['targets']
    def surf(comp, term, rel):
        for s in artifact['slab_total_energies']:
            if s['compound'] == comp and s['termination'] == term and s['thickness'] == 3 and s['relaxation'] == rel:
                sl_energy = s['energy_eV']
                break
        else:
            return None
        if comp == 'CsPbBr3':
            e_ax = b['CsBr']; e_bx2 = b['PbBr2']; e_tern = t['CsPbBr3']
        else:
            e_ax = b['MAI']; e_bx2 = b['PbI2']; e_tern = t['MAPbI3']
        if term == 'AX':
            mu_ax = e_ax; mu_bx2 = e_tern - mu_ax
            N_ax = 4; N_bx2 = 3
        else:
            mu_bx2 = e_bx2; mu_ax = e_tern - mu_bx2
            N_ax = 3; N_bx2 = 4
        return 0.5 * (sl_energy - N_ax * mu_ax - N_bx2 * mu_bx2)
    ok = 0.0
    total = 0
    for key, tv in targets.items():
        comp, term, rel = key.split('_')
        val = surf(comp, term, rel)
        if val is not None:
            total += 1
            if abs(val - tv) <= tol:
                ok += 1
    return ok / total if total > 0 else 0.0


# === block: score_2 (check id='cleavage_energies') ===
def score_2(artifact, step, ctx):
    b = artifact['binary_total_energies']
    t = artifact['ternary_total_energies']
    p = step['params']
    tol = p['tolerance_eV']
    targets = p['targets']
    def get_surf(comp, term, rel):
        for s in artifact['slab_total_energies']:
            if s['compound'] == comp and s['termination'] == term and s['thickness'] == 3 and s['relaxation'] == rel:
                sl_energy = s['energy_eV']
                break
        else:
            return None
        if comp == 'CsPbBr3':
            e_ax = b['CsBr']; e_bx2 = b['PbBr2']; e_tern = t['CsPbBr3']
        else:
            e_ax = b['MAI']; e_bx2 = b['PbI2']; e_tern = t['MAPbI3']
        if term == 'AX':
            mu_ax = e_ax; mu_bx2 = e_tern - mu_ax
            N_ax = 4; N_bx2 = 3
        else:
            mu_bx2 = e_bx2; mu_ax = e_tern - mu_bx2
            N_ax = 3; N_bx2 = 4
        return 0.5 * (sl_energy - N_ax * mu_ax - N_bx2 * mu_bx2)
    ok = 0.0
    total = 0
    for key, tv in targets.items():
        comp, relax = key.rsplit('_', 1)
        rel = 'ideal' if relax == 'ideal' else 'relaxed'
        s_ax = get_surf(comp, 'AX', rel)
        s_bx2 = get_surf(comp, 'BX2', rel)
        if s_ax is None or s_bx2 is None:
            continue
        if comp == 'CsPbBr3':
            ef = t['CsPbBr3'] - b['CsBr'] - b['PbBr2']
        else:
            ef = t['MAPbI3'] - b['MAI'] - b['PbI2']
        e_cl = s_ax + s_bx2 - 0.5 * ef
        total += 1
        if abs(e_cl - tv) <= tol:
            ok += 1
    return ok / total if total > 0 else 0.0


# === block: score_3 (check id='formation_energy_trends') ===
def score_3(artifact, step, ctx):
    b = artifact['binary_total_energies']
    t = artifact['ternary_total_energies']
    ef_bulk_Cs = t['CsPbBr3'] - b['CsBr'] - b['PbBr2']
    ef_bulk_MAP = t['MAPbI3'] - b['MAI'] - b['PbI2']
    def get_ef(comp, term, thick):
        for s in artifact['slab_total_energies']:
            if s['compound'] == comp and s['termination'] == term and s['thickness'] == thick and s['relaxation'] == 'relaxed':
                slab = s['energy_eV']
                break
        else:
            return None
        if comp == 'CsPbBr3':
            e_ax = b['CsBr']; e_bx2 = b['PbBr2']
        else:
            e_ax = b['MAI']; e_bx2 = b['PbI2']
        n = thick
        if term == 'AX':
            return (slab - (n+1)*e_ax - n*e_bx2) / n
        else:
            return (slab - n*e_ax - (n+1)*e_bx2) / n
    checks = 0.0
    passed = 0.0
    for comp in ['CsPbBr3', 'MAPbI3']:
        for thick in [1,2,3]:
            ax = get_ef(comp, 'AX', thick)
            bx2 = get_ef(comp, 'BX2', thick)
            if ax is not None and bx2 is not None:
                checks += 1
                if ax < bx2: passed += 1
    for comp, thick, term in [('CsPbBr3',1,'AX'),('CsPbBr3',2,'AX'),('CsPbBr3',3,'AX'),('CsPbBr3',1,'BX2'),('CsPbBr3',2,'BX2'),('CsPbBr3',3,'BX2')]:
        e = get_ef(comp, term, thick)
        if e is not None:
            checks += 1
            if e > ef_bulk_Cs: passed += 1
    for thick in [1,2,3]:
        e = get_ef('MAPbI3', 'AX', thick)
        if e is not None:
            checks += 1
            if e <= ef_bulk_MAP: passed += 1
    for comp in ['CsPbBr3', 'MAPbI3']:
        for term in ['AX', 'BX2']:
            e1 = get_ef(comp, term, 1)
            e2 = get_ef(comp, term, 2)
            e3 = get_ef(comp, term, 3)
            if e1 is not None and e2 is not None:
                checks += 1
                if e1 > e2: passed += 1
            if e2 is not None and e3 is not None:
                checks += 1
                if e2 > e3: passed += 1
    if checks == 0: return 0.0
    return passed / checks


# === block: score_4 (check id='surface_energy_trends') ===
def score_4(artifact, step, ctx):
    b = artifact['binary_total_energies']
    t = artifact['ternary_total_energies']
    def surf(comp, term, rel):
        for s in artifact['slab_total_energies']:
            if s['compound'] == comp and s['termination'] == term and s['thickness'] == 3 and s['relaxation'] == rel:
                sl_energy = s['energy_eV']
                break
        else:
            return None
        if comp == 'CsPbBr3':
            e_ax = b['CsBr']; e_bx2 = b['PbBr2']; e_tern = t['CsPbBr3']
        else:
            e_ax = b['MAI']; e_bx2 = b['PbI2']; e_tern = t['MAPbI3']
        if term == 'AX':
            mu_ax = e_ax; mu_bx2 = e_tern - mu_ax
            N_ax = 4; N_bx2 = 3
        else:
            mu_bx2 = e_bx2; mu_ax = e_tern - mu_bx2
            N_ax = 3; N_bx2 = 4
        return 0.5 * (sl_energy - N_ax * mu_ax - N_bx2 * mu_bx2)
    checks = 0.0
    passed = 0.0
    for comp in ['CsPbBr3', 'MAPbI3']:
        for rel in ['ideal', 'relaxed']:
            s_ax = surf(comp, 'AX', rel)
            s_bx2 = surf(comp, 'BX2', rel)
            if s_ax is not None and s_bx2 is not None:
                checks += 1
                if s_ax < s_bx2: passed += 1
    mai_rel = surf('MAPbI3', 'AX', 'relaxed')
    if mai_rel is not None:
        checks += 1
        if mai_rel <= -0.005: passed += 1
    for comp in ['CsPbBr3', 'MAPbI3']:
        for term in ['AX', 'BX2']:
            s_i = surf(comp, term, 'ideal')
            s_r = surf(comp, term, 'relaxed')
            if s_i is not None and s_r is not None:
                checks += 1
                if s_i > s_r: passed += 1
    if checks == 0: return 0.0
    return passed / checks


_SCORERS = {
    'bulk_formation_energies': score_0,
    'surface_energies': score_1,
    'cleavage_energies': score_2,
    'formation_energy_trends': score_3,
    'surface_energy_trends': score_4,
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
