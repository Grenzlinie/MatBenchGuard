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
    return {'spec': spec}


# === block: score_0 (check id='score_reproduction_results') ===
def score_0(artifact, step, ctx):
    import json

    gold = step.get("gold", {})
    if not gold:
        return 0.0

    try:
        if isinstance(artifact, str):
            data = json.loads(artifact)
        else:
            data = artifact
    except Exception:
        return 0.0

    if not isinstance(data, dict) or "complexes" not in data:
        return 0.0

    complexes = data["complexes"]
    if not isinstance(complexes, list):
        return 0.0
    # map by ligand
    c_map = {}
    for c in complexes:
        lig = c.get("ligand")
        if lig:
            c_map[lig] = c

    expected = ["dpmp-Cl", "dpdm-Cl", "salan-Cl"]
    checks_total = 0
    checks_passed = 0

    def check_tolerance(val, gold_val, tol):
        if val is None:
            return False
        try:
            diff = abs(float(val) - float(gold_val))
            return diff <= tol
        except (TypeError, ValueError):
            return False

    def check_ea_bde(val, gold_val):
        if val is None:
            return False
        try:
            diff = abs(float(val) - float(gold_val))
            threshold = max(0.1 * abs(float(gold_val)), 5.0)
            return diff <= threshold
        except (TypeError, ValueError):
            return False

    for lig in expected:
        gold_c = gold.get(lig)
        if gold_c is None:
            continue
        c = c_map.get(lig)
        if c is None:
            # all checks for this complex fail
            checks_total += 7
            continue
        # delta_E (tol 5.0)
        c_delta = c.get("delta_E_S1_S2")
        if check_tolerance(c_delta, gold_c["delta_E_S1_S2"], 5.0):
            checks_passed += 1
        else:
            checks_passed += 0
        checks_total += 1
        # spin_density_Fe (tol 0.5)
        c_sdFe = c.get("spin_density_Fe")
        if check_tolerance(c_sdFe, gold_c["spin_density_Fe"], 0.5):
            checks_passed += 1
        checks_total += 1
        # spin_density_NTs (tol 0.2)
        c_sdNTs = c.get("spin_density_NTs")
        if check_tolerance(c_sdNTs, gold_c["spin_density_NTs"], 0.2):
            checks_passed += 1
        checks_total += 1
        # LUMO_character (exact match)
        c_lumo_char = c.get("LUMO_character")
        if isinstance(c_lumo_char, str) and c_lumo_char == gold_c["LUMO_character"]:
            checks_passed += 1
        checks_total += 1
        # LUMO_energy (tol 2.0)
        c_lumo_e = c.get("LUMO_energy")
        if check_tolerance(c_lumo_e, gold_c["LUMO_energy"], 2.0):
            checks_passed += 1
        checks_total += 1
        # EA
        c_ea = c.get("EA")
        if check_ea_bde(c_ea, gold_c["EA"]):
            checks_passed += 1
        checks_total += 1
        # BDE
        c_bde = c.get("BDE")
        if check_ea_bde(c_bde, gold_c["BDE"]):
            checks_passed += 1
        checks_total += 1

    if checks_total == 0:
        return 0.0
    return checks_passed / checks_total


_SCORERS = {
    'score_reproduction_results': score_0,
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
