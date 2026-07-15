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
    import json, os
    compiled_path = os.path.join(outputs_dir, 'compiled_energies.json')
    derived_path = os.path.join(outputs_dir, 'derived_barriers.json')
    ctx = {}
    try:
        with open(compiled_path) as f:
            ctx['compiled'] = json.load(f)
    except Exception:
        ctx['compiled'] = None
    try:
        with open(derived_path) as f:
            ctx['derived'] = json.load(f)
    except Exception:
        ctx['derived'] = None
    return ctx


# === block: score_0 (check id='compiled_models_present') ===
def score_0(artifact, step, ctx):
    import json
    compiled = ctx.get('compiled')
    if compiled is None:
        return 0.0
    required_models = {'Ni@SV', 'Ni-N@SV', 'Co@SV', 'Co-N@SV'}
    req_keys = {'E_bare', 'E_COOH', 'E_CO', 'E_H'}
    models_found = set()
    for entry in compiled:
        if isinstance(entry, dict) and 'model' in entry:
            if entry['model'] in required_models and all(k in entry for k in req_keys):
                models_found.add(entry['model'])
    score = len(models_found) / len(required_models) if required_models else 0.0
    return score


# === block: score_1 (check id='derived_models_present') ===
def score_1(artifact, step, ctx):
    derived = ctx.get('derived')
    if derived is None:
        return 0.0
    required_models = {'Ni@SV', 'Ni-N@SV', 'Co@SV', 'Co-N@SV'}
    req_keys = {'CO_desorption_barrier', 'HER_limiting_potential'}
    found = set()
    for entry in derived:
        if isinstance(entry, dict) and 'model' in entry:
            if entry['model'] in required_models and all(k in entry for k in req_keys):
                found.add(entry['model'])
    return len(found) / len(required_models)


# === block: score_2 (check id='derived_consistency') ===
def score_2(artifact, step, ctx):
    compiled = ctx.get('compiled')
    derived = ctx.get('derived')
    if compiled is None or derived is None:
        return 0.0
    # Build dicts keyed by model
    energies = {e['model']: e for e in compiled if 'model' in e}
    barriers = {d['model']: d for d in derived if 'model' in d}
    shift_co = []
    shift_her = []
    for model in ['Ni@SV', 'Ni-N@SV', 'Co@SV', 'Co-N@SV']:
        e = energies.get(model)
        d = barriers.get(model)
        if e and d and all(k in e for k in ['E_CO', 'E_bare', 'E_H']) and all(k in d for k in ['CO_desorption_barrier', 'HER_limiting_potential']):
            # CO shift: CO_desorption_barrier should equal (E_CO - E_bare) + constant
            shift_co.append(d['CO_desorption_barrier'] - (e['E_CO'] - e['E_bare']))
            # HER shift: HER_limiting_potential + (E_H - E_bare) should be constant
            shift_her.append(d['HER_limiting_potential'] + (e['E_H'] - e['E_bare']))
    if len(shift_co) < 2:
        return 0.0
    # Check that shift is constant across models (tolerance 0.1 eV)
    co_const = max(shift_co) - min(shift_co) < 0.1
    her_const = max(shift_her) - min(shift_her) < 0.1
    return 1.0 if (co_const and her_const) else 0.0


# === block: score_3 (check id='trend_co_barrier') ===
def score_3(artifact, step, ctx):
    derived = ctx.get('derived')
    if derived is None:
        return 0.0
    barriers = {d['model']: d.get('CO_desorption_barrier') for d in derived if 'model' in d and 'CO_desorption_barrier' in d}
    pairs = [('Ni@SV', 'Co@SV'), ('Ni-N@SV', 'Co-N@SV')]
    correct = 0
    for ni_mod, co_mod in pairs:
        ni_val = barriers.get(ni_mod)
        co_val = barriers.get(co_mod)
        if ni_val is not None and co_val is not None and ni_val < co_val:
            correct += 1
    return correct / len(pairs)


# === block: score_4 (check id='trend_her_potential') ===
def score_4(artifact, step, ctx):
    derived = ctx.get('derived')
    if derived is None:
        return 0.0
    pots = {d['model']: d.get('HER_limiting_potential') for d in derived if 'model' in d and 'HER_limiting_potential' in d}
    pairs = [('Ni@SV', 'Co@SV'), ('Ni-N@SV', 'Co-N@SV')]
    correct = 0
    for ni_mod, co_mod in pairs:
        ni_val = pots.get(ni_mod)
        co_val = pots.get(co_mod)
        if ni_val is not None and co_val is not None and ni_val < co_val:
            correct += 1
    return correct / len(pairs)


_SCORERS = {
    'compiled_models_present': score_0,
    'derived_models_present': score_1,
    'derived_consistency': score_2,
    'trend_co_barrier': score_3,
    'trend_her_potential': score_4,
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
