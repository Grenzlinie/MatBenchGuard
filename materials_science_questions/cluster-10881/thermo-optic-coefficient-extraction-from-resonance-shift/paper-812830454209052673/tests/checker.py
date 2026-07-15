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


# === block: score_0 (check id='chi_t_60_check') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step["reference_value"]
        tol = step["tolerance_abs"]
        try:
            val = float(artifact.strip())
        except Exception:
            return 0.0
        return 1.0 if abs(val - gold) <= tol else 0.0


# === block: score_1 (check id='chi_t_temperature_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref_rows = step["reference_rows"]
        tol = step["tolerance_abs"]
        formula = step["formula_constants"]
        ref_keys = ["temperature_C","gamma_t_1e6","dn_e_dt_4358_1e6","dn_e_dt_5893_1e6","dn_e_dt_6563_1e6","chi_t_4358","chi_t_5893","chi_t_6563"]
        ref_dicts = []
        for row in ref_rows:
            d = {}
            for i, k in enumerate(ref_keys):
                d[k] = row[i]
            ref_dicts.append(d)
        ref_dicts.sort(key=lambda x: x["temperature_C"])
        try:
            artifact_sorted = sorted(artifact, key=lambda r: float(r.get("temperature_C", 0)))
        except Exception:
            return 0.0
        if len(artifact_sorted) != len(ref_dicts):
            return 0.0
        score = 0.0
        for rref, arow in zip(ref_dicts, artifact_sorted):
            try:
                temp = float(arow["temperature_C"])
                gamma = float(arow["gamma_t_1e6"])
                dn4358 = float(arow["dn_e_dt_4358_1e6"])
                dn5893 = float(arow["dn_e_dt_5893_1e6"])
                dn6563 = float(arow["dn_e_dt_6563_1e6"])
                chi4358_rep = float(arow["chi_t_4358"])
                chi5893_rep = float(arow["chi_t_5893"])
                chi6563_rep = float(arow["chi_t_6563"])
            except Exception:
                continue
            if abs(temp - rref["temperature_C"]) > 0.1:
                continue
            if abs(gamma - rref["gamma_t_1e6"]) > tol:
                continue
            if abs(dn4358 - rref["dn_e_dt_4358_1e6"]) > tol:
                continue
            if abs(dn5893 - rref["dn_e_dt_5893_1e6"]) > tol:
                continue
            if abs(dn6563 - rref["dn_e_dt_6563_1e6"]) > tol:
                continue
            const_4358 = formula["4358"]
            exp_4358 = - (const_4358["a"] * dn4358 + const_4358["b"] * gamma) / const_4358["divisor"]
            const_5893 = formula["5893"]
            exp_5893 = - (const_5893["a"] * dn5893 + const_5893["b"] * gamma) / const_5893["divisor"]
            const_6563 = formula["6563"]
            exp_6563 = - (const_6563["a"] * dn6563 + const_6563["b"] * gamma) / const_6563["divisor"]
            if abs(chi4358_rep - exp_4358) > tol:
                continue
            if abs(chi5893_rep - exp_5893) > tol:
                continue
            if abs(chi6563_rep - exp_6563) > tol:
                continue
            if abs(exp_4358 - rref["chi_t_4358"]) > tol:
                continue
            if abs(exp_5893 - rref["chi_t_5893"]) > tol:
                continue
            if abs(exp_6563 - rref["chi_t_6563"]) > tol:
                continue
            score += 1.0
        return score / len(ref_dicts) if ref_dicts else 0.0


_SCORERS = {
    'chi_t_60_check': score_0,
    'chi_t_temperature_check': score_1,
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
