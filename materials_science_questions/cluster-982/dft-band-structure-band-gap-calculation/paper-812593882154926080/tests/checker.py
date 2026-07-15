import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    c = artifact
    if not isinstance(c, dict) or not all(k in c for k in ('c11','c12','c44')):
        return 0.0
    c11, c12, c44 = c['c11'], c['c12'], c['c44']
    ref = step.get('reference', {})
    ref11 = ref.get('c11', 1715.3)
    ref12 = ref.get('c12', -283.5)
    ref44 = ref.get('c44', 1187.5)
    tol11 = step.get('tolerance_c11_pct', 15.0)/100.0
    tol12 = step.get('tolerance_c12_pct', 25.0)/100.0
    tol44 = step.get('tolerance_c44_pct', 15.0)/100.0

    def field_score(val, ref_val, tol):
        if abs(ref_val) < 1e-6:
            return 1.0 if abs(val) < 1e-6 else 0.0
        err = abs(val - ref_val)
        max_allowed = tol * abs(ref_val)
        if max_allowed <= 0:
            return 1.0
        return max(0.0, 1.0 - err / max_allowed)

    s11 = field_score(c11, ref11, tol11)
    s12 = field_score(c12, ref12, tol12)
    s44 = field_score(c44, ref44, tol44)
    avg = (s11 + s12 + s44) / 3.0

    born = (c11 - c12 > 0) and (c11 + 2*c12 > 0) and (c44 > 0)
    if not born:
        avg *= 0.4
    return max(0.0, min(1.0, avg))


# === block: score_1 (check id='mechanical_properties') ===
def score_1(artifact, step, ctx):
    path = os.path.join('/app/outputs', 'step_01_elastic_constants.json')
    if not os.path.exists(path):
        return 0.0
    try:
        with open(path) as f:
            elastic = json.load(f)
        c11 = float(elastic.get('c11'))
        c12 = float(elastic.get('c12'))
        c44 = float(elastic.get('c44'))
    except Exception:
        return 0.0

    B = (c11 + 2*c12) / 3.0
    G_V = (c11 - c12 + 3*c44) / 5.0
    denom = 3*B + G_V
    if denom == 0:
        return 0.0
    E_iso = (9 * B * G_V) / denom
    nu = (3*B - 2*G_V) / (2*denom)

    ref = step.get('reference', {})
    tol = step.get('tolerances', {})
    ref_B = ref.get('bulk_modulus', 381.0)
    ref_E = ref.get('youngs_modulus', 1691.0)
    ref_G = ref.get('shear_modulus', 1113.0)
    ref_nu = ref.get('poisson_ratio', -0.241)
    tol_B = tol.get('bulk_modulus_pct', 10.0)/100.0
    tol_E = tol.get('youngs_modulus_pct', 10.0)/100.0
    tol_G = tol.get('shear_modulus_pct', 10.0)/100.0
    tol_nu = tol.get('poisson_ratio_abs', 0.06)

    def prop_score(val, ref_val, tol_frac):
        err = abs(val - ref_val)
        max_allowed = tol_frac * abs(ref_val) if ref_val != 0 else 1.0
        if max_allowed <= 0:
            return 1.0 if err < 1e-6 else 0.0
        return max(0.0, 1.0 - err / max_allowed)

    sB = prop_score(B, ref_B, tol_B)
    sE = prop_score(E_iso, ref_E, tol_E)
    sG = prop_score(G_V, ref_G, tol_G)
    # Poisson ratio scored with absolute tolerance
    sNu = max(0.0, 1.0 - abs(nu - ref_nu) / tol_nu) if tol_nu > 0 else (1.0 if abs(nu - ref_nu) < 1e-6 else 0.0)
    score = (sB + sE + sG + sNu) / 4.0
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='band_gap') ===
def score_2(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    ref = step.get('reference', {})
    ref_gap = ref.get('band_gap', 2.52)
    ref_vbm = ref.get('vbm_kpoint', 'L').strip().upper()
    ref_cbm = ref.get('cbm_kpoint', 'X').strip().upper()
    vbm = str(art.get('vbm_kpoint', '')).strip().upper()
    cbm = str(art.get('cbm_kpoint', '')).strip().upper()
    gap = art.get('band_gap')
    if gap is None or not isinstance(gap, (int, float)):
        return 0.0
    tol_ev = step.get('tolerance_gap_ev', 0.5)
    gap_score = max(0.0, 1.0 - abs(gap - ref_gap) / tol_ev)
    k_score = 1.0 if vbm == ref_vbm and cbm == ref_cbm else 0.0
    score = 0.5 * gap_score + 0.5 * k_score
    return max(0.0, min(1.0, score))


_SCORERS = {
    'elastic_constants': score_0,
    'mechanical_properties': score_1,
    'band_gap': score_2,
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
