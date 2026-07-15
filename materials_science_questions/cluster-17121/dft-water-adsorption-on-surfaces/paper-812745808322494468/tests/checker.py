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
    ctx = {}
    for step in spec['steps']:
        if step['id'] == 'step_03_surface_energies':
            ctx['step_03_targets'] = step.get('targets', [])
        elif step['id'] == 'step_04_adsorption_energies':
            ctx['step_04_adsorption_targets'] = step.get('adsorption_targets', [])
            ctx['step_04_sub_weights'] = step.get('sub_weights', {'adsorption':0.5,'ordering':0.5})
    return ctx


# === block: score_0 (check id='step_03_surface_energies') ===
def score_0(artifact, step, ctx):
    targets = ctx.get('step_03_targets', [])
    if not targets:
        return 0.0
    correct = 0
    for t in targets:
        surf = t['surface']
        field = t['field']
        expected = t['expected']
        tol = t['tolerance']
        if surf in artifact and field in artifact[surf]:
            val = float(artifact[surf][field])
            if abs(val - expected) <= tol:
                correct += 1
    return correct / len(targets)


# === block: score_1 (check id='step_04_adsorption_energies') ===
def score_1(artifact, step, ctx):
    adsorption_targets = ctx.get('step_04_adsorption_targets', [])
    if not adsorption_targets:
        ads_score = 0.0
    else:
        correct = 0
        for t in adsorption_targets:
            surf = t['surface']
            ads = t['adsorbate']
            expected = t['expected']
            tol = t['tolerance']
            if surf in artifact and ads in artifact[surf]:
                val = float(artifact[surf][ads])
                if abs(val - expected) <= tol:
                    correct += 1
        ads_score = correct / len(adsorption_targets)
    ordering_score = 0.0
    try:
        a = artifact
        orders = []
        fluorite_surfs = ['fluorite_011','fluorite_111','fluorite_310']
        calcite_ma = a.get('calcite_104', {}).get('methanoic_acid', None)
        if calcite_ma is not None:
            orders.append(all(a[s]['methanoic_acid'] < calcite_ma for s in fluorite_surfs if s in a and 'methanoic_acid' in a[s]))
        else:
            orders.append(False)
        calcite_w = a.get('calcite_104', {}).get('water', None)
        if calcite_w is not None and calcite_ma is not None:
            orders.append(calcite_w < calcite_ma)
        else:
            orders.append(False)
        f011_w = a.get('fluorite_011',{}).get('water', None)
        f011_ma = a.get('fluorite_011',{}).get('methanoic_acid', None)
        if f011_w is not None and f011_ma is not None:
            orders.append(f011_ma < f011_w)
        else:
            orders.append(False)
        f111_w = a.get('fluorite_111',{}).get('water', None)
        f111_ma = a.get('fluorite_111',{}).get('methanoic_acid', None)
        if f111_w is not None and f111_ma is not None:
            orders.append(f111_ma < f111_w)
        else:
            orders.append(False)
        f310_w = a.get('fluorite_310',{}).get('water', None)
        f310_ma = a.get('fluorite_310',{}).get('methanoic_acid', None)
        if f310_w is not None and f310_ma is not None:
            orders.append(f310_w < f310_ma and (f310_ma - f310_w) > 100)
        else:
            orders.append(False)
        ordering_score = sum(orders) / 5.0
    except:
        ordering_score = 0.0
    sub = ctx.get('step_04_sub_weights', {'adsorption':0.5,'ordering':0.5})
    return sub['adsorption'] * ads_score + sub['ordering'] * ordering_score


_SCORERS = {
    'step_03_surface_energies': score_0,
    'step_04_adsorption_energies': score_1,
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
