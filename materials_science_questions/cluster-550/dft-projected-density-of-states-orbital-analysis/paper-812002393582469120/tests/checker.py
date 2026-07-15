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


# === block: score_0 (check id='heats_of_formation') ===
def score_0(artifact, step, ctx):
    gold = {
        "Sr2Si": {"prototype": "oP12", "value": -37.6},
        "Sr5Si3": {"prototype": "tI32-Cr5B3", "value": -40.2},
        "SrSi": {"prototype": "oC8", "value": -46.7},
        "SrSi2": {"prototype": "cP12", "value": -35.8}
    }
    tolerance = 2.0
    if not isinstance(artifact, list):
        return 0.0
    correct = 0
    for comp, spec in gold.items():
        found = False
        for entry in artifact:
            if entry.get("composition") == comp and entry.get("prototype") == spec["prototype"]:
                try:
                    val = float(entry.get("value_kJ_per_mol_at", None))
                except (TypeError, ValueError):
                    continue
                if abs(val - spec["value"]) <= tolerance:
                    correct += 1
                found = True
                break
    return correct / len(gold)


# === block: score_1 (check id='transition_pressures') ===
def score_1(artifact, step, ctx):
    gold = [
        {"phase": "Sr2Si", "from_lattice": "oP12", "to_lattice": "hP6", "pressure": 5.5},
        {"phase": "Sr5Si3", "from_lattice": "tI32-Cr5B3", "to_lattice": "tI32-Mo5Si3", "pressure": 19.9},
        {"phase": "SrSi", "from_lattice": "oC8", "to_lattice": "oP8", "pressure": 11.8},
        {"phase": "SrSi", "from_lattice": "oP8", "to_lattice": "tP2", "pressure": 60.0}
    ]
    tolerance = 5.0
    if not isinstance(artifact, list):
        return 0.0
    correct = 0
    for g in gold:
        for entry in artifact:
            if (entry.get("phase") == g["phase"] and entry.get("from_lattice") == g["from_lattice"] and entry.get("to_lattice") == g["to_lattice"]):
                try:
                    val = float(entry.get("pressure_GPa", None))
                except (TypeError, ValueError):
                    continue
                if abs(val - g["pressure"]) <= tolerance:
                    correct += 1
                break
    return correct / len(gold)


# === block: score_2 (check id='electronic_properties') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    # band gap
    band_gap_gold = 0.29
    band_gap_tol = 0.1
    band_score = 0.0
    try:
        bg = float(artifact.get("band_gap_Sr2Si_eV", None))
    except (TypeError, ValueError):
        bg = None
    if bg is not None and abs(bg - band_gap_gold) <= band_gap_tol:
        band_score = 1.0
    # charge transfer
    gold_charges = {
        "Sr2Si": {"Sr_charge": 1.48, "Si_charge": -2.97, "ionic_percent": 74},
        "Sr5Si3": {"Sr_charge": 1.52, "Si_charge": -2.53, "ionic_percent": 76},
        "SrSi": {"Sr_charge": 1.38, "Si_charge": -1.38, "ionic_percent": 69},
        "SrSi2": {"Sr_charge": 1.94, "Si_charge": -0.97, "ionic_percent": 97}
    }
    charge_tol = 0.2
    ionic_tol_percent = 10.0
    charge_transfer = artifact.get("charge_transfer", [])
    if not isinstance(charge_transfer, list):
        charge_score = 0.0
    else:
        correct = 0
        for phase, spec in gold_charges.items():
            for entry in charge_transfer:
                if entry.get("phase") == phase:
                    try:
                        sr = float(entry.get("Sr_charge"))
                        si = float(entry.get("Si_charge"))
                        ip = float(entry.get("ionic_percent"))
                    except (TypeError, ValueError, KeyError):
                        continue
                    if (abs(sr - spec["Sr_charge"]) <= charge_tol and
                        abs(si - spec["Si_charge"]) <= charge_tol and
                        abs(ip - spec["ionic_percent"]) <= ionic_tol_percent):
                        correct += 1
                    break
        charge_score = correct / len(gold_charges)
    return 0.5 * band_score + 0.5 * charge_score


_SCORERS = {
    'heats_of_formation': score_0,
    'transition_pressures': score_1,
    'electronic_properties': score_2,
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
