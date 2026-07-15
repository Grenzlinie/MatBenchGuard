import os
import json
import csv

# === author imports / helpers ===
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
    gold_rows = spec['steps'][0]['gold_rows']
    rel_threshold = spec['steps'][0]['rel_threshold']
    rel_tol = spec['steps'][0]['rel_tol']
    abs_tol = spec['steps'][0]['abs_tol']
    series_groups = spec['steps'][0]['series_groups']
    # Build a quick-lookup of gold by condition
    lookup_gold = {}
    for g in gold_rows:
        key = (int(g['temperature_K']), int(g['pressure_atm']), round(g['H2_mol'], 6), round(g['H2O_mol'], 6))
        lookup_gold[key] = g
    return {
        'lookup_gold': lookup_gold,
        'gold_rows': gold_rows,
        'rel_threshold': rel_threshold,
        'rel_tol': rel_tol,
        'abs_tol': abs_tol,
        'series_groups': series_groups
    }


# === block: score_0 (check id='step_ratios_value_and_trends') ===
def score_0(artifact, step, ctx):
    ctx = ctx
    artifacts = artifact  # list of dicts from CSV
    if not isinstance(artifacts, list) or len(artifacts) == 0:
        return 0.0
    # Build lookup from agent CSV
    agent_lookup = {}
    for row in artifacts:
        try:
            T = int(row['temperature_K'])
            P = int(row['pressure_atm'])
            H2 = round(float(row['H2_mol']), 6)
            H2O = round(float(row['H2O_mol']), 6)
            key = (T, P, H2, H2O)
            agent_lookup[key] = row
        except (ValueError, KeyError):
            continue
    gold_rows = ctx['gold_rows']
    rel_threshold = ctx['rel_threshold']
    rel_tol = ctx['rel_tol']
    abs_tol = ctx['abs_tol']
    # Evaluate per-row value pass
    row_weights = []
    row_passes_value = []
    for g in gold_rows:
        key = (int(g['temperature_K']), int(g['pressure_atm']), round(g['H2_mol'], 6), round(g['H2O_mol'], 6))
        a_row = agent_lookup.get(key)
        if a_row is None:
            # missing row
            ratio_names = ['I_CsI','HI_CsI','CsOH_CsI','Cs_CsI']
            max_ratio = max(abs(g[r]) for r in ratio_names)
            row_weights.append(max_ratio)
            row_passes_value.append(False)
            continue
        # check each ratio
        ratio_names = ['I_CsI','HI_CsI','CsOH_CsI','Cs_CsI']
        all_pass = True
        for r in ratio_names:
            try:
                a_val = float(a_row[r])
            except (ValueError, KeyError):
                all_pass = False
                break
            gold_val = g[r]
            if abs(gold_val) >= rel_threshold:
                margin = rel_tol * abs(gold_val)
            else:
                margin = abs_tol
            if abs(a_val - gold_val) > margin:
                all_pass = False
                break
        max_ratio = max(abs(g[r]) for r in ratio_names)
        row_weights.append(max_ratio)
        row_passes_value.append(all_pass)

    # Trend check: I_CsI must strictly increase with temperature for each series
    series_groups = ctx['series_groups']
    trend_pass = True
    for sg in series_groups:
        temps = sorted(sg['temperatures'])
        P = sg['pressure_atm']
        H2 = sg['H2_mol']
        H2O = sg['H2O_mol']
        vals = []
        for T in temps:
            key = (T, int(P), round(H2, 6), round(H2O, 6))
            a_row = agent_lookup.get(key)
            if a_row is None:
                vals.append(None)
            else:
                try:
                    vals.append(float(a_row['I_CsI']))
                except (ValueError, KeyError):
                    vals.append(None)
        # check increasing
        for i in range(len(vals)-1):
            if vals[i] is None or vals[i+1] is None:
                trend_pass = False
                break
            if vals[i+1] <= vals[i]:
                trend_pass = False
                break
        if not trend_pass:
            break

    # final weighted fraction
    num = 0.0
    den = 0.0
    for w, pv in zip(row_weights, row_passes_value):
        if pv and trend_pass:
            num += w
        den += w
    if den == 0:
        return 0.0
    return num / den


_SCORERS = {
    'step_ratios_value_and_trends': score_0,
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
