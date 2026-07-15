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
    gold = spec.get('hidden_gold_clean_sigma_max', {})
    return gold


# === block: score_0 (check id='step_shape_and_integrity') ===
def score_0(artifact, step, ctx):
    def check(data):
        keys = ['Ni_clean_RGS','Ni_clean_OUL','Co_clean_RGS','Co_clean_OUL','Ni_Si_RGS','Ni_Si_OUL','Ni_Te_RGS','Ni_Te_OUL']
        for k in keys:
            if k not in data: return False
            d = data[k]
            if not isinstance(d.get('strain'), list) or not isinstance(d.get('stress'), list):
                return False
            if len(d['strain']) != len(d['stress']): return False
            if len(d['strain']) < 20: return False
            if isinstance(d.get('sigma_max'), (int, float)): pass
            else: return False
            stress = d['stress']
            if not all(isinstance(v, (int,float)) for v in stress): return False
            strain = d['strain']
            if abs(strain[0]) > 0.001: return False
            if strain[0] >= strain[-1]: return False
            if len(set(stress)) < 2: return False
            if max(stress) == stress[-1] or max(stress) == stress[0]: return False
        return True
    return 1.0 if check(artifact) else 0.0


# === block: score_1 (check id='step_clean_sigma_max') ===
def score_1(artifact, step, ctx):
    def score_one(comp, gold, min_tol, max_tol):
        if gold <= 0: return 0.0
        err = abs(comp - gold) / gold
        if err <= min_tol: return 1.0
        if err >= max_tol: return 0.0
        return 1.0 - (err - min_tol) / (max_tol - min_tol)

    ni_rgs = max(artifact['Ni_clean_RGS']['stress'])
    ni_oul = max(artifact['Ni_clean_OUL']['stress'])
    co_rgs = max(artifact['Co_clean_RGS']['stress'])
    co_oul = max(artifact['Co_clean_OUL']['stress'])
    s1 = score_one(ni_rgs, ctx['Ni_RGS'], 0.25, 0.50)
    s2 = score_one(ni_oul, ctx['Ni_OUL'], 0.30, 0.60)
    s3 = score_one(co_rgs, ctx['Co_RGS'], 0.25, 0.50)
    s4 = score_one(co_oul, ctx['Co_OUL'], 0.30, 0.60)
    return min(s1, s2, s3, s4)


# === block: score_2 (check id='step_ratio_clean') ===
def score_2(artifact, step, ctx):
    def score_ratio(r, low, low_full, high_full, high):
        if r < low or r > high: return 0.0
        if low_full <= r <= high_full: return 1.0
        if r < low_full: return (r - low) / (low_full - low)
        else: return (high - r) / (high - high_full)

    ni_rgs = max(artifact['Ni_clean_RGS']['stress'])
    ni_oul = max(artifact['Ni_clean_OUL']['stress'])
    co_rgs = max(artifact['Co_clean_RGS']['stress'])
    co_oul = max(artifact['Co_clean_OUL']['stress'])
    ratio_ni = ni_rgs / ni_oul if ni_oul else 0
    ratio_co = co_rgs / co_oul if co_oul else 0
    s_ni = score_ratio(ratio_ni, 1.5, 1.8, 2.2, 2.5)
    s_co = score_ratio(ratio_co, 1.5, 1.8, 2.2, 2.5)
    return min(s_ni, s_co)


# === block: score_3 (check id='step_ordering_oul') ===
def score_3(artifact, step, ctx):
    clean_oul = max(artifact['Ni_clean_OUL']['stress'])
    si_oul = max(artifact['Ni_Si_OUL']['stress'])
    te_oul = max(artifact['Ni_Te_OUL']['stress'])
    def score_diff_strengthen(diff, tol=0.5):
        if diff >= 0: return 1.0
        return max(0.0, 1.0 - abs(diff)/tol)
    s_si = score_diff_strengthen(si_oul - clean_oul)
    s_te = score_diff_strengthen(te_oul - clean_oul)
    return min(s_si, s_te)


# === block: score_4 (check id='step_ordering_rgs') ===
def score_4(artifact, step, ctx):
    clean_rgs = max(artifact['Ni_clean_RGS']['stress'])
    si_rgs = max(artifact['Ni_Si_RGS']['stress'])
    te_rgs = max(artifact['Ni_Te_RGS']['stress'])
    def score_diff_strengthen(diff, tol=0.5):
        if diff >= 0: return 1.0
        return max(0.0, 1.0 - abs(diff)/tol)
    def score_diff_weaken(diff, tol=0.5):
        if diff <= 0: return 1.0
        return max(0.0, 1.0 - diff/tol)
    return min(score_diff_strengthen(si_rgs - clean_rgs), score_diff_weaken(te_rgs - clean_rgs))


_SCORERS = {
    'step_shape_and_integrity': score_0,
    'step_clean_sigma_max': score_1,
    'step_ratio_clean': score_2,
    'step_ordering_oul': score_3,
    'step_ordering_rgs': score_4,
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
