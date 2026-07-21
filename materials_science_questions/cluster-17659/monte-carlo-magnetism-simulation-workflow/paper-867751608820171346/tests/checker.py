import os
import json
import csv

# === author imports / helpers ===
import subprocess
import sys
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "numpy"])
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
    return {}


# === block: score_0 (check id='canonical_caloric_check') ===
def score_0(artifact, step, ctx):
    temperatures = np.array([float(r['temperature']) for r in artifact])
    energies = np.array([float(r['avg_potential_energy']) for r in artifact])
    if len(temperatures) < 4:
        return 0.0
    idx = np.argsort(temperatures)
    t = temperatures[idx]
    e = energies[idx]
    diff_e = np.diff(e)
    diff_t = np.diff(t)
    deriv = np.divide(diff_e, diff_t, out=np.full_like(diff_e, np.nan), where=diff_t!=0)
    if np.all(np.isnan(deriv)):
        return 0.0
    max_idx = np.nanargmax(np.abs(deriv))
    t_peak = 0.5 * (t[max_idx] + t[max_idx+1])
    score_peak = 1.0 if abs(t_peak - 15.5) <= 1.0 else (0.5 if abs(t_peak - 15.5) <= 2.0 else 0.0)
    phi_low = e[0]
    score_phi = 1.0 if phi_low <= -55.0 else (0.5 if phi_low <= -50.0 else 0.0)
    return 0.5 * score_peak + 0.5 * score_phi


# === block: score_1 (check id='microcanonical_caloric_check') ===
def score_1(artifact, step, ctx):
    energies = np.array([float(r['total_energy']) for r in artifact])
    temps = np.array([float(r['temperature']) for r in artifact])
    if len(energies) < 4:
        return 0.0
    idx = np.argsort(energies)
    E = energies[idx]
    T = temps[idx]
    dT = np.diff(T)
    dE = np.diff(E)
    deriv = np.divide(dT, dE, out=np.full_like(dT, np.nan), where=dE!=0)
    neg_mask = deriv < 0
    if not np.any(neg_mask):
        return 0.0
    neg_indices = np.where(neg_mask)[0]
    E_left = E[neg_indices[0]]
    E_right = E[neg_indices[-1] + 1]
    score_left = 1.0 if abs(E_left + 25.65) <= 3.0 else (0.5 if abs(E_left + 25.65) <= 5.0 else 0.0)
    score_right = 1.0 if abs(E_right - 15.24) <= 3.0 else (0.5 if abs(E_right - 15.24) <= 5.0 else 0.0)
    return 0.5 * score_left + 0.5 * score_right


# === block: score_2 (check id='trace_check') ===
def score_2(artifact, step, ctx):
    n_rows = len(artifact)
    if n_rows < 1_000_000:
        return 0.0
    phi = np.array([float(r['potential_energy']) for r in artifact])
    min_phi, max_phi = np.min(phi), np.max(phi)
    if max_phi - min_phi < 10:
        return 0.0
    bins = np.arange(np.floor(min_phi), np.ceil(max_phi)+1, 1.0)
    hist, _ = np.histogram(phi, bins=bins)
    if len(hist) < 3:
        return 0.0
    # simplified peak detection
    peaks = []
    for i in range(1, len(hist)-1):
        if hist[i] > hist[i-1] and hist[i] > hist[i+1]:
            peaks.append((hist[i], bins[i]))
    if len(peaks) < 2:
        return 0.0
    peaks_sorted = sorted(peaks, key=lambda x: x[0], reverse=True)
    peak1, peak2 = peaks_sorted[0], peaks_sorted[1]
    sep = abs(peak1[1] - peak2[1])
    total = np.sum(hist)
    mass1 = peak1[0] / total
    mass2 = peak2[0] / total
    if sep > 5 and mass1 > 0.05 and mass2 > 0.05:
        return 1.0
    return 0.0


_SCORERS = {
    'canonical_caloric_check': score_0,
    'microcanonical_caloric_check': score_1,
    'trace_check': score_2,
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
