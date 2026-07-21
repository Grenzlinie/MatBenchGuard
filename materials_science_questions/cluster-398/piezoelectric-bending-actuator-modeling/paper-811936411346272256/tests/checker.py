import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import curve_fit
import json
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
    return {}


# === block: score_0 (check id='step_flat_intensity') ===
def score_0(artifact, step, ctx):
    def score_flat_intensity(artifact, step, ctx):
        gold = step["gold"]
        a = 0.01
        beta_h_vals = artifact["beta_h_values"]
        results = artifact["results"]
        res_by_beta = {r["beta_h"]: r for r in results}
        total_score = 0.0
        count = 0
        tol_rel = 0.05
        for beta in beta_h_vals:
            beta_str = str(beta)
            if beta_str not in gold:
                continue
            res = res_by_beta.get(beta)
            if res is None:
                continue
            # pressure intensity factor
            pts_p = sorted(res["p_points"], key=lambda d: d["x"])
            x_p = np.array([pt["x"] for pt in pts_p])
            p = np.array([pt["p"] for pt in pts_p])
            # use points near x=a
            mask = (x_p >= 0.95 * a) & (x_p <= a)
            if np.sum(mask) < 3:
                continue
            x_near = x_p[mask]
            p_near = p[mask]
            f_p = p_near * np.sqrt(2.0 * (a - x_near))
            try:
                coeffs = np.polyfit(x_near, f_p, 1)
                K_raw = np.polyval(coeffs, a)
            except:
                continue
            sigma_a = 1000.0 / a  # P/a
            K_norm = K_raw / (sigma_a * np.sqrt(a))
            if abs(K_norm - gold[beta_str]["K_sigma"]) / abs(gold[beta_str]["K_sigma"]) <= tol_rel:
                total_score += 1.0
            count += 1
            # electric displacement intensity factor
            pts_q = sorted(res["q_points"], key=lambda d: d["x"])
            x_q = np.array([pt["x"] for pt in pts_q])
            q = np.array([pt["q"] for pt in pts_q])
            mask_q = (x_q >= 0.95 * a) & (x_q <= a)
            if np.sum(mask_q) < 3:
                continue
            x_near_q = x_q[mask_q]
            q_near = q[mask_q]
            f_q = q_near * np.sqrt(2.0 * (a - x_near_q))
            try:
                coeffs_q = np.polyfit(x_near_q, f_q, 1)
                K_raw_q = np.polyval(coeffs_q, a)
            except:
                continue
            sigma_b = 1e-6 / a
            K_norm_q = K_raw_q / (sigma_b * np.sqrt(a))
            if abs(K_norm_q - gold[beta_str]["K_D"]) / abs(gold[beta_str]["K_D"]) <= tol_rel:
                total_score += 1.0
            count += 1
        return total_score / count if count > 0 else 0.0


# === block: score_1 (check id='step_flat_eq') ===
def score_1(artifact, step, ctx):
    def score_flat_eq(artifact, step, ctx):
        a = 0.01
        P_target = 1000.0
        Q_target = 1e-6
        tol_rel = 0.05
        results = artifact["results"]
        total = 0.0
        cnt = 0
        for res in results:
            pts_p = sorted(res["p_points"], key=lambda d: d["x"])
            x = np.array([pt["x"] for pt in pts_p])
            p = np.array([pt["p"] for pt in pts_p])
            integral = np.trapz(p, x)
            if abs(integral - P_target) / P_target <= tol_rel:
                total += 1.0
            cnt += 1
            pts_q = sorted(res["q_points"], key=lambda d: d["x"])
            xq = np.array([pt["x"] for pt in pts_q])
            q = np.array([pt["q"] for pt in pts_q])
            integral_q = np.trapz(q, xq)
            if abs(integral_q - Q_target) / Q_target <= tol_rel:
                total += 1.0
            cnt += 1
        return total / cnt if cnt > 0 else 0.0


# === block: score_2 (check id='step_cyl_eq_trend') ===
def score_2(artifact, step, ctx):
    def score_cyl_eq_trend(artifact, step, ctx):
        P_target = 1000.0
        Q_target = 1e-6
        tol_rel = 0.05
        results = artifact["results"]
        # equilibrium
        eq_score = 0.0
        cnt = 0
        for res in results:
            pts_p = sorted(res["p_points"], key=lambda d: d["x"])
            x = np.array([pt["x"] for pt in pts_p])
            p = np.array([pt["p"] for pt in pts_p])
            integral = np.trapz(p, x)
            if abs(integral - P_target) / P_target <= tol_rel:
                eq_score += 1.0
            cnt += 1
            pts_q = sorted(res["q_points"], key=lambda d: d["x"])
            xq = np.array([pt["x"] for pt in pts_q])
            q = np.array([pt["q"] for pt in pts_q])
            integral_q = np.trapz(q, xq)
            if abs(integral_q - Q_target) / Q_target <= tol_rel:
                eq_score += 1.0
            cnt += 1
        eq_score = eq_score / cnt if cnt > 0 else 0.0
        # trend of half-width
        a_vals = {r["beta_h"]: r["a_half_width"] for r in results}
        if not a_vals:
            trend_score = 0.0
        else:
            betas = sorted(a_vals.keys())
            # paper shows contact region narrows as beta increases
            decreasing = all(a_vals[betas[i]] >= a_vals[betas[i+1]] - 1e-12 for i in range(len(betas)-1))
            positive = all(v > 0 for v in a_vals.values())
            trend_score = 1.0 if (decreasing and positive) else 0.0
        return 0.5 * eq_score + 0.5 * trend_score


# === block: score_3 (check id='step_cyl_indent') ===
def score_3(artifact, step, ctx):
    def score_cyl_indent(artifact, step, ctx):
        gold_list = step["gold"]
        gold_map = {(g["beta_h"], g["x0"]): g for g in gold_list}
        entries = artifact["cylindrical_indentation"]
        tol_rel = 0.05
        total = 0.0
        cnt = 0
        for e in entries:
            key = (e["beta_h"], e["x0"])
            if key not in gold_map:
                continue
            g = gold_map[key]
            if abs(e["delta0_m"] - g["delta0_m"]) / abs(g["delta0_m"]) <= tol_rel:
                total += 1.0
            cnt += 1
            if abs(e["phi0_V"] - g["phi0_V"]) / abs(g["phi0_V"]) <= tol_rel:
                total += 1.0
            cnt += 1
        return total / cnt if cnt > 0 else 0.0


_SCORERS = {
    'step_flat_intensity': score_0,
    'step_flat_eq': score_1,
    'step_cyl_eq_trend': score_2,
    'step_cyl_indent': score_3,
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
