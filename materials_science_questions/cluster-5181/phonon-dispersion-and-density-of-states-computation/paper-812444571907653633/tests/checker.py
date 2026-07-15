import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    import json
    import numpy as np

    # Load the original spec for other gold values
    with open('/tests/grading_spec.json', 'r') as f:
        spec = json.load(f)
    gold = spec.get('gold', {})

    # Replace phonon gold with the paper's calculated values from Tableau 1 "Résultats du calcul"
    # Tolerances: elastic constants ±5%, phonon frequencies ±2%
    gold['phonon'] = {
        "C11": {"value": 10.45, "tolerance_rel": 0.05},
        "C12": {"value": 5.76, "tolerance_rel": 0.05},
        "C44": {"value": 4.611, "tolerance_rel": 0.05},
        "ω_LO(Γ)": {"value": 10.36, "tolerance_rel": 0.02},
        "ω_TO(Γ)": {"value": 9.130, "tolerance_rel": 0.02},
        "ω_LA(X)": {"value": 5.500, "tolerance_rel": 0.02},
        "ω_LO(X)": {"value": 9.59, "tolerance_rel": 0.02},
        "ω_TA(X)": {"value": 2.058, "tolerance_rel": 0.02},
        "ω_TO(X)": {"value": 10.17, "tolerance_rel": 0.02},
        "ω_LO(L)": {"value": 10.45, "tolerance_rel": 0.02},
        "ω_LA(L)": {"value": 5.049, "tolerance_rel": 0.02},
        "ω_TA(L)": {"value": 1.648, "tolerance_rel": 0.02},
        "ω_TO(L)": {"value": 9.513, "tolerance_rel": 0.02}
    }

    return gold


# === block: score_0 (check id='phonon_qty') ===
def score_0(artifact, step, ctx):
    golds = ctx['phonon']
    total = 0
    count = len(golds)
    for qty, ginfo in golds.items():
        val = None
        for row in artifact:
            if row.get('quantity') == qty:
                try:
                    val = float(row['computed_value'])
                except (ValueError, TypeError):
                    pass
                break
        if val is None:
            continue
        ref = ginfo['value']
        if ref == 0:
            continue
        rel_err = abs(val - ref) / abs(ref)
        tol = ginfo.get('tolerance_rel', 0.05)
        if rel_err <= tol:
            score = 1.0
        else:
            score = max(0.0, 1.0 - (rel_err - tol) / (2 * tol))
        total += score
    return total / count if count > 0 else 0.0


# === block: score_1 (check id='gplus_peaks') ===
def score_1(artifact, step, ctx):
    golds = ctx['gplus_peaks']
    num_peaks = golds.get('num_peaks', 10)
    gold_positions = golds.get('peak_positions_cm1', [])
    tolerance = golds.get('tolerance_cm1', 5.0)
    omega = artifact['omega_cm1']
    gplus = artifact['gplus']
    g = np.array(gplus)
    peaks = []
    for i in range(1, len(g)-1):
        if g[i] > g[i-1] and g[i] > g[i+1]:
            peaks.append(omega[i])
    peaks_sorted = sorted(peaks, key=lambda p: np.interp(p, omega, gplus), reverse=True)
    selected = []
    for p in peaks_sorted:
        if len(selected) >= num_peaks:
            break
        if all(abs(p - sp) > 1.0 for sp in selected):
            selected.append(p)
    matched = sum(1 for gp in gold_positions if any(abs(p - gp) <= tolerance for p in selected))
    return matched / len(gold_positions) if gold_positions else 0.0


# === block: score_2 (check id='impurity_modes') ===
def score_2(artifact, step, ctx):
    golds = ctx['impurity']
    score = 0.0
    local = artifact.get('local_mode_cm1')
    if isinstance(local, (int, float)):
        ref = golds['local_mode_cm1']['value']
        tol = golds['local_mode_cm1'].get('tolerance_rel', 0.01)
        if ref != 0:
            rel_err = abs(local - ref) / abs(ref)
            score = 1.0 if rel_err <= tol else max(0.0, 1.0 - (rel_err - tol) / (2 * tol))
        else:
            score = 1.0 if local == 0 else 0.0
    else:
        score = 0.0
    gap = artifact.get('gap_mode_cm1')
    if isinstance(gap, (int, float)) and 'gap_mode_cm1' in golds:
        ref = golds['gap_mode_cm1']['value']
        tol = golds['gap_mode_cm1'].get('tolerance_rel', 0.05)
        if ref != 0:
            rel_err = abs(gap - ref) / abs(ref)
            gap_score = 1.0 if rel_err <= tol else max(0.0, 1.0 - (rel_err - tol) / (2 * tol))
        else:
            gap_score = 1.0 if gap == 0 else 0.0
        score = (score + gap_score) / 2.0
    return score


_SCORERS = {
    'phonon_qty': score_0,
    'gplus_peaks': score_1,
    'impurity_modes': score_2,
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
