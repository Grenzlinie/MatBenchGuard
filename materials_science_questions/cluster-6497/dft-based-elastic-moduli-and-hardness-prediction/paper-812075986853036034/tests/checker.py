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
    return {
        "gold_xi": -0.001,
        "tol_xi": 0.002,
        "gold_eta": 0.03,
        "tol_eta": 0.02,
        "gold_chi": 0.08,
        "tol_chi": 0.01,
        "gold_helices": [
            {"id": 1, "r0": 342, "p": 222, "t_min": 12.4, "t_max": 12.5, "F_norm": -1.1},
            {"id": 2, "r0": 175, "p": 133, "t_min": 8.5, "t_max": 8.6, "F_norm": -0.6},
            {"id": 3, "r0": 240, "p": 380, "t_min": 9.6, "t_max": 9.8, "F_norm": -0.7}
        ]
    }


# === block: score_0 (check id='step_01_fit_nanoring') ===
def score_0(artifact, step, ctx):
    xi = artifact.get("xi")
    eta = artifact.get("eta")
    chi = artifact.get("chi")
    if xi is None or eta is None or chi is None:
        return 0.0
    s_xi = 1.0 if abs(xi - ctx["gold_xi"]) <= ctx["tol_xi"] else 0.0
    s_eta = 1.0 if abs(eta - ctx["gold_eta"]) <= ctx["tol_eta"] else 0.0
    s_chi = 1.0 if abs(chi - ctx["gold_chi"]) <= ctx["tol_chi"] else 0.0
    return (s_xi + s_eta + s_chi) / 3.0


# === block: score_1 (check id='step_02_predict_helices') ===
def score_1(artifact, step, ctx):
    gold_helices = ctx["gold_helices"]
    if not isinstance(artifact, list):
        return 0.0
    gold_map = {h["id"]: h for h in gold_helices}
    scores = []
    for helix in artifact:
        hid = helix.get("helix_id")
        if hid not in gold_map:
            continue
        g = gold_map[hid]
        t_min = helix.get("t_min")
        t_max = helix.get("t_max")
        F_norm = helix.get("F_norm")
        if t_min is None or t_max is None or F_norm is None:
            score_h = 0.0
        else:
            s_tmin = 1.0 if abs(t_min - g["t_min"]) <= 0.5 else 0.0
            s_tmax = 1.0 if abs(t_max - g["t_max"]) <= 0.5 else 0.0
            s_F = 1.0 if abs(F_norm - g["F_norm"]) <= 0.2 else 0.0
            score_h = (s_tmin + s_tmax + s_F) / 3.0
        scores.append(score_h)
    if len(scores) != len(gold_helices):
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_01_fit_nanoring': score_0,
    'step_02_predict_helices': score_1,
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
