import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad


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


# === block: score_0 (check id='gb_energy_data') ===
def score_0(artifact, step, ctx):
    # GB energy computation helpers
    def compute_u_g(u_m, alpha):
        # Eq. (68): u_g/(1-u_g) = u_m/(1-u_m) * exp(alpha)
        # with beta*omega_A = 1.0
        factor = u_m / (1.0 - u_m) * np.exp(alpha)
        return factor / (1.0 + factor)

    def u_phi(phi, u_m, alpha):
        # Eq. (59): u(phi)/(1-u(phi)) = u_m/(1-u_m) * exp(alpha * g(phi))
        g = 4.0 * phi * (1.0 - phi)
        factor = u_m / (1.0 - u_m) * np.exp(alpha * g)
        return factor / (1.0 + factor)

    def integrand_model_I(phi, u_m, alpha):
        # sqrt of effective potential Omega1(phi) from Eq. (61) scaled by (4/pi)*sigma_A
        # sigma_A = 1; beta*omega_A = 1; omega_A = 1e9 but factor simplifies
        # Actually Eq. (62): sigma = (4/pi)*sigma_A * integral_0^1 sqrt(g(phi) + (1/beta omega_A) ln((1-u(phi))/(1-u_m))) dphi
        # Here sigma_A=1, beta*omega_A=1, so term inside sqrt = g + ln((1-u)/(1-u_m))
        g = 4.0 * phi * (1.0 - phi)
        u = u_phi(phi, u_m, alpha)
        if u >= 1.0 or u_m >= 1.0:
            return 0.0
        term = g + np.log((1.0 - u) / (1.0 - u_m))
        if term <= 0.0:
            return 0.0
        return np.sqrt(term)

    def expected_sigma(alpha, model, u_m):
        # returns expected GB energy for a given (alpha, model, u_m)
        # model is 'modelI', 'modelII', or 'classical'
        # parameters: sigma_A=1, beta*omega_A=1
        if model == 'modelI':
            # numerical integration
            integral, _ = quad(integrand_model_I, 0.0, 1.0, args=(u_m, alpha), limit=200)
            return 4.0 / np.pi * integral
        else:
            u_g = compute_u_g(u_m, alpha)
            ln_term = np.log((1.0 - u_g) / (1.0 - u_m)) if u_g < 1.0 and u_m < 1.0 else 0.0
            # Eq. (70): omega^e / omega_A = 1 + (1/(beta*omega_A))*ln(...) = 1 + ln_term
            ratio = 1.0 + ln_term
            if model == 'modelII':
                return np.sqrt(max(ratio, 0.0))   # Eq. (71)
            elif model == 'classical':
                return max(ratio, 0.0)            # Eq. (72)
            else:
                return np.nan

    # Parse agent CSV
    rows = artifact  # artifact is list of dicts with keys alpha, model, u_m, sigma
    # Validate columns
    if not rows or not all(k in rows[0] for k in ('alpha', 'model', 'u_m', 'sigma')):
        return 0.0

    # Build lookup: map (alpha, model) -> list of (u_m, sigma)
    data = {}
    for r in rows:
        try:
            a = int(r['alpha'])
            m = str(r['model']).strip()
            um = float(r['u_m'])
            s = float(r['sigma'])
        except (ValueError, KeyError):
            continue
        key = (a, m)
        data.setdefault(key, []).append((um, s))

    # Verification points: (alpha, model, u_m_target)
    models = ['modelI', 'modelII', 'classical']
    alphas = [2, 3, 4]
    test_u_m = [0.02, 0.05, 0.10, 0.15, 0.20]
    points = []
    for alpha in alphas:
        for model in models:
            for um_target in test_u_m:
                points.append((alpha, model, um_target))

    # Recomputation accuracy
    MAX_REL_ERROR_TOL = 0.01          # tolerance for relative error
    MIN_REL_ERROR_FLOOR = 1e-6        # full credit below this
    total_points = 0
    cum_score = 0.0
    for alpha, model, um_target in points:
        key = (alpha, model)
        if key not in data:
            continue
        entries = data[key]
        # find closest u_m in the agent's CSV
        closest_idx = min(range(len(entries)), key=lambda i: abs(entries[i][0] - um_target))
        um_agent, sigma_agent = entries[closest_idx]
        if abs(um_agent - um_target) > 1e-4:  # not a close enough match
            continue
        if not np.isfinite(sigma_agent):
            # if sigma is NaN, skip (e.g., Model I out of range)
            if model == 'modelI' and um_target > 0.2:  # reasonable for high alpha?
                continue
            # else treat as zero score
            cum_score += 0.0
            total_points += 1
            continue
        sigma_exp = expected_sigma(alpha, model, um_target)
        if not np.isfinite(sigma_exp) or sigma_exp == 0.0:
            continue
        rel_err = abs(sigma_agent - sigma_exp) / max(sigma_exp, 1e-12)
        if rel_err < MIN_REL_ERROR_FLOOR:
            pt_score = 1.0
        else:
            pt_score = max(0.0, 1.0 - (rel_err - MIN_REL_ERROR_FLOOR) / (MAX_REL_ERROR_TOL - MIN_REL_ERROR_FLOOR))
        cum_score += pt_score
        total_points += 1

    recompute_score = cum_score / total_points if total_points > 0 else 0.0

    # Structural checks
    struct_score = 1.0
    # 1) Model I monotonic decrease
    for alpha in alphas:
        key = (alpha, 'modelI')
        if key not in data:
            continue
        entries = data[key]
        entries.sort(key=lambda x: x[0])
        prev_sigma = None
        monotonic = True
        for um, s in entries:
            if not np.isfinite(s):
                continue
            if prev_sigma is not None and s > prev_sigma + 1e-10:
                monotonic = False
                break
            prev_sigma = s
        if not monotonic:
            struct_score -= 0.1
    # 2) Model I non-negative and positive lower bound (just non-negative)
    for alpha in alphas:
        key = (alpha, 'modelI')
        if key in data:
            sigmas = [s for _, s in data[key] if np.isfinite(s)]
            if sigmas and min(sigmas) < 0.0:
                struct_score -= 0.1
    # 3) Model II monotonic decrease
    for alpha in alphas:
        key = (alpha, 'modelII')
        if key not in data:
            continue
        entries = data[key]
        entries.sort(key=lambda x: x[0])
        prev_sigma = None
        monotonic = True
        for um, s in entries:
            if not np.isfinite(s):
                continue
            if prev_sigma is not None and s > prev_sigma + 1e-10:
                monotonic = False
                break
            prev_sigma = s
        if not monotonic:
            struct_score -= 0.1
    # 4) sigma_modelII < sigma_classical at a few common u_m
    for alpha in alphas:
        keyII = (alpha, 'modelII')
        keyCl = (alpha, 'classical')
        if keyII not in data or keyCl not in data:
            continue
        for um_target in [0.05, 0.10]:
            # find closest u_m in each model
            umII, sII = min(data[keyII], key=lambda x: abs(x[0]-um_target))
            umCl, sCl = min(data[keyCl], key=lambda x: abs(x[0]-um_target))
            if abs(umII - um_target) > 1e-4 or abs(umCl - um_target) > 1e-4:
                continue
            if np.isfinite(sII) and np.isfinite(sCl) and sII >= sCl:
                struct_score -= 0.05

    struct_score = max(0.0, struct_score)

    # Combine
    final_score = 0.7 * recompute_score + 0.3 * struct_score
    return final_score


_SCORERS = {
    'gb_energy_data': score_0,
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
