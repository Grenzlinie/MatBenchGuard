import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def compute_omega(qvec, k1, k2, a, M, omega0):
    """
    qvec: wavevector in 1/m (Cartesian)
    Returns sorted dimensionless frequencies Omega for 3 branches.
    """
    # nearest neighbors
    nn_vecs = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]) * a
    D = np.zeros((3,3), dtype=complex)
    for d in nn_vecs:
        phase = np.dot(qvec, d)
        factor = 1 - np.exp(1j * phase)
        d_hat = d / a
        D += k1 * factor * np.outer(d_hat, d_hat)
    # next-nearest neighbors
    nnn_vecs = np.array([[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0],
                         [1,0,1],[1,0,-1],[-1,0,1],[-1,0,-1],
                         [0,1,1],[0,1,-1],[0,-1,1],[0,-1,-1]]) * a
    for d in nnn_vecs:
        phase = np.dot(qvec, d)
        factor = 1 - np.exp(1j * phase)
        d_hat = d / (np.sqrt(2) * a)
        D += k2 * factor * np.outer(d_hat, d_hat)
    D /= M
    # D is hermitian real symmetric; take real part
    evals = np.linalg.eigvalsh(D.real)
    omega_vals = np.sqrt(np.abs(evals))
    Omega = omega_vals / omega0
    return np.sort(Omega)


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
    import os, json
    ctx = {}
    # physical constants
    ctx['a'] = 3.36e-10
    ctx['M'] = 3.49e-25
    ctx['omega0'] = 10.45e12
    # attempted load of force constants from agent submission
    fc_path = os.path.join(outputs_dir, 'force_constants.json')
    if os.path.exists(fc_path):
        with open(fc_path) as f:
            fc = json.load(f)
        ctx['k1_agent'] = fc.get('k1', None)
        ctx['k2_agent'] = fc.get('k2', None)
    else:
        ctx['k1_agent'] = None
        ctx['k2_agent'] = None
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    k1 = artifact.get('k1')
    k2 = artifact.get('k2')
    if k1 is None or k2 is None:
        return 0.0
    k1g = step['params']['k1_gold']
    k2g = step['params']['k2_gold']
    e1 = abs(k1 - k1g) / k1g if k1g != 0 else 1.0
    e2 = abs(k2 - k2g) / k2g if k2g != 0 else 1.0
    max_err = max(e1, e2)
    # full credit if relative error <= 2%, zero if >= 10%
    score = min(1.0, max(0.0, (0.10 - max_err) / 0.08))
    return float(score)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import csv
    from collections import defaultdict

    tol = step['params'].get('tolerance', 0.01)
    if ctx.get('k1_agent') is None or ctx.get('k2_agent') is None:
        return 0.0

    k1 = ctx['k1_agent']
    k2 = ctx['k2_agent']
    a = ctx['a']
    M = ctx['M']
    omega0 = ctx['omega0']

    # parse CSV artifact (list of dicts)
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # group by direction and q_norm
    by_q = defaultdict(list)
    for row in artifact:
        direction = row.get('direction')
        q_norm = float(row.get('q_norm', 0))
        branch = int(row.get('branch', 1))
        Omega = float(row.get('Omega', 0.0))
        by_q[(direction, q_norm)].append(Omega)

    max_err = 0.0
    n_points = 0
    for (direction, qn), omegas in by_q.items():
        if len(omegas) != 3:
            continue
        agent_omegas = sorted(omegas)
        # map direction to wave vector
        qval = qn * np.pi
        if direction == '[100]':
            qvec = np.array([qval, 0.0, 0.0])
        elif direction == '[110]':
            qvec = np.array([qval, qval, 0.0])
        elif direction == '[111]':
            qvec = np.array([qval, qval, qval])
        else:
            continue
        expected_omegas = compute_omega(qvec, k1, k2, a, M, omega0)
        errs = np.abs(expected_omegas - np.array(agent_omegas))
        max_err = max(max_err, np.max(errs))
        n_points += 1

    if n_points == 0:
        return 0.0
    score = max(0.0, 1.0 - max_err / tol)
    return float(score)


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    from collections import defaultdict
    import csv
    import math

    tol = step['params'].get('tolerance', 0.02)
    if ctx.get('k1_agent') is None or ctx.get('k2_agent') is None:
        return 0.0

    k1 = ctx['k1_agent']
    k2 = ctx['k2_agent']
    a = ctx['a']
    M = ctx['M']
    omega0 = ctx['omega0']

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # For each unique q_010, compute projected bulk band range
    # by sampling qz from 0 to pi
    qz_vals = np.linspace(0, np.pi, 201)
    points_by_q = defaultdict(list)
    for row in artifact:
        qy = float(row.get('q_010', 0.0))
        Omega = float(row.get('Omega', 0.0))
        mode_type = row.get('mode_type', '')
        points_by_q[qy].append((Omega, mode_type))

    correct = 0
    total = 0
    for qy, entries in points_by_q.items():
        # compute bulk projection for this qy
        bulk_omegas = []
        for qz in qz_vals:
            qvec = np.array([0.0, qy * np.pi, qz])
            omegas_3 = compute_omega(qvec, k1, k2, a, M, omega0)
            bulk_omegas.extend(omegas_3)
        min_bulk = min(bulk_omegas)
        max_bulk = max(bulk_omegas)
        for Omega, mtype in entries:
            if mtype == 'Rayleigh':
                if Omega < min_bulk - tol:
                    correct += 1
            elif mtype == 'resonance':
                if min_bulk - tol <= Omega <= max_bulk + tol:
                    correct += 1
            else:
                # unknown mode type, skip or treat as correct?
                pass
            total += 1

    if total == 0:
        return 0.0
    score = correct / total
    return float(score)


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    import numpy as np

    if not isinstance(artifact, list) or len(artifact) < 3:
        return 0.0

    # Extract arrays
    omega_vals = []
    bulk_v = []
    surf_v = []
    for row in artifact:
        omega_vals.append(float(row.get('Omega', 0.0)))
        bulk_v.append(float(row.get('bulk_VDOS', 0.0)))
        surf_v.append(float(row.get('surface_VDOS', 0.0)))
    omega_arr = np.array(omega_vals)
    bulk_arr = np.array(bulk_v)
    surf_arr = np.array(surf_v)

    # Non-negative check
    if np.any(bulk_arr < -1e-12) or np.any(surf_arr < -1e-12):
        return 0.0

    # Integration (area under curve)
    area_bulk = np.trapezoid(bulk_arr, omega_arr)
    area_surf = np.trapezoid(surf_arr, omega_arr)
    if area_bulk <= 1e-12 or area_surf <= 1e-12:
        return 0.0

    # High-frequency region: Omega > 1.5
    mask_high = omega_arr > 1.5
    if not np.any(mask_high):
        return 0.0

    high_bulk_frac = np.trapezoid(bulk_arr[mask_high], omega_arr[mask_high]) / area_bulk
    high_surf_frac = np.trapezoid(surf_arr[mask_high], omega_arr[mask_high]) / area_surf

    # Condition 1: surface has more high-frequency weight
    cond1 = high_surf_frac > high_bulk_frac

    # Condition 2: surface peak > bulk peak at that Omega
    idx_peak_surf = np.argmax(surf_arr)
    cond2 = surf_arr[idx_peak_surf] > bulk_arr[idx_peak_surf]

    score = 0.0
    if cond1 and cond2:
        score = 1.0
    elif cond1 or cond2:
        score = 0.5
    return float(score)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
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
