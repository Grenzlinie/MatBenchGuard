import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, os
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "numpy"])
import numpy as np
import json, math


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


# === block: score_0 (check id='order_preference') ===
def score_0(artifact, step, ctx):
    configs = artifact.get("configurations", [])
    if not configs:
        return 0.0
    eb = {}
    for c in configs:
        eb[c["name"]] = c["epsilon_b"]
    order = ["1H", "2H_ortho_same", "2H_ortho_counter", "3H", "4H", "6H_closed_ring", "10H", "16H", "24H", "CH_infinite"]
    checks = []
    for i in range(len(order)-1):
        a = eb.get(order[i])
        b = eb.get(order[i+1])
        if a is None or b is None:
            continue
        checks.append(1.0 if a <= b + 1e-6 else 0.0)
    if "12H_incomplete" in eb and "10H" in eb:
        checks.append(1.0 if eb["12H_incomplete"] < eb["10H"] else 0.0)
    if "12H_incomplete" in eb and "16H" in eb:
        checks.append(1.0 if eb["12H_incomplete"] < eb["16H"] else 0.0)
    if not checks:
        return 0.0
    return sum(checks) / len(checks)


# === block: score_1 (check id='linearity') ===
def score_1(artifact, step, ctx):
    configs = artifact.get("configurations", [])
    target_names = {"6H_closed_ring", "10H", "16H", "24H", "CH_infinite"}
    x = []
    y = []
    for c in configs:
        if c["name"] in target_names:
            try:
                xn = float(c["n23"]) / float(c["n_H"])
                yn = float(c["epsilon_b"])
                x.append(xn)
                y.append(yn)
            except:
                pass
    if len(x) < 3:
        return 0.0
    x = np.array(x)
    y = np.array(y)
    A = np.vstack([x, np.ones_like(x)]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]
    y_pred = m * x + b
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    if r2 >= 0.999:
        return 1.0
    elif r2 >= 0.99:
        return 0.7
    elif r2 >= 0.95:
        return 0.3
    else:
        return 0.0


# === block: score_2 (check id='barrier') ===
def score_2(artifact, step, ctx):
    nucleation = artifact.get("nucleation")
    if not nucleation:
        return 0.0
    params = nucleation.get("conditions", [])
    if not params:
        return 0.0
    eps_inf = nucleation.get("epsilon_b_infinity")
    gamma = nucleation.get("gamma")
    if eps_inf is None or gamma is None:
        return 0.0
    def check_condition(cond):
        mu = cond.get("mu_H")
        n = cond.get("n")
        DeltaG = cond.get("DeltaG")
        if mu is None or n is None or DeltaG is None or len(n) != len(DeltaG) or len(n) < 2:
            return False
        expected = [-(eps_inf + mu) * ni + gamma * math.sqrt(ni) for ni in n]
        for exp, got in zip(expected, DeltaG):
            if abs(exp - got) > 1e-3:
                return False
        max_val = max(DeltaG)
        max_idx = DeltaG.index(max_val)
        if max_idx == 0 or n[max_idx] <= 1:
            return False
        if DeltaG[-1] >= 0:
            return False
        return True
    passed = sum(check_condition(c) for c in params)
    return passed / len(params)


_SCORERS = {
    'order_preference': score_0,
    'linearity': score_1,
    'barrier': score_2,
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
