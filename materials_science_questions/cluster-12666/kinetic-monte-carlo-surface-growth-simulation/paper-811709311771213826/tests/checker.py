import os
import json
import csv

# === author imports / helpers ===
import csv, math, os, json


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
    spec = json.load(open('/tests/grading_spec.json'))
    steps = spec.get('steps', [])
    step_map = {s['id']: s for s in steps}
    return {'steps': steps, 'step_map': step_map}


# === block: score_0 (check id='step_kmc_format') ===
def score_0(artifact, step, ctx):
    file_path = os.path.join('/app/outputs', step.get('output_file', ''))
    if not os.path.exists(file_path):
        return 0.0
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if not rows:
            return 0.0
        cols = rows[0].keys()
        required = step.get('required_columns', [])
        if not all(c in cols for c in required):
            return 0.0
        if len(rows) < step.get('min_rows', 3):
            return 0.0
        return 1.0


# === block: score_1 (check id='step_kmc_ratios') ===
def score_1(artifact, step, ctx):
    file_path = os.path.join('/app/outputs', step.get('output_file', 'wavelength_results.csv'))
    if not os.path.exists(file_path):
        return 0.0
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    Phi_kBT = float(step.get('phi_kBT', 3.0))
    Omega = float(step.get('Omega', 1.0))
    kBT = float(step.get('k_BT', 1.0))
    tol_frac = float(step.get('lambda_max_tol_frac', 0.05))
    early_min = float(step.get('ratio_early_min', 0.7))
    early_max = float(step.get('ratio_early_max', 1.1))
    late_min = float(step.get('ratio_late_min', 2.0))
    late_max = float(step.get('ratio_late_max', 3.0))
    need_less = step.get('early_less_than_late', True)

    c_eq0 = math.exp(-Phi_kBT)

    def compute_beta(eps):
        # Eq.(3), a=1, kBT=1
        return 2.0 * (math.sinh(eps / 2.0) ** 2)

    def compute_V0(c0, l):
        # Eq.(11), Ds=1
        return -(1.0 / l) * math.log((1.0 - c0) / (1.0 - c_eq0))

    def compute_lambda_max(beta, V0):
        if V0 <= 0.0 or beta <= 0.0:
            return float('inf')
        lD = 1.0 / V0
        factor = (3.0 * Omega * Omega * beta * c_eq0 * lD) / (kBT * (1.0 - Omega * c_eq0))
        if factor < 0:
            return -1.0
        return 2.0 * math.pi * math.sqrt(factor)

    passed = 0
    for row in rows:
        try:
            eps = float(row['epsilon_kBT'])
            c0 = float(row['c0'])
            l = float(row['l'])
            lam_early = float(row['lambda_early'])
            lam_late = float(row['lambda_late'])
            lam_max_reported = float(row['lambda_max'])
        except (ValueError, KeyError):
            continue
        beta = compute_beta(eps)
        V0 = compute_V0(c0, l)
        lam_max_our = compute_lambda_max(beta, V0)
        if lam_max_our <= 0:
            continue
        # tolerance on lambda_max
        if abs(lam_max_reported - lam_max_our) / max(lam_max_our, 1e-12) > tol_frac:
            continue
        # early < late
        if need_less and lam_early >= lam_late:
            continue
        # ratios
        ratio_early = lam_early / lam_max_our
        ratio_late = lam_late / lam_max_our
        if ratio_early < early_min or ratio_early > early_max:
            continue
        if ratio_late < late_min or ratio_late > late_max:
            continue
        passed += 1

    if not rows:
        return 0.0
    return passed / len(rows)


# === block: score_2 (check id='step_kmc_scaling') ===
def score_2(artifact, step, ctx):
    file_path = os.path.join('/app/outputs', step.get('output_file', 'wavelength_results.csv'))
    if not os.path.exists(file_path):
        return 0.0
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    slope_min = float(step.get('slope_min', 0.4))
    slope_max = float(step.get('slope_max', 0.6))
    min_distinct = int(step.get('min_distinct_params', 3))

    points = []
    for row in rows:
        try:
            beta = float(row['beta_tilde_kBT'])
            V0 = float(row['V0'])
            lam_early = float(row['lambda_early'])
        except (ValueError, KeyError):
            continue
        if beta <= 0 or V0 <= 0 or lam_early <= 0:
            continue
        points.append((beta / V0, lam_early))

    # unique by beta/V ratio
    unique_x = set(p[0] for p in points)
    if len(unique_x) < min_distinct or len(points) < min_distinct:
        return 0.0

    log_x = [math.log(p[0]) for p in points]
    log_y = [math.log(p[1]) for p in points]

    N = len(log_x)
    sum_x = sum(log_x)
    sum_y = sum(log_y)
    sum_xx = sum(x**2 for x in log_x)
    sum_xy = sum(x*y for x,y in zip(log_x, log_y))
    denom = N*sum_xx - sum_x*sum_x
    if denom == 0:
        return 0.0
    slope = (N*sum_xy - sum_x*sum_y) / denom
    if slope_min <= slope <= slope_max:
        return 1.0
    return 0.0


_SCORERS = {
    'step_kmc_format': score_0,
    'step_kmc_ratios': score_1,
    'step_kmc_scaling': score_2,
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
