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


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    compounds_config = step.get('config', {}).get('compounds', {})
    if not compounds_config:
        return 0.0
    # relaxed tolerance for cross-code comparison (Quantum ESPRESSO vs. VASP)
    default_tol = 0.3  # eV
    default_total_max = -100.0    # eV; any plausible total energy must be below this
    default_ref_max = -500.0     # eV; total minus formation must be well below zero
    passed = 0
    for name, cfg in compounds_config.items():
        if name not in artifact:
            continue
        entry = artifact[name]
        if not isinstance(entry, dict):
            continue
        formation = entry.get('formation_energy_eV_per_fu')
        total = entry.get('total_energy_computed')
        if formation is None or total is None:
            continue
        try:
            formation = float(formation)
            total = float(total)
        except (TypeError, ValueError):
            continue
        target = cfg.get('target_formation_energy')
        if target is None:
            continue
        tol = cfg.get('tolerance_abs', default_tol)
        total_max = cfg.get('total_energy_max', default_total_max)
        ref_max = cfg.get('reference_energy_max', default_ref_max)
        # 1) formation energy within tolerance of paper target
        if abs(formation - target) > tol:
            continue
        # 2) total energy must be plausible (large negative, not zero/unset)
        if total > total_max:
            continue
        # 3) reference sum (binary+He/Xe energies) must also be plausible
        ref = total - formation
        if ref > ref_max:
            continue
        passed += 1
    return passed / len(compounds_config) if compounds_config else 0.0


# === block: score_1 (check id='phonon_stability') ===
def score_1(artifact, step, ctx):
    threshold = step.get('config', {}).get('threshold_frequency_cm-1', -5.0)
    compounds = step.get('config', {}).get('compounds', [])
    if not compounds:
        return 0.0
    passed = 0
    for name in compounds:
        if name not in artifact:
            continue
        entry = artifact[name]
        if not isinstance(entry, dict):
            continue
        stable = entry.get('dynamically_stable')
        freq = entry.get('minimum_frequency_cm-1')
        if stable is None or freq is None:
            continue
        try:
            freq = float(freq)
        except (TypeError, ValueError):
            continue
        if stable == True and freq > threshold:
            passed += 1
    return passed / len(compounds) if compounds else 0.0


_SCORERS = {
    'formation_energies': score_0,
    'phonon_stability': score_1,
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
