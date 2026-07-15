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


# === block: score_0 (check id='step_bulk') ===
def score_0(artifact, step, ctx):
    ref = step['reference']; tol = step['tolerances']; s=0; tot=12
    for pot in ['CY-EAM','CY-XEAM2']:
        d = artifact.get(pot,{}); r = ref[pot]
        for f in ['lattice_constant_A','cohesive_energy_eV','vacancy_formation_energy_eV','C11_GPa','C12_GPa','C44_GPa']:
            v = d.get(f,None); t = tol[f]
            if v is not None and abs(v - r[f]) <= t: s+=1
    return s / tot


# === block: score_1 (check id='step_cluster') ===
def score_1(artifact, step, ctx):
    ref = step['reference']; tol = step['tolerances']; dft = step['dft_reference']
    tw = step.get('trend_weight',0.3); nw = 1.0 - tw
    sn = 0; nf = 12
    for pot in ['CY-EAM','CY-XEAM2']:
        pd = artifact.get(pot,{}); rp = ref[pot]
        for cl in ['dimer','trimer','tetrahedron']:
            cd = pd.get(cl,{}); rc = rp[cl]
            vb = cd.get('bond_length_A',None); rb = rc['bond_length_A']
            if vb is not None and abs(vb - rb) <= tol['bond_length_A']: sn+=1
            ve = cd.get('binding_energy_eV_per_atom',None); re = rc['binding_energy_eV_per_atom']
            if ve is not None and abs(ve - re) <= tol['binding_energy_eV_per_atom']: sn+=1
    snum = sn / nf
    st = 0
    for cl in ['dimer','trimer','tetrahedron']:
        ee = artifact.get('CY-EAM',{}).get(cl,{}).get('binding_energy_eV_per_atom',None)
        ex = artifact.get('CY-XEAM2',{}).get(cl,{}).get('binding_energy_eV_per_atom',None)
        dft_val = dft[cl]
        if ee is not None and ex is not None:
            if abs(ex - dft_val) < abs(ee - dft_val): st+=1
    strend = st / 3.0
    return nw * snum + tw * strend


# === block: score_2 (check id='step_surface') ===
def score_2(artifact, step, ctx):
    ref = step['reference']; tol = step['tolerances']; exp = step['exp_reference']
    tw = step.get('trend_weight',0.2); nw = 1.0 - tw
    sn = 0; nf = 6
    for pot in ['CY-EAM','CY-XEAM2']:
        pd = artifact.get(pot,{}); rp = ref[pot]
        for f in ['surface_energy_111_eV_per_A2','surface_energy_100_eV_per_A2','adatom_diffusion_barrier_eV']:
            v = pd.get(f,None); t = tol[f]
            if v is not None and abs(v - rp[f]) <= t: sn+=1
    snum = sn / nf
    st = 0
    e111 = artifact.get('CY-EAM',{}).get('surface_energy_111_eV_per_A2',None)
    x111 = artifact.get('CY-XEAM2',{}).get('surface_energy_111_eV_per_A2',None)
    e100 = artifact.get('CY-EAM',{}).get('surface_energy_100_eV_per_A2',None)
    x100 = artifact.get('CY-XEAM2',{}).get('surface_energy_100_eV_per_A2',None)
    if (e111 is not None and x111 is not None and e100 is not None and x100 is not None):
        if abs(x111 - exp['surface_energy_111_eV_per_A2']) < abs(e111 - exp['surface_energy_111_eV_per_A2']) and abs(x100 - exp['surface_energy_100_eV_per_A2']) < abs(e100 - exp['surface_energy_100_eV_per_A2']):
            st += 0.5
    e_diff = artifact.get('CY-EAM',{}).get('adatom_diffusion_barrier_eV',None)
    x_diff = artifact.get('CY-XEAM2',{}).get('adatom_diffusion_barrier_eV',None)
    if (e_diff is not None and x_diff is not None):
        if abs(x_diff - exp['adatom_diffusion_barrier_eV']) < abs(e_diff - exp['adatom_diffusion_barrier_eV']):
            st += 0.5
    return nw * snum + tw * st


_SCORERS = {
    'step_bulk': score_0,
    'step_cluster': score_1,
    'step_surface': score_2,
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
