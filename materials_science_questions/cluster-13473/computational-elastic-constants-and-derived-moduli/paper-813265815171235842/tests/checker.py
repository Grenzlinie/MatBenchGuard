import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import json


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


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    targets = step.get('targets', [])
    tolerances = step.get('tolerances', {})
    total = 0
    score = 0.0
    for t in targets:
        mat = t.get('material', '').strip().lower()
        row = None
        for r in artifact:
            if r.get('material', '').strip().lower() == mat:
                row = r
                break
        if row is None:
            total += 5
            continue
        for field in ['c11','c12','c44','C_prime','B']:
            total += 1
            try:
                val = float(row.get(field, float('nan')))
            except (ValueError, TypeError):
                continue
            target = float(t.get(field, float('nan')))
            tol = tolerances.get(field, {})
            if 'rel' in tol:
                allowed = tol['rel'] * abs(target)
            elif 'abs' in tol:
                allowed = tol['abs']
            else:
                allowed = 1e-6
            if abs(val - target) <= allowed:
                score += 1.0
    return score / max(total, 1)


# === block: score_1 (check id='step3') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    row = artifact[0]
    targets = step.get('targets', [{}])[0]
    tolerances = step.get('tolerances', {})
    total = 0
    score = 0.0
    for field in ['R_SiSi','R_SiGe','R_GeGe','c_over_a','excess_energy']:
        total += 1
        try:
            val = float(row.get(field, float('nan')))
        except (ValueError, TypeError):
            continue
        target = float(targets.get(field, float('nan')))
        tol = tolerances.get(field, {})
        if 'abs' in tol:
            allowed = tol['abs']
        elif 'rel' in tol:
            allowed = tol['rel'] * abs(target)
        else:
            allowed = 1e-6
        if abs(val - target) <= allowed:
            score += 1.0
    return score / max(total, 1)


# === block: score_2 (check id='step4') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    targets = step.get('targets', [])
    # Only score Gamma_optical modes – the paper does not report zone‑edge TA frequencies
    gamma_targets = [t for t in targets if t.get('mode', '').strip().lower() == 'gamma_optical']
    total = len(gamma_targets)
    if total == 0:
        return 0.0
    score = 0.0
    for t in gamma_targets:
        mat = t.get('material', '').strip().lower()
        mode = t.get('mode', '').strip().lower()
        gold_freq = float(t.get('frequency', 0))
        tol_abs = float(t.get('tolerance_abs', 0))
        found = False
        for r in artifact:
            r_mat = r.get('material', '').strip().lower()
            r_mode = r.get('mode', '').strip().lower()
            if r_mat == mat and r_mode == mode:
                try:
                    freq = float(r.get('frequency', float('nan')))
                    if abs(freq - gold_freq) <= tol_abs:
                        score += 1.0
                except (ValueError, TypeError):
                    pass
                found = True
                break
        # if not found, score already not incremented
    return score / total


# === block: score_3 (check id='step5') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    targets = step.get('targets', [])
    tolerances = step.get('tolerances', {})
    total = len(targets) * 2  # energy and c_over_a per structure
    score = 0.0
    for t in targets:
        struct = t.get('structure', '').strip().lower()
        row = None
        for r in artifact:
            if r.get('structure', '').strip().lower() == struct:
                row = r
                break
        if row is None:
            continue
        for field in ['energy','c_over_a']:
            try:
                val = float(row.get(field, float('nan')))
            except (ValueError, TypeError):
                continue
            target = float(t.get(field, float('nan')))
            tol = tolerances.get(field, {})
            if 'abs' in tol:
                allowed = tol['abs']
            elif 'rel' in tol:
                allowed = tol['rel'] * abs(target)
            else:
                allowed = 1e-6
            if abs(val - target) <= allowed:
                score += 1.0
    return score / max(total, 1)


_SCORERS = {
    'step2': score_0,
    'step3': score_1,
    'step4': score_2,
    'step5': score_3,
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
