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
    params = {
        "aT": 20.0,
        "aZ": 1.0,
        "aV": 1.0,
        "epsA": 8.0,
        "epsB": 8.0,
        "betaB": 8.0
    }
    params["K"] = (params["aT"] + params["aZ"]) / (1 + params["aZ"]) * params["betaB"]
    return params


# === block: score_0 (check id='step02_spinodal') ===
def score_0(artifact, step, ctx):
    tol = step.get("tolerance_vs", 1e-4)
    if not artifact or len(artifact) < 20:
        return 0.0
    good = 0
    for row in artifact:
        try:
            phiA = float(row["phi_A"])
            phiB = float(row["phi_B"])
        except:
            continue
        if phiA <= 0 or phiB <= 0 or phiA + phiB > 1.0001:
            continue
        vs = ((1 + ctx["epsA"] * phiA) / phiA) * ((1 + ctx["epsB"] * phiB) / phiB) - ctx["K"]**2 / (ctx["aT"] * ctx["aV"])
        if abs(vs) <= tol:
            good += 1
    return good / max(len(artifact), 1)


# === block: score_1 (check id='step03_critical_point') ===
def score_1(artifact, step, ctx):
    tol_vs = step.get("tolerance_vs", 1e-4)
    tol_ratio = step.get("tolerance_ratio", 1e-4)
    try:
        phiA = float(artifact["phi_A_star"])
        phiB = float(artifact["phi_B_star"])
        phiS = float(artifact["phi_s_star"])
    except:
        return 0.0
    if abs(phiS - (1 - phiA - phiB)) > 1e-6:
        return 0.0
    if phiA <= 0 or phiB <= 0 or phiA + phiB > 1.0:
        return 0.0
    vs = ((1 + ctx["epsA"] * phiA) / phiA) * ((1 + ctx["epsB"] * phiB) / phiB) - ctx["K"]**2 / (ctx["aT"] * ctx["aV"])
    ratio = (phiB * (1 + ctx["epsB"] * phiB)) / ((1 + ctx["epsA"] * phiA)**2)
    target_ratio = ctx["aT"] * (1 + ctx["aZ"]) / (ctx["betaB"] * (ctx["aT"] + ctx["aZ"]))
    if abs(vs) <= tol_vs and abs(ratio - target_ratio) <= tol_ratio:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='step04_binodal') ===
def score_2(artifact, step, ctx):
    tol_mu = step.get("tolerance_mu", 1e-3)
    tol_p = step.get("tolerance_p", 1e-3)
    min_points = step.get("min_points", 20)
    if not artifact or len(artifact) < min_points:
        return 0.0
    good = 0
    for row in artifact:
        try:
            phiAa = float(row["phi_A_a"])
            phiBa = float(row["phi_B_a"])
            phiSa = float(row["phi_s_a"])
            phiAb = float(row["phi_A_b"])
            phiBb = float(row["phi_B_b"])
            phiSb = float(row["phi_s_b"])
        except:
            continue
        if (abs(phiSa - (1 - phiAa - phiBa)) > 1e-6 or
            abs(phiSb - (1 - phiAb - phiBb)) > 1e-6):
            continue
        if (phiAa <= 0 or phiBa <= 0 or phiAb <= 0 or phiBb <= 0 or
            phiAa + phiBa > 1.0 or phiAb + phiBb > 1.0):
            continue
        muAa = ctx["aT"] * (math.log(phiAa) + ctx["epsA"] * phiAa) + ctx["K"] * phiBa
        muBa = ctx["aV"] * (math.log(phiBa) + ctx["epsB"] * phiBa) + ctx["K"] * phiAa
        p_a = (ctx["aT"] * phiAa + ctx["aV"] * phiBa +
               (ctx["aT"] * ctx["epsA"] / 2) * phiAa**2 +
               (ctx["epsB"] / 2) * phiBa**2 + ctx["K"] * phiAa * phiBa)
        muAb = ctx["aT"] * (math.log(phiAb) + ctx["epsA"] * phiAb) + ctx["K"] * phiBb
        muBb = ctx["aV"] * (math.log(phiBb) + ctx["epsB"] * phiBb) + ctx["K"] * phiAb
        p_b = (ctx["aT"] * phiAb + ctx["aV"] * phiBb +
               (ctx["aT"] * ctx["epsA"] / 2) * phiAb**2 +
               (ctx["epsB"] / 2) * phiBb**2 + ctx["K"] * phiAb * phiBb)
        if (abs(muAa - muAb) <= tol_mu and abs(muBa - muBb) <= tol_mu and
            abs(p_a - p_b) <= tol_p):
            good += 1
    return good / max(len(artifact), 1)


_SCORERS = {
    'step02_spinodal': score_0,
    'step03_critical_point': score_1,
    'step04_binodal': score_2,
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
