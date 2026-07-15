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
    import json
    steps = spec.get("steps", [])
    ctx = {}
    for step in steps:
        sid = step.get("id", "")
        if sid == "check_transition_table":
            ctx["transition_gold"] = step.get("gold", [])
            ctx["transition_tolerances"] = step.get("tolerances", {})
        elif sid == "check_transition_trend":
            pass
        elif sid == "check_elastic_table":
            ctx["elastic_gold"] = step.get("gold", [])
            ctx["elastic_tolerances"] = step.get("tolerances", {})
    return ctx


# === block: score_0 (check id='check_transition_table') ===
def score_0(artifact, step, ctx):
    gold = ctx["transition_gold"]
    tolerances = ctx["transition_tolerances"]
    tol_P_0 = tolerances["transition_pressure_GPa_0K"]
    tol_P_300 = tolerances["transition_pressure_GPa_300K"]
    tol_V = tolerances["volume_drop_percent"]
    total = len(gold) * 2
    if total == 0:
        return 0.0
    gold_lookup = {(g['compound'], g['temperature_K']): g for g in gold}
    correct = 0
    for row in artifact:
        try:
            cp = row['compound']
            temp = int(row['temperature_K'])
            key = (cp, temp)
            if key not in gold_lookup:
                continue
            g = gold_lookup[key]
            p_sub = float(row['transition_pressure_GPa'])
            p_gold = g['transition_pressure_GPa']
            tol = tol_P_0 if temp == 0 else tol_P_300
            if abs(p_sub - p_gold) <= tol:
                correct += 1
            v_sub = float(row['volume_drop_percent'])
            v_gold = g['volume_drop_percent']
            if abs(v_sub - v_gold) <= tol_V:
                correct += 1
        except (KeyError, ValueError, TypeError):
            pass
    return correct / total


# === block: score_1 (check id='check_transition_trend') ===
def score_1(artifact, step, ctx):
    pressures = {}
    for row in artifact:
        try:
            cp = row['compound']
            temp = int(row['temperature_K'])
            if temp in (0, 300):
                pressures.setdefault(cp, {})[temp] = float(row['transition_pressure_GPa'])
        except (KeyError, ValueError, TypeError):
            pass
    ok = 0
    for compound in pressures:
        if 0 in pressures[compound] and 300 in pressures[compound]:
            if pressures[compound][300] < pressures[compound][0]:
                ok += 1
    total_compounds = 2
    return ok / total_compounds if total_compounds > 0 else 0.0


# === block: score_2 (check id='check_elastic_table') ===
def score_2(artifact, step, ctx):
    gold_list = ctx["elastic_gold"]
    tolerances = ctx.get("elastic_tolerances", {})
    default_rel = tolerances.get("default_relative", 0.05)
    default_abs = tolerances.get("default_absolute", 5.0)
    velocity_abs = tolerances.get("velocity_absolute", 50)
    pressure_deriv_abs = tolerances.get("pressure_derivative_absolute", 0.5)
    dimensionless_abs = tolerances.get("dimensionless_absolute", 0.05)
    dimensionless_props = {"A", "zeta", "sigma", "s2", "s3", "F12", "F44"}
    velocity_props = {"nu_l", "nu_t", "nu_m"}
    derivative_props = {"dBT_dP", "dCS_dP", "dC44_dP"}
    gold_lookup = {(g['compound'], g['temperature_K'], g['property']): g['value'] for g in gold_list}
    total = len(gold_list)
    if total == 0:
        return 0.0
    correct = 0
    for row in artifact:
        try:
            key = (row['compound'], int(row['temperature_K']), row['property'])
            if key not in gold_lookup:
                continue
            sub = float(row['value'])
            gold_val = gold_lookup[key]
            prop = row['property']
            if prop in dimensionless_props:
                abs_tol = dimensionless_abs
            elif prop in velocity_props:
                abs_tol = velocity_abs
            elif prop in derivative_props:
                abs_tol = pressure_deriv_abs
            else:
                abs_tol = default_abs
            tol = max(default_rel * abs(gold_val), abs_tol)
            if abs(sub - gold_val) <= tol:
                correct += 1
        except (KeyError, ValueError, TypeError):
            pass
    return correct / total


_SCORERS = {
    'check_transition_table': score_0,
    'check_transition_trend': score_1,
    'check_elastic_table': score_2,
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
