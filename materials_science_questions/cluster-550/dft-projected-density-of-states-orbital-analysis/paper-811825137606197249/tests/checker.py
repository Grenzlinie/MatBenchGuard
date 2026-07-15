import os
import json
import csv

# === author imports / helpers ===
import math
import statistics


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
    gold = spec.get('gold', {})
    return {
        'gold_forces': gold.get('forces', {}),
        'gold_bonds': gold.get('bonds', {}),
        'force_tolerance': gold.get('force_tolerance', 0.2)
    }


# === block: score_0 (check id='breaking_forces') ===
def score_0(artifact, step, ctx):
    gold_forces = ctx['gold_forces']
    gold_bonds = ctx['gold_bonds']
    tol = ctx['force_tolerance']
    expected = ['T1','T2','T3','T4','T5']
    force_correct = 0
    bond_correct = 0
    for j in expected:
        row = next((r for r in artifact if r.get('junction_type','').strip() == j), None)
        if row is None:
            continue
        try:
            force_val = float(row['breaking_force_nN'])
            if abs(force_val - gold_forces[j]) <= tol:
                force_correct += 1
        except (ValueError, KeyError):
            pass
        bond_val = (row.get('breaking_bond','') or '').strip()
        if bond_val == gold_bonds[j]:
            bond_correct += 1
    force_frac = force_correct / 5.0
    bond_frac = bond_correct / 5.0
    return 0.8 * force_frac + 0.2 * bond_frac


# === block: score_1 (check id='energy_curves') ===
def score_1(artifact, step, ctx):
    expected_keys = ['T1','T2','T3','T4','T5']
    if not all(k in artifact for k in expected_keys):
        return 0.0
    total_shape = 0
    total_mono = 0
    total_plateau = 0
    total_valid = 0
    count = 0
    for key in expected_keys:
        steps = artifact.get(key)
        if not isinstance(steps, list) or len(steps) == 0:
            continue
        count += 1
        lengths = []
        energies = []
        shape_ok = True
        for s in steps:
            if not isinstance(s, dict):
                shape_ok = False
                break
            try:
                l = float(s['length_angstrom'])
                e = float(s['total_energy_eV'])
            except (ValueError, KeyError):
                shape_ok = False
                break
            lengths.append(l)
            energies.append(e)
        if not shape_ok:
            continue
        total_shape += 1
        total_valid += 1
        # monotonic length increase (allow non‑decreasing with tiny epsilon)
        if all(lengths[i] <= lengths[i+1] + 1e-9 for i in range(len(lengths)-1)):
            total_mono += 1
        # energy plateau at end
        if len(energies) >= 3:
            n_last = max(3, int(0.2 * len(energies)))
            last_energies = energies[-n_last:]
            energy_range = max(energies) - min(energies) + 1e-12
            plateau_ratio = (max(last_energies) - min(last_energies)) / energy_range
            if plateau_ratio <= 0.1:
                total_plateau += 1
        else:
            total_plateau += 1
    if count == 0:
        return 0.0
    shape_score = total_shape / count
    mono_score = total_mono / count
    plateau_score = total_plateau / count
    valid_score = total_valid / count
    return 0.3 * shape_score + 0.3 * mono_score + 0.3 * plateau_score + 0.1 * valid_score


_SCORERS = {
    'breaking_forces': score_0,
    'energy_curves': score_1,
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
