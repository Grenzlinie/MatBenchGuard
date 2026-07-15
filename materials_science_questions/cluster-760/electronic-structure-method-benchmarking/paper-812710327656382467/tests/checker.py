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
    return {"hartree_to_kJ": 2625.5}


# === block: score_0 (check id='schema_and_identity') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 2:
        return 0.0
    ok = 0
    total = 0
    for entry in artifact:
        if not all(k in entry for k in ("molecule","level","E_chelate","E_open","E_HB","RB_D_chelate","RB_D_reference","E_HB1")):
            return 0.0
        if entry["molecule"] not in ("MDA", "ACAC"):
            return 0.0
        if entry["level"] != "B3LYP/6-31G**":
            return 0.0
        ok += 1
    return 1.0 if ok == 2 else 0.0


# === block: score_1 (check id='positive_values') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    fields = ("E_HB", "E_HB1", "RB_D_chelate", "RB_D_reference")
    for entry in artifact:
        for f in fields:
            if entry.get(f, 0) <= 0:
                return 0.0
    return 1.0


# === block: score_2 (check id='mda_gold_compare') ===
def score_2(artifact, step, ctx):
    mol = step.get("molecule", "MDA")
    targets = step["targets"]
    tol = step["tolerance_abs"]
    entry = next((e for e in artifact if e.get("molecule") == mol), None)
    if entry is None:
        return 0.0
    score = 0.0
    for key, gold in targets.items():
        if abs(entry.get(key, 0) - gold) <= tol:
            score += 0.5
        else:
            # partial credit if missing one? keep it strict: zero if out of tolerance
            # but we can still award partial if one of two passes
            pass
    # each of the two fields contributes 0.5 to the step weight; if both pass, total 1.0
    # Actually we return total score, so 0.5 per field. So:
    return score


# === block: score_3 (check id='acac_gold_compare') ===
def score_3(artifact, step, ctx):
    mol = step.get("molecule", "ACAC")
    targets = step["targets"]
    tol = step["tolerance_abs"]
    entry = next((e for e in artifact if e.get("molecule") == mol), None)
    if entry is None:
        return 0.0
    score = 0.0
    for key, gold in targets.items():
        if abs(entry.get(key, 0) - gold) <= tol:
            score += 0.5
    return score


# === block: score_4 (check id='internal_consistency') ===
def score_4(artifact, step, ctx):
    hartree_to_kJ = ctx["hartree_to_kJ"]
    rel_tol = step["rel_tol"]
    cons_tol = step["abs_consistency_tol_kJ"]
    score = 0.0
    for entry in artifact:
        E_HB = entry.get("E_HB", 0.0)
        E_HB1 = entry.get("E_HB1", 0.0)
        E_chelate = entry.get("E_chelate", 0.0)
        E_open = entry.get("E_open", 0.0)
        RB_D_chelate = entry.get("RB_D_chelate", 0.0)
        RB_D_reference = entry.get("RB_D_reference", 0.0)
        # self-consistency: E_HB computed
        comp_E_HB = (E_open - E_chelate) * hartree_to_kJ
        if abs(comp_E_HB - E_HB) > cons_tol:
            return 0.0
        comp_E_HB1 = RB_D_chelate - RB_D_reference
        if abs(comp_E_HB1 - E_HB1) > cons_tol:
            return 0.0
        # relative agreement between E_HB1 and E_HB
        if E_HB <= 0:
            return 0.0
        rel_dev = abs(E_HB1 - E_HB) / E_HB
        if rel_dev > rel_tol:
            return 0.0
        score += 0.5  # each molecule contributes 0.5 to step weight (2 molecules, total 1.0)
    return score


_SCORERS = {
    'schema_and_identity': score_0,
    'positive_values': score_1,
    'mda_gold_compare': score_2,
    'acac_gold_compare': score_3,
    'internal_consistency': score_4,
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
