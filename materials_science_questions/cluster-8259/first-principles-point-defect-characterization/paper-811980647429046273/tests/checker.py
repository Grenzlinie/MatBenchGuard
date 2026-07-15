import os
import json
import csv

# === author imports / helpers ===
import os, csv, math


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
    spec = globals().get('spec', {})  # unused
    # Hidden gold parameters
    expected_times = [
        1.0, 1.584893192461114, 2.5118864315095794, 3.981071705534972, 6.309573444801933,
        10.0, 15.848931924611132, 25.118864315095794, 39.81071705534972, 63.095734448019336,
        100.0, 158.48931924611142, 251.18864315095804, 398.1071705534972, 630.9573444801934,
        1000.0, 1584.8931924611134, 2511.8864315095824, 3981.071705534972, 6309.573444801933,
        10000.0
    ]
    beta = 0.70
    tau = 760.0
    reference_fractions = [math.exp(-(t / tau) ** beta) for t in expected_times]
    return {
        'expected_times': expected_times,
        'reference_fractions': reference_fractions,
        'mae_tolerance_full': 0.05,
        'mae_max': 0.20
    }


# === block: score_0 (check id='step_01_mae') ===
def score_0(artifact, step, ctx):
    import numpy as np
    from scipy.integrate import solve_ivp

    def score(artifact, step, ctx):
        # --- hidden physical constants and parameters ---
        k = 8.617333262145e-5          # eV/K
        Ta = 500.0                     # K
        eps0 = 0.10                    # eV
        eps_w = 0.29                   # eV
        nu0 = 1.0e12                   # s-1
        b_plus_over_b0 = 0.01          # capture coefficient ratio
        factor = b_plus_over_b0 / 2    # = 0.005, per conservation +

        # localization radius and tail state concentration (must be public)
        a_cm = 1e-8                    # cm
        N_cm3 = 1e20                   # cm-3
        arg = (3 * eps0 / (k * Ta)) * (a_cm / 2) * (N_cm3 ** (1 / 3))
        eps_t = 3 * eps0 * np.log(arg) # transport energy (eV)

        nu_t = nu0 * np.exp(-3 * eps0 / (k * Ta))  # hopping frequency at eps_t
        mu = 0.0   # Gaussian center (midgap)

        # exact 20 time points required by the contract
        expected_times = np.array([
            1.0, 1.584893192461114, 2.5118864315095794, 3.981071705534972,
            6.309573444801933, 10.0, 15.848931924611132, 25.118864315095794,
            39.81071705534972, 63.095734448019336, 100.0, 158.48931924611142,
            251.18864315095804, 398.1071705534972, 630.9573444801934,
            1000.0, 1584.8931924611134, 2511.8864315095824,
            3981.071705534972, 6309.573444801933, 10000.0
        ])

        # --- ODE: df/dt = -2 * G(eps_d) * kTa / t * f / (f + factor*(1-f)) ---
        def dfdt(t, f):
            eps_d = eps_t + k * Ta * np.log(nu_t * t)
            G = np.exp(-(eps_d - mu) ** 2 / (2 * eps_w ** 2)) / (
                np.sqrt(2 * np.pi) * eps_w
            )
            denom = f + factor * (1 - f)
            if denom == 0:
                return 0.0
            return -2 * G * k * Ta / t * f / denom

        # integrate from a small starting time to 10000 s
        t_start = 1e-3
        f0 = 1.0
        sol = solve_ivp(
            dfdt,
            (t_start, 10000.0),
            [f0],
            method='LSODA',
            t_eval=expected_times,
            rtol=1e-9,
            atol=1e-12
        )
        if not sol.success:
            return 0.0
        reference_fractions = sol.y[0]

        # --- parse agent's artifact ---
        if not artifact or len(artifact) != 20:
            return 0.0

        agent_times = []
        agent_fracs = []
        try:
            for row in artifact:
                t = float(row.get('time_s', ''))
                f = float(row.get('fraction_remaining', ''))
                agent_times.append(t)
                agent_fracs.append(f)
        except (ValueError, TypeError):
            return 0.0

        if len(agent_times) != 20:
            return 0.0

        # check time points within tolerance
        for i in range(20):
            if abs(agent_times[i] - expected_times[i]) > 1e-6 * max(1.0, expected_times[i]):
                return 0.0

        # --- compute MAE and score ---
        errors = [abs(a - r) for a, r in zip(agent_fracs, reference_fractions)]
        mae = sum(errors) / len(errors)

        mae_tol = 0.05
        mae_max = 0.20
        if mae <= mae_tol:
            return 1.0
        if mae >= mae_max:
            return 0.0
        return max(0.0, 1.0 - (mae - mae_tol) / (mae_max - mae_tol))


_SCORERS = {
    'step_01_mae': score_0,
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
