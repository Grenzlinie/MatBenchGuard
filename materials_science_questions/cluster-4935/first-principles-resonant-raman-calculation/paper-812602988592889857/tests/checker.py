import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.interpolate import interp1d


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
        # physical parameters
        N = 50
        omega_ex_over_gamma = 5.0
        Omega_L_tau_s = 20.0
        tau_s = Omega_L_tau_s       # dimensionless, Ω_L=1
        omega_ex2 = omega_ex_over_gamma**2
        s = 2.5
        Iz2 = N / 2.0 * (s * (s + 1) - s**2)
        Ix_avg = N * s
        mu_minus = (omega_ex2 / 2.0) * (Iz2 + Ix_avg / 2.0)
        mu2 = mu_minus   # μ_+ = 0 at T=0

        # time grid for correlation
        dt = 0.01
        Tmax = 200.0
        tau = np.arange(-Tmax, Tmax + dt/2, dt)
        abs_tau = np.abs(tau)
        corr = mu_minus * np.exp(1j * tau - abs_tau / tau_s)

        # k integration (0 to ∞, effectively limited by Gaussian)
        kmax = 5.0 / np.sqrt(mu2)
        nk = 200
        k = np.linspace(0, kmax, nk)
        dk = k[1] - k[0]
        Kg, _ = np.meshgrid(k, tau, indexing='ij')
        k2 = Kg**2
        exp_factor = np.exp(-2*Kg - mu2 * k2)
        sinh_arg = k2 * corr[np.newaxis, :]
        integrand = exp_factor * np.sinh(sinh_arg)
        if hasattr(np, 'trapezoid'):
            f_arr = np.trapezoid(integrand, k, axis=0)
        else:
            f_arr = np.trapz(integrand, k, axis=0)

        # Fourier transform → S_xy(Ω)
        N_t = len(tau)
        f_shift = np.fft.ifftshift(f_arr)
        G = np.fft.fft(f_shift) * dt
        freq_fft = np.fft.fftfreq(N_t, d=dt) * 2 * np.pi

        # symmetrize → S_FR(Ω) = (S_xy(Ω) + S_xy(-Ω))/2
        S_xy = np.real(G)
        S_FR = 0.5 * (S_xy + S_xy[::-1])
        freq = freq_fft

        # keep only [-10, 0] Ω_L
        mask = (freq >= -10.0) & (freq <= 0.0)
        gold_freq = freq[mask]
        gold_intensity = S_FR[mask]
        order = np.argsort(gold_freq)
        gold_freq = gold_freq[order]
        gold_intensity = gold_intensity[order]

        return {
            "gold_freq": gold_freq,
            "gold_intensity": gold_intensity,
            "params": {
                "N": N,
                "omega_ex_over_gamma": omega_ex_over_gamma,
                "Omega_L_tau_s": Omega_L_tau_s,
                "temperature": 0
            }
        }


# === block: score_0 (check id='spectrum') ===
def score_0(artifact, step, ctx):
        # load agent CSV columns
        agent_freq = np.array([float(row['frequency']) for row in artifact])
        agent_intensity = np.array([float(row['intensity']) for row in artifact])
        if len(agent_freq) == 0:
            return 0.0

        gold_freq = ctx['gold_freq']
        gold_intensity = ctx['gold_intensity']

        # interpolate agent onto gold grid
        try:
            interp = interp1d(agent_freq, agent_intensity, kind='linear',
                              bounds_error=False, fill_value=0.0)
            agent_interp = interp(gold_freq)
        except Exception:
            return 0.0

        # MAPE score
        eps = 1e-10
        mask = (gold_intensity > 1e-8) & (agent_interp >= 0.0)
        if mask.sum() == 0:
            return 0.0
        mape = np.mean(np.abs(agent_interp[mask] - gold_intensity[mask]) / (gold_intensity[mask] + eps))
        mape_score = 0.0
        if mape <= 0.05:
            mape_score = 1.0
        elif mape <= 0.20:
            mape_score = (0.20 - mape) / (0.20 - 0.05)
        else:
            mape_score = 0.0

        # structural: no even-harmonic peak > 5% of max
        max_int = np.max(np.clip(agent_intensity, 0, None))
        if max_int == 0:
            structural_score = 0.0
        else:
            threshold = 0.05 * max_int
            # simple peak finding
            peaks = []
            n = len(agent_freq)
            for i in range(1, n-1):
                if (agent_intensity[i] > agent_intensity[i-1] and
                    agent_intensity[i] > agent_intensity[i+1] and
                    agent_intensity[i] >= threshold):
                    peaks.append(agent_freq[i])
            # check each peak is within 0.1 of an odd integer
            odd_ok = True
            for pk in peaks:
                nearest_odd = round(pk / 2) * 2 + 1   # odd multiple of Ω_L
                if abs(pk - nearest_odd) > 0.1:
                    # allow tolerance: it must be within 0.1 of an odd integer
                    # but also check if it's an even multiple
                    nearest_even = round(pk / 2) * 2
                    if abs(pk - nearest_even) <= 0.1:
                        odd_ok = False
                        break
            structural_score = 1.0 if odd_ok else 0.0

        # combined score
        score = 0.8 * mape_score + 0.2 * structural_score
        return max(0.0, min(1.0, score))


_SCORERS = {
    'spectrum': score_0,
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
