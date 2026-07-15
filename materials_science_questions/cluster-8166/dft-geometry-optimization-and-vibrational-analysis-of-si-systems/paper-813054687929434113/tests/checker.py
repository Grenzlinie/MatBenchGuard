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


# === block: score_0 (check id='check_energies') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    cols = set(artifact[0].keys()) if artifact else set()
    if 'configuration' not in cols or 'relative_energy_eV' not in cols:
        return 0.0
    # extract energies
    energies = {}
    for row in artifact:
        conf = str(row.get('configuration', '')).strip()
        try:
            val = float(row.get('relative_energy_eV', 0))
        except (ValueError, TypeError):
            return 0.0
        energies[conf] = val
    def get_e(conf):
        return energies.get(conf)
    # load gold
    params = step.get('params', {})
    gold_energies = params.get('gold_energies', {})
    gold_ins = params.get('gold_insertion_barrier', 0.69)
    gold_ht = params.get('gold_htransfer_barrier', 0.37)
    energy_tol = params.get('energy_tol', 0.1)
    barrier_tol = params.get('barrier_tol', 0.2)
    # energy sub-scores (5 configs)
    energy_configs = ['A', 'B', 'C', 'D', 'E']
    energy_scores = []
    for c in energy_configs:
        v = get_e(c)
        if v is None:
            energy_scores.append(0.0)
            continue
        target = gold_energies.get(c, 0)
        diff = abs(v - target)
        energy_scores.append(1.0 if diff <= energy_tol else 0.0)
    energy_score = sum(energy_scores) / len(energy_scores) if energy_scores else 0.0
    # barrier sub-scores
    ins_e = get_e('A')
    ins_score = 0.0
    if ins_e is not None:
        if abs(ins_e - gold_ins) <= barrier_tol:
            ins_score = 1.0
    # H-transfer = E(D) - E(C)
    e_d = get_e('D')
    e_c = get_e('C')
    ht_score = 0.0
    if e_d is not None and e_c is not None:
        ht = e_d - e_c
        if abs(ht - gold_ht) <= barrier_tol:
            ht_score = 1.0
    barrier_score = (ins_score + ht_score) / 2.0
    # ordering sub-scores: A > 0, 0 > B, B > D, D > E, E > C
    a = get_e('A')
    b = get_e('B')
    d = get_e('D')
    e_val = get_e('E')
    c_val = get_e('C')
    order_checks = []
    if a is not None and b is not None:
        order_checks.append(1.0 if a > 0 and b < 0 else 0.0)
    else:
        order_checks.append(0.0)
    if b is not None and d is not None:
        order_checks.append(1.0 if b > d else 0.0)
    else:
        order_checks.append(0.0)
    if d is not None and e_val is not None:
        order_checks.append(1.0 if d > e_val else 0.0)
    else:
        order_checks.append(0.0)
    if e_val is not None and c_val is not None:
        order_checks.append(1.0 if e_val > c_val else 0.0)
    else:
        order_checks.append(0.0)
    if a is not None and d is not None and e_val is not None and c_val is not None:
        order_checks.append(1.0 if (a > 0 and b is not None and d is not None and e_val is not None and c_val is not None and b > d and d > e_val and e_val > c_val) else 0.0)
    else:
        order_checks.append(0.0)
    order_score = sum(order_checks) / len(order_checks) if order_checks else 0.0
    # final weighted
    final = energy_score * 0.4 + barrier_score * 0.3 + order_score * 0.3
    return min(max(final, 0.0), 1.0)


_SCORERS = {
    'check_energies': score_0,
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
