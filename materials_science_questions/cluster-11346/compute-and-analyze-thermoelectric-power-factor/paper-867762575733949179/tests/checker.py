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
    return {"expected_dE": [10,20,30,40,50,60,70,80,90,100,110,120], "expected_N": [2,3,5,7,10,12,15,18,21,25,30]}


# === block: score_0 (check id='step_01_power_factor') ===
def score_0(artifact, step, ctx):
    expected_dE = ctx["expected_dE"]
    expected_N = ctx["expected_N"]
    data = {}
    for r in artifact:
        try:
            dE = int(float(r["dE(meV)"]))
            N = int(float(r["N"]))
            cond = float(r["conductivity(S/m)"])
            S = float(r["Seebeck_coefficient(V/K)"])
            P = float(r["power_factor(W/(K^2 m))"])
            data[(dE, N)] = {"conductivity": cond, "Seebeck": S, "power_factor": P}
        except:
            continue
    n_total = len(expected_dE) * len(expected_N)
    n_rows = len(data)
    completeness = min(1.0, n_rows / n_total) if n_total > 0 else 0.0
    consist_cnt = 0
    for (dE, N), v in data.items():
        P = v["power_factor"]
        sigma = v["conductivity"]
        S = v["Seebeck"]
        expected_P = sigma * S * S
        tol = 1e-12 * max(abs(P), 1e-30)
        if abs(P - expected_P) <= tol:
            consist_cnt += 1
    consist_score = consist_cnt / max(1, n_rows) if n_rows > 0 else 0.0
    order_cnt = 0
    for dE in expected_dE:
        P2 = None
        max_P_gt2 = None
        if (dE, 2) in data:
            P2 = data[(dE, 2)]["power_factor"]
        for N in expected_N:
            if N > 2 and (dE, N) in data:
                val = data[(dE, N)]["power_factor"]
                if max_P_gt2 is None or val > max_P_gt2:
                    max_P_gt2 = val
        if P2 is not None and max_P_gt2 is not None and max_P_gt2 > P2 + 1e-12:
            order_cnt += 1
    order_score = order_cnt / len(expected_dE) if len(expected_dE) > 0 else 0.0
    seeb_cnt = 0
    n_N_with_data = 0
    for N in expected_N:
        vals = []
        for dE in expected_dE:
            if (dE, N) in data:
                vals.append((dE, data[(dE, N)]["Seebeck"]))
        if len(vals) >= 2:
            n_N_with_data += 1
            vals.sort(key=lambda x: x[0])
            inc = True
            for i in range(len(vals)-1):
                if vals[i+1][1] <= vals[i][1]:
                    inc = False
                    break
            if inc:
                seeb_cnt += 1
    seeb_score = seeb_cnt / n_N_with_data if n_N_with_data > 0 else 0.0
    cond_cnt = 0
    n_dE_with_data = 0
    for dE in expected_dE:
        vals = []
        for N in expected_N:
            if (dE, N) in data:
                vals.append((N, data[(dE, N)]["conductivity"]))
        if len(vals) >= 2:
            n_dE_with_data += 1
            vals.sort(key=lambda x: x[0])
            dec = True
            for i in range(len(vals)-1):
                if vals[i+1][1] >= vals[i][1]:
                    dec = False
                    break
            if dec:
                cond_cnt += 1
    cond_score = cond_cnt / n_dE_with_data if n_dE_with_data > 0 else 0.0
    sub_score = 0.2*consist_score + 0.5*order_score + 0.2*seeb_score + 0.1*cond_score
    return sub_score * completeness


_SCORERS = {
    'step_01_power_factor': score_0,
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
