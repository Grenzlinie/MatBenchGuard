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
    return {}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    if isinstance(artifact, dict) and "densities" in artifact and isinstance(artifact["densities"], list) and len(artifact["densities"]) == 3:
        return 1.0
    return 0.0


# === block: score_1 (check id='internal_consistency') ===
def score_1(artifact, step, ctx):
    densities = artifact.get("densities", [])
    if len(densities) != 3:
        return 0.0
    tol = float(step.get("tolerance", 1e-3))
    ok = 0
    for d in densities:
        fracs = d.get("layer_fractions", [])
        if len(fracs) != 60:
            return 0.0
        z = list(range(1, 61))
        avg = sum(z[i] * fracs[i] for i in range(60))
        var = sum((z[i] - avg) ** 2 * fracs[i] for i in range(60))
        sigma = math.sqrt(var)
        rep_avg = d.get("average_z")
        rep_sig = d.get("sigma")
        if rep_avg is None or rep_sig is None:
            return 0.0
        if abs(avg - rep_avg) <= tol and abs(sigma - rep_sig) <= tol:
            ok += 1
    return ok / 3.0


# === block: score_2 (check id='trends') ===
def score_2(artifact, step, ctx):
    densities = artifact.get("densities", [])
    if len(densities) != 3:
        return 0.0
    cond = [
        densities[0]["average_z"] > float(step["low_avg_min"]),
        densities[0]["sigma"] > float(step["low_sigma_min"]),
        densities[1]["average_z"] < float(step["mid_avg_max"]),
        densities[1]["sigma"] < float(step["mid_sigma_max"]),
        densities[2]["average_z"] < float(step["high_avg_max"]),
        densities[2]["sigma"] < float(step["high_sigma_max"]),
        densities[2]["layer_fractions"][0] > float(step["high_frac0_min"]),
    ]
    satisfied = sum(1 for c in cond if c)
    return satisfied / len(cond)


# === block: score_3 (check id='band_energy_ordering') ===
def score_3(artifact, step, ctx):
    densities = artifact.get("densities", [])
    if len(densities) != 3:
        return 0.0
    ok = 0
    for d in densities:
        bands = d.get("band_energies", [])
        if len(bands) != 6:
            return 0.0
        if all(e > 0.0 for e in bands) and all(bands[i] < bands[i+1] for i in range(len(bands)-1)):
            ok += 1
    return ok / 3.0


# === block: score_4 (check id='fraction_sum') ===
def score_4(artifact, step, ctx):
    densities = artifact.get("densities", [])
    if len(densities) != 3:
        return 0.0
    ok = 0
    for d in densities:
        fracs = d.get("layer_fractions", [])
        if len(fracs) != 60:
            return 0.0
        s = sum(fracs)
        if 0.99 <= s <= 1.01:
            ok += 1
    return ok / 3.0


_SCORERS = {
    'shape_check': score_0,
    'internal_consistency': score_1,
    'trends': score_2,
    'band_energy_ordering': score_3,
    'fraction_sum': score_4,
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
