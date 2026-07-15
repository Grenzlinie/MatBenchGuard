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


# === block: score_0 (check id='optimized_structure') ===
def score_0(artifact, step, ctx):
    ref = step['reference']
    tol_a = step['tolerances']['a']
    tol_c = step['tolerances']['c']
    tol_u = step['tolerances']['u']
    passed = 0
    total = 0
    for key, tol in [('a', tol_a), ('c', tol_c), ('u', tol_u)]:
        if key in artifact:
            total += 1
            if abs(artifact[key] - ref[key]) <= tol:
                passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='results') ===
def score_1(artifact, step, ctx):
    ref = step['reference']
    tol_born = step['tolerances']['born_diagonal']
    tol_ph = step['tolerances']['phonon_frequency']
    tol_diel = step['tolerances']['dielectric']
    passed = 0
    total = 0

    # Born effective charges
    born_ref = ref['born_effective_charges']
    if 'born_effective_charges' in artifact:
        born_art = artifact['born_effective_charges']
        for atom, val in born_ref.items():
            if atom not in born_art:
                total += 3
                continue
            art_matrix = born_art[atom]
            diag = [art_matrix[0][0], art_matrix[1][1], art_matrix[2][2]]
            ref_diag = val['diagonal']
            for i in range(3):
                total += 1
                if abs(diag[i] - ref_diag[i]) <= tol_born:
                    passed += 1
    else:
        total += 12

    # Phonon frequencies — match by mode_label, then compare sorted lists per label.
    ph_ref = ref['phonon_frequencies']  # list of objects with mode_label, lo, to
    ph_art = artifact.get('phonon_frequencies', None)
    if isinstance(ph_art, list) and ph_art:
        # group by mode_label
        def group_by_label(modes):
            groups = {}
            for m in modes:
                lbl = m.get('mode_label')
                if lbl:
                    groups.setdefault(lbl, []).append(m)
            return groups
        art_groups = group_by_label(ph_art)
        ref_groups = group_by_label(ph_ref)
        for label in ref_groups:
            ref_modes = sorted(ref_groups[label], key=lambda m: m['to'])
            art_modes = sorted(art_groups.get(label, []), key=lambda m: m.get('frequencies', {}).get('to', 0))
            for rm, am in zip(ref_modes, art_modes):
                total += 2
                art_freq = am.get('frequencies', {})
                for fkey in ('lo', 'to'):
                    if fkey in art_freq:
                        if abs(art_freq[fkey] - rm[fkey]) <= tol_ph:
                            passed += 1
    else:
        total += len(ref['phonon_frequencies']) * 2

    # Dielectric tensors
    diel_ref = ref['dielectric_tensors']
    if 'dielectric_tensors' in artifact:
        diel_art = artifact['dielectric_tensors']
        for key in ['epsilon_inf_perp', 'epsilon_inf_par', 'epsilon0_perp', 'epsilon0_par']:
            total += 1
            if key in diel_art and abs(diel_art[key] - diel_ref[key]) <= tol_diel:
                passed += 1
    else:
        total += 4

    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'optimized_structure': score_0,
    'results': score_1,
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
