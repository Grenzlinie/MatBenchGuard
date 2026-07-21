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


# === block: score_0 (check id='fig1_maxima') ===
def score_0(artifact, step, ctx):
    # Compare agent submissions for fig1_maxima.json
    # artifact should be a list of dicts with keys: kappa_tilde, M, omega, omega_m
    if not isinstance(artifact, list):
        return 0.0
    gold_list = step.get('gold_data', [])
    tol = step.get('tolerances', {})
    if not gold_list:
        return 0.0
    # build lookup by kappa_tilde
    agent_map = {}
    for entry in artifact:
        k = entry.get('kappa_tilde')
        if k is not None:
            agent_map[k] = entry
    # compare each gold entry
    total = len(gold_list)
    matched = 0
    for gold in gold_list:
        key = gold['kappa_tilde']
        agent_entry = agent_map.get(key)
        if agent_entry is None:
            continue
        ok_M = abs(agent_entry.get('M', -999) - gold['M']) <= tol.get('M', 0.01)
        ok_omega = abs(agent_entry.get('omega', -999) - gold['omega']) <= tol.get('omega', 0.01)
        ok_omega_m = abs(agent_entry.get('omega_m', -999) - gold['omega_m']) <= tol.get('omega_m', 0.01)
        if ok_M and ok_omega and ok_omega_m:
            matched += 1
    return matched / total if total > 0 else 0.0


# === block: score_1 (check id='triple_points') ===
def score_1(artifact, step, ctx):
    # Compare agent submissions for triple_points.json
    # artifact should be a list of dicts with keys: omega, triple_omega_m, transition_order_I_to_ordered, transition_order_FMN_AFMN
    if not isinstance(artifact, list):
        return 0.0
    gold_list = step.get('gold_data', [])
    tol = step.get('tolerances', {})
    string_exact = step.get('string_fields_exact', [])
    if not gold_list:
        return 0.0
    # build lookup by omega (allow small tolerance for matching key)
    agent_map = {}
    for entry in artifact:
        o = entry.get('omega')
        if o is None:
            continue
        # find matching omega (exact should be 0.0, 0.4, 1.2, but use tolerance to be safe)
        key = None
        for g in gold_list:
            if abs(o - g['omega']) <= 1e-6:
                key = g['omega']
                break
        if key is not None:
            agent_map[key] = entry
    total = len(gold_list)
    matched = 0
    for gold in gold_list:
        key = gold['omega']
        agent_entry = agent_map.get(key)
        if agent_entry is None:
            continue
        # triple_omega_m tolerance
        ok_wm = abs(agent_entry.get('triple_omega_m', -999) - gold['triple_omega_m']) <= tol.get('triple_omega_m', 0.001)
        # string fields exact match
        ok_strs = True
        for field in string_exact:
            if agent_entry.get(field) != gold.get(field):
                ok_strs = False
                break
        if ok_wm and ok_strs:
            matched += 1
    return matched / total if total > 0 else 0.0


_SCORERS = {
    'fig1_maxima': score_0,
    'triple_points': score_1,
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
