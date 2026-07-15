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
    compound_gold = spec.get('compound_gold', {})
    return {'gold': compound_gold}


# === block: score_0 (check id='file_gate') ===
def score_0(artifact, step, ctx):
    required_cols = {'compound','d','K_computed','B_computed'}
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    for row in artifact:
        if not required_cols.issubset(row.keys()):
            return 0.0
    return 1.0


# === block: score_1 (check id='k_precision') ===
def score_1(artifact, step, ctx):
    gold = ctx.get('gold', {})
    if not gold:
        return 0.0
    mape = 0.0
    n = 0
    for row in artifact:
        compound = row.get('compound')
        if compound is None:
            continue
        ref = gold.get(compound)
        if ref is None or 'K_ref' not in ref:
            continue
        K_computed = float(row.get('K_computed', 0))
        K_ref = float(ref['K_ref'])
        if K_ref == 0:
            continue
        ape = abs((K_computed - K_ref) / K_ref)
        mape += ape
        n += 1
    if n == 0:
        return 0.0
    mape /= n
    eps = 1e-8
    if mape <= eps:
        return 1.0
    else:
        return max(0.0, 1.0 - mape / 0.001)


# === block: score_2 (check id='b_precision') ===
def score_2(artifact, step, ctx):
    gold = ctx.get('gold', {})
    if not gold:
        return 0.0
    mape = 0.0
    n = 0
    for row in artifact:
        compound = row.get('compound')
        if compound is None:
            continue
        ref = gold.get(compound)
        if ref is None or 'B_ref' not in ref:
            continue
        B_computed = float(row.get('B_computed', 0))
        B_ref = float(ref['B_ref'])
        if B_ref == 0:
            continue
        ape = abs((B_computed - B_ref) / B_ref)
        mape += ape
        n += 1
    if n == 0:
        return 0.0
    mape /= n
    eps = 1e-8
    if mape <= eps:
        return 1.0
    else:
        return max(0.0, 1.0 - mape / 0.001)


# === block: score_3 (check id='structural_check') ===
def score_3(artifact, step, ctx):
    group_ii_vi = {'ZnS','ZnSe','ZnTe','CdS','CdSe','CdTe','HgS','HgSe','HgTe'}
    group_iii_v = {'AlN','AlP','AlAs','AlSb','GaN','GaP','GaAs','GaSb','InN','InP','InAs','InSb','BN','BP','BAs','BSb','TiN','TiP','TiAs','TiSb'}

    def _compute_r(compounds):
        if len(compounds) < 3:
            return None
        d_vals = []
        k_vals = []
        for d,k in compounds:
            if d <= 0 or k <= 0:
                return None
            d_vals.append(d)
            k_vals.append(k)
        log_d = [math.log10(d) for d in d_vals]
        log_k = [math.log10(k) for k in k_vals]
        n = len(log_d)
        mean_x = sum(log_d)/n
        mean_y = sum(log_k)/n
        num = sum((log_d[i]-mean_x)*(log_k[i]-mean_y) for i in range(n))
        denom_x = sum((x-mean_x)**2 for x in log_d)
        denom_y = sum((y-mean_y)**2 for y in log_k)
        if denom_x < 1e-12 or denom_y < 1e-12:
            return None
        r = num / (denom_x**0.5 * denom_y**0.5)
        return r

    pairs = []
    for row in artifact:
        compound = row.get('compound')
        d = row.get('d')
        K = row.get('K_computed')
        if compound is None or d is None or K is None:
            continue
        try:
            d = float(d)
            K = float(K)
        except Exception:
            continue
        pairs.append((compound, d, K))

    ii_vi_data = [(d,k) for comp,d,k in pairs if comp in group_ii_vi]
    iii_v_data = [(d,k) for comp,d,k in pairs if comp in group_iii_v]

    r1 = _compute_r(ii_vi_data)
    r2 = _compute_r(iii_v_data)

    if (r1 is None or r1 < -0.95) and (r2 is None or r2 < -0.95):
        return 1.0
    return 0.0


_SCORERS = {
    'file_gate': score_0,
    'k_precision': score_1,
    'b_precision': score_2,
    'structural_check': score_3,
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
