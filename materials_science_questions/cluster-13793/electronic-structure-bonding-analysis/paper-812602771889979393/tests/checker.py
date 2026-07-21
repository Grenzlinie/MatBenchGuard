import os
import json
import csv

# === author imports / helpers ===
import csv, json, os


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
    return {"spec": spec}


# === block: score_0 (check id='step_02_binding_curves') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    data = {}
    for row in artifact:
        s = row.get('structure')
        if s is None:
            continue
        s = s.strip()
        try:
            v = float(row['volume_norm'])
            e = float(row['binding_energy'])
        except (ValueError, TypeError, KeyError):
            continue
        data.setdefault(s, []).append((v, e))
    required = ['diamond', 'wurtzite', 'white-tin(4)', 'fcc', 'bcc']
    for s in required:
        if s not in data or not data[s]:
            return 0.0
    diamond_pts = data['diamond']
    eq_vol = min(diamond_pts, key=lambda x: x[1])[0]
    def energy_at_vol(pts, target):
        idx = min(range(len(pts)), key=lambda i: abs(pts[i][0] - target))
        return pts[idx][1]
    e_d = energy_at_vol(diamond_pts, eq_vol)
    e_w = energy_at_vol(data['wurtzite'], eq_vol)
    e_t4 = energy_at_vol(data['white-tin(4)'], eq_vol)
    e_f = energy_at_vol(data['fcc'], eq_vol)
    e_b = energy_at_vol(data['bcc'], eq_vol)
    t4_min_vol = min(data['white-tin(4)'], key=lambda x: x[1])[0]
    conditions = [
        e_d < e_w,
        e_w < e_t4,
        e_t4 < e_f,
        e_t4 < e_b,
        t4_min_vol < eq_vol
    ]
    return sum(conditions) / len(conditions)


# === block: score_1 (check id='step_03_diamond_properties') ===
def score_1(artifact, step, ctx):
    refs = step.get('reference_values', {})
    if not isinstance(artifact, dict) or not refs:
        return 0.0
    # Enforce presence of all required fields specified in the instruction
    for key in refs:
        if key not in artifact:
            return 0.0
    tols = step.get('tolerances', {})
    total = 0.0
    cnt = 0
    for key in refs:
        val = float(artifact[key])
        tol = float(tols[key])
        diff = abs(val - refs[key])
        if diff <= tol:
            total += 1.0
        else:
            total += max(0.0, 1.0 - (diff - tol) / tol)
        cnt += 1
    return total / cnt if cnt > 0 else 0.0


_SCORERS = {
    'step_02_binding_curves': score_0,
    'step_03_diamond_properties': score_1,
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