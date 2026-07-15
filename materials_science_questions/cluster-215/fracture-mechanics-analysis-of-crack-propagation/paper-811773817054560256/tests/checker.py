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
    import os, json, csv
    def prepare(outputs_dir, spec):
        summary_path = os.path.join(outputs_dir, "simulation_summary.json")
        csv_path = os.path.join(outputs_dir, "load_displacement.csv")
        summary = None
        csv_rows = []
        if os.path.exists(summary_path):
            with open(summary_path) as f:
                summary = json.load(f)
        if os.path.exists(csv_path):
            with open(csv_path, newline='') as f:
                reader = csv.DictReader(f)
                csv_rows = list(reader)
        return {"summary": summary, "csv_rows": csv_rows}


# === block: score_0 (check id='sim_summary_location') ===
def score_0(artifact, step, ctx):
    artifact = ctx["summary"]
    if artifact is None: return 0.0
    return 1.0 if artifact.get("crack_initiation_location") == "die_radius" else 0.0


# === block: score_1 (check id='sim_summary_mode') ===
def score_1(artifact, step, ctx):
    artifact = ctx["summary"]
    if artifact is None: return 0.0
    return 1.0 if artifact.get("fracture_mode") == "flat" else 0.0


# === block: score_2 (check id='sim_summary_travel') ===
def score_2(artifact, step, ctx):
    artifact = ctx["summary"]
    if artifact is None: return 0.0
    val = artifact.get("punch_travel_at_first_fracture_mm")
    if val is None: return 0.0
    diff = abs(val - 14.2)
    return 1.0 if diff <= 0.5 else 0.0


# === block: score_3 (check id='sim_summary_force') ===
def score_3(artifact, step, ctx):
    artifact = ctx["summary"]
    if artifact is None: return 0.0
    val = artifact.get("peak_force_N")
    if val is None: return 0.0
    diff = abs(val - 85000.0)
    return 1.0 if diff <= 2000.0 else 0.0


# === block: score_4 (check id='load_curve_structural') ===
def score_4(artifact, step, ctx):
    csv_rows = ctx["csv_rows"]
    summary = ctx["summary"]
    if not csv_rows or summary is None:
        return 0.0
    disps = []
    forces = []
    for row in csv_rows:
        try:
            d = float(row["punch_displacement_mm"])
            f = float(row["punch_force_N"])
            disps.append(d)
            forces.append(f)
        except:
            return 0.0
    n = len(disps)
    if n < 2:
        return 0.0
    # monotonic displacement
    mono = True
    for i in range(1, n):
        if disps[i] < disps[i-1] - 1e-6:
            mono = False
            break
    # peak
    peak_idx = max(range(n), key=lambda i: forces[i])
    peak_force = forces[peak_idx]
    peak_disp = disps[peak_idx]
    peak_force_summary = summary.get("peak_force_N")
    punch_travel = summary.get("punch_travel_at_first_fracture_mm")
    peak_ok = False
    if peak_force_summary is not None and punch_travel is not None:
        if abs(peak_force - peak_force_summary) <= 2000.0 and abs(peak_disp - punch_travel) <= 0.5:
            peak_ok = True
    # sharp drop: within next 5 points after peak, force <= 0.8*peak_force
    sharp = False
    for i in range(peak_idx+1, min(peak_idx+6, n)):
        if forces[i] <= 0.8 * peak_force:
            sharp = True
            break
    score = 0.0
    if mono:
        score += 0.3
    if peak_ok:
        score += 0.3
    if sharp:
        score += 0.4
    return min(1.0, score)


_SCORERS = {
    'sim_summary_location': score_0,
    'sim_summary_mode': score_1,
    'sim_summary_travel': score_2,
    'sim_summary_force': score_3,
    'load_curve_structural': score_4,
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
