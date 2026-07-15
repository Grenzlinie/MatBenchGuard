import os
import json
import csv

# === author imports / helpers ===
import os
import math
import json

def extract_shell_radii(xyz_text, gap_threshold=0.6):
    """
    Parse XYZ text, compute radial distances from z-axis (sqrt(x^2+y^2)),
    cluster atoms into shells using a gap threshold, and return sorted
    average radii from inner to outer.
    """
    lines = xyz_text.strip().split('\n')
    if len(lines) < 3:
        return []
    radii = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 3:
            continue
        try:
            x, y = float(parts[1]), float(parts[2])
            r = math.hypot(x, y)
            radii.append(r)
        except (ValueError, IndexError):
            continue
    if not radii:
        return []
    radii.sort()
    # cluster into shells
    shells = []
    current_shell = [radii[0]]
    for r in radii[1:]:
        if r - current_shell[-1] > gap_threshold:
            shells.append(current_shell)
            current_shell = [r]
        else:
            current_shell.append(r)
    shells.append(current_shell)
    # average per shell, sorted by average
    avg_radii = sorted([sum(sh)/len(sh) for sh in shells])
    return avg_radii


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
    gold_radii = spec.get('gold_radii', {})
    gold_indices = spec.get('gold_indices', {})
    return {
        'gold_radii': gold_radii,
        'gold_indices': gold_indices,
        'spec': spec
    }


# === block: score_0 (check id='radii_4.0') ===
def score_0(artifact, step, ctx):
    computed = extract_shell_radii(artifact)
    expected = ctx['gold_radii'].get('4.0', [])
    tol = 0.2
    if not computed or len(computed) != len(expected):
        return 0.0
    matched = 0
    for r_exp, r_comp in zip(expected, computed):
        if abs(r_exp - r_comp) <= tol:
            matched += 1
    return matched / len(expected)


# === block: score_1 (check id='radii_6.0') ===
def score_1(artifact, step, ctx):
    computed = extract_shell_radii(artifact)
    expected = ctx['gold_radii'].get('6.0', [])
    tol = 0.2
    if not computed or len(computed) != len(expected):
        return 0.0
    matched = 0
    for r_exp, r_comp in zip(expected, computed):
        if abs(r_exp - r_comp) <= tol:
            matched += 1
    return matched / len(expected)


# === block: score_2 (check id='radii_12.0') ===
def score_2(artifact, step, ctx):
    computed = extract_shell_radii(artifact)
    expected = ctx['gold_radii'].get('12.0', [])
    tol = 0.2
    if not computed or len(computed) != len(expected):
        return 0.0
    matched = 0
    for r_exp, r_comp in zip(expected, computed):
        if abs(r_exp - r_comp) <= tol:
            matched += 1
    return matched / len(expected)


# === block: score_3 (check id='summary_consistency') ===
def score_3(artifact, step, ctx):
    gold_indices = ctx['gold_indices']
    output_dir = '/app/outputs'
    score = 0.0
    for dkey in ['4.0','6.0','12.0']:
        # recompute radii from XYZ file
        xyz_path = os.path.join(output_dir, f'structure_{dkey}.xyz')
        if not os.path.exists(xyz_path):
            continue
        with open(xyz_path) as f:
            xyz_text = f.read()
        computed_radii = extract_shell_radii(xyz_text)
        summary_radii = artifact.get(dkey, {}).get('radii', [])
        # radii match within 0.01 of recomputed
        radii_ok = False
        if len(computed_radii) == len(summary_radii):
            radii_ok = all(abs(a-b) < 0.01 for a,b in zip(computed_radii, summary_radii))
        # indices exact match vs gold
        entry = artifact.get(dkey, {})
        kt_ok = entry.get('KT_index', '') == gold_indices.get(dkey, {}).get('KT', '')
        t_ok = entry.get('T_indices', []) == gold_indices.get(dkey, {}).get('T', [])
        if radii_ok and kt_ok and t_ok:
            score += 1.0
    # 3 diameters, each contributes equally
    return score / 3.0


_SCORERS = {
    'radii_4.0': score_0,
    'radii_6.0': score_1,
    'radii_12.0': score_2,
    'summary_consistency': score_3,
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
