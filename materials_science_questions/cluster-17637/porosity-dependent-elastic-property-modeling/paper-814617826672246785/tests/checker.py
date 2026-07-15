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
    nu = 0.28
    factor = 1.0 / (2.0 * (1.0 - nu*nu))
    porosities = [0.35, 0.45, 0.55, 0.65]
    analytical_ref = [factor * (1.0/p - 1.0) for p in porosities]
    # expected inferred E_wall from M=34.5, phi=0.60, nu=0.28
    M = 34.5
    phi_infer = 0.60
    expected_E = 2.0 * M * (1.0 - nu*nu) / (1.0/phi_infer - 1.0)
    return {"analytical_ref": analytical_ref, "expected_E": expected_E}


# === block: score_0 (check id='check_shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    keys_ok = all(k in artifact for k in ["analytical", "fem", "inferred_E_GPa"])
    arrays_ok = True
    for k in ["analytical", "fem"]:
        arr = artifact.get(k)
        if not isinstance(arr, list) or len(arr) != 4:
            arrays_ok = False
            break
        for item in arr:
            if not isinstance(item, dict) or "porosity" not in item or "M_over_E" not in item:
                arrays_ok = False
                break
        if not arrays_ok:
            break
    return 1.0 if keys_ok and arrays_ok else 0.0


# === block: score_1 (check id='check_analytical') ===
def score_1(artifact, step, ctx):
    if "analytical_ref" not in ctx:
        return 0.0
    analytical_arr = artifact.get("analytical")
    if not isinstance(analytical_arr, list) or len(analytical_arr) != 4:
        return 0.0
    ref = ctx["analytical_ref"]
    tol = step.get("tolerance_analytical_rel", 1e-6)
    porosities_order = step.get("porosities", [0.35,0.45,0.55,0.65])
    scores = []
    for i, expected_poro in enumerate(porosities_order):
        # find item with matching porosity
        match = None
        for item in analytical_arr:
            if abs(item["porosity"] - expected_poro) < 1e-9:
                match = item
                break
        if match is None:
            scores.append(0.0)
            continue
        reported = match["M_over_E"]
        expected = ref[i]
        if expected == 0.0:
            s = 1.0 if reported == 0.0 else 0.0
        else:
            err = abs(reported - expected) / abs(expected)
            s = 1.0 if err <= tol else 0.0
        scores.append(s)
    return sum(scores)/len(scores)


# === block: score_2 (check id='check_fem') ===
def score_2(artifact, step, ctx):
    if "analytical_ref" not in ctx:
        return 0.0
    fem_arr = artifact.get("fem")
    if not isinstance(fem_arr, list) or len(fem_arr) != 4:
        return 0.0
    ref = ctx["analytical_ref"]
    tol = step.get("tolerance_fem_rel", 0.10)
    porosities_order = step.get("porosities", [0.35,0.45,0.55,0.65])
    scores = []
    for i, expected_poro in enumerate(porosities_order):
        match = None
        for item in fem_arr:
            if abs(item["porosity"] - expected_poro) < 1e-9:
                match = item
                break
        if match is None:
            scores.append(0.0)
            continue
        reported = match["M_over_E"]
        expected = ref[i]
        if expected == 0.0:
            s = 1.0 if reported == 0.0 else 0.0
        else:
            err = abs(reported - expected) / abs(expected)
            s = 1.0 if err <= tol else 0.0
        scores.append(s)
    return sum(scores)/len(scores)


# === block: score_3 (check id='check_inferred') ===
def score_3(artifact, step, ctx):
    if "expected_E" not in ctx:
        return 0.0
    reported_E = artifact.get("inferred_E_GPa")
    if not isinstance(reported_E, (int, float)):
        return 0.0
    expected = ctx["expected_E"]
    tol = step.get("tolerance_inferred_rel", 0.05)
    if expected == 0.0:
        return 1.0 if reported_E == 0.0 else 0.0
    err = abs(reported_E - expected) / abs(expected)
    return 1.0 if err <= tol else 0.0


_SCORERS = {
    'check_shape': score_0,
    'check_analytical': score_1,
    'check_fem': score_2,
    'check_inferred': score_3,
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
