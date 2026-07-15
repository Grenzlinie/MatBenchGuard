import os
import json
import csv

# === author imports / helpers ===
import math

def f_val(kTc, D_str, n):
    beta = 1.0 / kTc
    x = n * beta
    if D_str == 'Inf':
        return math.tanh(x)
    D_val = float(D_str) if D_str != 'Inf' else 0.0
    eD = math.exp(D_val * beta)
    return 2 * eD * math.sinh(x) / (2 * eD * math.cosh(x) + 1)

def corr_1D(kTc, D_str):
    f2 = f_val(kTc, D_str, 2)
    disc = max(1 - 2*f2, 0)
    return (1 + math.sqrt(disc)) / f2 if f2 > 0 else 0.0

def sum_a_j(kTc, lattice, D_str):
    f1 = f_val(kTc, D_str, 1)
    f2 = f_val(kTc, D_str, 2)
    f3 = f_val(kTc, D_str, 3)
    if lattice == 'honeycomb':
        A1 = 3*f1
        A2 = 3*f2 - 6*f1
        A3 = (f3 - 3*f1)/4.0
        A4 = (3/4.0)*(5*f1 + f3 - 4*f2)
        c = corr_1D(kTc, D_str)
        a_j = A1 - abs(A2) - abs(A3)*c + A4
        return 3 * a_j
    elif lattice == 'square':
        f4 = f_val(kTc, D_str, 4)
        A1 = 4*f1
        A2 = 6*f2 - 12*f1
        A3 = f3 - 3*f1
        A4 = 15*f1 - 12*f2 + 3*f3
        A5 = 0.5*f4 - f3 - f2 + 3*f1
        A6 = 0.5*f4 - 3*f3 + 7*f2 - 7*f1
        c = corr_1D(kTc, D_str)
        a_j = A1 - abs(A2) - c * abs(A3) + A4 + c * A5 + A6
        return 4 * a_j
    elif lattice == 'cubic':
        f4_val = f_val(kTc, D_str, 4)
        f5_val = f_val(kTc, D_str, 5)
        f6_val = f_val(kTc, D_str, 6)
        A1 = 6*f1
        A2 = -30*f1 + 15*f2
        A3 = 5*f3 - 15*f1
        A4 = 75*f1 + 15*f3 - 60*f2
        A5 = -15*f3 + 45*f1 + 7.5*f4_val - 15*f2
        A6 = -45*f3 - 105*(f1 - f2) + 7.5*f4_val
        A7 = 0.375*f5_val - 1.875*f3 + 3.75*f1
        A8 = 11.25*f3 - 52.5*f1 + 3.75*f5_val - 15*f4_val + 30*f2
        A9 = -0.375*f5_val + 1.875*f3 - 3.75*f1 + 0.1875*f6_val - 0.75*f4_val + 0.9375*f2
        A10 = 50.625*f3 + 78.75*f1 + 1.875*f5_val - 15*f4_val - 90*f2
        A11 = -1.25*f3 + 22.5*f1 + 7.5*f4_val - 16.875*f2 - 3.75*f5_val + 0.625*f6_val
        c = corr_1D(kTc, D_str)
        a_j = A1 - abs(A2) - c * abs(A3) + A4 + c * A5 + A6 + A7 + A8 + A9 + A10 + A11
        return 6 * a_j
    else:
        return None


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


# === block: score_0 (check id='step_02_critical_temperatures') ===
def score_0(artifact, step, ctx):
    tol = float(step.get('tolerance', 0.001))
    if artifact is None or not isinstance(artifact, list) or len(artifact) != 6:
        return 0.0

    score = 0.0
    for row in artifact:
        try:
            lattice = row['lattice'].strip().lower()
            D = row['D'].strip().replace('∞', 'Inf')  # may be unicode infinity
            kTc = float(row['kTc_over_J'])
        except (KeyError, ValueError):
            return 0.0
        total = sum_a_j(kTc, lattice, D)
        if total is None:
            return 0.0
        residual = total - 1.0
        score += max(0.0, 1.0 - abs(residual)/tol)

    return score / 6.0


_SCORERS = {
    'step_02_critical_temperatures': score_0,
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
