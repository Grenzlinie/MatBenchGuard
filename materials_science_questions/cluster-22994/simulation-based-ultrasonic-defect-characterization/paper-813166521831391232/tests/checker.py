import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    import csv
    import numpy as np

    artifact = artifact  # loaded list of dicts

    # --- Structural sanity gate: if these fail, return 0.0 ---
    if not artifact or not isinstance(artifact, list) or len(artifact) < 30:
        return 0.0

    modes = {}
    for row in artifact:
        try:
            f = float(row['frequency_Hz'])
            m = int(row['mode_number'])
            v = float(row['phase_velocity_m_per_s'])
        except (KeyError, ValueError, TypeError):
            return 0.0
        modes.setdefault(m, []).append((f, v))

    # At least modes 1, 2, 3 must be present
    required_modes = {1, 2, 3}
    if not required_modes.issubset(modes.keys()):
        return 0.0

    # Each required mode must have at least 3 points and cover frequency beyond 0.9 MHz
    for m in required_modes:
        points = sorted(modes[m], key=lambda x: x[0])
        if len(points) < 3:
            return 0.0
        if points[-1][0] < 0.9e6:
            return 0.0

    # Velocity bounds (in m/s)
    for m in modes:
        for _, v in modes[m]:
            if v < 100 or v > 20000:
                return 0.0

    # --- Result-level comparison to digitized reference points from Fig. 2 ---
    # Reference points (frequency_Hz, mode_number, phase_velocity_m_per_s) are
    # extracted from the paper's phase‑velocity dispersion curves for the shell
    # with density=2800 kg/m³, outer radius=400 mm, thickness=1 mm.
    ref_points = [
        ( 100000, 1, 5450),
        ( 100000, 2, 3500),
        ( 100000, 3, 2550),
        ( 300000, 1, 5350),
        ( 300000, 2, 3450),
        ( 300000, 3, 2500),
        ( 600000, 1, 5250),
        ( 600000, 2, 3350),
        ( 600000, 3, 2400),
        ( 900000, 1, 5150),
        ( 900000, 2, 3250),
        ( 900000, 3, 2350),
    ]
    tolerance_rel = 0.05   # 5 % relative tolerance

    errors = []
    for rfreq, rmode, rvel in ref_points:
        if rmode not in modes:
            errors.append(1.0)
            continue
        points = modes[rmode]
        # Find the frequency closest to the reference point
        candidates = [(abs(f - rfreq), f, v) for f, v in points]
        candidates.sort(key=lambda x: x[0])
        if not candidates:
            errors.append(1.0)
            continue
        diff, best_f, best_v = candidates[0]
        if diff > 0.1 * rfreq:   # reject if the closest frequency is too far
            errors.append(1.0)
            continue
        rel_err = abs(best_v - rvel) / rvel
        errors.append(rel_err)

    mean_err = np.mean(errors) if errors else 0.0
    score = max(0.0, 1.0 - mean_err / tolerance_rel)
    return float(score)


_SCORERS = {
    's1': score_0,
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
