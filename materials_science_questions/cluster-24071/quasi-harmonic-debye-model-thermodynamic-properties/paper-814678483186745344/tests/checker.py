import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='step_phase_transition') ===
def score_0(artifact, step, ctx):
    artifact_dict = artifact if isinstance(artifact, dict) else json.loads(artifact)
    nb = artifact_dict.get('NbO_enthalpy')
    nias = artifact_dict.get('NiAs_enthalpy')
    if not nb or not nias or len(nb) < 2 or len(nias) < 2:
        return 0.0
    nb_sorted = sorted(nb, key=lambda x: x['P'])
    nias_sorted = sorted(nias, key=lambda x: x['P'])

    def interp(arr, P):
        if P <= arr[0]['P']:
            return arr[0]['H']
        if P >= arr[-1]['P']:
            return arr[-1]['H']
        for i in range(len(arr)-1):
            if arr[i]['P'] <= P <= arr[i+1]['P']:
                frac = (P - arr[i]['P']) / (arr[i+1]['P'] - arr[i]['P'])
                return arr[i]['H'] + frac * (arr[i+1]['H'] - arr[i]['H'])
        return arr[-1]['H']

    def diff(P):
        return interp(nb_sorted, P) - interp(nias_sorted, P)

    P_left = max(nb_sorted[0]['P'], nias_sorted[0]['P'])
    P_right = min(nb_sorted[-1]['P'], nias_sorted[-1]['P'])
    if P_left >= P_right:
        return 0.0

    d_left = diff(P_left)
    d_right = diff(P_right)
    if d_left * d_right >= 0:
        # no sign change, try to find minimum absolute difference
        best_p = P_left
        best_d = abs(d_left)
        for _ in range(200):
            p = P_left + (P_right - P_left) * _ / 200.0
            d = abs(diff(p))
            if d < best_d:
                best_d = d
                best_p = p
        pt = best_p
    else:
        for _ in range(50):
            P_mid = (P_left + P_right) / 2.0
            d_mid = diff(P_mid)
            if abs(d_mid) < 1e-8:
                break
            if d_left * d_mid <= 0:
                P_right = P_mid
                d_right = d_mid
            else:
                P_left = P_mid
                d_left = d_mid
        pt = (P_left + P_right) / 2.0

    gold = step.get('target', 52.8)
    tol = step.get('tolerance_abs', 5.0)
    dist = abs(pt - gold)
    if dist <= tol:
        score = 1.0
    else:
        decay = dist - tol
        score = max(0.0, 1.0 - decay / tol)
    return score


# === block: score_1 (check id='step_elastic') ===
def score_1(artifact, step, ctx):
    gold = step.get('target', {})
    tolerances = step.get('tolerances', {})
    elastic_tol = tolerances.get('elastic_moduli', 0.15)
    hardness_tol = tolerances.get('hardness', 0.20)
    poissons_tol = tolerances.get('poissons', 0.15)

    def field_score(val, ref, tol):
        denom = abs(ref) if abs(ref) > 1e-6 else 1.0
        err = abs(val - ref) / denom
        return max(0.0, 1.0 - err / tol)

    nbo = artifact.get('NbO', {})
    nias = artifact.get('NiAs', {})

    nb_fields = ['C11','C12','C44','bulk_modulus','shear_modulus','youngs_modulus','poissons_ratio','Vickers_hardness']
    ni_fields = ['C11','C33','C44','C12','C13','bulk_modulus','shear_modulus','youngs_modulus','poissons_ratio','Vickers_hardness']

    scores = []
    for f in nb_fields:
        if f not in nbo or f not in gold.get('NbO',{}):
            continue
        tol = hardness_tol if f == 'Vickers_hardness' else (poissons_tol if f == 'poissons_ratio' else elastic_tol)
        s = field_score(nbo[f], gold['NbO'][f], tol)
        scores.append(s)
    for f in ni_fields:
        if f not in nias or f not in gold.get('NiAs',{}):
            continue
        tol = hardness_tol if f == 'Vickers_hardness' else (poissons_tol if f == 'poissons_ratio' else elastic_tol)
        s = field_score(nias[f], gold['NiAs'][f], tol)
        scores.append(s)

    if not scores:
        avg = 0.0
    else:
        avg = sum(scores) / len(scores)

    if step.get('stability_check', False):
        c11 = nias.get('C11')
        c12 = nias.get('C12')
        c13 = nias.get('C13')
        c33 = nias.get('C33')
        c44 = nias.get('C44')
        if None in (c11,c12,c13,c33,c44):
            stable = False
        else:
            cond1 = c44 > 0
            cond2 = c11 > abs(c12)
            cond3 = (c11 + 2*c12) * c33 > 2 * c13**2
            stable = cond1 and cond2 and cond3
        if not stable:
            avg *= 0.2
    return min(1.0, avg)


# === block: score_2 (check id='step_thermo') ===
def score_2(artifact, step, ctx):
    gold = step.get('target', {})
    theta_gold = gold.get('Debye_temperature_K', 525)
    tol_theta = step.get('tolerances', {}).get('Debye_relative', 0.10)
    theta = artifact.get('Debye_temperature_NbO_K')
    if theta is None:
        s_debye = 0.0
    else:
        err = abs(theta - theta_gold) / theta_gold
        s_debye = max(0.0, 1.0 - err / tol_theta)

    Cv0 = artifact.get('heat_capacity_0GPa', [])
    Cv50 = artifact.get('heat_capacity_50GPa', [])
    dulong = gold.get('dulong_petit', 49.9)
    tol_cv = step.get('tolerances', {}).get('Cv_relative', 0.10)

    def high_t_values(arr):
        vals = [pt['Cv'] for pt in arr if pt.get('T',0) >= 1200]
        return vals

    def average_high(arr):
        vals = high_t_values(arr)
        if not vals:
            return None
        return sum(vals) / len(vals)

    avg_cv0 = average_high(Cv0)
    avg_cv50 = average_high(Cv50)

    def score_cv_avg(avg, target, tol):
        if avg is None:
            return 0.0
        err = abs(avg - target) / target
        return max(0.0, 1.0 - err / tol)

    s_cv = 0.0
    if avg_cv0 is not None and avg_cv50 is not None:
        s0 = score_cv_avg(avg_cv0, dulong, tol_cv)
        s50 = score_cv_avg(avg_cv50, dulong, tol_cv)
        s_cv = (s0 + s50) / 2.0
        if avg_cv50 >= avg_cv0:
            s_cv *= 0.5

    alpha0 = artifact.get('thermal_expansion_0GPa', [])
    alpha50 = artifact.get('thermal_expansion_50GPa', [])

    def alpha_metrics(arr):
        if not arr:
            return None
        low_vals = [pt['alpha'] for pt in arr if 50 <= pt.get('T',0) <= 200]
        high_vals = [pt['alpha'] for pt in arr if pt.get('T',0) >= 1000]
        low = sum(low_vals)/len(low_vals) if low_vals else None
        high = sum(high_vals)/len(high_vals) if high_vals else None
        return low, high

    low0, high0 = alpha_metrics(alpha0) if alpha_metrics(alpha0) else (None, None)
    low50, high50 = alpha_metrics(alpha50) if alpha_metrics(alpha50) else (None, None)

    mono0 = 1.0 if (low0 is not None and high0 is not None and high0 > low0) else 0.0
    mono50 = 1.0 if (low50 is not None and high50 is not None and high50 > low50) else 0.0
    pressure_order = 1.0 if (high0 is not None and high50 is not None and high0 > high50) else 0.0
    score_alpha = 0.4 * mono0 + 0.4 * mono50 + 0.2 * pressure_order
    score_alpha = min(1.0, score_alpha)

    s_thermo = 0.3 * s_debye + 0.4 * s_cv + 0.3 * score_alpha
    return s_thermo


_SCORERS = {
    'step_phase_transition': score_0,
    'step_elastic': score_1,
    'step_thermo': score_2,
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
