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


# === block: score_0 (check id='ref_energies') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_fields = step.get('fields', {})
    # find bulk row
    bulk_row = next((r for r in rows if r.get('system') == 'perfect_bulk'), None)
    if bulk_row is None:
        return 0.0
    bulk_total = float(bulk_row.get('total_energy_eV', 0))
    v_row = next((r for r in rows if r.get('system') == 'V'), None)
    i_row = next((r for r in rows if r.get('system') == 'I'), None)
    score = 0.0
    n = 0
    if v_row is not None:
        form_recomputed = float(v_row['total_energy_eV']) - bulk_total
        tol = gold_fields.get('V_formation', {}).get('tolerance', 0.3)
        gold = gold_fields.get('V_formation', {}).get('gold', 3.52)
        if abs(form_recomputed - gold) <= tol:
            score += 1
        n += 1
    if i_row is not None:
        form_recomputed = float(i_row['total_energy_eV']) - bulk_total
        tol = gold_fields.get('I_formation', {}).get('tolerance', 0.3)
        gold = gold_fields.get('I_formation', {}).get('gold', 3.44)
        if abs(form_recomputed - gold) <= tol:
            score += 1
        n += 1
    # bulk formation should be 0
    if bulk_row is not None:
        # formation_energy_eV should be ~0
        declared = abs(float(bulk_row.get('formation_energy_eV', 0)))
        tol = gold_fields.get('bulk_formation', {}).get('tolerance', 0.01)
        if declared <= tol:
            score += 1
        n += 1
    if n > 0:
        return score / n
    return 0.0


# === block: score_1 (check id='fp_results') ===
def score_1(artifact, step, ctx):
    import os
    ref_rows = load_artifact(os.path.join('/app/outputs', 'reference_energies.csv'))
    if not ref_rows:
        return 0.0
    bulk_row = next((r for r in ref_rows if r.get('system') == 'perfect_bulk'), None)
    if bulk_row is None:
        return 0.0
    bulk_total = float(bulk_row['total_energy_eV'])
    v_row = next((r for r in ref_rows if r.get('system') == 'V'), None)
    i_row = next((r for r in ref_rows if r.get('system') == 'I'), None)
    if v_row is None or i_row is None:
        return 0.0
    v_total = float(v_row['total_energy_eV'])
    i_total = float(i_row['total_energy_eV'])
    v_form = v_total - bulk_total
    i_form = i_total - bulk_total
    sum_form = v_form + i_form

    fp_rows = artifact
    if not fp_rows:
        return 0.0

    cfg = step.get('cfg', {})
    f_range = cfg.get('formation_range', [5.65, 7.0])
    b_range = cfg.get('binding_range', [0.0, 1.4])

    # 1. Range checks
    n = 0
    range_pass = 0
    for row in fp_rows:
        form_e = float(row['total_energy_eV']) - bulk_total
        bind_e = sum_form - form_e
        n += 1
        if f_range[0] <= form_e <= f_range[1] and b_range[0] <= bind_e <= b_range[1]:
            range_pass += 1
    range_score = range_pass / n if n else 0.0

    # 2. Charge-state trend (formation non-decreasing, binding non-increasing, stability non-increasing)
    stable_order = {'stable': 3, 'partially_recombined': 2, 'unstable': 1}
    from collections import defaultdict
    configs = defaultdict(list)
    for row in fp_rows:
        cid = row['config_id']
        chg = int(row['charge_state'])
        form = float(row['total_energy_eV']) - bulk_total
        bind = sum_form - form
        stab = row.get('stability', 'unstable')
        so = stable_order.get(stab, 0)
        configs[cid].append((chg, form, bind, so))
    charge_ok = 0
    n_configs = len(configs)
    if n_configs:
        for cg in configs.values():
            # sort descending +2,0,-2
            cg_sorted = sorted(cg, key=lambda x: -x[0])
            ok = True
            for i in range(1, len(cg_sorted)):
                if cg_sorted[i][1] < cg_sorted[i-1][1] - 1e-6:  # formation not decreasing
                    ok = False
                if cg_sorted[i][2] > cg_sorted[i-1][2] + 1e-6:  # binding not increasing
                    ok = False
                if cg_sorted[i][3] > cg_sorted[i-1][3]:  # stability not increasing
                    ok = False
            if ok:
                charge_ok += 1
    charge_score = charge_ok / n_configs

    # 3. Separation trend (binding non-increasing with separation for each charge state)
    charge_sep = defaultdict(list)
    for row in fp_rows:
        chg = int(row['charge_state'])
        sep = float(row['separation_A'])
        bind = sum_form - (float(row['total_energy_eV']) - bulk_total)
        charge_sep[chg].append((sep, bind))
    sep_score = 0.0
    total_pairs = 0
    for lst in charge_sep.values():
        lst_sorted = sorted(lst, key=lambda x: x[0])
        for i in range(len(lst_sorted)-1):
            total_pairs += 1
            if lst_sorted[i+1][1] <= lst_sorted[i][1] + 1e-6:
                sep_score += 1
    if total_pairs:
        sep_score /= total_pairs
    else:
        sep_score = 1.0

    return (range_score + charge_score + sep_score) / 3.0


_SCORERS = {
    'ref_energies': score_0,
    'fp_results': score_1,
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
