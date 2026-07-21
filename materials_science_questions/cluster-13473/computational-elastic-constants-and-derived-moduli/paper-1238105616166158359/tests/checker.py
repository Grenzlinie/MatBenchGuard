import os
import json
import csv
import math

# === author imports / helpers ===
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
            with open(path, newline="") as _ff_f:
                reader = _ff_csv.DictReader(_ff_f, delimiter=delim)
                required_cols = schema.get("required_columns", []) or []
                header = reader.fieldnames or []
                for col in required_cols:
                    if col not in header:
                        violations.append(base + ": missing column '" + col + "'")
    return violations


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


# === block: score_0 (check id='check_stress_8nm') ===
def score_0(artifact, step, ctx):
    # Hard-coded structural audit parameters for 8 nm sample
    yield_range_min = 4.0
    yield_range_max = 7.0
    early_strain_cutoff = 0.02
    early_stress_max = 2.5
    drop_ratio = 0.7

    if not artifact:
        return 0.0

    strains = []
    stresses = []
    for row in artifact:
        try:
            s = float(row['strain'])
            st = float(row['stress_GPa'])
            if math.isnan(s) or math.isnan(st):
                continue
            strains.append(s)
            stresses.append(st)
        except:
            continue

    if len(strains) < 5:
        return 0.0

    # 1) all stresses non-negative
    non_neg = all(v >= -1e-6 for v in stresses)
    score_nonneg = 0.15 if non_neg else 0.0

    # 2) not constant (std > 0.1 GPa)
    mean_stress = sum(stresses) / len(stresses) if len(stresses) > 1 else 0
    var = sum((x - mean_stress) ** 2 for x in stresses) / len(stresses) if len(stresses) > 1 else 0
    std = math.sqrt(var) if var > 0 else 0
    score_varied = 0.15 if std > 0.1 else 0.0

    # 3) discernible peak and drop after peak
    max_idx = max(range(len(stresses)), key=lambda i: stresses[i])
    peak_stress = stresses[max_idx]
    drop = False
    for i in range(max_idx, len(stresses)):
        if stresses[i] < drop_ratio * peak_stress:
            drop = True
            break
    score_drop = 0.25 if drop else 0.0

    # 4) peak stress within paper‑consistent range
    peak_ok = yield_range_min <= peak_stress <= yield_range_max
    score_peak = 0.25 if peak_ok else 0.0

    # 5) early elastic behaviour (up to early_cutoff): stress < early_stress_max and non‑decreasing
    early_ok = 0.20
    early_indices = [i for i, v in enumerate(strains) if v <= early_strain_cutoff]
    if early_indices:
        early_vals = [stresses[i] for i in early_indices if i < len(stresses)]
        if early_vals:
            if not all(s <= early_stress_max for s in early_vals):
                early_ok = 0.0
            elif not all(early_vals[i] <= early_vals[i+1] for i in range(len(early_vals)-1)):
                early_ok = 0.0
        else:
            early_ok = 0.0
    else:
        early_ok = 0.0

    score_early = early_ok

    total = score_nonneg + score_varied + score_drop + score_peak + score_early
    return min(total, 1.0)


# === block: score_1 (check id='check_stress_20nm') ===
def score_1(artifact, step, ctx):
    # Hard-coded structural audit parameters for 20 nm sample
    yield_range_min = 2.0
    yield_range_max = 5.0
    early_strain_cutoff = 0.02
    early_stress_max = 1.5
    drop_ratio = 0.7

    if not artifact:
        return 0.0

    strains = []
    stresses = []
    for row in artifact:
        try:
            s = float(row['strain'])
            st = float(row['stress_GPa'])
            if math.isnan(s) or math.isnan(st):
                continue
            strains.append(s)
            stresses.append(st)
        except:
            continue

    if len(strains) < 5:
        return 0.0

    # 1) all stresses non-negative
    non_neg = all(v >= -1e-6 for v in stresses)
    score_nonneg = 0.15 if non_neg else 0.0

    # 2) not constant (std > 0.1 GPa)
    mean_stress = sum(stresses) / len(stresses) if len(stresses) > 1 else 0
    var = sum((x - mean_stress) ** 2 for x in stresses) / len(stresses) if len(stresses) > 1 else 0
    std = math.sqrt(var) if var > 0 else 0
    score_varied = 0.15 if std > 0.1 else 0.0

    # 3) discernible peak and drop after peak
    max_idx = max(range(len(stresses)), key=lambda i: stresses[i])
    peak_stress = stresses[max_idx]
    drop = False
    for i in range(max_idx, len(stresses)):
        if stresses[i] < drop_ratio * peak_stress:
            drop = True
            break
    score_drop = 0.25 if drop else 0.0

    # 4) peak stress within paper‑consistent range
    peak_ok = yield_range_min <= peak_stress <= yield_range_max
    score_peak = 0.25 if peak_ok else 0.0

    # 5) early elastic behaviour (up to early_cutoff): stress < early_stress_max and non‑decreasing
    early_ok = 0.20
    early_indices = [i for i, v in enumerate(strains) if v <= early_strain_cutoff]
    if early_indices:
        early_vals = [stresses[i] for i in early_indices if i < len(stresses)]
        if early_vals:
            if not all(s <= early_stress_max for s in early_vals):
                early_ok = 0.0
            elif not all(early_vals[i] <= early_vals[i+1] for i in range(len(early_vals)-1)):
                early_ok = 0.0
        else:
            early_ok = 0.0
    else:
        early_ok = 0.0

    score_early = early_ok

    total = score_nonneg + score_varied + score_drop + score_peak + score_early
    return min(total, 1.0)


# === block: score_2 (check id='check_yield_strengths') ===
def score_2(artifact, step, ctx):
    # Hard-coded reference yield strengths and tolerances (from paper)
    ref_yield_8nm = 5.0
    tol_8nm = 1.0
    ref_yield_20nm = 3.0
    tol_20nm = 1.0

    if not isinstance(artifact, dict) or '8nm' not in artifact or '20nm' not in artifact:
        return 0.0

    try:
        y8 = float(artifact['8nm'])
        y20 = float(artifact['20nm'])
    except:
        return 0.0

    score = 0.0

    # 8 nm within tolerance
    if abs(y8 - ref_yield_8nm) <= tol_8nm:
        score += 0.35
    else:
        excess = abs(y8 - ref_yield_8nm) - tol_8nm
        if excess <= tol_8nm:
            score += 0.35 * (1.0 - excess / tol_8nm)

    # 20 nm within tolerance
    if abs(y20 - ref_yield_20nm) <= tol_20nm:
        score += 0.35
    else:
        excess = abs(y20 - ref_yield_20nm) - tol_20nm
        if excess <= tol_20nm:
            score += 0.35 * (1.0 - excess / tol_20nm)

    # ordering: 8 nm > 20 nm
    if y8 > y20:
        score += 0.30

    return score


_SCORERS = {
    'check_stress_8nm': score_0,
    'check_stress_20nm': score_1,
    'check_yield_strengths': score_2,
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