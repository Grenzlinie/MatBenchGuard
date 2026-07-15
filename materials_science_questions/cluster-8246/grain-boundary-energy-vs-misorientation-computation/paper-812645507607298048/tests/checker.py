import os
import json
import csv

# === author imports / helpers ===
import math


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
    gold = spec.get("gold_tables", {})

    def make_lookup(rows, energy_col):
        lookup = {}
        for r in rows:
            key = (r["GB_type"], float(r["distance_from_GB_plane"]))
            lookup[key] = float(r[energy_col])
        return lookup

    return {
        "vb_lookup": make_lookup(gold.get("vacancy_binding_energies", []), "vacancy_binding_energy"),
        "li_lookup": make_lookup(gold.get("li_segregation_energies", []), "li_segregation_energy")
    }


# === block: score_0 (check id='vacancy_binding') ===
def score_0(artifact, step, ctx):
    lookup = ctx["vb_lookup"]
    expected = 15
    matched = 0
    abs_errors = []
    sign_ok = 0
    for row in artifact:
        gb = row.get("GB_type", "")
        dist = float(row.get("distance_from_GB_plane", -1))
        energy = float(row.get("vacancy_binding_energy", 0.0))
        key = (gb, dist)
        if key not in lookup:
            continue
        ref = lookup[key]
        err = abs(energy - ref)
        if dist <= 4.0:
            tol = 0.04
        else:
            tol = 0.08
        site_score = max(0.0, 1.0 - err / tol) if tol > 0 else 0.0
        abs_errors.append(site_score)
        # sign check: zero threshold 0.002 for ref, 0.005 for agent
        if abs(ref) <= 0.002:
            if abs(energy) <= 0.005:
                sign_ok += 1
        elif ref < 0:
            if energy < -0.005:
                sign_ok += 1
        else:
            if energy > 0.005:
                sign_ok += 1
        matched += 1

    if matched == 0:
        return 0.0
    mean_err_score = sum(abs_errors) / matched if matched > 0 else 0.0
    sign_score = sign_ok / matched if matched > 0 else 0.0
    step_score = 0.7 * mean_err_score + 0.3 * sign_score
    coverage = min(1.0, matched / expected)
    return step_score * coverage


# === block: score_1 (check id='li_segregation') ===
def score_1(artifact, step, ctx):
    lookup = ctx["li_lookup"]
    expected = 15
    matched = 0
    abs_errors = []
    sign_ok = 0
    for row in artifact:
        gb = row.get("GB_type", "")
        dist = float(row.get("distance_from_GB_plane", -1))
        energy = float(row.get("li_segregation_energy", 0.0))
        key = (gb, dist)
        if key not in lookup:
            continue
        ref = lookup[key]
        err = abs(energy - ref)
        if dist <= 4.0:
            tol = 0.04
        else:
            tol = 0.08
        site_score = max(0.0, 1.0 - err / tol) if tol > 0 else 0.0
        abs_errors.append(site_score)
        if abs(ref) <= 0.002:
            if abs(energy) <= 0.005:
                sign_ok += 1
        elif ref < 0:
            if energy < -0.005:
                sign_ok += 1
        else:
            if energy > 0.005:
                sign_ok += 1
        matched += 1

    if matched == 0:
        return 0.0
    mean_err_score = sum(abs_errors) / matched if matched > 0 else 0.0
    sign_score = sign_ok / matched if matched > 0 else 0.0
    step_score = 0.7 * mean_err_score + 0.3 * sign_score
    coverage = min(1.0, matched / expected)
    return step_score * coverage


_SCORERS = {
    'vacancy_binding': score_0,
    'li_segregation': score_1,
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
