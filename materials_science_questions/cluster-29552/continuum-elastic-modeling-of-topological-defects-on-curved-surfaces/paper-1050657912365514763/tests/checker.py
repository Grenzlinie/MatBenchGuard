import os
import json
import csv

# === author imports / helpers ===
import csv, json, math
from collections import defaultdict

def compute_invariants(rows, gold):
    groups = defaultdict(list)
    for r in rows:
        groups[(r['model'], r['origin'])].append(r)
    result = {}
    for (model, origin), recs in groups.items():
        # cylinder
        cyl_recs = [r for r in recs if r.get('geometry') == 'cylinder' and str(r.get('L_y','')).strip().isdigit()]
        cyl_recs.sort(key=lambda r: int(r['L_y']))
        P_y = None
        if cyl_recs:
            L_y_list = [int(r['L_y']) for r in cyl_recs]
            Q_mod_list = []
            nu = gold[model]['nu']
            C = gold[model]['C']
            for r in cyl_recs:
                Q_W = float(r['Q_W'])
                n_W = float(r['n_W'])
                dPhi = float(r.get('delta_Phi_W', 0.0))
                Q_mod = (Q_W - nu * n_W - C * dPhi / (2 * math.pi)) % 1.0
                Q_mod_list.append(Q_mod)
            n = len(L_y_list)
            if n == 1:
                P_y = 0.0
            elif n == 2:
                dy = Q_mod_list[1] - Q_mod_list[0]
                dx = L_y_list[1] - L_y_list[0]
                P_y = dy / dx
            else:
                sum_x = sum_y = sum_xy = sum_xx = 0.0
                for x, y in zip(L_y_list, Q_mod_list):
                    sum_x += x
                    sum_y += y
                    sum_xy += x * y
                    sum_xx += x * x
                denom = n * sum_xx - sum_x * sum_x
                if abs(denom) < 1e-15:
                    P_y = 0.0
                else:
                    P_y = (n * sum_xy - sum_x * sum_y) / denom
            P_y = P_y % 1.0
        # ribbon
        rib_recs = [r for r in recs if r.get('geometry') == 'ribbon']
        delta_o = None
        if rib_recs:
            r = rib_recs[0]
            Q_W = float(r['Q_W'])
            n_W = float(r['n_W'])
            dPhi = float(r.get('delta_Phi_W', 0.0))
            Q_mod = (Q_W - gold[model]['nu'] * n_W - gold[model]['C'] * dPhi / (2 * math.pi)) % 1.0
            delta_o = (-4.0 * Q_mod) % 4.0
        result[(model, origin)] = {'P_y': P_y, 'delta_o': delta_o}
    return result


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
    return {'gold': spec['gold_invariants']}


# === block: score_0 (check id='invariants_from_csv') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0
    gold = ctx['gold']
    computed = compute_invariants(rows, gold)
    model_origins = [('hofstadter','alpha'), ('hofstadter','beta'), ('quadrupole','alpha'), ('quadrupole','beta')]
    tol_P = step.get('params',{}).get('tolerance_P', 0.02)
    tol_delta = step.get('params',{}).get('tolerance_delta', 0.05)
    sub_scores = []
    for m, orig in model_origins:
        comp = computed.get((m, orig), {})
        P_comp = comp.get('P_y')
        delta_comp = comp.get('delta_o')
        P_gold = gold[m]['P_'+orig]
        delta_gold = gold[m]['delta_'+orig]
        def score_val(val, target, tol):
            if val is None:
                return 0.0
            diff = abs(val - target)
            if diff <= tol:
                return 1.0
            return max(0.0, 1.0 - (diff - tol) / (5 * tol))
        s_p = score_val(P_comp, P_gold, tol_P)
        s_d = score_val(delta_comp, delta_gold, tol_delta)
        sub_scores.append(0.5 * (s_p + s_d))
    return sum(sub_scores) / len(sub_scores) if sub_scores else 0.0


# === block: score_1 (check id='invariants_consistency') ===
def score_1(artifact, step, ctx):
    # Recompute P_y and delta_o from charge_data.csv using robust difference/corner methods
    import csv, math
    csv_path = '/app/outputs/charge_data.csv'
    rows = []
    try:
        with open(csv_path, newline='') as f:
            rows = list(csv.DictReader(f))
    except Exception:
        return 0.0

    from collections import defaultdict

    gold = ctx['gold']
    model_origins = [('hofstadter','alpha'), ('hofstadter','beta'), ('quadrupole','alpha'), ('quadrupole','beta')]

    # compute invariants for each model/origin pair
    def compute_for_pair(rows, model, origin):
        # filter rows
        rows_cyl = [r for r in rows if r.get('model')==model and r.get('origin')==origin and r.get('geometry')=='cylinder' and r.get('L_y','').strip().isdigit()]
        rows_cyl.sort(key=lambda r: int(r['L_y']))
        P_y = None
        if rows_cyl:
            L_y_list = [int(r['L_y']) for r in rows_cyl]
            Q_mod_list = []
            nu = gold[model]['nu']
            C = gold[model]['C']
            for r in rows_cyl:
                Q_W = float(r['Q_W'])
                n_W = float(r['n_W'])
                dPhi = float(r.get('delta_Phi_W', 0.0))
                Q_mod = (Q_W - nu * n_W - C * dPhi / (2 * math.pi)) % 1
                Q_mod_list.append(Q_mod)
            # Use difference between consecutive L_y values; if single L_y set P=0
            if len(L_y_list) >= 2:
                # assume consecutive L_y differ by 1; compute slope from the first pair
                slope = (Q_mod_list[1] - Q_mod_list[0]) % 1
                P_y = slope if slope <= 0.5 else slope - 1.0   # map to [-0.5, 0.5] then mod 1
                P_y = P_y % 1.0
            else:
                P_y = 0.0
        # ribbon
        rows_rib = [r for r in rows if r.get('model')==model and r.get('origin')==origin and r.get('geometry')=='ribbon']
        delta_o = None
        if rows_rib:
            r = rows_rib[0]
            Q_W = float(r['Q_W'])
            n_W = float(r['n_W'])
            dPhi = float(r.get('delta_Phi_W', 0.0))
            Q_mod = (Q_W - gold[model]['nu'] * n_W - gold[model]['C'] * dPhi / (2 * math.pi)) % 1
            # corner angle Omega_cor = -pi/2; delta_o contribution: Q_mod = delta_o * Omega_cor/(2pi) mod 1 => delta_o = -4 * Q_mod mod 4
            delta_o = (-4.0 * Q_mod) % 4
        return P_y, delta_o

    tol_P = step.get('params',{}).get('tolerance_P', 0.02)
    tol_delta = step.get('params',{}).get('tolerance_delta', 0.05)
    sub_scores = []
    for model, origin in model_origins:
        P_comp, delta_comp = compute_for_pair(rows, model, origin)
        if P_comp is None or delta_comp is None:
            sub_scores.append(0.0)
            continue
        P_gold = gold[model]['P_'+origin]
        delta_gold = gold[model]['delta_'+origin]
        def score_val(val, target, tol):
            diff = abs(val - target)
            if diff <= tol:
                return 1.0
            return max(0.0, 1.0 - (diff - tol) / (5 * tol))
        s_p = score_val(P_comp, P_gold, tol_P)
        s_d = score_val(delta_comp, delta_gold, tol_delta)
        sub_scores.append(0.5 * (s_p + s_d))
    return sum(sub_scores) / len(sub_scores) if sub_scores else 0.0


_SCORERS = {
    'invariants_from_csv': score_0,
    'invariants_consistency': score_1,
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
