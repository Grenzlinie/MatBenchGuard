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


# === block: score_0 (check id='bulk_properties') ===
def score_0(artifact, step, ctx):
    fields = step.get("fields", [])
    if not isinstance(artifact, dict):
        return 0.0
    score = 0.0
    n = 0
    for f in fields:
        field_name = f["field"]
        if field_name == "total_dos_at_fermi":
            # no paper-reported target exists; exclude from scoring
            continue
        target = f["target"]
        tol_type = f["tolerance_type"]
        tol = f["tolerance"]
        if field_name not in artifact:
            continue
        val = float(artifact[field_name])
        if tol_type == "relative":
            if target == 0.0:
                if abs(val - target) <= tol:
                    score += 1.0
            else:
                if abs(val - target) / abs(target) <= tol:
                    score += 1.0
        else:
            if abs(val - target) <= tol:
                score += 1.0
        n += 1
    if n == 0:
        return 0.0
    return score / n


# === block: score_1 (check id='surface_results') ===
def score_1(artifact, step, ctx):
    targets = step.get("targets", {})
    tol_abs = step.get("tol_abs", {})
    if not isinstance(artifact, dict):
        return 0.0
    tol_be = tol_abs.get("binding_energy", 0.15)
    tol_bl = tol_abs.get("bond_length", 0.1)
    binding_fields = ["binding_energy_Ag_on_WO3", "binding_energy_glucose_on_WO3", "binding_energy_glucose_on_Ag_WO3"]
    bond_fields = ["bond_length_glucose_O_W", "bond_length_glucose_O_Ag"]
    be_ok = True
    for f in binding_fields:
        if f not in artifact:
            be_ok = False
            break
        if abs(float(artifact[f]) - targets[f]) > tol_be:
            be_ok = False
            break
    bl_ok = True
    for f in bond_fields:
        if f not in artifact:
            bl_ok = False
            break
        if abs(float(artifact[f]) - targets[f]) > tol_bl:
            bl_ok = False
            break
    trend_ok = False
    if all(k in artifact for k in ["binding_energy_glucose_on_Ag_WO3", "binding_energy_glucose_on_WO3"]):
        if float(artifact["binding_energy_glucose_on_Ag_WO3"]) <= float(artifact["binding_energy_glucose_on_WO3"]):
            trend_ok = True
    score = 0.0
    if be_ok:
        score += 0.3
    if bl_ok:
        score += 0.2
    if trend_ok:
        score += 0.5
    return score


# === block: score_2 (check id='pdos_comparison') ===
def score_2(artifact, step, ctx):
    required_cols = ["energy_eV", "pdos_W_d_bare", "pdos_W_d_Ag_doped"]
    if not artifact or not isinstance(artifact, list):
        return 0.0
    for row in artifact:
        if not all(col in row for col in required_cols):
            return 0.0
        try:
            row["energy"] = float(row["energy_eV"])
            row["bare"] = float(row["pdos_W_d_bare"])
            row["ag"] = float(row["pdos_W_d_Ag_doped"])
        except (ValueError, TypeError):
            return 0.0
    artifact.sort(key=lambda r: r["energy"])
    energies = [r["energy"] for r in artifact]
    min_e = min(energies)
    max_e = max(energies)
    required_range = step.get("required_energy_range", [-2.0, 2.0])
    if min_e > required_range[0] or max_e < required_range[1]:
        return 0.0
    e_low, e_high = step.get("energy_range", [-0.5, 0.0])
    int_bare = 0.0
    int_ag = 0.0
    for i in range(len(artifact)-1):
        e0 = artifact[i]["energy"]
        e1 = artifact[i+1]["energy"]
        if e1 <= e_low or e0 >= e_high:
            continue
        a = max(e0, e_low)
        b = min(e1, e_high)
        if b <= a:
            continue
        bare0 = artifact[i]["bare"]
        bare1 = artifact[i+1]["bare"]
        ag0 = artifact[i]["ag"]
        ag1 = artifact[i+1]["ag"]
        avg_bare = 0.5 * (bare0 + bare1)
        avg_ag = 0.5 * (ag0 + ag1)
        int_bare += avg_bare * (b - a)
        int_ag += avg_ag * (b - a)
    if int_bare <= 0:
        return 0.0
    enhancement = int_ag / int_bare
    if enhancement >= step.get("enhancement_factor", 1.1):
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'bulk_properties': score_0,
    'surface_results': score_1,
    'pdos_comparison': score_2,
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
