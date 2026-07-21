import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    np = None


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


# === block: score_0 (check id='check_ergo_L4') ===
def score_0(artifact, step, ctx):
    data = artifact.get("ergodicity_times", {})
    val = data.get("4", {}).get("mean", None)
    if not isinstance(val, (int, float)):
        return 0.0
    target = 35.3
    rel_tol = 0.2
    rel_dev = abs(val - target) / target
    if rel_dev <= rel_tol:
        return 1.0
    return max(0.0, 1.0 - (rel_dev - rel_tol) / 0.3)


# === block: score_1 (check id='check_ergo_L12') ===
def score_1(artifact, step, ctx):
    data = artifact.get("ergodicity_times", {})
    val = data.get("12", {}).get("mean", None)
    if not isinstance(val, (int, float)):
        return 0.0
    target = 2607.0
    rel_tol = 0.2
    rel_dev = abs(val - target) / target
    if rel_dev <= rel_tol:
        return 1.0
    return max(0.0, 1.0 - (rel_dev - rel_tol) / 0.3)


# === block: score_2 (check id='check_ergo_L24') ===
def score_2(artifact, step, ctx):
    data = artifact.get("ergodicity_times", {})
    val = data.get("24", {}).get("mean", None)
    if not isinstance(val, (int, float)):
        return 0.0
    target = 193750.0
    rel_tol = 0.2
    rel_dev = abs(val - target) / target
    if rel_dev <= rel_tol:
        return 1.0
    return max(0.0, 1.0 - (rel_dev - rel_tol) / 0.3)


# === block: score_3 (check id='check_ergo_L48') ===
def score_3(artifact, step, ctx):
    data = artifact.get("ergodicity_times", {})
    val = data.get("48", {}).get("mean", None)
    if not isinstance(val, (int, float)):
        return 0.0
    target = 1457315.0
    rel_tol = 0.2
    rel_dev = abs(val - target) / target
    if rel_dev <= rel_tol:
        return 1.0
    return max(0.0, 1.0 - (rel_dev - rel_tol) / 0.3)


# === block: score_4 (check id='check_scaling_exponent_recompute') ===
def score_4(artifact, step, ctx):
    L_vals = artifact.get("L_values")
    if not isinstance(L_vals, list) or len(L_vals) < 4:
        return 0.0
    erg = artifact.get("ergodicity_times", {})
    try:
        Ls = np.array([4,12,24,48], dtype=float)
        taus = np.array([erg[str(L)]["mean"] for L in [4,12,24,48]], dtype=float)
        logL = np.log10(Ls)
        logtau = np.log10(taus)
        slope = np.polyfit(logL, logtau, 1)[0]
    except Exception:
        return 0.0
    target = 4.4
    tol = 0.5
    diff = abs(slope - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff - tol) / 0.5)


# === block: score_5 (check id='check_energy_infinite') ===
def score_5(artifact, step, ctx):
    e0 = artifact.get("energy_infinite")
    if not isinstance(e0, (int, float)):
        return 0.0
    target = -1.394
    tol = 0.014
    if abs(e0 - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_6 (check id='check_entropy_infinite') ===
def score_6(artifact, step, ctx):
    s0 = artifact.get("entropy_infinite")
    if not isinstance(s0, (int, float)):
        return 0.0
    target = 0.081
    tol = 0.008
    if abs(s0 - target) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'check_ergo_L4': score_0,
    'check_ergo_L12': score_1,
    'check_ergo_L24': score_2,
    'check_ergo_L48': score_3,
    'check_scaling_exponent_recompute': score_4,
    'check_energy_infinite': score_5,
    'check_entropy_infinite': score_6,
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
