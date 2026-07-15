import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='equilibrium_curves') ===
def score_0(artifact, step, ctx):
        def alpha(w):
            if w == 0.0:
                return 1.2  # asymptotic constant for ω→0
            # fcc macrolattice: volume per precipitate Ω = a³/4, so ω = (4πR³/3) / (a³/4)
            #  => (R/a)³ = 3ω/(16π)
            R_over_a = (3.0 * w / (16.0 * math.pi)) ** (1.0 / 3.0)
            sum_val = 0.0
            nmax = 15
            for h in range(0, nmax + 1):
                for k in range(0, nmax + 1):
                    for l in range(0, nmax + 1):
                        if h == 0 and k == 0 and l == 0:
                            continue
                        if (h + k + l) % 2 != 0:
                            continue
                        mult = 1
                        if h > 0:
                            mult *= 2
                        if k > 0:
                            mult *= 2
                        if l > 0:
                            mult *= 2
                        norm_sq = h * h + k * k + l * l
                        norm = math.sqrt(norm_sq)
                        u = 2.0 * math.pi * R_over_a * norm
                        if u < 1e-4:
                            term = 1.0 / (u * u)
                        else:
                            val = 3.0 * (u * math.cos(u) - math.sin(u)) / (u ** 3)
                            term = (val * val) / (u * u)
                        sum_val += mult * term
            return 3.0 * w * sum_val

        def solve_x(C):
            lo, hi = 0.25, 1.0
            for _ in range(50):
                mid = (lo + hi) / 2.0
                val = mid ** (1.0/3.0) * (1.0 - mid) - C
                if val > 0:
                    lo = mid
                else:
                    hi = mid
            return (lo + hi) / 2.0

        xi = 0.5
        beta_c = 3.0 * (4.0 ** (-4.0/3.0))
        n_grid = 3000
        omegas = [i / n_grid for i in range(n_grid // 2 + 1)]   # 0 to 0.5

        def compute_expected(omega0):
            best_f = float('inf')
            best_w = 0.0
            best_x = 0.0
            for w in omegas:
                if w == 0.0:
                    f_val = 0.5 * omega0**2
                    if f_val < best_f:
                        best_f = f_val
                        best_w = 0.0
                        best_x = 0.0
                    continue
                aw = alpha(w)
                if aw <= 0:
                    continue
                C = xi * (aw ** (1.0/3.0)) / (3.0 * (1.0 - w))
                if C > beta_c:
                    continue
                x = solve_x(C)
                f_val = (1.5 * x * (1.0 - x) * w * (1.0 - w)
                         + 0.5 * w * (1.0 - omega0 - (1.0 - w) * x)**2
                         + 0.5 * (1.0 - w) * (omega0 - w * x)**2)
                if f_val < best_f:
                    best_f = f_val
                    best_w = w
                    best_x = x
            if best_w < 1e-8:
                return 0.0, 0.0, 0.0
            R_eq = best_x ** (-2.0/3.0) * alpha(best_w) ** (-1.0/3.0)
            return best_w, best_x, R_eq

        tol_omega = step.get('tolerance_omega_eq', 0.02)
        tol_x = step.get('tolerance_x_eq', 0.02)
        tol_R = step.get('tolerance_R_eq_norm', 0.05)
        n_correct = 0
        n_total = len(artifact)
        if n_total == 0:
            return 0.0
        for row in artifact:
            try:
                omega0 = float(row['omega0'])
                w_agent = float(row['omega_eq'])
                x_agent = float(row['x_eq'])
                r_agent = float(row['R_eq_norm'])
            except (ValueError, KeyError):
                continue
            exp_w, exp_x, exp_r = compute_expected(omega0)
            if exp_w < 1e-6:
                if abs(w_agent - exp_w) <= tol_omega:
                    n_correct += 1
            else:
                if (abs(w_agent - exp_w) <= tol_omega and
                    abs(x_agent - exp_x) <= tol_x and
                    abs(r_agent - exp_r) <= tol_R):
                    n_correct += 1
        return n_correct / n_total if n_total else 0.0


_SCORERS = {
    'equilibrium_curves': score_0,
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
