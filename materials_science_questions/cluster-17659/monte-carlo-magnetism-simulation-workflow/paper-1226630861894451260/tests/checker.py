import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
    from scipy.optimize import minimize
    from scipy.interpolate import UnivariateSpline
except ImportError:
    pass


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
    return {"outputs_dir": outputs_dir, "gold_chi": spec["steps"][1]["gold_chi"], "gold_g": spec["steps"][1]["gold_g"], "tolerances": spec["steps"][1]["tolerances"]}


# === block: score_0 (check id='observed_data_audit') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact
        score = 1.0
        required_keys = ["L3","L4","L5"]
        for key in required_keys:
            if key not in data or not isinstance(data[key], list):
                return 0.0
        if not all(data[key] for key in required_keys):
            return 0.0
        required_fields = ["T","chi_SG","chi_SG_err","g","g_err"]
        for key in required_keys:
            for obj in data[key]:
                for f in required_fields:
                    if f not in obj or not isinstance(obj[f], (int,float)):
                        return 0.0
                if obj["chi_SG"] <= 0 or obj["chi_SG_err"] <= 0 or obj["g"] < 0 or obj["g"] > 1 or obj["g_err"] <= 0:
                    return 0.0
        for key in required_keys:
            arr = data[key]
            T_vals = [o["T"] for o in arr]
            g_vals = [o["g"] for o in arr]
            sorted_pairs = sorted(zip(T_vals, g_vals), key=lambda x: x[0])
            g_sorted = [p[1] for p in sorted_pairs]
            if g_sorted[0] <= g_sorted[-1]:
                score -= 0.3
            if score <= 0:
                score = 0.0
        return score
    except:
        return 0.0


# === block: score_1 (check id='critical_params_recompute') ===
def score_1(artifact, step, ctx):
    import json
    import numpy as np
    from scipy.optimize import minimize

    try:
        outputs_dir = ctx["outputs_dir"]
        obs_path = os.path.join(outputs_dir, "observed_data.json")
        with open(obs_path) as f:
            obs = json.load(f)

        all_T = []
        all_chi = []
        all_g = []
        all_L = []
        L_map = {"L3": 3, "L4": 4, "L5": 5}
        for label, Lval in L_map.items():
            arr = obs[label]
            for pt in arr:
                all_T.append(pt["T"])
                all_chi.append(pt["chi_SG"])
                all_g.append(pt["g"])
                all_L.append(Lval)
        T = np.array(all_T)
        chi = np.array(all_chi)
        g = np.array(all_g)
        L = np.array(all_L)

        def collapse_rss_scaled(x, y, deg=3):
            """Sort by x, fit a degree-deg polynomial, return RSS."""
            sorted_idx = np.argsort(x)
            x_sorted = x[sorted_idx]
            y_sorted = y[sorted_idx]
            # Fit polynomial, compute residuals
            try:
                coeffs = np.polyfit(x_sorted, y_sorted, deg)
                pred = np.polyval(coeffs, x_sorted)
                return np.sum((y_sorted - pred) ** 2)
            except:
                return np.inf

        def chi_rss(params):
            Tc, nu, eta = params
            # Avoid division by zero or negative exponents that cause complex values
            if nu <= 0:
                return np.inf
            x = (T - Tc) * (L ** (1.0 / nu))
            y = chi / (L ** (2.0 - eta))
            return collapse_rss_scaled(x, y, deg=3)

        res = minimize(chi_rss, [0.5, 0.6, 0.2],
                       bounds=[(0.3, 0.7), (0.3, 1.5), (-1.0, 1.0)],
                       method='L-BFGS-B')
        if not res.success:
            # Try a second starting point
            res = minimize(chi_rss, [0.52, 0.8, 0.1],
                           bounds=[(0.3, 0.7), (0.3, 1.5), (-1.0, 1.0)],
                           method='L-BFGS-B')
        Tc_chi_fit, nu_chi_fit, eta_chi_fit = res.x

        def g_rss(params):
            Tc, nu = params
            if nu <= 0:
                return np.inf
            x = (T - Tc) * (L ** (1.0 / nu))
            return collapse_rss_scaled(x, g, deg=3)

        res_g = minimize(g_rss, [0.5, 0.6],
                         bounds=[(0.3, 0.7), (0.3, 1.5)],
                         method='L-BFGS-B')
        if not res_g.success:
            res_g = minimize(g_rss, [0.52, 0.8],
                             bounds=[(0.3, 0.7), (0.3, 1.5)],
                             method='L-BFGS-B')
        Tc_g_fit, nu_g_fit = res_g.x

        gold_chi = ctx["gold_chi"]
        gold_g = ctx["gold_g"]
        tols = ctx["tolerances"]

        def param_score(val, gold, tol):
            return max(0.0, 1.0 - abs(val - gold) / tol)

        sc_chi = (param_score(Tc_chi_fit, gold_chi["Tc"], tols["Tc_chi"]) +
                  param_score(nu_chi_fit, gold_chi["nu"], tols["nu_chi"]) +
                  param_score(eta_chi_fit, gold_chi["eta"], tols["eta_chi"])) / 3.0
        sc_g = (param_score(Tc_g_fit, gold_g["Tc"], tols["Tc_g"]) +
                param_score(nu_g_fit, gold_g["nu"], tols["nu_g"])) / 2.0
        score = 0.5 * sc_chi + 0.5 * sc_g
        return max(0.0, min(1.0, score))
    except Exception:
        return 0.0


_SCORERS = {
    'observed_data_audit': score_0,
    'critical_params_recompute': score_1,
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
