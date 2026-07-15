import os
import json
import csv

# === author imports / helpers ===
import os
import sys
import subprocess

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    import numpy as np

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
    al001_path = os.path.join(outputs_dir, 'al001_relaxation.csv')
    al110_path = os.path.join(outputs_dir, 'al110_relaxation.csv')
    with open(al001_path, newline='') as f:
        al001 = list(csv.DictReader(f))
    with open(al110_path, newline='') as f:
        al110 = list(csv.DictReader(f))

    for row in al001:
        row['spacing_change'] = float(row['spacing_change'])
        row['total_energy'] = float(row['total_energy'])
        row['work_function'] = float(row['work_function'])
        row['force_direct'] = float(row['force_direct'])
        row['force_from_derivative'] = float(row['force_from_derivative'])
    for row in al110:
        row['spacing_change'] = float(row['spacing_change'])
        row['total_energy'] = float(row['total_energy'])
        row['force'] = float(row['force'])

    x001 = np.array([r['spacing_change'] for r in al001])
    y001 = np.array([r['total_energy'] for r in al001])
    wf001 = np.array([r['work_function'] for r in al001])
    sort001 = np.argsort(x001)
    x001_s = x001[sort001]
    y001_s = y001[sort001]
    wf001_s = wf001[sort001]
    coeffs001 = np.polyfit(x001_s, y001_s, 6)
    poly001 = np.poly1d(coeffs001)
    x_fine001 = np.linspace(x001_s.min(), x001_s.max(), 1000)
    y_fine001 = poly001(x_fine001)
    d_eq001 = x_fine001[np.argmin(y_fine001)]
    wf_eq001 = np.interp(d_eq001, x001_s, wf001_s)
    idx001 = np.argmin(np.abs(x001 - d_eq001))
    force_diff = abs(al001[idx001]['force_direct'] - al001[idx001]['force_from_derivative'])

    x110 = np.array([r['spacing_change'] for r in al110])
    y110 = np.array([r['total_energy'] for r in al110])
    sort110 = np.argsort(x110)
    x110_s = x110[sort110]
    y110_s = y110[sort110]
    coeffs110 = np.polyfit(x110_s, y110_s, 6)
    poly110 = np.poly1d(coeffs110)
    x_fine110 = np.linspace(x110_s.min(), x110_s.max(), 1000)
    y_fine110 = poly110(x_fine110)
    d_eq110 = x_fine110[np.argmin(y_fine110)]

    ctx = {
        'al001_d_eq': d_eq001,
        'al001_wf_eq': wf_eq001,
        'al001_force_diff': force_diff,
        'al110_d_eq': d_eq110
    }
    return ctx


# === block: score_0 (check id='al001_equilibrium') ===
def score_0(artifact, step, ctx):
    t = step['target']
    d = ctx['al001_d_eq']
    wf = ctx['al001_wf_eq']
    d_err = abs(d - t['d_eq'])
    d_score = 1.0 if d_err <= t['d_tol_abs'] else max(0.0, 1.0 - (d_err - t['d_tol_abs']) / t['d_tol_abs'])
    wf_err = abs(wf - t['work_function'])
    wf_score = 1.0 if wf_err <= t['wf_tol_abs'] else max(0.0, 1.0 - (wf_err - t['wf_tol_abs']) / t['wf_tol_abs'])
    return 0.7 * d_score + 0.3 * wf_score


# === block: score_1 (check id='al110_equilibrium') ===
def score_1(artifact, step, ctx):
    t = step['target']
    d = ctx['al110_d_eq']
    d_err = abs(d - t['d_eq'])
    return 1.0 if d_err <= t['d_tol_abs'] else max(0.0, 1.0 - (d_err - t['d_tol_abs']) / t['d_tol_abs'])


# === block: score_2 (check id='al001_force') ===
def score_2(artifact, step, ctx):
    diff = ctx['al001_force_diff']
    max_diff = step['target']['force_diff_max']
    if diff <= max_diff:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - max_diff) / max_diff)


# === block: score_3 (check id='results_validation') ===
def score_3(artifact, step, ctx):
    t = step['target']
    summary = artifact
    r1 = summary.get('al001_relaxation_percent')
    wf = summary.get('al001_work_function_eV')
    r2 = summary.get('al110_relaxation_percent')
    total = 0.0
    if r1 is not None:
        err1 = abs(r1 - t['al001_relaxation_pct'])
        s1 = 1.0 if err1 <= t['al001_relaxation_tol'] else 0.0
        total += 0.4 * s1
    if wf is not None:
        err_wf = abs(wf - t['al001_work_function_eV'])
        swf = 1.0 if err_wf <= t['al001_work_function_tol'] else 0.0
        total += 0.2 * swf
    if r2 is not None:
        err2 = abs(r2 - t['al110_relaxation_pct'])
        s2 = 1.0 if err2 <= t['al110_relaxation_tol'] else 0.0
        total += 0.4 * s2
    return total


_SCORERS = {
    'al001_equilibrium': score_0,
    'al110_equilibrium': score_1,
    'al001_force': score_2,
    'results_validation': score_3,
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
