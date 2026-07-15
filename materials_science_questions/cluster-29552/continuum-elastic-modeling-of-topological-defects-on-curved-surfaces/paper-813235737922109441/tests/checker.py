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
    import csv

    def parse_csv(path):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def runner(outputs_dir, spec):
        ctx = {}
        step = spec['steps'][0]
        ctx['required_chi'] = step.get('required_chi_Wall', [])
        tols = step.get('tolerances', {})
        ctx['high_minus_low_target'] = tols.get('high_minus_low_target_kT', 12.2)
        ctx['high_minus_low_tol'] = tols.get('high_minus_low_abs_tol_kT', 2.0)
        ctx['max_minus_high_target'] = tols.get('max_minus_high_target_kT', 3.5)
        ctx['max_minus_high_tol'] = tols.get('max_minus_high_abs_tol_kT', 1.0)
        return ctx


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
        rows = artifact
        required_chi = ctx['required_chi']
        if not isinstance(rows, list) or not rows:
            return 0.0
        # validate columns
        if 'chi_Wall' not in rows[0] or 'defect_free_energy_kT' not in rows[0]:
            return 0.0
        # map chi to value
        chi_vals = {}
        try:
            for r in rows:
                chi_str = r.get('chi_Wall')
                val_str = r.get('defect_free_energy_kT')
                if chi_str is None or val_str is None:
                    return 0.0
                chi = int(float(chi_str))
                val = float(val_str)
                chi_vals[chi] = val
        except (ValueError, TypeError):
            return 0.0
        # require exactly the specified list
        if set(chi_vals.keys()) != set(required_chi):
            return 0.0
        # Compute plateau average (chi >= 44)
        plateau_vals = [chi_vals[c] for c in required_chi if c >= 44]
        if not plateau_vals:
            return 0.0
        plateau_mean = sum(plateau_vals) / len(plateau_vals)
        low_val = chi_vals[0]
        max_val = chi_vals[42]  # paper states max at 42
        # Check that 42 is the global max
        global_max = max(chi_vals.values())
        if chi_vals[42] < global_max - 1e-6:
            max_penalty = 0.2
        else:
            max_penalty = 0.0
        # amplitude differences
        high_minus_low = plateau_mean - low_val
        max_minus_high = max_val - plateau_mean
        tol_hl = ctx['high_minus_low_tol']
        target_hl = ctx['high_minus_low_target']
        tol_mh = ctx['max_minus_high_tol']
        target_mh = ctx['max_minus_high_target']
        score_hl = 1.0 if abs(high_minus_low - target_hl) <= tol_hl else 0.0
        score_mh = 1.0 if abs(max_minus_high - target_mh) <= tol_mh else 0.0
        base_score = 0.5 * score_hl + 0.5 * score_mh
        # subtract max_penalty if max not at 42
        base_score -= max_penalty
        return max(0.0, base_score)


_SCORERS = {
    'step1': score_0,
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
