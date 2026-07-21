import os
import json
import csv

# === author imports / helpers ===
import os, json, math, collections


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
        def parse_xyz(content):
            lines = content.strip().split('\n')
            if len(lines) < 3:
                return None
            try:
                n = int(lines[0].strip())
            except:
                return None
            atoms = []
            for line in lines[2:]:
                parts = line.split()
                if len(parts) != 4:
                    continue
                elem, x, y, z = parts[0], float(parts[1]), float(parts[2]), float(parts[3])
                atoms.append((elem, (x, y, z)))
            if len(atoms) != n:
                return None
            return atoms

        def compute_dist(p1, p2):
            return math.sqrt(sum((a-b)**2 for a,b in zip(p1, p2)))

        def analyze(atoms, halogen_sym):
            si = []
            h = []
            for elem, pos in atoms:
                if elem == 'Si':
                    si.append(pos)
                elif elem == halogen_sym:
                    h.append(pos)
            si_count = len(si)
            h_count = len(h)
            total = si_count + h_count
            # Si-X bonds: for each Si, nearest halogen
            si_x_dists = []
            for s in si:
                min_d = min(compute_dist(s, hp) for hp in h)
                si_x_dists.append(min_d)
            # Si-Si bonds: all pairs, collect distances under cutoff 2.8 Å
            si_si_dists = []
            for i in range(si_count):
                for j in range(i+1, si_count):
                    d = compute_dist(si[i], si[j])
                    if d < 2.8:
                        si_si_dists.append(d)
            si_si_min = min(si_si_dists) if si_si_dists else None
            si_si_max = max(si_si_dists) if si_si_dists else None
            return {
                'atom_count': total,
                'elements': {'Si': si_count, halogen_sym: h_count},
                'si_x_distances': si_x_dists,
                'si_si_distances': si_si_dists,
                'si_si_min': si_si_min,
                'si_si_max': si_si_max,
                'si_x_min': min(si_x_dists) if si_x_dists else None,
                'si_x_max': max(si_x_dists) if si_x_dists else None
            }

        ctx = {}
        for fname, hsym in [('si60f60_relaxed.xyz', 'F'), ('si60cl60_relaxed.xyz', 'Cl')]:
            path = os.path.join(outputs_dir, fname)
            if os.path.exists(path):
                with open(path) as f:
                    atoms = parse_xyz(f.read())
                if atoms is not None:
                    key = 'f60' if hsym == 'F' else 'cl60'
                    ctx[key] = analyze(atoms, hsym)
                else:
                    ctx[key] = None
            else:
                ctx[key] = None
        return ctx
    


# === block: score_0 (check id='step_struct_f60') ===
def score_0(artifact, step, ctx):
    data = ctx.get('f60')
    if data is None:
        return 0.0
    spec = step['hidden']
    score = 0.0

    # atom count
    if data['atom_count'] == spec['expected_atom_count']:
        score += 0.1
    # element counts
    if data['elements'].get('Si',0) == spec['expected_Si_count'] and data['elements'].get('F',0) == spec['expected_F_count']:
        score += 0.1
    # symmetry uniformity (Ih)
    si_min = data['si_si_min']
    si_max = data['si_si_max']
    if si_min is not None and si_max is not None:
        variation = si_max - si_min
        if variation <= spec['symmetry_tol']:
            score += 0.2
    # Si-F bond length (average)
    if data['si_x_distances']:
        avg = sum(data['si_x_distances'])/len(data['si_x_distances'])
        if abs(avg - spec['Si_F_bond_ref']) <= spec['Si_F_bond_tol']:
            score += 0.3
    # Si-Si bond range
    if si_min is not None and si_max is not None:
        if si_min >= spec['Si_Si_min_ref'] - spec['Si_Si_tol'] and si_max <= spec['Si_Si_max_ref'] + spec['Si_Si_tol']:
            score += 0.3
    return min(score, 1.0)


# === block: score_1 (check id='step_struct_cl60') ===
def score_1(artifact, step, ctx):
    data = ctx.get('cl60')
    if data is None:
        return 0.0
    spec = step['hidden']
    score = 0.0

    if data['atom_count'] == spec['expected_atom_count']:
        score += 0.1
    if data['elements'].get('Si',0) == spec['expected_Si_count'] and data['elements'].get('Cl',0) == spec['expected_Cl_count']:
        score += 0.1
    si_min = data['si_si_min']
    si_max = data['si_si_max']
    if si_min is not None and si_max is not None:
        variation = si_max - si_min
        if variation <= spec['symmetry_tol']:
            score += 0.2
    if data['si_x_distances']:
        avg = sum(data['si_x_distances'])/len(data['si_x_distances'])
        if abs(avg - spec['Si_Cl_bond_ref']) <= spec['Si_Cl_bond_tol']:
            score += 0.3
    if si_min is not None and si_max is not None:
        if si_min >= spec['Si_Si_min_ref'] - spec['Si_Si_tol'] and si_max <= spec['Si_Si_max_ref'] + spec['Si_Si_tol']:
            score += 0.3
    return min(score, 1.0)


# === block: score_2 (check id='step_results') ===
def score_2(artifact, step, ctx):
    results = artifact
    if not isinstance(results, dict):
        return 0.0

    f60 = results.get('Si60F60', {})
    cl60 = results.get('Si60Cl60', {})
    atomic = results.get('atomic_energies', {})

    f60_ctx = ctx.get('f60')
    cl60_ctx = ctx.get('cl60')

    hidden = step['hidden']
    f60g = hidden['Si60F60']
    cl60g = hidden['Si60Cl60']

    # sub-weights
    w_sym = 0.05
    w_bond = 0.15
    w_gap = 0.1
    w_charge = 0.1
    w_bind = 0.15
    w_te = 0.05
    w_ic = 0.1
    w_trend = 0.3

    score = 0.0

    # 1) symmetry string
    sym_ok = 0
    if f60.get('symmetry','') == f60g['symmetry']:
        sym_ok += 0.5
    if cl60.get('symmetry','') == cl60g['symmetry']:
        sym_ok += 0.5
    score += w_sym * sym_ok

    # 2) bond length cross-check between reported and XYZ recomputed
    bond_checks = 0
    tol_b = 0.02
    if f60_ctx and f60_ctx['si_si_min'] is not None:
        if abs(f60.get('Si_Si_bond_length_min_Ang',0) - f60_ctx['si_si_min']) <= tol_b:
            bond_checks += 1
        if abs(f60.get('Si_Si_bond_length_max_Ang',0) - f60_ctx['si_si_max']) <= tol_b:
            bond_checks += 1
        if f60_ctx['si_x_distances']:
            avg_x_f = sum(f60_ctx['si_x_distances'])/len(f60_ctx['si_x_distances'])
            if abs(f60.get('Si_X_bond_length_Ang',0) - avg_x_f) <= tol_b:
                bond_checks += 1
    else:
        bond_checks += 0
    if cl60_ctx and cl60_ctx['si_si_min'] is not None:
        if abs(cl60.get('Si_Si_bond_length_min_Ang',0) - cl60_ctx['si_si_min']) <= tol_b:
            bond_checks += 1
        if abs(cl60.get('Si_Si_bond_length_max_Ang',0) - cl60_ctx['si_si_max']) <= tol_b:
            bond_checks += 1
        if cl60_ctx['si_x_distances']:
            avg_x_c = sum(cl60_ctx['si_x_distances'])/len(cl60_ctx['si_x_distances'])
            if abs(cl60.get('Si_X_bond_length_Ang',0) - avg_x_c) <= tol_b:
                bond_checks += 1
    else:
        bond_checks += 0
    bond_checks = min(bond_checks, 6)  # max 6
    score += w_bond * (bond_checks / 6.0)

    # 3) HOMO-LUMO gaps
    val_gap_f = f60.get('HOMO_LUMO_gap_eV', None)
    val_gap_c = cl60.get('HOMO_LUMO_gap_eV', None)
    gap_sc = 0
    if val_gap_f is not None and abs(val_gap_f - f60g['gap_ref']) <= f60g['gap_tol']:
        gap_sc += 0.5
    if val_gap_c is not None and abs(val_gap_c - cl60g['gap_ref']) <= cl60g['gap_tol']:
        gap_sc += 0.5
    score += w_gap * gap_sc

    # 4) Mulliken charges
    val_ch_f = f60.get('Mulliken_charge_transfer_e', None)
    val_ch_c = cl60.get('Mulliken_charge_transfer_e', None)
    ch_sc = 0
    if val_ch_f is not None and abs(val_ch_f - f60g['charge_ref']) <= f60g['charge_tol']:
        ch_sc += 0.5
    if val_ch_c is not None and abs(val_ch_c - cl60g['charge_ref']) <= cl60g['charge_tol']:
        ch_sc += 0.5
    score += w_charge * ch_sc

    # 5) binding energies (threshold_or_better)
    val_bind_f = f60.get('binding_energy_eV_per_atom', 0)
    val_bind_c = cl60.get('binding_energy_eV_per_atom', 0)
    bind_sc = 0
    def threshold_score(val, ref, tol):
        if val >= ref - tol:
            return 1.0
        lower = ref - tol * 2
        if lower < 0: lower = 0
        if ref - tol - lower > 0:
            return max(0.0, (val - lower) / (ref - tol - lower))
        return 0.0
    bind_sc = 0.5 * threshold_score(val_bind_f, f60g['binding_ref'], f60g['binding_tol']) + 0.5 * threshold_score(val_bind_c, cl60g['binding_ref'], cl60g['binding_tol'])
    score += w_bind * bind_sc

    # 6) total energy negative
    te_sc = 0
    if isinstance(f60.get('total_energy_Ha'),(int,float)) and f60['total_energy_Ha'] < 0:
        te_sc += 0.5
    if isinstance(cl60.get('total_energy_Ha'),(int,float)) and cl60['total_energy_Ha'] < 0:
        te_sc += 0.5
    score += w_te * te_sc

    # 7) internal consistency: recompute binding from total energy and atomic energies
    ic_sc = 0
    try:
        Ha2eV = 27.2114
        E_total_f = f60['total_energy_Ha']
        E_total_c = cl60['total_energy_Ha']
        E_Si = atomic['Si_Ha']
        E_F = atomic['F_Ha']
        E_Cl = atomic['Cl_Ha']
        bind_f_calc = (E_total_f - 60*E_Si - 60*E_F) / 120 * Ha2eV
        bind_c_calc = (E_total_c - 60*E_Si - 60*E_Cl) / 120 * Ha2eV
        if abs(bind_f_calc - val_bind_f) < 0.1:
            ic_sc += 0.5
        if abs(bind_c_calc - val_bind_c) < 0.1:
            ic_sc += 0.5
    except:
        pass
    score += w_ic * ic_sc

    # 8) relative trends
    tr = 0
    if val_bind_f > val_bind_c:
        tr += 0.1
    if val_gap_c is not None and val_gap_f is not None and val_gap_c > val_gap_f:
        tr += 0.1
    if val_ch_f is not None and val_ch_c is not None and val_ch_f > val_ch_c:
        tr += 0.1
    score += w_trend * (tr / 0.3)  # max of tr is 0.3, so scale to fraction of trend weight

    return min(score, 1.0)


_SCORERS = {
    'step_struct_f60': score_0,
    'step_struct_cl60': score_1,
    'step_results': score_2,
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
