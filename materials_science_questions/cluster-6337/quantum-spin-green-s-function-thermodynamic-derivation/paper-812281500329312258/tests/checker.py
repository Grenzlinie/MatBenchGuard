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


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0

    TOL_L1 = 1e-4
    TOL_L2 = 1e-4
    TOL_LINF = 1e-6

    total = 0
    passed = 0
    for row in artifact:
        try:
            a = float(row['alpha'])
            L1 = float(row['L1'])
            L2 = float(row['L2'])
            L_inf = float(row['L_inf'])
        except (KeyError, ValueError):
            continue

        # --- L1 reference ---
        denom = 1.0 + a/2.0
        if abs(denom) < 1e-12:
            # singularity at alpha = -2; skip row
            continue
        L1r = 1.5 * (1.0 + a/6.0) / denom

        # --- L_inf reference ---
        if a > 0:
            sr = math.sqrt(a)
            L_inf_r = math.tanh(sr) / sr
        elif a < 0:
            sr = math.sqrt(-a)
            L_inf_r = math.tan(sr) / sr
        else:
            L_inf_r = 1.0

        # --- L2 reference via recursion (n=2) ---
        n = 2
        Z = 1.0   # Z'(0)
        G = 1.0   # G'(0) = Z'(0)
        for k in range(1, n+1):
            Zk = Z + a/(2*n) * G
            Gk = (2*k)/(2*k+1) * G + (1/(2*k+1)) * Zk
            Z = Zk
            G = Gk
        L2r = (2*n+1)/(2*n) * G / Z

        # skip rows where any reference is non‑finite
        if not (math.isfinite(L1r) and math.isfinite(L2r) and math.isfinite(L_inf_r)):
            continue
        if not (math.isfinite(L1) and math.isfinite(L2) and math.isfinite(L_inf)):
            continue

        ok = True
        if abs(L1 - L1r) > TOL_L1:
            ok = False
        if abs(L2 - L2r) > TOL_L2:
            ok = False
        if abs(L_inf - L_inf_r) > TOL_LINF:
            ok = False

        total += 1
        if ok:
            passed += 1

    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    target = float(step.get('target', 0.1907))
    tol = float(step.get('tolerance_abs', 0.0005))
    val = float(artifact.strip())
    return 1.0 if abs(val - target) <= tol else 0.0


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
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
