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
    return {}


# === block: score_0 (check id='step_03_bond_orders') ===
def score_0(artifact, step, ctx):
    rows = artifact
    epsilon = step.get('config', {}).get('delta_noise_epsilon', 0.001)
    cn_max = step.get('config', {}).get('cn_max_abs_delta', 0.005)

    bond_data = {}
    for r in rows:
        p = float(r['pressure_GPa'])
        bond = r['bond_label'].strip()
        if p in (0.0, 0.5, 1.0):
            if bond not in bond_data:
                bond_data[bond] = {}
            bond_data[bond][round(p, 2)] = float(r['effective_bond_order'])

    def bond_type(bond_label):
        parts = bond_label.split('-')
        if len(parts) != 2:
            return None
        elems = []
        for part in parts:
            e = ''.join(c for c in part if c.isalpha())
            elems.append(e)
        elems = sorted(elems)
        return '-'.join(elems)

    type_changes = {}
    for bond, vals in bond_data.items():
        if round(0.0,2) not in vals or round(1.0,2) not in vals:
            continue
        delta = vals[round(1.0,2)] - vals[round(0.0,2)]
        bt = bond_type(bond)
        if bt:
            if bt not in type_changes:
                type_changes[bt] = []
            type_changes[bt].append((bond, delta))

    correct_types = 0
    total_types = 4
    expected = {
        'C-H': 'decrease',
        'N-O': 'decrease',
        'N-N': 'increase',
        'C-N': 'constant'
    }
    for bt, expected_trend in expected.items():
        if bt not in type_changes:
            continue
        deltas = [d for _, d in type_changes[bt]]
        if expected_trend == 'decrease':
            if all(d < -epsilon for d in deltas):
                correct_types += 1
        elif expected_trend == 'increase':
            if all(d > epsilon for d in deltas):
                correct_types += 1
        elif expected_trend == 'constant':
            if all(abs(d) <= cn_max for d in deltas):
                correct_types += 1

    score = correct_types / total_types
    return score


# === block: score_1 (check id='step_04_phonon') ===
def score_1(artifact, step, ctx):
    rows = artifact  # list of dicts: pressure_GPa, mode_index, frequency_cm1
    epsilon = step.get('config', {}).get('freq_noise_epsilon', 0.01)
    min_modes = step.get('config', {}).get('min_modes', 500)

    # Group by mode_index
    modes = {}
    for r in rows:
        idx = int(r['mode_index'])
        p = round(float(r['pressure_GPa']), 2)
        if p in (0.0, 0.5, 1.0):
            if idx not in modes:
                modes[idx] = {}
            modes[idx][p] = float(r['frequency_cm1'])

    # Check minimum mode count at 0 and 1.0 GPa
    mode0 = [idx for idx, vals in modes.items() if round(0.0,2) in vals]
    mode1 = [idx for idx, vals in modes.items() if round(1.0,2) in vals]
    if len(mode0) < min_modes or len(mode1) < min_modes:
        return 0.0

    blue_count = 0
    total = len(mode0)
    for idx in mode0:
        if idx in modes and round(0.0,2) in modes[idx] and round(1.0,2) in modes[idx]:
            f0 = modes[idx][round(0.0,2)]
            f1 = modes[idx][round(1.0,2)]
            if f1 - f0 > epsilon:
                blue_count += 1

    if total == 0:
        return 0.0
    return blue_count / total


_SCORERS = {
    'step_03_bond_orders': score_0,
    'step_04_phonon': score_1,
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
