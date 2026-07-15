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


# === block: score_0 (check id='step_01_bulk_and_defect_formation') ===
def score_0(artifact, step, ctx):
    exp = step.get('expected', {})
    try:
        d = artifact
        sc = 0.0
        n = 0
        if 'bulk_lattice_constant_A' in d:
            if abs(d['bulk_lattice_constant_A'] - exp['bulk_lattice_constant_A']) <= exp.get('bulk_lattice_constant_A_tol', 0.02):
                sc += 1.0
            n += 1
        if 'bulk_band_gap_eV' in d:
            if abs(d['bulk_band_gap_eV'] - exp['bulk_band_gap_eV']) <= exp.get('bulk_band_gap_eV_tol', 0.1):
                sc += 1.0
            n += 1
        fe = d.get('defect_formation_energies', {})
        expected_fe = exp.get('defect_formation_energies', {})
        tol_fe = exp.get('formation_energy_tol', 0.2)
        for key in ['(CN)_Si_0', 'C_Si_0', '(NSi)_Si_0']:
            if key in fe:
                if abs(fe[key] - expected_fe.get(key, 0.0)) <= tol_fe:
                    sc += 1.0
                n += 1
        tl = d.get('charge_transition_levels', {})
        expected_tl = exp.get('charge_transition_level', {})
        tol_tl = exp.get('transition_level_tol', 0.15)
        for key in ['(CN)_Si_0_to_minus1']:
            if key in tl:
                if abs(tl[key] - expected_tl.get(key, 0.0)) <= tol_tl:
                    sc += 1.0
                n += 1
        if n == 0:
            return 0.0
        return sc / n
    except Exception:
        return 0.0


# === block: score_1 (check id='step_02_main_results') ===
def score_1(artifact, step, ctx):
    exp = step.get('expected', {})
    try:
        d = artifact
        sc = 0.0
        n = 0
        # 1. recompute decomposition energy from step_01
        import os, json
        st1_path = os.path.join('/app/outputs', 'step_01_bulk_and_defect_formation.json')
        if os.path.exists(st1_path):
            with open(st1_path) as f:
                st1 = json.load(f)
            fe = st1.get('defect_formation_energies', {})
            if all(k in fe for k in ['(CN)_Si_0', 'C_Si_0', '(NSi)_Si_0']):
                recomputed_de = fe['C_Si_0'] + fe['(NSi)_Si_0'] - fe['(CN)_Si_0']
                target_de = exp['decomposition_energy_eV']
                tol_de = exp.get('decomposition_energy_tol', 0.1)
                if abs(recomputed_de - target_de) <= tol_de:
                    sc += 1.0
                n += 1
        # 2. migration barrier
        if 'migration_barrier_eV' in d:
            if abs(d['migration_barrier_eV'] - exp['migration_barrier_eV']) <= exp.get('migration_barrier_tol', 0.1):
                sc += 1.0
            n += 1
        # 3. Debye-Waller factor
        if 'dW_factor_percent' in d:
            if abs(d['dW_factor_percent'] - exp['dW_factor_percent']) <= exp.get('dW_factor_tol', 1.0):
                sc += 1.0
            n += 1
        # 4. ZPL values
        zpl = d.get('zpl_values_meV', {})
        expected_zpl = exp.get('zpl_values_meV', {})
        tol_zpl = exp.get('zpl_tol', 20.0)
        for key in ['supercell_216', 'supercell_512', 'supercell_1000']:
            if key in zpl:
                if abs(zpl[key] - expected_zpl.get(key, 0.0)) <= tol_zpl:
                    sc += 1.0
                n += 1
        # 5. extrapolated ZPL
        if 'extrapolated_zpl_meV' in d:
            if abs(d['extrapolated_zpl_meV'] - exp['extrapolated_zpl_meV']) <= exp.get('extrapolated_zpl_tol', 20.0):
                sc += 1.0
            n += 1
        # 6. radiative lifetime
        if 'radiative_lifetime_us' in d:
            if abs(d['radiative_lifetime_us'] - exp['radiative_lifetime_us']) <= exp.get('radiative_lifetime_tol', 0.5):
                sc += 1.0
            n += 1
        if n == 0:
            return 0.0
        return sc / n
    except Exception:
        return 0.0


_SCORERS = {
    'step_01_bulk_and_defect_formation': score_0,
    'step_02_main_results': score_1,
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
