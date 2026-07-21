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


# === block: score_0 (check id='random_critical_strain_scored') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get('gold', {})
        tolerance = step.get('tolerance', 0.1)
        data = {}
        for row in artifact:
            try:
                cov = float(row.get('coverage', None))
            except:
                continue
            row_dict = {}
            for config in ['sl_armchair','sl_zigzag','dl_armchair','dl_zigzag']:
                try:
                    row_dict[config] = float(row.get(config, None))
                except:
                    row_dict[config] = None
            data[cov] = row_dict
        total_pts = 0
        within_tol = 0
        for config, points in gold.items():
            for cov_str, exp_val in points.items():
                cov = float(cov_str)
                if cov not in data:
                    continue
                actual = data[cov].get(config)
                if actual is None:
                    continue
                total_pts += 1
                denom = max(abs(exp_val), 1e-12)
                if abs(actual - exp_val) / denom <= tolerance:
                    within_tol += 1
        acc_score = (within_tol / total_pts) if total_pts > 0 else 0.0
        mono_ok = True
        for config in ['sl_armchair','sl_zigzag','dl_armchair','dl_zigzag']:
            sorted_covs = sorted([c for c in data if data[c].get(config) is not None])
            if len(sorted_covs) < 2:
                continue
            vals = [data[c][config] for c in sorted_covs]
            for i in range(len(vals)-1):
                if vals[i+1] > vals[i] + 1e-6:
                    mono_ok = False
                    break
            if not mono_ok:
                break
        mono_score = 1.0 if mono_ok else 0.0
        return acc_score * 0.9 + mono_score * 0.1


# === block: score_1 (check id='patterned_properties_scored') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_list = step.get('gold', [])
        tolerance = step.get('tolerance', 0.1)
        gold = {item['configuration']: item for item in gold_list}
        total_props = 0
        within_tol = 0
        for row in artifact:
            config = row.get('configuration', '').strip()
            try:
                cs = float(row.get('critical_strain', None))
                us = float(row.get('ultimate_strength', None))
            except:
                continue
            exp = gold.get(config)
            if not exp:
                continue
            for prop_name, actual in [('critical_strain', cs), ('ultimate_strength', us)]:
                exp_val = exp[prop_name]
                total_props += 1
                denom = max(abs(exp_val), 1e-12)
                if abs(actual - exp_val) / denom <= tolerance:
                    within_tol += 1
        return (within_tol / total_props) if total_props > 0 else 0.0


_SCORERS = {
    'random_critical_strain_scored': score_0,
    'patterned_properties_scored': score_1,
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
