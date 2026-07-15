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
    x_vals = np.array([0.0, 0.1, 0.3, 0.5, 0.9, 1.0])
    ref_shifted_gap = 1.8367 + 0.2732 * np.exp(-6.2 * x_vals)
    ref_map = {str(x): ref_shifted_gap[i] for i, x in enumerate(x_vals)}
    return {'outputs_dir': outputs_dir, 'ref_shifted_gaps': ref_map}


# === block: score_0 (check id='band_gaps') ===
def score_0(artifact, step, ctx):
    rows = artifact
    data = []
    for row in rows:
        x = float(row['x'])
        gap = float(row['band_gap_unshifted'])
        data.append((x, gap))
    data.sort(key=lambda t: t[0])
    x_vals_agent = np.array([d[0] for d in data])
    gaps = np.array([d[1] for d in data])
    shifted = gaps + 0.2
    ref_gaps = np.array([ctx['ref_shifted_gaps'][str(x)] for x in x_vals_agent])
    deviation = np.abs(shifted - ref_gaps)
    tol = 0.2
    tol_score = np.mean(np.where(deviation <= tol, 1.0, 0.0))
    monotonic_ok = np.all(np.diff(gaps) < 0)
    mono_score = 1.0 if monotonic_ok else 0.0
    return 0.8 * tol_score + 0.2 * mono_score


# === block: score_1 (check id='epsilon2') ===
def score_1(artifact, step, ctx):
    import os
    import numpy as np
    from scipy.interpolate import interp1d

    # Load hidden reference curve (bundled with the checker)
    ref_path = os.path.join(os.path.dirname(__file__), 'ref_epsilon2.csv')
    try:
        ref_data = np.loadtxt(ref_path, delimiter=',', skiprows=1)
        ref_energy = ref_data[:, 0]
        ref_eps2 = ref_data[:, 1]
    except Exception:
        # Fallback to structural checks if reference is absent (should not happen in a valid task)
        rows = artifact
        energy = np.array([float(r['energy']) for r in rows])
        eps2 = np.array([float(r['epsilon2']) for r in rows])
        if len(energy) < 200 or np.any(eps2 < 0):
            return 0.0
        from scipy.signal import argrelextrema
        max_idx = argrelextrema(eps2, np.greater)[0]
        if len(max_idx) < 2 or np.max(eps2[max_idx]) < 0.5:
            return 0.0
        low_peak = np.any((energy[max_idx] >= 2) & (energy[max_idx] <= 4))
        mid_peak = np.any((energy[max_idx] >= 4) & (energy[max_idx] <= 8))
        return 0.4 if low_peak and mid_peak else 0.2
    else:
        rows = artifact
        energy = np.array([float(r['energy']) for r in rows])
        eps2 = np.array([float(r['epsilon2']) for r in rows])
        if len(energy) < 200 or np.any(eps2 < 0):
            return 0.0
        # Interpolate agent's epsilon2 onto the reference energy grid
        f = interp1d(energy, eps2, kind='linear', bounds_error=False, fill_value=0.0)
        agent_interp = f(ref_energy)
        # Pearson correlation
        corr = np.corrcoef(agent_interp, ref_eps2)[0, 1]
        if np.isnan(corr):
            corr = 0.0
        # Normalised mean absolute error
        ref_range = np.max(ref_eps2) - np.min(ref_eps2)
        if ref_range == 0:
            ref_range = 1.0
        mae = np.mean(np.abs(agent_interp - ref_eps2)) / ref_range
        # Combine correlation and MAE into a final score
        score = 0.5 * max(0.0, corr) + 0.5 * np.exp(-mae * 3.0)
        return float(score)


# === block: score_2 (check id='epsilon1') ===
def score_2(artifact, step, ctx):
    # Hard‑coded hidden reference ε₁ digitised from the paper's Figure 4 for SbI₃ (x=1.0).
    # (Replace the arrays below with the actual digitised data when available.)
    import numpy as np
    from scipy.interpolate import interp1d

    ref_energy_eps1 = np.array([
        0.0, 0.2, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
        5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0
    ])
    ref_eps1 = np.array([
        6.1, 6.1, 6.2, 6.4, 6.8, 7.2, 7.5, 5.3, 1.2, -1.8, -1.5,
        0.8, 2.5, 3.8, 4.5, 4.9, 5.1, 5.2, 5.3, 5.3, 5.3, 5.3
    ])

    rows = artifact
    energy = np.array([float(r['energy']) for r in rows])
    eps1_agent = np.array([float(r['epsilon1']) for r in rows])

    # Basic structural filter
    if len(energy) < 200 or np.any(eps1_agent < 0):
        return 0.0

    try:
        # Interpolate agent's ε₁ onto the reference energy grid
        f = interp1d(energy, eps1_agent, kind='linear', bounds_error=False, fill_value=0.0)
        agent_interp = f(ref_energy_eps1)
    except Exception:
        return 0.0

    # Pearson correlation
    corr = np.corrcoef(agent_interp, ref_eps1)[0, 1]
    if np.isnan(corr):
        corr = 0.0

    # Normalised mean absolute error
    ref_range = np.max(ref_eps1) - np.min(ref_eps1)
    if ref_range == 0:
        ref_range = 1.0
    mae = np.mean(np.abs(agent_interp - ref_eps1)) / ref_range

    # Combined score (correlation + MAE penalty)
    score = 0.6 * max(0.0, corr) + 0.4 * np.exp(-mae * 3.0)

    return float(score)


_SCORERS = {
    'band_gaps': score_0,
    'epsilon2': score_1,
    'epsilon1': score_2,
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
