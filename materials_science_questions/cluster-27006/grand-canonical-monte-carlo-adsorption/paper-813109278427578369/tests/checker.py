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


# === block: score_0 (check id='check_binding_energies') ===
def score_0(artifact, step, ctx):
    import csv, io
    ref = step.get('reference', {})
    tol = step.get('tolerance', 1.5)
    if not isinstance(artifact, list) or len(artifact) < 4:
        return 0.0
    vals = {}
    for row in artifact:
        site = row.get('site', '').strip()
        try:
            e = float(row['E_ads_kJmol'])
        except:
            continue
        vals[site] = e
    all_sites = ['hollow', 'ligand', 'metal_side_on', 'metal_end_on']
    if not all(s in vals for s in all_sites):
        return 0.0
    val_score = 0.0
    count = 0
    for s in all_sites:
        expected = ref.get(s)
        if expected is None:
            continue
        diff = abs(vals[s] - expected)
        if diff <= tol:
            val_score += 1.0
        else:
            val_score += max(0.0, 1.0 - (diff - tol) / (tol * 2))
        count += 1
    if count == 0:
        return 0.0
    val_score /= count
    order_correct = (vals['hollow'] <= vals['ligand'] <= vals['metal_side_on'] <= vals['metal_end_on'])
    order_score = 1.0 if order_correct else 0.0
    return 0.7 * val_score + 0.3 * order_score


# === block: score_1 (check id='check_isotherms_77K') ===
def score_1(artifact, step, ctx):
    tol_exc = step.get('tolerance_exc', 0.5)
    tol_abs = step.get('tolerance_abs', 0.5)
    ref_points = step.get('reference_points', [])
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    agent_data = {}
    for row in artifact:
        try:
            p = float(row['pressure_bar'])
            exc = float(row['exc_wt'])
            abs_ = float(row['abs_wt'])
            agent_data[p] = (exc, abs_)
        except:
            continue
    if not agent_data:
        return 0.0
    total_score = 0.0
    n = 0
    for rp in ref_points:
        p = float(rp['pressure_bar'])
        if p not in agent_data:
            continue
        ex, ab = agent_data[p]
        ref_ex = float(rp['exc_wt'])
        ref_ab = float(rp['abs_wt'])
        diff_ex = abs(ex - ref_ex)
        diff_ab = abs(ab - ref_ab)
        sc_ex = 1.0 if diff_ex <= tol_exc else max(0.0, 1.0 - (diff_ex - tol_exc) / tol_exc)
        sc_ab = 1.0 if diff_ab <= tol_abs else max(0.0, 1.0 - (diff_ab - tol_abs) / tol_abs)
        total_score += (sc_ex + sc_ab) / 2.0
        n += 1
    if n == 0:
        return 0.0
    return total_score / n


# === block: score_2 (check id='check_isotherms_298K') ===
def score_2(artifact, step, ctx):
    tol_exc = step.get('tolerance_exc', 0.1)
    tol_abs = step.get('tolerance_abs', 0.1)
    ref_points = step.get('reference_points', [])
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    agent_data = {}
    for row in artifact:
        try:
            p = float(row['pressure_bar'])
            exc = float(row['exc_wt'])
            abs_ = float(row['abs_wt'])
            agent_data[p] = (exc, abs_)
        except:
            continue
    if not agent_data:
        return 0.0
    total_score = 0.0
    n = 0
    for rp in ref_points:
        p = float(rp['pressure_bar'])
        if p not in agent_data:
            continue
        ex, ab = agent_data[p]
        ref_ex = float(rp['exc_wt'])
        ref_ab = float(rp['abs_wt'])
        diff_ex = abs(ex - ref_ex)
        diff_ab = abs(ab - ref_ab)
        sc_ex = 1.0 if diff_ex <= tol_exc else max(0.0, 1.0 - (diff_ex - tol_exc) / tol_exc)
        sc_ab = 1.0 if diff_ab <= tol_abs else max(0.0, 1.0 - (diff_ab - tol_abs) / tol_abs)
        total_score += (sc_ex + sc_ab) / 2.0
        n += 1
    if n == 0:
        return 0.0
    return total_score / n


# === block: score_3 (check id='check_electrostatic_contrib') ===
def score_3(artifact, step, ctx):
    ref_rows = step.get('reference_rows', [])
    tol_val = step.get('tolerance_val', 0.1)
    tol_pct = step.get('tolerance_pct', 3.0)
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    agent_data = {}
    for row in artifact:
        try:
            p = float(row['pressure_bar'])
            agent_data[p] = {
                'LJplusCoulomb': float(row['abs_wt_LJplusCoulomb']),
                'LJonly': float(row['abs_wt_LJonly']),
                'coulomb_wt': float(row['coulomb_wt']),
                'pct': float(row['electrostatic_pct'])
            }
        except:
            continue
    if not agent_data:
        return 0.0
    total_val_score = 0.0
    n = 0
    for r in ref_rows:
        p = float(r['pressure_bar'])
        if p not in agent_data:
            continue
        ad = agent_data[p]
        diffs = [
            abs(ad['LJplusCoulomb'] - float(r['abs_wt_LJplusCoulomb'])),
            abs(ad['LJonly'] - float(r['abs_wt_LJonly'])),
            abs(ad['coulomb_wt'] - float(r['coulomb_wt'])),
            abs(ad['pct'] - float(r['electrostatic_pct']))
        ]
        sc = 0.0
        for i, diff in enumerate(diffs):
            tol = tol_pct if i == 3 else tol_val
            if diff <= tol:
                sc += 1.0
            else:
                sc += max(0.0, 1.0 - (diff - tol) / tol)
        sc /= 4.0
        total_val_score += sc
        n += 1
    if n == 0:
        return 0.0
    val_score = total_val_score / n
    pressures = sorted([p for p in agent_data if agent_data[p] is not None])
    if len(pressures) >= 2:
        pcts = [agent_data[p]['pct'] for p in pressures]
        decreasing = all(pcts[i] >= pcts[i+1] - 0.5 for i in range(len(pcts)-1))
        struct_score = 1.0 if decreasing else 0.0
    else:
        struct_score = 1.0
    return 0.8 * val_score + 0.2 * struct_score


_SCORERS = {
    'check_binding_energies': score_0,
    'check_isotherms_77K': score_1,
    'check_isotherms_298K': score_2,
    'check_electrostatic_contrib': score_3,
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
