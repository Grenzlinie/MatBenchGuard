import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
import math

# Pure-Python replacement for numpy functions used by scorers

class _NpArray(list):
    def __getitem__(self, idx):
        if isinstance(idx, list):
            return _NpArray([self[i] for i in idx])
        return super().__getitem__(idx)

def _np_gradient(y, x):
    n = len(y)
    if n < 2:
        return [0.0] * n
    grad = [(y[1] - y[0]) / (x[1] - x[0]) if x[1] != x[0] else 0.0]
    for i in range(1, n - 1):
        grad.append((y[i+1] - y[i-1]) / (x[i+1] - x[i-1]) if x[i+1] != x[i-1] else 0.0)
    grad.append((y[-1] - y[-2]) / (x[-1] - x[-2]) if x[-1] != x[-2] else 0.0)
    return grad

def _np_argsort(a):
    return sorted(range(len(a)), key=lambda i: a[i])

def _np_argmin(a):
    return min(range(len(a)), key=lambda i: a[i])

def _np_argmax(a):
    return max(range(len(a)), key=lambda i: a[i])

class _FakeNumpy:
    @staticmethod
    def array(iterable, dtype=None):
        return _NpArray(iterable)
    gradient = staticmethod(_np_gradient)
    argsort = staticmethod(_np_argsort)
    argmin = staticmethod(_np_argmin)
    argmax = staticmethod(_np_argmax)

np = _FakeNumpy()


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
    return {
        "half_gold": 726.0,
        "half_tol": 10.0,
        "quarter_gold": 480.0,
        "quarter_tol": 20.0,
        "delta_gold": 8.0,
        "delta_tol": 0.2,
        "heat_peak_gold": 726.0,
        "heat_peak_tol": 10.0
    }


# === block: score_0 (check id='interaction_energies') ===
def score_0(artifact, step, ctx):
    eps1 = float(artifact.get("epsilon1", 0))
    eps2 = float(artifact.get("epsilon2", 0))
    eps4 = float(artifact.get("epsilon4", 0))
    # recompute delta
    delta = 3.0 * eps2 - 4.0 * eps4
    d_g = step.get("parameters", {}).get("delta_gold", ctx.get("delta_gold", 8.0))
    d_t = step.get("parameters", {}).get("delta_tol", ctx.get("delta_tol", 0.2))
    # Scoring: 0.8 for delta within tolerance, 0.2 for correct signs (epsilon1<0, eps2>0, eps4<0)
    score_delta = 1.0 if abs(delta - d_g) <= max(0.01, d_t) else 0.0
    sign_ok = (eps1 < 0) and (eps2 > 0) and (eps4 < 0)
    score_signs = 1.0 if sign_ok else 0.0
    score = 0.8 * score_delta + 0.2 * score_signs
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='half_monolayer_it_curve') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    T = np.array([float(r["T"]) for r in rows])
    I1 = np.array([float(r["I1"]) for r in rows])
    I2 = np.array([float(r["I2"]) for r in rows])
    # Sort by T
    order = np.argsort(T)
    T = T[order]
    I1 = I1[order]
    I2 = I2[order]
    # Compute gradient for each domain to find inflection (max negative slope)
    grad1 = np.gradient(I1, T)
    grad2 = np.gradient(I2, T)
    idx1 = np.argmin(grad1)
    idx2 = np.argmin(grad2)
    T_inf1 = T[idx1]
    T_inf2 = T[idx2]
    T_inf = (T_inf1 + T_inf2) / 2.0
    target = float(step.get("parameters", {}).get("T_tr_gold", ctx.get("half_gold", 726.0)))
    tol = float(step.get("parameters", {}).get("T_tr_tol", ctx.get("half_tol", 10.0)))
    dev = abs(T_inf - target)
    if dev <= tol:
        return 1.0
    elif dev <= 2 * tol:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='quarter_monolayer_it_curve') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    T = np.array([float(r["T"]) for r in rows])
    I1 = np.array([float(r["I1"]) for r in rows])
    I2 = np.array([float(r["I2"]) for r in rows])
    order = np.argsort(T)
    T = T[order]
    I1 = I1[order]
    I2 = I2[order]
    grad1 = np.gradient(I1, T)
    grad2 = np.gradient(I2, T)
    idx1 = np.argmin(grad1)
    idx2 = np.argmin(grad2)
    T_inf1 = T[idx1]
    T_inf2 = T[idx2]
    T_inf = (T_inf1 + T_inf2) / 2.0
    target = float(step.get("parameters", {}).get("T_tr_gold", ctx.get("quarter_gold", 480.0)))
    tol = float(step.get("parameters", {}).get("T_tr_tol", ctx.get("quarter_tol", 20.0)))
    dev = abs(T_inf - target)
    if dev <= tol:
        return 1.0
    elif dev <= 2 * tol:
        return 0.5
    else:
        return 0.0


# === block: score_3 (check id='heat_capacity_curve') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    T = np.array([float(r["T"]) for r in rows])
    Cv = np.array([float(r["Cv"]) for r in rows])
    # find peak temperature
    idx = np.argmax(Cv)
    T_peak = T[idx]
    target = float(step.get("parameters", {}).get("T_peak_gold", ctx.get("heat_peak_gold", 726.0)))
    tol = float(step.get("parameters", {}).get("T_peak_tol", ctx.get("heat_peak_tol", 10.0)))
    dev = abs(T_peak - target)
    if dev <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'interaction_energies': score_0,
    'half_monolayer_it_curve': score_1,
    'quarter_monolayer_it_curve': score_2,
    'heat_capacity_curve': score_3,
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
