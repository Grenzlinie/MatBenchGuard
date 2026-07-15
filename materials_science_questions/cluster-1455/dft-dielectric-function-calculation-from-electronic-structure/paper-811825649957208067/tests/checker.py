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
    step = spec['steps'][0]
    gold = step['gold']
    tolerances = step['tolerances']
    return {'gold': gold, 'tolerances': tolerances}


# === block: score_0 (check id='results_json') ===
def score_0(artifact, step, ctx):
    import os

    artifact_path = '/app/outputs/results.json'
    if not os.path.exists(artifact_path):
        return 0.0

    try:
        with open(artifact_path) as f:
            data = json.load(f)
    except Exception:
        return 0.0

    gold = ctx['gold']
    tolerances = ctx['tolerances']

    compounds_list = data.get('compounds', [])
    if not isinstance(compounds_list, list) or not compounds_list:
        return 0.0

    by_name = {}
    for comp in compounds_list:
        if not isinstance(comp, dict):
            continue
        name = comp.get('compound_name')
        if name:
            by_name[name] = comp

    all_keys = ['optimized_a', 'optimized_c', 'optimized_volume',
                'band_gap_calculated', 'scissor_shift', 'band_gap_corrected',
                'refractive_index_n0', 'sellmeyer_A', 'sellmeyer_B',
                'sellmeyer_C_nm', 'sellmeyer_D']

    lattice_keys = {'optimized_a', 'optimized_c', 'optimized_volume'}
    bandgap_keys = {'band_gap_calculated', 'scissor_shift', 'band_gap_corrected'}
    refractive_key = 'refractive_index_n0'
    sellmeier_keys = {'sellmeyer_A', 'sellmeyer_B', 'sellmeyer_C_nm', 'sellmeyer_D'}

    tol_lattice_rel = tolerances.get('lattice_relative', 0.02)
    tol_bandgap_abs = tolerances.get('band_gap_absolute', 0.1)
    tol_refractive_abs = tolerances.get('refractive_absolute', 0.05)
    tol_sellmeier_rel = tolerances.get('sellmeyer_relative', 0.10)

    compound_scores = []
    weights_per_compound = len(all_keys)

    for name, gold_vals in gold.items():
        comp = by_name.get(name)
        if comp is None:
            compound_scores.append(0.0)
            continue
        field_scores = []
        for key in all_keys:
            val = comp.get(key)
            gold_val = gold_vals.get(key)
            if val is None or gold_val is None:
                field_scores.append(0)
                continue
            try:
                val = float(val)
                gold_val = float(gold_val)
            except (TypeError, ValueError):
                field_scores.append(0)
                continue
        
            if key in lattice_keys:
                if gold_val == 0:
                    ok = abs(val - gold_val) < 1e-12
                else:
                    ok = abs(val - gold_val) / abs(gold_val) <= tol_lattice_rel
            elif key in bandgap_keys:
                ok = abs(val - gold_val) <= tol_bandgap_abs
            elif key == refractive_key:
                ok = abs(val - gold_val) <= tol_refractive_abs
            elif key in sellmeier_keys:
                if gold_val == 0:
                    ok = abs(val - gold_val) < 1e-12
                else:
                    ok = abs(val - gold_val) / abs(gold_val) <= tol_sellmeier_rel
            else:
                ok = False
            field_scores.append(1.0 if ok else 0.0)
    
        compound_scores.append(sum(field_scores) / len(field_scores))

    if not compound_scores:
        return 0.0

    return sum(compound_scores) / len(compound_scores)


_SCORERS = {
    'results_json': score_0,
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
