import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    import numpy as np

import csv
import os
from collections import defaultdict

def compute_properties(data, strain_limit=0.02):
    strains = np.array([float(r['strain']) for r in data])
    stresses = np.array([float(r['stress_GPa']) for r in data])
    mask = strains <= strain_limit
    if np.sum(mask) < 2:
        return None, None
    x = strains[mask]
    y = stresses[mask]
    A = np.vstack([x, np.ones_like(x)]).T
    slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
    young_modulus = slope
    uts = np.max(stresses)
    return young_modulus, uts

def get_condition_groups(rows):
    groups = defaultdict(list)
    for r in rows:
        key = (float(r['thickness_nm']), float(r['temperature_K']))
        groups[key].append(r)
    for key in groups:
        groups[key].sort(key=lambda x: float(x['strain']))
    return groups


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


# === block: score_0 (check id='raw_data') ===
def score_0(artifact, step, ctx):
    required_cols = {'thickness_nm', 'temperature_K', 'strain', 'stress_GPa'}
    if not artifact:
        return 0.0
    cols = set(artifact[0].keys())
    if not required_cols <= cols:
        return 0.0
    expected = [(1,300),(2,300),(3,300),(4,300),(5,300),(6,300),
                (1,200),(1,500),(1,700),(1,900)]
    present = set()
    for r in artifact:
        try:
            t = round(float(r['thickness_nm']), 2)
            T = round(float(r['temperature_K']), 2)
            present.add((t, T))
        except:
            pass
    for (th,tm) in expected:
        found = any(abs(t-th) < 0.1 and abs(T-tm) < 0.1 for t,T in present)
        if not found:
            return 0.0

    # All required conditions are present; now evaluate qualitative trends
    from collections import defaultdict
    groups = defaultdict(list)
    for r in artifact:
        key = (float(r['thickness_nm']), float(r['temperature_K']))
        groups[key].append(r)
    for key in groups:
        groups[key].sort(key=lambda x: float(x['strain']))

    def _safe_compute(data):
        strains = np.array([float(r['strain']) for r in data])
        stresses = np.array([float(r['stress_GPa']) for r in data])
        mask = strains <= 0.02
        if np.sum(mask) < 2:
            return None, None
        x = strains[mask]
        y = stresses[mask]
        A = np.vstack([x, np.ones_like(x)]).T
        slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
        uts = np.max(stresses)
        return float(slope), float(uts)

    score = 1.0

    # Thickness trend: 1..4 nm at 300 K – both E and UTS must strictly decrease
    for t in (1,2,3):
        key1 = (t, 300); key2 = (t+1, 300)
        if key1 not in groups or key2 not in groups:
            return 0.0
        E1, U1 = _safe_compute(groups[key1])
        E2, U2 = _safe_compute(groups[key2])
        if E1 is None or E2 is None:
            return 0.0
        if E1 <= E2:
            score -= 0.05
        if U1 <= U2:
            score -= 0.05

    # Plateau: 4,5,6 nm – values should be within 10 % of each other
    for prop in ('E','UTS'):
        vals = []
        for t in (4,5,6):
            key = (t, 300)
            if key not in groups:
                return 0.0
            E, U = _safe_compute(groups[key])
            if E is None:
                return 0.0
            vals.append(E if prop == 'E' else U)
        if max(vals) - min(vals) > 0.1 * max(vals):
            score -= 0.1

    # Temperature trend: 1 nm film – E and UTS must strictly decrease
    for i in range(4):
        T1 = [200,300,500,700,900][i]
        T2 = [200,300,500,700,900][i+1]
        key1 = (1, T1); key2 = (1, T2)
        if key1 not in groups or key2 not in groups:
            return 0.0
        E1, U1 = _safe_compute(groups[key1])
        E2, U2 = _safe_compute(groups[key2])
        if E1 is None or E2 is None:
            return 0.0
        if E1 <= E2:
            score -= 0.05
        if U1 <= U2:
            score -= 0.05

    # Drop from 500 K to 900 K must be positive (any decrease)
    key500 = (1, 500); key900 = (1, 900)
    E500, U500 = _safe_compute(groups[key500])
    E900, U900 = _safe_compute(groups[key900])
    if E500 is None or E900 is None:
        return 0.0
    if E500 <= E900:
        score -= 0.1
    if U500 <= U900:
        score -= 0.1

    # Curve shape: 1 nm global max after first crest; thicker films global max at first crest
    for t in (1,2,3,4,5,6):
        key = (t, 300)
        data = groups[key]
        strains = np.array([float(r['strain']) for r in data])
        stresses = np.array([float(r['stress_GPa']) for r in data])
        if len(stresses) == 0:
            return 0.0
        max_stress = np.max(stresses)
        if max_stress <= 0:
            return 0.0
        n = len(stresses)
        local_max_indices = []
        for i in range(1, n-1):
            if stresses[i] > stresses[i-1] and stresses[i] > stresses[i+1] and stresses[i] > 0.01 * max_stress:
                local_max_indices.append(i)
        if not local_max_indices:
            return 0.0
        global_max_idx = int(np.argmax(stresses))
        if t == 1:
            if len(local_max_indices) < 2 or global_max_idx <= local_max_indices[0]:
                score -= 0.1
        else:
            if global_max_idx != local_max_indices[0]:
                score -= 0.05

    return max(0.0, min(1.0, score))


# === block: score_1 (check id='thickness_trend') ===
def score_1(artifact, step, ctx):
    groups = get_condition_groups(artifact)
    conditions_300 = [(t,300) for t in [1,2,3,4,5,6]]
    props = {}
    for (th,temp) in conditions_300:
        key = (th, temp)
        data = groups.get(key)
        if not data:
            return 0.0
        E, UTS = compute_properties(data)
        if E is None or UTS is None:
            return 0.0
        props[(th,temp)] = (E, UTS)
    e_vals = [props[(t,300)][0] for t in range(1,5)]
    uts_vals = [props[(t,300)][1] for t in range(1,5)]
    for i in range(3):
        if e_vals[i] < e_vals[i+1] * 0.98:
            return 0.0
    for i in range(3):
        if uts_vals[i] < uts_vals[i+1] * 0.98:
            return 0.0
    e4 = props[(4,300)][0]; e5 = props[(5,300)][0]; e6 = props[(6,300)][0]
    if abs(e4 - e5) > 0.05*max(e4,e5) or abs(e5 - e6) > 0.05*max(e5,e6):
        return 0.0
    u4 = props[(4,300)][1]; u5 = props[(5,300)][1]; u6 = props[(6,300)][1]
    if abs(u4 - u5) > 0.05*u4 or abs(u5 - u6) > 0.05*u5:
        return 0.0
    if e_vals[0] < 1.5 * e_vals[1] or uts_vals[0] < 1.5 * uts_vals[1]:
        return 0.0
    return 1.0


# === block: score_2 (check id='temperature_trend') ===
def score_2(artifact, step, ctx):
    groups = get_condition_groups(artifact)
    temps = [200,300,500,700,900]
    props = {}
    for T in temps:
        key = (1, T)
        data = groups.get(key)
        if not data:
            return 0.0
        E, UTS = compute_properties(data)
        if E is None or UTS is None:
            return 0.0
        props[(1,T)] = (E, UTS)
    e_vals = [props[(1,T)][0] for T in temps]
    uts_vals = [props[(1,T)][1] for T in temps]
    for i in range(4):
        if e_vals[i] < e_vals[i+1] * 0.98:
            return 0.0
        if uts_vals[i] < uts_vals[i+1] * 0.98:
            return 0.0
    e500 = props[(1,500)][0]; e900 = props[(1,900)][0]
    if (e500 - e900) / e500 < 0.2:
        return 0.0
    u500 = props[(1,500)][1]; u900 = props[(1,900)][1]
    if (u500 - u900) / u500 < 0.2:
        return 0.0
    return 1.0


# === block: score_3 (check id='shape_check') ===
def score_3(artifact, step, ctx):
    groups = get_condition_groups(artifact)
    thicknesses = [1,2,3,4,5,6]
    for th in thicknesses:
        key = (th, 300)
        data = groups.get(key)
        if not data:
            return 0.0
        strains = np.array([float(r['strain']) for r in data])
        stresses = np.array([float(r['stress_GPa']) for r in data])
        max_stress = np.max(stresses) if len(stresses) else 0
        if max_stress <= 0:
            return 0.0
        local_max_indices = []
        n = len(stresses)
        for i in range(1, n-1):
            if stresses[i] > stresses[i-1] and stresses[i] > stresses[i+1] and stresses[i] > 0.01 * max_stress:
                local_max_indices.append(i)
        if not local_max_indices:
            return 0.0
        global_max_idx = int(np.argmax(stresses))
        if th == 1:
            if len(local_max_indices) < 2:
                return 0.0
            if global_max_idx <= local_max_indices[0]:
                return 0.0
        else:
            if global_max_idx != local_max_indices[0]:
                return 0.0
    return 1.0


# === block: score_4 (check id='consistency') ===
def score_4(artifact, step, ctx):
    stress_path = os.path.join('/app/outputs', 'stress_strain_data.csv')
    with open(stress_path, 'r') as f:
        reader = csv.DictReader(f)
        stress_rows = list(reader)
    groups = get_condition_groups(stress_rows)
    recomputed = {}
    for key, data in groups.items():
        E, UTS = compute_properties(data)
        if E is None:
            continue
        recomputed[key] = (E, UTS)
    for row in artifact:
        try:
            th = float(row['thickness_nm'])
            T = float(row['temperature_K'])
        except:
            continue
        key = (th, T)
        if key not in recomputed:
            continue
        agent_E = float(row['young_modulus_GPa'])
        agent_UTS = float(row['ultimate_tensile_strength_GPa'])
        ref_E, ref_UTS = recomputed[key]
        if ref_E != 0:
            if abs(agent_E - ref_E) / abs(ref_E) > 0.01:
                return 0.0
        else:
            if abs(agent_E) > 1e-6:
                return 0.0
        if ref_UTS != 0:
            if abs(agent_UTS - ref_UTS) / abs(ref_UTS) > 0.01:
                return 0.0
        else:
            if abs(agent_UTS) > 1e-6:
                return 0.0
    return 1.0


_SCORERS = {
    'raw_data': score_0,
    'thickness_trend': score_1,
    'temperature_trend': score_2,
    'shape_check': score_3,
    'consistency': score_4,
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
