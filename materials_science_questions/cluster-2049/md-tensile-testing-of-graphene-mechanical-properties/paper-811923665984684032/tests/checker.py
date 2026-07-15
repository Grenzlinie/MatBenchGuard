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
    return {}


# === block: score_0 (check id='key_zero_strain') ===
def score_0(artifact, step, ctx):
    targets = step['params']['targets']
    tolerance = step['params']['tolerance']
    matches = 0
    for t in targets:
        row = None
        for r in artifact:
            try:
                if (abs(float(r['side_length_nm'])-t['side_length_nm'])<0.02
                    and abs(float(r['width_nm'])-t['width_nm'])<0.02
                    and r['chirality'].strip().lower()==t['chirality'].lower()
                    and abs(float(r['strain_fraction'])-t['strain_fraction'])<1e-6):
                    row = r
                    break
            except: pass
        if row is None:
            continue
        freq = float(row['frequency_ghz'])
        if freq <= 0:
            continue
        rel_err = abs(freq - t['frequency_ghz']) / float(t['frequency_ghz'])
        if rel_err <= tolerance:
            matches += 1
    score = matches / len(targets) if targets else 1.0
    return score


# === block: score_1 (check id='key_strained_frequencies') ===
def score_1(artifact, step, ctx):
    targets = step['params']['targets']
    tolerance = step['params']['tolerance']
    matches = 0
    for t in targets:
        row = None
        for r in artifact:
            try:
                if (abs(float(r['side_length_nm'])-t['side_length_nm'])<0.02
                    and abs(float(r['width_nm'])-t['width_nm'])<0.02
                    and r['chirality'].strip().lower()==t['chirality'].lower()
                    and abs(float(r['strain_fraction'])-t['strain_fraction'])<1e-6):
                    row = r
                    break
            except: pass
        if row is None:
            continue
        freq = float(row['frequency_ghz'])
        if freq <= 0:
            continue
        rel_err = abs(freq - t['frequency_ghz']) / float(t['frequency_ghz'])
        if rel_err <= tolerance:
            matches += 1
    score = matches / len(targets) if targets else 1.0
    return score


# === block: score_2 (check id='monotonic_strain') ===
def score_2(artifact, step, ctx):
    groups = {}
    for r in artifact:
        try:
            key = (round(float(r['side_length_nm']),4), round(float(r['width_nm']),4), r['chirality'].strip())
            strain = float(r['strain_fraction'])
            freq = float(r['frequency_ghz'])
            if freq <= 0:
                continue
            groups.setdefault(key, []).append((strain, freq))
        except: pass
    total_pairs = 0
    violations = 0
    for key, values in groups.items():
        values.sort(key=lambda x: x[0])
        for i in range(len(values)-1):
            total_pairs += 1
            if values[i+1][1] < values[i][1] - 1e-9:
                violations += 1
    if total_pairs == 0:
        return 0.0
    return max(0.0, 1.0 - violations/total_pairs)


# === block: score_3 (check id='aspect_ratio_insensitivity') ===
def score_3(artifact, step, ctx):
    target_side_zig = step['params']['target_side_zig']
    target_side_arm = step['params']['target_side_arm']
    strain = step['params']['strain']
    max_dev = step['params']['max_relative_deviation']
    def check(chirality, target_side):
        freqs = []
        for r in artifact:
            try:
                side = float(r['side_length_nm'])
                if abs(side - target_side) > 0.05:
                    continue
                if r['chirality'].strip().lower() != chirality:
                    continue
                if abs(float(r['strain_fraction']) - strain) > 1e-6:
                    continue
                freq = float(r['frequency_ghz'])
                if freq > 0:
                    freqs.append(freq)
            except: pass
        if len(freqs) < 2:
            return 1.0
        mean = sum(freqs)/len(freqs)
        max_rel = max(abs(f-mean)/mean for f in freqs)
        if max_rel <= max_dev:
            return 1.0
        return max(0.0, 1.0 - (max_rel - max_dev)/(0.5 - max_dev))
    score_zig = check('zigzag', target_side_zig)
    score_arm = check('armchair', target_side_arm)
    return (score_zig + score_arm) / 2.0


# === block: score_4 (check id='chirality_insensitivity') ===
def score_4(artifact, step, ctx):
    pairs = step['params']['pairs']
    max_diff = step['params']['max_relative_diff']
    strain = step['params']['strain']
    total = 0
    score_sum = 0.0
    for pair in pairs:
        side = pair['side']
        zig_width = pair['zig_width']
        arm_width = pair['arm_width']
        zig_freq = None
        arm_freq = None
        for r in artifact:
            try:
                if abs(float(r['side_length_nm'])-side) > 0.02:
                    continue
                if abs(float(r['strain_fraction'])-strain) > 1e-6:
                    continue
                width = float(r['width_nm'])
                chir = r['chirality'].strip().lower()
                if chir == 'zigzag' and abs(width - zig_width) < 0.02:
                    zig_freq = float(r['frequency_ghz'])
                elif chir == 'armchair' and abs(width - arm_width) < 0.02:
                    arm_freq = float(r['frequency_ghz'])
            except: pass
        if zig_freq is None or arm_freq is None or zig_freq <= 0 or arm_freq <= 0:
            continue
        rel = abs(zig_freq - arm_freq) / ((zig_freq + arm_freq)/2.0)
        if rel <= max_diff:
            score_sum += 1.0
        else:
            score_sum += max(0.0, 1.0 - (rel - max_diff)/(0.3 - max_diff))
        total += 1
    return score_sum / total if total > 0 else 1.0


_SCORERS = {
    'key_zero_strain': score_0,
    'key_strained_frequencies': score_1,
    'monotonic_strain': score_2,
    'aspect_ratio_insensitivity': score_3,
    'chirality_insensitivity': score_4,
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
