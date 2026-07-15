import os
import json
import csv

# === author imports / helpers ===
import os
import math
import re

def parse_space_file(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            rows.append([float(p) for p in parts])
    return rows


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


# === block: score_0 (check id='step_03_total_dos') ===
def score_0(artifact, step, ctx):
    try:
        rows = parse_space_file(os.path.join('/app/outputs', 'total_dos.dat'))
        if len(rows) < 100:
            return 0.0
        for row in rows:
            if len(row) < 2:
                return 0.0
        return 1.0
    except:
        return 0.0


# === block: score_1 (check id='step_04_projected_dos') ===
def score_1(artifact, step, ctx):
    try:
        total_rows = parse_space_file(os.path.join('/app/outputs', 'total_dos.dat'))
        proj_rows = parse_space_file(os.path.join('/app/outputs', 'projected_dos.dat'))
        window = step.get('energy_window', [-0.05, 0.05])
        target_atoms = {1, 12, 14, 15, 16, 17, 18, 19}
        sum_total = 0.0
        sum_pdos = 0.0
        for er, td in total_rows:
            if window[0] <= er <= window[1]:
                sum_total += td
        for er, atom_idx, pd in proj_rows:
            if window[0] <= er <= window[1] and int(atom_idx) in target_atoms:
                sum_pdos += pd
        if sum_total == 0.0:
            return 0.0
        fraction = sum_pdos / sum_total
        deviation = abs(fraction - step['target_fraction'])
        tol = step.get('tolerance', 0.10)
        if deviation <= tol:
            return 1.0
        elif deviation <= 2 * tol:
            return 0.5
        else:
            return 0.0
    except:
        return 0.0


# === block: score_2 (check id='step_05_band_structure') ===
def score_2(artifact, step, ctx):
    try:
        rows = parse_space_file(os.path.join('/app/outputs', 'band_structure.dat'))
        if len(rows) < 100:
            return 0.0
        bands = {}
        for kdist, band_idx, energy in rows:
            bid = int(band_idx)
            if bid not in bands:
                bands[bid] = {'min': energy, 'max': energy}
            else:
                bands[bid]['min'] = min(bands[bid]['min'], energy)
                bands[bid]['max'] = max(bands[bid]['max'], energy)
        metallic = any(b['min'] <= 0 <= b['max'] for b in bands.values())
        return 1.0 if metallic else 0.0
    except:
        return 0.0


# === block: score_3 (check id='step_06_fermi_surface_sheets') ===
def score_3(artifact, step, ctx):
    import re
    if not isinstance(artifact, str):
        return 0.0
    match = re.search(r'\d+', artifact)
    if match:
        n = int(match.group())
        return 1.0 if n == step['target'] else 0.0
    return 0.0


_SCORERS = {
    'step_03_total_dos': score_0,
    'step_04_projected_dos': score_1,
    'step_05_band_structure': score_2,
    'step_06_fermi_surface_sheets': score_3,
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
