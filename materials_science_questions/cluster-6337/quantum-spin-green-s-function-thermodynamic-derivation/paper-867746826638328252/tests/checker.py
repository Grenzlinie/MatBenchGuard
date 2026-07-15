import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    path = os.path.join(outputs_dir, 'sigma_Bx_results.csv')
    sigma_Bx_nuclear = None
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('R (nm)', '').strip() == '100':
                sigma_Bx_nuclear = float(row['sigma_Bx (T)'])
                break
    if sigma_Bx_nuclear is None:
        sigma_Bx_nuclear = 5.5e-8

    muN = 5.0507837461e-27
    g_star = 0.342
    I = 5/2
    C_sigma = g_star * muN * np.sqrt(I*(I+1))
    B_ext = 0.1
    hbar = 1.054571817e-34
    larmor_freq = g_star * muN * B_ext / (2*np.pi*hbar)

    ctx = {
        'sigma_Bx_nuclear': sigma_Bx_nuclear,
        'C_sigma': C_sigma,
        'larmor_freq': larmor_freq,
        'sigma_Bx_vac_target': 1.0e-6,
    }
    return ctx


# === block: score_0 (check id='sigma_Bx_results') ===
def score_0(artifact, step, ctx):
    import math
    rows = artifact
    if not rows:
        return 0.0

    tolerance = float(step.get('config', {}).get('tolerance', 0.01))

    R_targets = {'100': None, '50': None}
    for row in rows:
        r = row.get('R (nm)','').strip()
        if r in R_targets:
            R_targets[r] = row

    scores = []
    for r, row in R_targets.items():
        if row is None:
            scores.append(0.0)
            continue
        try:
            sum_Xi2 = float(row['sum_Xi2 (nm^-4)'])
            sigma_Bx_reported = float(row['sigma_Bx (T)'])
        except:
            scores.append(0.0)
            continue
        sigma_Bx_recomp = ctx['C_sigma'] * math.sqrt(sum_Xi2)
        rel_err = abs(sigma_Bx_reported - sigma_Bx_recomp) / (sigma_Bx_reported + 1e-30)
        if rel_err <= tolerance:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (rel_err - tolerance)/tolerance))
    return float(np.mean(scores))


# === block: score_1 (check id='nuclear_spectrum') ===
def score_1(artifact, step, ctx):
    rows = artifact
    freqs = np.array([float(r['frequency_Hz']) for r in rows])
    Sx = np.array([float(r['S_x (T/sqrt(Hz))']) for r in rows])
    Sx2 = Sx**2
    idx = np.argsort(freqs)
    freqs = freqs[idx]
    Sx2 = Sx2[idx]
    area = np.trapz(Sx2, freqs)

    sigma_Bx = ctx['sigma_Bx_nuclear']
    expected_var = sigma_Bx**2 / 3.0
    rel_err = abs(area - expected_var) / (expected_var + 1e-30)
    if rel_err <= 0.10:
        int_score = 1.0
    else:
        int_score = max(0.0, 1.0 - (rel_err - 0.10)/0.20)

    max_idx = np.argmax(Sx)
    peak_freq = freqs[max_idx]
    if 0.2e6 <= peak_freq <= 0.3e6:
        peak_score = 1.0
    else:
        peak_score = 0.0
    return 0.7*int_score + 0.3*peak_score


# === block: score_2 (check id='vacancy_spectrum') ===
def score_2(artifact, step, ctx):
    import os
    rows = artifact

    # Try to compute sigma_Bx_vac from the geometry tensors produced by step_04
    try:
        geom_path = os.path.join('/app/outputs', 'vacancy_geometry.npz')
        data = np.load(geom_path)
        if 'sum_Xi2' in data:
            sum_Xi2_vac = float(data['sum_Xi2'])
        else:
            Xi = data['Xi']  # shape (N,3,3) where Xi[i,a,b] corresponds to Xi_ab(i)
            Xi_x = Xi[:,0,:]  # a=x (index 0)
            sum_Xi2_vac = np.sum(Xi_x**2)
        # Use the same spin constants as the agent: quantum spin formula
        mu_B  = 9.274009994e-24      # J/T
        g_e   = 2.0
        S     = 1
        C_vac = g_e * mu_B * np.sqrt(S*(S+1))
        sigma_Bx_vac = C_vac * np.sqrt(sum_Xi2_vac)
    except Exception:
        # Geometry unavailable – cannot verify integral consistency
        sigma_Bx_vac = None

    freqs = np.array([float(r['frequency_Hz']) for r in rows])
    Sx   = np.array([float(r['S_x (T/sqrt(Hz))']) for r in rows])
    Sx2  = Sx**2
    idx  = np.argsort(freqs)
    freqs = freqs[idx]
    Sx   = Sx[idx]
    Sx2  = Sx2[idx]

    area = np.trapz(Sx2, freqs)

    if sigma_Bx_vac is not None:
        expected_var = sigma_Bx_vac**2 / 3.0
        rel_err = abs(area - expected_var) / (expected_var + 1e-30)
        if rel_err <= 0.10:
            int_score = 1.0
        else:
            int_score = max(0.0, 1.0 - (rel_err - 0.10)/0.20)
    else:
        int_score = 0.0

    max_Sx = np.max(Sx)
    local_max = []
    for i in range(1, len(Sx)-1):
        if Sx[i] > Sx[i-1] and Sx[i] > Sx[i+1]:
            local_max.append(Sx[i])
    count_peaks = sum(1 for val in local_max if val >= 0.2*max_Sx)
    peak_score = 1.0 if count_peaks >= 3 else 0.0

    return 0.7*int_score + 0.3*peak_score


_SCORERS = {
    'sigma_Bx_results': score_0,
    'nuclear_spectrum': score_1,
    'vacancy_spectrum': score_2,
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
