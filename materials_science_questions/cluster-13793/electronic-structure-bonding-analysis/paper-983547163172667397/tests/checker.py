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


# === block: score_0 (check id='step_results') ===
def score_0(artifact, step, ctx):
    systems = artifact.get('systems', [])
    if not systems:
        return 0.0
    lookup = {s['name']: s for s in systems if 'name' in s}
    required = ['Cu3P', 'CuPIn', 'CuPSi', 'CuPSc', 'CuPTa']
    missing = [n for n in required if n not in lookup]
    presence_score = 1.0 if not missing else max(0.0, 1.0 - len(missing)*0.3)

    sanity_ok = 0
    sanity_total = 0
    for sys in lookup.values():
        b = sys.get('bulk_modulus_GPa')
        sh = sys.get('shear_modulus_GPa')
        y = sys.get('youngs_modulus_GPa')
        nu = sys.get('poisson_ratio')
        for val in [b, sh, y]:
            sanity_total += 1
            if val is not None and val > 0:
                sanity_ok += 1
        sanity_total += 1
        if nu is not None and 0.0 <= nu <= 0.5:
            sanity_ok += 1
    sanity_score = sanity_ok / sanity_total if sanity_total > 0 else 0.0

    poisson_trend_ok = 0
    poisson_trend_total = 4
    pristine_nu = lookup['Cu3P'].get('poisson_ratio')
    if pristine_nu is not None:
        for dop in ['CuPIn', 'CuPSi']:
            nu_dop = lookup[dop].get('poisson_ratio')
            if nu_dop is not None and nu_dop < pristine_nu:
                poisson_trend_ok += 1
        for dop in ['CuPSc', 'CuPTa']:
            nu_dop = lookup[dop].get('poisson_ratio')
            if nu_dop is not None and nu_dop > pristine_nu:
                poisson_trend_ok += 1
    poisson_score = poisson_trend_ok / poisson_trend_total

    hard_trend_ok = 0
    hard_trend_total = 4
    pristine_h = lookup['Cu3P'].get('hardness_GPa')
    if pristine_h is not None:
        for dop in ['CuPIn', 'CuPSi']:
            h_dop = lookup[dop].get('hardness_GPa')
            if h_dop is not None and h_dop > pristine_h:
                hard_trend_ok += 1
        for dop in ['CuPSc', 'CuPTa']:
            h_dop = lookup[dop].get('hardness_GPa')
            if h_dop is not None and h_dop < pristine_h:
                hard_trend_ok += 1
    hard_score = hard_trend_ok / hard_trend_total

    total = 0.05 * presence_score + 0.1 * sanity_score + 0.2 * poisson_score + 0.65 * hard_score
    return min(total, 1.0)


_SCORERS = {
    'step_results': score_0,
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
