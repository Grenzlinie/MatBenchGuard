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


# === block: score_0 (check id='step_binding_and_dipole') ===
def score_0(artifact, step, ctx):
    import json
    def score(artifact, step, ctx):
        be = artifact.get("binding_energies")
        dm = artifact.get("dipole_moments")
        if be is None or dm is None:
            return 0.0
        monomers = ["DMAPS","MPC","CBMA"]
        interactions = ["SO4_near_N","H2O_near_N","Zn_near_neg","H2O_near_neg"]
        try:
            barray = {}
            for inter in interactions:
                vals = []
                for m in monomers:
                    vals.append(float(be.get(inter,{}).get(m)))
                barray[inter] = vals
            dvals = [float(dm.get(m)) for m in monomers]
        except (TypeError, ValueError):
            return 0.0
        conditions = []
        # Internal ordering per monomer: SO4_near_N < H2O_near_N, H2O_near_neg < Zn_near_neg
        for i, m in enumerate(monomers):
            conditions.append(barray["SO4_near_N"][i] < barray["H2O_near_N"][i])
            conditions.append(barray["H2O_near_neg"][i] < barray["Zn_near_neg"][i])
        # Cross-monomer ordering for each interaction: DMAPS < MPC < CBMA
        for inter in interactions:
            arr = barray[inter]
            conditions.append(arr[0] < arr[1])  # DMAPS < MPC
            conditions.append(arr[1] < arr[2])  # MPC < CBMA
        # Dipole moment: DMAPS > MPC > CBMA
        conditions.append(dvals[0] > dvals[1])
        conditions.append(dvals[1] > dvals[2])
        total = len(conditions)
        if total == 0:
            return 0.0
        passed = sum(1 for c in conditions if c)
        return passed / total


# === block: score_1 (check id='step_water_states') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        free = artifact.get("free_H2O")
        poly = artifact.get("polymer_fixed_H2O")
        if free is None or poly is None:
            return 0.0
        polymers = ["PDMAPS","PMPC","PCBMA"]
        try:
            free_vals = [float(free.get(p)) for p in polymers]
            poly_vals = [float(poly.get(p)) for p in polymers]
        except (TypeError, ValueError):
            return 0.0
        conditions = []
        # free water: PDMAPS < PMPC and PDMAPS < PCBMA
        conditions.append(free_vals[0] < free_vals[1])
        conditions.append(free_vals[0] < free_vals[2])
        # polymer-fixed: PDMAPS > PMPC and PDMAPS > PCBMA
        conditions.append(poly_vals[0] > poly_vals[1])
        conditions.append(poly_vals[0] > poly_vals[2])
        total = len(conditions)
        passed = sum(1 for c in conditions if c)
        return passed / total


_SCORERS = {
    'step_binding_and_dipole': score_0,
    'step_water_states': score_1,
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
