import os
import json
import csv

# === author imports / helpers ===
import math, itertools


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


# === block: score_0 (check id='step_compute_magnetization') ===
def score_0(artifact, step, ctx):
    import math, itertools

    tol = step.get('tolerance', 0.05)
    threshold_frac = step.get('correct_fraction_threshold', 0.8)

    rows = artifact
    if not rows:
        return 0.0

    # --- Physics constants ---
    kB = 1.380649e-23
    mu0 = 4.0 * math.pi * 1e-7
    muB = 9.274009e-24
    M_per_cluster = 5.4  # muB
    H_Oe_to_A_per_m = 79.5774715

    # Hamiltonian parameters
    J11 = 0.9e-23
    # J11/J12 = -1.96 => J12 = J11 / (-1.96)
    J12 = J11 / (-1.96)   # negative, magnitude ~ 0.459e-23
    EMAE = 3.04e-26
    D12 = 1.5e-23

    # --- Spin state vectors (5 orientations) ---
    # 0: +x, 1: -x, 2: +y, 3: -y, 4: +z
    spin_vecs = [
        (1.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, -1.0, 0.0),
        (0.0, 0.0, 1.0),
    ]

    # --- Lattice (4x2 rectangular grid) ---
    positions = [
        (0,0), (1,0), (2,0), (3,0),
        (0,1), (1,1), (2,1), (3,1)
    ]
    n_clusters = 8

    # --- Build bond lists ---
    bonds = []
    for i in range(n_clusters):
        for j in range(i+1, n_clusters):
            dx = positions[i][0] - positions[j][0]
            dy = positions[i][1] - positions[j][1]
            dist = math.sqrt(dx*dx + dy*dy)
            # Nearest neighbours (distance 1) -> J12 (90° bonds)
            if abs(dist - 1.0) < 1e-9:
                bonds.append((i, j, 'J12'))
            # Second-nearest neighbours (distance sqrt(2)) -> J11 (180° bonds)
            elif abs(dist - math.sqrt(2)) < 1e-9:
                bonds.append((i, j, 'J11'))

    # --- Precompute pair energies for each bond type and DMI flag ---
    # exchange: -J * dot(s_i, s_j)
    # DMI: -D * sin(theta) with sin = sqrt(1 - dot^2)
    # Only J12 bonds get DMI (all are surface here)
    def dot(s1, s2):
        return s1[0]*s2[0] + s1[1]*s2[1] + s1[2]*s2[2]

    def sin_theta(s1, s2):
        d = dot(s1, s2)
        d = max(-1.0, min(1.0, d))
        return math.sqrt(1.0 - d*d)

    bond_energy_ex = {}   # (bond_type, s1, s2) -> exchange energy
    bond_energy_dmi = {}  # (bond_type, s1, s2) -> DMI energy (only for J12)
    for btype in ('J11', 'J12'):
        Jval = J11 if btype == 'J11' else J12
        for s1 in range(5):
            for s2 in range(5):
                v1 = spin_vecs[s1]
                v2 = spin_vecs[s2]
                cos_t = dot(v1, v2)
                bond_energy_ex[(btype, s1, s2)] = -Jval * cos_t
                if btype == 'J12':
                    sin_t = sin_theta(v1, v2)
                    bond_energy_dmi[(btype, s1, s2)] = -D12 * sin_t
                else:
                    bond_energy_dmi[(btype, s1, s2)] = 0.0

    # --- Anisotropy: easy axis +x, penalty EMAE if not aligned ---
    def anisotropy_energy(s_idx):
        v = spin_vecs[s_idx]
        if v[0] < 0.999:
            return EMAE
        return 0.0

    # --- Precompute per-configuration base energy (no Zeeman) and sum_cos ---
    # Iterate over all 5^8 configurations
    base_energies = []
    sum_cos_vals = []

    for config in itertools.product(range(5), repeat=n_clusters):
        spins = list(config)
        # Exchange + DMI
        e = 0.0
        for (i, j, btype) in bonds:
            s1 = spins[i]
            s2 = spins[j]
            e += bond_energy_ex[(btype, s1, s2)]
            if btype == 'J12':
                e += bond_energy_dmi[(btype, s1, s2)]
        # Anisotropy
        for s in spins:
            e += anisotropy_energy(s)
        # sum_cos (projection onto field direction = +x)
        sc = sum(spin_vecs[s][0] for s in spins)
        base_energies.append(e)
        sum_cos_vals.append(sc)

    n_configs = len(base_energies)

    # --- Expected (T,H) points ---
    fields = [200, 500, 1000]
    temps = list(range(2, 31))   # 2..30 inclusive

    expected = {}  # (T, H) -> magnetization

    # Precompute Zeeman coefficient C_H = mu0 * M_per_cluster * muB * H
    M_per_cluster_SI = M_per_cluster * muB  # J/T
    for H in fields:
        H_SI = H * H_Oe_to_A_per_m   # A/m
        C_H = mu0 * M_per_cluster_SI * H_SI   # J
        for T in temps:
            numer = 0.0
            denom = 0.0
            beta = 1.0 / (kB * T)
            for idx in range(n_configs):
                e_base = base_energies[idx]
                sc = sum_cos_vals[idx]
                e_total = e_base - C_H * sc
                # clamp exponent to prevent overflow
                exp_val = math.exp(-e_total * beta)
                numer += sc * exp_val  # total moment in units of M_per_cluster
                denom += exp_val
            avg_moment = numer / denom   # in units of M_per_cluster per config?
            # normalized magnetization = avg_moment / (n_clusters)
            norm_m = avg_moment / n_clusters
            expected[(T, H)] = norm_m

    # --- Compare with agent's rows ---
    present = set()
    agent = {}
    for row in rows:
        try:
            T_val = float(row['Temperature_K'])
            H_val = int(row['Field_Oe'])
            norm = float(row['Normalized_Magnetization'])
        except (ValueError, KeyError):
            continue
        agent[(T_val, H_val)] = norm
        present.add((T_val, H_val))

    # Count correct matches
    total_points = 0
    correct = 0
    for T in temps:
        for H in fields:
            key = (T, H)
            total_points += 1
            if key not in present:
                continue
            diff = abs(agent[key] - expected[key])
            if diff <= tol:
                correct += 1

    if total_points == 0:
        return 0.0

    frac = correct / total_points
    # Partial credit: fraction correct, or full if >= threshold
    if frac >= threshold_frac:
        return 1.0
    else:
        # Linear scaling below threshold, never below 0
        return max(0.0, frac / threshold_frac)


_SCORERS = {
    'step_compute_magnetization': score_0,
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
