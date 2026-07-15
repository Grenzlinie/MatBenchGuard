import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='moduli') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    young = artifact.get('young_modulus_GPa')
    shear = artifact.get('shear_modulus_GPa')
    if young is None or shear is None:
        return 0.0
    params = step.get('params', {})
    young_gold = params.get('young_gold', 16.52)
    shear_gold = params.get('shear_gold', 3.94)
    tol_rel = params.get('tolerance_rel', 0.3)
    score_struct = 0.3 if shear < young else 0.0
    if young_gold > 0:
        young_ok = abs(young - young_gold) / young_gold <= tol_rel
    else:
        young_ok = abs(young - young_gold) <= tol_rel
    if shear_gold > 0:
        shear_ok = abs(shear - shear_gold) / shear_gold <= tol_rel
    else:
        shear_ok = abs(shear - shear_gold) <= tol_rel
    score_magn = 0.35 * young_ok + 0.35 * shear_ok
    total = score_struct + score_magn
    return min(max(total, 0.0), 1.0)


# === block: score_1 (check id='diffusion') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) < 12:
        return 0.0
    params = step.get('params', {})
    shear_dev = params.get('shear_deviation_tol', 0.5)
    def get_D(guest, stype, svalue):
        for r in rows:
            try:
                g = str(r.get('guest','')).strip()
                st = str(r.get('strain_type','')).strip().lower()
                sv = float(r.get('strain_value',0))
                dv = float(r.get('diffusion_coefficient_m2_per_s',0))
                if g == guest and st == stype and abs(sv - svalue) < 0.01:
                    return dv
            except (ValueError, TypeError):
                continue
        return None
    conditions_met = 0
    d_h2_t0 = get_D('H2', 'tensile', 0.0)
    d_h2_t7 = get_D('H2', 'tensile', 7.0)
    d_h2_t10 = get_D('H2', 'tensile', 10.0)
    if d_h2_t0 is not None and d_h2_t7 is not None and d_h2_t10 is not None:
        if d_h2_t0 < d_h2_t7 < d_h2_t10:
            conditions_met += 1
    d_co2_t0 = get_D('CO2', 'tensile', 0.0)
    d_co2_t7 = get_D('CO2', 'tensile', 7.0)
    d_co2_t10 = get_D('CO2', 'tensile', 10.0)
    if d_co2_t0 is not None and d_co2_t7 is not None and d_co2_t10 is not None:
        if d_co2_t0 < d_co2_t7 < d_co2_t10:
            conditions_met += 1
    d_h2_s0 = get_D('H2', 'shear', 0.0)
    d_h2_s7 = get_D('H2', 'shear', 7.0)
    d_h2_s10 = get_D('H2', 'shear', 10.0)
    if d_h2_s0 is not None and d_h2_s7 is not None and d_h2_s10 is not None:
        d_val = d_h2_s0
        if d_val <= 0:
            d_val = 1e-20
        if (0.5*d_val <= d_h2_s7 <= 1.5*d_val) and (0.5*d_val <= d_h2_s10 <= 1.5*d_val):
            conditions_met += 1
    d_co2_s0 = get_D('CO2', 'shear', 0.0)
    d_co2_s7 = get_D('CO2', 'shear', 7.0)
    d_co2_s10 = get_D('CO2', 'shear', 10.0)
    if d_co2_s0 is not None and d_co2_s7 is not None and d_co2_s10 is not None:
        d_val = d_co2_s0
        if d_val <= 0:
            d_val = 1e-20
        if (0.5*d_val <= d_co2_s7 <= 1.5*d_val) and (0.5*d_val <= d_co2_s10 <= 1.5*d_val):
            conditions_met += 1
    score = conditions_met / 4.0
    return score


# === block: score_2 (check id='c2c2') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) < 6:
        return 0.0
    params = step.get('params', {})
    tol_abs = params.get('tolerance_abs', 0.2)
    tensile_gold = params.get('tensile_gold', [5.15, 5.40, 5.54])
    shear_gold = params.get('shear_gold', [5.15, 5.20, 5.24])
    entries = {}
    for r in rows:
        try:
            st = str(r.get('strain_type','')).strip().lower()
            sv = float(r.get('strain_value',0))
            av = float(r.get('avg_c2c2_length_angstrom',0))
            entries[(st, sv)] = av
        except:
            continue
    correct_count = 0
    for sv, gold in zip([0,7,10], tensile_gold):
        key = ('tensile', sv)
        if key in entries:
            if abs(entries[key] - gold) <= tol_abs:
                correct_count += 1
    for sv, gold in zip([0,7,10], shear_gold):
        key = ('shear', sv)
        if key in entries:
            if abs(entries[key] - gold) <= tol_abs:
                correct_count += 1
    tol_score = correct_count / 6.0 if 6 > 0 else 0.0
    monotonic_ok = 0.0
    t0 = entries.get(('tensile',0))
    t7 = entries.get(('tensile',7))
    t10 = entries.get(('tensile',10))
    if t0 is not None and t7 is not None and t10 is not None:
        if t0 < t7 < t10:
            monotonic_ok = 1.0
    total = 0.9 * tol_score + 0.1 * monotonic_ok
    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'moduli': score_0,
    'diffusion': score_1,
    'c2c2': score_2,
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
