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
    import csv
    import os, math

    def parse_gold(checks):
        for check in checks:
            if check.get('output_file') == 'step_07_computed_properties.csv':
                gold_rows = check.get('gold_values', [])
                gold = {}
                for row in gold_rows:
                    cid = int(row['compound_id'])
                    gold[cid] = row
                tols = check.get('tolerances', {})
                cols = list(gold_rows[0].keys()) if gold_rows else []
                return {'gold': gold, 'tolerances': tols, 'cols': cols}
        return {'gold': {}, 'tolerances': {}, 'cols': []}

    checks = spec.get("checks", [])
    return parse_gold(checks)


# === block: score_0 (check id='table1_reproduction') ===
def score_0(artifact, step, ctx):
    import math

    gold_values = [
        {"compound_id": 1, "V_m": 240.5, "A_S": 239.2, "ρ": 1.79, "V̄_S": 7.5, "V̄_S^+": 24.1, "V̄_S^-": -19.1, "σ_tot^2": 275.9, "σ_+^2": 184.6, "σ_-^2": 91.3, "ν": 0.221, "vσ_tot^2": 61.1, "Π": 21.0, "ΔH_sub^°": 31.1, "Δ_fH^°(g)": 280.4, "Δ_fH^°(s)": 249.3},
        {"compound_id": 2, "V_m": 260.3, "A_S": 259.0, "ρ": 1.91, "V̄_S": 4.5, "V̄_S^+": 28.6, "V̄_S^-": -19.8, "σ_tot^2": 467.2, "σ_+^2": 364.1, "σ_-^2": 103.1, "ν": 0.172, "vσ_tot^2": 80.3, "Π": 24.4, "ΔH_sub^°": 35.7, "Δ_fH^°(g)": 277.2, "Δ_fH^°(s)": 241.5},
        {"compound_id": 3, "V_m": 301.0, "A_S": 295.2, "ρ": 1.89, "V̄_S": 5.7, "V̄_S^+": 20.9, "V̄_S^-": -12.7, "σ_tot^2": 222.7, "σ_+^2": 150.8, "σ_-^2": 71.9, "ν": 0.219, "vσ_tot^2": 48.7, "Π": 17.1, "ΔH_sub^°": 37.7, "Δ_fH^°(g)": 347.3, "Δ_fH^°(s)": 309.6},
        {"compound_id": 4, "V_m": 319.8, "A_S": 310.9, "ρ": 1.93, "V̄_S": 6.0, "V̄_S^+": 21.7, "V̄_S^-": -12.1, "σ_tot^2": 236.6, "σ_+^2": 176.5, "σ_-^2": 60.1, "ν": 0.189, "vσ_tot^2": 44.8, "Π": 17.4, "ΔH_sub^°": 39.8, "Δ_fH^°(g)": 328.4, "Δ_fH^°(s)": 288.6},
        {"compound_id": 5, "V_m": 399.5, "A_S": 380.9, "ρ": 1.93, "V̄_S": 4.8, "V̄_S^+": 19.4, "V̄_S^-": -12.2, "σ_tot^2": 230.4, "σ_+^2": 154.9, "σ_-^2": 75.5, "ν": 0.220, "vσ_tot^2": 50.8, "Π": 16.1, "ΔH_sub^°": 53.5, "Δ_fH^°(g)": 298.8, "Δ_fH^°(s)": 245.3},
        {"compound_id": 6, "V_m": 418.2, "A_S": 396.2, "ρ": 1.96, "V̄_S": 5.0, "V̄_S^+": 20.3, "V̄_S^-": -12.1, "σ_tot^2": 242.5, "σ_+^2": 173.2, "σ_-^2": 69.3, "ν": 0.204, "vσ_tot^2": 49.5, "Π": 16.6, "ΔH_sub^°": 56.5, "Δ_fH^°(g)": 278.9, "Δ_fH^°(s)": 222.4},
        {"compound_id": 7, "V_m": 378.6, "A_S": 368.5, "ρ": 1.87, "V̄_S": 3.4, "V̄_S^+": 15.7, "V̄_S^-": -13.2, "σ_tot^2": 204.3, "σ_+^2": 88.7, "σ_-^2": 115.6, "ν": 0.246, "vσ_tot^2": 50.2, "Π": 14.4, "ΔH_sub^°": 50.9, "Δ_fH^°(g)": 428.3, "Δ_fH^°(s)": 377.4},
        {"compound_id": 8, "V_m": 396.9, "A_S": 383.2, "ρ": 1.94, "V̄_S": 3.9, "V̄_S^+": 17.0, "V̄_S^-": -14.4, "σ_tot^2": 238.4, "σ_+^2": 103.9, "σ_-^2": 134.1, "ν": 0.246, "vσ_tot^2": 58.4, "Π": 15.6, "ΔH_sub^°": 54.8, "Δ_fH^°(g)": 430.6, "Δ_fH^°(s)": 375.8},
        {"compound_id": 9, "V_m": 307.9, "A_S": 301.0, "ρ": 1.86, "V̄_S": 4.4, "V̄_S^+": 23.5, "V̄_S^-": -19.0, "σ_tot^2": 252.4, "σ_+^2": 178.3, "σ_-^2": 74.1, "ν": 0.207, "vσ_tot^2": 52.2, "Π": 21.2, "ΔH_sub^°": 39.1, "Δ_fH^°(g)": 213.4, "Δ_fH^°(s)": 174.3},
        {"compound_id": 10, "V_m": 327.6, "A_S": 317.0, "ρ": 1.90, "V̄_S": 5.3, "V̄_S^+": 23.2, "V̄_S^-": -16.0, "σ_tot^2": 281.4, "σ_+^2": 214.0, "σ_-^2": 67.4, "ν": 0.182, "vσ_tot^2": 51.2, "Π": 19.8, "ΔH_sub^°": 41.6, "Δ_fH^°(g)": 206.0, "Δ_fH^°(s)": 164.4}
    ]

    gold_map = {item["compound_id"]: item for item in gold_values}

    tolerances = {
        "ρ": {"abs": 0.05},
        "ΔH_sub^°": {"abs": 5.0},
        "Δ_fH^°(g)": {"abs": 5.0},
        "Δ_fH^°(s)": {"abs": 5.0},
        "V_m": {"rel": 0.1},
        "A_S": {"rel": 0.1},
        "V̄_S": {"rel": 0.1},
        "V̄_S^+": {"rel": 0.1},
        "V̄_S^-": {"rel": 0.1},
        "σ_tot^2": {"rel": 0.1},
        "σ_+^2": {"rel": 0.1},
        "σ_-^2": {"rel": 0.1},
        "ν": {"rel": 0.1},
        "vσ_tot^2": {"rel": 0.1},
        "Π": {"rel": 0.1}
    }

    rows = artifact
    if not rows:
        return 0.0

    prop_cols = [k for k in gold_values[0].keys() if k != "compound_id"]

    compound_scores = []
    agent_by_id = {}
    for r in rows:
        cid = int(r.get("compound_id", -1))
        if cid > 0:
            agent_by_id[cid] = r

    for cid in range(1, 11):
        if cid not in agent_by_id or cid not in gold_map:
            compound_scores.append(0.0)
            continue
        agent = agent_by_id[cid]
        gold = gold_map[cid]
        passed = 0
        total = 0
        for col in prop_cols:
            if col not in agent or col not in gold:
                continue
            try:
                aval = float(agent[col])
                gval = float(gold[col])
            except (ValueError, TypeError):
                continue
            total += 1
            tol = tolerances.get(col, {})
            abs_tol = tol.get("abs")
            rel_tol = tol.get("rel")
            diff = abs(aval - gval)
            ok = False
            if abs_tol is not None and diff <= abs_tol:
                ok = True
            elif rel_tol is not None and abs(gval) > 1e-12 and diff / abs(gval) <= rel_tol:
                ok = True
            if ok:
                passed += 1
        if total > 0:
            compound_scores.append(passed / total)
        else:
            compound_scores.append(0.0)

    if compound_scores:
        return sum(compound_scores) / len(compound_scores)
    else:
        return 0.0


_SCORERS = {
    'table1_reproduction': score_0,
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
