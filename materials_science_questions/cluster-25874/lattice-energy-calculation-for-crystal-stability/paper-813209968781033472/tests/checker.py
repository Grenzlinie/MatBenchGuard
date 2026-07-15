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
    with open('/tests/grading_spec.json') as f: spec = json.load(f)
    gold = spec['hidden_assets'][0]['gold']
    return {'gold': gold}


# === block: score_0 (check id='csv_numeric') ===
def score_0(artifact, step, ctx):
    import json
    csv_rows = artifact
    gold = ctx['gold']
    tol_def = {
        'DeltaH_f_gas': ('rel', 0.1, 5.0),
        'DeltaH_f_solid': ('rel', 0.1, 5.0),
        'D': ('abs', 0.5),
        'P': ('abs', 2.0),
        'SE': ('rel', 0.1),
        'BDE_ring_CN': ('rel', 0.1),
        'BDE_N_NO2': ('rel', 0.1),
        'BDE_N_R': ('rel', 0.1),
        'BDE_C_NO2': ('rel', 0.1),
        'Delta_V': ('rel', 0.1)
    }
    scores = []
    for row in csv_rows:
        cpd = row['compound']
        if cpd not in gold:
            continue
        g = gold[cpd]
        for prop, cfg in tol_def.items():
            gval = g.get(prop)
            if gval is None or gval == '':
                continue
            aval_str = row.get(prop, None)
            try:
                aval = float(aval_str)
            except:
                scores.append(0.0)
                continue
            error = abs(aval - gval)
            if cfg[0] == 'abs':
                tol = cfg[1]
            else:
                rel_tol = cfg[1]
                abs_floor = cfg[2] if len(cfg) > 2 else 0.0
                tol = max(rel_tol * abs(gval), abs_floor)
            if error <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (error - tol) / tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='trend_check') ===
def score_1(artifact, step, ctx):
    csv_rows = artifact
    data = {r['compound']: r for r in csv_rows}
    def get_val(cpd, prop):
        try:
            return float(data[cpd][prop])
        except:
            return None
    a0_gas = get_val('A0', 'DeltaH_f_gas')
    a0_solid = get_val('A0', 'DeltaH_f_solid')
    b0_gas = get_val('B0', 'DeltaH_f_gas')
    b0_solid = get_val('B0', 'DeltaH_f_solid')
    checks = []
    # dinitromethyl A1 series lower than A0
    for cpd in ['A11','A12','A13']:
        vg = get_val(cpd, 'DeltaH_f_gas')
        vs = get_val(cpd, 'DeltaH_f_solid')
        if vg is not None and a0_gas is not None:
            checks.append(vg < a0_gas)
        if vs is not None and a0_solid is not None:
            checks.append(vs < a0_solid)
    # dinitromethyl B1 series lower than B0
    for cpd in ['B11','B12','B13','B14','B15']:
        vg = get_val(cpd, 'DeltaH_f_gas')
        vs = get_val(cpd, 'DeltaH_f_solid')
        if vg is not None and b0_gas is not None:
            checks.append(vg < b0_gas)
        if vs is not None and b0_solid is not None:
            checks.append(vs < b0_solid)
    # trinitromethyl A2 series higher than A0
    for cpd in ['A21','A22','A23']:
        vg = get_val(cpd, 'DeltaH_f_gas')
        vs = get_val(cpd, 'DeltaH_f_solid')
        if vg is not None and a0_gas is not None:
            checks.append(vg > a0_gas)
        if vs is not None and a0_solid is not None:
            checks.append(vs > a0_solid)
    # trinitromethyl B2 series higher than B0
    for cpd in ['B21','B22','B23','B24','B25']:
        vg = get_val(cpd, 'DeltaH_f_gas')
        vs = get_val(cpd, 'DeltaH_f_solid')
        if vg is not None and b0_gas is not None:
            checks.append(vg > b0_gas)
        if vs is not None and b0_solid is not None:
            checks.append(vs > b0_solid)
    if not checks:
        return 0.0
    return sum(checks) / len(checks)


_SCORERS = {
    'csv_numeric': score_0,
    'trend_check': score_1,
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
