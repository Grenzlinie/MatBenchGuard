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


# === block: score_0 (check id='step_spin') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) != 6:
        return 0.0
    total_checks = 0
    passed = 0
    for i, entry in enumerate(data):
        n = i + 1
        if not isinstance(entry, dict):
            return 0.0
        # all_freq_positive
        if entry.get("all_freq_positive") is True:
            passed += 1
        total_checks += 1
        # delta_E_eV sign
        delta = entry.get("delta_E_eV")
        if delta is None:
            total_checks += 1
            continue
        if n == 1:
            if delta > 0:
                passed += 1
        else:
            if delta < 0:
                passed += 1
        total_checks += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='step_binding') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) != 6:
        return 0.0
    be = {}
    for entry in data:
        if not isinstance(entry, dict):
            return 0.0
        cluster = entry.get("cluster", "")
        if cluster.startswith("YSi"):
            try:
                n = int(cluster[3:])
            except:
                continue
            be[n] = entry.get("binding_energy_per_atom")
    # must have n=1..6
    if set(be.keys()) != set(range(1,7)):
        return 0.0
    total = 0
    passed = 0
    # peak at n=2
    if be.get(2, 0) > be.get(1, 0) and be.get(2, 0) > be.get(3, 0):
        passed += 1
    total += 1
    # peak at n=5
    if be.get(5, 0) > be.get(4, 0) and be.get(5, 0) > be.get(6, 0):
        passed += 1
    total += 1
    # additional: check general upward trend or at least binding energies are positive? Not required; we can add positivity check for robustness, but weight accounted by these. We'll add two more checks: positive binding energies for all? The paper expects positive. We'll check all be > 0 and add fraction passed. But the spec only asks peaks. We'll keep it simple: two peaks -> 2 conditions. So total=2. return passed/total.
    # Actually the plan says verify local maxima at n=2 and n=5, that's 4 inequalities. We'll score as 2 condition groups.
    return passed / total


# === block: score_2 (check id='step_fragmentation') ===
def score_2(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) != 6:
        return 0.0
    fe1 = {}
    fe2 = {}
    for entry in data:
        if not isinstance(entry, dict):
            return 0.0
        cluster = entry.get("cluster", "")
        if cluster.startswith("YSi"):
            try:
                n = int(cluster[3:])
            except:
                continue
            fe1[n] = entry.get("FE1_Y_Si_n")
            fe2[n] = entry.get("FE2_Si_YSi_{n-1}")
    if set(fe1.keys()) != set(range(1,7)) or set(fe2.keys()) != set(range(1,7)):
        return 0.0
    total = 0
    passed = 0
    # FE1 peaks at n=2 and n=5
    if fe1.get(2, 0) > fe1.get(1, 0) and fe1.get(2, 0) > fe1.get(3, 0):
        passed += 1
    total += 1
    if fe1.get(5, 0) > fe1.get(4, 0) and fe1.get(5, 0) > fe1.get(6, 0):
        passed += 1
    total += 1
    # FE2 peaks at n=2 and n=5
    if fe2.get(2, 0) > fe2.get(1, 0) and fe2.get(2, 0) > fe2.get(3, 0):
        passed += 1
    total += 1
    if fe2.get(5, 0) > fe2.get(4, 0) and fe2.get(5, 0) > fe2.get(6, 0):
        passed += 1
    total += 1
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'step_spin': score_0,
    'step_binding': score_1,
    'step_fragmentation': score_2,
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
