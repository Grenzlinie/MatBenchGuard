import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import math
import os


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
    gold = {}
    tol = {}
    min_images = 8
    for step in spec.get('steps', []):
        if step['id'] == 'csv_check':
            gold.update(step.get('parameters', {}).get('gold_barriers', {}))
            tol['csv_tol'] = step.get('parameters', {}).get('tolerance', 0.2)
            min_images = step.get('parameters', {}).get('min_images', 8)
        elif step['id'] == 'json_check':
            gold.update(step.get('parameters', {}).get('target_values', {}))
            tol['json_tol'] = step.get('parameters', {}).get('tolerance', 0.2)
    return {'gold': gold, 'tol': tol, 'min_images': min_images}


# === block: score_0 (check id='csv_check') ===
def score_0(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    if not rows:
        return 0.0
    profiles = {}
    for r in rows:
        cs = r.get('charge_state', '').strip()
        idx = int(r.get('image_index', -1))
        try:
            en = float(r.get('energy', None))
        except:
            continue
        if cs not in profiles:
            profiles[cs] = []
        profiles[cs].append((idx, en))
    score_parts = []
    for cs, expected in ctx['gold'].items():
        key = cs.replace('^', '').replace('+', '^+').replace('-', '^-')  # normalize
        # map to CSV charge_state: V_As^+
        csv_key = key
        # fallback
        if csv_key not in profiles:
            for k in profiles:
                if k.replace(' ', '') == csv_key:
                    csv_key = k
                    break
        if csv_key not in profiles or len(profiles[csv_key]) == 0:
            score_parts.append(0.0)
            continue
        pts = profiles[csv_key]
        if len(pts) < ctx.get('min_images', 8):
            score_parts.append(0.0)
            continue
        energies = [e for _, e in pts]
        min_e = min(energies)
        max_e = max(energies)
        barrier = max_e - min_e
        if max_e - min_e < 0.001:  # flat profile
            score_parts.append(0.0)
            continue
        tol = ctx['tol'].get('csv_tol', 0.2)
        diff = abs(barrier - expected)
        if diff <= tol:
            score_parts.append(1.0)
        else:
            score_parts.append(max(0.0, 1.0 - (diff - tol) / (2 * tol)))  # linear decay beyond tol
    if not score_parts:
        return 0.0
    return sum(score_parts) / len(score_parts)


# === block: score_1 (check id='json_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = ctx['gold']
    tol = ctx['tol'].get('json_tol', 0.2)
    keys = [('V_As_plus_barrier', 'V_As^+'), ('V_As_minus_barrier', 'V_As^-')]
    score_parts = []
    for k, expected_key in keys:
        if k not in artifact:
            score_parts.append(0.0)
            continue
        val = artifact[k]
        if not isinstance(val, (int, float)):
            score_parts.append(0.0)
            continue
        expected = gold.get(expected_key)
        if expected is None:
            score_parts.append(1.0)  # no gold, pass
            continue
        diff = abs(val - expected)
        if diff <= tol:
            score_parts.append(1.0)
        else:
            score_parts.append(max(0.0, 1.0 - (diff - tol) / (2 * tol)))
    if not score_parts:
        return 0.0
    return sum(score_parts) / len(score_parts)


_SCORERS = {
    'csv_check': score_0,
    'json_check': score_1,
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
