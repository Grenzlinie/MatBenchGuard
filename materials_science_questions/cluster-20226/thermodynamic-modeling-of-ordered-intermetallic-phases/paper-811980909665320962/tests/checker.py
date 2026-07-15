import os
import json
import csv

# === author imports / helpers ===
import math, json


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
    def equilibrium_n3(c, N=1000, mu=2, nu=1, K=None):
        if K is None:
            K = math.exp((mu+nu) * (-3.0))
        n3_max = min(N*c/mu, N*(1-c)/nu)
        a = 0.0
        b = n3_max
        f_a = a - K * (N*c)**mu * (N*(1-c))**nu
        if N*c - mu*b >= 0:
            f_b = b - K * (N*c - mu*b)**mu * (N*(1-c) - nu*b)**nu
        else:
            f_b = b
        if f_a * f_b >= 0:
            return float('nan')
        for _ in range(100):
            mid = (a + b) / 2
            n1 = N*c - mu*mid
            n2 = N*(1-c) - nu*mid
            if n1 < 0 or n2 < 0:
                b = mid
                continue
            f_mid = mid - K * (n1**mu) * (n2**nu)
            if f_mid == 0.0:
                return mid
            if f_a * f_mid < 0:
                b = mid
                f_b = f_mid
            else:
                a = mid
                f_a = f_mid
        return (a + b) / 2

    def S_CC(c, n3, N=1000, mu=2, nu=1):
        cc = mu / (mu + nu)
        bracket = mu*(1-c)**2 + nu*c**2 - (mu+nu)**2 * (cc - c)**2
        return c*(1-c) - (n3/N)*bracket

    N=1000; mu=2; nu=1; G_MRT=-3.0; K=math.exp((mu+nu)*G_MRT)
    gold = {}
    for c, keysuffix in [(0.1, "c0p1"), (2.0/3.0, "c2p3")]:
        frozen_n3 = N * c / mu
        eq_n3 = equilibrium_n3(c, N, mu, nu, K)
        gold["frozen_in_" + keysuffix] = S_CC(c, frozen_n3, N, mu, nu)
        gold["equilibrium_" + keysuffix] = S_CC(c, eq_n3, N, mu, nu)
    return {"gold": gold}


# === block: score_0 (check id='compute_scc') ===
def score_0(artifact, step, ctx):
    gold = ctx["gold"]
    tol_rel = 1e-6
    tol_abs = 1e-12
    matches = 0
    for key in ["frozen_in_c0p1", "equilibrium_c0p1", "frozen_in_c2p3", "equilibrium_c2p3"]:
        if key not in artifact:
            return 0.0
        v = float(artifact[key])
        g = gold[key]
        if abs(g) < 1e-12:
            ok = abs(v - g) <= tol_abs
        else:
            ok = abs(v - g) / abs(g) <= tol_rel
        if ok:
            matches += 1
    score = matches / 4.0
    return score


_SCORERS = {
    'compute_scc': score_0,
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
