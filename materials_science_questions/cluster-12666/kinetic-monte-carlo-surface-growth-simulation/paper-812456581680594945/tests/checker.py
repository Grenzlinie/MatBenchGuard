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
    return {'steps': list(spec.get('steps', []))}


# === block: score_0 (check id='percolation') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', [])
    tol_rel = step.get('tolerance_rel', 0.05)
    correct = 0
    for g in gold:
        found = False
        for row in artifact:
            if row.get('system','') == g['system'] and row.get('method','') == g['method']:
                val = float(row.get('threshold', 0))
                gval = float(g['threshold'])
                if gval != 0:
                    err = abs(val - gval) / abs(gval)
                else:
                    err = abs(val - gval) if gval == 0 else 1.0
                if err <= tol_rel:
                    correct += 1
                found = True
                break
        if not found:
            pass
    if not gold:
        return 0.0
    return max(0.0, min(1.0, correct / len(gold)))


# === block: score_1 (check id='tortuosity') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', [])
    tol_abs = step.get('tolerance_abs', 0.15)
    correct = 0
    for g in gold:
        found = False
        for row in artifact:
            try:
                row_cube = str(row.get('cube_size',''))
                row_por = float(row.get('microporosity', -999))
            except:
                continue
            g_por = float(g['microporosity'])
            if row_cube == g['cube_size'] and abs(row_por - g_por) < 1e-12:
                val = float(row.get('inverse_tortuosity', 0))
                gval = float(g['inverse_tortuosity'])
                if abs(val - gval) <= tol_abs:
                    correct += 1
                found = True
                break
        if not found:
            pass
    if not gold:
        return 0.0
    return max(0.0, min(1.0, correct / len(gold)))


# === block: score_2 (check id='structural_params') ===
def score_2(artifact, step, ctx):
    gold = step.get('gold', [])
    tol_rel = step.get('tolerance_rel', 0.10)
    trend_req = step.get('structural_trend', {}).get('require', False)
    fields = step.get('structural_trend', {}).get('fields', ['internal_surface_area','free_energy'])
    group_key = step.get('structural_trend', {}).get('group_by', 'N0')
    # numeric accuracy
    correct = 0
    for g in gold:
        found = False
        for row in artifact:
            try:
                if int(row.get('N0',-1)) == int(g['N0']) and row.get('method','') == g['method']:
                    # check both fields
                    sa_rel_err = 0.0
                    fe_rel_err = 0.0
                    g_sa = float(g['internal_surface_area'])
                    row_sa = float(row.get('internal_surface_area', 0))
                    if g_sa != 0:
                        sa_rel_err = abs(row_sa - g_sa) / abs(g_sa)
                    else:
                        sa_rel_err = abs(row_sa - g_sa)
                    g_fe = float(g['free_energy'])
                    row_fe = float(row.get('free_energy', 0))
                    if g_fe != 0:
                        fe_rel_err = abs(row_fe - g_fe) / abs(g_fe)
                    else:
                        fe_rel_err = abs(row_fe - g_fe)
                    if sa_rel_err <= tol_rel and fe_rel_err <= tol_rel:
                        correct += 1
                    found = True
                    break
            except:
                continue
        if not found:
            pass
    numeric_score = correct / len(gold) if gold else 0.0
    # trend check
    if trend_req:
        groups = {}
        for row in artifact:
            try:
                n0 = int(row.get('N0',-1))
                meth = row.get('method','')
                sa = float(row.get('internal_surface_area',0))
                fe = float(row.get('free_energy',0))
            except:
                continue
            if n0 not in groups:
                groups[n0] = {}
            groups[n0][meth] = {'sa': sa, 'fe': fe}
        trend_count = 0
        for n0 in groups:
            if 'thermo' in groups[n0] and 'random' in groups[n0]:
                t = groups[n0]['thermo']
                r = groups[n0]['random']
                ok = True
                for f in fields:
                    if f in t and f in r:
                        if t[f] >= r[f]:
                            ok = False
                            break
                    else:
                        ok = False
                        break
                if ok:
                    trend_count += 1
        trend_score = trend_count / len(groups) if groups else 0.0
    else:
        trend_score = 1.0

    final = 0.7 * numeric_score + 0.3 * trend_score
    return max(0.0, min(1.0, final))


_SCORERS = {
    'percolation': score_0,
    'tortuosity': score_1,
    'structural_params': score_2,
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
