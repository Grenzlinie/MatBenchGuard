import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    E = 70e9
    nu = 0.3
    E_star = E/(1 - nu**2)
    Rs = [0.25e-6, 1e-6]
    s_hertz = {}
    for R in Rs:
        s_hertz[R] = (4.0/3.0) * E_star * np.sqrt(R)
    return {'s_hertz': s_hertz}


# === block: score_0 (check id='force_depth_parabolic') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    # group by (R_um, L_um)
    groups = {}
    for r in rows:
        key = (float(r['R_um']), float(r['L_um']))
        groups.setdefault(key, []).append((float(r['depth_nm']), float(r['force_nN'])))
    s_hertz_map = ctx['s_hertz']
    slope_scores = []
    r2_scores = []
    for (R_um, L_um), points in groups.items():
        depths = np.array([p[0] for p in points]) * 1e-9
        forces = np.array([p[1] for p in points]) * 1e-9
        mask = depths >= 50e-9
        if np.sum(mask) < 2:
            continue
        d = depths[mask]
        f = forces[mask]
        x = d ** 1.5
        A = np.vstack([x, np.ones_like(x)]).T
        slope, intercept = np.linalg.lstsq(A, f, rcond=None)[0]
        f_pred = slope * x + intercept
        ss_res = np.sum((f - f_pred) ** 2)
        ss_tot = np.sum((f - np.mean(f)) ** 2)
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
        R = R_um * 1e-6
        s_ref = s_hertz_map.get(R)
        if s_ref is None: continue
        rel_err = abs(slope - s_ref) / s_ref
        slope_score = max(0.0, 1.0 - (rel_err - 0.15) / 0.15)
        slope_scores.append(slope_score)
        r2_score = max(0.0, min(1.0, (r2 - 0.9) / 0.08))
        r2_scores.append(r2_score)
    if not slope_scores: return 0.0
    slope_avg = np.mean(slope_scores)
    r2_avg = np.mean(r2_scores)
    return 0.5 * slope_avg + 0.5 * r2_avg


# === block: score_1 (check id='stress_slice_parabolic') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    zs = np.array([float(r['z_um']) for r in rows])
    sigmas = np.array([float(r['sigma_zz_Pa']) for r in rows])
    if len(zs) < 2: return 0.0
    all_neg = np.all(sigmas < 0)
    neg_score = 1.0 if all_neg else 0.0
    diffs = np.diff(sigmas)
    monotonic = np.all(diffs >= 0)
    mono_score = 1.0 if monotonic else 0.0
    return 0.4 * neg_score + 0.6 * mono_score


# === block: score_2 (check id='convergence_mse') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) != 5: return 0.0
    expected = [32,64,128,256,512]
    present = set()
    mse_vals = []
    for r in rows:
        gs = int(r['grid_size'])
        mse = float(r['MSE'])
        present.add(gs)
        if gs in expected:
            mse_vals.append((gs, mse))
    if set(expected) != present:
        return 0.0
    mse_sorted = sorted(mse_vals, key=lambda x: x[0])
    mses = [m[1] for m in mse_sorted]
    decreasing = all(mses[i] > mses[i+1] for i in range(len(mses)-1))
    plausible = all(0 < m < 0.5 for m in mses)
    score = 0.2 + (0.4 if decreasing else 0.0) + (0.4 if plausible else 0.0)
    return score


_SCORERS = {
    'force_depth_parabolic': score_0,
    'stress_slice_parabolic': score_1,
    'convergence_mse': score_2,
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
