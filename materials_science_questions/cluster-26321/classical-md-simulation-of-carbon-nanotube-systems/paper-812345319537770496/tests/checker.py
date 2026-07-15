import os
import json
import csv

# === author imports / helpers ===
import json
import os
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
    ctx = {}
    for step in spec.get("steps", []):
        if step["id"] == "step04_score":
            ctx["step04_score"] = {
                "target_transition": step["target_transition_aspect_ratio"],
                "tol_transition": step["tol_transition"],
                "min_curve_points": step["min_curve_points"],
                "strain_range": step["strain_range"],
                "aspect_ratio_range": step["aspect_ratio_range"]
            }
    return ctx


# === block: score_0 (check id='step03_score') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) < 3:
        return 0.0

    labels_expected = step.get("expected_labels", [])
    strain_range = step.get("strain_range", [0.01, 0.5])
    min_d = step.get("min_diameter_nm", 0.3)
    max_d = step.get("max_diameter_nm", 3.5)

    data = []
    for item in artifact:
        if not all(k in item for k in ("tube_label","diameter_nm","critical_strain")):
            continue
        label = str(item["tube_label"])
        d = float(item["diameter_nm"])
        eps = float(item["critical_strain"])
        if d < min_d or d > max_d or eps < strain_range[0] or eps > strain_range[1]:
            continue
        data.append({"label": label, "d": d, "eps": eps})

    # require exactly the three requested tubes
    if len(data) != 3 or set([x["label"] for x in data]) != set(labels_expected):
        return 0.0

    # sort by diameter increasing
    data.sort(key=lambda x: x["d"])
    eps_vals = [x["eps"] for x in data]
    d_vals = [x["d"] for x in data]

    # check monotonic non-increasing (allow tiny float noise)
    mono_ok = all(eps_vals[i] <= eps_vals[i-1] + 1e-9 for i in range(1, len(eps_vals)))
    mono_score = 0.3 if mono_ok else 0.0

    # compute product eps*d and coefficient of variation
    products = [eps_vals[i] * d_vals[i] for i in range(len(eps_vals))]
    mean_p = sum(products) / len(products)
    std_p = math.sqrt(sum((p - mean_p) ** 2 for p in products) / len(products))
    cv = std_p / mean_p if mean_p > 0 else 1.0
    if cv <= 0.05:
        product_score = 0.6
    elif cv <= 0.2:
        product_score = 0.6 * (1.0 - (cv - 0.05) / 0.15)
    else:
        product_score = 0.0

    base_score = 0.1  # structural existence
    return min(1.0, base_score + product_score + mono_score)


# === block: score_1 (check id='step04_score') ===
def score_1(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, dict):
        return 0.0

    curve = artifact.get("curve")
    if not isinstance(curve, list):
        return 0.0
    transition = artifact.get("transition_aspect_ratio")
    if transition is None:
        return 0.0
    transition = float(transition)

    cfg = ctx.get("step04_score", {})
    target_transition = cfg.get("target_transition", 12.5)
    tol_transition = cfg.get("tol_transition", 3.0)
    min_points = cfg.get("min_curve_points", 5)
    strain_range = cfg.get("strain_range", [0.001, 0.5])
    ar_range = cfg.get("aspect_ratio_range", [4.0, 35.0])

    # basic curve validity
    valid_points = []
    for pt in curve:
        if not isinstance(pt, dict):
            continue
        ar = pt.get("aspect_ratio")
        eps = pt.get("critical_strain")
        if ar is None or eps is None:
            continue
        ar = float(ar)
        eps = float(eps)
        if ar < ar_range[0] or ar > ar_range[1] or eps < strain_range[0] or eps > strain_range[1]:
            continue
        valid_points.append({"ar": ar, "eps": eps})

    if len(valid_points) < min_points:
        return 0.0

    # ensure aspect ratios are strictly increasing (allow tiny noise)
    for i in range(1, len(valid_points)):
        if valid_points[i]["ar"] <= valid_points[i-1]["ar"] - 1e-9:
            return 0.0

    # find index of maximum critical strain
    max_idx = max(range(len(valid_points)), key=lambda i: valid_points[i]["eps"])
    max_ar = valid_points[max_idx]["ar"]

    # curve shape score: after max, critical strain non-increasing (allow small tolerance 1e-6)
    post_peak_ok = True
    for i in range(max_idx + 1, len(valid_points)):
        if valid_points[i]["eps"] > valid_points[i-1]["eps"] + 1e-6:
            post_peak_ok = False
            break
    shape_score = 0.4 if post_peak_ok and max_idx > 0 else 0.0  # also require max not at edge

    # consistency: reported transition should be close to ar at max point
    diff_max_ar = abs(transition - max_ar)
    consistency_score = 0.3 if diff_max_ar <= 1.0 else 0.3 * max(0.0, 1.0 - (diff_max_ar - 1.0) / 2.0)

    # absolute gold match
    diff_target = abs(transition - target_transition)
    if diff_target <= tol_transition:
        gold_score = 0.3
    else:
        gold_score = 0.3 * max(0.0, 1.0 - (diff_target - tol_transition) / (2 * tol_transition))

    return min(1.0, shape_score + consistency_score + gold_score)


_SCORERS = {
    'step03_score': score_0,
    'step04_score': score_1,
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
