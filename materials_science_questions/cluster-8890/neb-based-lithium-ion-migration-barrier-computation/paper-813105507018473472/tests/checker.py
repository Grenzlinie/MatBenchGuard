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
    ctx = {}
    steps = spec.get("steps", [])
    for step in steps:
        sid = step["id"]
        if sid == "volumes":
            ctx["volumes_gold"] = step.get("gold", {})
            ctx["rel_tol"] = step.get("rel_tolerance", 0.05)
            ctx["rel_max"] = step.get("rel_max_decay", 0.15)
            ctx["swelling"] = step.get("swelling_checks", {})
        elif sid == "barriers":
            ctx["max_barrier"] = step.get("max_barrier", 0.3)
            ctx["decay_width"] = step.get("decay_width", 0.2)
            ctx["structural_weight"] = step.get("structural_weight", 0.2)
            ctx["trend"] = step.get("n8_n16_trend", "n8 >= n16")
    return ctx


# === block: score_0 (check id='volumes') ===
def score_0(artifact, step, ctx):
    gold = ctx["volumes_gold"]
    rel_tol = ctx["rel_tol"]
    rel_max = ctx["rel_max"]
    swelling = ctx.get("swelling", {})
    vol_scores = []
    for key in ["structure1","structure2","structure3","structure4","structure6"]:
        if key not in artifact:
            vol_scores.append(0.0)
            continue
        v = artifact[key]
        g = gold.get(key)
        if g is None or g == 0:
            vol_scores.append(0.0)
        else:
            err = abs(v - g) / g
            if err <= rel_tol:
                s = 1.0
            elif err >= rel_max:
                s = 0.0
            else:
                s = 1.0 - (err - rel_tol) / (rel_max - rel_tol)
            vol_scores.append(s)
    avg_vol = sum(vol_scores) / max(1, len(vol_scores))
    swelling_scores = []
    dry_key = swelling.get("dry", "structure1")
    dry_vol = artifact.get(dry_key)
    if dry_vol and dry_vol > 0:
        for key in swelling.get("n8_structures", []):
            v = artifact.get(key)
            if v:
                factor = v / dry_vol
                lo, hi = swelling.get("swelling_range_n8", [4.0,6.0])
                if lo <= factor <= hi:
                    swelling_scores.append(1.0)
                else:
                    swelling_scores.append(0.0)
        key16 = swelling.get("n16_structure")
        if key16:
            v16 = artifact.get(key16)
            if v16:
                factor16 = v16 / dry_vol
                lo16, hi16 = swelling.get("swelling_range_n16", [6.0,8.0])
                if lo16 <= factor16 <= hi16:
                    swelling_scores.append(1.0)
                else:
                    swelling_scores.append(0.0)
    avg_swell = sum(swelling_scores) / max(1, len(swelling_scores))
    swell_weight = swelling.get("swelling_weight", 0.3)
    vol_weight = 1.0 - swell_weight
    score = vol_weight * avg_vol + swell_weight * avg_swell
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='barriers') ===
def score_1(artifact, step, ctx):
    max_barrier = ctx["max_barrier"]
    decay_width = ctx["decay_width"]
    n8 = artifact.get("n8")
    n16 = artifact.get("n16")
    if n8 is None or n16 is None:
        return 0.0
    def barrier_score(val):
        if val < 0.05:
            return max(0.0, val / 0.05)
        elif val <= max_barrier:
            return 1.0
        else:
            return max(0.0, 1.0 - (val - max_barrier) / decay_width)
    s8 = barrier_score(n8)
    s16 = barrier_score(n16)
    structural = 1.0 if n8 >= n16 else 0.0
    w_struct = ctx.get("structural_weight", 0.2)
    w_bar = (1.0 - w_struct) / 2.0
    score = w_bar * s8 + w_bar * s16 + w_struct * structural
    return max(0.0, min(1.0, score))


_SCORERS = {
    'volumes': score_0,
    'barriers': score_1,
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
