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


# === block: score_0 (check id='s4') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    if not isinstance(artifact, dict):
        return 0.0
    rr = artifact.get('relaxation_ratio')
    rr_gold = gold.get('relaxation_ratio', 1.21)
    rr_tol = gold.get('tolerance_relaxation_ratio', 0.03)
    rr_ok = isinstance(rr, (int, float)) and abs(float(rr) - rr_gold) <= rr_tol
    pga = artifact.get('P_Ga', {})
    pga_gold = gold.get('P_Ga', {})
    pga_tol = gold.get('tolerance_P_Ga', {})
    pga_hits = 0
    pga_total = 0
    for key, gv in pga_gold.items():
        tol = pga_tol.get(key, 0.1)
        av = pga.get(key)
        pga_total += 1
        if isinstance(av, (int, float)) and isinstance(gv, (int, float)):
            if abs(float(av) - float(gv)) <= tol:
                pga_hits += 1
    p4_arr = artifact.get('P4', [])
    p4_gold_item = gold.get('P4', {})
    p4_tol = gold.get('tolerance_P4', {})
    p4_hits = 0
    p4_total = 0
    if isinstance(p4_arr, list) and len(p4_arr) == 4:
        for item in p4_arr:
            if not isinstance(item, dict):
                continue
            for key, gv in p4_gold_item.items():
                tol = p4_tol.get(key, 0.1)
                av = item.get(key)
                p4_total += 1
                if isinstance(av, (int, float)) and isinstance(gv, (int, float)):
                    if abs(float(av) - float(gv)) <= tol:
                        p4_hits += 1
    ga12_arr = artifact.get('Ga12', [])
    ga12_gold_item = gold.get('Ga12', {})
    ga12_tol = gold.get('tolerance_Ga12', {})
    ga12_hits = 0
    ga12_total = 0
    if isinstance(ga12_arr, list) and len(ga12_arr) == 12:
        for item in ga12_arr:
            if not isinstance(item, dict):
                continue
            for key, gv in ga12_gold_item.items():
                tol = ga12_tol.get(key, 0.1)
                av = item.get(key)
                ga12_total += 1
                if isinstance(av, (int, float)) and isinstance(gv, (int, float)):
                    if abs(float(av) - float(gv)) <= tol:
                        ga12_hits += 1
    total_possible = 1 + pga_total + p4_total + ga12_total
    total_hits = (1 if rr_ok else 0) + pga_hits + p4_hits + ga12_hits
    if total_possible == 0:
        return 0.0
    return total_hits / total_possible


# === block: score_1 (check id='s5') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    tolerance = step.get('tolerance', 0.01)
    if not isinstance(artifact, dict):
        return 0.0
    a1 = artifact.get('A1_01_amplitude')
    a2 = artifact.get('A1_11_amplitude')
    g1 = gold.get('A1_01_amplitude')
    g2 = gold.get('A1_11_amplitude')
    score = 0.0
    if isinstance(a1, (int, float)) and isinstance(g1, (int, float)):
        if abs(float(a1) - float(g1)) <= tolerance:
            score += 0.5
    if isinstance(a2, (int, float)) and isinstance(g2, (int, float)):
        if abs(float(a2) - float(g2)) <= tolerance:
            score += 0.5
    return score


_SCORERS = {
    's4': score_0,
    's5': score_1,
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
