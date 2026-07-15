import os
import json
import csv

# === author imports / helpers ===
import csv
import os


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
    spec = {"outputs_dir": os.path.join("/app/outputs")}
    gold_noise = {}
    # Safely extract gold_noise from the noise_match step params if available
    steps = spec.get("steps", [])
    if not steps:
        # fallback: try checking for 'checks' key if 'steps' missing (older spec)
        steps = spec.get("checks", [])
    for step in (steps or []):
        if step.get("id") == "noise_match":
            for k, v in step.get("params", {}).get("gold_noise", {}).items():
                gold_noise[k] = v
            break
    ctx = {"gold_noise": gold_noise}
    return ctx


# === block: score_0 (check id='noise_match') ===
def score_0(artifact, step, ctx):
    import csv
    import os

    rows = list(csv.DictReader(open(os.path.join("/app/outputs", "simulation_results.csv"), newline="")))
    total = len(rows)
    if total != 8:
        return 0.0

    # Embedded gold noise values from the paper's Table III (calculated intensities).
    # This eliminates dependency on prepare's ctx or step['params'].
    gold_noise = {
        "A,W": 106.1,
        "A,Ti": 10.9,
        "B,W": 16.5,
        "B,Ti": 1.8,
        "C,W": 31.9,
        "C,Ti": 3.4,
        "U,W": 0.8,
        "U,Ti": 0.3,
    }

    passed = 0
    for row in rows:
        key = f"{row['specimen']},{row['region']}"
        if key not in gold_noise:
            continue
        gold = gold_noise[key]
        try:
            val = float(row["noise_Si_cps"])
        except (ValueError, KeyError):
            continue
        if gold == 0:
            if abs(val) < 1e-6:
                passed += 1
            continue
        rel_err = abs(val - gold) / abs(gold)
        if rel_err <= 0.25:
            passed += 1
    return passed / total


# === block: score_1 (check id='structural_checks') ===
def score_1(artifact, step, ctx):
    import csv
    rows = list(csv.DictReader(open(os.path.join("/app/outputs", "simulation_results.csv"), newline="")))
    data = {}
    for r in rows:
        data[(r["specimen"], r["region"])] = float(r["noise_Si_cps"])

    checks = 0
    passed = 0

    # (1) For each specimen, noise_W > noise_Ti
    for s in ["A", "B", "C", "U"]:
        w = data.get((s, "W"))
        ti = data.get((s, "Ti"))
        if w is not None and ti is not None:
            checks += 1
            if w > ti:
                passed += 1

    # (2) U noise <= 5 for both W and Ti
    for r in ["W", "Ti"]:
        val = data.get(("U", r))
        if val is not None:
            checks += 1
            if val <= 5:
                passed += 1

    # (3) noise_A / noise_U >= 5 for both W and Ti
    for r in ["W", "Ti"]:
        a_val = data.get(("A", r))
        u_val = data.get(("U", r))
        if a_val is not None and u_val is not None and u_val > 1e-12:
            checks += 1
            if a_val / u_val >= 5:
                passed += 1

    if checks == 0:
        return 0.0
    return passed / checks


_SCORERS = {
    'noise_match': score_0,
    'structural_checks': score_1,
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
