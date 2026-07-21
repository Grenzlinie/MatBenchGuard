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


# === block: score_0 (check id='verify_results') ===
def score_0(artifact, step, ctx):
        if not artifact:
            return 0.0
        rows = artifact
        required = ['T','M_abs_tail','M_abs_free','M2_tail','M2_free','E_tail','E_free','Cv_tail','Cv_free','R2_tail','R2_free','S2_tail','S2_free','N_nn_tail','N1_tail']
        if any(r not in rows[0] for r in required):
            return 0.0
        try:
            data = [{k: float(v) for k,v in row.items()} for row in rows]
        except:
            return 0.0
        data.sort(key=lambda r: r['T'])
        T = [r['T'] for r in data]
        M_abs_tail = [r['M_abs_tail'] for r in data]
        M_abs_free = [r['M_abs_free'] for r in data]
        E_tail = [r['E_tail'] for r in data]
        E_free = [r['E_free'] for r in data]
        Cv_tail = [r['Cv_tail'] for r in data]
        R2_tail = [r['R2_tail'] for r in data]
        R2_free = [r['R2_free'] for r in data]
        S2_tail = [r['S2_tail'] for r in data]
        S2_free = [r['S2_free'] for r in data]
        N1_tail = [r['N1_tail'] for r in data]
        n = len(T)
        if n < 5:
            return 0.0
        passed = 0
        total = 0

        # 1. Tc from steepest change in M_abs_tail (max -dM/dT)
        der = [(M_abs_tail[i+1]-M_abs_tail[i])/(T[i+1]-T[i]) for i in range(n-1)]
        idx = max(range(len(der)), key=lambda i: -der[i])
        Tc_M = T[idx]
        if 1.28 <= Tc_M <= 1.32:
            passed += 1
        total += 1

        # 2. Tc from Cv_tail maximum
        idx_cv = max(range(n), key=lambda i: Cv_tail[i])
        Tc_CV = T[idx_cv]
        if 1.28 <= Tc_CV <= 1.32:
            passed += 1
        total += 1

        # 3. M_abs_tail at lowest T > 0.9
        if M_abs_tail[0] > 0.9:
            passed += 1
        total += 1

        # 4. M_abs_tail at highest T < 0.2
        if M_abs_tail[-1] < 0.2:
            passed += 1
        total += 1

        # 5. Surface independence: |M_abs_tail - M_abs_free| < 0.1 for all T
        if all(abs(M_abs_tail[i]-M_abs_free[i]) < 0.1 for i in range(n)):
            passed += 1
        total += 1

        # 6. Surface independence: |E_tail - E_free| < 0.2 for all T
        if all(abs(E_tail[i]-E_free[i]) < 0.2 for i in range(n)):
            passed += 1
        total += 1

        # 7. Configurational size: R2_tail > R2_free for all T
        if all(R2_tail[i] > R2_free[i] for i in range(n) if R2_free[i] != 0):
            passed += 1
        total += 1

        # 8. Configurational size: S2_tail > S2_free for all T
        if all(S2_tail[i] > S2_free[i] for i in range(n) if S2_free[i] != 0):
            passed += 1
        total += 1

        # 9. Surface contact: N1_tail at lowest T > N1_tail at highest T
        if N1_tail[0] > N1_tail[-1]:
            passed += 1
        total += 1

        # 10. Specific heat peak clarity: max(Cv) > 1.5 * mean(Cv)
        if max(Cv_tail) > 1.5 * sum(Cv_tail)/n:
            passed += 1
        total += 1

        return passed / total if total > 0 else 0.0


_SCORERS = {
    'verify_results': score_0,
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
