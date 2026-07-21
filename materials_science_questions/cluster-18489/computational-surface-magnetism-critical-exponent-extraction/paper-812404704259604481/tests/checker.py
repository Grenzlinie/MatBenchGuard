import os
import json
import csv

# === author imports / helpers ===
import math

def _sec_eq_t(t, Delta_S, D_S, Delta_1=0.0, D_1=0.0):
    def A(Delta, D):
        numer1 = 1.0 + Delta + D
        denom1 = 5.0 * t + 1.0 + Delta + D
        numer2 = 1.0 + Delta - D
        denom2 = 5.0 * t + 1.0 + Delta - D
        return 0.5 * (numer1 / denom1 + numer2 / denom2)
    A_S = A(Delta_S, D_S)
    A_1 = A(Delta_1, D_1)
    disc = 5.0 * (t - 1.0) * (t - 0.2)
    if disc < 0:
        # outside the physical domain → return a large number to preserve sign logic
        return 1000.0
    a = -1.5 + 2.5 * t - 0.5 * math.sqrt(disc)
    lhs = (4.0 * A_S - 1.0) * ((4.0 + a) / (5.0 * t + 1.0) - 1.0)
    rhs = A_1 ** 2
    return lhs - rhs

def compute_tc(Delta_S, D_S, Delta_1=0.0, D_1=0.0):
    """Find physical root t in [0,1] using bisection; returns None if no sign change."""
    lo = 1e-9
    hi = 1.0 - 1e-9
    f = lambda t: _sec_eq_t(t, Delta_S, D_S, Delta_1, D_1)
    fa = f(lo)
    fb = f(hi)
    if fa == 0:
        return lo
    if fb == 0:
        return hi
    if fa * fb > 0:
        return None
    for _ in range(60):
        mid = (lo + hi) * 0.5
        fm = f(mid)
        if abs(fm) < 1e-12:
            return mid
        if fa * fm < 0:
            hi = mid
            fb = fm
        else:
            lo = mid
            fa = fm
    return (lo + hi) * 0.5

def solve_delta_c(D_S):
    """Solve A_S(Delta, D_S) = 5/24 at t = 1; returns critical Delta_S."""
    target = 5.0 / 24.0
    def f(Delta):
        numer1 = 1.0 + Delta + D_S
        denom1 = 6.0 + Delta + D_S
        numer2 = 1.0 + Delta - D_S
        denom2 = 6.0 + Delta - D_S
        # denominators cannot be zero for the parameter range used (Delta > -1, D_S >=0)
        A_S = 0.5 * (numer1 / denom1 + numer2 / denom2)
        return A_S - target
    lo = -0.99
    hi = 10.0
    # expand hi if needed
    for _ in range(20):
        fl = f(lo)
        fh = f(hi)
        if fl * fh <= 0:
            break
        hi += 2.0
    else:
        return None
    for _ in range(80):
        mid = (lo + hi) * 0.5
        fm = f(mid)
        if abs(fm) < 1e-12:
            return mid
        if fl * fm < 0:
            hi = mid
            fh = fm
        else:
            lo = mid
            fl = fm
    return (lo + hi) * 0.5


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


# === block: score_0 (check id='step_01_phase_diagram') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        dmap = {'pure': 0.0, 'amorphized': 2.0}
        tol = step.get('tolerance_abs', 1e-3)
        correct = 0
        total = 0
        for row in artifact:
            try:
                delta = float(row['Delta_S'])
                pl = row['param_label'].strip()
                D_S = dmap[pl]
                tc_sub = float(row['t_c'])
                tc_exp = compute_tc(delta, D_S, Delta_1=0.0, D_1=0.0)
                if tc_exp is None:
                    continue
                if abs(tc_sub - tc_exp) <= tol:
                    correct += 1
                total += 1
            except (KeyError, ValueError):
                continue
        if total == 0:
            return 0.0
        return correct / total


# === block: score_1 (check id='step_02_critical_delta') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        tol = step.get('tolerance_abs', 0.01)
        correct = 0
        total = 0
        for row in artifact:
            try:
                D_S = float(row['D_S'])
                delta_c_sub = float(row['Delta_c_S'])
                delta_c_exp = solve_delta_c(D_S)
                if delta_c_exp is None:
                    continue
                if abs(delta_c_sub - delta_c_exp) <= tol:
                    correct += 1
                total += 1
            except (KeyError, ValueError):
                continue
        if total == 0:
            return 0.0
        return correct / total


# === block: score_2 (check id='step_03_reentrant_curve') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        tol = step.get('tolerance_abs', 1e-3)
        Delta_S_fixed = 7.0
        Delta_1 = -0.9
        D_1 = 0.0
        correct = 0
        total = 0
        for row in artifact:
            try:
                delta_s = float(row['delta_S'])
                D_S = delta_s * (1.0 + Delta_S_fixed)  # = 8.0 * delta_s
                tc_sub = float(row['t_c'])
                tc_exp = compute_tc(Delta_S_fixed, D_S, Delta_1, D_1)
                if tc_exp is None:
                    continue
                if abs(tc_sub - tc_exp) <= tol:
                    correct += 1
                total += 1
            except (KeyError, ValueError):
                continue
        if total == 0:
            return 0.0
        return correct / total


_SCORERS = {
    'step_01_phase_diagram': score_0,
    'step_02_critical_delta': score_1,
    'step_03_reentrant_curve': score_2,
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
