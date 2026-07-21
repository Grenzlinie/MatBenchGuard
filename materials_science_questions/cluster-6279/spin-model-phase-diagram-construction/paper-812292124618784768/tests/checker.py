import os
import json
import csv

# === author imports / helpers ===
import json, math
from scipy.optimize import fsolve, brentq


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


# === block: score_0 (check id='phase_lines') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        Ax, Dx, Ay, Dy, mux, k = 1.0, 0.5, 1.0, 0.0, 1.0, 1.0
        Sum_AD = Ax + Dx
        # Helper: b from a and t
        def get_b(a, t):
            if a >= 1.0 or a <= -1.0:
                return None
            def eq(b):
                if abs(b) >= 1.0:
                    return 1e6
                return a - b - t * (math.atanh(a) - math.atanh(b))
            b0 = -a
            if b0 >= 1.0: b0 = 0.9
            elif b0 <= -1.0: b0 = -0.9
            try:
                sol = fsolve(eq, b0, maxfev=1000, xtol=1e-12)
                b = sol[0]
                if abs(b) >= 1.0: return None
                return b
            except:
                return None
        # spinodal function f(a) = u+v - 2 t u v
        def f_spinodal(a, t):
            if a >= 1.0 or a <= -1.0:
                return None
            b = get_b(a, t)
            if b is None: return None
            u = 1.0 / (1.0 - a*a)
            v = 1.0 / (1.0 - b*b)
            return u + v - 2.0 * t * u * v
        # find roots of f_spinodal(a,t) for a in [a_min, a_max]
        def find_roots(t, a_min=0.001, a_max=0.999, n_scan=200):
            import numpy as np
            a_vals = np.linspace(a_min, a_max, n_scan)
            f_vals = np.array([f_spinodal(a, t) for a in a_vals])
            roots = []
            signs = np.sign(f_vals)
            for i in range(1, n_scan):
                if signs[i-1] == 0 or signs[i] == 0: continue
                if signs[i-1] != signs[i] and np.isfinite(f_vals[i-1]) and np.isfinite(f_vals[i]):
                    try:
                        root = brentq(lambda aa: f_spinodal(aa, t), a_vals[i-1], a_vals[i], xtol=1e-12)
                        if all(abs(root - r) > 1e-8 for r in roots):
                            roots.append(root)
                    except: pass
            roots.sort()
            return roots
        # binary search for critical t (highest t with two roots)
        t_lo, t_hi = 0.01, 0.45
        roots_lo = find_roots(t_lo)
        if len(roots_lo) < 2:
            for _ in range(10):
                t_lo += 0.02
                roots_lo = find_roots(t_lo)
                if len(roots_lo) >= 2: break
        while t_hi - t_lo > 1e-7:
            t_mid = (t_lo + t_hi)/2
            if len(find_roots(t_mid)) >= 2:
                t_lo = t_mid
            else:
                t_hi = t_mid
        t_crit = t_lo
        roots_crit = find_roots(t_crit)
        if len(roots_crit) == 1:
            a_crit = roots_crit[0]
        elif len(roots_crit) == 2:
            a_crit = (roots_crit[0] + roots_crit[1]) / 2.0
        else:
            a_crit = None
        exp_crit = None
        if a_crit is not None:
            b_crit = get_b(a_crit, t_crit)
            if b_crit is not None:
                m_plus = (a_crit + b_crit) / 2.0
                h_plus = (t_crit / 2.0) * (math.atanh(a_crit) + math.atanh(b_crit))
                h = h_plus + ((Ax - Dx) / Sum_AD) * m_plus
                H_x_c = h * Sum_AD / mux
                T_c = t_crit * Sum_AD / k
                exp_crit = {"T_c": T_c, "H_x_c": H_x_c}
        # expected transition properties
        exp_ap2_exists = (Ax + Dx > 0)
        exp_ap2_order = "second" if exp_ap2_exists else None
        exp_ap2_H = (Ax - Dx) / mux if exp_ap2_exists else None
        exp_ap2_T = (Ax + Dx) / k if exp_ap2_exists else None
        exp_ap1_exists = (Dx > 0)
        exp_ap1_order = "first" if exp_ap1_exists else None
        exp_ap1_H = Ax / mux if exp_ap1_exists else None
        exp_ap1_T = None
        exp_int_exists = (0 < Dx < 3/5 * Ax)
        exp_int_order = "first" if exp_int_exists else None
        exp_bp2_exists = (Ax + Ay - Dx + Dy > 0) and (Ay + Dy > 0)
        exp_bp2_order = "second" if exp_bp2_exists else None
        exp_bp2_H = (Ax + Ay - Dx + Dy) / mux if exp_bp2_exists else None
        exp_bp2_T = (Ay + Dy) / k if exp_bp2_exists else None
        exp_ab_exists = not (Ay + Dy < Dx)
        exp_ab_order = "first" if exp_ab_exists else None
        exp_ab_H = math.sqrt((Ax + Ay - Dx + Dy) * (Ax - Ay + Dx - Dy)) / mux if exp_ab_exists else None
        exp_ab_T = None
        # tolerance helpers
        def close(a, b, rtol=1e-6, atol=1e-10):
            if a is None and b is None: return True
            if a is None or b is None: return False
            return abs(a - b) <= atol + rtol * max(abs(a), abs(b))
        def is_null(x):
            return x is None or x == "null"
        # map expected per type
        expected = {
            "a-p second-order": {"exists": exp_ap2_exists, "order": exp_ap2_order, "Hx": exp_ap2_H, "T": exp_ap2_T, "crit": None},
            "a-p first-order": {"exists": exp_ap1_exists, "order": exp_ap1_order, "Hx": exp_ap1_H, "T": exp_ap1_T, "crit": None},
            "internal a first-order": {"exists": exp_int_exists, "order": exp_int_order, "Hx": None, "T": None, "crit": exp_crit if exp_int_exists else None},
            "b-p second-order": {"exists": exp_bp2_exists, "order": exp_bp2_order, "Hx": exp_bp2_H, "T": exp_bp2_T, "crit": None},
            "a-b first-order": {"exists": exp_ab_exists, "order": exp_ab_order, "Hx": exp_ab_H, "T": exp_ab_T, "crit": None}
        }
        trans = artifact.get("transitions")
        if not isinstance(trans, list): return 0.0
        total_items = 0
        correct = 0
        for rec in trans:
            typ = rec.get("type")
            if typ not in expected: continue
            exp = expected[typ]
            # exists
            if rec.get("exists") == exp["exists"]:
                correct += 1
            total_items += 1
            # order
            if rec.get("order") == exp["order"]:
                correct += 1
            total_items += 1
            # H_x_intercept
            if close(rec.get("H_x_intercept"), exp["Hx"]):
                correct += 1
            total_items += 1
            # T_intercept (null check)
            agent_T = rec.get("T_intercept")
            exp_T = exp["T"]
            if is_null(agent_T) and is_null(exp_T):
                correct += 1
            elif (not is_null(agent_T)) and (not is_null(exp_T)) and close(agent_T, exp_T):
                correct += 1
            total_items += 1
            # critical point
            if typ == "internal a first-order":
                agent_crit = rec.get("critical_point")
                exp_crit_val = exp["crit"]
                if (agent_crit is None and exp_crit_val is None) or (exp_crit_val is None):
                    correct += 2 if (agent_crit is None) == (exp_crit_val is None) else 0
                    total_items += 2
                else:
                    if isinstance(agent_crit, dict) and isinstance(exp_crit_val, dict):
                        c1 = close(agent_crit.get("T_c"), exp_crit_val.get("T_c"), rtol=1e-4, atol=1e-8)
                        c2 = close(agent_crit.get("H_x_c"), exp_crit_val.get("H_x_c"), rtol=1e-4, atol=1e-8)
                        correct += (c1 + c2)
                    total_items += 2
        if total_items == 0: return 0.0
        return min(1.0, correct / total_items)


_SCORERS = {
    'phase_lines': score_0,
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
