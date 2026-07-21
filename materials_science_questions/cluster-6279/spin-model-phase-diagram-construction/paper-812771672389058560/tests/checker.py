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
    return {'z_star': 1.0/(4.0*math.pi), 'T_star': 0.25}


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    z_star = ctx['z_star']
    T_star = ctx['T_star']
    if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    rows = artifact
    valid_rows = 0
    correct = 0
    kt_correct_z = []
    fo_correct_z = []
    for row in rows:
        try:
            z = float(row['z'])
            T = float(row['T'])
            ttype = int(row['transition_type'])
            valid_rows += 1
            ok = False
            if ttype == 0:
                if abs(T - T_star) <= 1e-4 and -1e-6 <= z <= z_star + 1e-6:
                    ok = True
                    kt_correct_z.append(z)
            elif ttype == 1:
                if T <= T_star + 1e-6 and T > 0:
                    a = 1.0/(4.0*T)
                    if a > 1:
                        try:
                            z_ref = (T / math.pi) * (a**(1+a)) * ((a-1)**(1-a))
                            if abs(z - z_ref) <= 1e-10 + 1e-5*abs(z_ref):
                                ok = True
                                fo_correct_z.append(z)
                        except Exception:
                            pass
            if ok:
                correct += 1
        except Exception:
            pass
    if valid_rows == 0:
        return 0.0
    correct_frac = float(correct) / max(valid_rows, 1)
    # Coverage checks
    kt_cov = 0.5
    if kt_correct_z:
        mn = min(kt_correct_z)
        mx = max(kt_correct_z)
        if mn < 0.01 and mx > z_star - 0.01:
            kt_cov = 1.0
    fo_cov = 0.5
    if fo_correct_z:
        mn = min(fo_correct_z)
        mx = max(fo_correct_z)
        if mn < z_star + 0.05 and mx >= 0.3:
            fo_cov = 1.0
    cov = (kt_cov + fo_cov) / 2.0
    return correct_frac * cov


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    z_star = ctx['z_star']
    T_star = ctx['T_star']
    if not isinstance(artifact, dict):
        return 0.0
    if 'z_star' in artifact and 'T_star' in artifact:
        z = float(artifact['z_star'])
        T = float(artifact['T_star'])
        if abs(z - z_star) <= 1e-4 and abs(T - T_star) <= 1e-4:
            return 1.0
    return 0.0


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
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
