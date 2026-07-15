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


# === block: score_0 (check id='ep_shape') ===
def score_0(artifact, step, ctx):
    def check_shape(artifact):
        required_cols = ['model_type','initial_d_Al_G','final_d_Al_G','Fermi_level','N2_Ef','conductivity_300K','work_function','avg_bader_charge_C','avg_bader_charge_Al']
        if not artifact or not isinstance(artifact, list):
            return 0.0
        first = artifact[0]
        for col in required_cols:
            if col not in first:
                return 0.0
        model_types = set(row.get('model_type','') for row in artifact)
        if not {'pure_Al','SL','DL'}.issubset(model_types):
            return 0.0
        pure_rows = [r for r in artifact if r.get('model_type')=='pure_Al']
        if not pure_rows:
            return 0.0
        return 1.0
    score = check_shape(artifact)
    return score


# === block: score_1 (check id='ep_trends') ===
def score_1(artifact, step, ctx):
    import math
    required_models = {'DL','SL'}
    score = 0.0
    counts = 0
    for mtype in required_models:
        rows = [r for r in artifact if r.get('model_type')==mtype and r.get('initial_d_Al_G','').strip()!='']
        if len(rows)<2:
            continue
        rows.sort(key=lambda r: float(r['initial_d_Al_G']), reverse=True)
        conds = [float(r['conductivity_300K']) for r in rows]
        fermis = [float(r['Fermi_level']) for r in rows]
        cond_mono = all(cond>=prev for prev,cond in zip(conds, conds[1:]))
        fermi_mono = all(fermi>=prev for prev,fermi in zip(fermis, fermis[1:]))
        if cond_mono and fermi_mono:
            score += 0.3
        counts += 1
    if counts>0:
        score /= counts
    pure_rows = [r for r in artifact if r.get('model_type')=='pure_Al']
    dl_shortest = [r for r in artifact if r.get('model_type')=='DL' and float(r.get('initial_d_Al_G',0))==3.00]
    if pure_rows and dl_shortest:
        pure_cond = float(pure_rows[0]['conductivity_300K'])
        dl_cond = float(dl_shortest[0]['conductivity_300K'])
        ratio = dl_cond / pure_cond if pure_cond>0 else 0
        if 1.3 <= ratio <= 1.5:
            score += 0.4
    return min(score, 1.0)


# === block: score_2 (check id='ep_gold') ===
def score_2(artifact, step, ctx):
    def score_gold(artifact, targets):
        if not targets:
            return 0.0
        sub_scores = []
        dl_row = None
        pure_row = None
        for r in artifact:
            if r.get('model_type')=='DL' and float(r.get('initial_d_Al_G',0))==3.00:
                dl_row = r
            if r.get('model_type')=='pure_Al':
                pure_row = r
        for name, spec in targets.items():
            gold = spec['value']
            tol = spec['tolerance']
            try:
                if name == 'DL_2.97_fermi' and dl_row:
                    val = float(dl_row['Fermi_level'])
                elif name == 'DL_2.97_cond' and dl_row:
                    val = float(dl_row['conductivity_300K'])
                elif name == 'pure_Al_cond' and pure_row:
                    val = float(pure_row['conductivity_300K'])
                else:
                    sub_scores.append(0.0)
                    continue
                rel_err = abs(val - gold) / gold if gold != 0 else abs(val-gold)
                if rel_err <= tol:
                    sub_scores.append(1.0)
                elif rel_err <= 2*tol:
                    sub_scores.append(1.0 - (rel_err - tol)/tol)
                else:
                    sub_scores.append(0.0)
            except:
                sub_scores.append(0.0)
        if not sub_scores:
            return 0.0
        return sum(sub_scores)/len(sub_scores)
    score = score_gold(artifact, step.get('targets',{}))


# === block: score_3 (check id='tc_shape') ===
def score_3(artifact, step, ctx):
    def check_shape(artifact):
        required = ['model_id','temperature','average_conductivity','std_conductivity']
        if not artifact or not isinstance(artifact, list):
            return 0.0
        first = artifact[0]
        for col in required:
            if col not in first:
                return 0.0
        expected_models = {'pure_Al','DL_2.97','DL_3.41','SL_3.01','SL_3.40'}
        present = {r.get('model_id') for r in artifact}
        if not expected_models.issubset(present):
            return 0.0
        return 1.0
    score = check_shape(artifact)


# === block: score_4 (check id='tc_trends') ===
def score_4(artifact, step, ctx):
    models = {
        'DL_2.97': {'peak': (300,400), 'non_monotonic': True},
        'DL_3.41': {'overall_decrease': True},
        'SL_3.01': {'overall_decrease': True},
        'SL_3.40': {'overall_decrease': True},
        'pure_Al': {'overall_decrease': True}
    }
    score = 0.0
    total = 0.0
    for mid, specs in models.items():
        rows = [r for r in artifact if r.get('model_id')==mid]
        if not rows:
            continue
        temp_cond = {}
        for r in rows:
            try:
                temp_cond[int(r['temperature'])] = float(r['average_conductivity'])
            except:
                pass
        if 'non_monotonic' in specs and specs['non_monotonic']:
            if 300 in temp_cond and 400 in temp_cond and temp_cond[400] > temp_cond[300]:
                score += 0.4
            total += 0.4
        elif specs.get('overall_decrease'):
            if 100 in temp_cond and 600 in temp_cond and temp_cond[600] < temp_cond[100]:
                score += 0.15
            total += 0.15
    if total == 0:
        score_out = 0.0
    else:
        score_out = score/total
    score = score_out


# === block: score_5 (check id='tc_gold') ===
def score_5(artifact, step, ctx):
    def score_gold(artifact, targets):
        sub_scores = []
        for name, spec in targets.items():
            gold = spec['value']
            tol = spec['tolerance']
            try:
                parts = name.rsplit('_', 1)
                mid = parts[0]
                temp = int(parts[1])
                rows = [r for r in artifact if r.get('model_id')==mid and int(r['temperature'])==temp]
                if not rows:
                    sub_scores.append(0.0)
                    continue
                val = float(rows[0]['average_conductivity'])
                rel_err = abs(val - gold) / gold
                if rel_err <= tol:
                    sub_scores.append(1.0)
                elif rel_err <= 2*tol:
                    sub_scores.append(1.0 - (rel_err - tol)/tol)
                else:
                    sub_scores.append(0.0)
            except:
                sub_scores.append(0.0)
        if not sub_scores:
            return 0.0
        return sum(sub_scores)/len(sub_scores)
    score = score_gold(artifact, step.get('targets',{}))


_SCORERS = {
    'ep_shape': score_0,
    'ep_trends': score_1,
    'ep_gold': score_2,
    'tc_shape': score_3,
    'tc_trends': score_4,
    'tc_gold': score_5,
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
