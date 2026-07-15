import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad
import json


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
    return {'alpha': 10.0, 'delta': 0.01}


# === block: score_0 (check id='harmonic_results') ===
def score_0(artifact, step, ctx):
    alpha = ctx['alpha']
    delta = ctx['delta']
    def e_bar(t_ratio):
        if t_ratio <= 0: return 0.0
        upper = 1.0 / t_ratio
        # Integrate up to upper, but if very large use a cutoff to avoid numerical difficulty
        if upper > 50:
            upper = 50
        res, _ = quad(lambda x: x / (np.exp(x) - 1), 0, upper)
        return t_ratio**2 * res

    def bound_A(t_ratio, eb):
        if eb == 0: return 0.0
        return (1.0 / t_ratio) * (alpha / (4 * eb)) * ((4 * eb / alpha) + 1)**2

    def bound_B(t_ratio, eb):
        return (2 * alpha / delta) * (1.0 / t_ratio) * eb

    def recompute_n_min(t_ratio):
        eb = e_bar(t_ratio)
        nA = bound_A(t_ratio, eb)
        nB = bound_B(t_ratio, eb)
        return max(nA, nB)

    # Shape check scores
    shape_score = 0.0
    if 'n_min_curve' in artifact and 'material_estimates' in artifact:
        curve = artifact['n_min_curve']
        mat = artifact['material_estimates']
        if isinstance(curve, list) and len(curve) >= 10 and isinstance(mat, list) and len(mat) == 4:
            shape_score = 1.0

    # ---- Recompute n_min curve points ----
    curve_pts_score = 0.0
    if shape_score > 0:
        xs_agent = np.array([p['T_ratio'] for p in curve])
        ys_agent = np.array([p['n_min'] for p in curve])
        # Sort by T_ratio for interpolation
        idx = np.argsort(xs_agent)
        xs_agent = xs_agent[idx]
        ys_agent = ys_agent[idx]
        # Sample 50 log-spaced check points
        xs_check = np.logspace(np.log10(0.01), np.log10(100.0), 50)
        ys_check = np.array([recompute_n_min(xc) for xc in xs_check])
        # Interpolate agent's y at check points
        ys_agent_interp = np.interp(xs_check, xs_agent, ys_agent)
        passed = 0
        for yc, ya in zip(ys_check, ys_agent_interp):
            rel_err = abs(ya - yc) / max(yc, 1e-12)
            if yc < 10.0:
                if abs(ya - yc) <= 0.5:
                    passed += 1
            else:
                if rel_err <= 0.1:
                    passed += 1
        curve_pts_score = passed / len(xs_check)

    # ---- Asymptotics ----
    asym_high_score = 0.0
    asym_low_score = 0.0
    if shape_score > 0:
        # High T (T_ratio >= 10)
        high_mask = xs_agent >= 10.0
        if np.sum(high_mask) >= 2:
            y_high = ys_agent[high_mask]
            mean_high = np.mean(y_high)
            # Check near constant 2000
            target = 2.0 * alpha / delta
            deviations = np.abs(y_high - target) / target
            if np.all(deviations < 0.15) and abs(mean_high - target)/target < 0.1:
                asym_high_score = 1.0
            else:
                # partial
                frac = np.mean(deviations < 0.15)
                asym_high_score = frac
        # Low T (T_ratio <= 0.1)
        low_mask = xs_agent <= 0.1
        if np.sum(low_mask) >= 3:
            log_x = np.log10(xs_agent[low_mask])
            log_y = np.log10(ys_agent[low_mask])
            coeffs = np.polyfit(log_x, log_y, 1)
            slope = coeffs[0]
            # R-squared
            p = np.poly1d(coeffs)
            yhat = p(log_x)
            ybar = np.mean(log_y)
            ssreg = np.sum((yhat - ybar)**2)
            sstot = np.sum((log_y - ybar)**2)
            rsq = ssreg / sstot if sstot > 0 else 0
            if -3.5 <= slope <= -2.5 and rsq > 0.95:
                asym_low_score = 1.0
            elif -3.5 <= slope <= -2.5:
                asym_low_score = 0.5
            else:
                asym_low_score = 0.0

    # ---- Material estimates ----
    material_score = 0.0
    if shape_score > 0:
        expected_materials = [
            {'material': 'iron', 'T': 470.0, 'a0_angstrom': 2.5, 'theta': 470.0},
            {'material': 'iron', 'T': 1.0, 'a0_angstrom': 2.5, 'theta': 470.0},
            {'material': 'carbon', 'T': 270.0, 'a0_angstrom': 1.5, 'theta': 2230.0},
            {'material': 'silicon', 'T': 1.0, 'a0_angstrom': 2.4, 'theta': 645.0}
        ]
        item_scores = []
        for exp in expected_materials:
            found = None
            for mi in mat:
                if mi.get('material','') == exp['material'] and abs(mi.get('T',0)-exp['T']) < 1e-3:
                    found = mi
                    break
            if found is None:
                item_scores.append(0.0)
                continue
            n_recalc = recompute_n_min(exp['T'] / exp['theta'])
            a0_um = exp['a0_angstrom'] * 1e-4
            l_recalc = n_recalc * a0_um
            err_n = abs(found['n_min'] - n_recalc) / max(n_recalc, 1e-12)
            err_l = abs(found['l_min_um'] - l_recalc) / max(l_recalc, 1e-12)
            if err_n <= 0.1 and err_l <= 0.1:
                item_scores.append(1.0)
            else:
                item_scores.append(0.0)
        material_score = np.mean(item_scores) if item_scores else 0.0

    # Combine with weights: shape 0.05, curve pts 0.5, asym high 0.2, asym low 0.1, material 0.15
    total = 0.05*shape_score + 0.5*curve_pts_score + 0.2*asym_high_score + 0.1*asym_low_score + 0.15*material_score
    return float(total)


_SCORERS = {
    'harmonic_results': score_0,
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
