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
    import json
    import csv

    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        gold = {}
        for step in steps:
            if step["id"] == "roton_counts":
                gold_dict = step.get("params", {}).get("gold", {})
                gold = {int(k): int(v) for k, v in gold_dict.items()}
                break
        return {"gold": gold}


# === block: score_0 (check id='dispersion_structural') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0

    expected_groups = {3, 10, 15}
    min_points = step.get("params", {}).get("min_points_per_g", 100)
    q_min = float(step.get("params", {}).get("q_min", 0.0))
    q_max = float(step.get("params", {}).get("q_max", 6.0))

    from collections import defaultdict
    points_per_g = defaultdict(int)
    q_in_range = True
    for row in artifact:
        g = int(row["g"])
        qx = float(row["q_x"])
        points_per_g[g] += 1
        if qx < q_min - 1e-9 or qx > q_max + 1e-9:
            q_in_range = False

    all_present = all(g in points_per_g for g in expected_groups)
    enough = all(points_per_g[g] >= min_points for g in expected_groups)

    if all_present and enough and q_in_range:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='roton_counts') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0

    import csv
    import os

    dispersion_path = os.path.join("/app/outputs", "step_03_dispersion.csv")
    if not os.path.exists(dispersion_path):
        return 0.0

    disp_data = {}
    with open(dispersion_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            g = int(row["g"])
            qx = float(row["q_x"])
            omega = float(row["omega_lowest"])
            disp_data.setdefault(g, []).append((qx, omega))

    def count_minima(points, ignore_q=0.0):
        sorted_pts = sorted(points)
        minima = 0
        for i in range(1, len(sorted_pts)-1):
            q, val = sorted_pts[i]
            if abs(q - ignore_q) < 1e-9:
                continue
            if val < sorted_pts[i-1][1] and val < sorted_pts[i+1][1]:
                minima += 1
        return minima

    target_g = [3, 10, 15]
    disp_minima = {}
    for g in target_g:
        pts = disp_data.get(g, [])
        if not pts:
            disp_minima[g] = -1
        else:
            disp_minima[g] = count_minima(pts)

    agent_counts = {}
    for row in artifact:
        g = int(row["g"])
        agent_counts[g] = int(row["num_minima"])

    gold = ctx["gold"]
    exact_ok = all(agent_counts.get(g) == gold.get(g) for g in target_g)
    exact_score = 1.0 if exact_ok else 0.0

    consistency_ok = all(agent_counts.get(g) == disp_minima.get(g) for g in target_g) and all(disp_minima[g] >= 0 for g in target_g)
    consistency_score = 1.0 if consistency_ok else 0.0

    final = 0.9 * exact_score + 0.1 * consistency_score
    return final


_SCORERS = {
    'dispersion_structural': score_0,
    'roton_counts': score_1,
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
