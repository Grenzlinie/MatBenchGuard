import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='check_csv_schema') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0
    return 1.0


# === block: score_1 (check id='check_numeric_accuracy') ===
def score_1(artifact, step, ctx):
    # Constants (N/m^3) and lattice parameter (m)
    kbSi0 = 6.187e20
    kthetaSi0 = 1.813e20
    kbP0 = 7.897e20
    kthetaP0 = 1.561e20
    a0 = 1.3575e-10

    def a_temp(T):
        return a0 * (1.0 + 2.6e-6 * T)

    def expected_E(N, alpha, T):
        Nf = float(N)
        geom = 8.0 * Nf**2 / (4.0 * Nf + 1.0)**2
        aT = a_temp(T)
        s4 = (a0 / aT) ** 4
        s7 = (a0 / aT) ** 7
        sumSi = 2.0 * kbSi0 * s4 + 3.0 * kthetaSi0 * s7
        sumP = 2.0 * kbP0 * s4 + 3.0 * kthetaP0 * s7
        E_Pa = geom * aT * sumSi + 8.0 * alpha * (aT ** 4) * (sumP - sumSi)
        return E_Pa * 1e-9  # GPa

    # Build lookup from agent CSV: (int(N), float(alpha), int(T)) -> E
    lookup = {}
    for row in artifact:
        try:
            key = (int(row['N']), float(row['alpha']), int(float(row['T'])))
            lookup[key] = float(row['E'])
        except (ValueError, KeyError):
            return 0.0

    sample_points = [
        (1, 0.0, 0),
        (5, 0.0, 0),
        (10, 0.0, 0),
        (100, 0.0, 0),
        (1, 0.1, 0),
        (5, 0.1, 0),
        (10, 1.0, 0),
        (10, 0.1, 500),
        (10, 0.1, 1000),
        (20, 0.1, 0),
        (50, 0.0, 0),
        (100, 0.1, 0)
    ]
    tol = 0.05
    passed = 0
    for N, alpha, T in sample_points:
        key = (N, alpha, T)
        if key not in lookup:
            return 0.0
        E_agent = lookup[key]
        E_exp = expected_E(N, alpha, T)
        if E_exp == 0.0:
            return 0.0
        rel_err = abs(E_agent - E_exp) / abs(E_exp)
        if rel_err <= tol:
            passed += 1
    return passed / len(sample_points)


# === block: score_2 (check id='check_size_monotonic') ===
def score_2(artifact, step, ctx):
    # Build lookup as above
    lookup = {}
    for row in artifact:
        try:
            key = (int(row['N']), float(row['alpha']), int(float(row['T'])))
            lookup[key] = float(row['E'])
        except (ValueError, KeyError):
            return 0.0

    conditions = [
        (0.1, 0),
        (1.0, 0),
        (0.1, 500)
    ]
    N_ordered = [1, 2, 3, 5, 10, 20, 50, 100]
    n_pairs = len(N_ordered) - 1
    passed_pairs = 0
    for alpha, T in conditions:
        for i in range(n_pairs):
            N_small = N_ordered[i]
            N_large = N_ordered[i+1]
            key_small = (N_small, alpha, T)
            key_large = (N_large, alpha, T)
            if key_small not in lookup or key_large not in lookup:
                return 0.0
            if lookup[key_small] <= lookup[key_large]:
                passed_pairs += 1
        # per condition, count all pairs; we'll average over all pairs across conditions
    num_conditions = len(conditions)
    total_pairs = num_conditions * n_pairs
    if total_pairs == 0:
        return 0.0
    return passed_pairs / total_pairs


# === block: score_3 (check id='check_temp_monotonic') ===
def score_3(artifact, step, ctx):
    # Build lookup as above
    lookup = {}
    for row in artifact:
        try:
            key = (int(row['N']), float(row['alpha']), int(float(row['T'])))
            lookup[key] = float(row['E'])
        except (ValueError, KeyError):
            return 0.0

    conditions = [
        (20, 0.1),
        (5, 0.1),
        (10, 1.0)
    ]
    T_ordered = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    n_pairs = len(T_ordered) - 1
    passed_pairs = 0
    for N, alpha in conditions:
        for i in range(n_pairs):
            T_low = T_ordered[i]
            T_high = T_ordered[i+1]
            key_low = (N, alpha, T_low)
            key_high = (N, alpha, T_high)
            if key_low not in lookup or key_high not in lookup:
                return 0.0
            # Young's modulus should decrease (negative temperature coefficient)
            if lookup[key_high] <= lookup[key_low]:
                passed_pairs += 1
    num_conditions = len(conditions)
    total_pairs = num_conditions * n_pairs
    if total_pairs == 0:
        return 0.0
    return passed_pairs / total_pairs


_SCORERS = {
    'check_csv_schema': score_0,
    'check_numeric_accuracy': score_1,
    'check_size_monotonic': score_2,
    'check_temp_monotonic': score_3,
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
