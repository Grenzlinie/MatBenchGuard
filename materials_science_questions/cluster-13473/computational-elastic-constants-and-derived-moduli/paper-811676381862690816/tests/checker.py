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


# === block: score_0 (check id='percolation_threshold_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    p_c_str = rows[0].get("p_c", "").strip()
    try:
        p_c = float(p_c_str)
    except:
        return 0.0
    target = float(step.get("target", 0.34))
    tol = float(step.get("tolerance_abs", 0.05))
    if abs(p_c - target) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='simulation_E_over_E0') ===
def score_1(artifact, step, ctx):
    params = step["params"]
    p_l = float(params["p_l"])
    p_c = float(params["p_c"])
    m = float(params["m"])
    rel_tol_good = float(params["rel_tol_good"])
    rel_tol_bad = float(params["rel_tol_bad"])
    high_p_unity_tol = float(params["high_p_unity_tol"])

    def ref_E(p):
        if p <= p_c:
            return 0.0
        one_minus_p = 1.0 - p
        one_minus_pl = 1.0 - p_l
        term1 = one_minus_p / (m * one_minus_pl)
        one_minus_pc = 1.0 - p_c
        numerator = m * one_minus_pl - one_minus_pc
        denominator = m * one_minus_pl * (one_minus_pc ** 2)
        term2 = numerator * (one_minus_p ** 2) / denominator
        base = 1.0 - term1 - term2
        if base <= 0:
            return 0.0
        return base ** m

    rows = artifact
    if not rows:
        return 0.0
    sets_rows = {}
    for r in rows:
        sid = r.get("set_id", "").strip()
        if sid not in ("111","114","167"):
            continue
        try:
            p = float(r["p"])
            e = float(r["E_over_E0"])
        except:
            continue
        sets_rows.setdefault(sid, []).append((p, e))

    if not sets_rows:
        return 0.0

    # Monotonicity and high-p unity gates
    for sid, pairs in sets_rows.items():
        pairs_sorted = sorted(pairs, key=lambda x: x[0])
        for i in range(1, len(pairs_sorted)):
            if pairs_sorted[i][1] < pairs_sorted[i-1][1] - 1e-9:
                return 0.0
        max_p, max_e = max(pairs_sorted, key=lambda x: x[0])
        if max_p >= 0.98:
            if abs(max_e - 1.0) > high_p_unity_tol:
                return 0.0

    total_score = 0.0
    count = 0
    for sid, pairs in sets_rows.items():
        for p, e in pairs:
            ref = ref_E(p)
            denom = ref if ref >= 0.02 else 0.02
            rel_err = abs(e - ref) / denom if denom > 0 else 0.0
            if rel_err <= rel_tol_good:
                row_score = 1.0
            elif rel_err >= rel_tol_bad:
                row_score = 0.0
            else:
                row_score = 1.0 - (rel_err - rel_tol_good) / (rel_tol_bad - rel_tol_good)
            total_score += row_score
            count += 1

    if count == 0:
        return 0.0
    return total_score / count


# === block: score_2 (check id='simulation_sigma') ===
def score_2(artifact, step, ctx):
    params = step["params"]
    sigma_o_map = params["sigma_o"]
    const_tol = float(params["const_tol"])
    low_p_tol = float(params["low_p_tol"])
    high_p_tol = float(params["high_p_tol"])

    rows = artifact
    if not rows:
        return 0.0
    sets_groups = {}
    for r in rows:
        sid = r.get("set_id", "").strip()
        if sid not in ("111","114","167"):
            continue
        try:
            p = float(r["p"])
            sigma = float(r["sigma"])
        except:
            continue
        sets_groups.setdefault(sid, []).append((p, sigma))

    for sid, pairs in sets_groups.items():
        if sid == "111":
            target_sigma = 1.0/3.0
            for p, sigma in pairs:
                if abs(sigma - target_sigma) > const_tol:
                    return 0.0
        else:
            if sid not in sigma_o_map:
                return 0.0
            target_sigma_o = sigma_o_map[sid]
            pairs_sorted = sorted(pairs, key=lambda x: x[0])
            for i in range(1, len(pairs_sorted)):
                if pairs_sorted[i][1] < pairs_sorted[i-1][1] - 1e-9:
                    return 0.0
            for p, sigma in pairs_sorted:
                if p <= 0.4:
                    if abs(sigma - 1.0/3.0) > low_p_tol:
                        return 0.0
            max_p, max_sigma = max(pairs_sorted, key=lambda x: x[0])
            if abs(max_sigma - target_sigma_o) > high_p_tol:
                return 0.0
    return 1.0


_SCORERS = {
    'percolation_threshold_check': score_0,
    'simulation_E_over_E0': score_1,
    'simulation_sigma': score_2,
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
