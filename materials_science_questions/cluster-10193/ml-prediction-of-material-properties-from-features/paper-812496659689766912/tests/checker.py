import os
import json
import csv

# === author imports / helpers ===
import statistics

def lower_better_score(recomputed, gold, rel_tol=0.20, abs_tol=0.5):
    if recomputed <= gold + 1e-9:
        return 1.0
    eps = max(gold * rel_tol, abs_tol)
    if recomputed <= gold + eps:
        return max(0.0, 1.0 - (recomputed - gold) / eps)
    return 0.0


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
    return {"spec": spec}


# === block: score_0 (check id='check_bond_stretch_counts') ===
def score_0(artifact, step, ctx):
    rows = artifact
    params = step["params"]
    gold = params["gold"]
    tolerance = params["tolerance"]
    sums = {}
    for row in rows:
        method = row.get("method", "").strip()
        if not method:
            continue
        sums.setdefault(method, {"r0_correct": 0, "repulsive_wall_correct": 0, "attractive_forces_correct": 0, "spurious_minima": 0})
        for col in ["r0_correct", "repulsive_wall_correct", "attractive_forces_correct", "spurious_minima"]:
            try:
                val = int(row.get(col, 0))
            except (ValueError, TypeError):
                val = 0
            sums[method][col] += val

    criteria = ["r0_correct", "repulsive_wall_correct", "attractive_forces_correct", "spurious_minima"]
    total = 0.0
    count = 0
    for method, gold_dict in gold.items():
        if method not in sums:
            for col in criteria:
                count += 1
            continue
        for col in criteria:
            diff = abs(sums[method].get(col, 0) - gold_dict.get(col, 0))
            total += 1.0 if diff <= tolerance else 0.0
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_1 (check id='check_bond_stretch_mape') ===
def score_1(artifact, step, ctx):
    rows = artifact
    params = step["params"]
    gold = params["gold"]
    rel_tol = params["relative_tolerance"]

    mape_by_method = {}
    for row in rows:
        method = row.get("method", "").strip()
        try:
            mape = float(row.get("median_MAPE", 0.0))
        except (ValueError, TypeError):
            mape = None
        if method and mape is not None:
            mape_by_method.setdefault(method, []).append(mape)

    scores = []
    for method, g in gold.items():
        if method not in mape_by_method or not mape_by_method[method]:
            scores.append(0.0)
            continue
        median_mape = statistics.median(mape_by_method[method])
        scores.append(lower_better_score(median_mape, g, rel_tol=rel_tol, abs_tol=0.0))

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='check_dihedral_summary') ===
def score_2(artifact, step, ctx):
    rows = artifact
    params = step["params"]
    gold = params["gold"]
    tol_theta = params["tolerances"]["theta0_deg"]
    tol_barrier = params["tolerances"]["barrier_energy_kcal_per_mol"]["relative"]

    gold_map = {}
    for g in gold:
        key = (g["molecule"], g["method"])
        gold_map[key] = g

    scores = []
    for row in rows:
        mol = row.get("molecule", "").strip()
        method = row.get("method", "").strip()
        key = (mol, method)
        if key not in gold_map:
            continue
        g = gold_map[key]
        try:
            theta = float(row.get("theta0_deg", 0))
            barrier = float(row.get("barrier_energy_kcal_per_mol", 0))
        except (ValueError, TypeError):
            scores.append(0.0)
            continue
        theta_ok = abs(theta - g["theta0_deg"]) <= tol_theta
        g_barrier = float(g["barrier_energy_kcal_per_mol"])
        if g_barrier == 0.0:
            barrier_ok = abs(barrier) <= tol_barrier * 0.0 + 1e-6
        else:
            barrier_ok = abs(barrier - g_barrier) / abs(g_barrier) <= tol_barrier
        scores.append(1.0 if (theta_ok and barrier_ok) else 0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='check_torsion_2d_mae') ===
def score_3(artifact, step, ctx):
    rows = artifact
    params = step["params"]
    gold = params["gold"]
    rel_tol = params["relative_tolerance"]
    abs_tol = params["abs_tolerance"]

    gold_map = {}
    for g in gold:
        key = (g["molecule"], g["method"])
        gold_map[key] = g["MAE_kcal_per_mol"]

    scores = []
    for row in rows:
        mol = row.get("molecule", "").strip()
        method = row.get("method", "").strip()
        key = (mol, method)
        if key not in gold_map:
            continue
        try:
            mae = float(row.get("MAE_kcal_per_mol", 0.0))
        except (ValueError, TypeError):
            scores.append(0.0)
            continue
        scores.append(lower_better_score(mae, gold_map[key], rel_tol=rel_tol, abs_tol=abs_tol))

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'check_bond_stretch_counts': score_0,
    'check_bond_stretch_mape': score_1,
    'check_dihedral_summary': score_2,
    'check_torsion_2d_mae': score_3,
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
