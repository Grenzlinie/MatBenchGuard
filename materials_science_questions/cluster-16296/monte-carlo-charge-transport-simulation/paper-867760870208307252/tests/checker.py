import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, json


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
    gold = spec.get('gold', {})
    return gold


# === block: score_0 (check id='step_transmission_shape') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    cols = set(rows[0].keys())
    required = {'L_shift', 'frequency', 'transmission'}
    if required.issubset(cols):
        return 1.0
    return 0.0


# === block: score_1 (check id='step_resonance_shape') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    cols = set(artifact[0].keys())
    required = {'L_shift', 'resonance_frequency', 'resonance_depth', 'local_field_enhancement'}
    if required.issubset(cols):
        return 1.0
    return 0.0


# === block: score_2 (check id='step_recompute_depth_freq') ===
def score_2(artifact, step, ctx):
    freq_target_0 = ctx.get('freq_0', 0.73)
    freq_target_48 = ctx.get('freq_48', 0.47)
    freq_tol = ctx.get('freq_tol', 0.15)
    depth_ratio_min = ctx.get('depth_increase_min_ratio', 1.2)

    groups = {}
    for row in artifact:
        try:
            l = float(row['L_shift'])
            f = float(row['frequency'])
            t = float(row['transmission'])
        except:
            continue
        groups.setdefault(l, []).append((f, t))

    def find_dip(offset, freq_low, freq_high):
        if offset not in groups:
            return None, None
        best_t = None
        best_f = None
        for f, t in groups[offset]:
            if freq_low <= f <= freq_high:
                if best_t is None or t < best_t:
                    best_t = t
                    best_f = f
        return best_f, best_t

    f0, t0 = find_dip(0, 0.6, 0.9)
    f48, t48 = find_dip(48, 0.3, 0.6)

    if t0 is None or t48 is None:
        return 0.0

    score = 0.0
    if t0 > t48 and (t0 / (t48 + 1e-12)) > depth_ratio_min:
        score += 0.5
    if f0 and abs(f0 - freq_target_0) / freq_target_0 <= freq_tol:
        score += 0.25
    if f48 and abs(f48 - freq_target_48) / freq_target_48 <= freq_tol:
        score += 0.25
    return min(1.0, score)


# === block: score_3 (check id='step_field_enhancement') ===
def score_3(artifact, step, ctx):
    val0 = None
    val48 = None
    for row in artifact:
        try:
            l = float(row['L_shift'])
        except:
            continue
        enf = row.get('local_field_enhancement', '').strip()
        if enf == '':
            continue
        try:
            enf = float(enf)
        except:
            continue
        if l == 0:
            val0 = enf
        elif l == 48:
            val48 = enf

    if val0 is None or val48 is None or val0 <= 0 or val48 <= 0:
        return 0.0
    ratio = val48 / val0
    min_r = ctx.get('field_enhancement_min_ratio', 2.5)
    max_r = ctx.get('field_enhancement_max_ratio', 6.0)
    if min_r <= ratio <= max_r:
        return 1.0
    return 0.0


_SCORERS = {
    'step_transmission_shape': score_0,
    'step_resonance_shape': score_1,
    'step_recompute_depth_freq': score_2,
    'step_field_enhancement': score_3,
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
