import os
import json
import csv

# === author imports / helpers ===
import numpy as np

# DGS model function (recompute S for a single (distance, diameter) point)
def compute_S(dist_mm, diam_mm, freq_MHz, c_mm_per_us, width_mm, height_mm, dx_mm, dy_mm, dr_mm=0.2, n_angular=36):
    if diam_mm <= 0:
        return 0.0
    nx = max(1, int(round(width_mm / dx_mm)))
    ny = max(1, int(round(height_mm / dy_mm)))
    xp = (np.arange(nx) - (nx-1)/2.0) * dx_mm
    yp = (np.arange(ny) - (ny-1)/2.0) * dy_mm
    radius = diam_mm / 2.0
    nr = max(1, int(round(radius / dr_mm)))
    r_edges = np.linspace(0.0, radius, nr+1)
    r_c = 0.5*(r_edges[:-1] + r_edges[1:])
    dr = r_edges[1] - r_edges[0]
    dtheta = 2*np.pi / n_angular
    theta = (np.arange(n_angular) + 0.5) * dtheta
    xr = (r_c[:, None] * np.cos(theta[None, :])).ravel()
    yr = (r_c[:, None] * np.sin(theta[None, :])).ravel()
    area_r = (r_c[:, None] * dr * dtheta).ravel()
    xp_flat = np.tile(xp[:, None], (1, ny)).ravel()
    yp_flat = np.tile(yp[None, :], (nx, 1)).ravel()
    dx_vec = xp_flat[:, None] - xr[None, :]
    dy_vec = yp_flat[:, None] - yr[None, :]
    rho = np.sqrt(dx_vec**2 + dy_vec**2 + dist_mm**2)
    w = (dist_mm / rho)**4
    freq_Hz = freq_MHz * 1e6
    c_mm_per_s = c_mm_per_us * 1e6
    phase = (2 * np.pi * freq_Hz / c_mm_per_s) * rho
    A = w * np.exp(-1j * phase) / rho * dx_mm * dy_mm * area_r[None, :]
    C = np.sum(A, axis=0)
    S_val = np.abs(np.sum(C**2))
    return S_val

# Evaluate DGS artifact against recomputed hidden reference
def evaluate_dgs(artifact, step):
    freq_MHz = step['freq_MHz']
    c_mm_per_us = step['c_mm_per_us']
    width_mm = step['width_mm']
    height_mm = step['height_mm']
    dx_mm = step['dx_mm']
    dy_mm = step['dy_mm']
    dr_mm = step.get('dr_mm', 0.2)
    n_angular = step.get('n_angular', 36)
    tolerance_db = step.get('tolerance_db', 2.0)
    test_points = step['test_points']
    # build lookup from agent CSV
    lookup = {}
    for row in artifact:
        lookup[(float(row['distance_mm']), float(row['diameter_mm']))] = float(row['signal_dB'])
    # compute max_S by sampling coarse grid
    dist_grid = np.linspace(5, 600, 30)
    diam_grid = np.linspace(0.5, 20, 25)
    max_S = 0.0
    for dd in dist_grid:
        for ddiam in diam_grid:
            S = compute_S(dd, ddiam, freq_MHz, c_mm_per_us, width_mm, height_mm, dx_mm, dy_mm, dr_mm, n_angular)
            if S > max_S:
                max_S = S
    if max_S == 0.0:
        max_S = 1e-12
    scores = []
    for dist, diam in test_points:
        key = (float(dist), float(diam))
        agent_db = lookup.get(key)
        if agent_db is None:
            scores.append(0.0)
            continue
        S_point = compute_S(dist, diam, freq_MHz, c_mm_per_us, width_mm, height_mm, dx_mm, dy_mm, dr_mm, n_angular)
        expected_db = 10.0 * np.log10(max(S_point, 1e-12) / max_S)
        diff = abs(agent_db - expected_db)
        if diff <= tolerance_db:
            scores.append(1.0)
        else:
            penalty = max(0.0, (diff - tolerance_db) / 5.0)
            scores.append(max(0.0, 1.0 - penalty))
    return np.mean(scores) if scores else 0.0


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


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    return evaluate_dgs(artifact, step)


# === block: score_1 (check id='step_2') ===
def score_1(artifact, step, ctx):
    # step_2 repair: recompute with converged discretization.
    freq = step['freq_MHz']
    c = step['c_mm_per_us']
    w = step['width_mm']
    h = step['height_mm']
    test_points = step['test_points']
    tol_db = step.get('tolerance_db', 2.0)

    dx_fine = 0.2
    dy_fine = 0.2
    dr_fine = 0.05
    n_ang = 72

    lookup = {}
    for row in artifact:
        lookup[(float(row['distance_mm']), float(row['diameter_mm']))] = float(row['signal_dB'])

    # Dense max_S search
    dist_grid = np.linspace(5, 600, 60)
    diam_grid = np.linspace(0.5, 20, 40)
    max_S = 0.0
    for dd in dist_grid:
        for ddiam in diam_grid:
            S = compute_S(dd, ddiam, freq, c, w, h, dx_fine, dy_fine, dr_fine, n_ang)
            if S > max_S:
                max_S = S
    if max_S == 0.0:
        max_S = 1e-12

    scores = []
    for dist, diam in test_points:
        key = (float(dist), float(diam))
        agent_db = lookup.get(key)
        if agent_db is None:
            scores.append(0.0)
            continue
        S_pt = compute_S(dist, diam, freq, c, w, h, dx_fine, dy_fine, dr_fine, n_ang)
        expected_db = 10.0 * np.log10(max(S_pt, 1e-12) / max_S)
        diff = abs(agent_db - expected_db)
        if diff <= tol_db:
            scores.append(1.0)
        else:
            penalty = max(0.0, (diff - tol_db) / 5.0)
            scores.append(max(0.0, 1.0 - penalty))
    return np.mean(scores) if scores else 0.0


# === block: score_2 (check id='step_3') ===
def score_2(artifact, step, ctx):
    # step_3 repair: recompute with converged discretization.
    freq = step['freq_MHz']
    c = step['c_mm_per_us']
    w = step['width_mm']
    h = step['height_mm']
    test_points = step['test_points']
    tol_db = step.get('tolerance_db', 2.0)

    dx_fine = 0.2
    dy_fine = 0.2
    dr_fine = 0.05
    n_ang = 72

    lookup = {}
    for row in artifact:
        lookup[(float(row['distance_mm']), float(row['diameter_mm']))] = float(row['signal_dB'])

    # Dense max_S search
    dist_grid = np.linspace(5, 600, 60)
    diam_grid = np.linspace(0.5, 20, 40)
    max_S = 0.0
    for dd in dist_grid:
        for ddiam in diam_grid:
            S = compute_S(dd, ddiam, freq, c, w, h, dx_fine, dy_fine, dr_fine, n_ang)
            if S > max_S:
                max_S = S
    if max_S == 0.0:
        max_S = 1e-12

    scores = []
    for dist, diam in test_points:
        key = (float(dist), float(diam))
        agent_db = lookup.get(key)
        if agent_db is None:
            scores.append(0.0)
            continue
        S_pt = compute_S(dist, diam, freq, c, w, h, dx_fine, dy_fine, dr_fine, n_ang)
        expected_db = 10.0 * np.log10(max(S_pt, 1e-12) / max_S)
        diff = abs(agent_db - expected_db)
        if diff <= tol_db:
            scores.append(1.0)
        else:
            penalty = max(0.0, (diff - tol_db) / 5.0)
            scores.append(max(0.0, 1.0 - penalty))
    return np.mean(scores) if scores else 0.0


_SCORERS = {
    'step_1': score_0,
    'step_2': score_1,
    'step_3': score_2,
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
