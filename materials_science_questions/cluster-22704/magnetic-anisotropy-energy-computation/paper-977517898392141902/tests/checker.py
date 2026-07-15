import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    def prepare(output_dir, spec):
        gold = {}
        for step in spec.get('steps', []):
            gold[step['id']] = step.get('gold', {})
        return {'gold': gold}


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['gold']['step_03']
        score = 0.0
        if 'bandgap_GGA_U_eV' in artifact and abs(artifact['bandgap_GGA_U_eV'] - gold['bandgap_GGA_U_eV']) <= gold['tol_bandgap_GGA']:
            score += 0.25
        if 'bandgap_HSE06_eV' in artifact and abs(artifact['bandgap_HSE06_eV'] - gold['bandgap_HSE06_eV']) <= gold['tol_bandgap_HSE06']:
            score += 0.25
        if artifact.get('VBM_location','').lower().replace(' ','') == gold['VBM_location'].lower().replace(' ',''):
            score += 0.1
        if artifact.get('CBM_location','').lower().replace(' ','') == gold['CBM_location'].lower().replace(' ',''):
            score += 0.1
        if artifact.get('spin_polarized') == gold['spin_polarized']:
            score += 0.15
        if artifact.get('is_indirect') == gold['is_indirect']:
            score += 0.15
        return min(1.0, score)


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['gold']['step_04']
        s = 0.0
        if 'MAE_microeV' in artifact and abs(artifact['MAE_microeV'] - gold['MAE_microeV']) <= gold['tol_MAE']:
            s += 0.6
        if 'easy_axis' in artifact and len(artifact['easy_axis'])==3:
            dot = sum(a*b for a,b in zip(artifact['easy_axis'], gold['easy_axis']))
            norm_a = math.sqrt(sum(x*x for x in artifact['easy_axis']))
            norm_b = math.sqrt(sum(x*x for x in gold['easy_axis']))
            cos = dot/(norm_a*norm_b) if norm_a*norm_b>0 else 0.0
            if cos > 0.999:
                s += 0.3
        if artifact.get('is_out_of_plane') == gold['is_out_of_plane']:
            s += 0.1
        return min(1.0, s)


# === block: score_2 (check id='step_05') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['gold']['step_05']
        tol = gold['tol_rel']
        params = ['J1_meV','J2_meV','D_meV','lambda1_meV','lambda2_meV']
        total = 0.0
        for p in params:
            if p in artifact:
                diff = abs(artifact[p] - gold[p])
                if abs(gold[p]) > 1e-9:
                    if diff/abs(gold[p]) <= tol:
                        total += 1.0
                else:
                    if diff <= 1e-6:
                        total += 1.0
        return total / len(params)


# === block: score_3 (check id='step_06') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['gold']['step_06']
        s = 0.0
        if 'Tc_K' in artifact:
            diff = abs(artifact['Tc_K'] - gold['Tc_K'])
            if diff <= gold['tol_Tc']:
                s += 0.9
            else:
                score_k = max(0.0, 1.0 - (diff - gold['tol_Tc'])/(gold['tol_Tc']))
                s += 0.9 * score_k
        if artifact.get('Tc_range_K','') == gold['Tc_range']:
            s += 0.1
        return min(1.0, s)


# === block: score_4 (check id='step_07') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['gold']['step_07']
        strain_score = 0.0
        n = len(gold['strain_percent'])
        for i in range(n):
            mae_ok = 0
            if i < len(artifact.get('MAE_microeV',[])):
                if abs(artifact['MAE_microeV'][i] - gold['MAE_microeV'][i]) <= gold['tol_MAE']:
                    mae_ok = 1
            axis_ok = 0
            if i < len(artifact.get('easy_axis',[])):
                art_ax = artifact['easy_axis'][i]
                gold_ax = gold['easy_axis'][i]
                if len(art_ax)==3 and len(gold_ax)==3:
                    dot = sum(a*b for a,b in zip(art_ax, gold_ax))
                    na = math.sqrt(sum(x*x for x in art_ax))
                    nb = math.sqrt(sum(x*x for x in gold_ax))
                    if na*nb>0 and dot/(na*nb) > 0.999:
                        axis_ok = 1
            strain_score += 0.5*mae_ok + 0.5*axis_ok
        strain_score /= n
        threshold_ok = 0
        if artifact.get('strain_switch_threshold') == gold['strain_switch_threshold']:
            threshold_ok = 1
        return strain_score * 0.8 + threshold_ok * 0.2


_SCORERS = {
    'step_03': score_0,
    'step_04': score_1,
    'step_05': score_2,
    'step_06': score_3,
    'step_07': score_4,
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
