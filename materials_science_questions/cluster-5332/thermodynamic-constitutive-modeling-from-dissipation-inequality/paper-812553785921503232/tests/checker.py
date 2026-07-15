import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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


# === block: score_0 (check id='step1_scored') ===
def score_0(artifact, step, ctx):
    rows_by_case = {'zeta_b=0': [], 'zeta_b=0.2': []}
    for row in artifact:
        case = row.get('case', '')
        if case in rows_by_case:
            rows_by_case[case].append(row)
    rows_0 = rows_by_case['zeta_b=0']
    rows_02 = rows_by_case['zeta_b=0.2']
    if not rows_0 or not rows_02:
        return 0.0
    try:
        gap0 = np.array([float(r['opening_gap_mm']) for r in rows_0])
        trac0 = np.array([float(r['traction_MPa']) for r in rows_0])
        gap02 = np.array([float(r['opening_gap_mm']) for r in rows_02])
        trac02 = np.array([float(r['traction_MPa']) for r in rows_02])
    except (KeyError, ValueError):
        return 0.0

    score = 0.0

    # --- zeta_b=0 checks ---
    peak_idx0 = int(np.argmax(trac0))
    peak_val0 = trac0[peak_idx0]
    if abs(peak_val0 - 5.5) <= 0.1:
        score += 0.15

    # immediate softening after peak (next row must have lower traction)
    if peak_idx0 < len(trac0) - 1 and trac0[peak_idx0 + 1] < peak_val0:
        score += 0.2

    # --- zeta_b=0.2 checks ---
    peak_idx02 = int(np.argmax(trac02))
    peak_val02 = trac02[peak_idx02]
    if abs(peak_val02 - 5.5) <= 0.1:
        score += 0.15

    # Plateau: traction should be approximately constant near 5.5 MPa
    # over a gap range that at least extends to around 0.2 mm.
    plateau_mask = (trac02 >= 0.95 * peak_val02) & (trac02 <= 1.05 * peak_val02)
    if np.any(plateau_mask):
        plateau_gaps = gap02[plateau_mask]
        if np.max(plateau_gaps) >= 0.19:
            score += 0.2

        # identify post-plateau region starting after the last plateau point
        plateau_indices = np.where(plateau_mask)[0]
        last_plateau_idx = plateau_indices[-1]
        if last_plateau_idx < len(trac02) - 1:
            post_trac = trac02[last_plateau_idx + 1:]
            diffs = np.diff(post_trac)
            if len(diffs) > 0 and np.all(diffs <= 1e-6):
                score += 0.2
        # final drop to near zero at opening >= 1.1 mm (max residual opening)
        final_mask = gap02 >= 1.1
        if np.any(final_mask) and np.mean(trac02[final_mask]) < 0.1:
            score += 0.1

    return min(score, 1.0)


_SCORERS = {
    'step1_scored': score_0,
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
