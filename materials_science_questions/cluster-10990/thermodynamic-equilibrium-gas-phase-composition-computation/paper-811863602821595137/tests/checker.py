import os
import json
import csv

# === author imports / helpers ===
import math


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
    import math

    T = 1400.0
    R = 8.314
    RT = R * T
    P0 = 101325.0

    conditions = [
        {"P_Bi": 1.01, "P_O2": 0.00101, "label": "A"},
        {"P_Bi": 1010.0, "P_O2": 0.00101, "label": "B"}
    ]

    # Correct formation coefficients (n_Bi, n_O2, A, B, C, D, E) from Table 1
    coeffs = [
        ("Bi2", 2, 0, -197360.0, -105.9, 0.0, 0.0, 0.0),
        ("Bi3", 3, 0, -319671.0, -231.1, 0.0, 0.0, 0.0),
        ("Bi4", 4, 0, -583571.0, -348.1, 0.0, 0.0, 0.0),
        ("BiO", 1, 0.5, -97000.0, -84.0, 2.6, -0.22, 5.85e6),
        ("Bi2O_linear", 2, 0.5, -706200.0, 2533.0, -310.0, 0.06, 7.4e7),
        ("Bi2O_angular", 2, 0.5, 2.9e6, -24175.0, 3290.0, -1.1, -5.0e8),
        ("Bi2O2", 2, 1.0, 2.64e6, 65230.0, 3190.0, -1.1, -4.8e8),
        ("Bi2O3", 2, 1.5, 8.8e6, -70770.0, 9590.0, -3.16, -1.5e9),
        ("Bi3O4", 3, 2.0, 4.5e6, -43560.0, 6010.0, -2.21, -8.24e8),
        ("Bi4O6", 4, 3.0, -1.24e6, -4860.0, 818.0, -0.46, -27350.0)
    ]

    ref = {}
    for c in conditions:
        P_Bi = c['P_Bi']
        P_O2 = c['P_O2']
        l = c['label']
        # monomer
        ref[('Bi', l)] = P_Bi
        p_bi_atm = P_Bi / P0
        p_o2_atm = P_O2 / P0
        for name, n_Bi, n_O2, A, B, C, D, E in coeffs:
            dG = A + B * T + C * T * math.log(T) + D * T * T + E / T
            K = math.exp(-dG / RT)
            p_prod_atm = K * (p_bi_atm ** n_Bi) * (p_o2_atm ** n_O2)
            ref[(name, l)] = p_prod_atm * P0

    return {'ref': ref}


# === block: score_0 (check id='step_04_partial_pressures') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    ctx = ctx
    step = step
    ref = ctx['ref']
    major_species = step.get('parameters', {}).get('major_species', [])
    major_tol = step.get('parameters', {}).get('major_tol', 0.2)
    minor_tol = step.get('parameters', {}).get('minor_tol', 0.5)
    total = 0
    passed = 0
    for row in artifact:
        species = row.get('species', '')
        try:
            P_Bi_set = float(row['P_Bi_set'])
            P_O2_set = float(row['P_O2_set'])
            P_partial = float(row['P_partial'])
        except (ValueError, KeyError):
            continue
        label = None
        for c in step['parameters']['conditions']:
            if abs(P_Bi_set - c['P_Bi']) < 1e-6 and abs(P_O2_set - c['P_O2']) < 1e-9:
                label = c['label']
                break
        if label is None:
            continue
        ref_p = ref.get((species, label))
        if ref_p is None:
            continue
        if abs(ref_p) > 1e-30:
            rel_err = abs(P_partial - ref_p) / abs(ref_p)
        else:
            rel_err = float('inf')
        tol = major_tol if species in major_species else minor_tol
        if rel_err <= tol:
            passed += 1
        total += 1
    if total == 0:
        return 0.0
    return min(1.0, passed / total)


_SCORERS = {
    'step_04_partial_pressures': score_0,
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
