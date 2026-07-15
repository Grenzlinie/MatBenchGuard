import os
import json
import csv


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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    doped = artifact.get('doped')
    pristine = artifact.get('pristine')
    if not doped or not pristine:
        return 0.0
    doped_gap = doped.get('gap_eV')
    pristine_gap = pristine.get('gap_eV')
    if doped_gap is None or pristine_gap is None:
        return 0.0
    narrowing = pristine_gap - doped_gap
    threshold = 0.2
    if narrowing >= threshold:
        return 1.0
    elif narrowing > 0:
        return min(1.0, narrowing / threshold)
    else:
        return 0.0


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    doped = artifact.get('doped')
    pristine = artifact.get('pristine')
    if not doped or not pristine:
        return 0.0
    try:
        doped_wl = doped[0]['wavelength_nm']
        pristine_wl = pristine[0]['wavelength_nm']
    except (IndexError, KeyError, TypeError):
        return 0.0
    score_d = 1.0 if doped_wl > 1000 else 0.0
    score_p = 1.0 if 450 <= pristine_wl <= 600 else 0.0
    return (score_d + score_p) / 2.0


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    doped = artifact.get('doped', {})
    pristine = artifact.get('pristine', {})
    if not doped or not pristine:
        return 0.0
    def _unique(vals, tol=1.0):
        return len(set(round(v, 0) for v in vals))
    i_list = doped.get('127I', [])
    i_coord = [x['isotropic_shielding_ppm'] for x in i_list if x.get('coordinated_to_Mn')]
    i_non = [x['isotropic_shielding_ppm'] for x in i_list if not x.get('coordinated_to_Mn')]
    all_i = [x['isotropic_shielding_ppm'] for x in i_list]
    check_i_distinct = _unique(all_i, 1.0) >= 3
    if i_coord and i_non:
        diff = abs(sum(i_coord)/len(i_coord) - sum(i_non)/len(i_non))
        check_i_diff = diff > 5.0
    else:
        check_i_diff = False
    n_list = doped.get('14N', [])
    n_coord = [x['isotropic_shielding_ppm'] for x in n_list if x.get('coordinated_to_Mn')]
    check_n_distinct = _unique(n_coord, 0.1) >= 2 if n_coord else False
    c_doped = [x['isotropic_shielding_ppm'] for x in doped.get('13C', [])]
    c_pristine = [x['isotropic_shielding_ppm'] for x in pristine.get('13C', [])]
    if c_doped and c_pristine:
        avg_d = sum(c_doped)/len(c_doped)
        avg_p = sum(c_pristine)/len(c_pristine)
        check_C = (avg_d - avg_p) > 0.5
    else:
        check_C = False
    pb_doped = [x['isotropic_shielding_ppm'] for x in doped.get('207Pb', [])]
    check_Pb = (max(pb_doped) - min(pb_doped) < 5.0) if pb_doped else False
    return (check_i_distinct + check_i_diff + check_n_distinct + check_C + check_Pb) / 5.0


# === block: score_3 (check id='step_05') ===
def score_3(artifact, step, ctx):
    g_xx = artifact.get('g_xx')
    g_yy = artifact.get('g_yy')
    g_zz = artifact.get('g_zz')
    V_xx = artifact.get('V_xx')
    V_yy = artifact.get('V_yy')
    V_zz = artifact.get('V_zz')
    eta = artifact.get('eta')
    if None in [g_xx, g_yy, g_zz, V_xx, V_yy, V_zz, eta]:
        return 0.0
    check_g = (abs(g_xx - g_yy) > 1e-6) and (abs(g_yy - g_zz) > 1e-6) and (abs(g_xx - g_zz) > 1e-6)
    check_V = (V_zz > V_yy) and (V_yy > V_xx)
    check_eta = 0.2 <= eta <= 0.4
    return (check_g + check_V + check_eta) / 3.0


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
    'step_05': score_3,
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
