import os
import json
import csv

# === author imports / helpers ===
import os
import json
import csv
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
        return {"gold_t0": spec["steps"][0]["gold"], "gold_ft": spec["steps"][1]["gold"]}


# === block: score_0 (check id='step_01_t0_results') ===
def score_0(artifact, step, ctx):
    def score_t0(rows, step):
        tolerances = step["tolerances"]
        gold_map = step["gold"]
        if not rows:
            return 0.0
        expected_keys = list(gold_map.keys())
        fields = ["m","delta","Cg","Cd","C2g","Cg_plus_d","C2d"]
        total_possible = len(expected_keys) * len(fields)
        score_sum = 0.0
        for lam_key in expected_keys:
            gold_data = gold_map[lam_key]
            # find row with matching lambda
            matching_row = None
            for row in rows:
                if row.get("lambda") is None:
                    continue
                if f"{float(row['lambda']):.1f}" == lam_key:
                    matching_row = row
                    break
            if matching_row is None:
                continue  # all fields for this row count as 0
            # evaluate fields
            for field in fields:
                try:
                    val = float(matching_row.get(field, "nan"))
                except:
                    continue  # field missing => contribute 0
                gold_val = gold_data.get(field, 0)
                if field in ("m","delta"):
                    rel = tolerances[field]["rel"]
                    abs_tol = tolerances[field]["abs"]
                    diff = abs(val - gold_val)
                    if diff <= max(abs_tol, rel*abs(gold_val)):
                        score_sum += 1.0
                else:
                    rel = tolerances["corr_rel"]
                    abs_tol = tolerances["corr_abs"]
                    diff = abs(val - gold_val)
                    if diff <= max(abs_tol, rel*abs(gold_val)):
                        score_sum += 1.0
        if total_possible == 0:
            return 0.0
        return score_sum / total_possible

    score = score_t0(artifact, step)


# === block: score_1 (check id='step_02_ft_results') ===
def score_1(artifact, step, ctx):
    def score_ft(rows, step):
        tolerances = step["tolerances"]
        gold_map = step["gold"]
        if not rows:
            return 0.0
        # Collect all expected (lambda, T) combos from gold
        expected_combos = []
        for lam_key, t_dict in gold_map.items():
            for t_key in t_dict:
                expected_combos.append((lam_key, t_key))
        if not expected_combos:
            return 0.0
        fields = ["delta", "Cg", "Cd", "C2g", "chi"]
        total_possible = len(expected_combos) * len(fields)
        score_sum = 0.0
        # Build a lookup from (lam_key, t_key) to the row (first match)
        row_lookup = {}
        for row in rows:
            lam = row.get("lambda")
            t_val = row.get("T")
            if lam is None or t_val is None:
                continue
            lam_key = f"{float(lam):.1f}"
            t_key = f"{float(t_val):.1f}"
            if (lam_key, t_key) not in row_lookup:
                row_lookup[(lam_key, t_key)] = row
        # Score each expected combo
        for lam_key, t_key in expected_combos:
            gold_data = gold_map[lam_key][t_key]
            row = row_lookup.get((lam_key, t_key))
            if row is None:
                continue  # all fields contribute 0 for this combo
            for field in fields:
                try:
                    val = float(row.get(field, "nan"))
                except:
                    continue  # contributes 0
                gold_val = gold_data.get(field, 0)
                if field == "delta":
                    rel = tolerances["delta"]["rel"]
                    abs_tol = tolerances["delta"]["abs"]
                    diff = abs(val - gold_val)
                    if diff <= max(abs_tol, rel * abs(gold_val)):
                        score_sum += 1.0
                elif field == "chi":
                    rel = tolerances["chi_rel"]
                    abs_tol = tolerances["chi_abs"]
                    diff = abs(val - gold_val)
                    if diff <= max(abs_tol, rel * abs(gold_val)):
                        score_sum += 1.0
                else:
                    rel = tolerances["corr_rel"]
                    abs_tol = tolerances["corr_abs"]
                    diff = abs(val - gold_val)
                    if diff <= max(abs_tol, rel * abs(gold_val)):
                        score_sum += 1.0
        return score_sum / total_possible

    score = score_ft(artifact, step)


_SCORERS = {
    'step_01_t0_results': score_0,
    'step_02_ft_results': score_1,
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
