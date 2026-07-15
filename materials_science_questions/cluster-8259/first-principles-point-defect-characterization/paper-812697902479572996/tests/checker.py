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
    spec = locals().get('spec', {})
    gold = spec.get('gold', {})
    gold_reactions = gold.get('reaction_energies', [])
    gold_thermo = gold.get('thermo_levels', {})
    tolerances = gold.get('tolerances', {})
    thermo_tol = tolerances.get('thermo_eV', 0.2)
    react_tol = tolerances.get('reaction_eV', 0.3)
    return {
        'gold_reactions': gold_reactions,
        'gold_thermo': gold_thermo,
        'thermo_tol': thermo_tol,
        'react_tol': react_tol
    }


# === block: score_0 (check id='structure_check') ===
def score_0(artifact, step, ctx):
    import json
    try:
        if not isinstance(artifact, dict):
            return 0.0
        te = artifact.get('total_energies')
        re = artifact.get('reaction_energies')
        tl = artifact.get('thermodynamic_levels')
        if not isinstance(te, dict) or not isinstance(re, list) or not isinstance(tl, list):
            return 0.0
        required_te_keys = [
            'SiO2_bulk', 'VO', 'NO', 'O2', 'H',
            'S2_-1', 'S2_0', 'S2_+1',
            'S3_-1', 'S3_0', 'S3_+1',
            'S2O_-1', 'S2O_0', 'S2O_+1',
            'V2_-1', 'V2_0', 'V2_+1',
            'V3_-1', 'V3_0', 'V3_+1',
            'S2H_0', 'S2H_+1',
            'S3H_0', 'S3H_+1',
            'V2H_0', 'V2H_+2',
            'V3H_0', 'V3H_+1',
            'S2OH_0', 'S2OH_+1'
        ]
        present = sum(1 for k in required_te_keys if k in te and isinstance(te[k], (int, float)))
        return present / len(required_te_keys) if required_te_keys else 1.0
    except Exception:
        return 0.0


# === block: score_1 (check id='reaction_energies_check') ===
def score_1(artifact, step, ctx):
    te = artifact.get('total_energies', {})
    if not isinstance(te, dict):
        return 0.0
    try:
        e_sio2 = float(te.get('SiO2_bulk', float('nan')))
        e_vo = float(te.get('VO', float('nan')))
        e_no = float(te.get('NO', float('nan')))
        e_o2 = float(te.get('O2', float('nan')))
        e_s2_m1 = float(te.get('S2_-1', float('nan')))
        e_s3_m1 = float(te.get('S3_-1', float('nan')))
        e_s2o_m1 = float(te.get('S2O_-1', float('nan')))
        e_v2_m1 = float(te.get('V2_-1', float('nan')))
        e_v3_0 = float(te.get('V3_0', float('nan')))
        if any(math.isnan(v) for v in [e_sio2, e_vo, e_no, e_o2, e_s2_m1, e_s3_m1, e_s2o_m1, e_v2_m1, e_v3_0]):
            return 0.0
        computed = []
        computed.append(('NO + SiO2 -> O2 + S2', e_s2_m1 + e_o2 - e_sio2 - e_no))
        computed.append(('NO + SiO2 -> O2 + S3', e_s3_m1 + e_o2 - e_sio2 - e_no))
        computed.append(('NO + SiO2 -> 0.5 O2 + S2O', e_s2o_m1 + 0.5*e_o2 - e_sio2 - e_no))
        computed.append(('NO + VO -> O2 + V2', e_v2_m1 + e_o2 - e_vo - e_no))
        computed.append(('NO + VO -> O2 + V3', e_v3_0 + e_o2 - e_vo - e_no))
        computed.append(('NO + VO -> S2O', e_s2o_m1 - e_vo - e_no))
        computed.append(('NO + VO -> 0.5 O2 + S2', e_s2_m1 + 0.5*e_o2 - e_vo - e_no))
        gold_list = ctx.get('gold_reactions', [])
        gold_map = {gr['reaction']: gr['energy_eV'] for gr in gold_list if 'reaction' in gr}
        tol = ctx.get('react_tol', 0.3)
        scores = []
        for name, val in computed:
            gold_val = gold_map.get(name, None)
            if gold_val is None:
                continue
            diff = abs(val - gold_val)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff - tol) / tol))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    except Exception:
        return 0.0


# === block: score_2 (check id='thermo_levels_check') ===
def score_2(artifact, step, ctx):
    te = artifact.get('total_energies', {})
    if not isinstance(te, dict):
        return 0.0
    try:
        # Define transitions: (struct, transition, key_low_charge, key_high_charge, formula_type)
        # formula_type: 'simple' for Q->Q+1, 'half' for 0/++ (mu = (E0 - E2)/2)
        transitions = [
            ('S2', '0/+', 'S2_0', 'S2_+1', 'simple'),
            ('S2', '-/0', 'S2_-1', 'S2_0', 'simple'),
            ('S3', '0/+', 'S3_0', 'S3_+1', 'simple'),
            ('S3', '-/0', 'S3_-1', 'S3_0', 'simple'),
            ('V2', '0/+', 'V2_0', 'V2_+1', 'simple'),
            ('V2', '-/0', 'V2_-1', 'V2_0', 'simple'),
            ('V3', '0/+', 'V3_0', 'V3_+1', 'simple'),
            ('V3', '-/0', 'V3_-1', 'V3_0', 'simple'),
            ('S2O', '0/+', 'S2O_0', 'S2O_+1', 'simple'),
            ('S2O', '-/0', 'S2O_-1', 'S2O_0', 'simple'),
            ('S2H', '0/+', 'S2H_0', 'S2H_+1', 'simple'),
            ('S3H', '0/+', 'S3H_0', 'S3H_+1', 'simple'),
            ('V2H', '0/++', 'V2H_0', 'V2H_+2', 'half'),
            ('V3H', '0/+', 'V3H_0', 'V3H_+1', 'simple'),
            ('S2OH', '0/+', 'S2OH_0', 'S2OH_+1', 'simple')
        ]
        raw_mu_th = {}
        for struct, trans, k_low, k_high, ftype in transitions:
            e_low = float(te.get(k_low, float('nan')))
            e_high = float(te.get(k_high, float('nan')))
            if math.isnan(e_low) or math.isnan(e_high):
                continue
            if ftype == 'simple':
                raw = e_low - e_high
            else:  # half
                raw = (e_low - e_high) / 2.0
            raw_mu_th[(struct, trans)] = raw
        # alignment using S2 0/+ with gold -3.8
        s2_ref = raw_mu_th.get(('S2', '0/+'), None)
        if s2_ref is None:
            return 0.0
        shift = -3.8 - s2_ref
        gold_thermo = ctx.get('gold_thermo', {})
        tol = ctx.get('thermo_tol', 0.2)
        scores = []
        for struct, trans in raw_mu_th:
            gold_val = gold_thermo.get(struct, {}).get(trans)
            if gold_val is None:
                continue
            aligned = raw_mu_th[(struct, trans)] + shift
            diff = abs(aligned - gold_val)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff - tol) / tol))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    except Exception:
        return 0.0


# === block: score_3 (check id='h_terminated_gap_check') ===
def score_3(artifact, step, ctx):
    tl = artifact.get('thermodynamic_levels', [])
    if not isinstance(tl, list):
        return 0.0
    h_structures = ['S2H', 'S3H', 'V2H', 'V3H', 'S2OH']
    try:
        score_fraction = 0.0
        for struct in h_structures:
            entries = [entry for entry in tl if entry.get('structure') == struct]
            if not entries:
                continue
            all_outside = True
            for e in entries:
                mu = e.get('mu_th_eV')
                if not isinstance(mu, (int, float)):
                    all_outside = False
                    break
                if abs(mu) <= 0.55:
                    all_outside = False
                    break
            if all_outside:
                score_fraction += 1.0
        return score_fraction / len(h_structures) if h_structures else 1.0
    except Exception:
        return 0.0


_SCORERS = {
    'structure_check': score_0,
    'reaction_energies_check': score_1,
    'thermo_levels_check': score_2,
    'h_terminated_gap_check': score_3,
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
