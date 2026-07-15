import os
import json
import csv

# === author imports / helpers ===
import math

def find_peaks(energies, values, min_rel_height=0.05, window=1):
    n = len(values)
    if n == 0:
        return []
    max_val = max(values)
    thresh = min_rel_height * max_val
    peaks = []
    for i in range(n):
        left = max(0, i - window)
        right = min(n, i + window + 1)
        if values[i] >= thresh and all(values[i] >= values[j] for j in range(left, right) if j != i):
            peaks.append((energies[i], values[i]))
    return peaks


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


# === block: score_0 (check id='band_properties') ===
def score_0(artifact, step, ctx):
    spec = ctx["spec"]
    step = [s for s in spec["steps"] if s["id"] == "band_properties"][0]
    gold = step["gold"]
    # build list of test cases (compound, field, target, tol)
    tests = []
    for comp in ["Li2CO3", "Na2CO3"]:
        if comp not in gold:
            continue
        for field, info in gold[comp].items():
            tests.append((comp, field, info["value"], info["tol"]))
    # compute passes
    passes = 0
    for comp, field, target, tol in tests:
        if comp not in artifact or not isinstance(artifact[comp], dict):
            continue
        agent_val = artifact[comp].get(field)
        if isinstance(agent_val, (int, float)):
            if abs(agent_val - target) <= tol:
                passes += 1
    numeric_score = passes / len(tests) if tests else 0.0
    # trend check
    trend_pass = 0.0
    try:
        li_gap = float(artifact["Li2CO3"].get("band_gap_eV", 0))
        na_gap = float(artifact["Na2CO3"].get("band_gap_eV", 0))
        if li_gap > na_gap:
            trend_pass = 1.0
    except:
        pass
    trend_weight = step.get("trend_weight", 0.1)
    score = numeric_score * (1 - trend_weight) + trend_pass * trend_weight
    return score


# === block: score_1 (check id='eps2_spectra') ===
def score_1(artifact, step, ctx):
    spec = ctx["spec"]
    step = [s for s in spec["steps"] if s["id"] == "eps2_spectra"][0]
    gold_peaks = step["gold_peaks"]
    tolerance = step["tolerance_ev"]
    ordering = step.get("intensity_ordering", [])
    # artifact is list of dicts
    if not artifact:
        return 0.0
    energy_col = "Energy_eV"
    compound_cols = {
        "Li2CO3": "eps2_Li2CO3",
        "Na2CO3": "eps2_Na2CO3",
        "K2CO3": "eps2_K2CO3",
        "LiKCO3": "eps2_LiKCO3"
    }
    energies = []
    for row in artifact:
        try:
            e = float(row.get(energy_col, 0))
        except:
            e = 0.0
        energies.append(e)
    # compute match score per compound
    compound_scores = []
    matched_peaks_all = {}
    for comp, expected_list in gold_peaks.items():
        col = compound_cols.get(comp)
        if not col:
            continue
        values = []
        for row in artifact:
            try:
                v = float(row.get(col, 0))
            except:
                v = 0.0
            values.append(v)
        if not values:
            continue
        peaks = find_peaks(energies, values, min_rel_height=0.05, window=1)
        matched = 0
        matched_peaks = []
        for ep in expected_list:
            best = None
            best_dist = None
            for pk_e, pk_v in peaks:
                dist = abs(pk_e - ep)
                if dist <= tolerance:
                    if best is None or dist < best_dist:
                        best = (pk_e, pk_v)
                        best_dist = dist
            if best is not None:
                matched += 1
                matched_peaks.append(best)
        matched_peaks_all[comp] = matched_peaks
        compound_scores.append(matched / len(expected_list) if expected_list else 1.0)
    if not compound_scores:
        peak_match_score = 0.0
    else:
        peak_match_score = sum(compound_scores) / len(compound_scores)
    # intensity ordering check
    ordering_score = 0.0
    if ordering:
        for rule in ordering:
            comp = rule["compound"]
            first_pos = rule["first_peak_pos"]
            second_pos = rule["second_peak_pos"]
            relation = rule.get("relation", "less")
            peaks_comp = matched_peaks_all.get(comp, [])
            first_val = None
            second_val = None
            for pk_e, pk_v in peaks_comp:
                if abs(pk_e - first_pos) <= tolerance:
                    first_val = pk_v
                if abs(pk_e - second_pos) <= tolerance:
                    second_val = pk_v
            if first_val is not None and second_val is not None:
                if relation == "less" and first_val < second_val:
                    ordering_score = 1.0
                elif relation == "greater" and first_val > second_val:
                    ordering_score = 1.0
    # combine: 0.9 peak match, 0.1 intensity ordering
    score = 0.9 * peak_match_score + 0.1 * ordering_score
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'band_properties': score_0,
    'eps2_spectra': score_1,
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
