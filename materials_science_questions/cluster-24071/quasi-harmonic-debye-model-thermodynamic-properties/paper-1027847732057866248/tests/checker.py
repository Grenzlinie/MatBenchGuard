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


# === block: score_0 (check id='step04_elastic_postprocessing') ===
def score_0(artifact, step, ctx):
    import json, math
    ref = step.get('reference_values', {})
    tol_ec = step.get('tolerances', {}).get('elastic_constant', 0.05)
    tol_mod = step.get('tolerances', {}).get('moduli', 0.03)
    ec_fields = set(step.get('elastic_constant_fields', []))
    mod_fields = set(step.get('moduli_fields', []))
    phases = ['Pm-3m-Fe3Pt', 'I4/mmm-Fe3Pt', 'P4/mmm-FePt', 'Pm-3m-FePt3']
    total = 0
    passed = 0
    for phase in phases:
        if phase not in artifact: return 0.0
        d = artifact[phase]
        ref_phase = ref.get(phase)
        if not ref_phase:
            continue
        for key, gold in ref_phase.items():
            if key == 'born_stable':
                total += 1
                if isinstance(d.get(key), bool) and d.get(key) == bool(gold):
                    passed += 1
                continue
            val = d.get(key)
            if val is None or not isinstance(val, (int, float)):
                continue
            tol = tol_ec if key in ec_fields else tol_mod
            total += 1
            if abs(gold) < 1e-9:
                if abs(val) < 1e-9:
                    passed += 1
                continue
            if abs(val - gold) / abs(gold) <= tol:
                passed += 1
    score = passed / max(total, 1) if total > 0 else 0.0
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='step06_dynamical_stability_extraction') ===
def score_1(artifact, step, ctx):
    expect = step.get('stability_expectations', {})
    phases = ['Pm-3m-Fe3Pt', 'I4/mmm-Fe3Pt', 'P4/mmm-FePt', 'Pm-3m-FePt3']
    total = 0
    passed = 0
    for phase in phases:
        d = artifact.get(phase, {})
        exp = expect.get(phase)
        if not exp:
            continue
        freq = d.get('min_phonon_frequency_THz')
        if freq is None:
            continue
        total += 1
        threshold = exp.get('min_threshold', 0.0)
        if exp['stable']:
            if freq >= threshold and d.get('dynamically_stable', False):
                passed += 1
        else:
            if freq <= threshold and not d.get('dynamically_stable', True):
                passed += 1
    score = passed / max(total, 1) if total > 0 else 0.0
    return min(1.0, max(0.0, score))


# === block: score_2 (check id='step07_thermodynamic_computation') ===
def score_2(artifact, step, ctx):
    import math
    ref = step.get('reference_values', {})
    tols = step.get('tolerances', {})
    tol_T = tols.get('Debye_temperature_K', 15.0)
    tol_C = tols.get('heat_capacity_Cv_at_300K', 3.0)
    phases = ['Pm-3m-Fe3Pt', 'I4/mmm-Fe3Pt', 'P4/mmm-FePt', 'Pm-3m-FePt3']
    n = 2 * len([p for p in phases if p in ref])
    if n == 0: return 0.0
    score_sum = 0.0
    for phase in phases:
        d = artifact.get(phase, {})
        r = ref.get(phase)
        if not r: continue
        val_T = d.get('Debye_temperature_K'); gold_T = r.get('Debye_temperature_K')
        if val_T is not None and gold_T is not None:
            err = abs(val_T - gold_T)
            if err <= tol_T:
                score_sum += 1.0
            else:
                score_sum += max(0.0, 1.0 - (err - tol_T) / (gold_T * 0.5))
        val_C = d.get('heat_capacity_Cv_at_300K'); gold_C = r.get('heat_capacity_Cv_at_300K')
        if val_C is not None and gold_C is not None:
            err = abs(val_C - gold_C)
            if err <= tol_C:
                score_sum += 1.0
            else:
                score_sum += max(0.0, 1.0 - (err - tol_C) / (gold_C * 0.5))
    return min(1.0, max(0.0, score_sum / n))


_SCORERS = {
    'step04_elastic_postprocessing': score_0,
    'step06_dynamical_stability_extraction': score_1,
    'step07_thermodynamic_computation': score_2,
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
