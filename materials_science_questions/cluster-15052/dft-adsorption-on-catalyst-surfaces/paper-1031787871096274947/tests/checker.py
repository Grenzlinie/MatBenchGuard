import os
import json
import csv

# === author imports / helpers ===
import json


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


# === block: score_0 (check id='ch4_barriers_check') ===
def score_0(artifact, step, ctx):
        tolerance = step['tolerance']
        gold = step['gold']
        # Find barrier values for ordering
        pd_ceo2_val = None
        pd_ic_val = None
        for e in artifact:
            if e.get('system') == 'Pd-CeO2' and e.get('step') == 'CH4_activation':
                pd_ceo2_val = e.get('activation_energy_eV')
            elif e.get('system') == 'Pd-iC-CeO2' and e.get('step') == 'CH4_activation':
                pd_ic_val = e.get('activation_energy_eV')
        order_ok = False
        if isinstance(pd_ceo2_val, (int, float)) and isinstance(pd_ic_val, (int, float)):
            if step.get('expected_ordering') == 'Pd-iC-CeO2 > Pd-CeO2':
                order_ok = pd_ic_val > pd_ceo2_val
        # Count barrier matches
        n_correct = 0
        for g in gold:
            for e in artifact:
                if e.get('system') == g['system'] and e.get('step') == g['step']:
                    if abs(e.get('activation_energy_eV', float('nan')) - g['activation_energy_eV']) <= tolerance:
                        n_correct += 1
                    break
        barrier_score = n_correct / len(gold) if gold else 0.0
        return 0.5 * barrier_score + 0.5 * (1.0 if order_ok else 0.0)


# === block: score_1 (check id='er_barriers_check') ===
def score_1(artifact, step, ctx):
        tolerance = step['tolerance']
        gold = step['gold']
        # Count correct barriers
        n_gold = len(gold)
        correct_barrier = 0
        for g in gold:
            for e in artifact:
                if e.get('system') == g['system'] and e.get('step') == g['step']:
                    if abs(e.get('activation_energy_eV', float('nan')) - g['activation_energy_eV']) <= tolerance:
                        correct_barrier += 1
                    break
        barrier_score = correct_barrier / n_gold if n_gold else 0.0
        # Check orderings
        orderings = step.get('orderings', {})
        n_orders = len(orderings)
        order_ok_count = 0
        for step_name, rel in orderings.items():
            val_ceo2 = None
            val_ic = None
            for e in artifact:
                if e.get('system') == 'Pd-CeO2' and e.get('step') == step_name:
                    val_ceo2 = e.get('activation_energy_eV')
                elif e.get('system') == 'Pd-iC-CeO2' and e.get('step') == step_name:
                    val_ic = e.get('activation_energy_eV')
            if isinstance(val_ceo2, (int, float)) and isinstance(val_ic, (int, float)):
                if rel == 'Pd-CeO2 > Pd-iC-CeO2' and val_ceo2 > val_ic:
                    order_ok_count += 1
                elif rel == 'Pd-iC-CeO2 > Pd-CeO2' and val_ic > val_ceo2:
                    order_ok_count += 1
        order_score = order_ok_count / n_orders if n_orders else 0.0
        return 0.5 * barrier_score + 0.5 * order_score


_SCORERS = {
    'ch4_barriers_check': score_0,
    'er_barriers_check': score_1,
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
