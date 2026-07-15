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


# === block: score_0 (check id='step_masses') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    try:
        me_mapbi3 = float(data["MAPbI3_eff_mass_electron"])
        mh_mapbi3 = float(data["MAPbI3_eff_mass_hole"])
        me_mapbmn = float(data["MAPbMn_eff_mass_electron"])
        mh_mapbmn = float(data["MAPbMn_eff_mass_hole"])
    except (KeyError, TypeError, ValueError):
        return 0.0

    # Positivity
    pos = 1.0 if (me_mapbi3 > 0 and mh_mapbi3 > 0 and me_mapbmn > 0 and mh_mapbmn > 0) else 0.0

    # MAPbI3 balance (ratio in [0.5, 2.0])
    ratio_mapbi3 = mh_mapbi3 / me_mapbi3 if me_mapbi3 != 0 else float('inf')
    bal = 1.0 if 0.5 <= ratio_mapbi3 <= 2.0 else 0.0

    # MAPbMn ratio (target >> 1)
    ratio_mapbmn = mh_mapbmn / me_mapbmn if me_mapbmn != 0 else float('inf')
    if ratio_mapbmn >= 2.5:
        ratio_score = 1.0
    elif ratio_mapbmn >= 1.0:
        ratio_score = (ratio_mapbmn - 1.0) / 1.5
    else:
        ratio_score = 0.0

    # Distance‑based closeness to paper reference values
    ref = {
        "MAPbI3_eff_mass_electron": 0.23,
        "MAPbI3_eff_mass_hole": 0.25,
        "MAPbMn_eff_mass_electron": 0.25,
        "MAPbMn_eff_mass_hole": 1.37
    }
    closeness_scores = []
    tol_factor = 0.35  # allow up to 35% deviation per mass
    for key, val in zip(ref.keys(), [me_mapbi3, mh_mapbi3, me_mapbmn, mh_mapbmn]):
        ref_val = ref[key]
        err = min(abs(val - ref_val), tol_factor * ref_val)
        score = max(0.0, 1.0 - err / (tol_factor * ref_val))
        closeness_scores.append(score)
    closeness = sum(closeness_scores) / len(closeness_scores)

    # Combine with fixed weights
    w_pos = 0.05
    w_bal = 0.05
    w_ratio = 0.40
    w_closeness = 0.50

    total = w_pos * pos + w_bal * bal + w_ratio * ratio_score + w_closeness * closeness
    return total


_SCORERS = {
    'step_masses': score_0,
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
