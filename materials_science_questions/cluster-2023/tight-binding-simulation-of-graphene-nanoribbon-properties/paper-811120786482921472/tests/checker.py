import os
import json
import csv

# === author imports / helpers ===
import math


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
    gold_bonds = None
    tol = 0.0
    for s in spec.get("steps", []):
        if s.get("id") == "bond_lengths":
            gold_bonds = s.get("gold")
            tol = s.get("tolerance", 0.0)
            break
    return {"gold_bonds": gold_bonds, "tolerance": tol}


# === block: score_0 (check id='bond_lengths') ===
def score_0(artifact, step, ctx):
    gold = ctx.get("gold_bonds")
    tol = ctx.get("tolerance", 0.0)
    if gold is None or not isinstance(artifact, dict):
        return 0.0
    total = 0
    correct = 0
    for config in ("A", "B", "C"):
        if config not in artifact or config not in gold:
            continue
        refs = gold[config]
        vals = artifact[config]
        if not isinstance(vals, list) or len(vals) != len(refs):
            continue
        for r, v in zip(refs, vals):
            total += 1
            if abs(v - r) <= tol:
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='transport_ndc') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    conf_names = ["Per", "A", "B", "C"]
    ok = 0
    total = 0
    for name in conf_names:
        if name not in artifact:
            continue
        d = artifact[name]
        bias = d.get("bias")
        current = d.get("current")
        if not isinstance(bias, list) or not isinstance(current, list) or len(bias) < 3 or len(current) < 3:
            continue
        try:
            target_bias = 1.0
            if target_bias not in bias:
                idx = min(range(len(bias)), key=lambda i: abs(bias[i] - target_bias))
                if abs(bias[idx] - target_bias) > 0.001:
                    continue
            else:
                idx = bias.index(target_bias)
            if idx < 1 or idx > len(bias) - 2:
                continue
            dv = bias[idx+1] - bias[idx-1]
            di = current[idx+1] - current[idx-1]
            if dv == 0:
                continue
            cond = di / dv
        except Exception:
            continue
        total += 1
        if name == "C":
            if cond >= 0:
                ok += 1
        else:
            if cond < 0:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_2 (check id='transport_current_ordering') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    conf_names = ["Per", "A", "B", "C"]
    current_at_2v = {}
    for name in conf_names:
        if name not in artifact:
            return 0.0
        d = artifact[name]
        bias = d.get("bias")
        curr = d.get("current")
        if not isinstance(bias, list) or not isinstance(curr, list) or len(bias) < 1:
            return 0.0
        target = 2.0
        if target not in bias:
            idx = min(range(len(bias)), key=lambda i: abs(bias[i] - target))
            if abs(bias[idx] - target) > 0.001:
                return 0.0
        else:
            idx = bias.index(target)
        current_at_2v[name] = curr[idx]
    c_val = current_at_2v["C"]
    others = [current_at_2v[n] for n in ["Per", "A", "B"]]
    max_others = max(others)
    return 1.0 if c_val > max_others else 0.0


_SCORERS = {
    'bond_lengths': score_0,
    'transport_ndc': score_1,
    'transport_current_ordering': score_2,
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
