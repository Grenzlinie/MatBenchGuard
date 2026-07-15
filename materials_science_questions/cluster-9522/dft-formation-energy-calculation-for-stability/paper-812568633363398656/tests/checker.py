import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='results_comparison') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts from CSV
    if not artifact:
        return 0.0
    gold = step.get("gold", {})
    tolerances = step.get("tolerances", {})
    default_fe = tolerances.get("default_formation_energy", 0.02)
    default_lat = tolerances.get("default_lattice", 0.1)
    default_bm = tolerances.get("default_bulk_modulus", 5.0)
    special = tolerances.get("special_phases", {})
    row_map = {}
    for row in artifact:
        name = (row.get("phase","") or "").strip().lower()
        if name:
            row_map[name] = row
    total_fields = 0
    matched = 0
    for phase_name, gv in gold.items():
        row = row_map.get(phase_name.strip().lower())
        if row is None:
            total_fields += 5
            continue
        fe_tol = default_fe
        bm_tol = default_bm
        if phase_name in special:
            if "formation_energy" in special[phase_name]:
                fe_tol = special[phase_name]["formation_energy"]
            if "bulk_modulus" in special[phase_name]:
                bm_tol = special[phase_name]["bulk_modulus"]
        # formation energy
        fe = float(row.get("formation_energy_eV_per_atom", 0.0))
        if abs(fe - float(gv["formation_energy"])) <= fe_tol + 1e-12:
            matched += 1
        total_fields += 1
        # lattice a
        a = float(row.get("a_angstrom", 0.0))
        if abs(a - float(gv["a"])) <= default_lat + 1e-12:
            matched += 1
        total_fields += 1
        # lattice b
        b = float(row.get("b_angstrom", 0.0))
        if abs(b - float(gv["b"])) <= default_lat + 1e-12:
            matched += 1
        total_fields += 1
        # lattice c
        c = float(row.get("c_angstrom", 0.0))
        if abs(c - float(gv["c"])) <= default_lat + 1e-12:
            matched += 1
        total_fields += 1
        # bulk modulus
        bm = float(row.get("bulk_modulus_GPa", 0.0))
        if abs(bm - float(gv["bulk_modulus"])) <= bm_tol + 1e-12:
            matched += 1
        total_fields += 1
    if total_fields == 0:
        return 0.0
    return matched / total_fields


_SCORERS = {
    'results_comparison': score_0,
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
