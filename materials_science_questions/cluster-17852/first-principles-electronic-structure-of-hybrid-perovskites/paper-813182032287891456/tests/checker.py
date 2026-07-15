import os
import json
import csv

# === author imports / helpers ===
import csv
import io
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


# === block: score_0 (check id='step_01_lattice') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    # Build lookup by functional
    data_by_func = {r.get('functional','').strip(): r for r in rows}
    gold = step['gold_data']
    tol = step['tolerance']
    score_per_row = []
    for g in gold:
        f = g['functional']
        if f not in data_by_func:
            score_per_row.append(0.0)
            continue
        row = data_by_func[f]
        try:
            a = float(row.get('a_A',0))
            b = float(row.get('b_A',0))
            c = float(row.get('c_A',0))
            v = float(row.get('volume_A3',0))
        except (ValueError, TypeError):
            score_per_row.append(0.0)
            continue
        ok_a = abs(a - g['a_A']) <= tol['a_A']
        ok_b = abs(b - g['b_A']) <= tol['b_A']
        ok_c = abs(c - g['c_A']) <= tol['c_A']
        ok_v = abs(v - g['volume_A3']) <= tol['volume_A3']
        # Partial credit: fraction of within-tolerance values
        frac = (ok_a + ok_b + ok_c + ok_v) / 4.0
        score_per_row.append(frac)
    if not score_per_row:
        return 0.0
    return sum(score_per_row) / len(score_per_row)


# === block: score_1 (check id='step_02_band_gap') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    data_by_func = {r.get('functional','').strip(): r for r in rows}
    gold = step['gold_data']
    tol = step['tolerance']
    score_per_row = []
    for g in gold:
        f = g['functional']
        if f not in data_by_func:
            score_per_row.append(0.0)
            continue
        try:
            gap = float(data_by_func[f].get('band_gap_eV',0))
        except (ValueError, TypeError):
            score_per_row.append(0.0)
            continue
        if abs(gap - g['band_gap_eV']) <= tol:
            score_per_row.append(1.0)
        else:
            score_per_row.append(0.0)
    if not score_per_row:
        return 0.0
    return sum(score_per_row) / len(score_per_row)


# === block: score_2 (check id='step_03_dos_recompute') ===
def score_2(artifact, step, ctx):
    text = artifact
    if not isinstance(text, str):
        return 0.0
    energies = []
    dos_vals = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 2:
            try:
                e = float(parts[0])
                d = float(parts[1])
                energies.append(e)
                dos_vals.append(d)
            except (ValueError, TypeError):
                continue
    if len(energies) < 10:
        return 0.0
    max_dos = max(dos_vals)
    threshold = max_dos * step['dos_threshold_fraction']
    # Find the widest energy gap where DOS < threshold
    sorted_pairs = sorted(zip(energies, dos_vals))
    gap_start = None
    gap_end = None
    max_gap = 0.0
    for e, d in sorted_pairs:
        if d < threshold:
            if gap_start is None:
                gap_start = e
            gap_end = e
        else:
            if gap_start is not None and gap_end is not None:
                width = gap_end - gap_start
                if width > max_gap:
                    max_gap = width
            gap_start = None
            gap_end = None
    if gap_start is not None and gap_end is not None:
        width = gap_end - gap_start
        if width > max_gap:
            max_gap = width
    estimated_gap = max_gap
    target = step['gold_gap_eV']
    max_dev = step['max_allowed_deviation']
    decay_range = step['decay_range']
    error = abs(estimated_gap - target)
    if error <= max_dev:
        return 1.0
    elif error >= max_dev + decay_range:
        return 0.0
    else:
        return max(0.0, 1.0 - (error - max_dev) / decay_range)


# === block: score_3 (check id='step_04_pdos_structural') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    # Group by (atom, orbital) collect (energy, pdos)
    groups = {}
    for r in rows:
        atom = r.get('atom','').strip()
        orb = r.get('orbital','').strip()
        try:
            e = float(r.get('energy_eV',0))
            pd = float(r.get('pdos',0))
        except (ValueError, TypeError):
            continue
        key = (atom, orb)
        groups.setdefault(key, []).append((e, pd))
    # Check I1 p and I2 p
    atoms_of_interest = step.get('atoms_of_interest', [])
    energy_window = step.get('energy_window', [-2.0, 0.0])
    def peak_energy(atom, orbital):
        key = (atom, orbital)
        if key not in groups:
            return None
        pair_list = groups[key]
        # find global maximum pdos within energy_window
        best_e = None
        best_pd = -float('inf')
        for e, pd in pair_list:
            if energy_window[0] <= e <= energy_window[1]:
                if pd > best_pd:
                    best_pd = pd
                    best_e = e
        if best_e is None:
            # window may be too narrow; use full range
            for e, pd in pair_list:
                if pd > best_pd:
                    best_pd = pd
                    best_e = e
            return best_e
        return best_e
    e_I1 = peak_energy('I1','p')
    e_I2 = peak_energy('I2','p')
    if e_I1 is None or e_I2 is None:
        return 0.0
    # I2 peak should be at higher energy (closer to Fermi, i.e., less negative)
    if e_I2 > e_I1:
        return 1.0
    else:
        return 0.0


# === block: score_4 (check id='step_05_band_structure') ===
def score_4(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    # Determine band columns (exclude first four)
    headers = list(rows[0].keys())
    band_cols = []
    for h in headers:
        if h not in ('kpoint_index','kx','ky','kz'):
            band_cols.append(h)
    if not band_cols:
        return 0.0
    kpoints = []
    eigenvalues = []  # list of lists of (kpt, energies)
    for row in rows:
        try:
            kx = float(row.get('kx',0))
            ky = float(row.get('ky',0))
            kz = float(row.get('kz',0))
        except (ValueError, TypeError):
            continue
        bands = []
        for c in band_cols:
            try:
                bands.append(float(row.get(c,0)))
            except (ValueError, TypeError):
                continue
        bands.sort()
        kpoints.append((kx, ky, kz, bands))
    if not kpoints:
        return 0.0
    # Compute direct gaps
    min_gap = float('inf')
    gamma_gap = None
    for kx, ky, kz, bands in kpoints:
        # Find largest gap between consecutive sorted eigenvalues
        gap = float('inf')
        for i in range(len(bands)-1):
            diff = bands[i+1] - bands[i]
            if diff > 0:
                gap = min(gap, diff)
        # gap is the direct gap at this kpt
        if gap < min_gap:
            min_gap = gap
        # Check if point is Gamma (0,0,0) within tolerance
        if abs(kx) < 1e-6 and abs(ky) < 1e-6 and abs(kz) < 1e-6:
            gamma_gap = gap
    if min_gap == float('inf'):
        return 0.0
    # The minimum direct gap should be at Gamma (or gamma gap close to min_gap)
    if gamma_gap is not None and gamma_gap <= min_gap + 1e-6:
        return 1.0
    else:
        # If no exact gamma point found, we can't confirm; score 0
        return 0.0


# === block: score_5 (check id='step_06_bader') ===
def score_5(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    gold = step['gold_data']
    tol = step['tolerance']
    # Build lookup from (functional, atom_type) to charge
    data_map = {}
    for r in rows:
        func = r.get('functional','').strip()
        at = r.get('atom_type','').strip()
        try:
            ch = float(r.get('charge_e',0))
        except (ValueError, TypeError):
            continue
        data_map[(func, at)] = ch
    score_count = 0
    total = 0
    for g in gold:
        func = g['functional']
        at = g['atom_type']
        key = (func, at)
        if key in data_map:
            total += 1
            if abs(data_map[key] - g['charge_e']) <= tol:
                score_count += 1
    if total == 0:
        return 0.0
    return score_count / total


_SCORERS = {
    'step_01_lattice': score_0,
    'step_02_band_gap': score_1,
    'step_03_dos_recompute': score_2,
    'step_04_pdos_structural': score_3,
    'step_05_band_structure': score_4,
    'step_06_bader': score_5,
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
