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
    return spec['steps'][0]['gold']


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    try:
        import json, math
    except:
        pass

    artifact = artifact  # the loaded results.json dict
    ctx = ctx
    gold = ctx
    tol = gold['tolerances']
    score = 0.0

    # Part 1: Lattice optimizations (weight 0.6)
    opt_gold = gold['lattice_optimizations']
    compounds = ['Ti2FeAl', 'Ti2CoAl', 'Ti2NiAl']
    opt_list = artifact.get('lattice_optimizations', [])
    opt_map = {}
    for item in opt_list:
        opt_map[item.get('compound', '')] = item

    comp_scores = []
    for comp in compounds:
        g = opt_gold[comp]
        d = opt_map.get(comp)
        if not d:
            comp_scores.append(0.0)
            continue
        c_s = 0.0
        # total moment
        mom = d.get('total_moment_muB')
        if mom is not None and abs(mom - g['moment']) <= tol['moment_tol']:
            c_s += 0.5
        # minority gap
        gap = d.get('minority_gap_eV')
        if gap is not None and abs(gap - g['gap']) <= tol['gap_tol']:
            c_s += 0.4
        # lattice constant
        a = d.get('a_opt_angstrom')
        if a is not None and abs(a - g['a_opt']) <= tol['a_tol']:
            c_s += 0.1
        comp_scores.append(c_s)

    if comp_scores:
        score += (sum(comp_scores) / len(comp_scores)) * 0.6

    # Part 2: Z‑removal (weight 0.25)
    z = artifact.get('z_removal')
    if z:
        z_sc = 0.0
        # minority gap destroyed
        if z.get('minority_gap_eV', 1.0) <= gold['z_removal']['gap_max']:
            z_sc += 0.6
        # moment deviates from integer 2.0
        z_mom = z.get('total_moment_muB')
        if z_mom is not None and abs(z_mom - gold['z_removal']['integer_ref_moment']) > gold['z_removal']['moment_integer_tol']:
            z_sc += 0.4
        score += z_sc * 0.25

    # Part 3: Lattice parameter effect (weight 0.15)
    lp = artifact.get('lattice_parameter_effect')
    if lp:
        lp_gold = gold['lattice_parameter_effect']
        lp_scores = []
        for item in lp:
            a_val = item.get('a')
            gap_val = item.get('gap')
            key = str(a_val) if a_val is not None else None
            target = lp_gold.get(key, {}).get('gap') if key else None
            if target is not None and gap_val is not None and abs(gap_val - target) <= tol['gap_tol']:
                lp_scores.append(1.0)
            else:
                lp_scores.append(0.0)
        if lp_scores:
            score += (sum(lp_scores) / len(lp_scores)) * 0.15

    # Ensure 0–1
    return max(0.0, min(1.0, score))


_SCORERS = {
    'step_01': score_0,
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
