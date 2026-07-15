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
    gold = spec['steps'][0]['gold']
    tolerance = spec['steps'][0]['tolerance_abs']
    trend_weight = spec['steps'][0]['trend_weight']
    value_weight = spec['steps'][0]['value_weight']
    return {
        'gold': gold,
        'tolerance': tolerance,
        'trend_weight': trend_weight,
        'value_weight': value_weight
    }


# === block: score_0 (check id='step_03_formation_energies') ===
def score_0(artifact, step, ctx):
    import math

    trend_weight = ctx['trend_weight']
    value_weight = ctx['value_weight']

    # Material‑level expected minimum formation energies from the paper’s explicit statements.
    # Pure SrFeO₃ : “around 2.0 eV”
    # Cu‑doped (SrFe₀.₇₅Cu₀.₂₅O₃) : “decreases sharply to 0.9 eV”
    expected_min = {
        'SrFeO3': 2.0,
        'SrFe0.75Cu0.25O3': 0.9,
    }
    # Tolerance generous enough to absorb differences between VASP (original paper)
    # and open‑source DFT codes with different pseudopotentials / settings.
    tol = 0.5

    # Build dict from rows
    energies = {}
    for row in artifact:
        mat = row.get('material', '').strip()
        site = row.get('vacancy_site', '').strip()
        val = None
        try:
            val = float(row['formation_energy_eV'])
        except (ValueError, TypeError):
            return 0.0
        energies.setdefault(mat, {})[site] = val

    # Required rows check
    required = {
        'SrFeO3': ['V_O1', 'V_O2'],
        'SrFe0.75Cu0.25O3': ['V_O1', 'V_O2', 'V_O3', 'V_O4'],
    }
    for mat, sites in required.items():
        if mat not in energies:
            return 0.0
        for s in sites:
            if s not in energies[mat]:
                return 0.0

    # Compute minimum formation energy for each material
    pure_min = min(energies['SrFeO3'].values())
    cu_min   = min(energies['SrFe0.75Cu0.25O3'].values())

    # Trend: Cu‑doped minimum must be lower than pure minimum
    trend_ok = 1.0 if cu_min < pure_min else 0.0

    # How many material minima lie within the expected paper value? (0, 1, or 2)
    pure_within = 1.0 if abs(pure_min - expected_min['SrFeO3']) <= tol else 0.0
    cu_within   = 1.0 if abs(cu_min   - expected_min['SrFe0.75Cu0.25O3']) <= tol else 0.0
    value_ok = (pure_within + cu_within) / 2.0

    score = trend_weight * trend_ok + value_weight * value_ok
    return max(0.0, min(score, 1.0))


_SCORERS = {
    'step_03_formation_energies': score_0,
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
