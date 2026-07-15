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
    # Build fcc neighbor list up to 20 shells and compute reference dispersion curves
    def _fcc_neighbors(n_shells=20):
        basis = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]) * 0.5
        rmax = np.sqrt(n_shells * 2)
        shells = []
        for i in range(-n_shells, n_shells + 1):
            for j in range(-n_shells, n_shells + 1):
                for k in range(-n_shells, n_shells + 1):
                    for b in basis:
                        R = np.array([i + b[0], j + b[1], k + b[2]])
                        dist = np.sqrt(np.dot(R, R))
                        if dist > 0 and dist < rmax:
                            shells.append(R)
        shells.sort(key=lambda x: np.dot(x, x))
        return shells

    def _lattice_sums(shells, q, n, alpha=None, beta=None):
        result = 0 + 0j
        for R in shells:
            rho = np.linalg.norm(R)
            phase = np.exp(2j * np.pi * np.dot(q, R))
            if alpha is None:
                result += phase / (rho ** n)
            else:
                result += (R[alpha] * R[beta] * phase) / (rho ** n)
        return result

    def _dynamical_matrix(q, sigma_over_a):
        a = 1.0 / sigma_over_a
        prefactor = 24.0 / (a ** 2) * (1.0 / a) ** 8
        s16_ab = np.zeros((3, 3), dtype=complex)
        s10_ab = np.zeros((3, 3), dtype=complex)
        for alpha in range(3):
            for beta in range(3):
                s16_ab[alpha, beta] = _lattice_sums(shells, q, 16, alpha, beta)
                s10_ab[alpha, beta] = _lattice_sums(shells, q, 10, alpha, beta)
        s14_q = _lattice_sums(shells, q, 14)
        s8_q = _lattice_sums(shells, q, 8)
        s14_0 = _lattice_sums(shells, np.zeros(3), 14)
        s8_0 = _lattice_sums(shells, np.zeros(3), 8)
        term = -28 * (1 / a) ** 6 * s16_ab + 8 * s10_ab
        diag_term = (22 / 3) * (1 / a) ** 6 * s14_0 - (5 / 3) * s8_0 + 2 * (1 / a) ** 6 * s14_q - s8_q
        D = prefactor * (term + np.diag([diag_term] * 3))
        return np.real_if_close(D)

    def _compute_dispersion(sigma_over_a, q_points=np.linspace(0, 1, 101)):
        freqs = []
        for q in q_points:
            qvec = np.array([q, 0.0, 0.0])
            D = _dynamical_matrix(qvec, sigma_over_a)
            w2 = np.linalg.eigvalsh(D)
            w = np.sqrt(np.abs(w2))
            w_sorted = np.sort(w)
            omega_L = w_sorted[2]
            omega_T = w_sorted[1]
            freqs.append((omega_L, omega_T))
        return np.array(freqs)

    shells = _fcc_neighbors(n_shells=20)
    ref_disp_130 = _compute_dispersion(1.30)
    ref_disp_124 = _compute_dispersion(1.24)
    ctx = {
        'ref_130': ref_disp_130,
        'ref_124': ref_disp_124,
        'q_eval': np.arange(0, 1.01, 0.1)
    }
    return ctx


# === block: score_0 (check id='step_02_dispersion_1.30') ===
def score_0(artifact, step, ctx):
    import numpy as np
    q_agent = np.array([float(row['q']) for row in artifact])
    omegaL_agent = np.array([float(row['omega_L']) for row in artifact])
    omegaT_agent = np.array([float(row['omega_T']) for row in artifact])
    sort_idx = np.argsort(q_agent)
    q_agent = q_agent[sort_idx]
    omegaL_agent = omegaL_agent[sort_idx]
    omegaT_agent = omegaT_agent[sort_idx]
    ref = ctx['ref_130']
    q_eval = ctx['q_eval']
    tol = step.get('tolerance_relative', 0.05)
    total_points = len(q_eval)
    passed = 0
    for qi in q_eval:
        omegaL_interp = np.interp(qi, q_agent, omegaL_agent)
        omegaT_interp = np.interp(qi, q_agent, omegaT_agent)
        idx = np.argmin(np.abs(np.linspace(0, 1, ref.shape[0]) - qi))
        refL, refT = ref[idx]
        if refL > 0 and abs(omegaL_interp - refL) <= tol * refL:
            passed += 1
        if refT > 0 and abs(omegaT_interp - refT) <= tol * refT:
            passed += 1
    max_possible = total_points * 2
    score = passed / max_possible if max_possible > 0 else 0.0
    return score


# === block: score_1 (check id='step_03_dispersion_1.24') ===
def score_1(artifact, step, ctx):
    import numpy as np
    q_agent = np.array([float(row['q']) for row in artifact])
    omegaL_agent = np.array([float(row['omega_L']) for row in artifact])
    omegaT_agent = np.array([float(row['omega_T']) for row in artifact])
    sort_idx = np.argsort(q_agent)
    q_agent = q_agent[sort_idx]
    omegaL_agent = omegaL_agent[sort_idx]
    omegaT_agent = omegaT_agent[sort_idx]
    ref = ctx['ref_124']
    q_eval = ctx['q_eval']
    tol = step.get('tolerance_relative', 0.05)
    total_points = len(q_eval)
    passed = 0
    for qi in q_eval:
        omegaL_interp = np.interp(qi, q_agent, omegaL_agent)
        omegaT_interp = np.interp(qi, q_agent, omegaT_agent)
        idx = np.argmin(np.abs(np.linspace(0, 1, ref.shape[0]) - qi))
        refL, refT = ref[idx]
        if refL > 0 and abs(omegaL_interp - refL) <= tol * refL:
            passed += 1
        if refT > 0 and abs(omegaT_interp - refT) <= tol * refT:
            passed += 1
    max_possible = total_points * 2
    score = passed / max_possible if max_possible > 0 else 0.0
    return score


# === block: score_2 (check id='step_04_dos_1.30') ===
def score_2(artifact, step, ctx):
    import numpy as np
    bins = []
    for row in artifact:
        bs = float(row['bin_start'])
        be = float(row['bin_end'])
        cnt = int(row['count'])
        bins.append((bs, be, cnt))
    if len(bins) < 2:
        return 0.0
    bins.sort(key=lambda x: x[0])
    centers = [(b[0] + b[1]) / 2.0 for b in bins]
    counts = [b[2] for b in bins]
    peaks = []
    for i in range(len(counts)):
        if i == 0:
            if len(counts) > 1 and counts[i] > 0 and counts[i] > counts[i + 1]:
                peaks.append((centers[i], counts[i]))
        elif i == len(counts) - 1:
            if counts[i] > 0 and counts[i] > counts[i - 1]:
                peaks.append((centers[i], counts[i]))
        else:
            if counts[i] > 0 and counts[i] > counts[i - 1] and counts[i] > counts[i + 1]:
                peaks.append((centers[i], counts[i]))
    if len(peaks) < 2:
        return 0.0
    peaks_sorted = sorted(peaks, key=lambda x: x[1], reverse=True)
    peak1, peak2 = peaks_sorted[0], peaks_sorted[1]
    if peak1[0] > peak2[0]:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_02_dispersion_1.30': score_0,
    'step_03_dispersion_1.24': score_1,
    'step_04_dos_1.30': score_2,
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
