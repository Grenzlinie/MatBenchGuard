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


# === block: score_0 (check id='barrier_he') ===
def score_0(artifact, step, ctx):
    val = artifact.get("energy_barriers", {}).get("He")
    if val is None or not isinstance(val, (int, float)):
        return 0.0
    target = step.get("target", 0.11)
    tol = step.get("tolerance_abs", 0.05)
    diff = abs(val - target)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    return 0.0


# === block: score_1 (check id='barrier_ne') ===
def score_1(artifact, step, ctx):
    val = artifact.get("energy_barriers", {}).get("Ne")
    if val is None or not isinstance(val, (int, float)):
        return 0.0
    target = step.get("target", 0.51)
    tol = step.get("tolerance_abs", 0.05)
    diff = abs(val - target)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    return 0.0


# === block: score_2 (check id='barrier_ar') ===
def score_2(artifact, step, ctx):
    val = artifact.get("energy_barriers", {}).get("Ar")
    if val is None or not isinstance(val, (int, float)):
        return 0.0
    target = step.get("target", 2.45)
    tol = step.get("tolerance_abs", 0.05)
    diff = abs(val - target)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    return 0.0


# === block: score_3 (check id='selectivity_hene') ===
def score_3(artifact, step, ctx):
    val = artifact.get("selectivities", {}).get("He_Ne")
    if val is None or not isinstance(val, (int, float)) or val <= 0:
        return 0.0
    target_log10 = step.get("target_log10", 6.7135)
    tol_log10 = step.get("tolerance_log10", 0.5)
    diff = abs(math.log10(val) - target_log10)
    if diff < tol_log10:
        return 1.0
    elif diff < 2 * tol_log10:
        return 0.5
    return 0.0


# === block: score_4 (check id='selectivity_hear') ===
def score_4(artifact, step, ctx):
    val = artifact.get("selectivities", {}).get("He_Ar")
    if val is None or not isinstance(val, (int, float)) or val <= 0:
        return 0.0
    target_log10 = step.get("target_log10", 39.2765)
    tol_log10 = step.get("tolerance_log10", 0.5)
    diff = abs(math.log10(val) - target_log10)
    if diff < tol_log10:
        return 1.0
    elif diff < 2 * tol_log10:
        return 0.5
    return 0.0


# === block: score_5 (check id='consistency') ===
def score_5(artifact, step, ctx):
    k_B = 8.617333262145e-5
    T = 300.0
    barriers = artifact.get("energy_barriers", {})
    selectivities = artifact.get("selectivities", {})
    E_He = barriers.get("He")
    E_Ne = barriers.get("Ne")
    E_Ar = barriers.get("Ar")
    S_He_Ne = selectivities.get("He_Ne")
    S_He_Ar = selectivities.get("He_Ar")
    if any(v is None or not isinstance(v, (int, float)) for v in [E_He, E_Ne, E_Ar, S_He_Ne, S_He_Ar]):
        return 0.0
    if S_He_Ne <= 0 or S_He_Ar <= 0:
        return 0.0
    S_He_Ne_calc = math.exp(-(E_He - E_Ne) / (k_B * T))
    S_He_Ar_calc = math.exp(-(E_He - E_Ar) / (k_B * T))
    diff_hene = abs(math.log10(S_He_Ne) - math.log10(S_He_Ne_calc))
    diff_hear = abs(math.log10(S_He_Ar) - math.log10(S_He_Ar_calc))
    score_hene = 1.0 if diff_hene < 0.1 else (0.5 if diff_hene < 0.5 else 0.0)
    score_hear = 1.0 if diff_hear < 0.1 else (0.5 if diff_hear < 0.5 else 0.0)
    return (score_hene + score_hear) / 2.0


_SCORERS = {
    'barrier_he': score_0,
    'barrier_ne': score_1,
    'barrier_ar': score_2,
    'selectivity_hene': score_3,
    'selectivity_hear': score_4,
    'consistency': score_5,
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
