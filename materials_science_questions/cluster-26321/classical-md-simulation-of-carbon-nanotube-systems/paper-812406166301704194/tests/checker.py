import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import os
import csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict, LeaveOneOut


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
    gold_energies = spec.get('gold_interaction_energies', [])
    descriptors = spec.get('gold_descriptors', [])
    ctx = {
        'gold_energies': gold_energies,
        'descriptors': descriptors,
    }
    return ctx


# === block: score_0 (check id='interaction_energies') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts from CSV
    step = step
    ctx = ctx

    # build mapping from CNP_name to E_int_total
    agent_map = {}
    for row in artifact:
        name = str(row.get('CNP_name', '')).strip()
        try:
            e = float(row.get('E_int_total', None))
        except (ValueError, TypeError):
            continue
        if name and not np.isnan(e):
            agent_map[name] = e

    if not agent_map:
        return 0.0

    gold_list = ctx.get('gold_energies', [])
    tol_rel = step.get('tolerance_rel', 0.15)

    required_names = [g['CNP_name'] for g in gold_list]
    all_present = all(n in agent_map for n in required_names)

    # 1. shape / all required CNPs present (0.05)
    shape_score = 0.05 if all_present else 0.0

    # 2. all E_int_total negative (0.1)
    if all_present:
        neg = all(agent_map[n] < 0 for n in required_names)
    else:
        neg = False
    neg_score = 0.1 if neg else 0.0

    # 3. ordering: fullerenes < graphene < CNTs (0.2)
    fullerene_names = required_names[:7]
    cnt_names = required_names[7:15]   # indices 7..14 (SCNT(10,0) to SCNT(16,0)@C60)
    graphene_names = ['MG', 'BG']

    if all(n in agent_map for n in fullerene_names + cnt_names + graphene_names):
        mean_full = np.mean([abs(agent_map[n]) for n in fullerene_names])
        mean_gra = np.mean([abs(agent_map[n]) for n in graphene_names])
        mean_cnt = np.mean([abs(agent_map[n]) for n in cnt_names])
        order_ok = (mean_full < mean_gra) and (mean_gra < mean_cnt)
    else:
        order_ok = False
    order_score = 0.2 if order_ok else 0.0

    # 4. reference match per CNP (0.65)
    match_count = 0
    total = len(gold_list)
    for g in gold_list:
        name = g['CNP_name']
        gold_val = g['E_int_total']
        if name in agent_map:
            agent_val = agent_map[name]
            if abs(gold_val) < 1e-12:
                match = abs(agent_val) < 1e-12
            else:
                rel_err = abs(agent_val - gold_val) / abs(gold_val)
                match = rel_err <= tol_rel
            if match:
                match_count += 1
    ref_score = 0.65 * (match_count / total) if total > 0 else 0.0

    total_score = shape_score + neg_score + order_score + ref_score
    return max(0.0, min(1.0, total_score))


# === block: score_1 (check id='qsar_models') ===
def score_1(artifact, step, ctx):
    import numpy as np
    import os
    import csv
    from sklearn.cross_decomposition import PLSRegression
    from sklearn.model_selection import cross_val_predict, LeaveOneOut

    artifact = artifact  # dict with fullerenes, cnt_graphenes, all
    step = step
    ctx = ctx

    # load interaction energies from the scored CSV
    energy_path = '/app/outputs/interaction_energies.csv'
    if not os.path.exists(energy_path):
        return 0.0

    agent_energies = {}
    with open(energy_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = str(row.get('CNP_name', '')).strip()
            try:
                e = float(row['E_int_total'])
            except (ValueError, KeyError, TypeError):
                continue
            if name:
                agent_energies[name] = e

    # load agent's own descriptors from descriptors.csv
    desc_path = '/app/outputs/descriptors.csv'
    if not os.path.exists(desc_path):
        return 0.0

    agent_desc = {}
    with open(desc_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = str(row.get('CNP_name', '')).strip()
            if not name:
                continue
            d = {}
            for key in ('Mw', 'OSA', 'Vol', 'SSA', 'SDeg'):
                val = row.get(key)
                if val is None or (isinstance(val, str) and val.strip() == ''):
                    d = None
                    break
                try:
                    d[key] = float(val)
                except (ValueError, TypeError):
                    d = None
                    break
            if d is not None:
                agent_desc[name] = d

    if not agent_desc or not agent_energies:
        return 0.0

    def regress_and_metrics(y, X):
        # OPLS via PLSRegression with n_components = number of predictors
        # (equivalent to full space, no dimensionality reduction)
        n_comp = X.shape[1] if X.ndim > 1 else 1
        reg = PLSRegression(n_components=n_comp, scale=True)
        reg.fit(X, y.reshape(-1, 1))
        y_pred = reg.predict(X).ravel()
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        if ss_tot == 0:
            return 0.0, 0.0
        r2 = 1.0 - ss_res / ss_tot
        loo = LeaveOneOut()
        y_cv = cross_val_predict(reg, X, y, cv=loo).ravel()
        press = np.sum((y - y_cv) ** 2)
        q2 = 1.0 - press / ss_tot
        return float(r2), float(q2)

    tol_abs = step.get('tolerance_abs', 0.1)

    # predefined CNP lists matching the paper's grouping
    fullerenes_names = ["C20","C36","C60","C70","C240","C20@C60","C20@C60@C240"]
    cnt_graphenes_names = ["SCNT (10,0)","SCNT (6,6)","SCNT (28,0)","DCNT (10,0)","DCNT (6,6)","TCNT (10,0)","NR (6,6)","SCNT (16,0)@C60","MG","BG"]
    all_names = fullerenes_names + cnt_graphenes_names

    models = {
        'fullerenes': {'names': fullerenes_names, 'predictors': ['SSA']},
        'cnt_graphenes': {'names': cnt_graphenes_names, 'predictors': ['OSA', 'SDeg']},
        'all': {'names': all_names, 'predictors': ['Mw', 'SDeg']}
    }

    group_scores = []
    for group_key, cfg in models.items():
        group = artifact.get(group_key, {})
        if not isinstance(group, dict):
            group_scores.append(0.0)
            continue
        agent_r2 = group.get('R2')
        agent_q2 = group.get('Q2_CUM')
        if agent_r2 is None or agent_q2 is None:
            group_scores.append(0.0)
            continue

        # extract data for this group from agent's files
        group_names = [n for n in cfg['names'] if n in agent_energies and n in agent_desc]
        if len(group_names) < 2:
            group_scores.append(0.0)
            continue

        y = np.array([agent_energies[n] for n in group_names])
        preds = cfg['predictors']
        X_list = []
        for p in preds:
            col = [agent_desc[n][p] for n in group_names]
            X_list.append(col)
        X = np.column_stack(X_list) if len(X_list) > 1 else np.array(X_list).reshape(-1, 1)

        try:
            r2_calc, q2_calc = regress_and_metrics(y, X)
        except Exception:
            group_scores.append(0.0)
            continue

        r2_ok = abs(float(agent_r2) - r2_calc) <= tol_abs
        q2_ok = abs(float(agent_q2) - q2_calc) <= tol_abs
        group_scores.append(1.0 if (r2_ok and q2_ok) else 0.0)

    if not group_scores:
        return 0.0
    score = sum(group_scores) / len(group_scores)
    return float(score)


_SCORERS = {
    'interaction_energies': score_0,
    'qsar_models': score_1,
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
