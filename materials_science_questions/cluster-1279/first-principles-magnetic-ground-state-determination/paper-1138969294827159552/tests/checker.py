import os
import json
import csv

# === author imports / helpers ===
import json

def get_nested(data, path, default=None):
    keys = path.split('.')
    val = data
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            return default
        if val is None:
            return default
    return val

def score_numeric(value, ref, tol, tol_type):
    if value is None or not isinstance(value, (int, float)):
        return 0.0
    if tol_type == 'abs':
        if abs(value - ref) <= tol:
            return 1.0
        else:
            return 0.0
    elif tol_type == 'rel':
        if ref == 0:
            if abs(value) <= tol:
                return 1.0
            else:
                return 0.0
        relative_error = abs(value - ref) / abs(ref)
        if relative_error <= tol:
            return 1.0
        else:
            return 0.0
    return 0.0

def score_numeric_group(artifact, config):
    fields = config['fields']
    refs = config['reference']
    tols = config['tolerance']
    types = config['tolerance_type']
    scores = []
    for i, f in enumerate(fields):
        val = get_nested(artifact, f)
        s = score_numeric(val, refs[i], tols[i], types[i])
        scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0

def score_numeric_group_array(artifact, config):
    fields = config['fields']
    refs = config['reference'] # list of lists
    tols = config['tolerance'] # per field
    types = config['tolerance_type'] # per field
    scores = []
    for i, f in enumerate(fields):
        arr = get_nested(artifact, f)
        ref_arr = refs[i]
        if not isinstance(arr, list) or len(arr) != len(ref_arr):
            scores.append(0.0)
            continue
        field_scores = []
        for j in range(len(arr)):
            s = score_numeric(arr[j], ref_arr[j], tols[i], types[i])
            field_scores.append(s)
        scores.append(sum(field_scores)/len(field_scores) if field_scores else 0.0)
    return sum(scores)/len(scores) if scores else 0.0


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape and content violations against grading_spec['output_contract']."""
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

        # === content integrity check: file must be non-empty and have reasonable size ===
        try:
            stat = _ff_os.stat(path)
            if stat.st_size < 50:
                violations.append(base + ": file is too small or empty (size < 50 bytes)")
                continue
        except Exception as exc:
            violations.append(base + ": cannot stat file (" + str(exc) + ")")
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
                    rows = list(_ff_csv.reader(_f, delimiter=delim))
                if len(rows) < 2:
                    violations.append(base + ": CSV/TSV file must have at least a header and one data row")
                    continue
                cols = set(rows[0] or [])
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
    """Zero the reward and exit if the submission violates the output_contract shape or content."""
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


# === block: score_0 (check id='check_gga_structural') ===
def score_0(artifact, step, ctx):
    return score_numeric_group(artifact, step['config'])


# === block: score_1 (check id='check_gga_ground_state') ===
def score_1(artifact, step, ctx):
    try:
        e_fm = get_nested(artifact, 'gga_fm_total_energy')
        e_nm = get_nested(artifact, 'gga_nm_total_energy')
        fm_confirmed = get_nested(artifact, 'fm_ground_state_confirmed')
        if None in (e_fm, e_nm, fm_confirmed):
            return 0.0
        if e_fm < e_nm and fm_confirmed == True:
            return 1.0
        else:
            return 0.0
    except Exception:
        return 0.0


# === block: score_2 (check id='check_gga_u_structural') ===
def score_2(artifact, step, ctx):
    return score_numeric_group_array(artifact, step['config'])


# === block: score_3 (check id='check_band_gaps') ===
def score_3(artifact, step, ctx):
    return score_numeric_group(artifact, step['config'])


# === block: score_4 (check id='check_elastic_constants') ===
def score_4(artifact, step, ctx):
    return score_numeric_group(artifact, step['config'])


# === block: score_5 (check id='check_elastic_derived') ===
def score_5(artifact, step, ctx):
    try:
        c11 = get_nested(artifact, 'elastic_constants_C11')
        c12 = get_nested(artifact, 'elastic_constants_C12')
        c44 = get_nested(artifact, 'elastic_constants_C44')
        if None in (c11, c12, c44):
            return 0.0
        # recompute B, G, B/G, poisson, Cauchy pressure
        B_expected = (c11 + 2*c12) / 3.0
        G_expected = (c11 - c12 + 3*c44) / 5.0
        BG_expected = B_expected / G_expected if G_expected != 0 else 0
        poisson_expected = (3*B_expected - 2*G_expected) / (2*(3*B_expected + G_expected)) if (3*B_expected + G_expected) != 0 else 0
        cauchy_expected = c12 - c44

        # compare with submitted values with small tolerances
        bulk_sub = get_nested(artifact, 'bulk_modulus_elastic')
        shear_sub = get_nested(artifact, 'shear_modulus')
        bg_sub = get_nested(artifact, 'B_G_ratio')
        poisson_sub = get_nested(artifact, 'poisson_ratio')
        cauchy_sub = get_nested(artifact, 'cauchy_pressure')
        debye_sub = get_nested(artifact, 'debye_temperature')

        sub_scores = []
        if bulk_sub is not None:
            sub_scores.append(score_numeric(bulk_sub, B_expected, 0.5, 'abs')) # 0.5 GPa tol
        else:
            sub_scores.append(0.0)
        if shear_sub is not None:
            sub_scores.append(score_numeric(shear_sub, G_expected, 0.5, 'abs'))
        else:
            sub_scores.append(0.0)
        if bg_sub is not None:
            sub_scores.append(score_numeric(bg_sub, BG_expected, 0.02, 'abs'))
        else:
            sub_scores.append(0.0)
        if poisson_sub is not None:
            sub_scores.append(score_numeric(poisson_sub, poisson_expected, 0.005, 'abs'))
        else:
            sub_scores.append(0.0)
        if cauchy_sub is not None:
            sub_scores.append(score_numeric(cauchy_sub, cauchy_expected, 1.0, 'abs'))
        else:
            sub_scores.append(0.0)
        # debye temperature compared against hidden gold (480.942 K) with 2 K tolerance
        if debye_sub is not None:
            sub_scores.append(score_numeric(debye_sub, 480.942, 2.0, 'abs'))
        else:
            sub_scores.append(0.0)
        return sum(sub_scores)/len(sub_scores) if sub_scores else 0.0
    except Exception:
        return 0.0


# === block: score_6 (check id='check_magnetic_moments') ===
def score_6(artifact, step, ctx):
    return score_numeric_group(artifact, step['config'])


# === block: score_7 (check id='check_ductility') ===
def score_7(artifact, step, ctx):
    try:
        bg = get_nested(artifact, 'B_G_ratio')
        poisson = get_nested(artifact, 'poisson_ratio')
        is_ductile = get_nested(artifact, 'is_ductile')
        if None in (bg, poisson, is_ductile):
            return 0.0
        expected_ductile = (bg is not None and bg > 1.75) and (poisson is not None and poisson > 0.26)
        if expected_ductile == is_ductile:
            return 1.0
        else:
            return 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'check_gga_structural': score_0,
    'check_gga_ground_state': score_1,
    'check_gga_u_structural': score_2,
    'check_band_gaps': score_3,
    'check_elastic_constants': score_4,
    'check_elastic_derived': score_5,
    'check_magnetic_moments': score_6,
    'check_ductility': score_7,
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