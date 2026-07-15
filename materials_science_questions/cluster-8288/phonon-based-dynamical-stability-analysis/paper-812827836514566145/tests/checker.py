import os
import json
import csv

# === author imports / helpers ===
import math


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
    return {
      'k_B': 8.617333262145e-5,
      'T': 300.0,
      'nu0': 1e13,
      'cm2_to_A2': 1e16
    }


# === block: score_0 (check id='check_transition_pressure') ===
def score_0(artifact, step, ctx):
    enthalpy = artifact.get('enthalpy_data', [])
    if not enthalpy:
        return 0.0
    try:
        points = sorted([(p['P'], p['H_P21c'] - p['H_P42m']) for p in enthalpy], key=lambda x: x[0])
        cross_P = None
        for i in range(len(points)-1):
            p1, d1 = points[i]
            p2, d2 = points[i+1]
            if d1 * d2 <= 0:
                cross_P = p1 - d1 * (p2 - p1) / (d2 - d1)
                break
        if cross_P is None:
            return 0.0
        target = step.get('target', 2.78)
        tol = step.get('tolerance_abs', 0.5)
        err = abs(cross_P - target)
        if err <= tol:
            return 1.0
        elif err <= 2*tol:
            return 0.5
        else:
            return 0.0
    except Exception:
        return 0.0


# === block: score_1 (check id='check_phonon_stability') ===
def score_1(artifact, step, ctx):
    phonon_data = artifact.get('phonon_band_data', [])
    if not phonon_data:
        return 0.0
    min_freq = float('inf')
    for entry in phonon_data:
        freqs = entry.get('frequency_cm1', [])
        if freqs:
            for f in freqs:
                if f < min_freq:
                    min_freq = f
    stable_flag = artifact.get('phonon_stable', False)
    if min_freq >= -1.0 and stable_flag:
        return 1.0
    elif min_freq >= -1.0 and not stable_flag:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='check_pbe_bandgap') ===
def score_2(artifact, step, ctx):
    val = artifact.get('pbe_bandgap_eV')
    if val is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_abs']
    err = abs(val - target)
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 0.5
    else:
        return 0.0


# === block: score_3 (check id='check_hse06_bandgap') ===
def score_3(artifact, step, ctx):
    val = artifact.get('hse06_bandgap_eV')
    if val is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_abs']
    err = abs(val - target)
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 0.5
    else:
        return 0.0


# === block: score_4 (check id='check_discharge_voltage') ===
def score_4(artifact, step, ctx):
    energies = artifact.get('raw_energies', {})
    if not energies or 'E_Li2S2_eV' not in energies or 'E_Li_eV' not in energies or 'E_Li2S_eV' not in energies:
        return 0.0
    try:
        E_Li2S2 = float(energies['E_Li2S2_eV'])
        E_Li = float(energies['E_Li_eV'])
        E_Li2S = float(energies['E_Li2S_eV'])
        V_computed = (E_Li2S2 + E_Li - 2 * E_Li2S) / 2.0
    except Exception:
        return 0.0
    target = step.get('target_voltage', 2.34)
    tol = step.get('tolerance_abs', 0.2)
    err = abs(V_computed - target)
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 0.5
    else:
        return 0.0


# === block: score_5 (check id='check_diffusion_paths') ===
def score_5(artifact, step, ctx):
    paths = artifact.get('diffusion_paths', [])
    if not paths:
        return 0.0
    targets = step.get('targets', {})
    D_tol_factor = step.get('D_tolerance_factor', 5.0)
    k_B = ctx['k_B']
    T = ctx['T']
    nu0 = ctx['nu0']
    cm2_to_A2 = ctx['cm2_to_A2']
    score_sum = 0.0
    count = 0
    for path in paths:
        pid = path.get('path_id')
        if pid not in targets:
            continue
        target = targets[pid]
        barrier = path.get('barrier_eV')
        D_rep = path.get('D_cm2_per_s')
        d = path.get('hopping_distance_A')
        if barrier is None or D_rep is None or d is None:
            continue
        tar_barrier = target['barrier_eV']
        if tar_barrier > 0.2:
            tol_bar = 0.2
        elif tar_barrier > 0.05:
            tol_bar = 0.1
        else:
            tol_bar = 0.05
        err_bar = abs(barrier - tar_barrier)
        if err_bar <= tol_bar:
            score_bar = 1.0
        else:
            score_bar = max(0.0, 1.0 - (err_bar - tol_bar) / tol_bar)
        tar_D = target['D_cm2_per_s']
        if D_rep > 0 and tar_D > 0:
            log_ratio = math.log10(D_rep / tar_D)
        else:
            log_ratio = 1.0 if D_rep != tar_D else 0.0
        max_log = math.log10(D_tol_factor)
        if abs(log_ratio) <= max_log:
            score_D = 1.0
        else:
            score_D = max(0.0, 1.0 - (abs(log_ratio) - max_log) / max_log)
        try:
            D_pred = (d ** 2) * nu0 * math.exp(-barrier / (k_B * T)) / cm2_to_A2
            rel_err = abs(D_pred - D_rep) / abs(D_rep) if D_rep != 0 else 1.0
            score_cons = 1.0 if rel_err < 0.2 else max(0.0, 1.0 - (rel_err - 0.2) / 0.8)
        except Exception:
            score_cons = 0.0
        path_score = 0.4 * score_bar + 0.4 * score_D + 0.2 * score_cons
        score_sum += path_score
        count += 1
    if count == 0:
        return 0.0
    return score_sum / count


_SCORERS = {
    'check_transition_pressure': score_0,
    'check_phonon_stability': score_1,
    'check_pbe_bandgap': score_2,
    'check_hse06_bandgap': score_3,
    'check_discharge_voltage': score_4,
    'check_diffusion_paths': score_5,
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
