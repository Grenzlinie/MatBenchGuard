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


# === block: score_0 (check id='step_extract_mechanical') ===
def score_0(artifact, step, ctx):
    groups = {}
    for row in artifact:
        k3 = row.get("K3")
        if k3 is None:
            continue
        try:
            k3_val = float(k3)
        except:
            return 0.0
        strain_val = float(row["strain"])
        force_val = float(row["force_normalized"])
        ym_val = float(row["youngs_modulus_normalized"])
        if k3_val not in groups:
            groups[k3_val] = []
        groups[k3_val].append((strain_val, force_val, ym_val))

    expected_k3s = {0.1, 0.05, 0.01}
    if set(groups.keys()) != expected_k3s:
        return 0.0

    for k3 in groups:
        groups[k3].sort(key=lambda x: x[0])

    # sub-scores
    scores = {}

    # 1. file structure: each K3 group has at least 10 rows
    struct_ok = all(len(data) >= 10 for data in groups.values())
    scores["struct"] = 1.0 if struct_ok else 0.0

    # 2. force >= strain for all rows (coating contribution non-negative)
    force_cond = True
    for k3, data in groups.items():
        for s, f, _ in data:
            if f < s - 1e-9:
                force_cond = False
                break
        if not force_cond:
            break
    scores["force"] = 1.0 if force_cond else 0.0

    # 3. modulus monotonic non-increasing (allow tiny float errors)
    mono_ok = True
    for k3, data in groups.items():
        yms = [y for _, _, y in data]
        for i in range(len(yms)-1):
            if yms[i+1] - yms[i] > 1e-8:
                mono_ok = False
                break
        if not mono_ok:
            break
    scores["mono"] = 1.0 if mono_ok else 0.0

    # 4. ordering of initial modulus
    init_mod = {k3: data[0][2] for k3, data in groups.items()}
    ordering_ok = (init_mod.get(0.1, 0) > init_mod.get(0.05, 0) > init_mod.get(0.01, 0))
    scores["order"] = 1.0 if ordering_ok else 0.0

    # 5. convergence to 1
    final_mod = {k3: data[-1][2] for k3, data in groups.items()}
    converge_ok = all(final_mod.get(k3, 100) <= 1.05 for k3 in expected_k3s)
    scores["converge"] = 1.0 if converge_ok else 0.0

    weights = {"struct": 0.05, "force": 0.1, "mono": 0.35, "order": 0.25, "converge": 0.25}
    total = sum(scores[k] * weights[k] for k in scores)
    return total


_SCORERS = {
    'step_extract_mechanical': score_0,
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
