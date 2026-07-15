import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math


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
    spec = json.load(open("/tests/grading_spec.json"))
    ctx = {"gold": spec.get("gold", {})}
    return ctx


# === block: score_0 (check id='fitted_params') ===
def score_0(artifact, step, ctx):
    def score_param(val, gold, tol=0.02):
        if abs(gold) < 1e-9:
            return 1.0 if abs(val) < 1e-9 else 0.0
        rel = abs(val - gold) / abs(gold)
        if rel <= tol:
            return 1.0
        return max(0.0, 1.0 - (rel - tol) / 0.1)

    def score_aad_lower(agent, ref, abs_tol=0.5):
        if agent <= ref + abs_tol:
            return 1.0
        excess = agent - (ref + abs_tol)
        max_ex = max(ref * 2.0, 2.0)
        return max(0.0, 1.0 - excess / max_ex)

    def score_r2_higher(agent, ref):
        if agent >= ref - 0.02:
            return 1.0
        if agent >= 0.95:
            return 0.5
        return 0.0

    gold_rows = ctx["gold"]["fitted_parameters"]["data"]
    gold_map = {row["gas_name"]: row for row in gold_rows}
    comp_scores = []
    for row in artifact:
        name = row.get("gas_name", "").strip()
        if name in gold_map:
            g = gold_map[name]
            cp0 = float(row.get("Cp0", 0))
            cpinf = float(row.get("Cp_inf", 0))
            ti = float(row.get("Ti", 0))
            aad = float(row.get("AAD_Cp", 0))
            r2 = float(row.get("R2_Cp", 0))
            s_cp0 = score_param(cp0, float(g["Cp0"]))
            s_cpinf = score_param(cpinf, float(g["Cp_inf"]))
            s_ti = score_param(ti, float(g["Ti"]))
            s_aad = score_aad_lower(aad, float(g["AAD_Cp"]))
            s_r2 = score_r2_higher(r2, float(g["R2_Cp"]))
            comp = (s_cp0 + s_cpinf + s_ti) / 3.0 * 0.4 + s_aad * 0.3 + s_r2 * 0.3
            comp_scores.append(comp)
    if not comp_scores:
        return 0.0
    return sum(comp_scores) / len(comp_scores)


# === block: score_1 (check id='entropy') ===
def score_1(artifact, step, ctx):
    def score_aad_lower(agent, ref, abs_tol=0.5):
        if agent <= ref + abs_tol:
            return 1.0
        excess = agent - (ref + abs_tol)
        max_ex = max(ref * 2.0, 2.0)
        return max(0.0, 1.0 - excess / max_ex)

    def score_r2_higher(agent, ref):
        if agent >= ref - 0.03:
            return 1.0
        if agent >= 0.95:
            return 0.5
        return 0.0

    gold_rows = ctx["gold"]["entropy_results"]["data"]
    gold_map = {row["gas_name"]: row for row in gold_rows}
    comp_scores = []
    for row in artifact:
        name = row.get("gas_name", "").strip()
        if name in gold_map:
            g = gold_map[name]
            aad = float(row.get("AAD_S", 0))
            r2 = float(row.get("R2_S", 0))
            s_aad = score_aad_lower(aad, float(g["AAD_S"]))
            s_r2 = score_r2_higher(r2, float(g["R2_S"]))
            comp = s_aad * 0.5 + s_r2 * 0.5
            comp_scores.append(comp)
    if not comp_scores:
        return 0.0
    return sum(comp_scores) / len(comp_scores)


# === block: score_2 (check id='linear') ===
def score_2(artifact, step, ctx):
    def score_param(val, gold, tol=0.05):
        if abs(gold) < 1e-9:
            return 1.0 if abs(val) < 1e-9 else 0.0
        rel = abs(val - gold) / abs(gold)
        if rel <= tol:
            return 1.0
        return max(0.0, 1.0 - (rel - tol) / 0.15)

    gold_rows = ctx["gold"]["linear_trends"]["data"]
    gold_map = {row["parameter"]: row for row in gold_rows}
    row_scores = []
    for row in artifact:
        param = row.get("parameter", "").strip()
        if param in gold_map:
            g = gold_map[param]
            slope = float(row.get("slope", 0))
            intercept = float(row.get("intercept", 0))
            r2 = float(row.get("R2", 0))
            s_slope = score_param(slope, float(g["slope"]))
            s_intercept = score_param(intercept, float(g["intercept"]))
            s_r2 = 1.0 if r2 >= float(g["R2"]) - 0.05 else 0.0
            row_scores.append((s_slope + s_intercept + s_r2) / 3.0)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


_SCORERS = {
    'fitted_params': score_0,
    'entropy': score_1,
    'linear': score_2,
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
