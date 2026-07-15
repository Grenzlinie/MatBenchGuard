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


# === block: score_0 (check id='check_results_csv_content') ===
def score_0(artifact, step, ctx):
    # artifact is a list of dicts from csv.DictReader
    # step contains gold_data and tolerances
    # ctx is the prepare return value (empty dict here)

    if not isinstance(artifact, list):
        return 0.0

    gold_data = step.get("gold_data", {})
    tolerances = step.get("tolerances", {})
    expected_metals = list(gold_data.keys())
    num_expected = len(expected_metals)

    if num_expected == 0:
        return 1.0

    # Build lookup from artifact rows
    agent_data = {}
    for row in artifact:
        metal = str(row.get("metal", "")).strip()
        if metal:
            agent_data[metal] = row

    # Score each expected metal
    metal_scores = []
    for metal in expected_metals:
        if metal not in agent_data:
            metal_scores.append(0.0)
            continue

        g = gold_data[metal]
        row = agent_data[metal]

        # Helper to safely get float from row
        def safe_float(val):
            try:
                return float(val)
            except (ValueError, TypeError):
                return float("nan")

        # Check Δd values
        d_checks = {}
        for key in ["Δd12", "Δd23", "Δd34", "Δd45", "Δd56"]:
            col = f"{key}_percent"
            agent_val = safe_float(row.get(col))
            tol = tolerances.get(key, 0.5)
            gold_val = g.get(key, 0.0)
            if math.isfinite(agent_val) and abs(agent_val - gold_val) <= tol:
                d_checks[key] = 1.0
            else:
                d_checks[key] = 0.0

        # Check surface energies
        se_checks = {}
        for se_key in ["surface_energy_relaxed", "surface_energy_unrelaxed"]:
            agent_val = safe_float(row.get(se_key))
            tol = tolerances.get(se_key, 50)
            gold_val = g.get(se_key, 0.0)
            if math.isfinite(agent_val) and abs(agent_val - gold_val) <= tol:
                se_checks[se_key] = 1.0
            else:
                se_checks[se_key] = 0.0

        # Relaxation direction: relaxed < unrelaxed (surface energy must decrease)
        agent_rel = safe_float(row.get("surface_energy_relaxed"))
        agent_unrel = safe_float(row.get("surface_energy_unrelaxed"))
        if math.isfinite(agent_rel) and math.isfinite(agent_unrel) and agent_unrel > agent_rel:
            relaxation_ok = 1.0
        else:
            relaxation_ok = 0.0

        # Sign check for Δd12 (outward=positive, inward=negative)
        agent_d12 = safe_float(row.get("Δd12_percent"))
        gold_d12 = g.get("Δd12", 0.0)
        if abs(gold_d12) > 0.01:
            sign_ok = 1.0 if (agent_d12 > 0) == (gold_d12 > 0) else 0.0
        else:
            sign_ok = 1.0

        # Per-metal weighted score (weights sum to 1.0)
        metal_score = (
            0.35 * d_checks.get("Δd12", 0) +
            0.10 * sign_ok +
            0.10 * d_checks.get("Δd23", 0) +
            0.05 * d_checks.get("Δd34", 0) +
            0.05 * d_checks.get("Δd45", 0) +
            0.05 * d_checks.get("Δd56", 0) +
            0.15 * se_checks.get("surface_energy_relaxed", 0) +
            0.10 * se_checks.get("surface_energy_unrelaxed", 0) +
            0.05 * relaxation_ok
        )
        metal_scores.append(metal_score)

    # Overall score: average across all expected metals (missing metals score 0)
    overall = sum(metal_scores) / num_expected
    return max(0.0, min(1.0, overall))


_SCORERS = {
    'check_results_csv_content': score_0,
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
