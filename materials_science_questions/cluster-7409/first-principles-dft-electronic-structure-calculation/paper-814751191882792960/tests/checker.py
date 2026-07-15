import os
import json
import csv

# === author imports / helpers ===
import math
import csv
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
    csv_path = os.path.join(outputs_dir, "formation_energies_Fermi_level.csv")
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception:
        return {"transition_VBM": None, "band_gap": None}

    if not rows:
        return {"transition_VBM": None, "band_gap": None}

    required = {"Fermi_energy_eV", "Ef_H_minus_eV", "Ef_H_plus_eV"}
    if not required.issubset(rows[0].keys()):
        return {"transition_VBM": None, "band_gap": None}

    E, minus, plus = [], [], []
    for row in rows:
        try:
            e = float(row["Fermi_energy_eV"])
            m = float(row["Ef_H_minus_eV"])
            p = float(row["Ef_H_plus_eV"])
            E.append(e)
            minus.append(m)
            plus.append(p)
        except Exception:
            pass

    if len(E) < 2:
        return {"transition_VBM": None, "band_gap": None}

    combined = sorted(zip(E, minus, plus), key=lambda x: x[0])
    E_sorted = [c[0] for c in combined]
    minus_sorted = [c[1] for c in combined]
    plus_sorted = [c[2] for c in combined]

    crossing = None
    for i in range(len(E_sorted) - 1):
        d1 = minus_sorted[i] - plus_sorted[i]
        d2 = minus_sorted[i+1] - plus_sorted[i+1]
        if d1 * d2 <= 0:
            if abs(d1 - d2) < 1e-12:
                crossing = E_sorted[i]
            else:
                t = -d1 / (d2 - d1)
                crossing = E_sorted[i] + t * (E_sorted[i+1] - E_sorted[i])
            break

    if crossing is None:
        idx = None
        min_diff = float('inf')
        for i in range(len(E_sorted)):
            diff = abs(minus_sorted[i] - plus_sorted[i])
            if diff < min_diff:
                min_diff = diff
                idx = i
        if idx is not None:
            crossing = E_sorted[idx]

    band_gap = E_sorted[-1] - E_sorted[0] if E_sorted else None
    return {"transition_VBM": crossing, "band_gap": band_gap}


# === block: score_0 (check id='step_relaxed_geometries') ===
def score_0(artifact, step, ctx):
    target_values = step.get("target_values", {})
    tolerance_full = step.get("tolerance_full", 0.05)
    tolerance_partial = step.get("tolerance_partial", 0.2)
    scores = []
    for field_str, target in target_values.items():
        parts = field_str.split(".")
        obj = artifact
        for p in parts:
            obj = obj.get(p) if isinstance(obj, dict) else None
            if obj is None:
                break
        if obj is None or not isinstance(obj, (int, float)):
            scores.append(0.0)
            continue
        diff = abs(obj - target)
        if diff <= tolerance_full:
            scores.append(1.0)
        elif diff <= tolerance_partial:
            scores.append(max(0.0, 1.0 - (diff - tolerance_full) / (tolerance_partial - tolerance_full)))
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_transition_level_recompute') ===
def score_1(artifact, step, ctx):
    target = step.get("target_transition_VBM", 5.4)
    tol = step.get("tolerance_VBM", 0.3)
    transition = ctx.get("transition_VBM")
    if transition is None:
        return 0.0
    diff = abs(transition - target)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_2 (check id='step_charge_transition_levels_consistency') ===
def score_2(artifact, step, ctx):
    keys = step.get("expected_keys", ["transition_energy_above_VBM_eV", "transition_energy_below_CBM_eV"])
    above = artifact.get(keys[0]) if isinstance(artifact, dict) else None
    below = artifact.get(keys[1]) if isinstance(artifact, dict) else None
    if above is None or below is None:
        return 0.0
    transition_csv = ctx.get("transition_VBM")
    band_gap = ctx.get("band_gap")
    tol = step.get("tolerance_consistency", 0.3)
    score = 0.0
    if transition_csv is not None and abs(above - transition_csv) <= tol:
        score += 0.5
    if band_gap is not None and abs(above + below - band_gap) <= tol:
        score += 0.5
    return score


_SCORERS = {
    'step_relaxed_geometries': score_0,
    'step_transition_level_recompute': score_1,
    'step_charge_transition_levels_consistency': score_2,
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
