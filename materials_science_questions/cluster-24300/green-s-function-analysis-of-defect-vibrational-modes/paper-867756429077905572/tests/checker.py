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
    import numpy as np
    g = 3.5
    theta = 1.2
    E0 = 2.0
    omega = 0.2
    N_cycles = 5
    Delta = 6.0
    q = 1.0
    m = 1.0
    tau = 2 * np.pi * N_cycles / omega
    dt = 0.01
    t_arr = np.arange(0, tau + dt, dt)
    Nt = len(t_arr)
    A_arr = -E0 / (2 * omega) * np.sin(omega * t_arr)
    sh = np.sinh(theta)
    ch = np.cosh(theta)
    D_arr = 1 - 1j * (q / 4) * (4 / g**2 + 1 + A_arr**2) * sh
    R_arr = -ch / D_arr
    D_neg_arr = 1 + 1j * (q / 4) * (4 / g**2 + 1 + A_arr**2) * sh
    R_neg_arr = -ch / D_neg_arr
    term1 = 4 / g - 1j * (4 / g**2 + 1 + A_arr**2) * sh
    num = 1j * (1 + (A_arr - 2j / g)**2) * sh * term1
    T_arr = num / D_arr
    vg = np.tanh(theta)
    x0 = 20.0
    L = 60.0
    dx_val = 0.2
    x = np.arange(0, L, dx_val)
    u_plus = np.array([np.exp(-theta / 2), np.exp(theta / 2)]) / np.sqrt(2)
    u_minus = np.array([np.exp(theta / 2), np.exp(-theta / 2)]) / np.sqrt(2)
    d_arr = np.zeros(Nt)
    dx_val = x[1] - x[0]  # use actual spacing for safety
    for idx in range(Nt):
        t = t_arr[idx]
        A = A_arr[idx]
        T = T_arr[idx]
        Rneg = R_neg_arr[idx]
        xc = x0 + vg * t
        G = np.exp(-(x - xc)**2 / (2 * Delta**2))
        laser = np.exp(1j * x * A)
        exp_ipx = np.exp(1j * sh * x)
        exp_minus_ipx = np.exp(-1j * sh * x)
        f1 = u_plus[:, None] * exp_ipx[None, :]
        f2 = u_minus[:, None] * exp_minus_ipx[None, :]
        phi = laser[None, :] * G[None, :] * T * (f1 + Rneg * f2)
        prob = np.sum(np.abs(phi)**2, axis=0)
        # manual trapezoidal integration (uniform grid, equally spaced)
        norm = (np.sum(prob[1:-1]) + 0.5 * (prob[0] + prob[-1])) * dx_val
        integrand = x * prob
        dipole = (np.sum(integrand[1:-1]) + 0.5 * (integrand[0] + integrand[-1])) * dx_val / norm
        d_arr[idx] = dipole
    d_centered = d_arr - np.mean(d_arr)
    amp = np.abs(np.fft.fft(d_centered))
    freqs = np.fft.fftfreq(Nt, d=dt)
    omega_multiples = np.arange(0, 21)
    intensity_vals = np.zeros(len(omega_multiples))
    for i, n in enumerate(omega_multiples):
        target = n * omega
        idx_f = np.argmin(np.abs(freqs - target))
        intensity_vals[i] = amp[idx_f] if idx_f < len(amp) else 0.0
    max_intensity = np.max(intensity_vals)
    if max_intensity > 0:
        intensity_vals /= max_intensity
    return {"ref_intensities": intensity_vals}


# === block: score_0 (check id='step_compute_spectrum') ===
def score_0(artifact, step, ctx):
    import numpy as np
    agent_omega = [float(row["omega_multiples"]) for row in artifact]
    agent_intensity = [float(row["intensity"]) for row in artifact]
    agent_dict = {om: intens for om, intens in zip(agent_omega, agent_intensity)}
    ref_intensities = ctx["ref_intensities"]
    even_harmonics = [2, 4, 6, 8, 10]
    max_agent = max(agent_intensity) if agent_intensity else 1e-12
    if max_agent == 0:
        max_agent = 1.0
    harmonic_scores = []
    for n in even_harmonics:
        I_ref = ref_intensities[n]
        if n in agent_dict:
            I_agent = agent_dict[n]
        else:
            I_agent = 0.0
        I_agent_norm = I_agent / max_agent
        if I_ref > 1e-8:
            rel_err = abs(I_agent_norm - I_ref) / I_ref
            harmonic_scores.append(max(0.0, 1.0 - rel_err / 0.2))
        else:
            harmonic_scores.append(1.0 if I_agent_norm < 0.01 else 0.0)
    harmonic_score = np.mean(harmonic_scores) * 0.75 if harmonic_scores else 0.0
    env_score = 0.0
    seq = [agent_dict.get(n, 0.0) for n in even_harmonics]
    if seq[0] > 0:
        norm_seq = [s/seq[0] for s in seq]
        if all(norm_seq[i] >= norm_seq[i+1] - 0.05 for i in range(len(norm_seq)-1)):
            env_score = 0.25
    total_score = harmonic_score + env_score
    return float(total_score)


_SCORERS = {
    'step_compute_spectrum': score_0,
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
