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
    return {"gold": spec.get("hidden_gold", {})}


# === block: score_0 (check id='carbon_fine_scan') ===
def score_0(artifact, step, ctx):
    rows = {}
    for r in artifact:
        try:
            d = float(r["pore_diameter"])
        except (ValueError, TypeError):
            continue
        rows[d] = r
    score = 0.0

    # 1. correct number of diameters and range (10 rows, 0.36‑0.45)
    if len(rows) == 10 and all(0.36 <= d <= 0.45 for d in rows):
        score += 0.1

    # 2. charge transfer at 0.4 nm within ±0.1 |e| of paper value 0.458
    if 0.4 in rows:
        ct = float(rows[0.4]["charge_transfer"])
        if abs(ct - 0.458) <= 0.1:
            score += 0.2

    # 3. O–O bond length maximum at 0.41 nm and within [1.27, 1.30] Å
    all_bl = [float(r["oo_bond_length"]) for r in artifact]
    if 0.41 in rows:
        bl41 = float(rows[0.41]["oo_bond_length"])
        if 1.27 <= bl41 <= 1.30 and bl41 == max(all_bl) and all_bl.count(bl41) == 1:
            score += 0.2

    # 4. adsorption energy sign change: ≥ 0 for D ≤ 0.40, ≤ 0 for D ≥ 0.41
    ads_sign_ok = True
    for d in [0.36, 0.37, 0.38, 0.39, 0.40]:
        if d in rows:
            ae = float(rows[d]["adsorption_energy"])
            if ae < -0.05:
                ads_sign_ok = False
    for d in [0.41, 0.42, 0.43, 0.44, 0.45]:
        if d in rows:
            ae = float(rows[d]["adsorption_energy"])
            if ae > 0.05:
                ads_sign_ok = False
    if ads_sign_ok:
        score += 0.2

    # 5. Gibbs free energy signs: ≥ 0 for D ≤ 0.39, ≤ 0 for D ≥ 0.43
    gfe_sign_ok = True
    for d in [0.36, 0.37, 0.38, 0.39]:
        if d in rows:
            gfe = float(rows[d]["gibbs_free_energy"])
            if gfe < -0.05:
                gfe_sign_ok = False
    for d in [0.43, 0.44, 0.45]:
        if d in rows:
            gfe = float(rows[d]["gibbs_free_energy"])
            if gfe > 0.05:
                gfe_sign_ok = False
    if gfe_sign_ok:
        score += 0.2

    # 6. charge transfer decreases after 0.4 nm (monotonic overall, checked at D > 0.4)
    if 0.4 in rows:
        ct04 = float(rows[0.4]["charge_transfer"])
        decr_ok = True
        for d in [0.41, 0.42, 0.43, 0.44, 0.45]:
            if d in rows:
                if float(rows[d]["charge_transfer"]) > ct04 + 0.05:
                    decr_ok = False
        if decr_ok:
            score += 0.1

    return score


# === block: score_1 (check id='material_comparison_D0.4') ===
def score_1(artifact, step, ctx):
    gold_vals = ctx["gold"]["material_comparison"]
    score = 0.0
    for r in artifact:
        mat = r.get("material", "")
        if mat in gold_vals:
            ct = float(r.get("charge_transfer", 0))
            if abs(ct - gold_vals[mat]) <= 0.1:
                score += 1.0 / 3.0
    return score


_SCORERS = {
    'carbon_fine_scan': score_0,
    'material_comparison_D0.4': score_1,
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
