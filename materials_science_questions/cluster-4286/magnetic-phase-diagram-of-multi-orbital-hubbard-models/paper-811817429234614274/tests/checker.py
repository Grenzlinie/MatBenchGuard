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


# === block: score_0 (check id='k_rho_score') ===
def score_0(artifact, step, ctx):
    try:
        artifact_dict = {item['U_prime']: item for item in artifact}
    except Exception:
        return 0.0

    gold_k = step.get('gold_K_rho', {})
    gold_s = step.get('gold_spin', {})
    tol = step.get('tolerance', 0.2)
    points = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    passed = 0
    for u in points:
        entry = artifact_dict.get(u)
        if entry is None:
            continue
        gk = gold_k.get(str(u))
        gs = gold_s.get(str(u))
        if gk is None or gs is None:
            continue
        if abs(entry['K_rho'] - gk) <= tol and entry['ground_state_spin'] == gs:
            passed += 1
    return passed / len(points) if points else 0.0


# === block: score_1 (check id='pairing_score') ===
def score_1(artifact, step, ctx):
    sc_i = None
    sc_ii = None
    for ent in artifact:
        p = ent.get('parameters', {})
        if p.get('U') == 2.4 and p.get('U_prime') == 1.0:
            sc_i = ent
        elif p.get('U') == -0.4 and p.get('U_prime') == 1.0:
            sc_ii = ent

    if sc_i is None or sc_ii is None:
        return 0.0

    corr_i = sc_i.get('correlations', {})
    corr_ii = sc_ii.get('correlations', {})

    def safe_idx(arr, idx):
        if isinstance(arr, list) and len(arr) > idx:
            return arr[idx]
        return 0.0

    s_nn_l_i = safe_idx(corr_i.get('S_nn_l', []), 1)
    s_on_l_i = safe_idx(corr_i.get('S_on_l', []), 1)
    s_nn_lu_i = safe_idx(corr_i.get('S_nn_l-u', []), 1)

    cond1_i = abs(s_nn_l_i) > 2.0 * abs(s_on_l_i)
    cond2_i = s_nn_lu_i < 0

    singlet_keys = ['S_on_u', 'S_nn_u', 'S_on_l', 'S_nn_l']
    vals = []
    for k in singlet_keys:
        vals.append(abs(safe_idx(corr_ii.get(k, []), 1)))
    if not vals:
        return 0.0
    max_val = max(vals)
    cond_ii = abs(safe_idx(corr_ii.get('S_on_u', []), 1)) == max_val

    points = 0.0
    if cond1_i and cond2_i:
        points += 0.5
    elif cond1_i or cond2_i:
        points += 0.25
    if cond_ii:
        points += 0.5
    return points


_SCORERS = {
    'k_rho_score': score_0,
    'pairing_score': score_1,
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
