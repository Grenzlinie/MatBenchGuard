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


# === block: score_0 (check id='step_05') ===
def score_0(artifact, step, ctx):
        # artifact is list of dicts, loaded from CSV
        if not isinstance(artifact, list) or len(artifact) < 6:
            return 0.0
        rows = artifact
        gold = step.get("targets", {})
        binding_tol = step.get("binding_tolerance_kJmol", 25.0)
        bond_tol = step.get("bond_tolerance_A", 0.05)
        diff_tol = step.get("diff_tolerance_kJmol", 15.0)

        # sub-weights
        w_struct = 0.1
        w_binding = 0.3
        w_bond = 0.3
        w_diff = 0.2
        w_order = 0.1

        # 1. Structural: all 6 surface-method pairs present
        expected_surfaces = {"100-A", "100-B", "110-A"}
        expected_methods = {"PBE+U", "HSE06"}
        found = {}
        for row in rows:
            s = str(row.get("surface", "")).strip()
            m = str(row.get("method", "")).strip()
            found[(s, m)] = found.get((s, m), 0) + 1
        expected_pairs = {(s, m) for s in expected_surfaces for m in expected_methods}
        struct_ok = set(found.keys()) == expected_pairs and all(v == 1 for v in found.values())
        struct_score = 1.0 if struct_ok else 0.0

        # 2. Binding energy & bond length errors
        be_errors = []
        bond_errors = []
        for row in rows:
            s = str(row.get("surface", "")).strip()
            m = str(row.get("method", "")).strip()
            if (s, m) not in expected_pairs:
                continue
            t = gold.get(s, {}).get(m, {})
            if not t:
                continue
            # binding energy
            be = float(row.get("binding_energy_kJmol", 0))
            be_ref = t.get("binding")
            if be_ref is not None:
                be_errors.append(abs(be - be_ref))
            # Co-O bond
            co_o = float(row.get("Co_O_bond_A", 0))
            co_o_ref = t.get("co_o")
            if co_o_ref is not None:
                bond_errors.append(abs(co_o - co_o_ref))
            # O-O lattice bond (nullable)
            oo_str = str(row.get("O_O_lattice_bond_A", "")).strip()
            oo = float(oo_str) if oo_str and oo_str.lower() not in ("", "null", "na") else None
            oo_ref = t.get("oo_lattice")
            if oo_ref is not None:
                if oo is None:
                    # missing expected value -> assign maximum error
                    bond_errors.append(bond_tol)
                else:
                    bond_errors.append(abs(oo - oo_ref))

        if be_errors:
            be_max = max(be_errors)
            binding_score = max(0.0, 1.0 - be_max / binding_tol)
        else:
            binding_score = 0.0

        if bond_errors:
            bond_max = max(bond_errors)
            bond_score = max(0.0, 1.0 - bond_max / bond_tol)
        else:
            bond_score = 0.0

        # 3. PBE+U vs HSE06 difference per surface
        pbeu = {}
        hse = {}
        for row in rows:
            s = str(row.get("surface", "")).strip()
            m = str(row.get("method", "")).strip()
            be = float(row.get("binding_energy_kJmol", 0))
            if m == "PBE+U":
                pbeu[s] = be
            elif m == "HSE06":
                hse[s] = be
        diff_score = 0.0
        if set(pbeu.keys()) == expected_surfaces and set(hse.keys()) == expected_surfaces:
            diffs = [abs(pbeu[s] - hse[s]) for s in expected_surfaces]
            if diffs:
                max_diff = max(diffs)
                diff_score = max(0.0, 1.0 - max_diff / diff_tol)

        # 4. Surface ordering (PBE+U): 110-A > 100-A > 100-B
        order_score = 0.0
        if set(pbeu.keys()) == expected_surfaces:
            ok1 = pbeu["110-A"] > pbeu["100-A"]
            ok2 = pbeu["100-A"] > pbeu["100-B"]
            order_score = (ok1 + ok2) / 2.0

        total = (struct_score * w_struct + binding_score * w_binding +
                 bond_score * w_bond + diff_score * w_diff + order_score * w_order)
        return max(0.0, min(1.0, total))


_SCORERS = {
    'step_05': score_0,
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
