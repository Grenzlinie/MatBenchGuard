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
    import json

    def prepare(outputs_dir, spec):
        energetics_step = next((s for s in spec['steps'] if s['id'] == 'step_01_energetics'), None)
        dos_step = next((s for s in spec['steps'] if s['id'] == 'step_02_dos'), None)
        return {
            'energetics_gold': energetics_step.get('gold', {}) if energetics_step else {},
            'energetics_tolerance': energetics_step.get('tolerance_kJmol', 2.0) if energetics_step else 2.0,
            'dos_step': dos_step
        }


# === block: score_0 (check id='step_01_energetics') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['energetics_gold']
        tol = ctx['energetics_tolerance']
        total = 0
        matches = 0
        for surf_name, surf_species in gold.items():
            if surf_name not in artifact:
                continue
            for species_name, species_fields in surf_species.items():
                if species_name not in artifact[surf_name]:
                    continue
                for field_name, gold_val in species_fields.items():
                    total += 1
                    agent_val = artifact[surf_name][species_name].get(field_name, None)
                    if gold_val is None:
                        if agent_val is None or agent_val is None:
                            matches += 1
                    elif agent_val is not None and isinstance(agent_val, (int, float)):
                        if abs(agent_val - gold_val) <= tol:
                            matches += 1
        if total == 0:
            return 0.0
        return round(matches / total, 5)


# === block: score_1 (check id='step_02_dos') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        dos_step = ctx['dos_step']
        peak_energy = dos_step['peak_energy_eV']
        window = dos_step['peak_window_eV']
        threshold_factor = dos_step['peak_detect_threshold_factor']
        expected_peak = dos_step['expected_peak_configs']
        expected_no_peak = dos_step['expected_no_peak_configs']
        config_data = {}
        for row in artifact:
            cfg = row.get('Configuration')
            if cfg not in config_data:
                config_data[cfg] = {'energy': [], 'dos': []}
            try:
                e = float(row['Energy_eV'])
                d = float(row['DOS_arb_units'])
            except:
                continue
            config_data[cfg]['energy'].append(e)
            config_data[cfg]['dos'].append(d)
        def has_peak(cfg):
            if cfg not in config_data:
                return False
            energies = config_data[cfg]['energy']
            dos_vals = config_data[cfg]['dos']
            peak_vals = [d for e,d in zip(energies, dos_vals) if peak_energy - window <= e <= peak_energy + window]
            far_vals = [d for e,d in zip(energies, dos_vals) if e >= 5.0 and e <= 10.0]
            if not peak_vals or not far_vals:
                return False
            avg_peak = sum(peak_vals)/len(peak_vals)
            avg_far = sum(far_vals)/len(far_vals)
            return (avg_peak > threshold_factor * avg_far)
        correct = 0
        total = 0
        for cfg in expected_peak:
            total += 1
            if has_peak(cfg):
                correct += 1
        for cfg in expected_no_peak:
            total += 1
            if not has_peak(cfg):
                correct += 1
        if total == 0:
            return 0.0
        return round(correct / total, 5)


_SCORERS = {
    'step_01_energetics': score_0,
    'step_02_dos': score_1,
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
