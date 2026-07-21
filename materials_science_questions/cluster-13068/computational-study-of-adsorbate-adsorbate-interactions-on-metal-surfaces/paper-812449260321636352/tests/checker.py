import os
import json
import csv

# === author imports / helpers ===
import math
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


# === block: score_0 (check id='step1_adiabatic') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts with keys q, occupation, rate
    # step contains tolerance_relative = 0.05
    tol = step.get("tolerance_relative", 0.05)
    Delta1 = Delta2 = 0.01
    Delta = Delta1 + Delta2
    lam = 0.6
    Vb = 0.2
    eta = 0.0
    epsilon_a = lam - eta
    E_F_tip = -Vb
    hbar = 1.0
    scaling = 0.05  # same arbitrary scaling used in reference solver

    if not artifact or len(artifact) == 0:
        return 0.0

    n = len(artifact)
    errors_occ = []
    errors_rate = []
    prev_occ = -1
    monotonic = True

    for row in artifact:
        try:
            q = float(row["q"])
            occ = float(row["occupation"])
            rt = float(row["rate"])
        except:
            return 0.0

        teps = epsilon_a - 2 * lam * q
        arg1 = -teps / Delta
        arg2 = (E_F_tip - teps) / Delta

        # Reference occupation from Eq (3)
        ref_occ = (1.0 / math.pi) * (
            (Delta1 / Delta) * (math.atan(arg1) + math.pi / 2) +
            (Delta2 / Delta) * (math.atan(arg2) + math.pi / 2)
        )

        # Reference rate from Eq (4), scaled as in the reference solver
        integral_rate = (1.0 / Delta) * (math.atan(arg1) - math.atan(arg2))
        ref_rate = (Delta1 * Delta2 / (math.pi * hbar * Delta)) * integral_rate * scaling

        # Relative error with a floor to avoid division by zero
        denom_occ = max(abs(ref_occ), 1e-9)
        errors_occ.append(abs(occ - ref_occ) / denom_occ)
        denom_rate = max(abs(ref_rate), 1e-9)
        errors_rate.append(abs(rt - ref_rate) / denom_rate)

        if prev_occ > occ + 1e-6:  # allow minor noise
            monotonic = False
        prev_occ = occ

    # Fraction of points within tolerance
    ok_occ = sum(1 for e in errors_occ if e <= tol)
    ok_rate = sum(1 for e in errors_rate if e <= tol)
    score_occ = ok_occ / n if n else 0.0
    score_rate = ok_rate / n if n else 0.0
    score_mono = 1.0 if monotonic else 0.0

    # Combine: 40% occupation, 40% rate, 20% monotonicity
    final_score = 0.4 * score_occ + 0.4 * score_rate + 0.2 * score_mono
    return max(0.0, min(1.0, final_score))


# === block: score_1 (check id='step2_current') ===
def score_1(artifact, step, ctx):
    # artifact is list of dicts with scenario, independent_variable, independent_value, current
    tol_abs = step.get("tolerance_absolute", 0.2)

    def compute_avg_k(lam, Vb, eta, Delta1, Delta2):
        Delta = Delta1 + Delta2
        epsilon_a = lam - eta
        E_F_tip = -Vb
        qs = np.linspace(0, 1, 200)
        n_a_vals = []
        k_vals = []
        E_vals = []
        kT = 0.05

        for q in qs:
            teps = epsilon_a - 2 * lam * q
            arg1 = -teps / Delta
            arg2 = (E_F_tip - teps) / Delta
            n_a = (1.0 / math.pi) * (
                (Delta1 / Delta) * (math.atan(arg1) + math.pi / 2) +
                (Delta2 / Delta) * (math.atan(arg2) + math.pi / 2)
            )
            integral_rate = (1.0 / Delta) * (math.atan(arg1) - math.atan(arg2))
            rate = (Delta1 * Delta2 / (math.pi * 1.0 * Delta)) * integral_rate  # hbar=1
            n_a_vals.append(n_a)
            k_vals.append(rate)
            E = lam * q * q + (epsilon_a - 2 * lam * q) * n_a
            E_vals.append(E)

        E_min = np.min(E_vals)
        w = np.exp(-(np.array(E_vals) - E_min) / kT)
        Z = np.trapz(w, qs)
        avg_k = np.trapz(w * np.array(k_vals), qs) / Z if Z > 0 else 0.0
        return avg_k

    if not artifact or len(artifact) == 0:
        return 0.0

    # Group rows by scenario
    scenarios = {}
    for row in artifact:
        sc = row.get("scenario", "").strip()
        if not sc:
            continue
        scenarios.setdefault(sc, []).append(row)

    num_points = 0
    errors = []
    trend_checks = []

    for sc, rows in scenarios.items():
        parts = sc.split("_")
        fig = parts[0]  # fig4, fig6, fig7
        try:
            lam_val = float(parts[-1])
        except:
            continue

        if fig == "fig4":
            Delta1 = Delta2 = 0.01
            eta = 0.01
        elif fig == "fig6":
            Delta1 = Delta2 = 0.01
            Vb = 0.1
        elif fig == "fig7":
            Delta1 = 0.01
            Delta2 = 0.001
            Vb = 0.05
        else:
            continue

        ref_vals = []
        agent_vals = []
        indep_vals = []

        for row in rows:
            try:
                iv = float(row["independent_value"])
                cur = float(row["current"])
            except:
                continue

            if fig == "fig4":
                Vb = iv
            elif fig in ("fig6", "fig7"):
                eta = iv

            ref_avg = compute_avg_k(lam_val, Vb, eta, Delta1, Delta2)
            ref_vals.append(ref_avg)
            agent_vals.append(cur)
            indep_vals.append(iv)

        if len(ref_vals) == 0:
            continue

        # Normalise reference by its own max (paper normalises each curve to max=1)
        max_ref = max(ref_vals)
        if max_ref <= 0:
            continue
        norm_ref = [v / max_ref for v in ref_vals]

        for i in range(len(norm_ref)):
            err = abs(agent_vals[i] - norm_ref[i])
            errors.append(err)
            num_points += 1

        # Trend checks
        if fig == "fig4" and len(indep_vals) > 1:
            sorted_pairs = sorted(zip(indep_vals, agent_vals))
            cur_prev = -1
            monotonic_inc = True
            for v, c in sorted_pairs:
                if c < cur_prev - 1e-4:
                    monotonic_inc = False
                cur_prev = c
            trend_checks.append(1.0 if monotonic_inc else 0.0)
        elif fig in ("fig6", "fig7") and len(indep_vals) > 2:
            max_idx = int(np.argmax(agent_vals))
            peak_eta = indep_vals[max_idx]
            if -0.1 <= peak_eta <= 0.1:
                trend_checks.append(1.0)
            else:
                trend_checks.append(0.5)

    if num_points == 0:
        return 0.0

    ok_points = sum(1 for e in errors if e <= tol_abs)
    score_points = ok_points / num_points if num_points else 0.0
    score_trend = np.mean(trend_checks) if trend_checks else 0.0

    final_score = 0.8 * score_points + 0.2 * score_trend
    return max(0.0, min(1.0, final_score))


_SCORERS = {
    'step1_adiabatic': score_0,
    'step2_current': score_1,
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
