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


# === block: score_0 (check id='mechanical_properties') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict) or "SrPdH3" not in artifact or "SrLiH3" not in artifact:
        return 0.0

    def safe_div(a, b):
        return a / b if b != 0 else 0.0

    def get_props(ec):
        C11 = ec["C11"]
        C12 = ec["C12"]
        C44 = ec["C44"]
        B = (C11 + 2*C12) / 3.0
        GR = safe_div(5 * C44 * (C11 - C12), 4 * C44 + 3 * (C11 - C12))
        GV = (C11 - C12 + 3 * C44) / 5.0
        G = (GR + GV) / 2.0
        denom_E = 3 * B + G
        E = safe_div(9 * B * G, denom_E)
        sigma = safe_div(3 * B - 2 * G, 2 * denom_E)
        denom_zeta = 7 * C11 + 2 * C12
        zeta = safe_div(C11 + 8 * C12, denom_zeta)
        denom_A = C11 - C12
        A = safe_div(2 * C44, denom_A)
        B_over_G = safe_div(B, G)
        Cauchy = C12 - C44
        return {"G": G, "E": E, "sigma": sigma, "zeta": zeta, "A": A, "B_over_G": B_over_G, "Cauchy": Cauchy}

    props_pd = get_props(artifact["SrPdH3"])
    props_li = get_props(artifact["SrLiH3"])
    gold = step["gold"]
    tols = step["tolerances"]

    def in_tol(value, gold_val, tol_desc):
        typ, val = tol_desc.split()
        tol = float(val)
        if typ == "rel":
            ref = abs(gold_val) if abs(gold_val) > 1e-9 else 1e-9
            return abs(value - gold_val) <= tol * ref
        else:
            return abs(value - gold_val) <= tol

    numeric_keys = ["G", "E", "sigma", "zeta", "A", "B_over_G", "Cauchy"]
    max_score = len(numeric_keys) * 2 + 6  # 14 numeric + 6 classification = 20
    score = 0
    for compound, props in [("SrPdH3", props_pd), ("SrLiH3", props_li)]:
        g = gold[compound]
        for k in numeric_keys:
            if k in props and k in g and k in tols:
                if in_tol(props[k], g[k], tols[k]):
                    score += 1

    # Ductility classifications
    if props_pd["B_over_G"] > 1.75:
        score += 1
    if props_li["B_over_G"] < 1.75:
        score += 1
    if props_pd["sigma"] > 0.26:
        score += 1
    if props_li["sigma"] < 0.26:
        score += 1
    if props_pd["Cauchy"] > 0:
        score += 1
    if props_li["Cauchy"] < 0:
        score += 1

    return score / max_score


_SCORERS = {
    'mechanical_properties': score_0,
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
