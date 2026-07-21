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


# === block: score_0 (check id='check_adsorption_energies') ===
def score_0(artifact, step, ctx):
    expected_rows = step.get("expected_rows", [])
    if not artifact or not expected_rows:
        return 0.0
    rows_by_key = {}
    for row in artifact:
        key = (row.get("Model","").strip(), row.get("Orientation","").strip(), row.get("Site","").strip(), str(row.get("Lambda","")).strip())
        rows_by_key[key] = row
    matched = 0
    for exp in expected_rows:
        key = (exp["Model"], exp["Orientation"], exp["Site"], str(exp.get("Lambda","")).strip())
        row = rows_by_key.get(key)
        if row is None:
            continue
        try:
            z_ok = 'z_equilibrium' in exp and abs(float(row.get('z_equilibrium', float('inf'))) - exp['z_equilibrium']) <= exp.get('tolerance_z', 0.0)
            energy_ok = 'AdsorptionEnergy' in exp and abs(float(row.get('AdsorptionEnergy', float('inf'))) - exp['AdsorptionEnergy']) <= exp.get('tolerance_energy', 0.0)
            if z_ok and energy_ok:
                matched += 1
        except (ValueError, TypeError):
            pass
    return matched / len(expected_rows)


# === block: score_1 (check id='check_vibrational_shifts') ===
def score_1(artifact, step, ctx):
    expected_rows = step.get("expected_rows", [])
    if not artifact or not expected_rows:
        return 0.0
    rows_by_model = {}
    for row in artifact:
        model = row.get("Model","").strip()
        rows_by_model[model] = row
    matched = 0
    for exp in expected_rows:
        model = exp["Model"]
        row = rows_by_model.get(model)
        if row is None:
            continue
        try:
            tol = exp.get('tolerance', 0.0)
            ok1 = abs(float(row.get('nu_perp_minus_nu2', float('inf'))) - exp['nu_perp_minus_nu2']) <= tol
            ok2 = abs(float(row.get('nu_parallel_minus_nu2', float('inf'))) - exp['nu_parallel_minus_nu2']) <= tol
            ok3 = abs(float(row.get('nu_perp_minus_nu_parallel', float('inf'))) - exp['nu_perp_minus_nu_parallel']) <= tol
            if ok1 and ok2 and ok3:
                matched += 1
        except (ValueError, TypeError):
            pass
    return matched / len(expected_rows)


_SCORERS = {
    'check_adsorption_energies': score_0,
    'check_vibrational_shifts': score_1,
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
