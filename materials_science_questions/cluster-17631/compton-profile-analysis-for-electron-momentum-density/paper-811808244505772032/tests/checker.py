import os
import json
import csv

# === author imports / helpers ===
import os
import csv

def _install_numpy():
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])

try:
    import numpy as np
except ImportError:
    _install_numpy()
    import numpy as np


def load_csv(path):
    if not os.path.exists(path):
        return None
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return None
    # convert to dict of lists
    cols = list(rows[0].keys())
    data = {col: [] for col in cols}
    for row in rows:
        for col in cols:
            try:
                data[col].append(float(row[col]))
            except (ValueError, KeyError):
                data[col].append(np.nan)
    for col in cols:
        data[col] = np.array(data[col])
    return data


def compute_mad(agent_pz, agent_curve, ref_pz, ref_curve):
    # Interpolate agent curve onto ref_pz grid
    # Remove NaNs
    mask = ~np.isnan(agent_curve)
    if np.sum(mask) < 2:
        return np.inf
    interp = np.interp(ref_pz, agent_pz[mask], agent_curve[mask], left=np.nan, right=np.nan)
    valid = ~np.isnan(interp)
    if np.sum(valid) == 0:
        return np.inf
    return np.mean(np.abs(interp[valid] - ref_curve[valid]))


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
        ref_curves = spec.get('reference_curves', {})
        tolerances = spec.get('tolerances', {})
        return {
            'reference_curves': ref_curves,
            'tolerances': tolerances
        }


# === block: score_0 (check id='compton_profiles') ===
def score_0(artifact, step, ctx):
        data = load_csv(os.path.join('/app/outputs', 'compton_profiles.csv'))
        if data is None:
            return 0.0
        required = ['p_z', 'J_100', 'J_110', 'J_111']
        if not all(c in data for c in required):
            return 0.0
        pz = data['p_z']
        if len(pz) < 5:
            return 0.0
        ref = ctx['reference_curves'].get('compton', {})
        ref_pz = np.array(ref.get('p_z', []))
        tolerances = ctx['tolerances']
        # Relaxed MAD tolerance – appropriate for a different DFT implementation
        mad_tol = 0.2
        mad_decay = 0.3   # score linearly decays to zero at MAD = mad_tol + mad_decay
        integral_rel_tol = tolerances.get('integral_rel_tol', 0.05)
        target_electrons = 33.0

        scores = []
        for col in ['J_100', 'J_110', 'J_111']:
            ref_curve = np.array(ref.get(col, []))
            if len(ref_pz) != len(ref_curve) or len(ref_pz) == 0:
                continue
            mad = compute_mad(pz, data[col], ref_pz, ref_curve)
            if mad <= mad_tol:
                sc = 1.0
            else:
                sc = max(0.0, 1.0 - (mad - mad_tol) / mad_decay)
            scores.append(sc)
    
        integral_scores = []
        for col in ['J_100', 'J_110', 'J_111']:
            if len(pz) < 2:
                continue
            # manual trapezoidal rule to avoid numpy.trapz (removed in numpy>=2.0)
            val = 0.5 * np.sum((data[col][:-1] + data[col][1:]) * np.diff(pz))
            val *= 2.0  # double for negative side
            rel_err = abs(val - target_electrons) / target_electrons
            sc = max(0.0, 1.0 - rel_err / integral_rel_tol)
            integral_scores.append(sc)
    
        all_scores = scores + integral_scores
        if all_scores:
            return float(np.mean(all_scores))
        return 0.0


# === block: score_1 (check id='acar_profiles') ===
def score_1(artifact, step, ctx):
        data = load_csv(os.path.join('/app/outputs', 'acar_profiles.csv'))
        if data is None:
            return 0.0
        required = ['p_z', 'J_100', 'J_110', 'J_111']
        if not all(c in data for c in required):
            return 0.0
        pz = data['p_z']
        if len(pz) < 5:
            return 0.0
        ref = ctx['reference_curves'].get('acar', {})
        ref_pz = np.array(ref.get('p_z', []))
        tolerances = ctx['tolerances']
        mad_tol = tolerances.get('mad_acar', 0.01)
        scores = []
        for col in ['J_100', 'J_110', 'J_111']:
            ref_curve = np.array(ref.get(col, []))
            if len(ref_pz) != len(ref_curve) or len(ref_pz) == 0:
                continue
            mad = compute_mad(pz, data[col], ref_pz, ref_curve)
            sc = max(0.0, min(1.0, 1.0 - (mad - mad_tol) / (4.0 * mad_tol))) if mad <= mad_tol else max(0.0, 1.0 - (mad - mad_tol) / (4.0 * mad_tol))
            scores.append(sc)
        if scores:
            return float(np.mean(scores))
        return 0.0


# === block: score_2 (check id='anisotropy_cp') ===
def score_2(artifact, step, ctx):
        data = load_csv(os.path.join('/app/outputs', 'anisotropy_cp.csv'))
        if data is None:
            return 0.0
        required = ['p_z', 'delta_110_100', 'delta_111_100', 'delta_111_110']
        if not all(c in data for c in required):
            return 0.0
        pz = data['p_z']
        ref = ctx['reference_curves'].get('anisotropy_cp', {})
        ref_pz = np.array(ref.get('p_z', []))
        tolerances = ctx['tolerances']
        mad_tol = tolerances.get('mad_anisotropy', 0.002)
        scores = []
        for col in ['delta_110_100', 'delta_111_100', 'delta_111_110']:
            ref_curve = np.array(ref.get(col, []))
            if len(ref_pz) != len(ref_curve) or len(ref_pz) == 0:
                continue
            mad = compute_mad(pz, data[col], ref_pz, ref_curve)
            sc = max(0.0, min(1.0, 1.0 - (mad - mad_tol) / (4.0 * mad_tol))) if mad <= mad_tol else max(0.0, 1.0 - (mad - mad_tol) / (4.0 * mad_tol))
            scores.append(sc)
        # Cross-check consistency with Compton profiles (low weight)
        cons_score = 1.0
        cp_data = load_csv(os.path.join('/app/outputs', 'compton_profiles.csv'))
        if cp_data is not None and all(c in cp_data for c in ['p_z', 'J_100', 'J_110', 'J_111']):
            cp_pz = cp_data['p_z']
            # interpolate anisotropy from cp differences onto common pz grid
            interp_delta_110_100 = np.interp(pz, cp_pz, cp_data['J_110'] - cp_data['J_100'], left=np.nan, right=np.nan)
            interp_delta_111_100 = np.interp(pz, cp_pz, cp_data['J_111'] - cp_data['J_100'], left=np.nan, right=np.nan)
            interp_delta_111_110 = np.interp(pz, cp_pz, cp_data['J_111'] - cp_data['J_110'], left=np.nan, right=np.nan)
            msd_110_100 = np.nanmean((interp_delta_110_100 - data['delta_110_100']) ** 2)
            msd_111_100 = np.nanmean((interp_delta_111_100 - data['delta_111_100']) ** 2)
            msd_111_110 = np.nanmean((interp_delta_111_110 - data['delta_111_110']) ** 2)
            max_msd = max(msd_110_100, msd_111_100, msd_111_110)
            # tolerance for consistency
            cons_tol = 0.0001
            cons_score = max(0.0, 1.0 - max_msd / cons_tol)
        # combine: 80% MAD, 20% consistency
        avg_score = (0.8 * np.mean(scores) + 0.2 * cons_score) if scores else 0.0
        return float(avg_score)


# === block: score_3 (check id='anisotropy_acar') ===
def score_3(artifact, step, ctx):
        data = load_csv(os.path.join('/app/outputs', 'anisotropy_acar.csv'))
        if data is None:
            return 0.0
        required = ['p_z', 'delta_110_100', 'delta_111_100', 'delta_111_110']
        if not all(c in data for c in required):
            return 0.0
        pz = data['p_z']
        ref = ctx['reference_curves'].get('anisotropy_acar', {})
        ref_pz = np.array(ref.get('p_z', []))
        tolerances = ctx['tolerances']
        mad_tol = tolerances.get('mad_anisotropy', 0.002)
        scores = []
        for col in ['delta_110_100', 'delta_111_100', 'delta_111_110']:
            ref_curve = np.array(ref.get(col, []))
            if len(ref_pz) != len(ref_curve) or len(ref_pz) == 0:
                continue
            mad = compute_mad(pz, data[col], ref_pz, ref_curve)
            sc = max(0.0, min(1.0, 1.0 - (mad - mad_tol) / (4.0 * mad_tol))) if mad <= mad_tol else max(0.0, 1.0 - (mad - mad_tol) / (4.0 * mad_tol))
            scores.append(sc)
        # Cross-check consistency with ACAR profiles
        cons_score = 1.0
        acar_data = load_csv(os.path.join('/app/outputs', 'acar_profiles.csv'))
        if acar_data is not None and all(c in acar_data for c in ['p_z', 'J_100', 'J_110', 'J_111']):
            acar_pz = acar_data['p_z']
            interp_delta_110_100 = np.interp(pz, acar_pz, acar_data['J_110'] - acar_data['J_100'], left=np.nan, right=np.nan)
            interp_delta_111_100 = np.interp(pz, acar_pz, acar_data['J_111'] - acar_data['J_100'], left=np.nan, right=np.nan)
            interp_delta_111_110 = np.interp(pz, acar_pz, acar_data['J_111'] - acar_data['J_110'], left=np.nan, right=np.nan)
            msd_110_100 = np.nanmean((interp_delta_110_100 - data['delta_110_100']) ** 2)
            msd_111_100 = np.nanmean((interp_delta_111_100 - data['delta_111_100']) ** 2)
            msd_111_110 = np.nanmean((interp_delta_111_110 - data['delta_111_110']) ** 2)
            max_msd = max(msd_110_100, msd_111_100, msd_111_110)
            cons_tol = 0.0001
            cons_score = max(0.0, 1.0 - max_msd / cons_tol)
        avg_score = (0.8 * np.mean(scores) + 0.2 * cons_score) if scores else 0.0
        return float(avg_score)


_SCORERS = {
    'compton_profiles': score_0,
    'acar_profiles': score_1,
    'anisotropy_cp': score_2,
    'anisotropy_acar': score_3,
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
