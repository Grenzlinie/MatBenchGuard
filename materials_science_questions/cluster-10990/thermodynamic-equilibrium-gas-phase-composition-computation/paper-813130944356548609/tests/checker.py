import os
import json
import csv

# === author imports / helpers ===
import csv


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


# === block: score_0 (check id='equilibrium_metrics') ===
def score_0(artifact, step, ctx):
    # artifact: list of dicts from CSV with required columns
    if not artifact or len(artifact) == 0:
        return 0.0
    rows = sorted(artifact, key=lambda r: float(r['temperature_K']))
    temps = [float(r['temperature_K']) for r in rows]
    sio2s = [float(r['SiO2(s)']) for r in rows]
    al2o3s = [float(r['Al2O3(s)']) for r in rows]
    fe2o3s = [float(r['Fe2O3(s)']) for r in rows]
    fe3o4s = [float(r['Fe3O4(s)']) for r in rows]
    sio2g = [float(r['SiO2(g)']) for r in rows]
    alog = [float(r['AlO(g)']) for r in rows]

    threshold_fraction = 0.01
    epsilon = step.get('gas_present_epsilon', 1e-9)

    def find_disappear_temperature(masses, temps):
        max_mass = max(masses) if masses else 0.0
        if max_mass == 0.0:
            return None
        threshold = threshold_fraction * max_mass
        for m, t in zip(masses, temps):
            if m < threshold:
                return t
        return None

    t_sio2_disappear = find_disappear_temperature(sio2s, temps)
    t_al2o3_disappear = find_disappear_temperature(al2o3s, temps)

    sio2_range = step['sio2_disappear_range']
    al2o3_min = step['al2o3_disappear_min']

    def score_sio2_disappear(t):
        if t is None:
            return 0.0
        low, high = sio2_range
        if low <= t <= high:
            return 1.0
        dist = min(abs(t - low), abs(t - high))
        return max(0.0, 1.0 - dist / 1000.0)

    def score_al2o3_disappear(t):
        if t is None:
            return 1.0
        if t >= al2o3_min:
            return 1.0
        dist = al2o3_min - t
        return max(0.0, 1.0 - dist / 1000.0)

    s1 = score_sio2_disappear(t_sio2_disappear)
    s2 = score_al2o3_disappear(t_al2o3_disappear)

    # dominant iron phase above 2000 K
    candidates = [(i, fe3o4s[i] + fe2o3s[i]) for i, T in enumerate(temps) if T > 2000]
    if candidates:
        idx, _ = max(candidates, key=lambda x: x[1])
        if fe3o4s[idx] > fe2o3s[idx]:
            dominant = 'Fe3O4'
        elif fe2o3s[idx] > fe3o4s[idx]:
            dominant = 'Fe2O3'
        else:
            dominant = None
    else:
        dominant = None

    s3 = 1.0 if dominant == step.get('dominant_iron_phase_expected') else 0.0

    # gas presence above 3000 K
    sio2g_present = any(sio2g[i] > epsilon for i, T in enumerate(temps) if T > 3000)
    alog_present = any(alog[i] > epsilon for i, T in enumerate(temps) if T > 3000)
    s4 = 1.0 if sio2g_present else 0.0
    s5 = 1.0 if alog_present else 0.0

    sub_weights = step['sub_weights']
    total = (sub_weights['sio2_disappear'] * s1 +
             sub_weights['al2o3_disappear'] * s2 +
             sub_weights['dominant_iron'] * s3 +
             sub_weights['sio2_gas_present'] * s4 +
             sub_weights['alo_gas_present'] * s5)
    return total


_SCORERS = {
    'equilibrium_metrics': score_0,
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
