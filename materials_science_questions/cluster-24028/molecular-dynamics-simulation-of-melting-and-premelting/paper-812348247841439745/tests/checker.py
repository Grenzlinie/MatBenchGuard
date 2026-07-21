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
    return {}


# === block: score_0 (check id='step4_nanowire_diff') ===
def score_0(artifact, step, ctx):
    import csv
    import io

    params = step.get("params", {})
    assemblies = params.get("assemblies", [])
    temps_expected = params.get("temperatures", [])
    low_T_max = float(params.get("low_T_max", 0.02))
    high_T_min = float(params.get("high_T_min", 0.005))

    if not artifact or len(artifact) == 0:
        return 0.0

    # Build dict from artifact rows
    rows_by_key = {}
    for row in artifact:
        assem = str(row.get("assembly", "")).strip()
        try:
            temp = int(float(row.get("temperature", 0)))
        except:
            continue
        try:
            d_val = float(row.get("diffusion_coefficient", 0))
        except:
            continue
        rows_by_key[(assem, temp)] = d_val

    # Per-temperature scoring (unchanged logic)
    per_temp_scores = []
    assem_temps = {a: [] for a in assemblies}
    for assem in assemblies:
        for temp in temps_expected:
            key = (assem, temp)
            s = 0.0
            if key in rows_by_key:
                d = rows_by_key[key]
                if d < 0:
                    s = 0.0
                elif temp <= 800:
                    if d <= low_T_max:
                        s = 1.0
                    elif d <= 5 * low_T_max:
                        s = 0.5
                    else:
                        s = 0.0
                elif temp >= 1000:
                    if d >= high_T_min:
                        s = 1.0
                    elif d >= 0.1 * high_T_min:
                        s = 0.5
                    else:
                        s = 0.0
                else:  # 900 K
                    if d < 0:
                        s = 0.0
                    elif d > 10 * low_T_max:
                        s = 0.5
                    else:
                        s = 1.0
            per_temp_scores.append(s)
            assem_temps[assem].append(s)

    # Baseline average
    if not per_temp_scores:
        return 0.0
    base_avg = sum(per_temp_scores) / len(per_temp_scores)

    # Trend penalty: for each assembly, D(1400 K) must be at least 20x D(800 K)
    target_ratio = 20.0
    assembly_factors = []
    for assem in assemblies:
        key_low = (assem, 800)
        key_high = (assem, 1400)
        if key_low not in rows_by_key or key_high not in rows_by_key:
            # cannot evaluate trend, assume no penalty
            assembly_factors.append(1.0)
            continue
        d_low = rows_by_key[key_low]
        d_high = rows_by_key[key_high]
        if d_low <= 0 or d_high <= 0:
            assembly_factors.append(0.0)  # negative/zero D is invalid, full penalty
        else:
            ratio = d_high / d_low
            factor = min(ratio / target_ratio, 1.0)
            assembly_factors.append(factor)

    # Per-assembly average after trend penalty
    final_score = 0.0
    if assemblies:
        assembly_scores = []
        for i, assem in enumerate(assemblies):
            assay_scores = assem_temps[assem]
            if assay_scores:
                avg = sum(assay_scores) / len(assay_scores)
                assembly_scores.append(avg * assembly_factors[i])
        if assembly_scores:
            final_score = sum(assembly_scores) / len(assembly_scores)

    return min(max(final_score, 0.0), 1.0)


# === block: score_1 (check id='step5_nanofilm_planarity') ===
def score_1(artifact, step, ctx):
    params = step.get("params", {})
    assemblies = params.get("assemblies", [])
    temps_expected = params.get("temperatures", [])
    stable_min = float(params.get("stable_min", 1.5))
    collapse_max = float(params.get("collapse_max", 2.0))
    stable_max_T = float(params.get("stable_range_max_T", 1000))
    collapse_min_T = float(params.get("collapse_range_min_T", 1100))

    if not artifact or len(artifact) == 0:
        return 0.0

    rows_by_key = {}
    for row in artifact:
        assem = str(row.get("assembly", "")).strip()
        try:
            temp = int(float(row.get("temperature", 0)))
        except:
            continue
        try:
            ratio = float(row.get("planarity_ratio", 0))
        except:
            continue
        rows_by_key[(assem, temp)] = ratio

    scores = []
    for assem in assemblies:
        for temp in temps_expected:
            key = (assem, temp)
            if key not in rows_by_key:
                scores.append(0.0)
                continue
            r = rows_by_key[key]
            if temp <= stable_max_T:
                if r >= stable_min:
                    s = 1.0
                elif r >= stable_min * 0.6:
                    s = 0.5
                else:
                    s = 0.0
            elif temp >= collapse_min_T:
                if r <= collapse_max:
                    s = 1.0
                elif r <= 1.5 * collapse_max:
                    s = 0.5
                else:
                    s = 0.0
            else:
                # intermediate temperature not strictly specified
                s = 1.0 if r > 0 else 0.0
            scores.append(s)

    if not scores:
        return 0.0
    avg = sum(scores) / len(scores)
    return min(max(avg, 0.0), 1.0)


_SCORERS = {
    'step4_nanowire_diff': score_0,
    'step5_nanofilm_planarity': score_1,
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
