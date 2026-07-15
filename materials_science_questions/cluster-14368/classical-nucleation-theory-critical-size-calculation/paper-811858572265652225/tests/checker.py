import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from math import sqrt, pi, sin, cos, sinh, cosh, tan
import csv
import json
import os

def analytical_solution_grid(a, b, D_m, k_m, C0, Ceq):
    Da = k_m * b / D_m
    # solve y = beta * b from y tan(y) = Da
    # find first 20 positive roots
    roots = []
    # initial guesses
    for n in range(1, 20):
        # interval ((n-1)*pi, n*pi)
        low = (n-1)*pi + 0.01
        high = n*pi - 0.01
        # find root via binary search or simple scan
        y = low
        step = (high-low)/1000.0
        for _ in range(1000):
            y_test = y
            f = y_test*tan(y_test) - Da
            if abs(f) < 1e-6:
                break
            # simple sign change
            y += step
        else:
            y = (low+high)/2.0
        roots.append(y)
    beta_n = [y / b for y in roots if y > 0]
    # compute C array
    xs = np.arange(0, a, 1.0)  # x from 0 to a-1? But x is integer 0..124, with a=125, so positions: 0,1,...,124. Use center of cell? We'll use node positions as x indices.
    ys = np.arange(0, b, 1.0)  # 0..99
    C = np.zeros((len(ys), len(xs)))
    for iy, y in enumerate(ys):  # y coordinate
        for ix, x in enumerate(xs):
            s = 0.0
            for bn in beta_n:
                # compute Nn^2
                bn_b = bn * b
                Nn2 = b/2.0 * (1.0 + sin(2.0*bn_b)/(2.0*bn_b))
                term = sin(bn_b) / (Nn2 * bn) * cosh(bn*(x - a)) / cosh(bn*a) * cos(bn*y)
                s += term
            C[iy, ix] = (C0 - Ceq) * s + Ceq
    return C

def box_counting_fractal_dimension(grid):
    # grid is 2D boolean array
    sizes = np.array(range(1, min(grid.shape)//2, 2))
    counts = []
    for size in sizes:
        if size > min(grid.shape):
            break
        # count boxes covering grid
        cnt = 0
        for i in range(0, grid.shape[0], size):
            for j in range(0, grid.shape[1], size):
                sub = grid[i:i+size, j:j+size]
                if np.any(sub):
                    cnt += 1
        counts.append(cnt)
    # linear regression on log-log
    valid = (np.array(counts) > 0).all()  # need at least some non-zero counts
    if not valid or len(sizes) < 3:
        return 0.0
    log_sizes = np.log(sizes)
    log_counts = np.log(np.array(counts))
    coeffs = np.polyfit(log_sizes, log_counts, 1)
    return -coeffs[0]


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
    specs = spec.get("steps", [])
    analytical_C = None
    for s in specs:
        if s.get("id") == "val_contour":
            p = s.get("params", {})
            a = p.get("a", 125)
            b = p.get("b", 100)
            D_m = p.get("D_m", 0.00347)
            k_m = p.get("k_m", 0.05)
            C0 = p.get("C0", 10.0)
            Ceq = p.get("Ceq", 1.0)
            analytical_C = analytical_solution_grid(a, b, D_m, k_m, C0, Ceq)
            break
    ctx = {"analytical_C": analytical_C}
    return ctx


# === block: score_0 (check id='val_contour') ===
def score_0(artifact, step, ctx):
    # agent artifact is list of dicts with keys x,y,concentration
    import numpy as np
    # reconstruct grid
    x_max = 125
    y_max = 100
    grid = np.full((y_max, x_max), np.nan)
    for row in artifact:
        x = int(row["x"])
        y = int(row["y"])
        if 0 <= x < x_max and 0 <= y < y_max:
            grid[y, x] = float(row["concentration"])
    if np.any(np.isnan(grid)):
        return 0.0
    analytical_C = ctx.get("analytical_C")
    if analytical_C is None:
        return 0.0
    rmse = np.sqrt(np.mean((grid - analytical_C)**2))
    p = step.get("params", {})
    rmse_full = p.get("rmse_full_credit", 0.05)
    rmse_zero = p.get("rmse_zero_credit", 0.5)
    if rmse <= rmse_full:
        return 1.0
    if rmse >= rmse_zero:
        return 0.0
    return float((rmse_zero - rmse) / (rmse_zero - rmse_full))


# === block: score_1 (check id='growth_da16') ===
def score_1(artifact, step, ctx):
    # agent artifact list of dicts
    import numpy as np
    grid_size = step.get("params", {}).get("grid_size", 100)
    try:
        coords = set()
        min_mass = 0.0
        has_solid = False
        for row in artifact:
            x = int(row["x"])
            y = int(row["y"])
            mass = float(row["solid_mass"])
            if mass < 0:
                return 0.0
            if mass >= 0.5:
                has_solid = True
            coords.add((x, y))
            min_mass = min(min_mass, mass)
        # check rectangular grid complete
        expected = set((x,y) for x in range(grid_size) for y in range(grid_size))
        if coords != expected:
            return 0.0
        if not has_solid:
            return 0.0
        return 1.0
    except Exception:
        return 0.0


# === block: score_2 (check id='growth_da400') ===
def score_2(artifact, step, ctx):
    import numpy as np
    grid_size = step.get("params", {}).get("grid_size", 100)
    try:
        coords = set()
        has_solid = False
        for row in artifact:
            x = int(row["x"])
            y = int(row["y"])
            mass = float(row["solid_mass"])
            if mass < 0:
                return 0.0
            if mass >= 0.5:
                has_solid = True
            coords.add((x, y))
        expected = set((x,y) for x in range(grid_size) for y in range(grid_size))
        if coords != expected:
            return 0.0
        if not has_solid:
            return 0.0
        return 1.0
    except Exception:
        return 0.0


# === block: score_3 (check id='fractal_dims') ===
def score_3(artifact, step, ctx):
    import numpy as np
    import os
    # First, load growth arrays from /app/outputs
    path_da16 = os.path.join("/app/outputs", "step_02_growth_da16.csv")
    path_da400 = os.path.join("/app/outputs", "step_03_growth_da400.csv")
    def load_grid(path):
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        x_max = 100; y_max = 100
        grid = np.zeros((y_max, x_max))
        for row in rows:
            x = int(row["x"])
            y = int(row["y"])
            mass = float(row["solid_mass"])
            if 0 <= x < x_max and 0 <= y < y_max:
                grid[y, x] = mass
        return grid
    grid_da16 = load_grid(path_da16)
    grid_da400 = load_grid(path_da400)
    if grid_da16 is None or grid_da400 is None:
        return 0.0
    # Binarise
    binary_da16 = (grid_da16 >= 0.5).astype(np.bool_)
    binary_da400 = (grid_da400 >= 0.5).astype(np.bool_)
    # Compute fractal dimensions
    Df_da16 = box_counting_fractal_dimension(binary_da16)
    Df_da400 = box_counting_fractal_dimension(binary_da400)
    # Read self-reported values
    reported = artifact  # JSON object with da16, da400
    rep_da16 = float(reported.get("da16", 0))
    rep_da400 = float(reported.get("da400", 0))
    # Thresholds from params
    p = step.get("params", {})
    min_da16 = p.get("da16_min", 1.95)
    max_da400 = p.get("da400_max", 1.75)
    # Scoring
    score_da16 = 0.0
    if Df_da16 >= min_da16:
        score_da16 = 1.0
    elif Df_da16 >= 1.0:
        score_da16 = max(0.0, (Df_da16 - 1.0) / (min_da16 - 1.0))
    score_da400 = 0.0
    if Df_da400 <= max_da400:
        score_da400 = 1.0
    elif Df_da400 <= 2.0:
        score_da400 = max(0.0, (2.0 - Df_da400) / (2.0 - max_da400))
    # Consistency check: reported vs recomputed
    consistency = 1.0
    if abs(rep_da16 - Df_da16) > 0.1 or abs(rep_da400 - Df_da400) > 0.1:
        consistency = 0.0
    # Combine: weights 0.4|0.4|0.2
    return 0.4*score_da16 + 0.4*score_da400 + 0.2*consistency


# === block: score_4 (check id='spacing') ===
def score_4(artifact, step, ctx):
    import math
    # Expected lambda_c from parameters: S=1.20, lambda_p=1.5 um
    # lambda_c = 2*pi * lambda_p * sqrt(S/(S-1))
    lp = 1.5  # um
    S = 1.20
    expected_lc = 2*math.pi * lp * math.sqrt(S/(S-1))  # ~23.08 um
    p = step.get("params", {})
    expected = p.get("expected_lambda_c_um", expected_lc)
    tol = p.get("tolerance", 0.2)
    agent_lc = float(artifact.get("lambda_c", 0))
    if expected == 0:
        return 0.0
    rel_err = abs(agent_lc - expected) / expected
    if rel_err <= tol:
        return 1.0
    else:
        # partial linear decay to 0 at 2*tol
        if rel_err <= 2*tol:
            return float((2*tol - rel_err) / tol)
        return 0.0


_SCORERS = {
    'val_contour': score_0,
    'growth_da16': score_1,
    'growth_da400': score_2,
    'fractal_dims': score_3,
    'spacing': score_4,
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
