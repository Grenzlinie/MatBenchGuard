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
    step = None
    for s in spec.get("steps", []):
        if s.get("id") == "step2":
            step = s
            break
    if step is None:
        return {}
    gold = step.get("gold", {})
    tolerances = step.get("tolerances", {})
    return {"gold": gold, "tolerances": tolerances, "penalty_range_factor": step.get("penalty_range_factor", 2.0)}


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    if not isinstance(artifact, dict):
        return 0.0
    expected_methods = ["MM2", "MNDO", "STO-3G", "3-21G"]
    for m in expected_methods:
        if m not in artifact:
            return 0.0
    gold = ctx.get("gold", {})
    factor = ctx.get("penalty_range_factor", 2.0)
    gold_bl = gold.get("bond_lengths", {})
    gold_ba = gold.get("bond_angles", {})
    gold_dm = gold.get("dipole_moment", 0.0)
    bl_keys = ["C=O", "C1-C2", "C1-C4", "C1...C3"]
    ba_keys = ["C1C2C3", "C1C4C3", "C2MC4"]

    tol_overrides = {
        "MM2":    {"bond_lengths_tol": 0.1, "bond_angles_tol": 5.0, "dipole_moment_tol": 0.2},
        "MNDO":   {"bond_lengths_tol": 0.1, "bond_angles_tol": 5.0, "dipole_moment_tol": 1.0},
        "STO-3G": {"bond_lengths_tol": 0.03, "bond_angles_tol": 3.0, "dipole_moment_tol": 1.5},
        "3-21G":  {"bond_lengths_tol": 0.03, "bond_angles_tol": 3.0, "dipole_moment_tol": 0.3},
    }

    total = 0.0
    count = 0
    def param_score(dev, tol):
        if dev <= tol:
            return 1.0
        excess = dev - tol
        if excess >= factor * tol:
            return 0.0
        return max(0.0, 1.0 - excess / (factor * tol))

    for method in expected_methods:
        data = artifact.get(method)
        if not isinstance(data, dict):
            return 0.0
        bl_data = data.get("bond_lengths")
        ba_data = data.get("bond_angles")
        dm = data.get("dipole_moment")
        if not isinstance(bl_data, dict) or not isinstance(ba_data, dict) or dm is None:
            return 0.0
        tolerances = tol_overrides.get(method, {})
        bl_tol = tolerances.get("bond_lengths_tol", 0.02)
        ba_tol = tolerances.get("bond_angles_tol", 2.0)
        dm_tol = tolerances.get("dipole_moment_tol", 0.1)
        for key in bl_keys:
            val = bl_data.get(key)
            if val is None:
                return 0.0
            dev = abs(val - gold_bl.get(key, 0.0))
            total += param_score(dev, bl_tol)
            count += 1
        for key in ba_keys:
            val = ba_data.get(key)
            if val is None:
                return 0.0
            dev = abs(val - gold_ba.get(key, 0.0))
            total += param_score(dev, ba_tol)
            count += 1
        dev = abs(dm - gold_dm)
        total += param_score(dev, dm_tol)
        count += 1
    if count == 0:
        return 0.0
    return total / count


_SCORERS = {
    'step2': score_0,
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
