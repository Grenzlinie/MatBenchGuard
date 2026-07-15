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
    return {}


# === block: score_0 (check id='step_01_dz_hcl') ===
def score_0(artifact, step, ctx):
    # Structural checks for dZ_HCl.csv
    rows = artifact
    if not rows:
        return 0.0
    required_ids = set(range(1,12))
    ids_present = set()
    temp_set = {1000.0,1200.0,1400.0}
    data = {}
    for r in rows:
        rid = int(r.get('reaction_id', -1))
        T = float(r.get('T_K', -1))
        dZ = float(r.get('dZ_kJ_per_mol', 0))
        if rid not in required_ids or T not in temp_set:
            continue
        ids_present.add(rid)
        data[(rid,T)] = dZ
    if ids_present != required_ids or len(data)!=33:
        return 0.0
    # sign: all dZ <= 0.5
    sign_score = 1.0
    for dz in data.values():
        if dz > 0.5:
            sign_score -= 1.0/33.0
    sign_score = max(0.0, sign_score)
    # monotonic increase with T for each reaction
    mono_score = 0.0
    n_good = 0
    for rid in required_ids:
        dZ1000 = data.get((rid,1000.0))
        dZ1200 = data.get((rid,1200.0))
        dZ1400 = data.get((rid,1400.0))
        if dZ1000 is None or dZ1200 is None or dZ1400 is None:
            continue
        if dZ1400 >= dZ1200 - 1e-3 and dZ1200 >= dZ1000 - 1e-3:
            n_good += 1
    mono_score = n_good / 11.0
    # inter-group ordering
    groups = {
        'Cr': [1,2,3],
        'Fe': [4,5,6],
        'Ni': [7],
        'Si': [8,9],
        'Al': [10,11]
    }
    def median(lst):
        sl = sorted(lst)
        n = len(sl)
        if n==0: return None
        mid = n//2
        if n%2: return sl[mid]
        else: return (sl[mid-1]+sl[mid])/2.0
    group_order = ['Cr','Fe','Ni','Si','Al']
    order_score = 0.0
    n_orders = 0
    for T in [1000.0,1200.0,1400.0]:
        medians = {}
        for gname, ids in groups.items():
            vals = [data.get((rid,T)) for rid in ids if data.get((rid,T)) is not None]
            if not vals:
                medians[gname] = None
            else:
                medians[gname] = median(vals)
        ok = True
        for i in range(len(group_order)-1):
            g1 = group_order[i]
            g2 = group_order[i+1]
            m1 = medians.get(g1)
            m2 = medians.get(g2)
            if m1 is None or m2 is None:
                ok=False; break
            if not (m1 <= m2 + 1.0):  # small slack
                ok=False; break
        if ok:
            n_orders += 1
    order_score = n_orders / 3.0
    score = (sign_score + mono_score + order_score) / 3.0
    return score


# === block: score_1 (check id='step_02_dz_hf') ===
def score_1(artifact, step, ctx):
    # Structural checks for dZ_HF.csv (same logic as HCl)
    rows = artifact
    if not rows:
        return 0.0
    required_ids = set(range(1,12))
    ids_present = set()
    temp_set = {1000.0,1200.0,1400.0}
    data = {}
    for r in rows:
        rid = int(r.get('reaction_id', -1))
        T = float(r.get('T_K', -1))
        dZ = float(r.get('dZ_kJ_per_mol', 0))
        if rid not in required_ids or T not in temp_set:
            continue
        ids_present.add(rid)
        data[(rid,T)] = dZ
    if ids_present != required_ids or len(data)!=33:
        return 0.0
    sign_score = 1.0
    for dz in data.values():
        if dz > 0.5:
            sign_score -= 1.0/33.0
    sign_score = max(0.0, sign_score)
    mono_score = 0.0
    n_good = 0
    for rid in required_ids:
        dZ1000 = data.get((rid,1000.0))
        dZ1200 = data.get((rid,1200.0))
        dZ1400 = data.get((rid,1400.0))
        if dZ1000 is None or dZ1200 is None or dZ1400 is None:
            continue
        if dZ1400 >= dZ1200 - 1e-3 and dZ1200 >= dZ1000 - 1e-3:
            n_good += 1
    mono_score = n_good / 11.0
    groups = {
        'Cr': [1,2,3],
        'Fe': [4,5,6],
        'Ni': [7],
        'Si': [8,9],
        'Al': [10,11]
    }
    def median(lst):
        sl = sorted(lst)
        n = len(sl)
        if n==0: return None
        mid = n//2
        if n%2: return sl[mid]
        else: return (sl[mid-1]+sl[mid])/2.0
    group_order = ['Cr','Fe','Ni','Si','Al']
    order_score = 0.0
    n_orders = 0
    for T in [1000.0,1200.0,1400.0]:
        medians = {}
        for gname, ids in groups.items():
            vals = [data.get((rid,T)) for rid in ids if data.get((rid,T)) is not None]
            if not vals:
                medians[gname] = None
            else:
                medians[gname] = median(vals)
        ok = True
        for i in range(len(group_order)-1):
            g1 = group_order[i]
            g2 = group_order[i+1]
            m1 = medians.get(g1)
            m2 = medians.get(g2)
            if m1 is None or m2 is None:
                ok=False; break
            if not (m1 <= m2 + 2.0):  # looser slack for fluorides
                ok=False; break
        if ok:
            n_orders += 1
    order_score = n_orders / 3.0
    score = (sign_score + mono_score + order_score) / 3.0
    return score


# === block: score_2 (check id='step_03_dz_nonstandard') ===
def score_2(artifact, step, ctx):
    # Structural checks for dZ_nonstandard.csv
    rows = artifact
    if not rows:
        return 0.0
    expected_T = {815.0,1300.0,1500.0}
    expected_HCl = {5.0,20.0,50.0}
    data = {}
    for r in rows:
        rid = int(r.get('reaction_id', -1))
        if rid != 1:
            continue
        T = float(r.get('T_C', -1))
        HCl = float(r.get('HCl_pct', -1))
        dZ = float(r.get('dZ_kJ_per_mol', 0))
        if T not in expected_T or HCl not in expected_HCl:
            continue
        data[(T,HCl)] = dZ
    if len(data) != 9:
        return 0.0
    # sign: all negative
    neg_score = 1.0
    for dz in data.values():
        if dz > 0.5:
            neg_score -= 1.0/9.0
    neg_score = max(0.0, neg_score)
    # monotonic with T within each HCl concentration
    T_order_score = 0.0
    n_ok = 0
    for HCl in [5.0,20.0,50.0]:
        dz815 = data.get((815.0,HCl))
        dz1300 = data.get((1300.0,HCl))
        dz1500 = data.get((1500.0,HCl))
        if dz815 is None or dz1300 is None or dz1500 is None:
            continue
        if dz1500 >= dz1300 - 1e-3 and dz1300 >= dz815 - 1e-3:
            n_ok += 1
    T_order_score = n_ok / 3.0
    # monotonic with HCl concentration: for each T, dZ(5%) < dZ(20%) < dZ(50%)
    HCl_order_score = 0.0
    n_ok2 = 0
    for T in [815.0,1300.0,1500.0]:
        dz5 = data.get((T,5.0))
        dz20 = data.get((T,20.0))
        dz50 = data.get((T,50.0))
        if dz5 is None or dz20 is None or dz50 is None:
            continue
        if dz50 >= dz20 - 1e-3 and dz20 >= dz5 - 1e-3:
            n_ok2 += 1
    HCl_order_score = n_ok2 / 3.0
    score = (neg_score + T_order_score + HCl_order_score) / 3.0
    return score


_SCORERS = {
    'step_01_dz_hcl': score_0,
    'step_02_dz_hf': score_1,
    'step_03_dz_nonstandard': score_2,
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
