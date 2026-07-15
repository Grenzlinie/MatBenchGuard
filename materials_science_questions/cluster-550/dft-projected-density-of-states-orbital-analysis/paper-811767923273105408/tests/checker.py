import os
import json
import csv

# === author imports / helpers ===
import json, math, os


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


# === block: score_0 (check id='scored_binding_energies') ===
def score_0(artifact, step, ctx):
    fields = step['parameters']['fields']
    score = 0.0
    for entry in fields:
        field = entry['field']
        sub_w = entry['sub_weight']
        if field == 'max_H2_released':
            value = artifact.get('max_H2_released')
            sub = 1.0 if value == entry['gold'] else 0.0
        else:
            value = artifact.get(field)
            if value is None:
                sub = 0.0
            else:
                diff = abs(value - entry['gold'])
                sub = 1.0 if diff <= entry['tolerance'] else 0.0
        score += sub * sub_w
    return score


# === block: score_1 (check id='scored_occupation_numbers') ===
def score_1(artifact, step, ctx):
    bind_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', 'outputs', 'binding_energies.json')
    if not os.path.exists(bind_path):
        return 0.0
    with open(bind_path) as f:
        binding = json.load(f)
    k = 8.617333262145e-5
    T1 = 298.0
    T2 = 195.0
    mu1 = -0.21
    mu2 = -0.10
    e1_raw = binding.get('released_1H2_binding_energy_eV')
    e2_raw = binding.get('released_2H2_binding_energy_per_H2_eV')
    if e1_raw is None or e2_raw is None:
        return 0.0
    e1 = e1_raw * 0.75
    e2 = e2_raw * 0.75
    def grand(mu, T, e1, e2):
        kT = k * T
        num = 1 * math.exp((mu + e1) / kT) + 2 * math.exp(2 * (mu + e2) / kT)
        den = 1 + math.exp((mu + e1) / kT) + math.exp(2 * (mu + e2) / kT)
        return num / den
    f1 = grand(mu1, T1, e1, e2)
    f2 = grand(mu2, T2, e1, e2)
    consistency = 0.0
    if all(k in artifact for k in ('occupation_25C_60atm','occupation_minus78C_60atm')):
        if abs(artifact['occupation_25C_60atm'] - f1) < 0.01 and abs(artifact['occupation_minus78C_60atm'] - f2) < 0.01:
            consistency = 1.0
    tol = step['parameters']['tolerance']
    gold1 = step['parameters']['occupation_25C_gold']
    gold2 = step['parameters']['occupation_minus78C_gold']
    gold = 1.0 if (abs(f1 - gold1) <= tol and abs(f2 - gold2) <= tol) else 0.0
    cw = step['parameters']['consistency_weight']
    gw = step['parameters']['gold_weight']
    return cw * consistency + gw * gold


_SCORERS = {
    'scored_binding_energies': score_0,
    'scored_occupation_numbers': score_1,
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
