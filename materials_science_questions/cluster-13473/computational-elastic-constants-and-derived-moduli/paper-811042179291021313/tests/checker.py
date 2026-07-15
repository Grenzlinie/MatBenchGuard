import os
import json
import csv

# === author imports / helpers ===
import csv
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
    return {'Tg_gold': 450.0, 'tol': 10.0}


# === block: score_0 (check id='step_04_density') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0

    import math

    # Parse temperatures and densities
    temps = []
    dens = []
    for row in artifact:
        try:
            t = float(row['temperature'])
            d = float(row['density'])
            temps.append(t)
            dens.append(d)
        except (KeyError, ValueError):
            return 0.0

    if len(temps) < 30:
        return 0.0
    if max(temps) < 550.0 or min(temps) > 400.0:
        return 0.0
    if min(dens) <= 0:
        return 0.0

    # Reference density at T0 = 600 K
    best_idx = 0
    best_diff = float('inf')
    for i, t in enumerate(temps):
        diff = abs(t - 600.0)
        if diff < best_diff:
            best_diff = diff
            best_idx = i
    d0 = dens[best_idx]

    # Reduced volume
    rv = [d0 / d - 1.0 for d in dens]
    n = len(temps)
    min_T = min(temps)
    max_T = max(temps)

    # Grid search over breakpoint temperature
    best_break = None
    min_rss = float('inf')

    # Helper: solve 3x3 linear system M * x = rhs via Cramer's rule
    def solve_3x3(M, rhs):
        (a00, a01, a02, a10, a11, a12, a20, a21, a22) = (
            M[0][0], M[0][1], M[0][2],
            M[1][0], M[1][1], M[1][2],
            M[2][0], M[2][1], M[2][2]
        )
        det = a00*(a11*a22 - a12*a21) - a01*(a10*a22 - a12*a20) + a02*(a10*a21 - a11*a20)
        if det == 0:
            return None
        det0 = rhs[0]*(a11*a22 - a12*a21) - a01*(rhs[1]*a22 - a12*rhs[2]) + a02*(rhs[1]*a21 - a11*rhs[2])
        det1 = a00*(rhs[1]*a22 - a12*rhs[2]) - rhs[0]*(a10*a22 - a12*a20) + a02*(a10*rhs[2] - rhs[1]*a20)
        det2 = a00*(a11*rhs[2] - rhs[1]*a21) - a01*(a10*rhs[2] - rhs[1]*a20) + rhs[0]*(a10*a21 - a11*a20)
        x = det0 / det
        y = det1 / det
        z = det2 / det
        return x, y, z

    # We'll try breakpoints from min_T+5 to max_T-5 with step 1.0 K
    step = 1.0
    T_break = min_T + 5.0
    while T_break < max_T - 5.0:
        low_count = 0
        high_count = 0
        # Build design matrix sums for the model: y = b + m_low*low_dT + m_high*high_dT
        # where low_dT = min(T - T_break, 0), high_dT = max(T - T_break, 0)
        S00 = 0.0  # number of points effectively used (will be n)
        S10 = 0.0  # sum low_dT
        S20 = 0.0  # sum high_dT
        S11 = 0.0  # sum low_dT^2
        S22 = 0.0  # sum high_dT^2
        # S21 = 0.0 because low_dT * high_dT = 0 for all points
        b0 = 0.0
        b1 = 0.0
        b2 = 0.0
        used = 0
        for i in range(n):
            Ti = temps[i]
            dT = Ti - T_break
            if dT >= 0:
                low = 0.0
                high = dT
                high_count += 1
            else:
                low = dT
                high = 0.0
                low_count += 1
            S10 += low
            S20 += high
            S11 += low * low
            S22 += high * high
            yi = rv[i]
            b0 += yi
            b1 += low * yi
            b2 += high * yi
            used += 1
        S00 = float(used)
        # Need at least 3 points in each segment to avoid degenerate fits
        if low_count < 3 or high_count < 3:
            T_break += step
            continue

        M = [
            [S00, S10, S20],
            [S10, S11, 0.0],
            [S20, 0.0, S22]
        ]
        rhs = [b0, b1, b2]
        sol = solve_3x3(M, rhs)
        if sol is None:
            T_break += step
            continue
        b, m_low, m_high = sol

        # Compute residual sum of squares
        rss = 0.0
        for i in range(n):
            dT = temps[i] - T_break
            if dT >= 0:
                pred = b + m_high * dT
            else:
                pred = b + m_low * dT
            rss += (pred - rv[i]) ** 2

        if rss < min_rss:
            min_rss = rss
            best_break = T_break

        T_break += step

    if best_break is None:
        return 0.0

    Tg_recomputed = best_break

    tol = ctx['tol']
    if abs(Tg_recomputed - ctx['Tg_gold']) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='step_05_tg') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    raw = artifact if isinstance(artifact, str) else str(artifact)
    raw = raw.strip()
    try:
        reported_tg = float(raw.split()[0])
    except (ValueError, IndexError):
        return 0.0

    if abs(reported_tg - ctx['Tg_gold']) <= ctx['tol']:
        return 1.0
    return 0.0


_SCORERS = {
    'step_04_density': score_0,
    'step_05_tg': score_1,
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
