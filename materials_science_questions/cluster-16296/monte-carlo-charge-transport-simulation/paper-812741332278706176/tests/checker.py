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
    steps = spec.get("steps", [])
    steady_step = next((s for s in steps if s.get("id") == "step03_extract_steady_state"), {})
    overshoot_step = next((s for s in steps if s.get("id") == "step04_extract_overshoot_peak"), {})
    rr = overshoot_step.get("ratio_range", [0.95, 1.05])
    return {
        "steady_gold": steady_step.get("gold_fields", {}),
        "steady_abs_tol": steady_step.get("abs_tolerance_frac", 0.15),
        "steady_low_fields": set(steady_step.get("crossover_low_fields", [])),
        "steady_high_fields": set(steady_step.get("crossover_high_fields", [])),
        "steady_rel_margin": steady_step.get("relative_margin", 0.02),
        "overshoot_gold_eq": overshoot_step.get("gold_equil_peak", 37000000.0),
        "overshoot_gold_ne": overshoot_step.get("gold_nonequil_peak", 37000000.0),
        "overshoot_abs_tol": overshoot_step.get("abs_tolerance_frac", 0.15),
        "overshoot_ratio_lo": rr[0] if len(rr) >= 1 else 0.95,
        "overshoot_ratio_hi": rr[1] if len(rr) >= 2 else 1.05,
    }


# === block: score_0 (check id='step03_extract_steady_state') ===
def score_0(artifact, step, ctx):
    # artifact: list of dicts from csv.DictReader with keys electric_field_kVcm, v_equilibrium_cms, v_nonequilibrium_cms
    rows_by_field = {}
    for row in (artifact or []):
        try:
            f = float(row.get("electric_field_kVcm", ""))
            ve = float(row.get("v_equilibrium_cms", 0))
            vn = float(row.get("v_nonequilibrium_cms", 0))
            rows_by_field[f] = (ve, vn)
        except (ValueError, TypeError):
            continue

    gold = ctx.get("steady_gold", {})
    low_fields = ctx.get("steady_low_fields", set())
    high_fields = ctx.get("steady_high_fields", set())
    margin = ctx.get("steady_rel_margin", 0.02)
    abs_tol = ctx.get("steady_abs_tol", 0.15)

    if not rows_by_field:
        return 0.0

    crossover_correct = 0
    crossover_total = 0
    abs_correct = 0
    abs_total = 0

    for f_str, g in gold.items():
        f = float(f_str)
        if f not in rows_by_field:
            continue
        ve, vn = rows_by_field[f]
        gve = g.get("v_equil", 0.0)
        gvn = g.get("v_nonequil", 0.0)
        if gve == 0.0 and gvn == 0.0:
            continue

        # Crossover check
        crossover_total += 1
        if f in low_fields and vn > ve * (1.0 + margin):
            crossover_correct += 1
        elif f in high_fields and vn < ve * (1.0 - margin):
            crossover_correct += 1

        # Absolute check
        if abs(gve) > 1e-9:
            abs_total += 1
            dev = abs(ve - gve) / (abs_tol * abs(gve))
            if dev <= 1.0:
                abs_correct += 1.0
            else:
                abs_correct += max(0.0, 2.0 - dev)
        if abs(gvn) > 1e-9:
            abs_total += 1
            dev = abs(vn - gvn) / (abs_tol * abs(gvn))
            if dev <= 1.0:
                abs_correct += 1.0
            else:
                abs_correct += max(0.0, 2.0 - dev)

    if crossover_total == 0 and abs_total == 0:
        return 0.0

    crossover_score = crossover_correct / max(crossover_total, 1)
    abs_score = abs_correct / max(abs_total, 1)
    score = 0.6 * crossover_score + 0.4 * abs_score
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='step04_extract_overshoot_peak') ===
def score_1(artifact, step, ctx):
    # artifact: list of dicts from csv.DictReader; expects ONE row with keys electric_field_kVcm, v_equilibrium_peak_cms, v_nonequilibrium_peak_cms
    if not artifact or len(artifact) == 0:
        return 0.0
    row = artifact[0]
    try:
        field_val = float(row.get("electric_field_kVcm", 0))
        ve = float(row.get("v_equilibrium_peak_cms", 0))
        vn = float(row.get("v_nonequilibrium_peak_cms", 0))
    except (ValueError, TypeError):
        return 0.0

    # Field identity check (must be ~8.0 kV/cm)
    if abs(field_val - 8.0) <= 0.1:
        field_score = 1.0
    else:
        field_score = max(0.0, 1.0 - abs(field_val - 8.0) / 2.0)

    # Ratio check
    if abs(ve) < 1e-9:
        return 0.0
    ratio = vn / ve
    ratio_lo = ctx.get("overshoot_ratio_lo", 0.95)
    ratio_hi = ctx.get("overshoot_ratio_hi", 1.05)
    if ratio_lo <= ratio <= ratio_hi:
        ratio_score = 1.0
    else:
        dist = min(abs(ratio - ratio_lo), abs(ratio - ratio_hi))
        ratio_score = max(0.0, 1.0 - dist / 0.2)

    # Absolute value check
    abs_tol = ctx.get("overshoot_abs_tol", 0.15)
    gold_eq = ctx.get("overshoot_gold_eq", 37000000.0)
    gold_ne = ctx.get("overshoot_gold_ne", 37000000.0)

    def abs_partial(val, gold, tol):
        if abs(gold) < 1e-9:
            return 1.0 if abs(val) < 1e-9 else 0.0
        dev = abs(val - gold) / (tol * abs(gold))
        if dev <= 1.0:
            return 1.0
        return max(0.0, 2.0 - dev)

    abs_eq_score = abs_partial(ve, gold_eq, abs_tol)
    abs_ne_score = abs_partial(vn, gold_ne, abs_tol)
    abs_score = 0.5 * abs_eq_score + 0.5 * abs_ne_score

    score = 0.05 * field_score + 0.55 * ratio_score + 0.4 * abs_score
    return min(1.0, max(0.0, score))


_SCORERS = {
    'step03_extract_steady_state': score_0,
    'step04_extract_overshoot_peak': score_1,
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
