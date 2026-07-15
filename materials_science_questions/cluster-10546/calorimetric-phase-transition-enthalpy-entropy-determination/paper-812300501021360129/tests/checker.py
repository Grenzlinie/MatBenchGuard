import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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


# === block: score_0 (check id='scored_transition_enthalpy') ===
def score_0(artifact, step, ctx):
    fields = step.get("fields", [])
    scores = []
    for f in fields:
        val = artifact.get(f["field"])
        if val is None:
            scores.append(0.0)
        else:
            diff = abs(val - f["target"])
            tol = f["tolerance_abs"]
            scores.append(1.0 if diff <= tol else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='scored_glass_transition') ===
def score_1(artifact, step, ctx):
    fields = step.get("fields", [])
    scores = []
    for f in fields:
        val = artifact.get(f["field"])
        if val is None:
            scores.append(0.0)
        else:
            diff = abs(val - f["target"])
            tol = f["tolerance_abs"]
            scores.append(1.0 if diff <= tol else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='scored_config_entropy') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    data = artifact
    if "T" not in data[0] or "S_c" not in data[0]:
        return 0.0
    points = []
    for row in data:
        try:
            T = float(row["T"])
            Sc = float(row["S_c"])
            points.append((T, Sc))
        except:
            pass
    if len(points) == 0:
        return 0.0
    points.sort(key=lambda x: x[0])
    Trange = [p[0] for p in points]
    Sr = [p[1] for p in points]
    params = step["params"]
    # endpoint at T_trs
    idx_trs = min(range(len(Trange)), key=lambda i: abs(Trange[i] - params["T_trs"]))
    Sc_trs = Sr[idx_trs]
    score_trs = 1.0 if abs(Sc_trs - params["S_c_at_Ttrs"]) <= params["tolerance_endpoint_abs"] else 0.0
    # endpoint at Tg
    idx_tg = min(range(len(Trange)), key=lambda i: abs(Trange[i] - params["T_g"]))
    Sc_tg = Sr[idx_tg]
    score_tg = 1.0 if abs(Sc_tg - params["S_c_at_Tg"]) <= params["tolerance_endpoint_abs"] else 0.0
    # monotonic non-decreasing
    mono = all(Sr[i] >= Sr[i-1] - 1e-6 for i in range(1, len(Sr)))
    score_mono = 1.0 if mono else 0.0
    # plateau below Tg
    below_Tg = [Sr[i] for i in range(len(Trange)) if Trange[i] <= params["T_g"] - 0.5]
    if len(below_Tg) >= 2:
        plateau_var = max(below_Tg) - min(below_Tg)
        score_plateau = 1.0 if plateau_var <= params["max_variation_plateau"] else 0.0
    else:
        score_plateau = 0.0
    return 0.4*score_trs + 0.3*score_tg + 0.2*score_mono + 0.1*score_plateau


# === block: score_3 (check id='scored_residual_entropy') ===
def score_3(artifact, step, ctx):
    fields = step.get("fields", [])
    scores = []
    for f in fields:
        val = artifact.get(f["field"])
        if val is None:
            scores.append(0.0)
        else:
            diff = abs(val - f["target"])
            tol = f["tolerance_abs"]
            scores.append(1.0 if diff <= tol else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'scored_transition_enthalpy': score_0,
    'scored_glass_transition': score_1,
    'scored_config_entropy': score_2,
    'scored_residual_entropy': score_3,
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
