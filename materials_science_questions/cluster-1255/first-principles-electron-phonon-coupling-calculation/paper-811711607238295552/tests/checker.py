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
    return {}


# === block: score_0 (check id='phonon_check') ===
def score_0(artifact, step, ctx):
    data = artifact.get('pressure_0GPa', {})
    q_min = data.get('q_minimum', [0,0,0])
    gold = step['params']['gold']
    q_tol = gold['q_tol']
    max_dev = max(abs(q_min[i]-gold['q_min'][i]) for i in range(3))
    q_score = max(0.0, 1.0 - max_dev/q_tol) if q_tol>0 else 1.0
    freq = data.get('imaginary_frequency', 0.0)
    freq_tol = gold['freq_tol']
    ref_freq = gold['freq_ref']
    freq_score = 0.0
    if freq < 0:
        ref_mag = abs(ref_freq)
        err = abs(abs(freq) - ref_mag)
        freq_score = max(0.0, 1.0 - err/(freq_tol*ref_mag)) if freq_tol*ref_mag>0 else 1.0
    smear = data.get('critical_smearing_width', None)
    smear_score = 0.0
    if smear is not None and abs(smear - gold['crit_smear_ref']) <= gold['crit_smear_tol']:
        smear_score = 1.0
    score = (q_score + freq_score + smear_score) / 3.0
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='ccdw_check') ===
def score_1(artifact, step, ctx):
    def _score_param(reported, gold_val, tol_type, tol_value):
        if gold_val is None:
            return 0.0
        if tol_type == 'rel':
            if abs(gold_val) < 1e-9:
                return 1.0 if abs(reported) < tol_value else 0.0
            rel_err = abs(reported - gold_val) / abs(gold_val)
            return 1.0 if rel_err <= tol_value else 0.0
        else:
            return 1.0 if abs(reported - gold_val) <= tol_value else 0.0

    g = step['params']['gold']
    tol = step['params']['tolerances']
    stack_scores = []
    for stack in ['triclinic', 'hexagonal']:
        if stack not in artifact:
            stack_scores.append(0.0)
            continue
        d = artifact[stack]
        gs = g[stack]
        items = []
        items.append(_score_param(d.get('a',0), gs['a'], 'rel', tol['a_rel']))
        items.append(_score_param(d.get('c',0), gs['c'], 'rel', tol['c_rel']))
        items.append(_score_param(d.get('delta_d1',0), gs['delta_d1'], 'rel', tol['dd_rel']))
        items.append(_score_param(d.get('delta_d2',0), gs['delta_d2'], 'rel', tol['dd_rel']))
        items.append(_score_param(d.get('delta_E_mRy_per_fu',0), gs['delta_E'], 'abs', tol['E_abs']))
        stack_scores.append(sum(items)/len(items))
    return (stack_scores[0] + stack_scores[1]) / 2.0


# === block: score_2 (check id='highp_check') ===
def score_2(artifact, step, ctx):
    g = step['params']['gold']
    tol = step['params']['tolerances']
    press_rep = artifact.get('cdw_disappearance_pressure_GPa', None)
    press_score = 0.0
    if press_rep is not None:
        err = abs(press_rep - g['cdw_press'])
        if err <= tol['cdw_press_abs']:
            press_score = 1.0
        else:
            press_score = max(0.0, 1.0 - (err - tol['cdw_press_abs'])/tol['cdw_press_abs'])
    entries = artifact.get('pressures', [])
    rep_by_p = {}
    for e in entries:
        p = e.get('P_GPa')
        if p is not None:
            rep_by_p[p] = e
    entry_scores = []
    map_keys = [('N0_states_per_Ry_spin','N0', tol['N0_rel']),
                ('hbar_omega_log_meV','wlog', tol['wlog_rel']),
                ('hbar_omega_ave_meV','wave', tol['wave_rel']),
                ('lambda','lam', tol['lam_rel']),
                ('Tc_K','Tc', tol['Tc_rel'])]
    for ge in g['pressures']:
        p = ge['P']
        rep = rep_by_p.get(p)
        if rep is None:
            entry_scores.append(0.0)
            continue
        s = 0.0
        n = 0
        for art_key, gold_key, rel_tol in map_keys:
            rep_val = rep.get(art_key)
            gold_val = ge[gold_key]
            if rep_val is None:
                continue
            if abs(gold_val) < 1e-9:
                item_score = 1.0 if abs(rep_val - gold_val) <= 0.01 else 0.0
            else:
                err_rel = abs(rep_val - gold_val) / abs(gold_val)
                item_score = max(0.0, 1.0 - err_rel/(2*rel_tol))
            s += item_score
            n += 1
        entry_scores.append(s/n if n else 0.0)
    entry_avg = sum(entry_scores)/len(entry_scores) if entry_scores else 0.0
    return press_score*0.2 + entry_avg*0.8


_SCORERS = {
    'phonon_check': score_0,
    'ccdw_check': score_1,
    'highp_check': score_2,
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
