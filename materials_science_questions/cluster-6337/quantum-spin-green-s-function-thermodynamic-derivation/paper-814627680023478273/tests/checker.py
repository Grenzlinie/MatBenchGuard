import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import loggamma


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


# === block: score_0 (check id='check_spin_current') ===
def score_0(artifact, step, ctx):
    m = 600

    def get_p(gamma, h):
        return 1j / (2.0 * (gamma - 1j * h))

    def build_B0(p):
        k = np.arange(m, dtype=float)
        p_minus_k_sq = (p.real - k)**2 + p.imag**2
        two_p_minus_k_sq = (2*p.real - k)**2 + (2*p.imag)**2
        B0 = np.zeros((m, m), dtype=float)
        for i in range(m):
            B0[i, i] = 2.0 * p_minus_k_sq[i]
            if i > 0:
                B0[i, i-1] = two_p_minus_k_sq[i-1]
            if i < m-1:
                B0[i, i+1] = (i+1)**2
        return B0

    def compute_vR(p, theta):
        if theta == 0.0:
            vR = np.zeros(m, dtype=float)
            vR[0] = 1.0
            return vR
        psi = np.tan(theta / 2.0)
        psi2 = psi * psi
        k = np.arange(m, dtype=float)
        # log terms with loggamma for stability
        logterms = k * np.log(psi2) + 2.0 * np.real(
            loggamma(2*p + 1) - loggamma(k + 1) - loggamma(2*p - k + 1)
        )
        max_log = np.max(logterms)
        # avoid overflow by exponentiating shifted values
        vR = np.exp(logterms - max_log)
        return vR

    def compute_J(N, h, gamma, theta):
        p = get_p(gamma, h)
        B0 = build_B0(p)
        vR = compute_vR(p, theta)
        a = np.zeros(m, dtype=float)
        a[0] = 1.0
        a_prev = None
        s_last = 1.0
        for _ in range(N):
            a_prev = a.copy()
            b = a @ B0
            s = np.max(np.abs(b))
            if s > 0:
                a = b / s
            else:
                a = np.zeros_like(b)
            s_last = s  # keep the final scaling factor
        if N == 0:
            # not used in our parameter set, but handle gracefully
            return 0.0
        dot1 = np.dot(a_prev, vR)
        dot2 = np.dot(a, vR)
        if dot2 == 0.0 or s_last == 0.0:
            return 0.0
        ratio = dot1 / (dot2 * s_last)
        # guard against NaN/Inf
        if not np.isfinite(ratio):
            return 0.0
        prefactor = 2.0 * gamma / (gamma**2 + h**2)
        J = prefactor * ratio
        return J

    tol = step.get('tolerance', 1e-3)
    rows = artifact
    total = 0.0
    count = 0
    for row in rows:
        try:
            N_val = int(row['N'])
            h_val = float(row['h'])
            gamma_val = float(row['gamma'])
            theta_val = float(row['theta'])
            J_agent = float(row['J'])
        except (KeyError, ValueError):
            continue
        try:
            J_gold = float(compute_J(N_val, h_val, gamma_val, theta_val))
        except Exception:
            J_gold = 0.0
        if J_gold == 0.0:
            err = abs(J_agent)
        else:
            err = abs(J_agent - J_gold) / (abs(J_gold) + 1e-15)
        score_row = max(0.0, 1.0 - err / tol)
        total += score_row
        count += 1
    return 0.0 if count == 0 else total / count


_SCORERS = {
    'check_spin_current': score_0,
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
