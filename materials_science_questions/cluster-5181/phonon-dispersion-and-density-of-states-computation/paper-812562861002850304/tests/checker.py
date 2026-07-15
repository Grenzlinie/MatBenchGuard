import os
import json
import csv

# === author imports / helpers ===
import os, json, math


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
    return {"outputs_dir": outputs_dir}


# === block: score_0 (check id='plb4_values') ===
def score_0(artifact, step, ctx):
    gold = step.get("gold", {})
    # Thermal conductivity
    tol_k = step.get("tolerances", {}).get("thermal_conductivity_abs", 1.767)
    k_agent = artifact.get("thermal_conductivity_300K")
    if k_agent is None:
        score_k = 0.0
    else:
        diff = abs(k_agent - gold.get("thermal_conductivity_300K", 0))
        if diff <= tol_k:
            score_k = 1.0
        else:
            score_k = max(0.0, 1.0 - (diff - tol_k) / (2.0 * tol_k))
    # Scattering rates
    sr_agent = artifact.get("branch_averaged_scattering_rates")
    sr_gold = gold.get("scattering_rates", {})
    score_s = 0.0
    n_s = 0
    if sr_agent and sr_gold:
        for b in ["TA1","TA2","LA","Optical"]:
            av = sr_agent.get(b)
            gv = sr_gold.get(b)
            if av is not None and gv is not None and gv != 0:
                ratio = av / gv
                if 0.5 <= ratio <= 2.0:
                    score_s += 1.0
                else:
                    dist = abs(math.log2(ratio)) - 1.0
                    score_s += max(0.0, 1.0 - dist / 5.0)
                n_s += 1
    if n_s > 0:
        score_s /= n_s
    # Group velocities
    gv_agent = artifact.get("branch_averaged_group_velocities")
    gv_gold = gold.get("group_velocities", {})
    score_v = 0.0
    n_v = 0
    if gv_agent and gv_gold:
        for b in ["TA1","TA2","LA","Optical"]:
            av = gv_agent.get(b)
            gv = gv_gold.get(b)
            if av is not None and gv is not None and gv != 0:
                ratio = av / gv
                if 0.5 <= ratio <= 1.5:
                    score_v += 1.0
                else:
                    dist = abs(math.log2(ratio))
                    score_v += max(0.0, 1.0 - dist / 5.0)
                n_v += 1
    if n_v > 0:
        score_v /= n_v
    # Combine
    total = (score_k + score_s + score_v) / 3.0
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='plb8_values') ===
def score_1(artifact, step, ctx):
    gold = step.get("gold", {})
    tol_k = step.get("tolerances", {}).get("thermal_conductivity_abs", 2.0)
    k_agent = artifact.get("thermal_conductivity_300K")
    if k_agent is None:
        score_k = 0.0
    else:
        diff = abs(k_agent - gold.get("thermal_conductivity_300K", 0))
        if diff <= tol_k:
            score_k = 1.0
        else:
            score_k = max(0.0, 1.0 - (diff - tol_k) / (2.0 * tol_k))
    sr_agent = artifact.get("branch_averaged_scattering_rates")
    sr_gold = gold.get("scattering_rates", {})
    score_s = 0.0
    n_s = 0
    if sr_agent and sr_gold:
        for b in ["TA1","TA2","LA","Optical"]:
            av = sr_agent.get(b)
            gv = sr_gold.get(b)
            if av is not None and gv is not None and gv != 0:
                ratio = av / gv
                if 0.5 <= ratio <= 2.0:
                    score_s += 1.0
                else:
                    dist = abs(math.log2(ratio)) - 1.0
                    score_s += max(0.0, 1.0 - dist / 5.0)
                n_s += 1
    if n_s > 0:
        score_s /= n_s
    gv_agent = artifact.get("branch_averaged_group_velocities")
    gv_gold = gold.get("group_velocities", {})
    score_v = 0.0
    n_v = 0
    if gv_agent and gv_gold:
        for b in ["TA1","TA2","LA","Optical"]:
            av = gv_agent.get(b)
            gv = gv_gold.get(b)
            if av is not None and gv is not None and gv != 0:
                ratio = av / gv
                if 0.5 <= ratio <= 1.5:
                    score_v += 1.0
                else:
                    dist = abs(math.log2(ratio))
                    score_v += max(0.0, 1.0 - dist / 5.0)
                n_v += 1
    if n_v > 0:
        score_v /= n_v
    total = (score_k + score_s + score_v) / 3.0
    return max(0.0, min(1.0, total))


# === block: score_2 (check id='trends') ===
def score_2(artifact, step, ctx):
    outputs_dir = ctx.get("outputs_dir", "/app/outputs")
    try:
        with open(os.path.join(outputs_dir, "step_04_results_PL-B8.json")) as f:
            plb8 = json.load(f)
    except Exception:
        return 0.0
    plb4 = artifact
    if not (plb4 and plb8):
        return 0.0
    k4 = plb4.get("thermal_conductivity_300K")
    k8 = plb8.get("thermal_conductivity_300K")
    sr4 = plb4.get("branch_averaged_scattering_rates", {})
    sr8 = plb8.get("branch_averaged_scattering_rates", {})
    points = 0
    if k4 is not None and k8 is not None and k4 < k8:
        points += 1
    acoustic_branches = ["TA1","TA2","LA"]
    for b in acoustic_branches:
        v4 = sr4.get(b)
        v8 = sr8.get(b)
        if v4 is not None and v8 is not None and v8 > 0 and v4 >= 2.0 * v8:
            points += 1
    v4_opt = sr4.get("Optical")
    v8_opt = sr8.get("Optical")
    if v4_opt is not None and v8_opt is not None and v8_opt > 0 and v4_opt >= 5.0 * v8_opt:
        points += 1
    return float(points) / 5.0


_SCORERS = {
    'plb4_values': score_0,
    'plb8_values': score_1,
    'trends': score_2,
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
