import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy', 'scipy', 'pycalphad'])
import csv, math, sys, os
import numpy as np
from scipy import optimize, interpolate
from pycalphad import Database, calculate, equilibrium, variables as v
import pkgutil
import warnings
warnings.filterwarnings('ignore')


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
    import numpy as np

    sigma = 0.235
    Vm = 16.26e-6
    R = 8.314
    T = 423.15
    X0 = 0.1929
    Xb = 0.98
    e_factor = 0.487
    RT = R * T

    N = 10000
    X_arr = np.linspace(X0, Xb, N)
    integrand_vals = ((Xb - X_arr) / (1.0 - X_arr)) * (1.0 / X_arr)
    cum_integral = np.zeros(N)
    cum_integral[0] = 0.0
    for i in range(1, N):
        h = X_arr[i] - X_arr[i-1]
        cum_integral[i] = cum_integral[i-1] + 0.5 * (integrand_vals[i-1] + integrand_vals[i]) * h

    def target_to_X(target):
        target_integral = target / e_factor
        idx = np.searchsorted(cum_integral, target_integral)
        idx = np.clip(idx, 1, N-1)
        x1, x2 = X_arr[idx-1], X_arr[idx]
        f1, f2 = cum_integral[idx-1], cum_integral[idx]
        if f2 == f1:
            return x1
        return x1 + (target_integral - f1) * (x2 - x1) / (f2 - f1)

    gold_radii = np.logspace(np.log10(1.0), np.log10(200.0), 50)
    gold_X = np.zeros_like(gold_radii)
    for i, r in enumerate(gold_radii):
        rhs = (2 * sigma * Vm) / (r * 1e-9 * RT)
        gold_X[i] = target_to_X(rhs)

    return {
        'gold_radii': gold_radii,
        'gold_X': gold_X,
        'X_flat': X0
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import numpy as np
    radii = np.array([float(row['radius_nm']) for row in artifact])
    X_agent = np.array([float(row['X_Sn_fcc']) for row in artifact])
    if len(radii) == 0:
        return 0.0

    gold_radii = ctx['gold_radii']
    gold_X = ctx['gold_X']
    X_flat = ctx['X_flat']
    # interpolate gold curve at agent's radii
    X_gold = np.interp(radii, gold_radii, gold_X, left=gold_X[0], right=X_flat)

    with np.errstate(divide='ignore', invalid='ignore'):
        rel_errors = np.abs(X_agent - X_gold) / np.clip(np.abs(X_gold), 1e-9, None)
    mare = np.nanmean(rel_errors)
    if np.isnan(mare):
        mare = 1.0

    if mare <= 0.1:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (mare - 0.1) / 0.2)
    return float(score)


_SCORERS = {
    'step_01': score_0,
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
