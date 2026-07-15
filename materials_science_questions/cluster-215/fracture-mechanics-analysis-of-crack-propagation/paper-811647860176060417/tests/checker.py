import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad

def F(x):
    # geometry factor for three-point bend, S/W=4 (Tada, Paris, Irwin)
    return 1.107 - 1.65*x + 0.93*x**2

def compute_I(x0, n):
    if x0 <= 0.0 or x0 >= 1.0:
        return 0.0
    integrand = lambda x: ( (np.sqrt(x0)*F(x0)) / (np.sqrt(x)*F(x)) )**n
    I, _ = quad(integrand, x0, 1.0, limit=200, epsabs=1e-12, epsrel=1e-12)
    return I


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


# === block: score_0 (check id='step_compute_i') ===
def score_0(artifact, step, ctx):
    total = len(artifact) if artifact else 0
    if total == 0:
        return 0.0
    correct = 0
    for row in artifact:
        try:
            x0 = float(row['x0'])
            n = int(row['n'])
            I_val = float(row['I_value'])
        except (ValueError, KeyError):
            continue
        I_calc = compute_I(x0, n)
        if np.isclose(I_val, I_calc, rtol=1e-4, atol=1e-8):
            correct += 1
    return correct / total


# === block: score_1 (check id='step_verify_scaling') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    large_rows = []
    small_rows = []
    for row in artifact:
        try:
            W = float(row['W'])
            a0 = float(row['a0'])
            K = float(row['K_Ii'])
            Tf = float(row['T_f'])
        except (ValueError, KeyError):
            continue
        if W == 0:
            continue
        x0 = a0 / W
        if x0 > 0.05:
            large_rows.append((W, a0, K, Tf))
        else:
            small_rows.append((W, a0, K, Tf))

    # large crack groups: fixed (K_Ii, a0), varying W
    groups_large = {}
    for W, a0, K, Tf in large_rows:
        key = (round(K, 4), round(a0, 6))
        groups_large.setdefault(key, []).append((W, Tf))

    large_good = 0
    for key, rows in groups_large.items():
        if len(rows) < 2:
            continue
        ratios = [Tf/W for W,Tf in rows if W != 0]
        if len(ratios) < 2:
            continue
        arr = np.array(ratios)
        mean_val = np.mean(arr)
        if mean_val == 0:
            cv = 1.0
        else:
            cv = np.std(arr) / mean_val
        if cv < 0.01:
            large_good += 1

    # small crack groups: fixed (K_Ii, W), varying a0
    groups_small = {}
    for W, a0, K, Tf in small_rows:
        key = (round(K, 4), round(W, 6))
        groups_small.setdefault(key, []).append((a0, Tf))

    small_good = 0
    for key, rows in groups_small.items():
        if len(rows) < 2:
            continue
        ratios = [Tf/a0 for a0,Tf in rows if a0 != 0]
        if len(ratios) < 2:
            continue
        arr = np.array(ratios)
        mean_val = np.mean(arr)
        if mean_val == 0:
            cv = 1.0
        else:
            cv = np.std(arr) / mean_val
        if cv < 0.01:
            small_good += 1

    total_groups = len(groups_large) + len(groups_small)
    if total_groups == 0:
        return 0.0
    return (large_good + small_good) / total_groups


_SCORERS = {
    'step_compute_i': score_0,
    'step_verify_scaling': score_1,
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
