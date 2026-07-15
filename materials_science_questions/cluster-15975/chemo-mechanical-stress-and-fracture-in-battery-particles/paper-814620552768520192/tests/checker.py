import os
import json
import csv

# === author imports / helpers ===
import collections, math


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
    capacity_gold = {
        (1, 2): 2.60, (2, 2): 2.55, (3, 2): 2.50, (4, 2): 2.47, (5, 2): 2.44,
        (1, 4): 2.10, (2, 4): 2.05, (3, 4): 2.00, (4, 4): 1.97, (5, 4): 1.95
    }
    return {"capacity_gold": capacity_gold, "max_gradient_allowed": 100000.0}


# === block: score_0 (check id='conc_gradients') ===
def score_0(artifact, step, ctx):
    # Hidden reference gradients (paper's 2D benchmark, Figure 5)
    gold_gradients = {
        (2.5, 1): 200, (2.5, 2): 400, (2.5, 3): 600, (2.5, 4): 800,
        (2.5, 5): 1000, (2.5, 6): 1200, (2.5, 8): 1400, (2.5, 10): 1600,
        (5.0, 1): 400, (5.0, 2): 800, (5.0, 3): 1200, (5.0, 4): 1600,
        (5.0, 5): 2000, (5.0, 6): 2400, (5.0, 8): 3000, (5.0, 10): 3500,
        (7.5, 1): 600, (7.5, 2): 1200, (7.5, 3): 1800, (7.5, 4): 2400,
        (7.5, 5): 3000, (7.5, 6): 3600, (7.5, 8): 4500, (7.5, 10): 5500,
        (10.0, 1): 800, (10.0, 2): 1600, (10.0, 3): 2400, (10.0, 4): 3200,
        (10.0, 5): 4000, (10.0, 6): 4800, (10.0, 8): 6000, (10.0, 10): 7500,
        (12.5, 1): 1000, (12.5, 2): 2000, (12.5, 3): 3000, (12.5, 4): 4000,
        (12.5, 5): 5000, (12.5, 6): 6000, (12.5, 8): 7500, (12.5, 10): 9500,
        (15.0, 1): 1200, (15.0, 2): 2400, (15.0, 3): 3600, (15.0, 4): 4800,
        (15.0, 5): 6000, (15.0, 6): 7200, (15.0, 8): 9000, (15.0, 10): 11500
    }

    data = {}
    for row in artifact:
        r = float(row["particle_radius_um"])
        c = float(row["C_rate"])
        g = float(row["surface_concentration_gradient_mol_m3"])
        if g <= 0:
            return 0.0
        data[(r, c)] = g

    if len(data) < 48:
        return 0.0

    errors = []
    for key, target in gold_gradients.items():
        actual = data.get(key)
        if actual is None:
            errors.append(1.0)
        else:
            rel_err = abs(actual - target) / (abs(target) + 1e-9)
            errors.append(rel_err)

    avg_rel_err = sum(errors) / len(errors)
    return max(0.0, 1.0 - avg_rel_err / 0.10)


# === block: score_1 (check id='cap_fade') ===
def score_1(artifact, step, ctx):
    gold = ctx["capacity_gold"]
    errors = []
    for row in artifact:
        cyc = int(row["cycle_number"])
        cr = float(row["C_rate"])
        key = (cyc, cr)
        if key in gold:
            target = gold[key]
            actual = float(row["discharge_capacity_Ah"])
            rel_err = abs(actual - target) / (abs(target) + 1e-9)
            errors.append(rel_err)
    if not errors:
        return 0.0
    avg_rel_err = sum(errors) / len(errors)
    return max(0.0, 1.0 - avg_rel_err / 0.20)


_SCORERS = {
    'conc_gradients': score_0,
    'cap_fade': score_1,
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
