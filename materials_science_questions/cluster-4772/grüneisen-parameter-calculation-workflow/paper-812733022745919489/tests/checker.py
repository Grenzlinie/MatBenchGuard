import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, importlib, pkgutil, site
def _ensure_pkg(pkg, pip_name):
    if pkgutil.find_loader(pkg) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", pip_name])
        importlib.reload(site)
_ensure_pkg('numpy', 'numpy')
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
    return {}


# === block: score_0 (check id='thermal_expansivity') ===
def score_0(artifact, step, ctx):
        import numpy as np
        import csv
        if not artifact:
            return 0.0
        T_vals = []
        alpha_vals = []
        for row in artifact:
            try:
                t = float(row['T'])
                a = float(row['alpha'])
                T_vals.append(t)
                alpha_vals.append(a)
            except (ValueError, KeyError):
                return 0.0
        if len(T_vals) < 3:
            return 0.0
        T_arr = np.array(T_vals)
        alpha_arr = np.array(alpha_vals)
        # hidden references
        ref_T = np.array(step.get('hidden_reference_T', []))
        ref_alpha = np.array(step.get('hidden_reference_alpha', []))
        # 1. numeric deviation (0.4 weight)
        tol_mae = float(step.get('tolerance_mae', 1.5e-6))
        # we compute MAE at the common temperatures
        if len(ref_T) > 0 and len(ref_alpha) > 0:
            # interpolate agent alpha to ref temperature points
            alpha_interp = np.interp(ref_T, T_arr, alpha_arr)
            mae = np.mean(np.abs(alpha_interp - ref_alpha))
            # score decays linearly from 1 at mae=0 to 0 at mae=tol_mae
            score_num = max(0.0, 1.0 - mae/tol_mae)
        else:
            score_num = 0.0
        # 2. sign check: alpha negative at temperatures 5..55 K
        sign_neg_T = [t for t in range(5, 60, 5)]  # 5..55
        neg_pass = all(alpha_arr[np.argmin(np.abs(T_arr - t))] < 0 for t in sign_neg_T)
        # 3. minimum location in window 35-45 K
        min_idx = np.argmin(alpha_arr)
        min_T_val = T_arr[min_idx]
        low_win, high_win = step.get('min_T_window', [35, 45])
        min_loc_ok = low_win <= min_T_val <= high_win
        # 4. zero crossing: negative at 55, positive at 60
        idx_neg = np.argmin(np.abs(T_arr - float(step.get('zero_cross_neg_T', 55))))
        idx_pos = np.argmin(np.abs(T_arr - float(step.get('zero_cross_pos_T', 60))))
        cross_ok = (alpha_arr[idx_neg] < 0) and (alpha_arr[idx_pos] > 0)
        # 5. overall positive after 60
        high_T_ok = np.all(alpha_arr[T_arr >= 65] > 0)
        # combine scores: 0.4 for numeric, 0.6 for structural (distributed equally)
        struct_score = (0.2*int(neg_pass) + 0.2*int(min_loc_ok) + 0.2*int(cross_ok) + 0.2*int(high_T_ok))
        total = 0.4*score_num + 0.6*struct_score
        return max(0.0, min(1.0, total))


# === block: score_1 (check id='gruneisen_freq') ===
def score_1(artifact, step, ctx):
        import numpy as np
        if not artifact:
            return 0.0
        low_freqs = []
        gamma_Cs = []
        for row in artifact:
            try:
                lf = float(row['low_freq'])
                gc = float(row['gamma_C'])
                low_freqs.append(lf)
                gamma_Cs.append(gc)
            except (ValueError, KeyError):
                return 0.0
        if len(low_freqs) == 0:
            return 0.0
        low_arr = np.array(low_freqs)
        gc_arr = np.array(gamma_Cs)
        # sort by low_freq
        idx = np.argsort(low_arr)
        low_arr = low_arr[idx]
        gc_arr = gc_arr[idx]
        # 1. sum of gamma_C for bins with low_freq < 100
        sum_neg = np.sum(gc_arr[low_arr < 100])
        sum_ok = sum_neg < float(step.get('negative_sum_low_bound', 0.0))
        # 2. most negative bin within window [40,70]
        min_idx = np.argmin(gc_arr)
        min_low = low_arr[min_idx]
        win_low, win_high = step.get('most_negative_bin_window', [40, 70])
        min_loc_ok = win_low <= min_low <= win_high
        # 3. high-frequency bins (>100) are non-negative
        high_idx = low_arr >= float(step.get('pos_high_bound', 100))
        high_ok = bool(np.all(gc_arr[high_idx] >= 0)) if np.any(high_idx) else True
        # weighted score: 0.4 sum, 0.3 min loc, 0.3 high positivity
        score = 0.4*int(sum_ok) + 0.3*int(min_loc_ok) + 0.3*int(high_ok)
        return float(score)


# === block: score_2 (check id='total_gamma_cv') ===
def score_2(artifact, step, ctx):
        import math
        if not artifact or len(artifact) < 1:
            return 0.0
        row = artifact[0]
        try:
            val = float(row['gamma_CV'])
        except (KeyError, ValueError):
            return 0.0
        gold = float(step.get('hidden_gold', -0.04))
        tol = float(step.get('tolerance_rel', 0.2))
        if abs(gold) < 1e-12:
            return 1.0 if abs(val - gold) < 1e-12 else 0.0
        err_rel = abs(val - gold) / abs(gold)
        if err_rel <= tol:
            return 1.0
        else:
            # partial credit decays linearly up to 2*tol
            score = max(0.0, 1.0 - (err_rel - tol) / tol)
            return float(score)


_SCORERS = {
    'thermal_expansivity': score_0,
    'gruneisen_freq': score_1,
    'total_gamma_cv': score_2,
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
