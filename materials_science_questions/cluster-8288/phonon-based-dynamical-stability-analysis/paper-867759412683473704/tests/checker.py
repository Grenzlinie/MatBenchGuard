import os
import json
import csv

# === author imports / helpers ===
import os
import json
import csv
import subprocess
import sys

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'numpy', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])
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
    outputs = os.path.join(outputs_dir) if os.path.isdir(outputs_dir) else outputs_dir
    ctx = {}
    mono_path = os.path.join(outputs, 'monolayer_spin_splitting.json')
    if os.path.exists(mono_path):
        with open(mono_path) as f:
            ctx['mono'] = json.load(f)
    bilayer_path = os.path.join(outputs, 'bilayer_ez_splitting.csv')
    if os.path.exists(bilayer_path):
        with open(bilayer_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        ez = []
        dintra = []
        dinter = []
        for r in rows:
            try:
                ez.append(float(r['Ez']))
                dintra.append(float(r['Delta_intra']))
                dinter.append(float(r['Delta_inter']))
            except:
                continue
        if len(ez) >= 3:
            ez_np = np.array(ez)
            dinter_np = np.array(dinter)
            dintra_np = np.array(dintra)
            coeffs_inter = np.polyfit(ez_np, dinter_np, 1)
            slope_inter = coeffs_inter[0]
            intercept_inter = coeffs_inter[1]
            resid = dinter_np - np.polyval(coeffs_inter, ez_np)
            ss_res = np.sum(resid**2)
            ss_tot = np.sum((dinter_np - np.mean(dinter_np))**2)
            r2 = 1 - ss_res/ss_tot if ss_tot != 0 else 1.0
            coeffs_intra = np.polyfit(ez_np, dintra_np, 1)
            slope_intra = coeffs_intra[0]
            mean_dintra = float(np.mean(dintra_np))
            ctx['bilayer'] = {
                'slope_inter': slope_inter,
                'intercept_inter': intercept_inter,
                'r2': r2,
                'slope_intra': slope_intra,
                'mean_dintra': mean_dintra
            }
    return ctx


# === block: score_0 (check id='monolayer_delta_soc') ===
def score_0(artifact, step, ctx):
    mono = ctx.get('mono')
    if mono is None:
        return 0.0
    value = mono.get('delta_soc_mev', None)
    if value is None:
        return 0.0
    ref = step['reference']
    tol = step['tolerance']
    diff = abs(value - ref)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='monolayer_bandgap') ===
def score_1(artifact, step, ctx):
    mono = ctx.get('mono')
    if mono is None:
        return 0.0
    value = mono.get('band_gap_indirect_ev', None)
    if value is None:
        return 0.0
    ref = step['reference']
    tol = step['tolerance']
    diff = abs(value - ref)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='bilayer_linear_fit') ===
def score_2(artifact, step, ctx):
    b = ctx.get('bilayer')
    if b is None:
        return 0.0
    r2 = b['r2']
    slope = b['slope_inter']
    intercept = b['intercept_inter']
    r2_thresh = step['r2_threshold']
    slope_min = step.get('slope_min', 0.0)
    int_max = step['intercept_abs_max']
    r2_score = 1.0 if r2 >= r2_thresh else max(0.0, r2 / r2_thresh)
    slope_score = 1.0 if slope > slope_min else 0.0
    intercept_score = 1.0 if abs(intercept) <= int_max else max(0.0, 1.0 - (abs(intercept) - int_max) / int_max)
    score = (r2_score + slope_score + intercept_score) / 3.0
    return max(0.0, min(1.0, score))


# === block: score_3 (check id='bilayer_crossover') ===
def score_3(artifact, step, ctx):
    b = ctx.get('bilayer')
    if b is None:
        return 0.0
    slope_int = b['slope_inter']
    intercept_int = b['intercept_inter']
    mean_intra = b['mean_dintra']
    if slope_int <= 0:
        return 0.0
    ez_cross = (mean_intra - intercept_int) / slope_int
    target = step['crossover_target']
    tol = step['crossover_tolerance']
    diff = abs(ez_cross - target)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    else:
        return 0.0


# === block: score_4 (check id='bilayer_intra_slope') ===
def score_4(artifact, step, ctx):
    b = ctx.get('bilayer')
    if b is None:
        return 0.0
    s = b['slope_intra']
    thresh = step['slope_abs_max']
    if abs(s) <= thresh:
        return 1.0
    else:
        return max(0.0, 1.0 - (abs(s) - thresh) / thresh)


# === block: score_5 (check id='bilayer_intra_mean') ===
def score_5(artifact, step, ctx):
    b = ctx.get('bilayer')
    if b is None:
        return 0.0
    mean_val = b['mean_dintra']
    ref = step['reference']
    tol = step['tolerance']
    diff = abs(mean_val - ref)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'monolayer_delta_soc': score_0,
    'monolayer_bandgap': score_1,
    'bilayer_linear_fit': score_2,
    'bilayer_crossover': score_3,
    'bilayer_intra_slope': score_4,
    'bilayer_intra_mean': score_5,
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
