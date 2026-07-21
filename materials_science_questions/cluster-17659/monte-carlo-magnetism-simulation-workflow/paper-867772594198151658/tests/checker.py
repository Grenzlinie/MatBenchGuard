import os
import json
import csv

# === author imports / helpers ===
import csv, math, json, sys


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
    def solve_equilibrium(T):
        beta = 1.0 / T
        k = 3
        J = 1.0
        h = 2.0 if T < 3.0 else 0.5
        for _ in range(200):
            arg = min(1.0 - 1e-15, max(-1.0 + 1e-15, math.tanh(beta) * math.tanh(beta * h)))
            new_h = (k - 1) / beta * math.atanh(arg)
            if abs(new_h - h) < 1e-13:
                break
            h = new_h
        tanh_beta = math.tanh(beta)
        tanh_beta_h = math.tanh(beta * h)
        denom = 1.0 + tanh_beta * (tanh_beta_h ** 2)
        E = - (k / 2.0) * (tanh_beta + tanh_beta_h ** 2) / denom
        m = math.tanh(k * math.atanh(min(1.0 - 1e-15, max(-1.0 + 1e-15, tanh_beta * tanh_beta_h))))
        return E, m

    theoretical = {}
    for T in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        E, m = solve_equilibrium(T)
        theoretical[T] = (E, m)
    return {"theoretical": theoretical}


# === block: score_0 (check id='dense_recurrence') ===
def score_0(artifact, step, ctx):
    by_beta = {}
    for row in artifact:
        b = float(row['beta'])
        t = int(row['time_step'])
        m_sig = float(row['m_sigma'])
        m_tau = float(row['m_tau'])
        if b not in by_beta:
            by_beta[b] = {}
        by_beta[b][t] = (m_sig, m_tau)

    errors = []
    m_tau_vals = []
    for b, times in by_beta.items():
        sorted_t = sorted(times.keys())
        for idx, t in enumerate(sorted_t):
            if t < 20 or (t + 1) not in times:
                continue
            m_sig_t, m_tau_t = times[t]
            m_sig_next, _ = times[t + 1]
            pred = math.tanh(b * (m_sig_t + m_tau_t))
            errors.append(abs(m_sig_next - pred))
            m_tau_vals.append(abs(m_tau_t))

    avg_error = sum(errors) / len(errors) if errors else 0.0
    avg_mtau = sum(m_tau_vals) / len(m_tau_vals) if m_tau_vals else 0.0

    tol_rec = float(step.get('tolerance', 0.1))
    score_rec = 1.0 if avg_error <= tol_rec else max(0.0, 1.0 - (avg_error - tol_rec) / 0.4)
    tol_mtau = 0.05
    score_mtau = 1.0 if avg_mtau <= tol_mtau else max(0.0, 1.0 - (avg_mtau - tol_mtau) / 0.15)
    return (score_rec + score_mtau) / 2.0


# === block: score_1 (check id='sparse_equilibrium') ===
def score_1(artifact, step, ctx):
    theory = ctx['theoretical']
    tols = step.get('tolerance', {})
    energy_tol = tols.get('energy_relative', 0.05)
    magnet_tol = tols.get('magnet_absolute', 0.05)

    sim_scores = []
    pert_deviations = []
    temps = []
    for row in artifact:
        T = float(row['temperature'])
        # find closest theoretical temperature
        closest_T = min(theory.keys(), key=lambda x: abs(x - T))
        E_eq, m_eq = theory[closest_T]
        E_sim = float(row['energy_sim'])
        m_sim = float(row['magnet_sim'])
        E_pert = float(row['energy_pert_sim'])
        m_pert = float(row['magnet_pert_sim'])

        # energy relative error
        denom_energy = abs(E_eq) if abs(E_eq) > 1e-9 else 1.0
        rel_err_energy = abs(E_sim - E_eq) / denom_energy
        score_energy = max(0.0, 1.0 - rel_err_energy / energy_tol)

        # magnet absolute error
        abs_err_magnet = abs(m_sim - m_eq)
        score_magnet = max(0.0, 1.0 - abs_err_magnet / magnet_tol)

        sim_scores.append((score_energy + score_magnet) / 2.0)
        dev = (abs(E_pert - E_eq) + abs(m_pert - m_eq)) / 2.0
        pert_deviations.append(dev)
        temps.append(T)

    accuracy_score = sum(sim_scores) / len(sim_scores) if sim_scores else 0.0

    # structural: larger deviation near Tc (2.0, 2.5) than far (0.5, 3.0)
    near = []
    far = []
    for i, T in enumerate(temps):
        if abs(T - 2.0) < 0.1 or abs(T - 2.5) < 0.1:
            near.append(pert_deviations[i])
        if abs(T - 0.5) < 0.1 or abs(T - 3.0) < 0.1:
            far.append(pert_deviations[i])
    struct_score = 0.0
    if near and far:
        max_near = max(near)
        max_far = max(far)
        struct_score = 1.0 if max_near > max_far else 0.0

    return 0.8 * accuracy_score + 0.2 * struct_score


_SCORERS = {
    'dense_recurrence': score_0,
    'sparse_equilibrium': score_1,
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
