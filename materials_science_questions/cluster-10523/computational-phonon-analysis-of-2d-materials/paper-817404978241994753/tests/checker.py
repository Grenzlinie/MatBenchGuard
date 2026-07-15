import os
import json
import csv

# === author imports / helpers ===
import statistics
from collections import defaultdict


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
    cfg = spec['steps'][0]['config']
    gold = {
        "zb": {50: -2.0e-6, 100: -1.0e-6, 200: 2.0e-6, 300: 4.0e-6, 400: 5.0e-6,
               500: 5.5e-6, 600: 6.0e-6, 700: 6.2e-6, 800: 6.4e-6, 900: 6.5e-6, 1000: 6.6e-6},
        "wurtzite_a": {50: -1.0e-6, 100: 1.0e-6, 200: 4.0e-6, 300: 6.0e-6, 400: 7.0e-6,
                       500: 7.5e-6, 600: 7.8e-6, 700: 8.0e-6, 800: 8.2e-6, 900: 8.3e-6, 1000: 8.4e-6},
        "wurtzite_c": {50: -5.0e-6, 100: -2.0e-6, 200: 1.0e-6, 300: 2.5e-6, 400: 3.5e-6,
                       500: 4.0e-6, 600: 4.5e-6, 700: 4.8e-6, 800: 5.0e-6, 900: 5.2e-6, 1000: 5.3e-6},
        "2ML": {50: -40e-6, 100: -30e-6, 200: -20e-6, 300: -15e-6, 400: -10e-6,
                500: -6e-6, 600: -3e-6, 700: 0.0, 800: 2e-6, 900: 4e-6, 1000: 5e-6},
        "3ML": {50: -25e-6, 100: -18e-6, 200: -10e-6, 300: -5e-6, 400: -1e-6,
                500: 2e-6, 600: 3.5e-6, 700: 5e-6, 800: 6e-6, 900: 6.8e-6, 1000: 7.5e-6},
        "4ML": {50: -15e-6, 100: -10e-6, 200: -3e-6, 300: 2e-6, 400: 4e-6,
                500: 5.5e-6, 600: 6.5e-6, 700: 7.2e-6, 800: 7.8e-6, 900: 8.2e-6, 1000: 8.5e-6},
        "5ML": {50: -8e-6, 100: -4e-6, 200: 1e-6, 300: 4e-6, 400: 5.5e-6,
                500: 6.5e-6, 600: 7.2e-6, 700: 7.8e-6, 800: 8.3e-6, 900: 8.7e-6, 1000: 9.0e-6}
    }
    return {
        'gold': gold,
        'structures': cfg['structures'],
        'temperatures': cfg['temperatures'],
        'rel_error_threshold': cfg['rel_error_threshold']
    }


# === block: score_0 (check id='cte_values_check') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    structures = ctx['structures']
    threshold = ctx['rel_error_threshold']
    comp = defaultdict(dict)
    for row in artifact:
        s = row.get('structure', '')
        try:
            t = int(float(row.get('temperature_K', 0)))
        except (ValueError, TypeError):
            continue
        try:
            c = float(row.get('cte_K_minus1', 0))
        except (ValueError, TypeError):
            continue
        comp[s][t] = c
    within = 0
    for s in structures:
        gold_vals = gold.get(s, {})
        if not gold_vals:
            continue
        rel_errors = []
        for temp in gold_vals:
            computed_val = comp.get(s, {}).get(temp, None)
            if computed_val is None:
                rel_errors.append(1e6)
            else:
                g = gold_vals[temp]
                rel = abs(computed_val - g) / max(abs(g), 1e-8)
                rel_errors.append(rel)
        if rel_errors:
            med = statistics.median(rel_errors)
            if med <= threshold:
                within += 1
    ordering_ok = False
    npl_keys = ['2ML', '3ML', '4ML', '5ML']
    if all(k in comp for k in npl_keys):
        try:
            vals = [comp[k].get(300, None) for k in npl_keys]
            if all(v is not None for v in vals):
                if vals[0] < vals[1] < vals[2] < vals[3]:
                    ordering_ok = True
        except Exception:
            pass
    total_structures = len(structures)
    fraction = within / total_structures if total_structures > 0 else 0.0
    if within == total_structures and ordering_ok:
        score = 1.0
    else:
        score = fraction
    return score


_SCORERS = {
    'cte_values_check': score_0,
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
