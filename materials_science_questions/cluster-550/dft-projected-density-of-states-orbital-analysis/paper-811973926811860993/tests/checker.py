import os
import json
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


# === block: score_0 (check id='step_geometry') ===
def score_0(artifact, step, ctx):
    checks = step.get('checks', [])
    total = 0.0
    for c in checks:
        cid = c['id']
        w = c.get('weight', 0.0)
        if cid == 'adsorption_site':
            if artifact.get('adsorption_site') == c['value']:
                total += w
        elif cid == 'sc_tilt_angle':
            angle = artifact.get('sc_tilt_angle_deg')
            if angle is not None and c['min'] <= angle <= c['max']:
                total += w
        elif cid == 'total_energy':
            energy = artifact.get('total_energy_eV')
            if energy is not None and energy < 0:
                total += w
    return total


# === block: score_1 (check id='step_ldos') ===
def score_1(artifact, step, ctx):
    rows = artifact
    # locate energy 0 row
    idx_zero = None
    for i, row in enumerate(rows):
        en = float(row['energy'])
        if abs(en) < 0.001:
            idx_zero = i
            break
    if idx_zero is None:
        # closest to zero
        min_diff = None
        for i, row in enumerate(rows):
            en = float(row['energy'])
            diff = abs(en)
            if min_diff is None or diff < min_diff:
                min_diff = diff
                idx_zero = i
    if idx_zero is None:
        return 0.0
    ldos_s_ef = float(rows[idx_zero]['LDOS_S'])
    ldos_c_ef = float(rows[idx_zero]['LDOS_C'])
    # max LDOS_S in (0, 0.5]
    max_s_empty = 0.0
    for row in rows:
        en = float(row['energy'])
        if 0 < en <= 0.5:
            val = float(row['LDOS_S'])
            if val > max_s_empty:
                max_s_empty = val
    checks = step.get('checks', [])
    total = 0.0
    for c in checks:
        cid = c['id']
        w = c.get('weight', 0.0)
        if cid == 'ldos_s_ef':
            if ldos_s_ef > 0.02:
                total += w
        elif cid == 'ldos_c_ef':
            if ldos_c_ef < 0.02:
                total += w
        elif cid == 'ldos_s_empty':
            if max_s_empty > 0.02:
                total += w
    return total


_SCORERS = {
    'step_geometry': score_0,
    'step_ldos': score_1,
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
