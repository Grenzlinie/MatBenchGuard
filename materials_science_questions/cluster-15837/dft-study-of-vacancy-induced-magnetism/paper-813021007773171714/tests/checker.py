import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math, statistics
from collections import defaultdict


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
        ctx[step["id"]] = step.get("parameters", {})
    return ctx


# === block: score_0 (check id='adsorption_summary') ===
def score_0(artifact, step, ctx):
    params = ctx.get("adsorption_summary", {})
    gold = params.get("gold", {})
    tolerances = params.get("tolerances", {})
    if not isinstance(artifact, list):
        return 0.0
    fields = ["adsorption_energy_kcal_mol", "binding_energy_kcal_mol", "distance_angstrom", "D_minus_EF_eV", "doping_type"]
    total_points = 0.0
    max_points = 0.0
    for entry in artifact:
        name = entry.get("system_name")
        if name not in gold:
            continue
        g = gold[name]
        for field in fields:
            # pristine graphene doping type is not defined in the paper; skip this field for that system
            if name == "pristine graphene" and field == "doping_type":
                continue
            max_points += 1.0
            if field == "doping_type":
                if entry.get(field) == g[field]:
                    total_points += 1.0
            else:
                val = entry.get(field)
                target = g[field]
                tol = tolerances.get(field, 0.2)
                if val is None:
                    continue
                diff = abs(val - target)
                if diff <= tol:
                    total_points += 1.0
                elif diff <= 2 * tol:
                    total_points += 0.5
    if max_points == 0:
        return 0.0
    return total_points / max_points


# === block: score_1 (check id='defect_displacement') ===
def score_1(artifact, step, ctx):
    params = ctx.get("defect_displacement", {})
    ranges = params.get("ranges", {})
    ordering = params.get("ordering", [])
    last_frac = params.get("last_fraction", 0.5)
    sys_weight = params.get("system_range_weight", 0.2)
    ord_weight = params.get("ordering_weight", 0.2)
    sys_data = defaultdict(list)
    for row in artifact:
        sys_data[row["system"]].append((float(row["timestep_fs"]), float(row["displacement_angstrom"])))
    means = {}
    for sys_name, points in sys_data.items():
        points_sorted = sorted(points, key=lambda x: x[0])
        if not points_sorted:
            continue
        max_t = points_sorted[-1][0]
        threshold = max_t * (1 - last_frac) if last_frac < 1 else 0
        subset = [d for t, d in points_sorted if t >= threshold]
        if not subset:
            continue
        means[sys_name] = statistics.mean(subset)
    score = 0.0
    for sys_name, rng in ranges.items():
        if sys_name in means:
            val = means[sys_name]
            if rng[0] <= val <= rng[1]:
                score += sys_weight
    if ordering and all(s in means for s in ordering):
        ord_vals = [means[s] for s in ordering]
        if all(ord_vals[i] <= ord_vals[i+1] for i in range(len(ord_vals)-1)):
            score += ord_weight
    return min(score, 1.0)


# === block: score_2 (check id='rmsd') ===
def score_2(artifact, step, ctx):
    params = ctx.get("rmsd", {})
    ranges = params.get("ranges", {})
    ordering = params.get("ordering", [])
    last_frac = params.get("last_fraction", 0.5)
    sys_weight = params.get("system_range_weight", 0.2)
    ord_weight = params.get("ordering_weight", 0.2)
    sys_data = defaultdict(list)
    for row in artifact:
        sys_data[row["system"]].append((float(row["timestep_fs"]), float(row["rmsd_angstrom"])))
    means = {}
    for sys_name, points in sys_data.items():
        points_sorted = sorted(points, key=lambda x: x[0])
        if not points_sorted:
            continue
        max_t = points_sorted[-1][0]
        threshold = max_t * (1 - last_frac) if last_frac < 1 else 0
        subset = [d for t, d in points_sorted if t >= threshold]
        if not subset:
            continue
        means[sys_name] = statistics.mean(subset)
    score = 0.0
    for sys_name, rng in ranges.items():
        if sys_name in means:
            val = means[sys_name]
            if rng[0] <= val <= rng[1]:
                score += sys_weight
    if ordering and all(s in means for s in ordering):
        ord_vals = [means[s] for s in ordering]
        if all(ord_vals[i] <= ord_vals[i+1] for i in range(len(ord_vals)-1)):
            score += ord_weight
    return min(score, 1.0)


_SCORERS = {
    'adsorption_summary': score_0,
    'defect_displacement': score_1,
    'rmsd': score_2,
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
