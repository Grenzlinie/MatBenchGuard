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


# === block: score_0 (check id='check_formation') ===
def score_0(artifact, step, ctx):
        if artifact is None or len(artifact) == 0:
            return 0.0
        rows = artifact
        data = {}
        for r in rows:
            sys = r.get('system', '').strip()
            try:
                E = float(r.get('E_form_eV', ''))
            except:
                continue
            li = r.get('Li_number', '').strip()
            data[sys] = {'E': E, 'Li': li if li != '' else None}
        # sub-scores
        existence_score = 0.05 if len(data) > 0 else 0.0
        if existence_score == 0:
            return 0.0

        # all positive
        all_pos = all(v['E'] > 0 for v in data.values())
        pos_score = 0.1 if all_pos else 0.0

        # identify key systems
        bulk_perfect = None
        bulk_Mn_vac = None
        surf_perfect = None
        surf_Mn_vac = None
        surf_perfect_Li = {}
        surf_Mn_vac_Li = {}

        for sys, vals in data.items():
            s = sys.lower()
            if 'bulk' in s:
                if 'mn_vac' in s:
                    bulk_Mn_vac = vals['E']
                elif 'perfect' in s or 'perf' in s:
                    bulk_perfect = vals['E']
            elif 'surf' in s:
                if 'mn_vac' in s:
                    li_str = vals.get('Li')
                    if li_str is not None:
                        try:
                            li_num = int(li_str)
                            surf_Mn_vac_Li[li_num] = vals['E']
                        except:
                            if 'li' not in s:
                                surf_Mn_vac = vals['E']
                    else:
                        if 'li' not in s:
                            surf_Mn_vac = vals['E']
                elif 'perfect' in s or 'perf' in s:
                    li_str = vals.get('Li')
                    if li_str is not None:
                        try:
                            li_num = int(li_str)
                            surf_perfect_Li[li_num] = vals['E']
                        except:
                            if 'li' not in s:
                                surf_perfect = vals['E']
                    else:
                        if 'li' not in s:
                            surf_perfect = vals['E']

        # bulk trend: E(bulk_Mn_vac) < E(bulk_perfect)
        bulk_score = 0.0
        if bulk_perfect is not None and bulk_Mn_vac is not None:
            if bulk_Mn_vac < bulk_perfect:
                bulk_score = 0.2

        # surface trend (non-Li): E(surf_Mn_vac) < E(surf_perfect)
        surf_simple_score = 0.0
        if surf_perfect is not None and surf_Mn_vac is not None:
            if surf_Mn_vac < surf_perfect:
                surf_simple_score = 0.15

        # Li series: defect < perfect for each common Li number
        li_defect_lt_perfect_score = 0.0
        common_li = set(surf_perfect_Li.keys()) & set(surf_Mn_vac_Li.keys())
        if common_li:
            if all(surf_Mn_vac_Li[li] < surf_perfect_Li[li] for li in common_li):
                li_defect_lt_perfect_score = 0.2

        # non-monotonic defect Li series
        nonmono_score = 0.0
        li_vals = surf_Mn_vac_Li
        if len(li_vals) >= 3:
            li_sorted = sorted(li_vals.items())
            E_list = [e for _, e in li_sorted]
            min_E = min(E_list)
            first = E_list[0]
            last = E_list[-1]
            strictly_inc = all(E_list[i] < E_list[i+1] for i in range(len(E_list)-1))
            strictly_dec = all(E_list[i] > E_list[i+1] for i in range(len(E_list)-1))
            if not (strictly_inc or strictly_dec) and min_E < first and min_E < last:
                nonmono_score = 0.3
            elif min_E < first and min_E < last:
                nonmono_score = 0.15  # partial valley

        total = existence_score + pos_score + bulk_score + surf_simple_score + li_defect_lt_perfect_score + nonmono_score
        return min(total, 1.0)


# === block: score_1 (check id='check_adsorption') ===
def score_1(artifact, step, ctx):
        if artifact is None or len(artifact) == 0:
            return 0.0
        rows = artifact
        data = []
        for r in rows:
            st = r.get('surface_type', '').strip()
            ad = r.get('adsorbate', '').strip()
            try:
                E = float(r.get('E_ads_eV', ''))
            except:
                continue
            data.append({'surface': st, 'ads': ad, 'E': E})
        if len(data) == 0:
            return 0.0
        existence_score = 0.05

        # all negative
        all_neg = all(d['E'] < 0 for d in data)
        neg_score = 0.1 if all_neg else 0.0

        # helper to get energy for a surface+adsorbate
        def get_E(surf, ads):
            for d in data:
                if d['surface'].lower().replace(' ', '') == surf.lower().replace(' ', '') and d['ads'].lower() == ads.lower():
                    return d['E']
            return None

        # O3 trends
        E_O3_perfect = get_E('perfect', 'O3')
        E_O3_VO = get_E('V_O_only', 'O3')
        E_O3_VO_VMn = get_E('V_O+V_Mn', 'O3')
        E_O3_VO_VMn_Li = get_E('V_O+V_Mn+Li', 'O3')

        trend_O3_VO = 0.0
        if E_O3_perfect is not None and E_O3_VO is not None:
            if E_O3_VO < E_O3_perfect:  # more negative
                trend_O3_VO = 0.25

        trend_O3_VMn = 0.0
        if E_O3_VO is not None and E_O3_VO_VMn is not None:
            if E_O3_VO_VMn > E_O3_VO:  # less negative
                trend_O3_VMn = 0.25

        trend_O3_Li = 0.0
        if E_O3_VO_VMn is not None and E_O3_VO_VMn_Li is not None:
            if E_O3_VO_VMn_Li < E_O3_VO_VMn:  # more negative again
                trend_O3_Li = 0.25

        # H2O/O2 weaker than O3 on the Li-containing surface
        E_H2O_Li = get_E('V_O+V_Mn+Li', 'H2O')
        E_O2_Li = get_E('V_O+V_Mn+Li', 'O2')
        weak_H2O_O2 = 0.0
        if E_O3_VO_VMn_Li is not None:
            ok = True
            if E_H2O_Li is not None and not (E_H2O_Li > E_O3_VO_VMn_Li):
                ok = False
            if E_O2_Li is not None and not (E_O2_Li > E_O3_VO_VMn_Li):
                ok = False
            if ok and (E_H2O_Li is not None or E_O2_Li is not None):
                weak_H2O_O2 = 0.1

        total = existence_score + neg_score + trend_O3_VO + trend_O3_VMn + trend_O3_Li + weak_H2O_O2
        return min(total, 1.0)


_SCORERS = {
    'check_formation': score_0,
    'check_adsorption': score_1,
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
