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


# === block: score_0 (check id='interior_crack_check') ===
def score_0(artifact, step, ctx):
    def find_local_maxima(artifact):
        x_vals = []
        y_vals = []
        z_vals = []
        for row in artifact:
            x_vals.append(float(row['x']))
            y_vals.append(float(row['y']))
            z_vals.append(float(row['power_density']))
        xs = sorted(set(x_vals))
        ys = sorted(set(y_vals))
        if len(xs)*len(ys) != len(artifact):
            return [], None, None, None, None
        x_to_idx = {x: i for i, x in enumerate(xs)}
        y_to_idx = {y: i for i, y in enumerate(ys)}
        nx = len(xs)
        ny = len(ys)
        z_grid = [[None]*nx for _ in range(ny)]
        for x, y, z in zip(x_vals, y_vals, z_vals):
            i = y_to_idx[y]
            j = x_to_idx[x]
            z_grid[i][j] = z
        maxima = []
        for i in range(1, ny-1):
            for j in range(1, nx-1):
                if z_grid[i][j] is None:
                    continue
                center = z_grid[i][j]
                up = z_grid[i-1][j]
                down = z_grid[i+1][j]
                left = z_grid[i][j-1]
                right = z_grid[i][j+1]
                if center > up and center > down and center > left and center > right:
                    maxima.append((xs[j], ys[i]))
        return maxima, xs[0], xs[-1], ys[0], ys[-1]

    maxima, xmin, xmax, ymin, ymax = find_local_maxima(artifact)
    if len(maxima) != 2:
        return 0.0
    domain_x = xmax - xmin
    domain_y = ymax - ymin
    left = [m for m in maxima if m[0] < xmin + 0.5*domain_x]
    right = [m for m in maxima if m[0] >= xmin + 0.5*domain_x]
    if len(left) != 1 or len(right) != 1:
        return 0.0
    if abs(right[0][0] - left[0][0]) < 0.2*domain_x:
        return 0.0
    for m in maxima:
        if m[1] < ymin + 0.15*domain_y or m[1] > ymax - 0.15*domain_y:
            return 0.0
    return 1.0


# === block: score_1 (check id='border_crack_check') ===
def score_1(artifact, step, ctx):
    def find_local_maxima(artifact):
        x_vals = []
        y_vals = []
        z_vals = []
        for row in artifact:
            x_vals.append(float(row['x']))
            y_vals.append(float(row['y']))
            z_vals.append(float(row['power_density']))
        xs = sorted(set(x_vals))
        ys = sorted(set(y_vals))
        if len(xs)*len(ys) != len(artifact):
            return [], None, None, None, None
        x_to_idx = {x: i for i, x in enumerate(xs)}
        y_to_idx = {y: i for i, y in enumerate(ys)}
        nx = len(xs)
        ny = len(ys)
        z_grid = [[None]*nx for _ in range(ny)]
        for x, y, z in zip(x_vals, y_vals, z_vals):
            i = y_to_idx[y]
            j = x_to_idx[x]
            z_grid[i][j] = z
        maxima = []
        for i in range(1, ny-1):
            for j in range(1, nx-1):
                if z_grid[i][j] is None:
                    continue
                center = z_grid[i][j]
                up = z_grid[i-1][j]
                down = z_grid[i+1][j]
                left = z_grid[i][j-1]
                right = z_grid[i][j+1]
                if center > up and center > down and center > left and center > right:
                    maxima.append((xs[j], ys[i]))
        return maxima, xs[0], xs[-1], ys[0], ys[-1]

    maxima, xmin, xmax, ymin, ymax = find_local_maxima(artifact)
    if len(maxima) != 1:
        return 0.0
    x, y = maxima[0]
    domain_x = xmax - xmin
    domain_y = ymax - ymin
    if not (xmin + 0.1*domain_x < x < xmin + 0.6*domain_x):
        return 0.0
    if y < ymin + 0.2*domain_y or y > ymax - 0.2*domain_y:
        return 0.0
    return 1.0


_SCORERS = {
    'interior_crack_check': score_0,
    'border_crack_check': score_1,
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
