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
    gold_tau = spec.get('gold_tau', {'CF8C-Plus': 114.0, 'CF8C': 78.0})
    tol = spec.get('tol', 5.0)
    return {'gold': gold_tau, 'tol': tol}


# === block: score_0 (check id='step_02_orowan_recompute') ===
def score_0(artifact, step, ctx):
    def recompute_tau(row):
        G_GPa = float(row['G_GPa'])
        lambda_S_nm = float(row['lambda_S_nm'])
        d_S_nm = float(row['d_S_nm'])
        nu=0.25; M=3.06; b=2.53e-10; r0=b
        G_Pa = G_GPa * 1e9
        lambda_S_m = lambda_S_nm * 1e-9
        d_S_m = d_S_nm * 1e-9
        factor1 = (0.81 * M * G_Pa * b) / (2 * math.pi * math.sqrt(1-nu))
        factor2 = math.log(d_S_m / r0) / (lambda_S_m - d_S_m)
        tau_MPa = (factor1 * factor2) * 1e-6
        return tau_MPa

    rows = artifact
    if len(rows) != 2:
        return 0.0
    gold_tau = ctx['gold']
    tol = ctx['tol']
    alloys_tau = {}
    for r in rows:
        alloy = r.get('alloy')
        if not alloy:
            return 0.0
        tau_recomp = recompute_tau(r)
        alloys_tau[alloy] = tau_recomp
    scores = {}
    for alloy in ['CF8C-Plus', 'CF8C']:
        tau = alloys_tau.get(alloy, None)
        if tau is None:
            scores[alloy] = 0.0
            continue
        gold = gold_tau.get(alloy, None)
        if gold is None:
            scores[alloy] = 0.0
        else:
            if abs(tau - gold) <= tol:
                scores[alloy] = 1.0
            else:
                scores[alloy] = max(0.0, 1.0 - (abs(tau - gold) / (2*tol)))
    ordering_ok = (alloys_tau.get('CF8C-Plus', 0) > alloys_tau.get('CF8C', 0))
    ordering_score = 1.0 if ordering_ok else 0.0
    return 0.4 * scores.get('CF8C-Plus', 0) + 0.4 * scores.get('CF8C', 0) + 0.2 * ordering_score


_SCORERS = {
    'step_02_orowan_recompute': score_0,
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
