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
    path = os.path.join(outputs_dir, 'step_01_structural_params.csv')
    rows = []
    if os.path.exists(path):
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
    by_key = {}
    for r in rows:
        key = f"{r['dopant']}_{r['configuration']}_{r['charge_state']}"
        by_key[key] = r
    return {'by_key': by_key, 'rows': rows}


# === block: score_0 (check id='buckling_angle') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tolerance = step['tolerance']
    ctx_rows = ctx['by_key']
    valid = 0
    for key, target in gold.items():
        row = ctx_rows.get(key)
        if row is None:
            continue
        try:
            val = float(row['buckling_angle_deg'])
            if abs(val - target) <= tolerance:
                valid += 1
        except (ValueError, KeyError):
            pass
    return valid / len(gold) if gold else 1.0


# === block: score_1 (check id='bond_length') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tolerance = step['tolerance']
    ctx_rows = ctx['by_key']
    valid = 0
    for key, target in gold.items():
        row = ctx_rows.get(key)
        if row is None:
            continue
        try:
            val = float(row['bond_length_angstrom'])
            if abs(val - target) <= tolerance:
                valid += 1
        except (ValueError, KeyError):
            pass
    return valid / len(gold) if gold else 1.0


# === block: score_2 (check id='magnetic_moment') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    ctx_rows = ctx['by_key']
    valid = 0
    for key, target in gold.items():
        row = ctx_rows.get(key)
        if row is None:
            continue
        try:
            val = float(row['magnetic_moment_muB'])
            if abs(val - target) < 1e-6:
                valid += 1
        except (ValueError, KeyError):
            pass
    return valid / len(gold) if gold else 1.0


# === block: score_3 (check id='energy_diff') ===
def score_3(artifact, step, ctx):
    config = step['recompute_config']
    tol = config['tolerance']
    target_diff = config['target_diff']
    rows = ctx['rows']
    # Only evaluate neutral charge state, because charged system energies are not reported.
    count = 0
    correct = 0
    # Collect HD1 and HD2 energies for neutral (Ne) per dopant
    energies = {}  # dopant -> {'HD1': val, 'HD2': val}
    for r in rows:
        if r['charge_state'] != 'Ne':
            continue
        d = r['dopant']
        cfg = r['configuration']
        try:
            energy = float(r['total_energy_eV'])
        except (ValueError, KeyError):
            continue
        if d not in energies:
            energies[d] = {}
        energies[d][cfg] = energy
    for d, vals in energies.items():
        if 'HD1' in vals and 'HD2' in vals:
            diff = vals['HD2'] - vals['HD1']
            target = target_diff.get(d)
            if target is None:
                continue
            count += 1
            if abs(diff - target) <= tol:
                correct += 1
    return correct / count if count else 0.0


# === block: score_4 (check id='hd1_trend') ===
def score_4(artifact, step, ctx):
    config = step['config']
    field = config['field']
    rows = ctx['rows']
    dopants = config['dopants']
    score = 0.0
    total = 0.0
    for d in dopants:
        vals = {}
        for r in rows:
            if r['dopant'] == d and r['configuration'] == 'HD1':
                cs = r['charge_state']
                try:
                    vals[cs] = float(r[field])
                except:
                    pass
        if 'Ne' in vals and 'Ne+1' in vals and 'Ne+2' in vals:
            total += 1.0
            if vals['Ne'] > vals['Ne+1'] > vals['Ne+2']:
                if config.get('sign_Ne+2_negative', False) and vals['Ne+2'] >= 0:
                    score += 0.5  # partial credit if order correct but sign not negative
                else:
                    score += 1.0
            elif vals['Ne'] > vals['Ne+2']:  # partial credit for overall decrease
                score += 0.3
    return score / total if total > 0 else 1.0


# === block: score_5 (check id='hd2_trend') ===
def score_5(artifact, step, ctx):
    config = step['config']
    field = config['field']
    rows = ctx['rows']
    dopants = config['dopants']
    max_dev = config.get('max_deviation', 2.0)
    score = 0.0
    total = 0.0
    for d in dopants:
        vals = []
        for r in rows:
            if r['dopant'] == d and r['configuration'] == 'HD2':
                try:
                    vals.append(float(r[field]))
                except:
                    pass
        if len(vals) >= 2:
            total += 1.0
            if max(vals) - min(vals) <= max_dev:
                score += 1.0
            else:
                # partial credit if deviation not huge
                if max(vals) - min(vals) <= 4.0:
                    score += 0.5
    return score / total if total > 0 else 1.0


_SCORERS = {
    'buckling_angle': score_0,
    'bond_length': score_1,
    'magnetic_moment': score_2,
    'energy_diff': score_3,
    'hd1_trend': score_4,
    'hd2_trend': score_5,
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
