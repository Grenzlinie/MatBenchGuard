import os
import json
import csv

# === author imports / helpers ===
import os, math

def find_peaks_from_spectrum(data, energy_col='energy_eV', val_col='e2_imag', range_min=0.0, range_max=6.0):
    points = []
    for row in data:
        try:
            e = float(row[energy_col])
            v = float(row[val_col])
        except (ValueError, KeyError):
            continue
        if range_min <= e <= range_max:
            points.append((e, v))
    if not points:
        return []
    points.sort(key=lambda x: x[0])
    energies = [p[0] for p in points]
    values = [p[1] for p in points]
    peaks = []
    n = len(values)
    if n < 3:
        return []
    for i in range(1, n-1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peaks.append(energies[i])
    return peaks

def match_peaks_score(computed_peaks, gold_peaks, tol):
    gold_sorted = sorted(gold_peaks)
    comp_sorted = sorted(computed_peaks)
    matched = 0
    used = set()
    for g in gold_sorted:
        best_dist = tol + 1e-6
        best_idx = -1
        for i, c in enumerate(comp_sorted):
            if i in used:
                continue
            dist = abs(c - g)
            if dist < best_dist:
                best_dist = dist
                best_idx = i
        if best_idx >= 0 and best_dist <= tol:
            matched += 1
            used.add(best_idx)
    return matched / len(gold_sorted) if gold_sorted else 0.0


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
    return {'output_dir': outputs_dir}


# === block: score_0 (check id='cr_peaks') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold_peaks', [])
    tol = step.get('tolerance', 0.2)
    evidence_file = step.get('evidence_file', 'e2_spectrum_cr.csv')
    output_dir = ctx.get('output_dir', '/app/outputs')
    evidence_path = os.path.join(output_dir, evidence_file)
    spectrum = None
    if os.path.exists(evidence_path):
        spectrum = load_artifact(evidence_path)
    peaks = []
    if spectrum and isinstance(spectrum, list) and spectrum:
        peaks = find_peaks_from_spectrum(spectrum)
        if not peaks:
            peaks = []
    else:
        # fallback to submitted artifact
        if artifact and isinstance(artifact, list):
            peaks = [float(row['energy_eV']) for row in artifact if 'energy_eV' in row]
    score = match_peaks_score(peaks, gold, tol)
    return score


# === block: score_1 (check id='fe_peaks') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold_peaks', [])
    tol = step.get('tolerance', 0.2)
    evidence_file = step.get('evidence_file', 'e2_spectrum_fe.csv')
    output_dir = ctx.get('output_dir', '/app/outputs')
    evidence_path = os.path.join(output_dir, evidence_file)
    spectrum = None
    if os.path.exists(evidence_path):
        spectrum = load_artifact(evidence_path)
    peaks = []
    if spectrum and isinstance(spectrum, list) and spectrum:
        peaks = find_peaks_from_spectrum(spectrum)
        if not peaks:
            peaks = []
    else:
        if artifact and isinstance(artifact, list):
            peaks = [float(row['energy_eV']) for row in artifact if 'energy_eV' in row]
    score = match_peaks_score(peaks, gold, tol)
    return score


_SCORERS = {
    'cr_peaks': score_0,
    'fe_peaks': score_1,
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
