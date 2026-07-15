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


# === block: score_0 (check id='phonon_frequencies') ===
def score_0(artifact, step, ctx):
    target_peaks = step['target_peaks']
    tol_abs = step['tolerance_abs']
    tol_rel = step['tolerance_rel']
    sym_map = step.get('symmetry_map', {})
    sym_weight = step.get('symmetry_weight', 0.0)

    peak_matches = []
    sym_correct = []
    for peak in target_peaks:
        best = None
        best_diff = None
        for entry in artifact:
            pw = entry.get('peak_wavenumber')
            if pw is None:
                continue
            if abs(pw - peak) > 2.0:   # must be assigned to this experimental peak
                continue
            cf = entry.get('computed_frequency')
            if cf is None:
                continue
            diff = abs(cf - peak)
            rel_diff = diff / peak if peak != 0 else 0.0
            if diff <= tol_abs or rel_diff <= tol_rel:
                if best is None or diff < best_diff:
                    best = entry
                    best_diff = diff
        if best is not None:
            peak_matches.append(True)
            sym = best.get('symmetry_label')
            if str(peak) in sym_map:
                expected = sym_map[str(peak)]
                if sym and sym.upper() == expected.upper():
                    sym_correct.append(1)
                else:
                    sym_correct.append(0)
        else:
            peak_matches.append(False)
            if str(peak) in sym_map:
                sym_correct.append(0)

    freq_score = sum(peak_matches) / len(target_peaks) if target_peaks else 1.0
    sym_count = len(sym_map)
    if sym_count > 0:
        sym_score = sum(sym_correct) / sym_count
    else:
        sym_score = 1.0
    score = freq_score * (1 - sym_weight) + sym_score * sym_weight
    return score


# === block: score_1 (check id='gamma_300K') ===
def score_1(artifact, step, ctx):
    field = step['field']
    target = float(step['target'])
    tol = float(step['tolerance'])
    max_dev = float(step['max_deviation'])
    value = artifact.get(field)
    if value is None:
        return 0.0
    diff = abs(value - target)
    if diff <= tol:
        return 1.0
    score = max(0.0, 1.0 - (diff - tol) / (max_dev - tol))
    return score


# === block: score_2 (check id='kappa_L_300K') ===
def score_2(artifact, step, ctx):
    field = step['field']
    target = float(step['target'])
    tol = float(step['tolerance'])
    max_dev = float(step['max_deviation'])
    value = artifact.get(field)
    if value is None:
        return 0.0
    diff = abs(value - target)
    if diff <= tol:
        return 1.0
    score = max(0.0, 1.0 - (diff - tol) / (max_dev - tol))
    return score


_SCORERS = {
    'phonon_frequencies': score_0,
    'gamma_300K': score_1,
    'kappa_L_300K': score_2,
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
