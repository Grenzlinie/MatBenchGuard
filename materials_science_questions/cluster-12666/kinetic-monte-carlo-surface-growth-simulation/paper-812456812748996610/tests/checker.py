import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
    from scipy.stats import linregress
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy', 'scipy'])
    import numpy as np
    from scipy.stats import linregress

import math
import csv
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
    return violations


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
    return {'output_dir': '/app/outputs'}


# === block: score_0 (check id='arrhenius_structural') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    if len(rows) != 6:
        return 0.0
    tof_vals = []
    temps = []
    try:
        for r in rows:
            t = float(r['Temperature (K)'])
            f = float(r['TurnoverFrequency (s⁻¹)'])
            if f <= 0:
                return 0.0
            temps.append(t)
            tof_vals.append(f)
        if sorted(temps) != temps:  # ensure increasing
            return 0.0
        for i in range(1, len(tof_vals)):
            if tof_vals[i] >= tof_vals[i-1]:  # must decrease with T
                return 0.0
    except (ValueError, KeyError):
        return 0.0
    return 1.0


# === block: score_1 (check id='arrhenius_recompute_Ea') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if len(rows) != 6:
        return 0.0
    x = []
    y = []
    try:
        for r in rows:
            t = float(r['Temperature (K)'])
            tof = float(r['TurnoverFrequency (s⁻¹)'])
            if tof <= 0:
                return 0.0
            x.append(1.0/t)
            y.append(math.log(tof))
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        R_kcal = 0.001987  # kcal/(mol·K)
        Ea = -slope * R_kcal
        range_min = step.get('target', {}).get('range_min', 9.0)
        range_max = step.get('target', {}).get('range_max', 12.0)
        if range_min <= Ea <= range_max:
            return 1.0
        # linear decay outside range
        if Ea < range_min:
            dev = range_min - Ea
        else:
            dev = Ea - range_max
        decay_band = 0.5 * (range_max - range_min)  # 1.5 kcal
        if dev >= decay_band:
            return 0.0
        return 1.0 - dev / decay_band
    except (ValueError, KeyError, TypeError):
        return 0.0


# === block: score_2 (check id='activation_energy_consistency') ===
def score_2(artifact, step, ctx):
    reported = artifact  # string
    try:
        reported_val = float(reported.strip())
    except (ValueError, AttributeError):
        return 0.0
    # recompute Ea from arrhenius CSV
    dir_out = ctx.get('output_dir', '/app/outputs')
    arrh_path = os.path.join(dir_out, 'arrhenius_tof.csv')
    if not os.path.exists(arrh_path):
        return 0.0
    try:
        with open(arrh_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if len(rows) != 6:
            return 0.0
        x = []
        y = []
        for r in rows:
            t = float(r['Temperature (K)'])
            tof = float(r['TurnoverFrequency (s⁻¹)'])
            if tof <= 0:
                return 0.0
            x.append(1.0/t)
            y.append(math.log(tof))
        slope, _, _, _, _ = linregress(x, y)
        recomputed_Ea = -slope * 0.001987
        tol = step.get('tolerance', {}).get('abs_tol', 2.0)
        if abs(reported_val - recomputed_Ea) <= tol:
            return 1.0
        return 0.0
    except:
        return 0.0


# === block: score_3 (check id='orders_H2_order') ===
def score_3(artifact, step, ctx):
    rows = artifact
    h2_points = []
    try:
        for r in rows:
            lab = r.get('experiment_label', '')
            if lab.startswith('H2_'):
                p = float(r['Pressure_Torr'])
                tof = float(r['TurnoverFrequency_s-1'])
                if tof <= 0 or p <= 0:
                    return 0.0
                h2_points.append((math.log(p), math.log(tof)))
        if len(h2_points) < 2:
            return 0.0
        x = [p[0] for p in h2_points]
        y = [p[1] for p in h2_points]
        slope, _, _, _, _ = linregress(x, y)
        order = slope
        min_o = step.get('target', {}).get('order_range_min', 0.65)
        max_o = step.get('target', {}).get('order_range_max', 0.85)
        if min_o <= order <= max_o:
            return 1.0
        if order < min_o:
            dev = min_o - order
        else:
            dev = order - max_o
        decay_band = 0.5 * (max_o - min_o)
        if dev >= decay_band:
            return 0.0
        return 1.0 - dev / decay_band
    except (ValueError, KeyError):
        return 0.0


# === block: score_4 (check id='orders_C2H4_order') ===
def score_4(artifact, step, ctx):
    rows = artifact
    c2h4_points = []
    try:
        for r in rows:
            lab = r.get('experiment_label', '')
            if lab.startswith('C2H4_'):
                p = float(r['Pressure_Torr'])
                tof = float(r['TurnoverFrequency_s-1'])
                if tof <= 0 or p <= 0:
                    return 0.0
                c2h4_points.append((math.log(p), math.log(tof)))
        if len(c2h4_points) < 2:
            return 0.0
        x = [p[0] for p in c2h4_points]
        y = [p[1] for p in c2h4_points]
        slope, _, _, _, _ = linregress(x, y)
        order = slope
        min_o = step.get('target', {}).get('order_range_min', -0.4)
        max_o = step.get('target', {}).get('order_range_max', 0.0)
        if min_o <= order <= max_o:
            return 1.0
        if order < min_o:
            dev = min_o - order
        else:
            dev = order - max_o
        decay_band = 0.5 * (max_o - min_o)  # 0.2
        if dev >= decay_band:
            return 0.0
        return 1.0 - dev / decay_band
    except (ValueError, KeyError):
        return 0.0


_SCORERS = {
    'arrhenius_structural': score_0,
    'arrhenius_recompute_Ea': score_1,
    'activation_energy_consistency': score_2,
    'orders_H2_order': score_3,
    'orders_C2H4_order': score_4,
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
    violations = _ff_validate_output_contract()
    if violations:
        os.makedirs("/logs/verifier", exist_ok=True)
        with open("/logs/verifier/breakdown.json", "w") as f:
            json.dump({"output_contract_violations": violations}, f, indent=2)
        raise SystemExit(0)

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