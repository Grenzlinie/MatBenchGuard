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
    ref = {}
    # ---- high_temp_P2 reference ----
    gamma=1.0; m1=1.0; m2=4.0
    w1sq = 2*gamma/m1
    w2sq = 2*gamma/m2
    ref_p2 = {}
    for r in range(1,21):
        if r%2==1:
            if r==1:
                p2 = w1sq/(24*m1)
            else:
                p2 = w1sq/(12*m1)
        else:
            if r==20:
                p2 = w2sq/(24*m2)
            else:
                p2 = w2sq/(12*m2)
        ref_p2[r] = p2
    ref['ref_p2'] = ref_p2

    # ---- low_temp_msv reference ----
    N=20; m=1.0; gamma=1.0
    omega_L = math.sqrt(4*gamma/m)
    factor = omega_L / (16 * N * m)  # hbar=1
    d = math.pi/(8*N)
    ref_msv = {}
    for r in range(1, N+1):
        arg1 = (4*r-1)*d
        arg2 = (4*r-3)*d
        cot1 = math.cos(arg1)/math.sin(arg1)
        cot2 = math.cos(arg2)/math.sin(arg2)
        cotd = math.cos(d)/math.sin(d)
        msv = factor * (cot1 - cot2 + 2*cotd)
        ref_msv[r] = msv
    ref['ref_msv'] = ref_msv

    return ref


# === block: score_0 (check id='step_high_temp_P2') ===
def score_0(artifact, step, ctx):
    ref = ctx['ref_p2']
    tol_rel = step.get('tolerance_rel', 1e-8)
    if not artifact or not isinstance(artifact, list):
        return 0.0
    indices = set()
    for row in artifact:
        try:
            idx = int(row['atom_index'])
        except (ValueError, KeyError, TypeError):
            continue
        indices.add(idx)
    expected_indices = set(range(1,21))
    if indices != expected_indices:
        return 0.0
    ok = 0
    for row in artifact:
        idx = int(row['atom_index'])
        val = float(row['P2_value'])
        exp = ref[idx]
        if exp == 0.0:
            if abs(val) < 1e-12:
                ok += 1
        else:
            rel_err = abs(val - exp) / abs(exp)
            if rel_err <= tol_rel:
                ok += 1
    return ok / 20.0


# === block: score_1 (check id='step_low_temp_msv') ===
def score_1(artifact, step, ctx):
    ref = ctx['ref_msv']
    tol_rel = step.get('tolerance_rel', 1e-8)
    if not artifact or not isinstance(artifact, list):
        return 0.0
    indices = set()
    for row in artifact:
        try:
            idx = int(row['atom_index'])
        except (ValueError, KeyError, TypeError):
            continue
        indices.add(idx)
    expected_indices = set(range(1,21))
    if indices != expected_indices:
        return 0.0
    ok = 0
    for row in artifact:
        idx = int(row['atom_index'])
        val = float(row['mean_square_velocity'])
        exp = ref[idx]
        if exp == 0.0:
            if abs(val) < 1e-12:
                ok += 1
        else:
            rel_err = abs(val - exp) / abs(exp)
            if rel_err <= tol_rel:
                ok += 1
    return ok / 20.0


_SCORERS = {
    'step_high_temp_P2': score_0,
    'step_low_temp_msv': score_1,
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
