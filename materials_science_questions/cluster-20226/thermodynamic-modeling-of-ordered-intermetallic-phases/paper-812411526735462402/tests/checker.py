import os
import json
import csv

# === author imports / helpers ===
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
    import json
    spec = json.load(open('/tests/grading_spec.json'))
    hidden = spec.get('hidden_references', {})
    ctx = {
        'coexistence_refs': None,
        'lindemann_refs': None,
    }
    if 'coexistence_refs' in hidden:
        ctx['coexistence_refs'] = [tuple(r) for r in hidden['coexistence_refs']]
    if 'lindemann_refs' in hidden:
        ctx['lindemann_refs'] = [tuple(r) for r in hidden['lindemann_refs']]
    return ctx


# === block: score_0 (check id='lambda_line') ===
def score_0(artifact, step, ctx):
    # parameters (in units where kBT=1, R11=1)
    eps11 = 2.0
    eps22 = 2.0
    eps12 = 1.8877
    R11 = 1.0
    R22 = 0.665
    R12 = 0.6

    # tolerance for D(k) zero condition from grading_spec
    _tol = step.get('tol', 1e-4)
    try:
        tol = float(_tol)
    except (TypeError, ValueError):
        tol = 1e-4

    def v_hat(k, eps, R):
        # Fourier transform of Gaussian potential v(r)=eps*exp(-r^2/R^2)
        return eps * np.pi**1.5 * R**3 * np.exp(-k**2 * R**2 / 4.0)

    def D_val(k, rho, x):
        rho1 = rho * (1 - x)
        rho2 = rho * x
        v11 = v_hat(k, eps11, R11)
        v22 = v_hat(k, eps22, R22)
        v12 = v_hat(k, eps12, R12)
        return (1.0 + rho1 * v11) * (1.0 + rho2 * v22) - rho1 * rho2 * v12**2

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    k_vals = np.linspace(0.01, 15.0, 5000)  # fine grid; k in 1/R11 units
    pass_count = 0
    total = 0
    for p in artifact:
        try:
            rho = float(p['density'])
            x = float(p['concentration'])
        except (TypeError, KeyError, ValueError):
            continue
        total += 1
        D_curve = np.array([D_val(k, rho, x) for k in k_vals])
        min_idx = np.argmin(D_curve)
        min_val = D_curve[min_idx]
        if abs(min_val) <= tol:
            pass_count += 1

    if total == 0:
        return 0.0
    fraction = pass_count / total
    # Require at least 20% of points to pass; full credit at 80% or above
    if fraction < 0.2:
        return 0.0
    return min(1.0, fraction / 0.8)


# === block: score_1 (check id='coexistence_curve') ===
def score_1(artifact, step, ctx):
    refs = ctx.get('coexistence_refs')
    if not refs or not isinstance(artifact, list):
        return 0.0

    tol_rho = 0.5
    tol_x = 0.02

    matches = 0
    for ref_rho, ref_x in refs:
        found = False
        for p in artifact:
            try:
                rho = float(p['density'])
                x = float(p['concentration'])
            except (TypeError, KeyError, ValueError):
                continue
            if abs(rho - ref_rho) <= tol_rho and abs(x - ref_x) <= tol_x:
                found = True
                break
        if found:
            matches += 1

    return matches / len(refs) if refs else 0.0


# === block: score_2 (check id='lindemann_ratios') ===
def score_2(artifact, step, ctx):
    refs = ctx.get('lindemann_refs')
    if not refs or not isinstance(artifact, list):
        return 0.0

    tol_conc = 0.01
    tol_L = 0.05

    matches = 0
    for ref_conc, ref_L1, ref_L2 in refs:
        best_diff = float('inf')
        best_L1 = best_L2 = None
        for p in artifact:
            try:
                conc = float(p['concentration'])
                L1 = float(p['L1'])
                L2 = float(p['L2'])
            except (TypeError, KeyError, ValueError):
                continue
            if abs(conc - ref_conc) <= tol_conc:
                diff = (abs(L1 - ref_L1) + abs(L2 - ref_L2)) / 2.0
                if diff < best_diff:
                    best_diff = diff
                    best_L1 = L1
                    best_L2 = L2
        if best_diff <= tol_L:
            matches += 1

    return matches / len(refs) if refs else 0.0


_SCORERS = {
    'lambda_line': score_0,
    'coexistence_curve': score_1,
    'lindemann_ratios': score_2,
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
