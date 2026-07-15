import os
import json
import csv

# === author imports / helpers ===
import os
import csv
from collections import defaultdict
try:
    import numpy as np
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
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
    tau_dict = {}
    rev_path = os.path.join(outputs_dir, 'reversal_times.csv')
    if os.path.exists(rev_path):
        with open(rev_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                s = float(row['s'])
                h = float(row['h'])
                tau = float(row['tau'])
                key = (round(s, 5), round(h, 5))
                tau_dict[key] = tau
    return {'tau_dict': tau_dict}


# === block: score_0 (check id='reversal_scaling') ===
def score_0(artifact, step, ctx):
    required_s = step['params']['required_s']
    ratios = []
    r2s = []
    min_seg = step['params']['min_points_per_segment']
    for s_val in required_s:
        rows = [r for r in artifact if abs(float(r['s']) - s_val) < 1e-9]
        if len(rows) < 2 * min_seg:
            continue
        rows.sort(key=lambda r: abs(float(r['h'])))
        xs = []
        ys = []
        for r in rows:
            h = float(r['h'])
            tau = float(r['tau'])
            if tau <= 0:
                continue
            x = 1.0 / abs(h)
            y = np.log(tau)
            xs.append(x)
            ys.append(y)
        if len(xs) < 2 * min_seg:
            continue
        xs = np.array(xs)
        ys = np.array(ys)
        n = len(xs)
        best_r2 = -np.inf
        best_slopes = None
        for i in range(min_seg, n - min_seg + 1):
            # left segment = nucleation (larger 1/|h|), right = coalescence
            xn, yn = xs[:i], ys[:i]
            xc, yc = xs[i:], ys[i:]
            if len(xn) < min_seg or len(xc) < min_seg:
                continue
            pn = np.polyfit(xn, yn, 1)
            pc = np.polyfit(xc, yc, 1)
            if pn[0] <= 0 or pc[0] <= 0:
                continue
            ss_res = np.sum((yn - np.polyval(pn, xn))**2) + np.sum((yc - np.polyval(pc, xc))**2)
            ss_tot = np.sum((ys - np.mean(ys))**2)
            if ss_tot == 0:
                r2 = 1.0
            else:
                r2 = 1 - ss_res / ss_tot
            if r2 > best_r2:
                best_r2 = r2
                best_slopes = (pn[0], pc[0])
        if best_slopes is None:
            continue
        slope_nuc, slope_coal = best_slopes
        ratio = slope_nuc / slope_coal
        ratios.append(ratio)
        r2s.append(best_r2)
    pass_count = 0
    for ratio, r2 in zip(ratios, r2s):
        if r2 >= step['params']['r2_threshold'] and step['params']['slope_ratio_min'] <= ratio <= step['params']['slope_ratio_max']:
            pass_count += 1
    return float(pass_count) / len(required_s)


# === block: score_1 (check id='avrami_decay') ===
def score_1(artifact, step, ctx):
    tau_dict = ctx['tau_dict']
    h_vals = step['params']['h_values']
    s_tau = step['params']['s_for_tau']
    r2_threshold = step['params']['r2_threshold']
    require_peaks = step['params'].get('require_peaks', True)
    pass_h = 0
    for h in h_vals:
        key = (round(s_tau, 5), round(h, 5))
        tau = tau_dict.get(key)
        if tau is None or tau <= 0:
            continue
        rows = [r for r in artifact if abs(float(r['h']) - h) < 1e-9]
        rows.sort(key=lambda r: int(r['t']))
        if len(rows) == 0:
            continue
        ts = []
        totals = []
        fracs = []
        N5 = []
        N3 = []
        N1 = []
        for r in rows:
            t = int(r['t'])
            n72 = float(r['N_7_2'])
            n52 = float(r['N_5_2'])
            n32 = float(r['N_3_2'])
            n12 = float(r['N_1_2'])
            total = n72 + n52 + n32 + n12
            if total <= 0:
                continue
            frac = total
            ts.append(t)
            totals.append(total)
            fracs.append(frac)
            N5.append(n52)
            N3.append(n32)
            N1.append(n12)
        if len(ts) == 0:
            continue
        # Linear fit for t > tau
        x_fit = []
        y_fit = []
        for i, t in enumerate(ts):
            if t > tau and fracs[i] > 0:
                x_fit.append((t / tau) ** 3)
                y_fit.append(np.log(fracs[i]))
        if len(x_fit) < 3:
            continue
        x_arr = np.array(x_fit)
        y_arr = np.array(y_fit)
        coeffs = np.polyfit(x_arr, y_arr, 1)
        slope = coeffs[0]
        ss_res = np.sum((y_arr - np.polyval(coeffs, x_arr)) ** 2)
        ss_tot = np.sum((y_arr - np.mean(y_arr)) ** 2)
        if ss_tot == 0:
            r2 = 1.0
        else:
            r2 = 1 - ss_res / ss_tot
        linear_pass = slope < 0 and r2 >= r2_threshold
        # Peaks before tau
        peaks_ok = True
        if require_peaks:
            for arr in [N5, N3, N1]:
                # find max index among t<tau
                vals_bt = [(i, arr[i]) for i, t in enumerate(ts) if t < tau]
                if not vals_bt:
                    peaks_ok = False
                    break
                max_idx = max(vals_bt, key=lambda x: x[1])[0]
                if max_idx == 0:  # peak at start is invalid
                    peaks_ok = False
                    break
        if linear_pass and peaks_ok:
            pass_h += 1
    return float(pass_h) / len(h_vals)


_SCORERS = {
    'reversal_scaling': score_0,
    'avrami_decay': score_1,
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
