import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os

def parse_xyz(text):
    lines = text.strip().splitlines()
    if len(lines) < 3:
        return []
    coords = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) >= 4:
            try:
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                coords.append((x,y,z))
            except:
                continue
    return coords

def dist(p1, p2):
    return math.sqrt(sum((a-b)**2 for a,b in zip(p1, p2)))

def parse_frequencies(text):
    freqs = []
    for line in text.strip().splitlines():
        try:
            freqs.append(float(line.strip()))
        except:
            pass
    freqs.sort()
    return freqs

def load_csv_summary(path):
    if not os.path.exists(path):
        return None
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


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


# === block: score_0 (check id='check_sin_geometry') ===
def score_0(artifact, step, ctx):
    coords = parse_xyz(artifact)
    if len(coords) != 2:
        return 0.0
    d = dist(coords[0], coords[1])
    gold = step['params']['bonds'][0]['gold']
    tol = step['params']['bonds'][0]['tol']
    return 1.0 if abs(d - gold) <= tol else 0.0


# === block: score_1 (check id='check_sin_freq') ===
def score_1(artifact, step, ctx):
    freqs = parse_frequencies(artifact)
    if len(freqs) != 1:
        return 0.0
    gold = step['params']['freqs_gold'][0]
    tol = step['params']['tol_freq']
    return 1.0 if abs(freqs[0] - gold) <= tol else 0.0


# === block: score_2 (check id='check_sin2_geometry') ===
def score_2(artifact, step, ctx):
    coords = parse_xyz(artifact)
    if len(coords) < 3:
        return 0.0
    bonds = step['params']['bonds']
    correct = 0
    for b in bonds:
        gold = b['gold']
        tol_val = b['tol']
        pos = b['pos']
        if isinstance(pos[0], list):
            all_ok = True
            for pair in pos:
                p1, p2 = pair
                if p1 < len(coords) and p2 < len(coords):
                    d = dist(coords[p1], coords[p2])
                    if abs(d - gold) > tol_val:
                        all_ok = False
                        break
                else:
                    all_ok = False
                    break
            if all_ok:
                correct += 1
        else:
            p1, p2 = pos
            if p1 < len(coords) and p2 < len(coords):
                d = dist(coords[p1], coords[p2])
                if abs(d - gold) <= tol_val:
                    correct += 1
            else:
                pass
    score = correct / len(bonds) if bonds else 0.0
    return score


# === block: score_3 (check id='check_sin2_freq') ===
def score_3(artifact, step, ctx):
    freqs = parse_frequencies(artifact)
    expected = step['params']['freqs_gold']
    if len(freqs) != len(expected):
        return 0.0
    tol = step['params']['tol_freq']
    ok = sum(1 for f, g in zip(freqs, expected) if abs(f - g) <= tol)
    return ok / len(expected)


# === block: score_4 (check id='check_si2n_geometry') ===
def score_4(artifact, step, ctx):
    coords = parse_xyz(artifact)
    if len(coords) < 3:
        return 0.0
    bonds = step['params']['bonds']
    correct = 0
    for b in bonds:
        gold = b['gold']
        tol_val = b['tol']
        pos = b['pos']
        if isinstance(pos[0], list):
            all_ok = True
            for pair in pos:
                p1, p2 = pair
                if p1 < len(coords) and p2 < len(coords):
                    d = dist(coords[p1], coords[p2])
                    if abs(d - gold) > tol_val:
                        all_ok = False
                        break
                else:
                    all_ok = False
                    break
            if all_ok:
                correct += 1
        else:
            p1, p2 = pos
            if p1 < len(coords) and p2 < len(coords):
                d = dist(coords[p1], coords[p2])
                if abs(d - gold) <= tol_val:
                    correct += 1
            else:
                pass
    score = correct / len(bonds) if bonds else 0.0
    return score


# === block: score_5 (check id='check_si2n_freq') ===
def score_5(artifact, step, ctx):
    freqs = parse_frequencies(artifact)
    expected = step['params']['freqs_gold']
    if len(freqs) != len(expected):
        return 0.0
    tol = step['params']['tol_freq']
    ok = sum(1 for f, g in zip(freqs, expected) if abs(f - g) <= tol)
    return ok / len(expected)


# === block: score_6 (check id='check_consistency') ===
def score_6(artifact, step, ctx):
    systems = step['params']['systems']
    tight_bond_tol = step['params']['tight_bond_tol']
    tight_freq_tol = step['params']['tight_freq_tol']
    csv_rows = load_csv_summary(os.path.join('/app/outputs', 'benchmark_summary.csv'))
    if csv_rows is None:
        return 0.0
    total_values = 0
    matched = 0
    for sys_info in systems:
        system = sys_info['system']
        row = None
        for r in csv_rows:
            if r.get('system', '').strip() == system:
                row = r
                break
        if row is None:
            continue
        # check bonds
        xyz_path = os.path.join('/app/outputs', sys_info['xyz_file'])
        if os.path.exists(xyz_path):
            with open(xyz_path) as f:
                xyz_text = f.read()
            coords = parse_xyz(xyz_text)
        else:
            coords = []
        for bond_info in sys_info['bonds']:
            i1, i2 = bond_info['xyz_indices']
            csv_col = bond_info['csv_col']
            if i1 < len(coords) and i2 < len(coords):
                d = dist(coords[i1], coords[i2])
                csv_val = row.get(csv_col)
                if csv_val is not None:
                    try:
                        csv_d = float(csv_val)
                        total_values += 1
                        if abs(d - csv_d) <= tight_bond_tol:
                            matched += 1
                    except:
                        pass
        # check frequencies
        freq_path = os.path.join('/app/outputs', sys_info['freq_file'])
        if os.path.exists(freq_path):
            with open(freq_path) as f:
                freq_text = f.read()
            freqs = parse_frequencies(freq_text)
        else:
            freqs = []
        freq_cols = sys_info['freq_csv_cols']
        for idx, col in enumerate(freq_cols):
            if idx < len(freqs):
                csv_val = row.get(col)
                if csv_val is not None:
                    try:
                        csv_f = float(csv_val)
                        total_values += 1
                        if abs(freqs[idx] - csv_f) <= tight_freq_tol:
                            matched += 1
                    except:
                        pass
    if total_values == 0:
        return 0.0
    return matched / total_values


_SCORERS = {
    'check_sin_geometry': score_0,
    'check_sin_freq': score_1,
    'check_sin2_geometry': score_2,
    'check_sin2_freq': score_3,
    'check_si2n_geometry': score_4,
    'check_si2n_freq': score_5,
    'check_consistency': score_6,
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
