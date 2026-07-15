import os
import json
import csv

# === author imports / helpers ===
import re

def parse_xyz(content):
    """Parse an XYZ string with multiple frames.
    Returns (num_frames, atom_counts, element_set, all_finite)"""
    if not content:
        return 0, [], set(), False
    lines = content.strip().split('\n')
    line_idx = 0
    num_frames = 0
    atom_counts = []
    element_set = set()
    all_finite = True
    while line_idx < len(lines):
        line = lines[line_idx].strip()
        if not line:
            line_idx += 1
            continue
        try:
            nat = int(line)
            if nat <= 0:
                return 0, [], set(), False
        except ValueError:
            # not a valid frame header
            break
        line_idx += 1
        # skip comment line
        if line_idx >= len(lines):
            break
        line_idx += 1
        # read nat coordinate lines
        frame_coords = []
        for i in range(nat):
            if line_idx >= len(lines):
                break
            atom_line = lines[line_idx].strip()
            line_idx += 1
            parts = atom_line.split()
            if len(parts) < 4:
                continue
            elem = parts[0]
            element_set.add(elem)
            try:
                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])
                frame_coords.append((x, y, z))
            except ValueError:
                all_finite = False
                continue
        # frame complete
        num_frames += 1
        atom_counts.append(nat)
        if num_frames > 1000:  # safety
            break
    return num_frames, atom_counts, element_set, all_finite


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


# === block: score_0 (check id='barrier_gamma') ===
def score_0(artifact, step, ctx):
        val = artifact.get('gamma_alumina_barrier')
        if val is None:
            return 0.0
        target = step.get('target', 2.2)
        tol = step.get('tolerance_abs', 0.5)
        if abs(val - target) <= tol:
            return 1.0
        else:
            return 0.0


# === block: score_1 (check id='barrier_eta') ===
def score_1(artifact, step, ctx):
        val = artifact.get('eta_alumina_barrier')
        if val is None:
            return 0.0
        target = step.get('target', 5.0)
        tol = step.get('tolerance_abs', 0.5)
        if abs(val - target) <= tol:
            return 1.0
        else:
            return 0.0


# === block: score_2 (check id='barrier_ordering') ===
def score_2(artifact, step, ctx):
        gamma = artifact.get('gamma_alumina_barrier')
        eta = artifact.get('eta_alumina_barrier')
        if gamma is None or eta is None:
            return 0.0
        if eta > gamma:
            return 1.0
        else:
            return 0.0


# === block: score_3 (check id='xyz_gamma') ===
def score_3(artifact, step, ctx):
        expected = step.get('expected_atoms', 71)
        n_frames, atom_counts, element_set, all_finite = parse_xyz(artifact)
        if n_frames < 2:
            return 0.0
        if not all(ac == expected for ac in atom_counts):
            return 0.0
        required_elements = {'Al', 'O', 'Cr'}
        if not required_elements.issubset(element_set):
            return 0.0
        if not all_finite:
            return 0.0
        return 1.0


# === block: score_4 (check id='xyz_eta') ===
def score_4(artifact, step, ctx):
        expected = step.get('expected_atoms', 73)
        n_frames, atom_counts, element_set, all_finite = parse_xyz(artifact)
        if n_frames < 2:
            return 0.0
        if not all(ac == expected for ac in atom_counts):
            return 0.0
        required_elements = {'Al', 'O', 'Cr'}
        if not required_elements.issubset(element_set):
            return 0.0
        if not all_finite:
            return 0.0
        return 1.0


_SCORERS = {
    'barrier_gamma': score_0,
    'barrier_eta': score_1,
    'barrier_ordering': score_2,
    'xyz_gamma': score_3,
    'xyz_eta': score_4,
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
