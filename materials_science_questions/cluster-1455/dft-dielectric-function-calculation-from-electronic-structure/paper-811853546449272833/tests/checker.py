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
    ctx = {}


# === block: score_0 (check id='compile_results') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tols = gold.get('tolerances', {})
    sub_checks = gold.get('sub_checks', [])
    score = 0.0
    for ch in sub_checks:
        w = ch.get('weight', 0.0)
        name = ch.get('name', '')
        if 'ordering' in name:
            if 'beta_eps' in name:
                a = artifact.get('beta_Nb2O5', {}).get('epsilon_avg', -1)
                b = artifact.get('beta_Ta2O5', {}).get('epsilon_avg', -1)
                if a != -1 and b != -1 and a > b:
                    score += w
            elif 'deltaA_eps' in name:
                a = artifact.get('deltaA_Nb2O5', {}).get('epsilon_avg', -1)
                b = artifact.get('deltaA_Ta2O5', {}).get('epsilon_avg', -1)
                if a != -1 and b != -1 and a > b:
                    score += w
            continue
        phase = ch.get('phase')
        field = ch.get('field')
        if phase:
            val = artifact.get(phase, {}).get(field)
        else:
            val = artifact.get(field)
        if val is None:
            continue
        gold_val = ch.get('gold')
        if gold_val is None:
            continue
        tol = 0.0
        if 'epsilon' in field:
            rel = tols.get('epsilon_relative', 0.15)
            abst = tols.get('epsilon_absolute', 2.0)
            tol = max(abs(gold_val) * rel, abst)
        elif field == 'band_gap':
            tol = tols.get('band_gap_absolute', 0.3)
        elif 'Born' in field:
            if 'metal' in field:
                tol = tols.get('metal_born_abs', 0.5)
            else:
                tol = tols.get('oxygen_born_abs', 0.3)
        elif 'energy_diff' in field:
            tol = tols.get('energy_diff_abs', 0.1)
        satisfied = abs(val - gold_val) <= tol
        if field == 'epsilon_avg' and ch.get('check_self_consistency'):
            eps_xx = artifact.get(phase, {}).get('epsilon_xx')
            eps_yy = artifact.get(phase, {}).get('epsilon_yy')
            eps_zz = artifact.get(phase, {}).get('epsilon_zz')
            if eps_xx is not None and eps_yy is not None and eps_zz is not None:
                expected = (eps_xx + eps_yy + eps_zz) / 3.0
                satisfied = satisfied and abs(val - expected) <= 0.01
        if satisfied:
            score += w
    return score


_SCORERS = {
    'compile_results': score_0,
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
