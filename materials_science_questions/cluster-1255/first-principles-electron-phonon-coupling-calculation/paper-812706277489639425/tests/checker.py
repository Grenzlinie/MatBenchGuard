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
    return {}


# === block: score_0 (check id='step_05_cumulant_spectral') ===
def score_0(artifact, step, ctx):
    data = artifact.get('300')  # check 300 K only
    if not data:
        return 0.0
    omegas = [d['omega'] for d in data]
    As = [d['A'] for d in data]
    if not omegas:
        return 0.0
    # locate QP peak (global maximum)
    max_idx = max(range(len(As)), key=lambda i: As[i])
    qp_omega = omegas[max_idx]
    qp_A = As[max_idx]
    tol_qp = step['check_params']['qp_peak_omega_tol']
    score_qp = 1.0 if abs(qp_omega) < tol_qp else 0.0

    # find local maxima as satellite candidates
    peaks = []
    for i in range(1, len(As)-1):
        if As[i] > As[i-1] and As[i] > As[i+1] and As[i] > 0.02 * qp_A and omegas[i] > qp_omega + 0.005:
            peaks.append((omegas[i], As[i]))
    peaks.sort(key=lambda x: x[0])
    sat1_expected = step['check_params']['satellite1_energy']
    sat2_expected = step['check_params']['satellite2_energy']
    sat1_tol = step['check_params']['satellite1_tol_rel'] * sat1_expected
    sat2_tol = step['check_params']['satellite2_tol_rel'] * sat2_expected
    score_sat1 = 0.0
    score_sat2 = 0.0
    if len(peaks) >= 1:
        e_sat1 = peaks[0][0] - qp_omega
        if abs(e_sat1 - sat1_expected) < sat1_tol:
            score_sat1 = 1.0
        # if first peak matches sat1 but we may also match sat2 if close; but we search for two distinct peaks
    if len(peaks) >= 2:
        e_sat1 = peaks[0][0] - qp_omega
        e_sat2 = peaks[1][0] - qp_omega
        # check assignment: if the first peak is close to sat1 and second to sat2
        if abs(e_sat1 - sat1_expected) < sat1_tol and abs(e_sat2 - sat2_expected) < sat2_tol:
            score_sat1 = 1.0
            score_sat2 = 1.0
        elif abs(e_sat1 - sat2_expected) < sat2_tol and abs(e_sat2 - sat1_expected) < sat1_tol:
            # swapped order acceptable
            score_sat1 = 1.0
            score_sat2 = 1.0
        else:
            # partial assignment
            if abs(e_sat1 - sat1_expected) < sat1_tol or abs(e_sat1 - sat2_expected) < sat2_tol:
                score_sat1 = 1.0
            if abs(e_sat2 - sat1_expected) < sat1_tol or abs(e_sat2 - sat2_expected) < sat2_tol:
                score_sat2 = 1.0
    # area normalization check
    area = 0.0
    for i in range(len(omegas)-1):
        area += (As[i]+As[i+1]) * (omegas[i+1]-omegas[i]) / 2.0
    area_tol = step['check_params']['area_tol']
    score_area = max(0.0, 1.0 - abs(area-1.0)/area_tol)
    return 0.3 * score_qp + 0.25 * score_sat1 + 0.25 * score_sat2 + 0.2 * score_area


# === block: score_1 (check id='step_06_mobility') ===
def score_1(artifact, step, ctx):
    temp_list = step['check_params']['temperature_list']
    gold_mob = step['check_params']['gold_mobility']
    tol_rel = step['check_params']['tolerance_rel']
    temp_map = {}
    for row in artifact:
        t = float(row.get('temperature_K'))
        m = float(row.get('mobility_cm2_Vs'))
        temp_map[t] = m
    scores = []
    for t, gold in zip(temp_list, gold_mob):
        m = temp_map.get(t)
        if m is None:
            scores.append(0.0)
        else:
            if abs(gold) > 0:
                rel_err = abs(m - gold) / abs(gold)
            else:
                rel_err = abs(m - gold) / 0.01 if gold==0 else 0.0
            if rel_err <= tol_rel:
                scores.append(1.0)
            else:
                score = max(0.0, 1.0 - (rel_err - tol_rel) / (2 * tol_rel))
                scores.append(score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='step_07_optical_conductivity') ===
def score_2(artifact, step, ctx):
    omegas = []
    sigmas = []
    for row in artifact:
        w = float(row['omega_eV'])
        s = float(row['sigma_norm'])
        omegas.append(w)
        sigmas.append(s)
    if not omegas:
        return 0.0
    # 1. max at zero
    score1 = 1.0 if abs(sigmas[0] - max(sigmas)) < 1e-6 else 0.0
    # 2. monotonic decay (allow 1% up)
    fails = 0
    for i in range(1, len(sigmas)):
        if sigmas[i] > sigmas[i-1]*1.01:
            fails += 1
    score2 = max(0.0, 1.0 - 0.1*fails)
    # 3. shoulder via convex region (positive second derivative)
    found_shoulder = False
    for i in range(1, len(sigmas)-1):
        d2 = sigmas[i-1] - 2*sigmas[i] + sigmas[i+1]
        if omegas[i] > 0.02 and omegas[i] < 0.12 and d2 > 1e-6:
            found_shoulder = True
            break
    score3 = 1.0 if found_shoulder else 0.0
    # 4. tail ratio: sigma near 0.15 eV < 0.3 * max
    target_omega = 0.15
    idx = min(range(len(omegas)), key=lambda i: abs(omegas[i]-target_omega))
    tail_val = sigmas[idx]
    score4 = 1.0 if tail_val < 0.3 * max(sigmas) else 0.0
    return 0.3*score1 + 0.2*score2 + 0.3*score3 + 0.2*score4


# === block: score_3 (check id='step_08_scattering_rate') ===
def score_3(artifact, step, ctx):
    val = float(artifact.strip().split()[0])
    thresh = step['check_params']['threshold_meV']
    return 1.0 if val > thresh else 0.0


# === block: score_4 (check id='step_09_incoherent_ratio') ===
def score_4(artifact, step, ctx):
    val = float(artifact.strip().split()[0])
    min_val = step['check_params']['min_val']
    max_val = step['check_params']['max_val']
    return 1.0 if min_val <= val <= max_val else 0.0


_SCORERS = {
    'step_05_cumulant_spectral': score_0,
    'step_06_mobility': score_1,
    'step_07_optical_conductivity': score_2,
    'step_08_scattering_rate': score_3,
    'step_09_incoherent_ratio': score_4,
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
