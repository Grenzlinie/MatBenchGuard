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


# === block: score_0 (check id='step_01_bulk') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts with property,value,unit
    targets = step.get("targets", {})
    sub_scores = []
    for prop, tdef in targets.items():
        tol = tdef.get("tolerance_abs", 0)
        gold = tdef.get("value")
        unit = tdef.get("unit", "")
        match = [r for r in rows if r.get("property", "").strip().lower() == prop.lower()]
        if not match:
            sub_scores.append(0.0)
            continue
        try:
            val = float(match[0]["value"])
        except (ValueError, TypeError):
            sub_scores.append(0.0)
            continue
        if abs(val - gold) <= tol:
            sub_scores.append(1.0)
        else:
            sub_scores.append(0.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


# === block: score_1 (check id='step_03_adsorption') ===
def score_1(artifact, step, ctx):
    rows = artifact
    targets = step.get("targets", {})
    gold_A = targets.get("site_A_ZPE", {}).get("value")
    tol_A = targets.get("site_A_ZPE", {}).get("tolerance_abs", 10.0)
    # build dict
    zpe_by_site = {}
    for r in rows:
        site = r.get("site", "").strip().upper()
        if site not in ("A", "C", "E"):
            continue
        try:
            zpe = float(r.get("adsorption_energy_with_ZPE_kJ_per_mol"))
        except (ValueError, TypeError):
            continue
        zpe_by_site[site] = zpe
    if "A" not in zpe_by_site:
        return 0.0
    zpe_A = zpe_by_site["A"]
    # site A direct match
    match_score = 1.0 if abs(zpe_A - gold_A) <= tol_A else 0.0
    # ordering check: A should be more negative than C and E
    order_ok = True
    if "C" in zpe_by_site:
        order_ok = order_ok and (zpe_A < zpe_by_site["C"])
    if "E" in zpe_by_site:
        order_ok = order_ok and (zpe_A < zpe_by_site["E"])
    order_score = 1.0 if order_ok else 0.0
    return 0.7 * match_score + 0.3 * order_score


# === block: score_2 (check id='step_04_penetration') ===
def score_2(artifact, step, ctx):
    artifact_dict = artifact
    targets = step.get("targets", {})
    # Ensure OS_to_OS_barrier_eV is scored even if not included in grading_spec targets
    if "OS_to_OS_barrier_eV" not in targets:
        targets["OS_to_OS_barrier_eV"] = {
            "value": 1.64,
            "tolerance_abs": 0.1
        }
    sub_scores = []
    for key, tdef in targets.items():
        gold = tdef.get("value")
        tol = tdef.get("tolerance_abs", 0.0)
        if key not in artifact_dict:
            sub_scores.append(0.0)
            continue
        try:
            val = float(artifact_dict[key])
        except (ValueError, TypeError):
            sub_scores.append(0.0)
            continue
        if abs(val - gold) <= tol:
            sub_scores.append(1.0)
        else:
            sub_scores.append(0.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


# === block: score_3 (check id='step_05_vacancy') ===
def score_3(artifact, step, ctx):
    artifact_dict = artifact
    key = step.get("key", "h_near_vacancy_relative_energy_eV")
    if key not in artifact_dict:
        return 0.0
    try:
        val = float(artifact_dict[key])
    except (ValueError, TypeError):
        return 0.0
    return 1.0 if val < 0.0 else 0.0


_SCORERS = {
    'step_01_bulk': score_0,
    'step_03_adsorption': score_1,
    'step_04_penetration': score_2,
    'step_05_vacancy': score_3,
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
