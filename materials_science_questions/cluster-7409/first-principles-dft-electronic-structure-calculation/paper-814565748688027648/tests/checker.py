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
    gold = spec.get('gold', {})
    return {'gold': gold}


# === block: score_0 (check id='dft_result_verification') ===
def score_0(artifact, step, ctx):
    # artifact is the loaded JSON object (already validated shape).
    # ctx contains {'gold': gold_dict}
    import math

    artifact_json = artifact
    gold = ctx['gold']
    tolerances = gold['tolerances']
    tol_E = tolerances['E_ads']
    tol_d = tolerances['d_Ag_O']
    tol_phi = tolerances['Delta_phi']
    tol_mu = tolerances['mu']
    trend_eps = gold.get('trend_eps', 0.02)

    # Build coverage map
    cov_data = artifact_json.get('coverage_data', [])
    cov_map = {}
    for cd in cov_data:
        c = str(cd.get('coverage', '')).strip()
        cov_map[c] = cd

    # Helper: safe float from dict

    def safe_float(d, key, default=None):
        try:
            return float(d[key])
        except (KeyError, TypeError, ValueError):
            return default

    # E_ads scoring: directional (more negative is better). For each coverage,
    # if val <= ref: score=1; else score = max(0, 1 - (val-ref)/tol).
    score_eads = 0.0
    count_eads = 0
    for ml in ['1 ML','2 ML','4 ML']:
        cd = cov_map.get(ml)
        if not cd:
            continue
        val = safe_float(cd, 'E_ads_eV_per_atom')
        ref = gold[ml]['E_ads_eV_per_atom']
        if val is None:
            continue
        count_eads += 1
        if val <= ref:
            score_eads += 1.0
        else:
            score_eads += max(0.0, 1.0 - (val - ref) / tol_E)
    score_eads = score_eads / 3 if count_eads == 3 else 0.0

    # d_Ag-O: symmetric tolerance
    score_d = 0.0
    count_d = 0
    for ml in ['1 ML','2 ML','4 ML']:
        cd = cov_map.get(ml)
        if not cd:
            continue
        val = safe_float(cd, 'd_Ag_O_angstrom')
        ref = gold[ml]['d_Ag_O_angstrom']
        if val is None:
            continue
        count_d += 1
        if abs(val - ref) <= tol_d:
            score_d += 1.0
        else:
            score_d += 0.0
    score_d = score_d / 3 if count_d == 3 else 0.0

    # Delta_phi: symmetric
    score_phi = 0.0
    count_phi = 0
    for ml in ['1 ML','2 ML','4 ML']:
        cd = cov_map.get(ml)
        if not cd:
            continue
        val = safe_float(cd, 'Delta_phi_eV')
        ref = gold[ml]['Delta_phi_eV']
        if val is None:
            continue
        count_phi += 1
        if abs(val - ref) <= tol_phi:
            score_phi += 1.0
        else:
            score_phi += 0.0
    score_phi = score_phi / 3 if count_phi == 3 else 0.0

    # mu: symmetric
    score_mu = 0.0
    count_mu = 0
    for ml in ['1 ML','2 ML','4 ML']:
        cd = cov_map.get(ml)
        if not cd:
            continue
        val = safe_float(cd, 'mu_D')
        ref = gold[ml]['mu_D']
        if val is None:
            continue
        count_mu += 1
        if abs(val - ref) <= tol_mu:
            score_mu += 1.0
        else:
            score_mu += 0.0
    score_mu = score_mu / 3 if count_mu == 3 else 0.0

    # Bader charge: range [low, high]
    low_bader, high_bader = gold['bader_charge_range']
    bader = safe_float(artifact_json, 'bader_charge_Ag_e')
    score_bader = 1.0 if (bader is not None and low_bader <= bader <= high_bader) else 0.0

    # Trends check
    v1ml = cov_map.get('1 ML')
    v2ml = cov_map.get('2 ML')
    v4ml = cov_map.get('4 ML')
    def trend_ok():
        e1, e2, e4 = None, None, None
        d1, d2, d4 = None, None, None
        p1, p2, p4 = None, None, None
        m1, m2, m4 = None, None, None
        if v1ml and v2ml and v4ml:
            e1 = safe_float(v1ml, 'E_ads_eV_per_atom')
            e2 = safe_float(v2ml, 'E_ads_eV_per_atom')
            e4 = safe_float(v4ml, 'E_ads_eV_per_atom')
            d1 = safe_float(v1ml, 'd_Ag_O_angstrom')
            d2 = safe_float(v2ml, 'd_Ag_O_angstrom')
            d4 = safe_float(v4ml, 'd_Ag_O_angstrom')
            p1 = safe_float(v1ml, 'Delta_phi_eV')
            p2 = safe_float(v2ml, 'Delta_phi_eV')
            p4 = safe_float(v4ml, 'Delta_phi_eV')
            m1 = safe_float(v1ml, 'mu_D')
            m2 = safe_float(v2ml, 'mu_D')
            m4 = safe_float(v4ml, 'mu_D')
        if None in [e1,e2,e4,d1,d2,d4,p1,p2,p4,m1,m2,m4]:
            return 0.0
        score_t = 0.0
        # E_ads: 1ML > 2ML > 4ML (more negative = smaller numeric value)
        if (e1 >= e2 - trend_eps) and (e2 >= e4 - trend_eps):
            score_t += 1.0
        # d: increasing
        if (d1 <= d2 + trend_eps) and (d2 <= d4 + trend_eps):
            score_t += 1.0
        # phi: increasing
        if (p1 <= p2 + trend_eps) and (p2 <= p4 + trend_eps):
            score_t += 1.0
        # mu: decreasing and 4 ML ≈ 0
        if (m1 >= m2) and (m2 >= m4) and (abs(m4) <= 0.10):
            score_t += 1.0
        return score_t / 4.0

    score_trend = trend_ok()

    # Weights: eads 0.25, d 0.15, phi 0.15, mu 0.15, bader 0.1, trend 0.2
    final_score = (score_eads * 0.25 +
                   score_d * 0.15 +
                   score_phi * 0.15 +
                   score_mu * 0.15 +
                   score_bader * 0.1 +
                   score_trend * 0.2)
    return min(1.0, max(0.0, final_score))


_SCORERS = {
    'dft_result_verification': score_0,
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
