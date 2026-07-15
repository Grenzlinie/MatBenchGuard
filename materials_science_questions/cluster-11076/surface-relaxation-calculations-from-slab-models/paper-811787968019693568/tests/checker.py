import os
import json
import csv

# === author imports / helpers ===
import re, os, json, math


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
    ctx = {}
    # Parse bulk_relax.out for lattice constant
    bulk_path = os.path.join(outputs_dir, 'bulk_relax.out')
    ctx['a'] = None
    if os.path.exists(bulk_path):
        with open(bulk_path) as f:
            content = f.read()
        # Try alat pattern: "Final alat = <num> Bohr" or "alat = <num>"
        m = re.search(r'\balat\s*=\s*([\d.]+)', content)
        if m:
            alat_bohr = float(m.group(1))
            ctx['a'] = alat_bohr * 0.5291772108
        else:
            # Try cell parameters
            cell = re.findall(r'CELL_PARAMETERS.*?\n(.*?)(?=\n\s*$|\nATOMIC_POSITIONS|\nEnd)', content, re.DOTALL)
            if cell:
                lines = cell[0].strip().split('\n')[:3]
                matrix = [list(map(float, l.split())) for l in lines]
                a_bohr = matrix[0][0]
                ctx['a'] = a_bohr * 0.5291772108

    # Parse bulk_dos.dat
    ctx['dos_energy'] = []; ctx['dos_values'] = []
    dos_path = os.path.join(outputs_dir, 'bulk_dos.dat')
    if os.path.exists(dos_path):
        with open(dos_path) as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    try:
                        ctx['dos_energy'].append(float(parts[0]))
                        ctx['dos_values'].append(float(parts[1]))
                    except ValueError:
                        pass

    # Parse slab7_relax.out for total energy and atomic positions
    ctx['slab7_energy'] = None
    ctx['slab7_cell'] = None
    ctx['slab7_atoms'] = []  # list of (species, x, y, z_fractional)
    slab7_path = os.path.join(outputs_dir, 'slab7_relax.out')
    if os.path.exists(slab7_path):
        with open(slab7_path) as f:
            content7 = f.read()
        # total energy
        m = re.search(r'!\s+total energy\s+=\s+([-\d.]+)\s+Ry', content7)
        if m:
            ctx['slab7_energy'] = float(m.group(1))
        # cell parameters
        cell_sec = re.findall(r'CELL_PARAMETERS.*?\n(.*?)(?=\n\n|\n\s*$|\nATOMIC_POSITIONS)', content7, re.DOTALL)
        if cell_sec:
            lines = cell_sec[0].strip().split('\n')[:3]
            matrix = [list(map(float, l.split())) for l in lines]
            ctx['slab7_cell'] = matrix
        # atomic positions (crystal)
        atoms_sec = re.findall(r'ATOMIC_POSITIONS \(crystal\)\n(.*?)(?=\n\n|\n\s*$|\nEnd)', content7, re.DOTALL)
        if atoms_sec:
            for line in atoms_sec[0].strip().split('\n'):
                parts = line.split()
                if len(parts) >= 4:
                    species = parts[0]
                    try:
                        x, y, z = map(float, parts[1:4])
                        ctx['slab7_atoms'].append((species, x, y, z))
                    except ValueError:
                        pass

    # Parse slab5_relax.out for total energy
    ctx['slab5_energy'] = None
    slab5_path = os.path.join(outputs_dir, 'slab5_relax.out')
    if os.path.exists(slab5_path):
        with open(slab5_path) as f:
            content5 = f.read()
        m = re.search(r'!\s+total energy\s+=\s+([-\d.]+)\s+Ry', content5)
        if m:
            ctx['slab5_energy'] = float(m.group(1))

    # Load results.json if present
    ctx['results'] = None
    results_path = os.path.join(outputs_dir, 'results.json')
    if os.path.exists(results_path):
        with open(results_path) as f:
            ctx['results'] = json.load(f)

    return ctx


# === block: score_0 (check id='lattice') ===
def score_0(artifact, step, ctx):
    a = ctx.get('a')
    if a is None:
        return 0.0
    return 1.0 if abs(a - step['gold']) <= step['tolerance'] else 0.0


# === block: score_1 (check id='dos_fermi') ===
def score_1(artifact, step, ctx):
    energy = ctx.get('dos_energy')
    values = ctx.get('dos_values')
    if not energy or len(energy) < 2:
        return 0.0
    # interpolate at E=0
    if 0.0 in energy:
        idx = energy.index(0.0)
        dos_at_fermi = values[idx]
    else:
        # find bracket
        for i in range(len(energy)-1):
            if (energy[i] <= 0.0 <= energy[i+1]) or (energy[i+1] <= 0.0 <= energy[i]):
                # linear interpolation
                t = (0.0 - energy[i]) / (energy[i+1] - energy[i])
                dos_at_fermi = values[i] + t * (values[i+1] - values[i])
                break
        else:
            return 0.0
    gold = step['gold']
    tol = step['tolerance']
    return 1.0 if abs(dos_at_fermi - gold) <= tol else 0.0


# === block: score_2 (check id='surface_energy') ===
def score_2(artifact, step, ctx):
    a = ctx.get('a')
    if a is None:
        # try from slab7 cell
        cell = ctx.get('slab7_cell')
        if cell:
            a_bohr = cell[0][0]
            a = a_bohr * 0.5291772108
        else:
            return 0.0
    E7 = ctx.get('slab7_energy')
    E5 = ctx.get('slab5_energy')
    if E7 is None or E5 is None:
        return 0.0
    # Boettger formula for symmetric slab: σ = (E_n - n*ΔE) / (2A) with ΔE = (E_n - E_{n-2})/2
    # For n=7: σ = (7*E5 - 5*E7) / (4*A)
    dE_Ry = 7.0 * E5 - 5.0 * E7
    Ry_to_J = 13.605693 * 1.602176634e-19
    sigma_J = dE_Ry * Ry_to_J
    a_bohr = a / 0.5291772108
    area_m2 = (a_bohr * 5.291772108e-11) ** 2
    sigma = sigma_J / (4.0 * area_m2)
    gold = step['gold']
    tol = step['tolerance']
    return 1.0 if abs(sigma - gold) <= tol else 0.0


# === block: score_3 (check id='interlayer_accuracy') ===
def score_3(artifact, step, ctx):
    a = ctx.get('a')
    if a is None:
        return 0.0
    cell = ctx.get('slab7_cell')
    if not cell:
        return 0.0
    c_bohr = cell[2][2]
    c_A = c_bohr * 0.5291772108
    d_bulk = a  # bulk spacing for same-species (001) layers in rocksalt is a
    atoms = ctx.get('slab7_atoms')
    if not atoms:
        return 0.0
    # sort by z coordinate
    sorted_atoms = sorted(atoms, key=lambda x: x[3])
    C_zs = []
    Ti_zs = []
    for sym, x, y, z in sorted_atoms:
        if sym == 'C':
            C_zs.append(z * c_A)
        elif sym == 'Ti':
            Ti_zs.append(z * c_A)
    if len(C_zs) < 4 or len(Ti_zs) < 4:
        return 0.0
    def compute_deltas(zs):
        deltas = []
        for i in range(len(zs)-1):
            d = zs[i+1] - zs[i]
            delta = ((d - d_bulk) / d_bulk) * 100.0
            deltas.append(delta)
        return deltas
    C_deltas = compute_deltas(C_zs)[:3]  # 12,23,34
    Ti_deltas = compute_deltas(Ti_zs)[:3]
    gold = step['gold_deltas']
    tol = step['tolerance_per_delta']
    score = 0.0
    keys = ['C_12','C_23','C_34']
    for k, d in zip(keys, C_deltas):
        if abs(d - gold[k]) <= tol:
            score += 1.0
    keys = ['Ti_12','Ti_23','Ti_34']
    for k, d in zip(keys, Ti_deltas):
        if abs(d - gold[k]) <= tol:
            score += 1.0
    return score / 6.0


# === block: score_4 (check id='interlayer_trend') ===
def score_4(artifact, step, ctx):
    a = ctx.get('a')
    cell = ctx.get('slab7_cell')
    if a is None or not cell:
        return 0.0
    c_bohr = cell[2][2]
    c_A = c_bohr * 0.5291772108
    d_bulk = a  # bulk spacing for same-species (001) layers in rocksalt is a
    atoms = ctx.get('slab7_atoms')
    if not atoms:
        return 0.0
    sorted_atoms = sorted(atoms, key=lambda x: x[3])
    C_zs = []
    Ti_zs = []
    for sym, x, y, z in sorted_atoms:
        if sym == 'C':
            C_zs.append(z * c_A)
        elif sym == 'Ti':
            Ti_zs.append(z * c_A)
    if len(C_zs) < 4 or len(Ti_zs) < 4:
        return 0.0
    def get_abs_deltas(zs):
        abs_d = []
        for i in range(len(zs)-1):
            d = zs[i+1] - zs[i]
            delta = ((d - d_bulk) / d_bulk) * 100.0
            abs_d.append(abs(delta))
        return abs_d
    C_abs = get_abs_deltas(C_zs)[:3]
    Ti_abs = get_abs_deltas(Ti_zs)[:3]
    C_trend = C_abs[0] > C_abs[1] > C_abs[2]
    Ti_trend = Ti_abs[0] > Ti_abs[1] > Ti_abs[2]
    return 1.0 if (C_trend and Ti_trend) else 0.0


# === block: score_5 (check id='results_consistency') ===
def score_5(artifact, step, ctx):
    res = ctx.get('results')
    if not res:
        return 0.0
    # recompute values using same logic as scorers for a quick comparison
    # We'll re-extract from ctx, but we need intermediate recomputations.
    # Since prepare already extracted, we can compute again or store in ctx.
    # We'll store recomputed values in ctx after first scorer run? Not ideal.
    # Instead, we'll redo simple computations here.
    a = ctx.get('a')
    if a is None:
        return 0.0
    # DOS fermi (need to recompute)
    energy = ctx.get('dos_energy')
    values = ctx.get('dos_values')
    dos_fermi = None
    if energy and len(energy) >= 2:
        if 0.0 in energy:
            idx = energy.index(0.0)
            dos_fermi = values[idx]
        else:
            for i in range(len(energy)-1):
                if (energy[i] <= 0.0 <= energy[i+1]) or (energy[i+1] <= 0.0 <= energy[i]):
                    t = (0.0 - energy[i]) / (energy[i+1] - energy[i])
                    dos_fermi = values[i] + t * (values[i+1] - values[i])
                    break
    # Surface energy recompute
    sigma = None
    if ctx.get('slab7_energy') is not None and ctx.get('slab5_energy') is not None:
        E7 = ctx['slab7_energy']
        E5 = ctx['slab5_energy']
        dE = E7 - 3.5 * E5
        dE_J = dE * 13.605693 * 1.602176634e-19
        area_bohr2 = a / 0.5291772108
        area_m2 = (area_bohr2 * 5.291772108e-11) ** 2
        sigma = dE_J / (2 * area_m2)
    # Interlayer deltas
    C_deltas = []; Ti_deltas = []
    cell = ctx.get('slab7_cell')
    if cell:
        c_bohr = cell[2][2]
        c_A = c_bohr * 0.5291772108
        d_bulk = a / 2.0
        atoms = ctx.get('slab7_atoms', [])
        if atoms:
            sorted_atoms = sorted(atoms, key=lambda x: x[3])
            C_zs = []
            Ti_zs = []
            for sym, x, y, z in sorted_atoms:
                if sym == 'C':
                    C_zs.append(z * c_A)
                elif sym == 'Ti':
                    Ti_zs.append(z * c_A)
            for i in range(min(3, len(C_zs)-1)):
                d = C_zs[i+1] - C_zs[i]
                delta = ((d - d_bulk) / d_bulk) * 100.0
                C_deltas.append(delta)
            for i in range(min(3, len(Ti_zs)-1)):
                d = Ti_zs[i+1] - Ti_zs[i]
                delta = ((d - d_bulk) / d_bulk) * 100.0
                Ti_deltas.append(delta)
        else:
            C_deltas = [None]*3; Ti_deltas = [None]*3
    else:
        C_deltas = [None]*3; Ti_deltas = [None]*3
    # Compare with reported
    match_count = 0
    total_fields = 0
    # lattice constant
    if 'bulk_lattice_constant' in res:
        total_fields += 1
        if abs(res['bulk_lattice_constant'] - a) <= 0.1:
            match_count += 1
    # surface energy
    if 'surface_energy_7layer' in res and sigma is not None:
        total_fields += 1
        if abs(res['surface_energy_7layer'] - sigma) <= 0.2:
            match_count += 1
    # DOS Fermi
    if 'total_DOS_at_Fermi' in res and dos_fermi is not None:
        total_fields += 1
        if abs(res['total_DOS_at_Fermi'] - dos_fermi) <= 0.3:
            match_count += 1
    # interlayer spacings
    if 'interlayer_spacings' in res and isinstance(res['interlayer_spacings'], list):
        for entry in res['interlayer_spacings']:
            species = entry.get('species')
            pair = entry.get('layer_pair')
            dp = entry.get('delta_percent')
            if species == 'C' and pair in ('12','23','34'):
                idx = int(pair[1])-1
                if idx < len(C_deltas) and C_deltas[idx] is not None:
                    total_fields += 1
                    if abs(dp - C_deltas[idx]) <= 2.0:
                        match_count += 1
            elif species == 'Ti' and pair in ('12','23','34'):
                idx = int(pair[1])-1
                if idx < len(Ti_deltas) and Ti_deltas[idx] is not None:
                    total_fields += 1
                    if abs(dp - Ti_deltas[idx]) <= 2.0:
                        match_count += 1
    if total_fields == 0:
        return 0.0
    return match_count / total_fields


_SCORERS = {
    'lattice': score_0,
    'dos_fermi': score_1,
    'surface_energy': score_2,
    'interlayer_accuracy': score_3,
    'interlayer_trend': score_4,
    'results_consistency': score_5,
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
