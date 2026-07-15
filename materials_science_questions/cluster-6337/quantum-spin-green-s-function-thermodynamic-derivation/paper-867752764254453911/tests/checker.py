import os
import json
import csv

# === author imports / helpers ===
import numpy as np; import math


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
        lam = 0.1
        N = 10
        ctx = {}
        precomp = {}
        for ell in [2, 4]:
            beta = [n * (1 - n * lam) for n in range(1, ell + 1)]
            # p^{(0)}_n up to ell
            p0 = [np.array([1.0])]          # deg 0
            p0.append(np.array([1.0, 0.0])) # deg 1
            for n in range(1, ell):
                xpn = np.pad(p0[-1], (1, 0), mode='constant')
                p_prev = np.pad(p0[-2], (2, 0), mode='constant')
                p_next = xpn - beta[n-1] * p_prev
                p0.append(p_next)
            # p^{(1)} up to ell-1
            p1 = [np.array([1.0])]
            p1.append(np.array([1.0, 0.0]))
            for n in range(1, ell - 1):
                beta_idx = n + 1
                xpn = np.pad(p1[-1], (1, 0), mode='constant')
                p_prev = np.pad(p1[-2], (2, 0), mode='constant')
                p_next = xpn - beta[beta_idx - 1] * p_prev
                p1.append(p_next)
            zeros = np.roots(p0[ell])
            pos_zeros = zeros[np.isreal(zeros) & (np.real(zeros) > 0)].real
            pos_zeros.sort()
            poly0_deriv = np.polyder(p0[ell])
            residues = []
            for xk in pos_zeros:
                a = np.polyval(p1[ell - 1], xk) / np.polyval(poly0_deriv, xk)
                residues.append(float(a))
            precomp[ell] = {
                'zeros': pos_zeros.tolist(),
                'residues': residues
            }
        ctx['precomp'] = precomp
        return ctx


# === block: score_0 (check id='finite_N_accuracy') ===
def score_0(artifact, step, ctx):
        tol = 1e-5
        # Recompute correct reference time series on the fly, ignoring the broken ctx['precomp']
        lam = 0.1
    
        # Gather unique closure orders present in the artifact
        ells = set()
        for row in artifact:
            ells.add(int(row['closure_order']))
    
        # Precompute expected zeros and residues for each ℓ
        exp_cache = {}
        for ell in ells:
            beta = [n * (1 - n * lam) for n in range(1, max(ell, 4) + 1)]
            # p^{(0)} polynomials up to degree ell
            p0_nm1 = np.poly1d([1.0])               # p0_0
            p0_n   = np.poly1d([1.0, 0.0])          # p0_1
            for n in range(1, ell):
                xp0 = np.poly1d([1.0, 0.0]) * p0_n
                p0_np1 = xp0 - beta[n-1] * p0_nm1
                p0_nm1, p0_n = p0_n, p0_np1
            p0_ell = p0_n
        
            # p^{(1)} polynomials up to degree ell-1
            if ell >= 2:
                p1_nm1 = np.poly1d([1.0])
                p1_n   = np.poly1d([1.0, 0.0])
                for n in range(1, ell-1):
                    idx = n + 1
                    xp1 = np.poly1d([1.0, 0.0]) * p1_n
                    p1_np1 = xp1 - beta[idx-1] * p1_nm1
                    p1_nm1, p1_n = p1_n, p1_np1
                p1_ellm1 = p1_n
            else:
                p1_ellm1 = np.poly1d([1.0])  # fallback not used for ell<2
        
            zeros = np.roots(p0_ell.coeffs)
            pos_zeros = [z.real for z in zeros if abs(z.imag) < 1e-10 and z.real > 0]
            pos_zeros.sort()
            p0_deriv = np.polyder(p0_ell)
            residues = [float(np.polyval(p1_ellm1.coeffs, xk) / np.polyval(p0_deriv.coeffs, xk)) for xk in pos_zeros]
            exp_cache[ell] = (pos_zeros, residues)
    
        errors = []
        for row in artifact:
            tau = float(row['tau'])
            u1_real_act = float(row['u1_real'])
            u1_imag_act = float(row['u1_imag'])
            ell = int(row['closure_order'])
            zeros, residues = exp_cache.get(ell, ([], []))
            if not zeros:
                return 0.0
            comp = sum(a * math.cos(x * tau) for a, x in zip(residues, zeros))
            u1_real_exp = 2.0 * comp   # s^x=1, s^y=0
            u1_imag_exp = 0.0
            errors.append(abs(u1_real_exp - u1_real_act) + abs(u1_imag_exp - u1_imag_act))
    
        if not errors:
            return 0.0
        max_err = max(errors)
        if max_err <= tol:
            return 1.0
        return max(0.0, 1.0 - (max_err - tol) / (9.0 * tol))


# === block: score_1 (check id='finite_N_quasiperiodic') ===
def score_1(artifact, step, ctx):
        max_abs = 0.0
        for row in artifact:
            r = float(row['u1_real'])
            i = float(row['u1_imag'])
            mag = math.sqrt(r * r + i * i)
            if mag > max_abs:
                max_abs = mag
        return 1.0 if max_abs >= 0.9 else 0.0


# === block: score_2 (check id='thermo_limit_accuracy') ===
def score_2(artifact, step, ctx):
        tol = 1e-5
        errors = []
        for row in artifact:
            tau = float(row['tau'])
            u1_real_act = float(row['u1_real'])
            u1_imag_act = float(row['u1_imag'])
            exp_val = math.exp(-tau * tau / 2.0)
            u1_real_exp = exp_val
            u1_imag_exp = 0.0
            errors.append(abs(u1_real_exp - u1_real_act) + abs(u1_imag_exp - u1_imag_act))
        if not errors:
            return 0.0
        max_err = max(errors)
        if max_err <= tol:
            return 1.0
        return max(0.0, 1.0 - (max_err - tol) / (9 * tol))


_SCORERS = {
    'finite_N_accuracy': score_0,
    'finite_N_quasiperiodic': score_1,
    'thermo_limit_accuracy': score_2,
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
