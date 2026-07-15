import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    gold_table = []
    for step in spec['steps']:
        if step['id'] == 'compare_charge_table':
            gold_table = step['config']['gold_table']
            break
    gold_map = {}
    for g in gold_table:
        key = (g['material'].strip().lower(), float(g['epsilon']), float(g['eta']))
        gold_map[key] = g
    ctx = {'gold_map': gold_map}
    return ctx


# === block: score_0 (check id='compare_charge_table') ===
def score_0(artifact, step, ctx):
    gold_map = ctx['gold_map']
    avg_charge_tol = float(step['config'].get('avg_charge_tol', 0.2))
    rel_tol = float(step['config'].get('surface_charge_density_rel_tol', 0.2))
    abs_min = float(step['config'].get('surface_charge_density_abs_min', 1e-10))
    rows = artifact

    # --- build agent row lookup ---
    agent_map = {}
    for r in rows:
        try:
            mat = r['material'].strip().lower()
            eps = float(r['epsilon'])
            eta = float(r['eta'])
        except (ValueError, KeyError):
            continue
        agent_map[(mat, eps, eta)] = r

    # --- per-row value scores ---
    row_scores = []
    for key, gold in gold_map.items():
        match = agent_map.get(key)
        if match is None:
            row_scores.append(0.0)
            continue
        try:
            avg_val = float(match['avg_charge'])
            surf_val = float(match['surface_charge_density'])
        except (ValueError, KeyError):
            row_scores.append(0.0)
            continue
        gold_avg = float(gold['avg_charge'])
        gold_surf = float(gold['surface_charge_density'])
        # avg_charge
        diff = abs(avg_val - gold_avg)
        if diff <= avg_charge_tol:
            avg_score = 1.0
        else:
            avg_score = max(0.0, 1.0 - (diff - avg_charge_tol) / avg_charge_tol)
        # surface charge density
        ref = max(abs(gold_surf), abs_min)
        rel_err = abs(surf_val - gold_surf) / ref
        if rel_err <= rel_tol:
            surf_score = 1.0
        else:
            surf_score = max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol)
        row_scores.append((avg_score + surf_score) / 2.0)

    if not row_scores:
        return 0.0
    value_score = sum(row_scores) / len(row_scores)

    # --- trend audit (corrected) ---
    # group gold entries by (material, epsilon)
    gold_groups = {}
    for key, g in gold_map.items():
        gk = (key[0], key[1])   # (mat, eps)
        gold_groups.setdefault(gk, []).append((key[2], g))

    trend_pass = True
    for gk, items in gold_groups.items():
        items.sort(key=lambda x: x[0])   # sort by eta
        for i in range(len(items)-1):
            eta1, g1 = items[i]
            eta2, g2 = items[i+1]
            key1 = (gk[0], gk[1], eta1)
            key2 = (gk[0], gk[1], eta2)
            r1 = agent_map.get(key1)
            r2 = agent_map.get(key2)
            if r1 is None or r2 is None:
                trend_pass = False
                break
            try:
                avg1 = float(r1['avg_charge'])
                surf1 = float(r1['surface_charge_density'])
                avg2 = float(r2['avg_charge'])
                surf2 = float(r2['surface_charge_density'])
            except (ValueError, KeyError):
                trend_pass = False
                break
            gold_avg1 = float(g1['avg_charge'])
            gold_surf1 = float(g1['surface_charge_density'])
            gold_avg2 = float(g2['avg_charge'])
            gold_surf2 = float(g2['surface_charge_density'])
            # avg_charge direction check
            d_gold_avg = gold_avg2 - gold_avg1
            d_agent_avg = avg2 - avg1
            if abs(d_gold_avg) > 1e-4:
                if d_gold_avg > 0 and d_agent_avg < -1e-4:
                    trend_pass = False
                elif d_gold_avg < 0 and d_agent_avg > 1e-4:
                    trend_pass = False
            # surface_charge_density direction check
            d_gold_surf = gold_surf2 - gold_surf1
            d_agent_surf = surf2 - surf1
            if abs(d_gold_surf) > 1e-8:
                if d_gold_surf > 0 and d_agent_surf < -1e-8:
                    trend_pass = False
                elif d_gold_surf < 0 and d_agent_surf > 1e-8:
                    trend_pass = False
            if not trend_pass:
                break
        if not trend_pass:
            break

    trend_score = 1.0 if trend_pass else 0.0

    # combine value (0.9) and trend (0.1) into a single reward
    return value_score * 0.9 + trend_score * 0.1


# === block: score_1 (check id='trend_audit') ===
def score_1(artifact, step, ctx):
    constraints = step['config'].get('constraints', [])
    rows = artifact
    if not rows:
        return 0.0
    # group by material, epsilon
    grouped = {}
    for r in rows:
        try:
            mat = r['material'].strip().lower()
            eps = float(r['epsilon'])
            eta = float(r['eta'])
        except (ValueError, KeyError):
            continue
        grouped.setdefault((mat, eps), []).append((eta, r))
    for key in grouped:
        grouped[key].sort(key=lambda x: x[0])  # sort by eta
    all_ok = True
    for c in constraints:
        mat = c['material'].strip().lower()
        eps = float(c['epsilon'])
        field = c['field']
        direction = c['direction']
        key = (mat, eps)
        if key not in grouped:
            all_ok = False
            break
        vals = []
        for eta, r in grouped[key]:
            try:
                vals.append(float(r[field]))
            except (ValueError, KeyError):
                vals.append(None)
        if None in vals:
            all_ok = False
            break
        if len(vals) < 2:
            continue
        ok = True
        for i in range(len(vals)-1):
            diff = vals[i+1] - vals[i]
            if direction == 'non_decreasing':
                if diff < 0:
                    ok = False
                    break
            elif direction == 'non_increasing':
                if diff > 0:
                    ok = False
                    break
            else:
                ok = False
                break
        if not ok:
            all_ok = False
            break
    return 1.0 if all_ok else 0.0


_SCORERS = {
    'compare_charge_table': score_0,
    'trend_audit': score_1,
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
