import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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
    ctx = {}
    gold_by_id = {}
    steps = spec.get("steps", [])
    for step in steps:
        gold_by_id[step["id"]] = step.get("config", {})
    ctx["gold"] = gold_by_id
    return ctx


# === block: score_0 (check id='adsorption_energies') ===
def score_0(artifact, step, ctx):
    config = ctx.get("gold", {}).get(step.get("id"), {})
    gold_rows = config.get("gold_rows", [])
    if not gold_rows:
        return 0.0
    tols = config.get("tolerances", {})
    dirs = config.get("directions", {})
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    artifact_by_config = {}
    for row in artifact:
        cfg = row.get("configuration", "").strip()
        artifact_by_config[cfg] = row

    # Columns to score depend on configuration: bond length is not reported for CO(O-site) in the paper.
    all_columns = ["adsorption_energy_kcal_mol", "hirshfeld_charge_transfer_e", "bond_length_si_x_A"]
    columns_without_bond_length = ["adsorption_energy_kcal_mol", "hirshfeld_charge_transfer_e"]

    row_scores = []
    for gold in gold_rows:
        cfg = gold.get("configuration")
        if cfg not in artifact_by_config:
            row_scores.append(0.0)
            continue
        row = artifact_by_config[cfg]
        # Use the reduced column set for configurations that lack a paper-reported bond length.
        if cfg == "CO(O-site)":
            cols = columns_without_bond_length
        else:
            cols = all_columns

        col_scores = []
        for col in cols:
            try:
                val = float(row.get(col, math.nan))
            except (ValueError, TypeError):
                col_scores.append(0.0)
                continue
            target = gold.get(col, None)
            if target is None:
                col_scores.append(1.0)
                continue
            tol = tols.get(col, 0.0)
            direction = dirs.get(col, "absolute")
            if direction == "less_equal":
                # better if value <= target (more negative); full credit if value <= target + tol
                if val <= target + tol:
                    score = 1.0
                else:
                    excess = val - (target + tol)
                    if excess <= 0:
                        score = 1.0
                    else:
                        decay = 2.0 * tol if tol > 0 else 1.0
                        score = max(0.0, 1.0 - excess / decay)
            else:  # absolute
                err = abs(val - target)
                if err <= tol:
                    score = 1.0
                else:
                    excess = err - tol
                    decay = 2.0 * tol if tol > 0 else 1.0
                    score = max(0.0, 1.0 - excess / decay)
            col_scores.append(score)
        if col_scores:
            row_scores.append(sum(col_scores) / len(col_scores))
        else:
            row_scores.append(0.0)
    if row_scores:
        return sum(row_scores) / len(row_scores)
    return 0.0


# === block: score_1 (check id='dimer_dissociation_barrier') ===
def score_1(artifact, step, ctx):
    config = ctx.get("gold", {}).get(step.get("id"), {})
    target = config.get("target", None)
    tol = config.get("tolerance", 0.0)
    if target is None:
        return 0.0
    try:
        val_str = artifact.strip()
        val = float(val_str)
    except (ValueError, AttributeError):
        return 0.0
    # barrier better if lower: full credit if value <= target + tol
    if val <= target + tol:
        return 1.0
    excess = val - (target + tol)
    decay = 2.0 * tol if tol > 0 else 1.0
    return max(0.0, 1.0 - excess / decay)


# === block: score_2 (check id='o_removal_barrier') ===
def score_2(artifact, step, ctx):
    config = ctx.get("gold", {}).get(step.get("id"), {})
    target = config.get("target", None)
    tol = config.get("tolerance", 0.0)
    if target is None:
        return 0.0
    try:
        val_str = artifact.strip()
        val = float(val_str)
    except (ValueError, AttributeError):
        return 0.0
    # barrier better if lower: full credit if value <= target + tol
    if val <= target + tol:
        return 1.0
    excess = val - (target + tol)
    decay = 2.0 * tol if tol > 0 else 1.0
    return max(0.0, 1.0 - excess / decay)


_SCORERS = {
    'adsorption_energies': score_0,
    'dimer_dissociation_barrier': score_1,
    'o_removal_barrier': score_2,
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
