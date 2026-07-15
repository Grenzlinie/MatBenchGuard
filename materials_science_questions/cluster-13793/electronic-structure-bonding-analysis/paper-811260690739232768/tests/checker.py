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


# === block: score_0 (check id='intercalation_pref') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    signs = step.get('sign_checks', {})
    if not all(k in data for k in ('Li','Na','Mg')):
        return 0.0
    for metal, cond in signs.items():
        val = data[metal]
        if cond == 'gt_0' and not (val > 0):
            return 0.0
        if cond == 'lt_0' and not (val < 0):
            return 0.0
    return 1.0


# === block: score_1 (check id='diffusion_barriers') ===
def score_1(artifact, step, ctx):
    rows = load_artifact(step.get('output_file'))
    if not isinstance(rows, list) or not rows:
        return 0.0
    metal_path_map = {}
    for r in rows:
        metal = r.get('metal','').strip()
        path = r.get('path','').strip()
        try:
            barrier = float(r.get('barrier_eV'))
        except (ValueError, TypeError):
            return 0.0
        metal_path_map[(metal, path)] = barrier

    required = [('Li','zigzag'),('Li','armchair'),('Na','zigzag'),('Na','armchair'),('Mg','zigzag'),('Mg','armchair')]
    if not all(k in metal_path_map for k in required):
        return 0.0

    gold = step.get('gold', {})
    tol = step.get('tolerances', {})
    abs_tol = tol.get('absolute', {}) if isinstance(tol, dict) else {}
    zigzag_tol = abs_tol.get('zigzag', 0.1)
    armchair_tol_map = abs_tol.get('armchair', {})
    if not isinstance(armchair_tol_map, dict):
        armchair_tol_map = {m: armchair_tol_map for m in ('Li','Na','Mg')}

    def get_tol(metal, path):
        if path == 'zigzag':
            return zigzag_tol
        return armchair_tol_map.get(metal, 0.2)

    within_tol = 0
    for metal, path in required:
        expected = gold.get(metal, {}).get(path, None)
        if expected is None:
            return 0.0
        diff = abs(metal_path_map[(metal, path)] - expected)
        if diff <= get_tol(metal, path):
            within_tol += 1

    # ordering checks
    order_ok = True
    for metal in ('Li','Na','Mg'):
        if metal_path_map[(metal, 'zigzag')] >= metal_path_map[(metal, 'armchair')]:
            order_ok = False
            break
    if order_ok:
        zigzag_vals = [metal_path_map[(m, 'zigzag')] for m in ('Li','Na','Mg')]
        armchair_vals = [metal_path_map[(m, 'armchair')] for m in ('Li','Na','Mg')]
        if zigzag_vals != sorted(zigzag_vals) or armchair_vals != sorted(armchair_vals):
            order_ok = False

    score_tol = min(within_tol / len(required), 1.0)
    score_order = 1.0 if order_ok else 0.0
    return 0.4 * score_order + 0.6 * score_tol


# === block: score_2 (check id='bulk_moduli') ===
def score_2(artifact, step, ctx):
    rows = load_artifact(step.get('output_file'))
    if not isinstance(rows, list):
        return 0.0
    if not rows:
        return 0.0
    try:
        vals = {r['composition'].strip(): float(r['bulk_modulus_GPa']) for r in rows}
    except (KeyError, ValueError, TypeError):
        return 0.0

    needed = ['pristine', 'Li2P', 'Na2P', 'Mg2P']
    if not all(k in vals for k in needed):
        return 0.0

    ranges = step.get('tolerance_ranges', {})
    if not ranges:
        return 0.0

    passed = 0
    for comp in needed:
        val = vals[comp]
        lo, hi = ranges.get(comp, [None, None])
        if lo is not None and hi is not None and lo <= val <= hi:
            passed += 1
    return passed / len(needed)


_SCORERS = {
    'intercalation_pref': score_0,
    'diffusion_barriers': score_1,
    'bulk_moduli': score_2,
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
