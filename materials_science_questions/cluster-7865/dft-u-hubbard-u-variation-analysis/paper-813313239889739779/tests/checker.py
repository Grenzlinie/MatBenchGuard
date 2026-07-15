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


# === block: score_0 (check id='magnetic_data') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    row = artifact[0]
    checks = step.get('checks', [])
    passed = 0
    total = len(checks)
    if total == 0:
        return 1.0
    for check in checks:
        field = check['field']
        if field not in row:
            continue
        val = row[field]
        typ = check.get('type','')
        if typ == 'exact_string':
            if str(val).strip() == check['expected']:
                passed += 1
        elif typ == 'numeric_lower_bound':
            try:
                num = float(val)
            except:
                continue
            if num >= check['lower_bound']:
                passed += 1
        elif typ == 'numeric_abs_tol':
            try:
                num = float(val)
            except:
                continue
            if abs(num - check['gold']) <= check['tolerance']:
                passed += 1
    return passed / total


# === block: score_1 (check id='optical_spectra') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    energy_min = params.get('energy_min', 0.8)
    energy_max = params.get('energy_max', 1.5)
    gga_thresh = params.get('gga_peak_threshold', 0.3)
    ratio_thresh = params.get('u_suppression_ratio', 0.5)
    min_rows = params.get('min_rows', 200)
    if not artifact or not isinstance(artifact, list) or len(artifact) < min_rows:
        return 0.0
    energies = []
    eps_gga = []
    eps_ggau = []
    for row in artifact:
        try:
            e = float(row['energy_ev'])
            gga = float(row['epsilon2_gga'])
            ggau = float(row['epsilon2_gga_u'])
        except (ValueError, KeyError):
            continue
        energies.append(e)
        eps_gga.append(gga)
        eps_ggau.append(ggau)
    if len(energies) < min_rows:
        return 0.0
    max_gga_peak = 0.0
    max_ggau_peak = 0.0
    for e, gga, ggau in zip(energies, eps_gga, eps_ggau):
        if energy_min <= e <= energy_max:
            if gga > max_gga_peak:
                max_gga_peak = gga
            if ggau > max_ggau_peak:
                max_ggau_peak = ggau
    score = 0.0
    if max_gga_peak > gga_thresh:
        score += 0.5
    if max_ggau_peak < ratio_thresh * max_gga_peak:
        score += 0.5
    return score


_SCORERS = {
    'magnetic_data': score_0,
    'optical_spectra': score_1,
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
