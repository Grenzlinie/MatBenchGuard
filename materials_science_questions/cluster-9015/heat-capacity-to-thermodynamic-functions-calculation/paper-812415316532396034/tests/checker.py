import os
import json
import csv

# === author imports / helpers ===
def _score_thermo_table(artifact, step, ctx):
    gold_rows = ctx["gold_tables"].get(step.get("id"), [])
    if not gold_rows:
        return 0.0
    art_by_T = {}
    for row in artifact:
        try:
            t = float(row["T(K)"])
            art_by_T[int(t)] = (
                float(row["Cp(J/K/mol)"]),
                float(row["H_H298(J/mol)"]),
                float(row["S(J/K/mol)"]),
                float(row["G_H298_div_T(J/K/mol)"]),
            )
        except (ValueError, KeyError):
            continue
    tol = step.get("tolerances", {})
    cp_rel = tol.get("Cp_rel", 0.03)
    h_rel = tol.get("H_rel", 0.03)
    s_abs = tol.get("S_abs", 1.0)
    g_abs = tol.get("G_abs", 1.0)
    passed = 0
    total = len(gold_rows)
    for gold in gold_rows:
        T = int(gold["T"])
        if T not in art_by_T:
            continue
        a_cp, a_h, a_s, a_g = art_by_T[T]
        g_cp = float(gold["Cp"])
        g_h = float(gold["H_H298"])
        g_s = float(gold["S"])
        g_g = float(gold["G"])
        ok = True
        if g_cp != 0:
            if abs(a_cp - g_cp) / abs(g_cp) > cp_rel:
                ok = False
        elif abs(a_cp) > 1e-6:
            ok = False
        if g_h != 0:
            if abs(a_h - g_h) / abs(g_h) > h_rel:
                ok = False
        elif abs(a_h) > 1e-6:
            ok = False
        if abs(a_s - g_s) > s_abs:
            ok = False
        if abs(a_g - g_g) > g_abs:
            ok = False
        if ok:
            passed += 1
    return passed / total if total > 0 else 0.0


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
    gold_tables = {}
    for step in spec.get("steps", []):
        rid = step.get("id")
        gt = step.get("gold_table")
        if rid and gt:
            gold_tables[rid] = gt
    return {"gold_tables": gold_tables}


# === block: score_0 (check id='compute_puc082_thermo') ===
def score_0(artifact, step, ctx):
    return _score_thermo_table(artifact, step, ctx)


# === block: score_1 (check id='compute_pu2c3_thermo') ===
def score_1(artifact, step, ctx):
    return _score_thermo_table(artifact, step, ctx)


_SCORERS = {
    'compute_puc082_thermo': score_0,
    'compute_pu2c3_thermo': score_1,
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
