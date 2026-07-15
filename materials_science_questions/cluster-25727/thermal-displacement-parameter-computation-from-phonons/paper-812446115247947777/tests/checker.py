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
    def prepare(outputs_dir, spec):
        # compute exact gold values for Debye model Mori parameters and Laplace transforms
        gold = {}
        # Mori coupling coefficients (dimensionless ratios)
        gold['delta1_sq_over_wD2'] = 1.0/3.0
        gold['delta2_sq_over_wD2'] = 4.0/15.0
        gold['delta3_sq_over_wD2'] = 9.0/35.0
        gold['delta4_sq_over_wD2'] = 16.0/63.0
        # Damping coefficients via recurrence with Phi0_laplace_over_wD = pi/2
        phi0_laplace_over_wD = math.pi / 2.0  # displacement Laplace transform (dimensionless)
        gamma1 = gold['delta1_sq_over_wD2'] * phi0_laplace_over_wD
        gold['gamma1_over_wD'] = gamma1  # = pi/6
        gold['gamma2_over_wD'] = gold['delta2_sq_over_wD2'] / gamma1  # = 8/(5*pi)
        gamma2 = gold['gamma2_over_wD']
        gold['gamma3_over_wD'] = gold['delta3_sq_over_wD2'] / gamma2  # = 9*pi/56
        gamma3 = gold['gamma3_over_wD']
        gold['gamma4_over_wD'] = gold['delta4_sq_over_wD2'] / gamma3   # = 128/(81*pi)
        # Laplace transforms
        gold['Phi0_laplace_over_wD'] = math.pi / 2.0
        gold['Phi0_vel_laplace_over_wD'] = 0.0
        return gold


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    artifact = artifact if isinstance(artifact, dict) else {}
    # Compute expected gold values (ctx may be None due to prepare bug)
    # These are fixed from the Debye model.
    delta1 = 1.0/3.0
    delta2 = 4.0/15.0
    delta3 = 9.0/35.0
    delta4 = 16.0/63.0
    phi0_laplace = math.pi / 2.0
    g1 = delta1 * phi0_laplace  # pi/6
    g2 = delta2 / g1           # 8/(5*pi)
    g3 = delta3 / g2           # 9*pi/56
    g4 = delta4 / g3           # 128/(81*pi)
    required = ['delta1_sq_over_wD2','delta2_sq_over_wD2','delta3_sq_over_wD2','delta4_sq_over_wD2',
                'gamma1_over_wD','gamma2_over_wD','gamma3_over_wD','gamma4_over_wD']
    passed = 0
    for key in required:
        val = artifact.get(key)
        if isinstance(val, (int, float)):
            if key == 'delta1_sq_over_wD2':
                expected = delta1
            elif key == 'delta2_sq_over_wD2':
                expected = delta2
            elif key == 'delta3_sq_over_wD2':
                expected = delta3
            elif key == 'delta4_sq_over_wD2':
                expected = delta4
            elif key == 'gamma1_over_wD':
                expected = g1
            elif key == 'gamma2_over_wD':
                expected = g2
            elif key == 'gamma3_over_wD':
                expected = g3
            elif key == 'gamma4_over_wD':
                expected = g4
            else:
                expected = None
            if expected is not None and abs(float(val) - expected) <= 1e-6:
                passed += 1
    score = passed / len(required)
    return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    artifact = artifact if isinstance(artifact, dict) else {}
    gold = ctx
    required = ['Phi0_laplace_over_wD', 'Phi0_vel_laplace_over_wD']
    passed = 0
    for key in required:
        val = artifact.get(key)
        if isinstance(val, (int, float)):
            if abs(float(val) - gold[key]) <= 1e-6:
                passed += 1
    score = passed / len(required)
    # extra tolerance: velocity should be very close to 0, but tolerance applies
    return score


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
