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


# === block: score_0 (check id='spinodal_scaling') ===
def score_0(artifact, step, ctx):
    import math

    # Verify required keys
    required = step.get('required_keys', [])
    for k in required:
        if k not in artifact:
            return 0.0

    # Check L contains required sizes
    required_L = step.get('required_L_values', [])
    L = artifact.get('L', [])
    if not all(s in L for s in required_L):
        return 0.0

    # Check arrays length consistency
    n = len(L)
    if len(artifact.get('beta_spi_f', [])) != n or len(artifact.get('beta_spi_p', [])) != n:
        return 0.0

    # Check beta_c close to exact value
    beta_c_exact = step.get('beta_c_exact')
    beta_c_tol = step.get('beta_c_tolerance', 0.01)
    beta_c = artifact.get('beta_c')
    if beta_c_exact is not None and abs(beta_c - beta_c_exact) > beta_c_tol:
        return 0.0

    # Main check: fitted_nu in range
    nu = artifact.get('fitted_nu')
    if nu is None:
        return 0.0
    low, high = step.get('range', [0, 0])
    if low <= nu <= high:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='landscape_exponents') ===
def score_1(artifact, step, ctx):
    fields = step.get('fields', [])
    score_sum = 0.0
    count = 0
    for f in fields:
        name = f.get('name')
        rng = f.get('range', [None, None])
        val = artifact.get(name)
        if val is not None and rng[0] <= val <= rng[1]:
            score_sum += 1.0
        count += 1
    if count == 0:
        return 0.0
    return score_sum / count


# === block: score_2 (check id='dynamics_tau') ===
def score_2(artifact, step, ctx):
    import csv

    # artifact is a list of dicts from csv.DictReader
    required_cols = ['L', 'beta', 'tau_0.4']
    for col in required_cols:
        if not artifact or col not in artifact[0]:
            return 0.0

    # filter rows for L=256
    L_target = step.get('required_L', 256)
    rows_256 = []
    for row in artifact:
        try:
            if int(row['L']) == L_target:
                rows_256.append(row)
        except:
            continue
    if not rows_256:
        return 0.0

    # Convert to floats
    beta_c = step.get('beta_c')
    betas = []
    taus = []
    for row in rows_256:
        try:
            b = float(row['beta'])
            t = float(row['tau_0.4'])
            if beta_c is not None and b >= beta_c + 1e-6:
                return 0.0
            betas.append(b)
            taus.append(t)
        except:
            return 0.0

    # Sort by beta
    pairs = sorted(zip(betas, taus), key=lambda x: x[0])
    sorted_betas, sorted_taus = zip(*pairs)

    # Check monotonic increasing tau with increasing beta
    for i in range(1, len(sorted_taus)):
        if sorted_taus[i] < sorted_taus[i-1] - 1e-8:
            return 0.0
    return 1.0


# === block: score_3 (check id='dynamics_agreement') ===
def score_3(artifact, step, ctx):
    L_dynamics = artifact.get('L_dynamics')
    if L_dynamics != 256:
        return 0.0
    beta_dev = artifact.get('beta_deviation')
    beta_spi = artifact.get('beta_spi_f')
    if beta_dev is None or beta_spi is None:
        return 0.0

    # Compute difference (we don't trust their reported difference, recompute)
    diff = abs(beta_dev - beta_spi)
    max_diff = step.get('max_difference', 0.02)
    if diff >= max_diff:
        return 0.0

    # Hidden gold check for beta_spi_f
    beta_spi_gold = step.get('beta_spi_f_gold')
    gold_tol = step.get('gold_tolerance', 0.01)
    if beta_spi_gold is not None and abs(beta_spi - beta_spi_gold) > gold_tol:
        return 0.0

    return 1.0


_SCORERS = {
    'spinodal_scaling': score_0,
    'landscape_exponents': score_1,
    'dynamics_tau': score_2,
    'dynamics_agreement': score_3,
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
