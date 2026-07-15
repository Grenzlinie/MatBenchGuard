import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import re
from collections import defaultdict

try:
    import numpy as np
    from scipy.optimize import curve_fit
except ImportError:
    import subprocess
    import sys
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--quiet", "numpy", "scipy",
         "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"]
    )
    import numpy as np
    from scipy.optimize import curve_fit


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


# === block: score_0 (check id='lattice_parameters_shape') ===
def score_0(artifact, step, ctx):
    if artifact is None: return 0.0
    required_cols = ['condition_id', 'epsilon_aa', 'a', 'b', 'c', 'epsilon_bb', 'epsilon_cc']
    if not all(col in artifact[0] for col in required_cols):
        return 0.0
    has_strain = any(float(row.get('epsilon_aa', 0)) < -0.0001 for row in artifact)
    if not has_strain:
        return 0.0
    return 1.0


# === block: score_1 (check id='poisson_ratios_recompute') ===
def score_1(artifact, step, ctx):
    if artifact is None: return 0.0
    lattice_path = os.path.join('/app/outputs', 'lattice_parameters.csv')
    if not os.path.exists(lattice_path):
        return 0.0
    with open(lattice_path) as f:
        reader = csv.DictReader(f)
        lattice_data = list(reader)
    epsilon_aa = [float(row['epsilon_aa']) for row in lattice_data]
    epsilon_bb = [float(row['epsilon_bb']) for row in lattice_data]
    epsilon_cc = [float(row['epsilon_cc']) for row in lattice_data]
    def linear_fit(x, y):
        A = np.vstack([x, np.ones(len(x))]).T
        slope, _ = np.linalg.lstsq(A, y, rcond=None)[0]
        return slope
    x = [-e for e in epsilon_aa]
    slope_bb = linear_fit(x, epsilon_bb)
    slope_cc = linear_fit(x, epsilon_cc)
    gold = step['hidden']['gold_poisson']
    rel_tol = step['hidden']['rel_tol']
    def within_tol(val, gold):
        return abs(val - gold) / abs(gold) <= rel_tol
    score = 0.0
    if within_tol(slope_bb, gold['ν_ba']):
        score += 0.5
    if within_tol(slope_cc, gold['ν_ca']):
        score += 0.5
    return score


# === block: score_2 (check id='diffuse_line_cuts_shape') ===
def score_2(artifact, step, ctx):
    if artifact is None: return 0.0
    required_cols = ['condition_id', 'peak_label', 'H', 'intensity']
    if not all(col in artifact[0] for col in required_cols):
        return 0.0
    condition_ids = set(row['condition_id'] for row in artifact)
    peaks = set(row['peak_label'] for row in artifact)
    if len(condition_ids) < 3 or len(peaks) < 2:
        return 0.0
    return 1.0


# === block: score_3 (check id='fitting_results_loadbearing') ===
def score_3(artifact, step, ctx):
    if artifact is None: return 0.0
    lattice_path = os.path.join('/app/outputs', 'lattice_parameters.csv')
    if not os.path.exists(lattice_path):
        return 0.0
    with open(lattice_path) as f:
        lattice_data = list(csv.DictReader(f))
    strain_map = {}
    temp_map = {}
    for row in lattice_data:
        cid = row['condition_id']
        strain_map[cid] = float(row['epsilon_aa'])
        m = re.search(r'(\d+)K', cid)
        if m:
            temp_map[cid] = int(m.group(1))
    diffuse_path = os.path.join('/app/outputs', 'diffuse_line_cuts.csv')
    if not os.path.exists(diffuse_path):
        return 0.0
    with open(diffuse_path) as f:
        line_data = list(csv.DictReader(f))
    groups = defaultdict(list)
    for row in line_data:
        groups[(row['condition_id'], row['peak_label'])].append((float(row['H']), float(row['intensity'])))
    def lorentzian(x, A, q0, kappa, c, d):
        return A / ((x - q0)**2 + kappa**2) + c + d*x
    gold_q0 = step['hidden']['gold_q0']
    q0_tol = step['hidden']['q0_tol']
    gold_xi = step['hidden']['gold_xi']
    xi_tol = step['hidden']['xi_tol']
    scores = []
    for (cid, peak_label), points in groups.items():
        if len(points) < 10:
            continue
        points.sort(key=lambda x: x[0])
        H_vals = np.array([p[0] for p in points])
        I_vals = np.array([p[1] for p in points])
        imax = np.max(I_vals)
        imin = np.min(I_vals)
        q0_init = H_vals[np.argmax(I_vals)]
        try:
            popt, _ = curve_fit(lorentzian, H_vals, I_vals, p0=[imax-imin, q0_init, 0.1, imin, 0], maxfev=5000,
                                bounds=([0, -np.inf, 0, -np.inf, -np.inf], [np.inf, np.inf, np.inf, np.inf, np.inf]))
            A_fit, q0_fit, kappa_fit, c_fit, d_fit = popt
            xi_fit = 1.0 / kappa_fit if kappa_fit > 0 else float('inf')
        except Exception:
            continue
        expected_q0 = gold_q0.get(peak_label)
        if expected_q0 is None:
            continue
        q0_ok = abs(q0_fit - expected_q0) <= q0_tol
        xi_ok = abs(xi_fit - gold_xi) <= xi_tol
        score_cond = (0.5 if q0_ok else 0.0) + (0.5 if xi_ok else 0.0)
        scores.append(score_cond)
    if not scores:
        return 0.0
    avg_score = np.mean(scores)
    target_magnitudes = [0.0005, 0.002, 0.011]
    condition_sets = defaultdict(list)
    for cid, val in strain_map.items():
        magnitude = -val
        condition_sets.setdefault(round(magnitude, 6), []).append(cid)
    sat_ok = True
    for mag in target_magnitudes:
        if mag in condition_sets:
            if not any(cid for cid in condition_sets[mag] if any((cid, peak) in groups for peak in gold_q0)):
                sat_ok = False
        else:
            sat_ok = False
    temp_targets = {30, 78, 101}
    temp_present = set()
    for cid, val in strain_map.items():
        if abs(-val - 0.011) < 0.001:
            t = temp_map.get(cid)
            if t in temp_targets:
                if any(groups.get((cid, peak)) for peak in gold_q0):
                    temp_present.add(t)
    qual_score = 1.0 if (sat_ok and len(temp_present) == 3) else (0.5 if sat_ok else 0.0)
    total_score = avg_score * 0.9 + qual_score * 0.1
    return min(max(total_score, 0.0), 1.0)


_SCORERS = {
    'lattice_parameters_shape': score_0,
    'poisson_ratios_recompute': score_1,
    'diffuse_line_cuts_shape': score_2,
    'fitting_results_loadbearing': score_3,
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
