import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import json
import os


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
    p = {"alpha_D": 4.42e-5, "delta11": 5.38, "delta44": 2.49, "T_D": 900, "C11_0": 261.9, "C44_0": 148.1}
    ctx = {"tolerance": 0.001, "params": p}
    return ctx


# === block: score_0 (check id='compute_cij_mgo') ===
def score_0(artifact, step, ctx):
    expected_Ts = list(range(900, 2801, 100))
    tol = ctx["tolerance"]
    p = ctx["params"]
    alpha_D = p["alpha_D"]
    delta11 = p["delta11"]
    delta44 = p["delta44"]
    T_D = p["T_D"]
    C11_0 = p["C11_0"]
    C44_0 = p["C44_0"]
    column_names = ['C11_Mur1','C11_Mur2','C11_Tal1','C11_Tal2','C44_Mur1','C44_Mur2','C44_Tal1','C44_Tal2']
    total = len(expected_Ts) * len(column_names)
    correct = 0
    data_by_T = {}
    for row in artifact:
        try:
            T = int(row['Temperature(K)'])
            data_by_T[T] = row
        except:
            pass
    for T in expected_Ts:
        row = data_by_T.get(T, None)
        if row is None:
            continue
        dt = T - T_D
        e11_mur1 = C11_0 * (1 + alpha_D*dt + 0.5*alpha_D**2*delta11*dt**2) ** (-delta11)
        e11_mur2 = C11_0 * (1 + alpha_D*dt + 0.5*alpha_D**2*delta11*dt**2 + (1/3)*alpha_D**3*delta11**2*dt**3) ** (-delta11)
        e11_tal1 = C11_0 * math.exp(-delta11 * (alpha_D*dt + 0.5*alpha_D**2*delta11*dt**2))
        e11_tal2 = C11_0 * math.exp(-delta11 * (alpha_D*dt + 0.5*alpha_D**2*delta11*dt**2 + (1/3)*alpha_D**3*delta11**2*dt**3))
        e44_mur1 = C44_0 * (1 + alpha_D*dt + 0.5*alpha_D**2*delta44*dt**2) ** (-delta44)
        e44_mur2 = C44_0 * (1 + alpha_D*dt + 0.5*alpha_D**2*delta44*dt**2 + (1/3)*alpha_D**3*delta44**2*dt**3) ** (-delta44)
        e44_tal1 = C44_0 * math.exp(-delta44 * (alpha_D*dt + 0.5*alpha_D**2*delta44*dt**2))
        e44_tal2 = C44_0 * math.exp(-delta44 * (alpha_D*dt + 0.5*alpha_D**2*delta44*dt**2 + (1/3)*alpha_D**3*delta44**2*dt**3))
        expected = [e11_mur1, e11_mur2, e11_tal1, e11_tal2, e44_mur1, e44_mur2, e44_tal1, e44_tal2]
        for i, col in enumerate(column_names):
            try:
                val = float(row[col])
            except:
                continue
            ref = expected[i]
            if abs(ref) < 1e-12:
                rel_err = abs(val - ref)
            else:
                rel_err = abs(val - ref) / abs(ref)
            if rel_err <= tol:
                correct += 1
    score = correct / total
    return score


_SCORERS = {
    'compute_cij_mgo': score_0,
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
