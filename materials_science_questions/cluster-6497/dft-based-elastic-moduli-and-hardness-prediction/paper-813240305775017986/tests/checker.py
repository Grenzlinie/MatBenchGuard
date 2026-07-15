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


# === block: score_0 (check id='al24o24n8_results') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts from csv.DictReader
    ref = step['reference']
    tol = step.get('tolerance_d_NN', 0.1)
    d_NN_ref = ref['d_NN']
    energy_order_ref = ref['energy_order']

    # build per functional group
    from collections import defaultdict
    groups = defaultdict(list)
    for row in rows:
        func = row['functional'].strip()
        groups[func].append(row)

    energy_order_ok = 0
    for func, exp_order in energy_order_ref.items():
        rows_func = groups.get(func, [])
        if not rows_func:
            continue
        # find model with min total_energy
        min_row = min(rows_func, key=lambda r: float(r['total_energy']))
        if min_row['model'].strip() == str(exp_order[0]):
            energy_order_ok += 1

    # check all rows d_NN distance
    d_NN_passed = 0
    total_rows = 0
    for row in rows:
        model = row['model'].strip()
        func = row['functional'].strip()
        dnn = float(row['d_NN'])
        expected = d_NN_ref.get(model, {}).get(func)
        total_rows += 1
        if expected is not None and abs(dnn - expected) <= tol:
            d_NN_passed += 1

    score = 0.0
    if total_rows > 0:
        dnn_frac = d_NN_passed / total_rows
        order_frac = energy_order_ok / len(energy_order_ref) if energy_order_ref else 1.0
        score = (dnn_frac + order_frac) / 2.0
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='al23o27n5_results') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ref = step['reference']
    tol = step.get('tolerance_band_gap', 0.5)

    from collections import defaultdict
    groups = defaultdict(list)
    for row in rows:
        func = row['functional'].strip()
        groups[func].append(row)

    # energy ordering: model 1 should have lowest energy for both GGA and LDA
    energy_ok = 0
    for func in ['GGA', 'LDA']:
        rows_func = groups.get(func, [])
        if not rows_func:
            continue
        min_row = min(rows_func, key=lambda r: float(r['total_energy']))
        if min_row['model'].strip() == str(ref['lowest_energy_model']):
            energy_ok += 1

    # band gap for model 1
    band_gap_ok = 0
    for row in rows:
        if row['model'].strip() == str(ref['lowest_energy_model']):
            func = row['functional'].strip()
            bg = float(row['band_gap'])
            expected = ref['band_gap_model1'].get(func)
            if expected is not None and abs(bg - expected) <= tol:
                band_gap_ok += 1

    n_order = 2  # GGA, LDA
    n_gap = 2   # GGA, LDA
    order_frac = energy_ok / n_order if n_order else 1.0
    gap_frac = band_gap_ok / n_gap if n_gap else 1.0
    score = (order_frac + gap_frac) / 2.0
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='bulk_modulus_fit') ===
def score_2(artifact, step, ctx):
    text = artifact  # string content of bulk_modulus_fit.txt
    ref = step['reference']
    tol_rel = step.get('tolerance_relative', 0.05)

    lines = text.strip().split('\n')
    parsed = {}
    for line in lines:
        parts = line.split(',')
        entry = {}
        for part in parts:
            if '=' in part:
                k, v = part.split('=', 1)
                entry[k.strip()] = v.strip()
        func = entry.get('functional')
        if func:
            parsed[func] = entry

    checks = 0
    passed = 0
    for func, expected in ref.items():
        if func not in parsed:
            continue
        for key, target in expected.items():
            checks += 1
            val = parsed[func].get(key)
            if val is None:
                continue
            try:
                val = float(val)
            except ValueError:
                continue
            if abs(val - target) <= tol_rel * abs(target):
                passed += 1

    if checks == 0:
        return 0.0
    return passed / checks


# === block: score_3 (check id='elastic_constants') ===
def score_3(artifact, step, ctx):
    text = artifact
    ref = step['reference']
    tol_rel = step.get('tolerance_relative', 0.10)

    lines = text.strip().split('\n')
    vals = {}
    for line in lines:
        parts = line.split(',')
        for part in parts:
            if '=' in part:
                k, v = part.split('=', 1)
                k = k.strip()
                if k in ref:
                    try:
                        vals[k] = float(v.strip())
                    except ValueError:
                        pass

    checks = 0
    passed = 0
    for key, target in ref.items():
        checks += 1
        val = vals.get(key)
        if val is not None and abs(val - target) <= tol_rel * abs(target):
            passed += 1

    if checks == 0:
        return 0.0
    return passed / checks


_SCORERS = {
    'al24o24n8_results': score_0,
    'al23o27n5_results': score_1,
    'bulk_modulus_fit': score_2,
    'elastic_constants': score_3,
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
