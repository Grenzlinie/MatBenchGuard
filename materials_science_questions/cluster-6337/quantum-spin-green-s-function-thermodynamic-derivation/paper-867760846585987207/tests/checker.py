import os
import json
import csv

# === author imports / helpers ===
import math, json, numpy as np


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
    def ising_longitudinal_exact(n):
        # exact Ising limit connected correlation function (longitudinal) for J_I=1000, h=2, T=0.5
        # For large J_I the connected values approach +/-1
        return -1.0 if n % 2 == 0 else 1.0

    def ising_transversal_exact(n):
        return 0.0

    # expected keys
    ising_keys = ['ising_n2_longitudinal','ising_n3_longitudinal','ising_n4_longitudinal','ising_n2_transversal','ising_n3_transversal','ising_n4_transversal']
    paramagnet_keys = ['paramagnet_n2_longitudinal','paramagnet_n3_longitudinal','paramagnet_n4_longitudinal','paramagnet_n2_transversal','paramagnet_n3_transversal','paramagnet_n4_transversal']
    massive_keys = ['massive_n2_longitudinal','massive_n3_longitudinal','massive_n4_longitudinal','massive_n2_transversal','massive_n3_transversal','massive_n4_transversal']

    expected_ising = {}
    for key in ising_keys:
        parts = key.split('_')
        n = int(parts[1][1])
        typ = parts[2]
        if typ == 'longitudinal':
            expected_ising[key] = ising_longitudinal_exact(n)
        else:
            expected_ising[key] = ising_transversal_exact(n)

    ctx = {
        'expected_ising': expected_ising,
        'ising_keys': ising_keys,
        'paramagnet_keys': paramagnet_keys,
        'massive_keys': massive_keys
    }
    return ctx


# === block: score_0 (check id='ising_exact') ===
def score_0(artifact, step, ctx):
    data = artifact
    ctx = ctx
    ising_keys = ctx['ising_keys']
    expected = ctx['expected_ising']
    score_sum = 0.0
    nkeys = len(ising_keys)
    for key in ising_keys:
        if key not in data:
            continue
        val = float(data[key])
        target = expected[key]
        if abs(val - target) < 0.01:
            score_sum += 1.0
        else:
            # allow partial if close
            diff = abs(val - target)
            score_sum += max(0.0, 1.0 - diff/0.1)
    return score_sum / nkeys if nkeys > 0 else 0.0


# === block: score_1 (check id='paramagnet_exact') ===
def score_1(artifact, step, ctx):
    data = artifact
    keys = ctx['paramagnet_keys']
    score_sum = 0.0
    nkeys = len(keys)
    for key in keys:
        if key not in data:
            continue
        val = float(data[key])
        if abs(val) < 1e-6:
            score_sum += 1.0
        else:
            score_sum += max(0.0, 1.0 - abs(val)/1e-4)
    return score_sum / nkeys if nkeys > 0 else 0.0


# === block: score_2 (check id='massive_structure') ===
def score_2(artifact, step, ctx):
    data = artifact
    keys = ctx['massive_keys']
    long_keys = [k for k in keys if 'longitudinal' in k]
    trans_keys = [k for k in keys if 'transversal' in k]
    score = 0.0
    total = 0.0
    # all longitudinal negative
    all_neg = True
    vals_long = []
    for k in long_keys:
        if k in data:
            v = float(data[k])
            vals_long.append(v)
            if v >= 0:
                all_neg = False
    if len(vals_long) > 0 and all_neg:
        score += 0.5
        total += 0.5
    # monotonic magnitude with n (|val| non-increasing)
    monotonic = True
    for i in range(len(vals_long)-1):
        if abs(vals_long[i]) < abs(vals_long[i+1]):
            monotonic = False
            break
    if len(vals_long) >= 2 and monotonic:
        score += 0.5
        total += 0.5
    # transversal positive
    all_pos = True
    vals_trans = []
    for k in trans_keys:
        if k in data:
            v = float(data[k])
            vals_trans.append(v)
            if v <= 0:
                all_pos = False
    if len(vals_trans) > 0 and all_pos:
        score += 0.5
        total += 0.5
    # monotonic transversal magnitude
    monotonic_trans = True
    for i in range(len(vals_trans)-1):
        if abs(vals_trans[i]) < abs(vals_trans[i+1]):
            monotonic_trans = False
            break
    if len(vals_trans) >= 2 and monotonic_trans:
        score += 0.5
        total += 0.5
    return score / total if total > 0 else 0.0


_SCORERS = {
    'ising_exact': score_0,
    'paramagnet_exact': score_1,
    'massive_structure': score_2,
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
