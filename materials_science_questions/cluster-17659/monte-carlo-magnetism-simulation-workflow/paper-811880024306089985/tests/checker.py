import os
import json
import csv


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
    required_conditions = [
        'baseline', 'k0=0.5', 'k0=1.0', 'k0=5.0',
        'H=1', 'H=2', 'H=3',
        'L_HV=0.5', 'L_HV=1.0', 'L_HV=2.0',
        'R=2', 'R=4', 'R=6',
        'K=1', 'K=2', 'K=3'
    ]
    ndr_conditions = {'L_HV=0.5', 'L_HV=1.0', 'L_HV=2.0'}
    expected_V = [i * 0.5 for i in range(0, 11)]
    k0_order = ['k0=0.5', 'k0=1.0', 'baseline', 'k0=5.0']
    H_order = ['H=3', 'H=2', 'H=1', 'baseline']
    R_order = ['R=6', 'R=4', 'R=2', 'baseline']
    K_conditions = ['K=1', 'K=2', 'K=3']
    return {
        'required_conditions': required_conditions,
        'ndr_conditions': ndr_conditions,
        'expected_V': expected_V,
        'k0_order': k0_order,
        'H_order': H_order,
        'R_order': R_order,
        'K_conditions': K_conditions
    }


# === block: score_0 (check id='mc_simulation') ===
def score_0(artifact, step, ctx):
    def monotonic_non_decreasing(values, tol=1e-9):
        for i in range(len(values)-1):
            if values[i+1] < values[i] - tol:
                return False
        return True

    def has_decrease(values, tol=1e-9):
        for i in range(len(values)-1):
            if values[i+1] < values[i] - tol:
                return True
        return False

    data = {}
    for row in artifact:
        cid = row['condition_id']
        v = float(row['V'])
        j = float(row['J'])
        occ = float(row['occupancy'])
        data.setdefault(cid, []).append((v, j, occ))

    for cid in data:
        data[cid].sort(key=lambda x: x[0])

    for cid in list(data.keys()):
        vs = [x[0] for x in data[cid]]
        js = [x[1] for x in data[cid]]
        occs = [x[2] for x in data[cid]]
        data[cid] = (vs, js, occs)

    score = 0.0

    exist = all(cid in data for cid in ctx['required_conditions'])
    score += 0.1 if exist else 0.0

    v_ok = True
    for cid in ctx['required_conditions']:
        if cid not in data: continue
        vs, _, _ = data[cid]
        if len(vs) != len(ctx['expected_V']) or any(abs(v - ev) > 1e-6 for v, ev in zip(vs, ctx['expected_V'])):
            v_ok = False
            break
    score += 0.1 if v_ok else 0.0

    ndr_set = ctx['ndr_conditions']
    mono_passes = 0
    total = 0
    for cid in ctx['required_conditions']:
        if cid not in data: continue
        _, js, _ = data[cid]
        if cid in ndr_set:
            if has_decrease(js):
                mono_passes += 1
        else:
            if monotonic_non_decreasing(js):
                mono_passes += 1
        total += 1
    mono_frac = mono_passes / total if total > 0 else 0.0
    score += 0.3 * mono_frac

    def check_ordering(vs_list, js_list, expected_increasing=True):
        n = min(len(vs) for vs in vs_list)
        total_ok = 0
        for i in range(n):
            vals = [js[i] for js in js_list]
            ok = True
            if expected_increasing:
                for a, b in zip(vals, vals[1:]):
                    if a > b + 1e-9: ok = False; break
            else:
                for a, b in zip(vals, vals[1:]):
                    if b > a + 1e-9: ok = False; break
            if ok: total_ok += 1
        return total_ok / n if n > 0 else 0.0

    k0_conds = ctx['k0_order']
    k0_data = [data[cid] for cid in k0_conds if cid in data]
    if len(k0_data) == len(k0_conds) and k0_data:
        vs_ref = k0_data[0][0]
        js_list = [d[1] for d in k0_data]
        ok = all(v == vs_ref for v,_,_ in k0_data)
        if ok:
            order_frac = check_ordering([vs_ref], js_list, expected_increasing=True)
            score += 0.1 * order_frac

    H_conds = ctx['H_order']
    H_data = [data[cid] for cid in H_conds if cid in data]
    if len(H_data) == len(H_conds) and H_data:
        vs_ref = H_data[0][0]
        js_list = [d[1] for d in H_data]
        ok = all(v == vs_ref for v,_,_ in H_data)
        if ok:
            order_frac = check_ordering([vs_ref], js_list, expected_increasing=True)
            score += 0.1 * order_frac

    R_conds = ctx['R_order']
    R_data = [data[cid] for cid in R_conds if cid in data]
    if len(R_data) == len(R_conds) and R_data:
        vs_ref = R_data[0][0]
        occs_list = [d[2] for d in R_data]
        ok = all(v == vs_ref for v,_,_ in R_data)
        if ok:
            order_frac = check_ordering([vs_ref], occs_list, expected_increasing=True)
            score += 0.1 * order_frac

    baseline_cid = 'baseline'
    K_cond_list = ctx['K_conditions']
    if baseline_cid in data and all(cid in data for cid in K_cond_list):
        vs_base, j_base, _ = data[baseline_cid]
        min_j_k = []
        for i, v in enumerate(vs_base):
            vals = []
            for cid in K_cond_list:
                vs_k, js_k, _ = data[cid]
                if i < len(vs_k) and abs(vs_k[i] - v) < 1e-6:
                    vals.append(js_k[i])
            if vals:
                min_j_k.append(min(vals))
        if min_j_k and len(min_j_k) == len(j_base):
            ok_count = sum(1 for mk, bj in zip(min_j_k, j_base) if mk > bj + 1e-9)
            score += 0.1 * (ok_count / len(j_base) if j_base else 0)

    if baseline_cid in data and all(cid in data for cid in K_cond_list):
        vs_base, _, occ_base = data[baseline_cid]
        min_occ_k = []
        for i, v in enumerate(vs_base):
            vals = []
            for cid in K_cond_list:
                vs_k, _, occs_k = data[cid]
                if i < len(vs_k) and abs(vs_k[i] - v) < 1e-6:
                    vals.append(occs_k[i])
            if vals:
                min_occ_k.append(min(vals))
        if min_occ_k and len(min_occ_k) == len(occ_base):
            ok_count = sum(1 for mk, bo in zip(min_occ_k, occ_base) if mk > bo + 1e-9)
            score += 0.1 * (ok_count / len(occ_base) if occ_base else 0)

    return score


_SCORERS = {
    'mc_simulation': score_0,
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
