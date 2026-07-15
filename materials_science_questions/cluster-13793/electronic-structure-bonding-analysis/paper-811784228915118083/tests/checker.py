import os
import json
import csv

# === author imports / helpers ===
import math, json, csv


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
    spec = json.load(open('/tests/grading_spec.json'))
    gold_lattice = spec['gold_reference']['lattice']
    gold_hardness = spec['gold_reference']['hardness']
    tol = spec['tolerances']
    return {'gold_lattice': gold_lattice, 'gold_hardness': gold_hardness, 'tol': tol}


# === block: score_0 (check id='step_lattice') ===
def score_0(artifact, step, ctx):
    rows = artifact
    tol = ctx['tol']['lattice']
    gold = ctx['gold_lattice']
    cons_tol = ctx['tol']['consistency']
    ave_tol = 0.001
    def hex_moduli(C11,C12,C13,C33,C44):
        M = C11+C12+2*C33-4*C13
        C2 = (C11+C12)*C33 - 2*C13*C13
        C66 = (C11-C12)/2.0
        BV = (2*(C11+C12)+4*C13+C33)/9.0
        BR = C2/M
        B = (BV+BR)/2.0
        GV = (M+12*C44+12*C66)/30.0
        GR = (5*C2*C44*C66)/(2*(3*BV*C44*C66+C2*(C44+C66)))
        G = (GV+GR)/2.0
        E = 9*B*G/(3*B+G)
        nu = (3*B-2*G)/(2*(3*B+G))
        return B,G,E,nu

    compounds = ['TaC','WC','ReC','OsC','IrC','PtC']
    scores = []
    for comp in compounds:
        comp_rows = [r for r in rows if r['compound'].strip()==comp]
        if not comp_rows:
            scores.append(0.0)
            continue
        xc_map = {r['xc'].strip(): r for r in comp_rows}
        for xc in ['GGA','LDA','Ave']:
            if xc not in xc_map:
                scores.append(0.0)
                break
        else:
            gga = xc_map['GGA']
            lda = xc_map['LDA']
            ave = xc_map['Ave']
            # recompute Ave from GGA+LDA
            fields = ['a0','c0','C11','C12','C13','C33','C44']
            ave_ok = True
            for f in fields:
                expected = (float(gga[f])+float(lda[f]))/2.0
                if abs(float(ave[f])-expected) > max(ave_tol, 0.005*abs(expected)):
                    ave_ok = False
                    break
            if not ave_ok:
                scores.append(0.0)
                continue
            # check GGA/LDA values against gold
            gold_comp = gold.get(comp, None)
            if gold_comp is None:
                scores.append(0.0)
                continue
            cnt=0
            tot=0
            for xc in ['GGA','LDA']:
                row = xc_map[xc]
                gold_row = gold_comp.get(xc, None)
                if gold_row is None: continue
                for f in fields:
                    tot+=1
                    if abs(float(row[f])-gold_row[f]) <= tol.get(f, 15):
                        cnt+=1
                # moduli from Cij
                C11=float(row['C11']); C12=float(row['C12']); C13=float(row['C13']); C33=float(row['C33']); C44=float(row['C44'])
                bcalc,gcalc,ecalc,nucalc = hex_moduli(C11,C12,C13,C33,C44)
                for f, vcalc, goldv in [('B',bcalc,gold_row['B']), ('G',gcalc,gold_row['G']), ('E',ecalc,gold_row['E']), ('nu',nucalc,gold_row.get('nu',0))]:
                    tot+=1
                    if abs(vcalc-goldv) <= tol.get(f, 10):
                        cnt+=1
            # Ave values against gold
            gold_ave = gold_comp.get('Ave', None)
            if gold_ave:
                for f in fields:
                    tot+=1
                    if abs(float(ave[f])-gold_ave[f]) <= tol.get(f, 15):
                        cnt+=1
                C11=float(ave['C11']); C12=float(ave['C12']); C13=float(ave['C13']); C33=float(ave['C33']); C44=float(ave['C44'])
                bcalc,gcalc,ecalc,nucalc = hex_moduli(C11,C12,C13,C33,C44)
                for f, vcalc, goldv in [('B',bcalc,gold_ave['B']), ('G',gcalc,gold_ave['G']), ('E',ecalc,gold_ave['E']), ('nu',nucalc,gold_ave.get('nu',0))]:
                    tot+=1
                    if abs(vcalc-goldv) <= tol.get(f, 10):
                        cnt+=1
            scores.append(cnt/max(1,tot))
    if not scores:
        return 0.0
    return sum(scores)/len(scores)


# === block: score_1 (check id='step_hardness') ===
def score_1(artifact, step, ctx):
    rows = artifact
    tol = ctx['tol']['hardness']
    tol_hv = ctx['tol']['Hv_calc_tol']
    gold = ctx['gold_hardness']
    compounds = ['TaC','WC','ReC','OsC','IrC','PtC']
    scores = []
    for comp in compounds:
        comp_rows = [r for r in rows if r['compound'].strip()==comp]
        if not comp_rows:
            scores.append(0.0)
            continue
        xc_map = {r['xc'].strip(): r for r in comp_rows}
        if not all(xc in xc_map for xc in ['GGA','LDA','Ave']):
            scores.append(0.0)
            continue
        gold_comp = gold.get(comp, None)
        if gold_comp is None:
            scores.append(0.0)
            continue
        row_scores = []
        for xc in ['GGA','LDA','Ave']:
            row = xc_map[xc]
            gold_row = gold_comp.get(xc, None)
            if gold_row is None:
                row_scores.append(0.0)
                continue
            try:
                V = float(row['V'])
                P = float(row['P'])
                n_free = float(row['n_free'])
            except (KeyError, ValueError):
                row_scores.append(0.0)
                continue
            v_b_calc = V/6.0
            P_prime_calc = n_free/V
            f_m_calc = P_prime_calc/P
            Hv_calc = 740 * (P - P_prime_calc) * (v_b_calc ** (-5/3))
            cnt=0; tot=0
            # internal consistency checks
            for field, calc, goldv in [('v_b',v_b_calc,gold_row['v_b']), ('P\'',P_prime_calc,gold_row['P\'']), ('f_m',f_m_calc,gold_row['f_m'])]:
                tot+=1
                try:
                    val = float(row[field])
                except (KeyError, ValueError):
                    val = None
                if val is not None and abs(val - calc) <= max(tol.get(field,0.5), 0.01*abs(calc)):
                    cnt+=1
            # Hv consistency
            tot+=1
            try:
                hv_val = float(row['H_v'])
            except (KeyError, ValueError):
                hv_val = None
            if hv_val is not None and abs(hv_val - Hv_calc) <= tol_hv:
                cnt+=1
            # gold closeness (correct column names)
            fields_gold = ['d','V','P','v_b','Ep','N(E_f)','n_free','P\'','f_m','H_v']
            for f in fields_gold:
                tot+=1
                try:
                    val = float(row[f])
                except (KeyError, ValueError):
                    val = None
                if val is None:
                    continue
                if f == 'N(E_f)':
                    gf = gold_row['N_Ef']
                elif f == 'P\'':
                    gf = gold_row['P\'']
                elif f == 'H_v':
                    gf = gold_row['H_v']
                else:
                    gf = gold_row[f]
                if abs(val - gf) <= tol.get(f, 0.5):
                    cnt+=1
            row_scores.append(cnt/max(1,tot))
        scores.append(sum(row_scores)/len(row_scores))
    if not scores:
        return 0.0
    return sum(scores)/len(scores)


_SCORERS = {
    'step_lattice': score_0,
    'step_hardness': score_1,
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
