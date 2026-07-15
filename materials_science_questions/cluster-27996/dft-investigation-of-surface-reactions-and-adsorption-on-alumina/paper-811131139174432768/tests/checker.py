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


# === block: score_0 (check id='total_energies') ===
def score_0(artifact, step, ctx):
    hartree_tol = step.get("tolerance_abs_hartree", 0.001)
    expected = step["expected"]
    n_total = 0
    n_pass = 0
    # ions
    for ion, val in expected.get("ions", {}).items():
        n_total += 1
        art_val = artifact.get("ions", {}).get(ion, {}).get("total_energy_6_311G2dp")
        if art_val is not None and abs(art_val - val) <= hartree_tol:
            n_pass += 1
    # molecules
    for mol, val in expected.get("molecules", {}).items():
        n_total += 1
        art_val = artifact.get("molecules", {}).get(mol, {}).get("total_energy_6_311G2dp")
        if art_val is not None and abs(art_val - val) <= hartree_tol:
            n_pass += 1
    # complexes
    for mol_name in ["anthracene", "phenanthrene"]:
        for cation, sps in expected.get(mol_name, {}).items():
            art_sp_list = artifact.get(mol_name, {}).get(cation, {}).get("stationary_points", [])
            for label, val in sps.items():
                n_total += 1
                sp = next((s for s in art_sp_list if s.get("label") == label), None)
                if sp and "total_energy_6_311G2dp" in sp:
                    art_val = sp["total_energy_6_311G2dp"]
                    if abs(art_val - val) <= hartree_tol:
                        n_pass += 1
    score = n_pass / n_total if n_total else 0.0
    return score


# === block: score_1 (check id='relative_energies') ===
def score_1(artifact, step, ctx):
    hartree_to_kcal = 627.509
    tol = step["tolerance_kcal"]
    gold = step["gold_relative"]
    ref_labels = step["reference_labels"]
    n_total = 0
    n_pass = 0
    for mol_name in ["anthracene", "phenanthrene"]:
        mol_gold = gold.get(mol_name, {})
        mol_ref = ref_labels.get(mol_name, {})
        for cation, gold_sp in mol_gold.items():
            art_sp_list = artifact.get(mol_name, {}).get(cation, {}).get("stationary_points", [])
            ref_label = mol_ref.get(cation)
            if not ref_label:
                continue
            ref_sp = next((s for s in art_sp_list if s.get("label") == ref_label), None)
            if ref_sp is None or "total_energy_6_311G2dp" not in ref_sp:
                continue
            E_ref = ref_sp["total_energy_6_311G2dp"]
            for label, gold_val in gold_sp.items():
                n_total += 1
                sp = next((s for s in art_sp_list if s.get("label") == label), None)
                if sp and "total_energy_6_311G2dp" in sp:
                    rel = (sp["total_energy_6_311G2dp"] - E_ref) * hartree_to_kcal
                    if abs(rel - gold_val) <= tol:
                        n_pass += 1
    score = n_pass / n_total if n_total else 0.0
    return score


# === block: score_2 (check id='binding_energies') ===
def score_2(artifact, step, ctx):
    hartree_to_kcal = 627.509
    tol = step["tolerance_kcal"]
    gold_bind = step["gold_binding"]
    g_min = step["global_minimum"]
    n_pass = 0
    n_total = 0
    ions_art = artifact.get("ions", {})
    mols_art = artifact.get("molecules", {})
    for mol_name in ["anthracene", "phenanthrene"]:
        mol_data = mols_art.get(mol_name, {})
        E_mol = mol_data.get("total_energy_6_311G2dp")
        zpve_mol = mol_data.get("zpve_kcal_per_mol")
        if E_mol is None or zpve_mol is None:
            continue
        for cation, label in g_min.get(mol_name, {}).items():
            n_total += 1
            ion_data = ions_art.get(cation, {})
            E_ion = ion_data.get("total_energy_6_311G2dp")
            if E_ion is None:
                continue
            art_sp_list = artifact.get(mol_name, {}).get(cation, {}).get("stationary_points", [])
            sp = next((s for s in art_sp_list if s.get("label") == label), None)
            if sp is None:
                continue
            E_complex = sp.get("total_energy_6_311G2dp")
            zpve_complex = sp.get("zpve_kcal_per_mol")
            if E_complex is None or zpve_complex is None:
                continue
            bind_electronic = (E_mol + E_ion - E_complex) * hartree_to_kcal
            bind_total = bind_electronic + (zpve_mol - zpve_complex)
            gold_val = gold_bind.get(mol_name, {}).get(cation)
            if gold_val is None:
                continue
            if abs(bind_total - gold_val) <= tol:
                n_pass += 1
    score = n_pass / n_total if n_total else 0.0
    return score


# === block: score_3 (check id='activation_energies') ===
def score_3(artifact, step, ctx):
    hartree_to_kcal = 627.509
    tol = step["tolerance_kcal"]
    gold_act = step["gold_activation"]
    pathways = step["activation_pathways"]
    n_pass = 0
    n_total = 0
    for mol_name in ["anthracene", "phenanthrene"]:
        for cation, paths in pathways.get(mol_name, {}).items():
            if not isinstance(paths, list):
                paths = [paths]
            art_sp_list = artifact.get(mol_name, {}).get(cation, {}).get("stationary_points", [])
            for path in paths:
                n_total += 1
                reactant = path["reactant"]
                ts = path["ts"]
                gold_key = path.get("gold_key")
                sp_r = next((s for s in art_sp_list if s.get("label") == reactant), None)
                sp_ts = next((s for s in art_sp_list if s.get("label") == ts), None)
                if not sp_r or not sp_ts or "total_energy_6_311G2dp" not in sp_r or "total_energy_6_311G2dp" not in sp_ts:
                    continue
                act = (sp_ts["total_energy_6_311G2dp"] - sp_r["total_energy_6_311G2dp"]) * hartree_to_kcal
                gold_val = gold_act.get(mol_name, {}).get(cation, {}).get(gold_key)
                if gold_val is None:
                    continue
                if abs(act - gold_val) <= tol:
                    n_pass += 1
    score = n_pass / n_total if n_total else 0.0
    return score


# === block: score_4 (check id='symmetries') ===
def score_4(artifact, step, ctx):
    expected = step["expected_symmetries"]
    n_pass = 0
    n_total = 0
    for mol_name in ["anthracene", "phenanthrene"]:
        for cation, sps in expected.get(mol_name, {}).items():
            art_sp_list = artifact.get(mol_name, {}).get(cation, {}).get("stationary_points", [])
            for label, sym in sps.items():
                n_total += 1
                sp = next((s for s in art_sp_list if s.get("label") == label), None)
                if sp and sp.get("symmetry", "").strip() == sym:
                    n_pass += 1
    score = n_pass / n_total if n_total else 0.0
    return score


_SCORERS = {
    'total_energies': score_0,
    'relative_energies': score_1,
    'binding_energies': score_2,
    'activation_energies': score_3,
    'symmetries': score_4,
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
