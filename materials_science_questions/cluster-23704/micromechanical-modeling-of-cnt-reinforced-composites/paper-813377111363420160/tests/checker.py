import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='step_stress_strain') ===
def score_0(artifact, step, ctx):
    import csv, math

    # Digitized reference curve from Fig. 4 (25 CNTs, proposed method)
    ref_curve = [
        (0.0, 0.0), (0.005, 0.043), (0.01, 0.086), (0.015, 0.129),
        (0.02, 0.172), (0.025, 0.215), (0.03, 0.258), (0.035, 0.301),
        (0.04, 0.344), (0.045, 0.387), (0.05, 0.430)
    ]
    threshold = float(step.get('threshold_rmse_gpa', 0.5))
    decay_cutoff = float(step.get('decay_cutoff_factor', 1.0)) * threshold
    if decay_cutoff <= threshold:
        decay_cutoff = 2.0 * threshold

    strains = []
    stresses = []
    try:
        for row in artifact:
            s = float(row['strain'])
            sigma = float(row['stress'])
            strains.append(s)
            stresses.append(sigma)
    except Exception:
        return 0.0

    if not strains:
        return 0.0

    sum_sq = 0.0
    valid = 0
    for ref_s, ref_sigma in ref_curve:
        if ref_s < strains[0] or ref_s > strains[-1]:
            continue
        # find first index where strain >= ref_s
        idx = None
        for i, s_val in enumerate(strains):
            if s_val >= ref_s:
                idx = i
                break
        if idx is None:
            continue
        if idx == 0:
            interp_sigma = stresses[0]
        else:
            s0, sigma0 = strains[idx-1], stresses[idx-1]
            s1, sigma1 = strains[idx], stresses[idx]
            if s1 == s0:
                interp_sigma = sigma0
            else:
                interp_sigma = sigma0 + (ref_s - s0) * (sigma1 - sigma0) / (s1 - s0)
        sum_sq += (interp_sigma - ref_sigma) ** 2
        valid += 1

    if valid == 0:
        return 0.0

    rmse = math.sqrt(sum_sq / valid)

    if rmse <= threshold:
        return 1.0
    else:
        score = max(0.0, 1.0 - (rmse - threshold) / (decay_cutoff - threshold))
        return score


# === block: score_1 (check id='step_young_modulus') ===
def score_1(artifact, step, ctx):
    import csv

    gold_mod = float(step.get('reference_modulus_gpa', 8.6))
    tol = float(step.get('relative_tolerance', 0.15))
    counts = set(int(x) for x in step.get('expected_counts', [50,200,800,1000]))

    rows = []
    for row in artifact:
        try:
            n = int(row['num_cnts'])
            mod = float(row['young_modulus_gpa'])
            rows.append((n, mod))
        except Exception:
            continue

    if not rows:
        return 0.0

    scores = []
    for n, val in rows:
        if n in counts:
            rel_err = abs((val - gold_mod) / gold_mod)
            if rel_err <= tol:
                scores.append(1.0)
            else:
                s = max(0.0, 1.0 - (rel_err - tol) / tol)
                scores.append(s)
        else:
            scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_order_param') ===
def score_2(artifact, step, ctx):
    import csv

    gold = step.get('gold_order', {})
    tol = float(step.get('absolute_tolerance', 0.02))

    rows = []
    for row in artifact:
        try:
            n = str(int(row['num_cnts']))
            val = float(row['order_parameter'])
            rows.append((n, val))
        except Exception:
            continue

    if not rows:
        return 0.0

    scores = []
    for n, val in rows:
        if n in gold:
            abs_err = abs(val - gold[n])
            if abs_err <= tol:
                scores.append(1.0)
            else:
                s = max(0.0, 1.0 - (abs_err - tol) / tol)
                scores.append(s)
        else:
            scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='step_density_study') ===
def score_3(artifact, step, ctx):
    import csv

    gold = step.get('gold_density_moduli', {})
    tol = float(step.get('relative_tolerance', 0.10))

    rows = []
    for row in artifact:
        try:
            d = row['density_g_cm3']
            # format to two decimals to match gold keys
            d_key = f"{float(d):.2f}"
            mod = float(row['young_modulus_gpa'])
            rows.append((d_key, mod))
        except Exception:
            continue

    if not rows:
        return 0.0

    scores = []
    for d_key, val in rows:
        if d_key in gold:
            ref = gold[d_key]
            rel_err = abs((val - ref) / ref)
            if rel_err <= tol:
                scores.append(1.0)
            else:
                s = max(0.0, 1.0 - (rel_err - tol) / tol)
                scores.append(s)
        else:
            scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_stress_strain': score_0,
    'step_young_modulus': score_1,
    'step_order_param': score_2,
    'step_density_study': score_3,
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
