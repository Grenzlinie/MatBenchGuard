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
    refs = spec.get("hidden_reference", [])
    ref_dict = {}
    for r in refs:
        key = (round(float(r["lambda"]), 10), round(float(r["d"]), 10))
        ref_dict[key] = float(r["g_c_ref"])
    return {"ref_dict": ref_dict}


# === block: score_0 (check id='step_01_compute_gc_numeric') ===
def score_0(artifact, step, ctx):
    import math
    import scipy.integrate as integrate
    import scipy.special as sp
    import numpy as np

    def _compute_rhs(lam, d, tol=1e-6):
        """Compute RHS of the spherical constraint evaluated at s_c, stable version."""
        s_c = d * (1.0 + lam) / 2.0
        lam_sq = lam * lam
        term_A = d * (d - 1) * (1 - lam_sq) / 4.0
        term_B = d * (1 - lam_sq) / 8.0

        def _u_integral(phi):
            x = np.sin(phi)**2
            def f_u(u):
                rho = u * (x * (1.0 + lam) / 2.0 + (1.0 - x) * (1.0 - lam) / 2.0)
                i0e = sp.ive(0, rho)
                i1e = sp.ive(1, rho)
                i2e = sp.ive(2, rho)
                # avoid zero division
                if i0e == 0:
                    return 0.0
                ratio1 = i1e / i0e
                ratio2 = i2e / i0e
                term = (s_c**2 - term_A * ratio1**2 - term_B * (1.0 + ratio2))
                factor = np.exp(-u * d * lam * (1.0 - x)) * (i0e ** d)
                return factor * term
            res, _ = integrate.quad(f_u, 0.0, np.inf, limit=200, epsabs=tol, epsrel=tol)
            # The transformation x=sin^2φ gives dx = 2 sinφ cosφ dφ, and 1/√(x(1-x)) cancels,
            # so the integrand becomes 2 * f_u.
            return 2.0 * res

        integral, _ = integrate.quad(_u_integral, 0.0, np.pi / 2, limit=200, epsabs=tol, epsrel=tol)
        return integral * (s_c ** -1.5)

    rows = artifact
    tol = 1e-3
    n_correct = 0
    n_total = 0
    for row in rows:
        try:
            lam = float(row.get("lambda", None))
            d = float(row.get("d", None))
            g_c = float(row.get("g_c", None))
        except (ValueError, TypeError):
            continue
        n_total += 1
        # Analytical value for λ=0 (exact, no integration needed)
        if abs(lam) < 1e-12:
            expected = 4.0 * d
            if abs(g_c - expected) / max(abs(expected), 1e-10) < tol:
                n_correct += 1
            continue
        lhs = math.sqrt(8.0 * math.pi**2 / g_c)
        try:
            rhs = _compute_rhs(lam, d)
        except Exception:
            continue
        if rhs == 0.0:
            continue
        relerr = abs(lhs - rhs) / abs(rhs)
        if relerr < tol:
            n_correct += 1

    score = n_correct / n_total if n_total > 0 else 0.0
    return score


# === block: score_1 (check id='step_01_trend_d15') ===
def score_1(artifact, step, ctx):
    val0 = None
    val1 = None
    for row in artifact:
        try:
            lam = float(row.get("lambda", None))
            d = float(row.get("d", None))
            g = float(row.get("g_c", None))
        except (ValueError, TypeError):
            continue
        if abs(d - 1.5) < 1e-4 and abs(lam) < 1e-4:
            val0 = g
        if abs(d - 1.5) < 1e-4 and abs(lam - 0.1) < 1e-4:
            val1 = g
    if val0 is not None and val1 is not None and val1 < val0:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='step_01_trend_d21') ===
def score_2(artifact, step, ctx):
    val0 = None
    val1 = None
    for row in artifact:
        try:
            lam = float(row.get("lambda", None))
            d = float(row.get("d", None))
            g = float(row.get("g_c", None))
        except (ValueError, TypeError):
            continue
        if abs(d - 2.1) < 1e-4 and abs(lam) < 1e-4:
            val0 = g
        if abs(d - 2.1) < 1e-4 and abs(lam - 0.1) < 1e-4:
            val1 = g
    if val0 is not None and val1 is not None and val1 > val0:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='step_01_trend_d2_minimum') ===
def score_3(artifact, step, ctx):
    points = []
    for row in artifact:
        try:
            lam = float(row.get("lambda", None))
            d = float(row.get("d", None))
            g = float(row.get("g_c", None))
        except (ValueError, TypeError):
            continue
        if abs(d - 2.0) < 1e-4:
            points.append((lam, g))
    if len(points) < 4:
        return 0.0
    # retrieve specific lambdas
    g0 = next((g for lam, g in points if abs(lam) < 1e-4), None)
    g1 = next((g for lam, g in points if abs(lam - 1.0) < 1e-4), None)
    g01 = next((g for lam, g in points if abs(lam - 0.1) < 1e-4), None)
    g09 = next((g for lam, g in points if abs(lam - 0.9) < 1e-4), None)
    if g0 is None or g1 is None or g01 is None or g09 is None:
        return 0.0
    cond1 = (g01 < g0)
    cond2 = (g09 < g1)
    min_pair = min(points, key=lambda x: x[1])
    min_lam, min_g = min_pair
    cond3 = (min_g < g0 and min_g < g1)
    if cond1 and cond2 and cond3:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_01_compute_gc_numeric': score_0,
    'step_01_trend_d15': score_1,
    'step_01_trend_d21': score_2,
    'step_01_trend_d2_minimum': score_3,
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
