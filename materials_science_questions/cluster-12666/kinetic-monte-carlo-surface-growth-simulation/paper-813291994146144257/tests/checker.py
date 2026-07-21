import os
import json
import csv

# === author imports / helpers ===
import os


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
    return {"output_dir": "/app/outputs", "target_density": 35.0}


# === block: score_0 (check id='step_kmc_sim') ===
def score_0(artifact, step, ctx):
    entries = artifact if isinstance(artifact, list) else []
    if len(entries) != 6:
        return 0.0
    required_keys = {'critical_island_size', 'island_density_per_um2'}
    seen = set()
    densities = {}
    for e in entries:
        if not isinstance(e, dict):
            return 0.0
        if not required_keys.issubset(e.keys()):
            return 0.0
        i = e['critical_island_size']
        if not isinstance(i, int) or i < 3 or i > 8:
            return 0.0
        if i in seen:
            return 0.0
        seen.add(i)
        d = e['island_density_per_um2']
        if not isinstance(d, (int, float)) or d <= 0:
            return 0.0
        densities[i] = d
    if len(seen) != 6:
        return 0.0
    # use tolerance declared in grading_spec; fallback to 0.01 if missing
    tol_frac = float(step.get("tolerance", 0.01))
    max_den = max(densities.values())
    eps = max(tol_frac * max_den, 1e-9)
    num_steps = 0
    num_decreasing = 0
    for i in (3,4,5,6,7):
        if i in densities and (i+1) in densities:
            if densities[i] >= densities[i+1] - eps:
                num_decreasing += 1
            num_steps += 1
    score = 0.4
    if num_steps > 0:
        score += 0.6 * (num_decreasing / num_steps)
    return min(1.0, score)


# === block: score_1 (check id='step_select_i') ===
def score_1(artifact, step, ctx):
    import os
    output_dir = step.get("output_dir", ctx.get("output_dir", "/app/outputs"))
    target_density = ctx["target_density"]
    # load island_density_vs_i.json
    import json
    density_path = os.path.join(output_dir, "island_density_vs_i.json")
    try:
        with open(density_path, 'r') as f:
            entries = json.load(f)
    except Exception:
        return 0.0
    if not isinstance(entries, list) or len(entries) != 6:
        return 0.0
    densities = {}
    for e in entries:
        if isinstance(e, dict) and 'critical_island_size' in e and 'island_density_per_um2' in e:
            i = e['critical_island_size']
            d = e['island_density_per_um2']
            if isinstance(i, int) and isinstance(d, (int, float)):
                densities[i] = d
    if len(densities) != 6:
        return 0.0
    # find best i (smallest absolute difference, tie break smallest i)
    best_i = None
    best_diff = float('inf')
    for i, d in densities.items():
        diff = abs(d - target_density)
        if diff < best_diff or (diff == best_diff and (best_i is None or i < best_i)):
            best_diff = diff
            best_i = i
    # parse selected_critical_island_size.txt
    try:
        sel_content = artifact.strip()
        sel_i = int(sel_content)
    except Exception:
        return 0.0
    if best_i is None:
        return 0.0
    # scoring
    if best_i == 7 and sel_i == 7:
        return 1.0
    elif sel_i == best_i:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'step_kmc_sim': score_0,
    'step_select_i': score_1,
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
