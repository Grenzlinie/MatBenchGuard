import os
import json
import csv

# === author imports / helpers ===
import math


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
        step = None
        for s in spec.get('steps', spec.get('checks', [])):
            if s.get('id') == 'migration_barrier':
                step = s
                break
        if step is None:
            raise ValueError('Step "migration_barrier" not found')
        return {
            'target': step['target_barrier_eV'],
            'tolerance': step['tolerance_barrier_eV'],
            'max_dev': step.get('max_deviation_for_partial', 0.10),
            'ground_range': step['ground_state_energy_range'],
            'trans_range': step['transition_state_energy_range'],
            'rtol_kjmol': step.get('barrier_kJmol_consistency_rtol', 0.01),
            'rtol_eV': step.get('barrier_eV_consistency_rtol', 0.01),
        }


# === block: score_0 (check id='migration_barrier') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        try:
            ge = float(artifact['ground_state_energy'])
            te = float(artifact['transition_state_energy'])
            b_kj = float(artifact['barrier_kJmol'])
            b_ev = float(artifact['barrier_eV'])
        except (KeyError, TypeError, ValueError):
            return 0.0

        # partial credits
        shape_score = 0.1 if all(k in artifact for k in ('ground_state_energy', 'transition_state_energy', 'barrier_kJmol', 'barrier_eV')) else 0.0
        if shape_score == 0.0:
            return 0.0

        # recompute barrier from energies
        calc_kj = te - ge
        kj_conversion = 96.485  # kJ per eV
        calc_ev = calc_kj / kj_conversion

        # consistency
        kj_ok = abs(calc_kj - b_kj) <= ctx['rtol_kjmol'] * max(abs(calc_kj), 1.0)
        ev_ok = abs(b_ev - calc_ev) <= ctx['rtol_eV'] * max(abs(calc_ev), 1e-3)
        consistency_score = 0.1 if (kj_ok and ev_ok) else 0.0

        # energy range plausibility
        g_min, g_max = ctx['ground_range']
        t_min, t_max = ctx['trans_range']
        range_ok = (g_min <= ge <= g_max) and (t_min <= te <= t_max) and (b_kj > 0)
        range_score = 0.1 if range_ok else 0.0

        # barrier match score
        diff = abs(b_ev - ctx['target'])
        tol = ctx['tolerance']
        max_d = ctx['max_dev']
        if diff <= tol:
            barrier_score = 0.7
        elif diff <= max_d:
            barrier_score = 0.7 * (1.0 - (diff - tol) / (max_d - tol))
        else:
            barrier_score = 0.0

        total = shape_score + consistency_score + range_score + barrier_score
        # clamp
        return min(max(total, 0.0), 1.0)


_SCORERS = {
    'migration_barrier': score_0,
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
