import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
from collections import defaultdict
import os


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
        'output_dir': outputs_dir,
        'params': {
            'V':  {'Zd':3.50, 'Rd':1.85, 'nd':20.95},
            'Cr': {'Zd':4.50, 'Rd':1.70, 'nd':9.52},
            'Mn': {'Zd':5.50, 'Rd':1.63, 'nd':21.23},
            'Fe': {'Zd':6.50, 'Rd':1.51, 'nd':41.63}
        },
        'Nc': {'bcc':8, 'fcc':12, 'hcp':12},
        'kB_Ryd': 6.3336e-6,
        'T': 300.0
    }


# === block: score_0 (check id='free_energies_correctness') ===
def score_0(artifact, step, ctx):
    # Atomic volumes from paper Table 1 (atomic units)
    atomic_volumes = {
        'V': 93.54,
        'Cr': 81.54,
        'Mn': 82.59,
        'Fe': 79.48,
    }

    # Precompute fractional shells (distances in units of lattice constant a) for each structure

    def _build_shells_bcc(max_dist=5.0, max_shells=12):
        pts = []
        for i in range(-5, 6):
            for j in range(-5, 6):
                for k in range(-5, 6):
                    if i == 0 and j == 0 and k == 0:
                        continue
                    d = (i**2 + j**2 + k**2)**0.5
                    if d <= max_dist:
                        pts.append(d)
                    d2 = ((i+0.5)**2 + (j+0.5)**2 + (k+0.5)**2)**0.5
                    if d2 <= max_dist:
                        pts.append(d2)
        cnt = {}
        for d in pts:
            r = round(d, 8)
            cnt[r] = cnt.get(r, 0) + 1
        sorted_dists = sorted(cnt.items())
        return [(d, c) for d, c in sorted_dists[:max_shells]]

    def _build_shells_fcc(max_dist=5.0, max_shells=12):
        pts = []
        for i in range(-5, 6):
            for j in range(-5, 6):
                for k in range(-5, 6):
                    if i == 0 and j == 0 and k == 0:
                        continue
                    d0 = (i**2 + j**2 + k**2)**0.5
                    d1 = ((i+0.5)**2 + (j+0.5)**2 + k**2)**0.5
                    d2 = ((i+0.5)**2 + j**2 + (k+0.5)**2)**0.5
                    d3 = (i**2 + (j+0.5)**2 + (k+0.5)**2)**0.5
                    for d in (d0, d1, d2, d3):
                        if d <= max_dist:
                            pts.append(d)
        cnt = {}
        for d in pts:
            r = round(d, 8)
            cnt[r] = cnt.get(r, 0) + 1
        sorted_dists = sorted(cnt.items())
        return [(d, c) for d, c in sorted_dists[:max_shells]]

    def _build_shells_hcp(max_dist=5.0, max_shells=12):
        c_over_a = math.sqrt(8.0/3.0)
        a1 = (1.0, 0.0, 0.0)
        a2 = (0.5, math.sqrt(3)/2, 0.0)
        a3 = (0.0, 0.0, c_over_a)
        basis = [(0,0,0), (2/3, 1/3, 0.5)]
        pts = []
        for i in range(-5, 6):
            for j in range(-5, 6):
                for k in range(-5, 6):
                    tx = i*a1[0] + j*a2[0] + k*a3[0]
                    ty = i*a1[1] + j*a2[1] + k*a3[1]
                    tz = i*a1[2] + j*a2[2] + k*a3[2]
                    for b in basis:
                        x = tx + b[0]
                        y = ty + b[1]
                        z = tz + b[2]
                        d = (x**2 + y**2 + z**2)**0.5
                        if d > 0 and d <= max_dist:
                            pts.append(d)
        cnt = {}
        for d in pts:
            r = round(d, 8)
            cnt[r] = cnt.get(r, 0) + 1
        sorted_dists = sorted(cnt.items())
        return [(d, c) for d, c in sorted_dists[:max_shells]]

    FRAC_SHELLS = {
        'bcc': _build_shells_bcc(),
        'fcc': _build_shells_fcc(),
        'hcp': _build_shells_hcp(),
    }

    def lattice_constant(struct, omega):
        if struct == 'bcc':
            return (2 * omega) ** (1/3)
        elif struct == 'fcc':
            return (4 * omega) ** (1/3)
        elif struct == 'hcp':
            return (omega * math.sqrt(2)) ** (1/3)
        else:
            raise ValueError(struct)

    elements_params = ctx['params']
    Nc = ctx['Nc']
    kB_Ryd = ctx['kB_Ryd']
    T = ctx['T']

    # Compute T*Sd for each element
    T_Sd = {}
    for el, p in elements_params.items():
        nd = p['nd']
        T_Sd[el] = (math.pi**2 / 3.0) * (kB_Ryd**2) * nd * (T**2)

    rows = artifact
    total_rows = len(rows)
    if total_rows == 0:
        return 0.0

    dist_tol = 1e-4
    ud_tol = 0.001
    fd_tol = 0.001
    max_shells = 12

    ok_struct = 0
    ok_ud = 0
    ok_fd = 0

    for i, row in enumerate(rows):
        el = row['element']
        struct = row['structure']
        method = row['method']
        shell = int(row['shell'])  # 1-indexed
        R_agent = float(row['interatomic_distance'])
        N_agent = int(row['N_atoms'])
        Ud_agent = float(row['pair_potential_Ud'])
        Fd_agent = float(row['cumulative_free_energy_Fd'])

        omega = atomic_volumes.get(el)
        if omega is None:
            continue

        a = lattice_constant(struct, omega)
        frac_shells = FRAC_SHELLS[struct]
        if shell > len(frac_shells):
            continue  # no reference for this shell index => row fails structure check
        frac_ref, N_ref = frac_shells[shell-1]
        R_ref = frac_ref * a

        if abs(R_agent - R_ref) <= dist_tol and N_agent == N_ref:
            ok_struct += 1

            Zd = elements_params[el]['Zd']
            Rd = elements_params[el]['Rd']
            if method == 'Nc':
                factor = (12.0 / Nc[struct]) ** 0.5
            else:
                factor = (12.0 / N_ref) ** 0.5

            attractive = - (Zd * (1.0 - Zd/10.0) * factor * (56.12/math.pi) * (Rd**3) / (R_ref**5))
            repulsive = (450.0/(math.pi**2)) * Zd * (Rd**6) / (R_ref**8)
            dipole = ((1.0/137.0)**0.5) / (R_ref**3)
            Ud_ref = attractive + repulsive + dipole

            if abs(Ud_ref - Ud_agent) <= ud_tol:
                ok_ud += 1

            # recompute cumulative Fd up to this shell using reference distances and occupancies
            cum_Fd_ref = - T_Sd[el]
            for j in range(shell):
                r_frac_s, n_s = frac_shells[j]
                r_s = r_frac_s * a
                if method == 'Nc':
                    f = (12.0 / Nc[struct]) ** 0.5
                else:
                    f = (12.0 / n_s) ** 0.5
                Ud_s = - (Zd * (1.0 - Zd/10.0) * f * (56.12/math.pi) * (Rd**3) / (r_s**5)) \
                       + (450.0/(math.pi**2)) * Zd * (Rd**6) / (r_s**8) \
                       + ((1.0/137.0)**0.5) / (r_s**3)
                cum_Fd_ref += 0.5 * Ud_s * n_s

            if abs(cum_Fd_ref - Fd_agent) <= fd_tol:
                ok_fd += 1

    score = (ok_struct + ok_ud + ok_fd) / (3.0 * total_rows)
    return score


# === block: score_1 (check id='energy_differences_consistency') ===
def score_1(artifact, step, ctx):
    output_dir = ctx['output_dir']
    free_path = os.path.join(output_dir, 'free_energies.csv')
    free_data = load_artifact(free_path)
    if free_data is None:
        return 0.0

    # Build cumulative Fd lookup
    Fd = {}
    for row in free_data:
        key = (row['element'], row['structure'], row['method'], int(row['shell']))
        Fd[key] = float(row['cumulative_free_energy_Fd'])

    rows = artifact  # energy_differences.csv
    total = len(rows)
    if total == 0:
        return 0.0

    ok_consistency = 0
    # Collect deltas per (element, method) for convergence check
    deltas = defaultdict(lambda: {'fcc_bcc': [], 'fcc_hcp': []})
    for row in rows:
        el = row['element']
        method = row['method']
        shell = int(row['shell'])
        fd_fcc = Fd.get((el, 'fcc', method, shell))
        fd_bcc = Fd.get((el, 'bcc', method, shell))
        fd_hcp = Fd.get((el, 'hcp', method, shell))
        if fd_fcc is None or fd_bcc is None or fd_hcp is None:
            continue
        delta_fcc_bcc_expected = fd_fcc - fd_bcc
        delta_fcc_hcp_expected = fd_fcc - fd_hcp
        reported_delta_bcc = float(row['delta_F_fcc_bcc'])
        reported_delta_hcp = float(row['delta_F_fcc_hcp'])
        if (abs(delta_fcc_bcc_expected - reported_delta_bcc) <= 0.001 and
            abs(delta_fcc_hcp_expected - reported_delta_hcp) <= 0.001):
            ok_consistency += 1
        # store for convergence check
        deltas[(el, method)]['fcc_bcc'].append(reported_delta_bcc)
        deltas[(el, method)]['fcc_hcp'].append(reported_delta_hcp)

    # Convergence positivity: average over the last 5 shells (8-12) must be > 0
    # (only for combos that have data in that range)
    combos = 0
    ok_pos = 0
    for key, d in deltas.items():
        dbcc = d['fcc_bcc']
        dhcp = d['fcc_hcp']
        # take values with shell index in last 5 (approximation: last 5 values)
        # we don't have shell index preserved; we'll just take the last 5 entries
        # because input rows are sorted by shell
        last_bcc = dbcc[-5:] if len(dbcc) >= 5 else dbcc
        last_hcp = dhcp[-5:] if len(dhcp) >= 5 else dhcp
        if last_bcc and last_hcp:
            combos += 1
            if np.mean(last_bcc) > 0 and np.mean(last_hcp) > 0:
                ok_pos += 1

    consistency_score = ok_consistency / total if total > 0 else 0.0
    positivity_score = ok_pos / combos if combos > 0 else 1.0
    return 0.5 * consistency_score + 0.5 * positivity_score


_SCORERS = {
    'free_energies_correctness': score_0,
    'energy_differences_consistency': score_1,
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
