import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='band_gap') ===
def score_0(artifact, step, ctx):
    target = step["target"]
    tol = step["tolerance"]
    val = artifact.get(step["field"])
    if val is None:
        return 0.0
    try:
        diff = abs(float(val) - target)
    except (TypeError, ValueError):
        return 0.0
    return 1.0 if diff <= tol else 0.0


# === block: score_1 (check id='single_adsorption') ===
def score_1(artifact, step, ctx):
    gold = step["gold_table"]
    tol_E = step["tol_E_ads"]
    tol_Q = step["tol_charge"]
    low = step["ideal_window_low"]
    high = step["ideal_window_high"]
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    data = {}
    for row in artifact:
        gas = row.get("gas", "").strip()
        if not gas:
            continue
        try:
            e = float(row.get("E_ads", 0))
            q = float(row.get("charge_transfer", 0))
        except (TypeError, ValueError):
            continue
        data[gas] = (e, q)
    expected_gases = set(gold.keys())
    if set(data.keys()) != expected_gases:
        return 0.0
    e_score = 0.0
    q_score = 0.0
    for gas in expected_gases:
        ref_e = gold[gas]["E_ads"]
        ref_q = gold[gas]["charge_transfer"]
        ae, aq = data[gas]
        if abs(ae - ref_e) <= tol_E:
            e_score += 1.0
        if abs(aq - ref_q) <= tol_Q:
            q_score += 1.0
    e_score /= len(expected_gases)
    q_score /= len(expected_gases)
    # selectivity check
    in_window = 0
    so2_in = False
    for gas, (e, _) in data.items():
        mag = abs(e)
        if low <= mag <= high:
            in_window += 1
            if gas == "SO2":
                so2_in = True
    select_ok = (in_window == 1 and so2_in)
    select_score = 1.0 if select_ok else 0.0
    total = 0.6 * e_score + 0.2 * q_score + 0.2 * select_score
    return total


# === block: score_2 (check id='coadsorption') ===
def score_2(artifact, step, ctx):
    gold = step["gold_table"]
    tol_E = step["tol_E_ads"]
    tol_Q = step["tol_charge"]
    so2_thresh = step["so2_threshold_magnitude"]
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    data = {}
    for row in artifact:
        gas = row.get("gas", "").strip()
        if not gas:
            continue
        try:
            e = float(row.get("E_ads", 0))
            q = float(row.get("charge_transfer", 0))
        except (TypeError, ValueError):
            continue
        data[gas] = (e, q)
    expected = {"SO2", "H2O"}
    if set(data.keys()) != expected:
        return 0.0
    e_correct = 0
    q_correct = 0
    for gas in expected:
        ref_e = gold[gas]["E_ads"]
        ref_q = gold[gas]["charge_transfer"]
        ae, aq = data[gas]
        if abs(ae - ref_e) <= tol_E:
            e_correct += 1
        if abs(aq - ref_q) <= tol_Q:
            q_correct += 1
    e_score = e_correct / 2.0
    q_score = q_correct / 2.0
    # SO2 threshold
    so2_val = data.get("SO2", (0, 0))[0]
    so2_ok = (abs(so2_val) > so2_thresh) if so2_val else False
    so2_score = 1.0 if so2_ok else 0.0
    total = 0.5 * e_score + 0.3 * q_score + 0.2 * so2_score
    return total


_SCORERS = {
    'band_gap': score_0,
    'single_adsorption': score_1,
    'coadsorption': score_2,
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
