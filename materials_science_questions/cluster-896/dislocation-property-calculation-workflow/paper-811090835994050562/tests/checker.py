import os
import json
import csv

# === author imports / helpers ===
import json
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
    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        gold = {"factors": {"203136": 0.40, "1511": 0.50, "001": 0.41}}
        for step in steps:
            sid = step["id"]
            if sid.startswith("critical_sigma_"):
                orient = sid.split("_")[-1]
                gold[orient] = {"target": step["target"], "tolerance": step["tolerance"]}
            elif sid == "compliance_S2321":
                gold["S2321"] = {"target": step["target"], "tolerance": step["tolerance"]}
            elif sid == "compliance_S2323":
                gold["S2323"] = {"target": step["target"], "tolerance": step["tolerance"]}
        return {"gold": gold}


# === block: score_0 (check id='critical_sigma_203136') ===
def score_0(artifact, step, ctx):
    def score_critical_sigma_203136(artifact, step, ctx):
        orient = "203136"
        coeff = artifact[orient]["coefficient"]
        sigma = abs(coeff * ctx["gold"]["factors"][orient])
        target = ctx["gold"][orient]["target"]
        tol = ctx["gold"][orient]["tolerance"]
        error_relative = abs(sigma - target) / target
        if error_relative <= tol:
            return 1.0
        elif error_relative >= 2 * tol:
            return 0.0
        else:
            return max(0.0, 1.0 - (error_relative - tol) / tol)


# === block: score_1 (check id='critical_sigma_1511') ===
def score_1(artifact, step, ctx):
    def score_critical_sigma_1511(artifact, step, ctx):
        orient = "1511"
        coeff = artifact[orient]["coefficient"]
        sigma = abs(coeff * ctx["gold"]["factors"][orient])
        target = ctx["gold"][orient]["target"]
        tol = ctx["gold"][orient]["tolerance"]
        error_relative = abs(sigma - target) / target
        if error_relative <= tol:
            return 1.0
        elif error_relative >= 2 * tol:
            return 0.0
        else:
            return max(0.0, 1.0 - (error_relative - tol) / tol)


# === block: score_2 (check id='critical_sigma_001') ===
def score_2(artifact, step, ctx):
    def score_critical_sigma_001(artifact, step, ctx):
        orient = "001"
        coeff = artifact[orient]["coefficient"]
        sigma = abs(coeff * ctx["gold"]["factors"][orient])
        target = ctx["gold"][orient]["target"]
        tol = ctx["gold"][orient]["tolerance"]
        error_relative = abs(sigma - target) / target
        if error_relative <= tol:
            return 1.0
        elif error_relative >= 2 * tol:
            return 0.0
        else:
            return max(0.0, 1.0 - (error_relative - tol) / tol)


# === block: score_3 (check id='stress_ordering') ===
def score_3(artifact, step, ctx):
    def score_stress_ordering(artifact, step, ctx):
        sigma = {}
        for orient in ["203136", "1511", "001"]:
            coeff = artifact[orient]["coefficient"]
            sigma[orient] = abs(coeff * ctx["gold"]["factors"][orient])
        if sigma["203136"] < sigma["1511"] < sigma["001"]:
            return 1.0
        else:
            return 0.0


# === block: score_4 (check id='compliance_S2321') ===
def score_4(artifact, step, ctx):
    def score_compliance_S2321(artifact, step, ctx):
        val = artifact["S_prime_2321"]
        target = ctx["gold"]["S2321"]["target"]
        tol = ctx["gold"]["S2321"]["tolerance"]
        error_relative = abs(val - target) / abs(target)
        if error_relative <= tol:
            return 1.0
        elif error_relative >= 2 * tol:
            return 0.0
        else:
            return max(0.0, 1.0 - (error_relative - tol) / tol)


# === block: score_5 (check id='compliance_S2323') ===
def score_5(artifact, step, ctx):
    def score_compliance_S2323(artifact, step, ctx):
        val = artifact["S_prime_2323"]
        target = ctx["gold"]["S2323"]["target"]
        tol = ctx["gold"]["S2323"]["tolerance"]
        error_relative = abs(val - target) / abs(target)
        if error_relative <= tol:
            return 1.0
        elif error_relative >= 2 * tol:
            return 0.0
        else:
            return max(0.0, 1.0 - (error_relative - tol) / tol)


_SCORERS = {
    'critical_sigma_203136': score_0,
    'critical_sigma_1511': score_1,
    'critical_sigma_001': score_2,
    'stress_ordering': score_3,
    'compliance_S2321': score_4,
    'compliance_S2323': score_5,
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
