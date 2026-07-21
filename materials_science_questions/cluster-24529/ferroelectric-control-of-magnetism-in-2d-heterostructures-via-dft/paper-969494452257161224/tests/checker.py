import os
import json
import csv

# === author imports / helpers ===
import csv
import math
from collections import defaultdict


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
    a0 = spec['steps'][0]['parameters']['a0']
    pi = math.pi
    b1 = (2*pi/a0, -2*pi/(a0*math.sqrt(3)))
    b2 = (0, 4*pi/(a0*math.sqrt(3)))
    q1 = ((4*b1[0] - b2[0])/13, (4*b1[1] - b2[1])/13)
    q2 = ((b1[0] + 3*b2[0])/13, (b1[1] + 3*b2[1])/13)
    q3 = (-q1[0]-q2[0], -q1[1]-q2[1])
    expected_q = [q1, q2, q3, (-q1[0], -q1[1]), (-q2[0], -q2[1]), (-q3[0], -q3[1])]
    return {'expected_q': expected_q, 'tolerance': spec['steps'][0]['parameters']['tolerance_rad_per_ang'], 'rel_threshold': spec['steps'][0]['parameters']['rel_threshold']}


# === block: score_0 (check id='ldos_cdw_fft_check') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    # parse points
    points = []
    for row in artifact:
        try:
            x = float(row['x'])
            y = float(row['y'])
            ldos = float(row['integrated_LDOS'])
            points.append((x, y, ldos))
        except (KeyError, ValueError):
            return 0.0
    if not points:
        return 0.0

    # build regular grid
    xs = sorted(set(p[0] for p in points))
    ys = sorted(set(p[1] for p in points))
    if len(xs) < 3 or len(ys) < 3:
        return 0.0
    dx = xs[1] - xs[0]
    dy = ys[1] - ys[0]
    for i in range(1, len(xs)):
        if abs(xs[i] - xs[i-1] - dx) > 1e-3:
            return 0.0
    for j in range(1, len(ys)):
        if abs(ys[j] - ys[j-1] - dy) > 1e-3:
            return 0.0
    nx = len(xs)
    ny = len(ys)
    grid = [[0.0]*ny for _ in range(nx)]
    for (x, y, val) in points:
        ix = int(round((x - xs[0]) / dx))
        iy = int(round((y - ys[0]) / dy))
        if ix < 0 or ix >= nx or iy < 0 or iy >= ny:
            return 0.0
        grid[ix][iy] = val

    # Fourier amplitude at a single wavevector
    def amp(qx, qy):
        r = 0.0
        s = 0.0
        for ix in range(nx):
            x = xs[ix]
            row = grid[ix]
            for iy in range(ny):
                val = row[iy]
                phase = qx * x + qy * y
                r += val * math.cos(phase)
                s -= val * math.sin(phase)
        return math.sqrt(r*r + s*s)

    a0 = step['parameters']['a0']
    pi = math.pi
    b1 = (2*pi/a0, -2*pi/(a0*math.sqrt(3)))
    b2 = (0, 4*pi/(a0*math.sqrt(3)))

    # atomic reciprocal lattice vectors (six symmetric)
    atom_vecs = [b1, b2, (b1[0]+b2[0], b1[1]+b2[1]),
                 (-b1[0], -b1[1]), (-b2[0], -b2[1]),
                 (-b1[0]-b2[0], -b1[1]-b2[1])]

    tol = ctx['tolerance']
    rel_threshold = ctx['rel_threshold']

    # find maximum amplitude in a local window around (qx, qy)
    def max_amp_around(qx, qy, radius, npoints=5):
        maxv = 0.0
        step = 2*radius / (npoints-1) if npoints > 1 else 0.0
        for i in range(npoints):
            dqx = -radius + i*step
            for j in range(npoints):
                dqy = -radius + j*step
                if dqx*dqx + dqy*dqy <= radius*radius:
                    cur = amp(qx + dqx, qy + dqy)
                    if cur > maxv:
                        maxv = cur
        return maxv

    # detect atomic peaks
    atom_amps = [max_amp_around(vx, vy, tol) for vx, vy in atom_vecs]
    max_atom = max(atom_amps) if atom_amps else 0.0
    if max_atom == 0.0:
        return 0.0
    threshold = rel_threshold * max_atom

    # CDW reciprocal lattice vectors (six symmetric)
    q1 = ((4*b1[0] - b2[0])/13, (4*b1[1] - b2[1])/13)
    q2 = ((b1[0] + 3*b2[0])/13, (b1[1] + 3*b2[1])/13)
    q3 = (-q1[0]-q2[0], -q1[1]-q2[1])
    cdw_vecs = [q1, q2, q3,
                (-q1[0], -q1[1]), (-q2[0], -q2[1]), (-q3[0], -q3[1])]

    cdw_amps = [max_amp_around(vx, vy, tol) for vx, vy in cdw_vecs]

    matched = sum(1 for a in cdw_amps if a >= threshold)
    score_val = matched / len(cdw_vecs)
    return float(score_val)


_SCORERS = {
    'ldos_cdw_fft_check': score_0,
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
