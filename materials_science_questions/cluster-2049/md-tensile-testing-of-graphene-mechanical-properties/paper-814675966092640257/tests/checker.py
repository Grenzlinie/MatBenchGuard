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


# === block: score_0 (check id='step_04_grain_size_k') ===
def score_0(artifact, step, ctx):
    tol = step.get('tolerance', 0.02)
    expected = step.get('expected_values', {})
    if not expected:
        return 0.0
    found = {}
    for row in artifact:
        try:
            gs = float(row['grain_size_nm'])
            k = float(row['K_over_K0'])
            found[gs] = k
        except Exception:
            continue
    correct = 0
    for gs_str, exp in expected.items():
        gs = float(gs_str)
        if gs in found and abs(found[gs] - exp) <= tol:
            correct += 1
    return correct / float(len(expected)) if expected else 0.0


# === block: score_1 (check id='step_05_strain_k') ===
def score_1(artifact, step, ctx):
    tol = step.get('tolerance', 0.03)
    coeffs = step.get('coeffs', [])
    K0 = None
    rows_by_sample = {}
    for row in artifact:
        sample = row['sample_type'].strip()
        strain = float(row['strain'])
        K = float(row['thermal_conductivity'])
        rows_by_sample.setdefault(sample, []).append((strain, K))
        if sample == 'SC' and strain == 0.0:
            K0 = K
    if K0 is None:
        return 0.0
    total_points = 0
    good_points = 0
    mono_ok = True
    for sample, base_norm, factor in coeffs:
        data = rows_by_sample.get(sample, [])
        if not data:
            continue
        strain_map = {}
        for s, k in data:
            strain_map[s] = k
        expected_s = [0.0, 0.03, 0.06, 0.09, 0.12]
        values = []
        for s in expected_s:
            if s not in strain_map:
                mono_ok = False
                continue
            K = strain_map[s]
            norm = K / K0
            expected_norm = base_norm * (1.0 - factor * s / 0.12)
            total_points += 1
            if abs(norm - expected_norm) <= tol:
                good_points += 1
            values.append(K)
        for i in range(len(values)-1):
            if values[i] < values[i+1] - 1e-9:
                mono_ok = False
                break
    if total_points == 0:
        return 0.0
    score = good_points / float(total_points)
    return score if mono_ok else score * 0.5


# === block: score_2 (check id='step_06_temperature_k') ===
def score_2(artifact, step, ctx):
    tol = step.get('tolerance', 0.03)
    coeffs = step.get('coeffs', [])
    K0_300 = None
    rows_by_sample = {}
    for row in artifact:
        sample = row['sample_type'].strip()
        T = float(row['temperature_K'])
        K = float(row['thermal_conductivity'])
        rows_by_sample.setdefault(sample, []).append((T, K))
        if sample == 'SC' and abs(T - 300.0) < 1.0:
            K0_300 = K
    if K0_300 is None:
        return 0.0
    total_points = 0
    good_points = 0
    mono_ok = True
    for sample, base_norm, exponent in coeffs:
        data = rows_by_sample.get(sample, [])
        T_map = {}
        for t, k in data:
            T_map[t] = k
        expected_T = [200, 300, 400, 500, 600]
        values = []
        for t in expected_T:
            if t not in T_map:
                mono_ok = False
                continue
            K = T_map[t]
            norm = K / K0_300
            if abs(exponent) < 1e-9:
                expected_norm = base_norm
            else:
                expected_norm = base_norm * ((t / 300.0) ** exponent)
            total_points += 1
            if abs(norm - expected_norm) <= tol:
                good_points += 1
            values.append((t, K))
        for i in range(len(values)-1):
            if values[i][0] < values[i+1][0]:
                if values[i][1] < values[i+1][1] - 1e-9:
                    mono_ok = False
                    break
    if total_points == 0:
        return 0.0
    score = good_points / float(total_points)
    return score if mono_ok else score * 0.5


_SCORERS = {
    'step_04_grain_size_k': score_0,
    'step_05_strain_k': score_1,
    'step_06_temperature_k': score_2,
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
