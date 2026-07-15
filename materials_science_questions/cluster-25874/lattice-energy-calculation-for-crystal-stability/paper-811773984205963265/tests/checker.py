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
    return {"gold_table": spec["steps"][0]["gold"]}


# === block: score_0 (check id='check_minimization_results') ===
def score_0(artifact, step, ctx):
    gold_list = ctx.get("gold_table", [])
    if not isinstance(artifact, list) or len(artifact) != 3:
        return 0.0
    passed = 0
    def rel_ok(val, gold_val, tol):
        if gold_val == 0:
            return abs(val) <= tol
        return abs(val - gold_val) <= tol * abs(gold_val)
    def abs_ok(val, gold_val, tol):
        return abs(val - gold_val) <= tol
    for entry in artifact:
        comp = entry.get("compound")
        sg = entry.get("space_group")
        gold = next((g for g in gold_list if g.get("compound") == comp and g.get("space_group") == sg), None)
        if not gold:
            continue
        ok = True
        cell = entry.get("cell", {})
        gc = gold["cell"]
        ok = ok and rel_ok(cell.get("a", 0), gc["a"], 0.05)
        ok = ok and rel_ok(cell.get("b", 0), gc["b"], 0.05)
        ok = ok and rel_ok(cell.get("c", 0), gc["c"], 0.05)
        if "beta" in gc:
            ok = ok and abs_ok(cell.get("beta", 0), gc["beta"], 2.0)
        mol = entry.get("molecular_coordinates", {})
        gm = gold["molecular_coordinates"]
        ok = ok and abs_ok(mol.get("x", 0), gm["x"], 0.1)
        ok = ok and abs_ok(mol.get("y", 0), gm["y"], 0.1)
        ok = ok and abs_ok(mol.get("z", 0), gm["z"], 0.1)
        ok = ok and abs_ok(mol.get("theta", 0), gm["theta"], 2.0)
        ok = ok and abs_ok(mol.get("phi", 0), gm["phi"], 2.0)
        ok = ok and abs_ok(mol.get("psi", 0), gm["psi"], 2.0)
        ok = ok and abs_ok(entry.get("agreement_factor_phi", 0), gold["agreement_factor_phi"], 0.005)
        ok = ok and abs_ok(entry.get("packing_coefficient_K", 0), gold["packing_coefficient_K"], 0.05)
        ok = ok and abs_ok(entry.get("lattice_energy_E", 0), gold["lattice_energy_E"], 1.0)
        ok = ok and bool(entry.get("hessian_positive_eigenvalues", False)) == bool(gold["hessian_positive_eigenvalues"])
        if ok:
            passed += 1
    return passed / 3.0


_SCORERS = {
    'check_minimization_results': score_0,
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
