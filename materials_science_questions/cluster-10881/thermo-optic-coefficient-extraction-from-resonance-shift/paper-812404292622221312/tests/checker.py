import os
import json
import csv

# === author imports / helpers ===
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy'])
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
    def delta_t_solver(t_m, dt=0.1, t_max=150, t_points=None):
        # constants
        rho = 5370.0   # kg/m^3
        c = 320.0      # J/(kg K)
        V = 1.4e-13    # m^3
        I_max = 40.0   # A
        P_factor = 1.4 # V
        factor = 1.0 / (rho * c * V)

        def I(t):
            if t <= 0:
                return 0.0
            return I_max * (t / t_m)**2 * np.exp(-2.0 * t / t_m + 2.0)

        N = int(t_max / dt) + 1
        times = np.linspace(0, t_max, N)
        P = np.array([P_factor * I(t) for t in times])
        dT = np.zeros(N)
        # i=0 already 0
        for i in range(1, N):
            s = 0.0
            for j in range(1, i):
                Pj = P[j]
                if Pj == 0.0:
                    continue
                s += Pj * (dT[i-j] - dT[i-j-1])
            dT[i] = factor * s
        # interpolate to requested points
        if t_points is not None:
            vals = {}
            for tp in t_points:
                idx = int(round(tp / dt))
                if 0 <= idx < N:
                    vals[tp] = float(dT[idx])
                else:
                    vals[tp] = 0.0
            return vals
        return times, dT

    # compute reference values
    step_config = spec.get('steps', [])[0]  # only one step
    t_points = step_config['t_points']
    t_m_values = step_config['t_m_values']
    ref_vals = {}
    for tm in t_m_values:
        vals = delta_t_solver(tm, dt=0.1, t_max=150, t_points=t_points)
        ref_vals[tm] = vals
    return {'ref_vals': ref_vals, 'tolerance_K': step_config['tolerance_K']}


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    ref_vals = ctx['ref_vals']
    tolerance = step['tolerance_K']
    target_times = step['t_points']
    t_m_vals = step['t_m_values']
    # check CSV columns
    if not artifact:
        return 0.0
    first_row = artifact[0]
    required_cols = ['t_ns'] + [f'tm_{tm}_K' for tm in t_m_vals]
    if not all(col in first_row for col in required_cols):
        return 0.0
    # build lookup
    time_to_row = {}
    for row in artifact:
        try:
            t = float(row['t_ns'])
            time_to_row[t] = row
        except (ValueError, KeyError):
            continue
    total = len(target_times) * len(t_m_vals)
    correct = 0
    for t in target_times:
        if t not in time_to_row:
            continue
        row = time_to_row[t]
        for tm in t_m_vals:
            col = f'tm_{tm}_K'
            try:
                val = float(row[col])
            except (ValueError, KeyError):
                continue
            ref = ref_vals[tm][t]
            if abs(val - ref) < tolerance:
                correct += 1
    return correct / total


_SCORERS = {
    'step01': score_0,
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
