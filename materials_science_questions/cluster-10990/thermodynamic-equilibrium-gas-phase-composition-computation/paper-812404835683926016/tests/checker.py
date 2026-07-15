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
    steps = spec.get("steps", [])
    ctx = {}
    for step in steps:
        if step.get("output_file") == "gas_composition.csv":
            ctx["expected"] = step.get("expected", [])
            ctx["tolerances"] = step.get("tolerances", {})
            break
    return ctx


# === block: score_0 (check id='scored_composition') ===
def score_0(artifact, step, ctx):
    # --- composition scoring (existing logic, unchanged) ---
    expected_rows = ctx.get("expected", [])
    tolerances = ctx.get("tolerances", {})
    major_rel = tolerances.get("major_species_relative", 0.10)
    major_abs_floor = tolerances.get("major_species_absolute_floor", 0.005)
    minor_abs = tolerances.get("minor_species_absolute", 0.001)
    tot_rel = tolerances.get("total_moles_relative", 0.05)
    tot_abs_floor = tolerances.get("total_moles_absolute_floor", 0.5)
    slope = tolerances.get("slope_factor", 1.0)

    major_species = {"H2", "CO", "H2O", "CO2", "CH4"}
    all_fields = ["TotalMoles", "H2", "CO", "H2O", "CO2", "CH4", "N2", "H2S"]

    def norm_ratio(r):
        return str(r).replace(" ", "").strip()

    def tolerance_for(expected_val, field):
        if field == "TotalMoles":
            return max(tot_abs_floor, tot_rel * abs(expected_val))
        if field in major_species:
            return max(major_abs_floor, major_rel * abs(expected_val))
        return minor_abs

    def item_score(diff, tol):
        if tol <= 0:
            tol = 1e-9
        if diff <= tol:
            return 1.0
        penalty = (diff - tol) / (slope * tol)
        return max(0.0, 1.0 - penalty)

    if not expected_rows:
        composition_score = 0.0
    else:
        artifact_map = {}
        for row in artifact:
            try:
                temp = int(float(row.get("Temperature", 0)))
            except (ValueError, TypeError):
                continue
            wr = norm_ratio(row.get("WaterWoodRatio", ""))
            artifact_map[(temp, wr)] = row

        total_score = 0.0
        total_items = len(expected_rows) * len(all_fields)
        if total_items == 0:
            composition_score = 0.0
        else:
            for exp in expected_rows:
                temp = exp.get("Temperature")
                wr = norm_ratio(exp.get("WaterWoodRatio", ""))
                row = artifact_map.get((temp, wr))
                if row is None:
                    continue
                for field in all_fields:
                    exp_val = exp.get(field)
                    if exp_val is None:
                        continue
                    try:
                        agent_val = float(row.get(field, 0))
                    except (ValueError, TypeError):
                        continue
                    diff = abs(agent_val - exp_val)
                    tol = tolerance_for(exp_val, field)
                    s = item_score(diff, tol)
                    total_score += s
            composition_score = round(total_score / total_items, 6)

    # --- liquid presence scoring (new) ---
    # Paper finding: no liquid at 600°C or 700°C for any ratio.
    # At 800°C: no liquid for 0.5/1 and 1/1; liquid present for 0.75/1.
    # This matches the text: liquid present only above 800°C for 0.5/1 and 1/1,
    # and present down to 797°C for 0.75/1.
    liquid_expected = {
        (800, "0.5/1"): False,
        (700, "0.5/1"): False,
        (600, "0.5/1"): False,
        (800, "0.75/1"): True,
        (700, "0.75/1"): False,
        (600, "0.75/1"): False,
        (800, "1/1"): False,
        (700, "1/1"): False,
        (600, "1/1"): False,
    }

    liquid_correct = 0
    liquid_total = 0
    for (temp, wr), expected_present in liquid_expected.items():
        row = artifact_map.get((temp, wr))
        if row is None:
            continue
        liquid_total += 1
        agent_liquid = row.get("LiquidPresent")
        if agent_liquid is None:
            continue
        # Accept booleans or case-insensitive strings "true"/"false"
        if isinstance(agent_liquid, bool):
            agent_present = agent_liquid
        elif isinstance(agent_liquid, str):
            agent_present = agent_liquid.strip().lower() == "true"
        else:
            agent_present = bool(agent_liquid)
        if agent_present == expected_present:
            liquid_correct += 1

    if liquid_total > 0:
        liquid_score = liquid_correct / liquid_total
    else:
        liquid_score = 0.0

    # Final combined reward: equal weight to composition (paper's main table) and liquid threshold (co-equal headline)
    return 0.5 * composition_score + 0.5 * liquid_score


_SCORERS = {
    'scored_composition': score_0,
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
