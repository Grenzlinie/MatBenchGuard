import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import ellipk


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
    return {'A_c': 1.181, 'gamma_ref': 0.61, 'delta_ref': 0.87, 'test_A_list': [1.2, 1.25, 1.3, 1.35, 1.4]}


# === block: score_0 (check id='step_01_envelope') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts with keys 'A', 'q_env'
    rows = artifact
    if not rows:
        return 0.0
    A_vals = []
    q_vals = []
    for r in rows:
        try:
            A = float(r['A'])
            q = float(r['q_env'])
        except (ValueError, KeyError):
            return 0.0
        A_vals.append(A)
        q_vals.append(q)
    # sort by A
    pairs = sorted(zip(A_vals, q_vals), key=lambda x: x[0])
    A_sorted = [p[0] for p in pairs]
    q_sorted = [p[1] for p in pairs]
    A_c = ctx['A_c']
    # structural checks
    below_ok = 0
    below_total = 0
    above_ok = 0
    above_total = 0
    for A, q in zip(A_sorted, q_sorted):
        if A < A_c - 0.015:  # below critical
            below_total += 1
            if q < 0.1 * A:
                below_ok += 1
        elif A > A_c + 0.015:  # above critical
            above_total += 1
            if q > 0.02 * A:  # finite, not tiny
                above_ok += 1
    frac_below = below_ok / max(1, below_total) if below_total > 0 else 1.0
    frac_above = above_ok / max(1, above_total) if above_total > 0 else 1.0
    # sharpness: max absolute difference in q_env between adjacent A
    max_diff = 0.0
    for i in range(1, len(q_sorted)):
        diff = abs(q_sorted[i] - q_sorted[i-1])
        if diff > max_diff:
            max_diff = diff
    # a sharp transition should have max_diff at least around 0.05*A? We'll normalize
    sharp_score = min(1.0, max_diff / 0.1) if max_diff > 0 else 0.0
    score = 0.4 * frac_below + 0.4 * frac_above + 0.2 * sharp_score
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='step_02_frequency') ===
def score_1(artifact, step, ctx):
    # artifact: list of dicts with 'A', 'omega'
    rows = artifact
    if not rows:
        return 0.0
    # build dict A->omega
    freq_map = {}
    for r in rows:
        try:
            A = float(r['A'])
            omega = float(r['omega'])
        except (ValueError, KeyError):
            return 0.0
        freq_map[A] = omega
    test_As = ctx['test_A_list']
    errors = []
    for A_test in test_As:
        if A_test not in freq_map:
            errors.append(1.0)
        else:
            omega_agent = freq_map[A_test]
            # theoretical omega using scipy ellipk
            m = -A_test**2 / (2 + A_test**2)
            K = ellipk(m)
            omega_theory = (np.pi / 4.0) * np.sqrt(2 + A_test**2) / K
            rel_err = abs(omega_agent - omega_theory) / omega_theory if omega_theory != 0 else 1.0
            errors.append(rel_err)
    mean_err = np.mean(errors) if errors else 1.0
    score = max(0.0, 1.0 - mean_err / 0.05)
    return min(1.0, score)


# === block: score_2 (check id='step_03_relaxation_time') ===
def score_2(artifact, step, ctx):
    # artifact: list of dicts with 'A', 'tau_rel'
    rows = artifact
    if not rows:
        return 0.0
    A_vals = []
    tau_vals = []
    for r in rows:
        try:
            A = float(r['A'])
            tau = float(r['tau_rel'])
        except (ValueError, KeyError):
            return 0.0
        A_vals.append(A)
        tau_vals.append(tau)
    pairs = sorted(zip(A_vals, tau_vals), key=lambda x: x[0])
    A_sorted = [p[0] for p in pairs]
    tau_sorted = [p[1] for p in pairs]
    A_c = ctx['A_c']
    # pick points below A_c
    below_mask = [a < A_c for a in A_sorted]
    A_below = [a for a, m in zip(A_sorted, below_mask) if m]
    tau_below = [t for t, m in zip(tau_sorted, below_mask) if m]
    if len(tau_below) < 3:
        return 0.0
    # monotonicity: check non-decreasing with small noise tolerance (allow 2% drop)
    mono_ok = 0
    for i in range(1, len(tau_below)):
        if tau_below[i] >= 0.98 * tau_below[i-1]:
            mono_ok += 1
    mono_score = mono_ok / max(1, len(tau_below)-1) if len(tau_below) > 1 else 1.0
    # divergence: check last 3 tau > 1e4
    last_3 = tau_below[-3:] if len(tau_below) >= 3 else tau_below
    div_ok = sum(1 for t in last_3 if t > 1e4) / len(last_3)
    score = 0.5 * mono_score + 0.5 * div_ok
    return min(1.0, max(0.0, score))


# === block: score_3 (check id='step_04_critical_amplitude') ===
def score_3(artifact, step, ctx):
    # artifact is a string (the file content)
    try:
        Ac_agent = float(artifact.strip())
    except (ValueError, AttributeError):
        return 0.0
    Ac_gold = ctx['A_c']
    diff = abs(Ac_agent - Ac_gold)
    score = max(0.0, 1.0 - diff / 0.03)
    return min(1.0, score)


# === block: score_4 (check id='step_05_powerlaw_exponents') ===
def score_4(artifact, step, ctx):
    # artifact is a dict
    data = artifact
    if not data or not isinstance(data, dict):
        return 0.0
    # required keys
    required = ['gamma', 'delta', 'gamma_error', 'delta_error', 'fit_range']
    if not all(k in data for k in required):
        return 0.0
    # check exponents against reference with tolerance 0.1
    gamma = float(data['gamma'])
    delta = float(data['delta'])
    gamma_ref = ctx['gamma_ref']
    delta_ref = ctx['delta_ref']
    gamma_score = max(0.0, 1.0 - abs(gamma - gamma_ref) / 0.1)
    delta_score = max(0.0, 1.0 - abs(delta - delta_ref) / 0.1)
    exp_score = (gamma_score + delta_score) / 2.0
    # structural: errors positive, fit_range present
    struct = 0.0
    if float(data['gamma_error']) > 0 and float(data['delta_error']) > 0:
        struct += 0.3
    if isinstance(data['fit_range'], dict) and len(data['fit_range']) > 0:
        struct += 0.2
    struct = min(0.5, struct)
    score = 0.8 * exp_score + 0.2 * (struct / 0.5)  # normalize struct to 1
    return min(1.0, max(0.0, score))


_SCORERS = {
    'step_01_envelope': score_0,
    'step_02_frequency': score_1,
    'step_03_relaxation_time': score_2,
    'step_04_critical_amplitude': score_3,
    'step_05_powerlaw_exponents': score_4,
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
