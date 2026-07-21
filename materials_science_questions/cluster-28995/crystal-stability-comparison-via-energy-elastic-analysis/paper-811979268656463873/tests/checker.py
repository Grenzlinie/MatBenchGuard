import os
import json
import csv

# === author imports / helpers ===
import csv, math, re


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
    rows_spec = [
        {"element":"Cu","structure":"f.c.c.","C":11,"K":1,"r1":2.4151,"r2":3.4154,"n1":12,"n2":6,"N_free":9,"C_max":10,"sub":"Ni"},
        {"element":"Ni","structure":"f.c.c.","C":10,"K":1,"r1":2.3543,"r2":3.3295,"n1":12,"n2":6,"N_free":8,"C_max":10,"sub":"Ni"},
        {"element":"Co","structure":"f.c.c.","C":9,"K":1,"r1":2.3679,"r2":3.3487,"n1":12,"n2":6,"N_free":7,"C_max":10,"sub":"Ni"},
        {"element":"Fe","structure":"f.c.c.","C":8,"K":0,"r1":2.4368,"r2":3.4461,"n1":12,"n2":6,"N_free":6,"C_max":10,"sub":"Ni"},
        {"element":"Mn","structure":"f.c.c.","C":7,"K":0,"r1":2.440,"r2":2.5227,"n1":12,"n2":6,"N_free":5,"C_max":10,"sub":"Ni"},
        {"element":"Cr","structure":"f.c.c.","C":6,"K":0,"r1":2.5605,"r2":2.5680,"n1":12,"n2":6,"N_free":5,"C_max":10,"sub":"Ni"},
        {"element":"Sc","structure":"s.c. in f.c.c.","C":3,"K":0,"r1":3.062,"r2":4.3302,"n1":6,"n2":6,"N_free":1,"C_max":6,"sub":"V"},
        {"element":"Ti","structure":"s.c. in f.c.c.","C":4,"K":0,"r1":2.754,"r2":3.8941,"n1":6,"n2":6,"N_free":2,"C_max":6,"sub":"V"},
        {"element":"V","structure":"s.c. in f.c.c.","C":5,"K":0,"r1":2.478,"r2":3.5036,"n1":6,"n2":6,"N_free":3,"C_max":6,"sub":"V"},
        {"element":"Cr","structure":"s.c. in f.c.c.","C":6,"K":0,"r1":2.5605,"r2":2.5680,"n1":6,"n2":6,"N_free":5,"C_max":6,"sub":"V"}
    ]
    tol = 1e-5
    return {"rows_spec": rows_spec, "tol": tol}


# === block: score_0 (check id='step3') ===
def score_0(artifact, step, ctx):
    import re

    # Input parameters as given to the agent (from instruction.md)
    specs = [
        {"element":"Cu","structure":"f.c.c.","C":11,"K":1,"r1":2.4151,"r2":3.4154,"n1":12,"n2":6,"N_free":9,"C_max":10,"sub":"Ni"},
        {"element":"Ni","structure":"f.c.c.","C":10,"K":1,"r1":2.3543,"r2":3.3295,"n1":12,"n2":6,"N_free":8,"C_max":10,"sub":"Ni"},
        {"element":"Co","structure":"f.c.c.","C":9,"K":1,"r1":2.3679,"r2":3.3487,"n1":12,"n2":6,"N_free":7,"C_max":10,"sub":"Ni"},
        {"element":"Fe","structure":"f.c.c.","C":8,"K":0,"r1":2.4368,"r2":3.4461,"n1":12,"n2":6,"N_free":6,"C_max":10,"sub":"Ni"},
        {"element":"Mn","structure":"f.c.c.","C":7,"K":0,"r1":2.440,"r2":2.5227,"n1":12,"n2":6,"N_free":5,"C_max":10,"sub":"Ni"},
        {"element":"Cr","structure":"f.c.c.","C":6,"K":0,"r1":2.5605,"r2":2.5680,"n1":12,"n2":6,"N_free":5,"C_max":10,"sub":"Ni"},
        {"element":"Sc","structure":"s.c. in f.c.c.","C":3,"K":0,"r1":3.062,"r2":4.3302,"n1":6,"n2":6,"N_free":1,"C_max":6,"sub":"V"},
        {"element":"Ti","structure":"s.c. in f.c.c.","C":4,"K":0,"r1":2.754,"r2":3.8941,"n1":6,"n2":6,"N_free":2,"C_max":6,"sub":"V"},
        {"element":"V","structure":"s.c. in f.c.c.","C":5,"K":0,"r1":2.478,"r2":3.5036,"n1":6,"n2":6,"N_free":3,"C_max":6,"sub":"V"},
        {"element":"Cr","structure":"s.c. in f.c.c.","C":6,"K":0,"r1":1.816,"r2":2.5680,"n1":6,"n2":6,"N_free":5,"C_max":6,"sub":"V"},
    ]

    spec_lookup = {}
    for sp in specs:
        spec_lookup[(sp["element"], sp["structure"])] = sp

    # tolerances for numeric self‑consistency checks
    TOL = 0.01

    if not artifact or not isinstance(artifact, list) or not artifact:
        return 0.0

    expected_cols = ["element","structure","R","Z3d","b1","b2","Delta_m","Ntot_8","Ntot_9","EC_8","EC_9"]
    if any(col not in artifact[0] for col in expected_cols):
        return 0.0

    def read_float(row, col):
        try:
            return float(row[col])
        except:
            return None

    total_checks = 0
    passed = 0

    for row in artifact:
        key = (row.get("element"), row.get("structure"))
        sp = spec_lookup.get(key)
        if sp is None:
            continue

        C = sp["C"]
        K = sp["K"]
        r1 = sp["r1"]
        r2 = sp["r2"]
        n1 = sp["n1"]
        n2 = sp["n2"]
        N_free = sp["N_free"]
        C_max = sp["C_max"]
        sub = sp["sub"]

        # read submitted values
        R_a = read_float(row, "R")
        Z_a = read_float(row, "Z3d")
        b1_a = read_float(row, "b1")
        b2_a = read_float(row, "b2")
        dm_a = read_float(row, "Delta_m")
        n8_a = read_float(row, "Ntot_8")
        n9_a = read_float(row, "Ntot_9")

        # compute expected values from the public formula (coefficient 0.065)
        R_exp = 0.065 * ((C/2)**2 - (4.75+K)*(C-8) + 5)
        Z_exp = 9.0 / R_exp
        b1_exp = 0.6780 * n1 * (r1 - R_exp)
        b2_exp = 0.6780 * n2 * (r2 - R_exp)

        if sub == "Ni":
            dm_exp = (3.0*Z_exp - K*b1_exp - C_max) / 2.0
        else:  # V
            dm_exp = (Z_exp - C_max)/2.0 + b2_exp

        n8_exp = 8 + b1_exp - ((3.0*Z_exp - K*b1_exp)/2.0 - 5) * 0.1
        n9_exp = N_free + dm_exp

        # check each numeric field
        for val, exp, name in [
            (R_a, R_exp, "R"),
            (Z_a, Z_exp, "Z3d"),
            (b1_a, b1_exp, "b1"),
            (b2_a, b2_exp, "b2"),
            (dm_a, dm_exp, "Delta_m"),
            (n8_a, n8_exp, "Ntot_8"),
            (n9_a, n9_exp, "Ntot_9")
        ]:
            total_checks += 1
            if val is not None and abs(val - exp) <= TOL:
                passed += 1

        # EC_8 check
        ec8 = row.get("EC_8", "").strip()
        m8 = re.match(r"3d\^(\d+\.\d+)\s+4s\^(\d+\.\d+)$", ec8)
        total_checks += 1
        if m8:
            x8 = float(m8.group(1))
            y8 = float(m8.group(2))
            if n8_a is not None:
                if abs(x8 - round(n8_a, 1)) <= 0.05 and abs(y8 - (C - x8)) <= 0.05:
                    passed += 1

        # EC_9 check
        ec9 = row.get("EC_9", "").strip()
        m9 = re.match(r"3d\^(\d+\.\d+)\s+4s\^(\d+\.\d+)$", ec9)
        total_checks += 1
        if m9:
            x9 = float(m9.group(1))
            y9 = float(m9.group(2))
            if n9_a is not None:
                if abs(x9 - round(n9_a, 1)) <= 0.05 and abs(y9 - (C - x9)) <= 0.05:
                    passed += 1

    if total_checks == 0:
        return 0.0
    return passed / total_checks


_SCORERS = {
    'step3': score_0,
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
