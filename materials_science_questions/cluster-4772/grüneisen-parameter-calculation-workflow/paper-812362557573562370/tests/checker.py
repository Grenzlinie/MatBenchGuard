import os
import json
import csv

# === author imports / helpers ===
import math, json, csv


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
    import math
    steps = spec.get("steps", [])
    mstep = None
    for s in steps:
        if s.get("id") == "melting_curve":
            mstep = s
            break
    gold_params = mstep["target"]["gold_params"]
    gamma1 = gold_params["gamma1"]
    gamma2 = gold_params["gamma2"]
    q = gold_params["q"]
    rhom = mstep["target"]["reference_density"]
    Tmr = mstep["target"]["reference_Tm"]
    densities = mstep["target"]["required_densities"]
    rhom_cuberoot = rhom**(1/3)
    rhom_q = rhom**q
    A = 6 * gamma1 / rhom_cuberoot + 2 * gamma2 / (q * rhom_q)
    gold_Tm = {}
    for rho in densities:
        B = 6 * gamma1 / (rho**(1/3)) + 2 * gamma2 / (q * (rho**q))
        Tm = Tmr * (rho / rhom)**(1/3) * math.exp(A - B)
        gold_Tm[str(rho)] = Tm
    return {"gold_params": gold_params, "gold_Tm": gold_Tm, "densities": densities}


# === block: score_0 (check id='gruneisen_params') ===
def score_0(artifact, step, ctx):
    art = artifact
    gold = ctx.get("gold_params", {})
    if not gold:
        return 0.0
    gamma1_ok = abs(art.get("gamma1", 0) - gold["gamma1"]) <= gold["gamma1"] * 0.05
    gamma2_ok = False
    if art.get("gamma2", 0) > 0:
        gamma2_ok = abs(math.log10(art["gamma2"]) - math.log10(gold["gamma2"])) <= 1.0
    q_ok = abs(art.get("q", 0) - gold["q"]) <= 1.0
    score = 0.0
    if gamma1_ok: score += 0.5
    if gamma2_ok: score += 0.25
    if q_ok: score += 0.25
    return score


# === block: score_1 (check id='melting_curve') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold_Tm = ctx.get("gold_Tm", {})
    densities_list = ctx.get("densities", [])
    tol_rel = 0.10
    if not rows or not gold_Tm:
        return 0.0
    tol_dens = 0.001
    count_ok = 0
    for rd in densities_list:
        found = False
        for row in rows:
            if abs(float(row.get("density_g_per_cc", 0)) - rd) < tol_dens:
                tm = float(row.get("Tm_K", 0))
                gold_tm = gold_Tm.get(str(rd), 0)
                if abs(tm - gold_tm) <= tol_rel * max(gold_tm, 1.0):
                    count_ok += 1
                found = True
                break
        if not found:
            # consider missing density as fail; no increment
            pass
    return count_ok / max(1, len(densities_list))


_SCORERS = {
    'gruneisen_params': score_0,
    'melting_curve': score_1,
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
