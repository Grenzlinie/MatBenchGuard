import os
import json
import csv

# === author imports / helpers ===
import math

try:
    import numpy as np
    from scipy.integrate import tplquad
except ImportError:
    # Fallback when numpy/scipy are not installed in the verifier sandbox.
    # Provides a minimal numpy-like interface and a simple 3D Simpson integrator.
    class _np:
        pi = math.pi
        @staticmethod
        def cos(x):
            return math.cos(x)
    np = _np

    def tplquad(f, a, b, gfun, hfun, qfun=None, rfun=None, **kwargs):
        # Coarse triple Simpson integration over [0, pi]^3.
        # Ignores qfun/rfun because the paper's integrand uses constant z-limits.
        N = 60  # subintervals per dimension (must be even)
        if N % 2 != 0:
            N += 1
        h = math.pi / N

        # Simpson weights
        w = []
        for i in range(N + 1):
            if i == 0 or i == N:
                w.append(1)
            elif i % 2 == 1:
                w.append(4)
            else:
                w.append(2)
        w = [wi * h / 3.0 for wi in w]

        nodes = [i * h for i in range(N + 1)]
        total = 0.0
        for i, xi in enumerate(nodes):
            wx = w[i]
            for j, yj in enumerate(nodes):
                wy = w[j]
                for k, zk in enumerate(nodes):
                    wz = w[k]
                    total += wx * wy * wz * f(zk, yj, xi)
        return total, None


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
    S = 2.5
    J = 6.6
    TN = 0.85
    LHS_const = (4 * S * (S+1) * J) / (3 * TN)
    return {"LHS_const": LHS_const, "J": J}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    eta = artifact.get("eta")
    J_prime = artifact.get("J_prime")
    if eta is None or J_prime is None:
        return 0.0
    LHS = ctx["LHS_const"]
    J = ctx["J"]
    try:
        def integrand(z, y, x):
            denom = (1 - np.cos(x)) + eta * ((1 - np.cos(y)) + (1 - np.cos(z)))
            if denom == 0:
                return 0.0
            return 1.0 / denom
        I_eta, _ = tplquad(integrand, 0, np.pi, lambda x: 0, lambda x: np.pi, lambda x, y: 0, lambda x, y: np.pi, epsabs=1e-8, epsrel=1e-4)
        I_eta /= (np.pi**3)
    except Exception:
        return 0.0
    rel_error = abs(I_eta / LHS - 1.0) if LHS != 0 else abs(I_eta)
    tol = 1e-4
    if rel_error <= tol:
        score_int = 1.0
    else:
        decay_range = 0.1 - tol
        score_int = max(0.0, 1.0 - (rel_error - tol) / decay_range)
    expected_J = eta * J
    score_j = 1.0 if abs(J_prime - expected_J) <= 1e-3 else 0.0
    return 0.9 * score_int + 0.1 * score_j


_SCORERS = {
    'step_01': score_0,
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
