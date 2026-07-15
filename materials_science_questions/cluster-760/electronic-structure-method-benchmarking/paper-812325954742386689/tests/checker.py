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


# === block: score_0 (check id='step_geom') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerances"]
    n_fields_total = len(gold) * 6
    n_matched = 0
    for g in gold:
        found = False
        for row in artifact:
            if row.get("Radical","").strip().lower() == g["Radical"].lower() and row.get("Method","").strip().lower() == g["Method"].lower():
                found = True
                if abs(float(row["R_C1O2"]) - g["R_C1O2"]) <= tol["length"]:
                    n_matched += 1
                if abs(float(row["R_O2O3"]) - g["R_O2O3"]) <= tol["length"]:
                    n_matched += 1
                if abs(float(row["Angle_C1O2O3"]) - g["Angle_C1O2O3"]) <= tol["angle"]:
                    n_matched += 1
                for k in ["Torsion_X4","Torsion_X5","Torsion_X6"]:
                    if abs(float(row[k]) - g[k]) <= tol["torsion"]:
                        n_matched += 1
                break
    return n_matched / n_fields_total


# === block: score_1 (check id='step_charge') ===
def score_1(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerances"]
    n_total = 0
    n_matched = 0
    for g in gold:
        for entry in artifact:
            if entry.get("radical","").strip().lower() == g["radical"].lower() and entry.get("method","").strip().lower() == g["method"].lower():
                n_total += 1
                if abs(entry["dipole_moment"] - g["dipole_moment"]) <= tol["dipole"]:
                    n_matched += 1
                atoms_a = entry.get("atoms", [])
                atoms_g = g["atoms"]
                for i in range(min(len(atoms_a), len(atoms_g))):
                    n_total += 1
                    if abs(atoms_a[i]["charge"] - atoms_g[i]["charge"]) <= tol["charge"]:
                        n_matched += 1
                    n_total += 1
                    if abs(atoms_a[i]["spin_density"] - atoms_g[i]["spin_density"]) <= tol["spin"]:
                        n_matched += 1
                break
    return n_matched / n_total if n_total > 0 else 0.0


# === block: score_2 (check id='step_ch_bde') ===
def score_2(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    cols = ["CH4","CH3Cl","CH2Cl2","CHCl3","CHFCl2","CHF2Cl","CH2FCl"]
    total = len(gold) * len(cols)
    passed = 0
    for g in gold:
        for row in artifact:
            if row.get("Level","").strip().lower() == g["Level"].lower():
                for col in cols:
                    try:
                        v = float(row[col])
                    except:
                        continue
                    if abs(v - float(g[col])) <= tol:
                        passed += 1
                break
    return passed / total if total > 0 else 0.0


# === block: score_3 (check id='step_co_bde') ===
def score_3(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    cols = ["CH3-O2","CH2Cl-O2","CHCl2-O2","CCl3-O2","CFCl2-O2","CF2Cl-O2","CHFCl-O2"]
    total = len(gold) * len(cols)
    passed = 0
    for g in gold:
        for row in artifact:
            if row.get("Level","").strip().lower() == g["Level"].lower():
                for col in cols:
                    try:
                        v = float(row[col])
                    except:
                        continue
                    if abs(v - float(g[col])) <= tol:
                        passed += 1
                break
    return passed / total if total > 0 else 0.0


# === block: score_4 (check id='step_ea') ===
def score_4(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    cols = ["CH3-O2","CH2Cl-O2","CHCl2-O2","CCl3-O2","CFCl2-O2","CF2Cl-O2","CHFCl-O2"]
    total = len(gold) * len(cols)
    passed = 0
    for g in gold:
        for row in artifact:
            if row.get("Level","").strip().lower() == g["Level"].lower():
                for col in cols:
                    try:
                        v = float(row[col])
                    except:
                        continue
                    if abs(v - float(g[col])) <= tol:
                        passed += 1
                break
    return passed / total if total > 0 else 0.0


_SCORERS = {
    'step_geom': score_0,
    'step_charge': score_1,
    'step_ch_bde': score_2,
    'step_co_bde': score_3,
    'step_ea': score_4,
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
