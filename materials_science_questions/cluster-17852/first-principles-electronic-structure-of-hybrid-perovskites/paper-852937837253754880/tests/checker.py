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
    gold_tau = None
    for s in spec.get('steps', []):
        if s['id'] == 'reference_tau':
            gold_tau = s.get('gold_tau', [])
            break
    return {'gold_tau': gold_tau}


# === block: score_0 (check id='consistency_binding') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    consistent = 0
    total = 0
    for row in rows:
        try:
            e_ls = float(row['E_LHP_Spiro'])
            e_l = float(row['E_LHP'])
            e_s = float(row['E_Spiro'])
            e_l_star = float(row.get('E_LHP_star', 0.0))
            e_s_star = float(row.get('E_Spiro_star', 0.0))
            eb_reported = float(row['Eb'])
            ea_reported = float(row.get('Ea', float('nan')))
            ed_spiro_reported = float(row.get('Ed_spiro', float('nan')))
            ed_lhp_reported = float(row.get('Ed_lhp', float('nan')))
            eb_calc = e_ls - e_l - e_s
            ea_calc = e_ls - e_l_star - e_s_star
            ed_spiro_calc = e_s_star - e_s
            ed_lhp_calc = e_l_star - e_l
            if (abs(eb_calc - eb_reported) < 1e-3 and
                abs(ea_calc - ea_reported) < 1e-3 and
                abs(ed_spiro_calc - ed_spiro_reported) < 1e-3 and
                abs(ed_lhp_calc - ed_lhp_reported) < 1e-3):
                consistent += 1
        except Exception:
            pass
        total += 1
    if total == 0:
        return 0.0
    return consistent / total


# === block: score_1 (check id='ordering_binding') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    eb_map = {}
    for row in rows:
        iface = row.get('interface', '')
        try:
            eb = float(row['Eb'])
            eb_map[iface] = eb
        except Exception:
            pass
    inequalities = []
    if 'MAPI_MAI' in eb_map and 'MAPI_PbI2' in eb_map:
        inequalities.append(('MAPI MAI < PbI2', eb_map['MAPI_MAI'] < eb_map['MAPI_PbI2']))
    if 'triLHP_PbX2_Cs' in eb_map and 'triLHP_PbX2' in eb_map:
        inequalities.append(('triLHP PbX2_Cs < PbX2', eb_map['triLHP_PbX2_Cs'] < eb_map['triLHP_PbX2']))
    ax_keys = ['triLHP_FAMAX', 'triLHP_CsFAMAX', 'triLHP_CsFAMAX_OCs']
    pbx_key = 'triLHP_PbX2'
    if pbx_key in eb_map:
        for ax in ax_keys:
            if ax in eb_map:
                inequalities.append((f'{pbx_key} < {ax}', eb_map[pbx_key] < eb_map[ax]))
    if 'triLHP_FAMAX' in eb_map and 'triLHP_CsFAMAX' in eb_map:
        inequalities.append(('FAMAX < CsFAMAX', eb_map['triLHP_FAMAX'] < eb_map['triLHP_CsFAMAX']))
    if 'triLHP_CsFAMAX_OCs' in eb_map and 'triLHP_CsFAMAX' in eb_map:
        inequalities.append(('CsFAMAX_OCs < CsFAMAX', eb_map['triLHP_CsFAMAX_OCs'] < eb_map['triLHP_CsFAMAX']))
    if not inequalities:
        return 0.0
    passed = sum(1 for _, ok in inequalities if ok)
    return passed / len(inequalities)


# === block: score_2 (check id='reference_tau') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    gold_tau_list = ctx.get('gold_tau', [])
    gold_dict = {}
    for g in gold_tau_list:
        key = (g.get('interface'), g.get('donor_state'))
        gold_dict[key] = float(g['tau_ps'])
    matched = 0
    total = 0
    for row in rows:
        iface = row.get('interface', '')
        donor = row.get('donor_state', '')
        try:
            tau = float(row['tau_ps'])
        except Exception:
            continue
        if tau <= 0:
            total += 1
            continue
        key = (iface, donor)
        gold = gold_dict.get(key)
        if gold is not None:
            ratio = tau / gold
            if 1.0/3.0 <= ratio <= 3.0:
                matched += 1
            total += 1
        else:
            total += 1
    if total == 0:
        return 0.0
    return matched / total


_SCORERS = {
    'consistency_binding': score_0,
    'ordering_binding': score_1,
    'reference_tau': score_2,
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
