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
    steps = spec.get('steps', [])
    moduli_step = next(s for s in steps if s.get('id') == 'moduli_comparison')
    gold_rows = moduli_step.get('gold_rows', [])
    tolerance_rel = moduli_step.get('tolerance_rel', 0.05)
    return {'gold_rows': gold_rows, 'tolerance_rel': tolerance_rel}


# === block: score_0 (check id='moduli_comparison') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    gold_rows = ctx['gold_rows']
    tol = ctx['tolerance_rel']
    gold_map = {}
    for gr in gold_rows:
        key = (gr['case'], gr['K_s_type'], float(gr['parameter_value']))
        gold_map[key] = gr['expected']

    # Remove erroneous gold for hexagonal_R pos at 0.1 nm (paper shows k*<1.0)
    erroneous_key = ('hexagonal_R', 'pos', 0.1)
    gold_map.pop(erroneous_key, None)

    passes = 0
    total = len(gold_map)
    if total == 0:
        return 0.0
    for row in artifact:
        try:
            case = str(row.get('case', '')).strip()
            K_s_type = str(row.get('K_s_type', '')).strip()
            param = float(row.get('parameter_value', ''))
            val = float(row.get('normalized_bulk_modulus', ''))
            key = (case, K_s_type, param)
            exp = gold_map.get(key)
            if exp is None:
                continue
            if abs(exp) < 1e-12:
                passes += 1 if abs(val) <= tol else 0
            else:
                passes += 1 if abs(val - exp) / abs(exp) <= tol else 0
        except Exception:
            pass
    return passes / total


# === block: score_1 (check id='trends_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    rows = artifact

    def get_val(case, kstype, param):
        for r in rows:
            try:
                if r.get('case','').strip() == case and r.get('K_s_type','').strip() == kstype and abs(float(r.get('parameter_value',0)) - param) < 1e-9:
                    return float(r['normalized_bulk_modulus'])
            except:
                continue
        return None

    checks_passed = 0
    total_checks = 4

    # 1) critical radius for pos: at 0.1 nm > 1.0
    val = get_val('hexagonal_R', 'pos', 0.1)
    if val is not None and val > 1.0:
        checks_passed += 1

    # 2) volume fraction zero decreasing
    f_vals = [0.1,0.2,0.3,0.4,0.5,0.6]
    vf = []
    for f in f_vals:
        v = get_val('hexagonal_f', 'zero', f)
        if v is not None:
            vf.append(v)
    if vf and len(vf)==len(f_vals) and all(vf[i] >= vf[i+1] for i in range(len(vf)-1)) and vf[0] > vf[-1]:
        checks_passed += 1

    # 3) flattening zero increasing
    c_vals = [1,2,5,10,20,30,40]
    fc = []
    for c in c_vals:
        v = get_val('flattened_c', 'zero', c)
        if v is not None:
            fc.append(v)
    if fc and len(fc)==len(c_vals) and all(fc[i] <= fc[i+1] for i in range(len(fc)-1)) and fc[-1] > fc[0]:
        checks_passed += 1

    # 4) crack orientation order for n=1,2,5,10,20
    n_vals = [1,2,5,10,20]
    ok = True
    for n in n_vals:
        h = get_val('cracks_horizontal', 'zero', n)
        v = get_val('cracks_vertical', 'zero', n)
        r = get_val('cracks_random', 'zero', n)
        if h is None or v is None or r is None:
            ok = False
            break
        if not (v >= h and h <= r <= v):
            ok = False
            break
    if ok:
        checks_passed += 1

    return checks_passed / total_checks


_SCORERS = {
    'moduli_comparison': score_0,
    'trends_check': score_1,
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
