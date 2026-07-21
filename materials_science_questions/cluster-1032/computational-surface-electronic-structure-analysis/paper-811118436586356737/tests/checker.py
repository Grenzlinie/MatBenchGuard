import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from numpy.linalg import norm
import os

def point_in_polygon(poly, point):
    # Ray casting algorithm for 2D polygon (closed or not, we close).
    # poly is Nx2 array, point is (x, y).
    x, y = point
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


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
    import json
    import os

    def prep(outputs_dir, spec):
        bulk_path = os.path.join(outputs_dir, 'bulk_band_structure.json')
        with open(bulk_path) as f:
            bulk = json.load(f)
        node_line = np.array(bulk['node_line_points'])
        # Find Z point in kpath
        Z_gap = None
        for i, pkt in enumerate(bulk['kpath']):
            if pkt['label'].upper() == 'Z' and len(pkt['k']) == 3:
                evals = np.sort(bulk['eigenvalues'][i])
                Z_gap = float(evals[2] - evals[1])
                break
        return {'node_line_points': node_line, 'Z_gap': Z_gap}


# === block: score_0 (check id='bulk_band_inversion') ===
def score_0(artifact, step, ctx):
    Z_gap = ctx.get('Z_gap')
    if Z_gap is None:
        return 0.0
    # Band inversion: gap must be negative. Score 1.0 if gap <= -0.03 eV, 0.5 if <0 but > -0.03, else 0.
    if Z_gap <= -0.03:
        return 1.0
    elif Z_gap < 0.0:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='bulk_node_line') ===
def score_1(artifact, step, ctx):
    node_line = ctx['node_line_points']
    if len(node_line) < 4:
        return 0.0
    # Check k_x ≈ 0 (within 0.02)
    if np.any(np.abs(node_line[:, 0]) > 0.02):
        return 0.0
    # Project to (k_y, k_z)
    poly = node_line[:, 1:3]
    # Close polygon if needed: add first point at end if distance > 1e-10
    dist = np.linalg.norm(poly[0] - poly[-1])
    if dist > 1e-10:
        poly = np.vstack([poly, poly[0]])
    # Test if Z = (0, 0.5) is inside
    Z_point = (0.0, 0.5)
    inside = point_in_polygon(poly, Z_point)
    return 1.0 if inside else 0.0


# === block: score_2 (check id='berry_phase_zigzag') ===
def score_2(artifact, step, ctx):
    k_par = np.array(artifact['k_parallel'])
    bphases = np.array(artifact['berry_phase'])
    if len(k_par) == 0 or len(bphases) != len(k_par):
        return 0.0
    node_line = ctx['node_line_points']
    # Use bulk node line projected to (k_y, k_z) as boundary
    poly = node_line[:, 1:3]
    # close polygon
    dist = np.linalg.norm(poly[0] - poly[-1])
    if dist > 1e-10:
        poly = np.vstack([poly, poly[0]])
    # Classify each k point
    correct = 0.0
    for k, ph in zip(k_par, bphases):
        # k_par is [k2, k3]
        inside = point_in_polygon(poly, (k[0], k[1]))
        if inside:
            expected = 0.0
            tol = 0.25
        else:
            expected = 1.0
            tol = 0.25
        if abs(ph - expected) <= tol:
            correct += 1.0
    total = len(k_par)
    fraction = correct / total
    # Linear score from 0.5 to 1.0 mapped to 0.0 to 1.0
    score = max(0.0, (fraction - 0.5) / 0.5)
    return min(score, 1.0)


# === block: score_3 (check id='surface_band_beard') ===
def score_3(artifact, step, ctx):
    k_path = np.array(artifact['k_path'])
    eigenvalues = np.array(artifact['eigenvalues'])
    if len(k_path) == 0 or len(eigenvalues) == 0:
        return 0.0
    node_line = ctx['node_line_points']
    poly = node_line[:, 1:3]
    dist = np.linalg.norm(poly[0] - poly[-1])
    if dist > 1e-10:
        poly = np.vstack([poly, poly[0]])
    # Find k-points inside the projected node line
    inside_idx = [i for i, k in enumerate(k_path) if point_in_polygon(poly, (k[0], k[1]))]
    if not inside_idx:
        return 0.0
    # Extract eigenvalues for those points
    evals_inside = eigenvalues[inside_idx]  # shape (num_inside, num_bands)
    # Compute std for each band
    stds = np.std(evals_inside, axis=0)
    min_std = float(np.min(stds))
    # Score based on min_std: full credit if <= 0.02 eV, linear decay to 0 at 0.08 eV
    score = max(0.0, 1.0 - min_std / 0.08)
    return min(score, 1.0)


_SCORERS = {
    'bulk_band_inversion': score_0,
    'bulk_node_line': score_1,
    'berry_phase_zigzag': score_2,
    'surface_band_beard': score_3,
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
