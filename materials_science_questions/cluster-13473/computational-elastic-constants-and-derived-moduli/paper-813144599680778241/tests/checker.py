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


# === block: score_0 (check id='derived_elastic_quantities') ===
def score_0(artifact, step, ctx):
    gold_cases = step["gold_cases"]
    tolerances = step["tolerances"]

    def get_matrix_mean(case):
        return case.get("mean", None)

    def compute_derived(mat):
        C11_avg = (mat[0][0] + mat[1][1] + mat[2][2]) / 3.0
        C12 = mat[0][1]
        C13 = mat[0][2]
        C23 = mat[1][2]
        C12_avg = (C12 + C13 + C23) / 3.0
        C44_avg = (mat[3][3] + mat[4][4] + mat[5][5]) / 3.0
        cubic = [[0.0]*6 for _ in range(6)]
        for i in range(3): cubic[i][i] = C11_avg
        for i in range(3,6): cubic[i][i] = C44_avg
        off = [(0,1),(0,2),(1,2)]
        for (i,j) in off:
            cubic[i][j] = C12_avg
            cubic[j][i] = C12_avg
        sq_diff = sum((mat[i][j] - cubic[i][j])**2 for i in range(6) for j in range(6))
        sq_cubic = sum(cubic[i][j]**2 for i in range(6) for j in range(6))
        if sq_cubic == 0:
            dist = 0.0
        else:
            dist = math.sqrt(sq_diff) / math.sqrt(sq_cubic)
        return C11_avg, C12_avg, C44_avg, dist

    cases_list = ["D500_P1", "D1000_P1", "D1000_P10"]
    total_checks = 0
    passed = 0
    for case_id in cases_list:
        if case_id not in artifact:
            continue
        mat = get_matrix_mean(artifact[case_id])
        if mat is None or len(mat) != 6 or any(len(row) != 6 for row in mat):
            continue
        try:
            C11a, C12a, C44a, dista = compute_derived(mat)
        except Exception:
            continue
        gc = gold_cases.get(case_id, {})
        tol_C11 = tolerances.get("C11_avg", 0.1)
        tol_C12 = tolerances.get("C12_avg", 0.05)
        tol_C44 = tolerances.get("C44_avg", 0.05)
        tol_dist = tolerances.get("dist", 0.1)
        if abs(C11a - gc.get("C11_avg", None)) <= tol_C11: passed += 1
        total_checks += 1
        if abs(C12a - gc.get("C12_avg", None)) <= tol_C12: passed += 1
        total_checks += 1
        if abs(C44a - gc.get("C44_avg", None)) <= tol_C44: passed += 1
        total_checks += 1
        if abs(dista - gc.get("dist", None)) <= tol_dist: passed += 1
        total_checks += 1

    if "D1000_P1" in artifact and "D1000_P10" in artifact:
        mat1 = get_matrix_mean(artifact["D1000_P1"])
        mat10 = get_matrix_mean(artifact["D1000_P10"])
        if mat1 is not None and mat10 is not None and len(mat1)==6 and all(len(r)==6 for r in mat1) and len(mat10)==6 and all(len(r)==6 for r in mat10):
            try:
                C11_1, C12_1, C44_1, _ = compute_derived(mat1)
                C11_10, C12_10, C44_10, _ = compute_derived(mat10)
                if C11_10 > C11_1: passed += 1
                total_checks += 1
                if C12_10 > C12_1: passed += 1
                total_checks += 1
                if C44_10 > C44_1: passed += 1
                total_checks += 1
            except Exception:
                pass

    score = passed / total_checks if total_checks > 0 else 0.0
    return score


_SCORERS = {
    'derived_elastic_quantities': score_0,
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
