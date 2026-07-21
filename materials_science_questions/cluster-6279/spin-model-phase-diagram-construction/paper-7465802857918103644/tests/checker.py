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
    gold = spec['steps'][0].get('gold', {})
    return {'gold': gold}


# === block: score_0 (check id='score_results_json') ===
def score_0(artifact, step, ctx):
    import json, os
    from math import fabs

    def _safe_float(d, key):
        val = d.get(key)
        if isinstance(val, (int, float)) and not (isinstance(val, bool)):
            return float(val), True
        return None, False

    def _safe_bool(d, key):
        val = d.get(key)
        if isinstance(val, bool):
            return val, True
        return None, False

    artifact = json.loads(json.dumps(artifact))  # ensure dict
    gold = ctx['gold']

    weights = {
        'J2_0_Tc': 0.20,
        'J2_0_latent': 0.10,
        'J2_0_mAF2': 0.10,
        'sqrt3_Tc': 0.075,
        'sqrt3_latent': 0.075,
        'q0_Tc': 0.075,
        'q0_latent': 0.075,
        'triple_J2': 0.075,
        'triple_Tc': 0.075,
        'cv_sqrt3': 0.05,
        'pyro_order': 0.05,
        'pyro_diff': 0.05,
        'pyro_lowest_tol': 0.0  # just for existence check, negligible weight is folded into others
    }
    # pyro_lowest_T just a sanity, weighted zero

    score = 0.0

    # J2_0 block
    j2_0 = artifact.get('J2_0', {})
    gold_j2_0 = gold.get('J2_0', {})
    tc_val, ok0 = _safe_float(j2_0, 'Tc')
    if ok0:
        ref = gold_j2_0['Tc']
        if ref > 0:
            rel_err = fabs(tc_val - ref) / ref
            if rel_err <= 0.10:
                score += weights['J2_0_Tc']
            else:
                pass
        else:
            # fallback to absolute
            if fabs(tc_val - ref) < 0.01:
                score += weights['J2_0_Tc']
    lh_val, ok1 = _safe_float(j2_0, 'latent_heat')
    if ok1:
        ref = gold_j2_0['latent_heat']
        if ref > 0:
            rel_err = fabs(lh_val - ref) / ref
            if rel_err <= 0.10:
                score += weights['J2_0_latent']
            else:
                pass
        else:
            if fabs(lh_val) < 1e-6:
                score += weights['J2_0_latent']
    maf, ok2 = _safe_float(j2_0, 'mAF2_lowest_T')
    if ok2 and maf is not None:
        ref = gold_j2_0['mAF2_lowest_T']
        if fabs(maf - ref) <= 0.001:
            score += weights['J2_0_mAF2']

    # J2_critical_sqrt3
    d = artifact.get('J2_critical_sqrt3', {})
    gd = gold.get('J2_critical_sqrt3', {})
    tc_val, ok0 = _safe_float(d, 'Tc')
    if ok0:
        ref = gd['Tc']
        if ref > 0:
            if fabs(tc_val - ref) / ref <= 0.10:
                score += weights['sqrt3_Tc']
        else:
            if fabs(tc_val) < 1e-6:
                score += weights['sqrt3_Tc']
    lh_val, ok1 = _safe_float(d, 'latent_heat')
    if ok1:
        ref = gd['latent_heat']
        if ref > 0:
            if fabs(lh_val - ref) / ref <= 0.10:
                score += weights['sqrt3_latent']
        else:
            if fabs(lh_val) < 1e-6:
                score += weights['sqrt3_latent']

    # J2_critical_q0
    d = artifact.get('J2_critical_q0', {})
    gd = gold.get('J2_critical_q0', {})
    tc_val, ok0 = _safe_float(d, 'Tc')
    if ok0:
        ref = gd['Tc']
        if fabs(tc_val - ref) / ref <= 0.10:
            score += weights['q0_Tc']
    lh_val, ok1 = _safe_float(d, 'latent_heat')
    if ok1:
        ref = gd['latent_heat']
        if ref > 0:
            if fabs(lh_val - ref) / ref <= 0.10:
                score += weights['q0_latent']
        else:
            if fabs(lh_val) < 1e-6:
                score += weights['q0_latent']

    # triple_point
    d = artifact.get('triple_point', {})
    gd = gold.get('triple_point', {})
    tc_val, ok0 = _safe_float(d, 'Tc')
    if ok0:
        ref = gd['Tc']
        if ref > 0:
            if fabs(tc_val - ref) / ref <= 0.10:
                score += weights['triple_Tc']
    j2_val, ok1 = _safe_float(d, 'J2')
    if ok1:
        ref = gd['J2']
        scaled_ref = ref if ref != 0 else 1e-8
        if scaled_ref == 0:
            if fabs(j2_val) < 1e-8:
                score += weights['triple_J2']
        else:
            if fabs(j2_val - ref) / abs(scaled_ref) <= 0.10:
                score += weights['triple_J2']

    # cv_sqrt3_T0
    cv_val, ok = _safe_float(artifact, 'cv_sqrt3_T0')
    if ok:
        ref = gold['cv_sqrt3_T0']
        if fabs(cv_val - ref) <= 0.01:
            score += weights['cv_sqrt3']

    # pyrochlore
    d = artifact.get('pyrochlore', {})
    gd = gold.get('pyrochlore', {})
    ordered, ok = _safe_bool(d, 'ordered_state_found')
    if ok and ordered == gd['ordered_state_found']:
        score += weights['pyro_order']
    fd_val, ok = _safe_float(d, 'free_energy_diff')
    if ok:
        if fd_val > 0 and fabs(fd_val - gd['free_energy_diff']) < 1.0:
            score += weights['pyro_diff']
    # lowest_T existence check (negligible weight already integrated)

    return min(score, 1.0)


_SCORERS = {
    'score_results_json': score_0,
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
