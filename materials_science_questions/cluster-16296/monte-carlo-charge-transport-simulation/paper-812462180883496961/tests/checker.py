import os
import json
import csv

# === author imports / helpers ===
import csv, os


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


# === block: score_0 (check id='E20_T10') ===
def score_0(artifact, step, ctx):
    t_col = 'time_ps'
    qv_col = 'quantum_drift_velocity_cm_per_s'
    sv_col = 'semiclassical_drift_velocity_cm_per_s'
    q_vals, s_vals = [], []
    for row in artifact:
        t = float(row[t_col])
        if t < 0.5:
            try:
                q = float(row[qv_col])
                s = float(row[sv_col])
                q_vals.append(q)
                s_vals.append(s)
            except Exception:
                return 0.0
    if len(q_vals) < 2:
        return 0.0
    q_mean = sum(q_vals)/len(q_vals)
    s_mean = sum(s_vals)/len(s_vals)
    if q_mean < 1e6:
        return 0.0
    if s_mean <= 0:
        return 0.0
    ratio = q_mean / s_mean
    if ratio <= 1.0:
        return 0.0
    if ratio >= 1.2:
        return 1.0
    else:
        return (ratio - 1.0) / 0.2


# === block: score_1 (check id='E40_T10') ===
def score_1(artifact, step, ctx):
    t_col = 'time_ps'
    qv_col = 'quantum_drift_velocity_cm_per_s'
    sv_col = 'semiclassical_drift_velocity_cm_per_s'
    q_vals, s_vals = [], []
    for row in artifact:
        t = float(row[t_col])
        if t < 0.5:
            try:
                q = float(row[qv_col])
                s = float(row[sv_col])
                q_vals.append(q)
                s_vals.append(s)
            except Exception:
                return 0.0
    if len(q_vals) < 2:
        return 0.0
    q_mean = sum(q_vals)/len(q_vals)
    s_mean = sum(s_vals)/len(s_vals)
    if q_mean < 1e6:
        return 0.0
    if s_mean <= 0:
        return 0.0
    ratio = q_mean / s_mean
    if ratio <= 1.0:
        return 0.0
    if ratio >= 1.2:
        return 1.0
    else:
        return (ratio - 1.0) / 0.2


# === block: score_2 (check id='E60_T10') ===
def score_2(artifact, step, ctx):
    t_col = 'time_ps'
    qv_col = 'quantum_drift_velocity_cm_per_s'
    sv_col = 'semiclassical_drift_velocity_cm_per_s'
    q_vals, s_vals = [], []
    for row in artifact:
        t = float(row[t_col])
        if t < 0.5:
            try:
                q = float(row[qv_col])
                s = float(row[sv_col])
                q_vals.append(q)
                s_vals.append(s)
            except Exception:
                return 0.0
    if len(q_vals) < 2:
        return 0.0
    q_mean = sum(q_vals)/len(q_vals)
    s_mean = sum(s_vals)/len(s_vals)
    if q_mean < 1e6:
        return 0.0
    if s_mean <= 0:
        return 0.0
    ratio = q_mean / s_mean
    if ratio <= 1.0:
        return 0.0
    if ratio >= 1.2:
        return 1.0
    else:
        return (ratio - 1.0) / 0.2


# === block: score_3 (check id='E60_T300') ===
def score_3(artifact, step, ctx):
    t_col = 'time_ps'
    qv_col = 'quantum_drift_velocity_cm_per_s'
    sv_col = 'semiclassical_drift_velocity_cm_per_s'
    q_vals, s_vals = [], []
    for row in artifact:
        t = float(row[t_col])
        if t < 0.5:
            try:
                q = float(row[qv_col])
                s = float(row[sv_col])
                q_vals.append(q)
                s_vals.append(s)
            except Exception:
                return 0.0
    if len(q_vals) < 2:
        return 0.0
    q_mean = sum(q_vals)/len(q_vals)
    s_mean = sum(s_vals)/len(s_vals)
    if q_mean < 1e6:
        return 0.0
    if s_mean <= 0:
        return 0.0
    ratio = q_mean / s_mean
    if ratio <= 1.0:
        return 0.0
    if ratio >= 1.05:
        return 1.0
    else:
        return (ratio - 1.0) / 0.05


# === block: score_4 (check id='trend_10K') ===
def score_4(artifact, step, ctx):
    output_dir = "/app/outputs"
    files = ["drift_velocity_E20_T10.csv", "drift_velocity_E40_T10.csv", "drift_velocity_E60_T10.csv"]
    ratios = []
    for fname in files:
        path = os.path.join(output_dir, fname)
        if not os.path.exists(path):
            return 0.0
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            q_vals, s_vals = [], []
            for row in reader:
                try:
                    q = float(row['quantum_drift_velocity_cm_per_s'])
                    s = float(row['semiclassical_drift_velocity_cm_per_s'])
                    q_vals.append(q)
                    s_vals.append(s)
                except Exception:
                    pass
            if not q_vals or not s_vals:
                return 0.0
            q_peak = max(q_vals)
            s_peak = max(s_vals)
            if s_peak == 0:
                return 0.0
            ratios.append(q_peak / s_peak)
    R1, R2, R3 = ratios
    inc1 = 1.0 if R1 < R2 else 0.0
    inc2 = 1.0 if R2 < R3 else 0.0
    return (inc1 + inc2) / 2.0


# === block: score_5 (check id='mean_KE') ===
def score_5(artifact, step, ctx):
    output_dir = "/app/outputs"
    files = ["drift_velocity_E20_T10.csv", "drift_velocity_E40_T10.csv", "drift_velocity_E60_T10.csv", "drift_velocity_E60_T300.csv"]
    nonneg = True
    max_qke = 0.0
    for fname in files:
        path = os.path.join(output_dir, fname)
        if not os.path.exists(path):
            return 0.0
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    qke = float(row['quantum_mean_kinetic_energy_eV'])
                    ske = float(row['semiclassical_mean_kinetic_energy_eV'])
                    if qke < 0 or ske < 0:
                        nonneg = False
                    if qke > max_qke:
                        max_qke = qke
                except Exception:
                    return 0.0
    if not nonneg:
        return 0.0
    if max_qke < 0.001:
        return 0.0
    return 1.0


_SCORERS = {
    'E20_T10': score_0,
    'E40_T10': score_1,
    'E60_T10': score_2,
    'E60_T300': score_3,
    'trend_10K': score_4,
    'mean_KE': score_5,
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
