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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    ref = step.get('reference', {})
    dist_ref = ref.get('distances', {})
    tol = ref.get('tolerance', 0.05)
    rows_by_id = {row['compound_id']: row for row in artifact}
    def get_val(cid):
        r = rows_by_id.get(cid)
        if r is None:
            return None
        try:
            return float(r['o_H_O_distance_A'])
        except (ValueError, TypeError):
            return None

    v_no2 = get_val('pNHDPU')
    v_cn = get_val('pCyHDPU')
    v_cl = get_val('pClHDPU')
    if v_no2 is None or v_cn is None or v_cl is None:
        return 0.0

    # trend: NO2 < CN < Cl
    trend_ok = (v_no2 < v_cn) and (v_cn < v_cl)
    trend_score = 1.0 if trend_ok else 0.0

    abs_count = 0
    if abs(v_no2 - dist_ref.get('pNHDPU', v_no2)) <= tol:
        abs_count += 1
    if abs(v_cn - dist_ref.get('pCyHDPU', v_cn)) <= tol:
        abs_count += 1
    if abs(v_cl - dist_ref.get('pClHDPU', v_cl)) <= tol:
        abs_count += 1
    abs_score = abs_count / 3.0

    return 0.7 * trend_score + 0.3 * abs_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    ref = step.get('reference', {})
    eng_ref = ref.get('energies', {})
    tol = ref.get('tolerance', 5.0)
    rows_by_id = {row['compound_id']: row for row in artifact}
    def get_val(cid):
        r = rows_by_id.get(cid)
        if r is None:
            return None
        try:
            return float(r['E_lattice_kcal_mol'])
        except (ValueError, TypeError):
            return None

    e_cf3 = get_val('pCF3DPU')
    e_cyndpu = get_val('pCyNDPU')
    e_cypdu = get_val('pCyDPU')
    if e_cf3 is None or e_cyndpu is None or e_cypdu is None:
        return 0.0

    # ordering: pCF3DPU (most negative) < pCyNDPU < pCyDPU
    trend_ok = (e_cf3 < e_cyndpu) and (e_cyndpu < e_cypdu)
    trend_score = 1.0 if trend_ok else 0.0

    # absolute tolerance
    abs_count = 0
    if abs(e_cf3 - eng_ref.get('pCF3DPU', e_cf3)) <= tol:
        abs_count += 1
    if abs(e_cyndpu - eng_ref.get('pCyNDPU', e_cyndpu)) <= tol:
        abs_count += 1
    if abs(e_cypdu - eng_ref.get('pCyDPU', e_cypdu)) <= tol:
        abs_count += 1
    abs_score = abs_count / 3.0

    return 0.7 * trend_score + 0.3 * abs_score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
