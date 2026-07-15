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
    import os, json, csv

    ctx = {}
    transition_path = os.path.join(outputs_dir, "transition_temperatures.json")
    if os.path.exists(transition_path):
        with open(transition_path) as f:
            trans = json.load(f)
            ctx['gamma_m'] = trans.get('gamma_m')
            ctx['gamma_i'] = trans.get('gamma_i')
    else:
        ctx['gamma_m'] = None
        ctx['gamma_i'] = None

    specific_heat_path = os.path.join(outputs_dir, "specific_heat.csv")
    peak_gamma = None
    if os.path.exists(specific_heat_path):
        with open(specific_heat_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows:
                vals = []
                for r in rows:
                    try:
                        g = float(r['Gamma'])
                        c = float(r['c_N'])
                        vals.append((g, c))
                    except (ValueError, KeyError):
                        pass
                if vals:
                    peak_gamma = max(vals, key=lambda x: x[1])[0]
    ctx['specific_heat_peak'] = peak_gamma
    return ctx


# === block: score_0 (check id='transition_determination') ===
def score_0(artifact, step, ctx):
    gamma_m = artifact.get('gamma_m')
    gamma_i = artifact.get('gamma_i')
    if gamma_m is None or gamma_i is None:
        return 0.0

    targets = step.get('targets', {})
    gm_tol = targets.get('gamma_m', {}).get('tolerance', 2.0)
    gm_val = targets.get('gamma_m', {}).get('value', 69.25)
    gi_tol = targets.get('gamma_i', {}).get('tolerance', 2.0)
    gi_val = targets.get('gamma_i', {}).get('value', 68.25)

    score = 0.0
    if abs(gamma_m - gm_val) <= gm_tol:
        score += 0.5
    if abs(gamma_i - gi_val) <= gi_tol:
        score += 0.5
    return score


# === block: score_1 (check id='specific_heat') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    try:
        rows = [(float(r['Gamma']), float(r['c_N'])) for r in artifact]
    except Exception:
        return 0.0

    gamma_m = ctx.get('gamma_m')
    gamma_i = ctx.get('gamma_i')
    if gamma_m is None or gamma_i is None:
        return 0.0

    interval_rows = [(g, c) for g, c in rows if gamma_i <= g <= gamma_m]
    if not interval_rows:
        return 0.0

    peak = max(interval_rows, key=lambda x: x[1])
    peak_gamma, peak_c = peak[0], peak[1]

    checks = step.get('checks', {})
    ref_peak = checks.get('peak_reference', 68.5)
    tol = checks.get('peak_tolerance', 0.5)

    score = 0.0
    # peak between transitions (already satisfied by filtering)
    score += 0.3

    # closeness to reference peak
    if abs(peak_gamma - ref_peak) <= tol:
        score += 0.4

    # single peak: exactly one maximum in interval
    peak_count = sum(1 for g, c in interval_rows if c == peak_c)
    if peak_count == 1:
        score += 0.3

    return score


# === block: score_2 (check id='defect_density') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    try:
        rows = [(float(r['Gamma']), float(r['isolated_dislocation_frac'])) for r in artifact if r['Gamma'].strip() and r['isolated_dislocation_frac'].strip()]
    except Exception:
        return 0.0
    if len(rows) < 2:
        return 0.0

    rows.sort(key=lambda x: x[0])
    diffs = []
    for i in range(len(rows)-1):
        g1, f1 = rows[i]
        g2, f2 = rows[i+1]
        delta = f2 - f1
        gamma_mid = (g1 + g2) / 2.0
        diffs.append((delta, gamma_mid))
    if not diffs:
        return 0.0
    max_diff, steep_gamma = max(diffs, key=lambda x: x[0])

    peak_gamma = ctx.get('specific_heat_peak')
    if peak_gamma is None:
        return 0.0

    tol = step.get('checks', {}).get('steepest_dislocation_gamma_delta_tol', 0.5)
    diff = abs(steep_gamma - peak_gamma)
    if diff <= tol:
        return 1.0
    else:
        # partial credit decay (max difference beyond tolerance gives partial score)
        decay = max(0.0, 1.0 - (diff - tol) / 1.0)
        return decay


_SCORERS = {
    'transition_determination': score_0,
    'specific_heat': score_1,
    'defect_density': score_2,
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
