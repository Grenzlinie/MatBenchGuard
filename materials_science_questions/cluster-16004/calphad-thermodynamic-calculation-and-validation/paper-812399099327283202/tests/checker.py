import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from collections import defaultdict
import math
from pycalphad import Database, equilibrium, variables as v


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


# === block: score_0 (check id='step_compute_phase_equilibria') ===
def score_0(artifact, step, ctx):
        tol = step['params']['tolerance']
        temps = step['params']['temperatures']
        if not artifact:
            return 0.0

        # parse agent points (robust against missing/None fields)
        agent = defaultdict(list)
        for row in artifact:
            try:
                T_raw = row.get('temperature')
                ph_raw = row.get('phase')
                xc_raw = row.get('x_Cu')
                xf_raw = row.get('x_Fe')
                xn_raw = row.get('x_Ni')
                if None in (T_raw, ph_raw, xc_raw, xf_raw, xn_raw):
                    continue
                try:
                    T = int(T_raw)
                    ph = str(ph_raw).strip().lower()
                    xc = float(xc_raw)
                    xf = float(xf_raw)
                    xn = float(xn_raw)
                except (ValueError, TypeError):
                    continue
                if ph not in ('liq', 'fcc'):
                    continue
                ph_key = 'LIQUID' if ph == 'liq' else 'FCC_A1'
                s = xc + xf + xn
                if s <= 0:
                    continue
                agent[(T, ph_key)].append(np.array([xc, xf, xn]) / s)
            except Exception:
                continue

        # build pycalphad database
        db = Database()
        db.add_phase('FCC_A1', model='(CU,FE,NI)1')
        db.add_phase('LIQUID', model='(CU,FE,NI)1')

        # fcc endmember reference = 0
        for elem in ['CU','FE','NI']:
            db.add_parameter(f'G(FCC_A1,{elem};0)', 1, values=[(1, 10000, [0,0,0,0,0,0,0])])

        # lattice stabilities (liquid endmember)
        def add_liquid_endmember(elem, a, b, c, d):
            coeff = [a, b, d, c, 0, 0, 0]  # standard order: a, b, c=T*ln, d=T^2
            db.add_parameter(f'G(LIQUID,{elem};0)', 1, values=[(1, 10000, coeff)])

        add_liquid_endmember('CU', 13054.1, -9.6232, 4.1756e-3, 22.03)
        add_liquid_endmember('FE', -11274.0, 163.878, 4.1756e-3, 22.03)
        add_liquid_endmember('NI', 17614.6, -10.209, 4.1756e-3, 22.03)

        # binary Redlich-Kister parameters
        def add_redlich_kister(phase, i, j, v, a, b):
            coeff = [a, b, 0, 0, 0, 0, 0]
            db.add_parameter(f'G({phase},{i},{j};{v})', 1, values=[(1, 10000, coeff)])

        # Cu-Ni
        add_redlich_kister('FCC_A1','CU','NI',0,9534.49,2.83903)
        add_redlich_kister('FCC_A1','CU','NI',1,424.255,-0.62595)
        add_redlich_kister('FCC_A1','CU','NI',2,-1812.93,2.12233)
        add_redlich_kister('LIQUID','CU','NI',0,32238.7,-11.1093)
        add_redlich_kister('LIQUID','CU','NI',1,-619.65,-1.08812)
        add_redlich_kister('LIQUID','CU','NI',2,-213.489,0.97309)
        # Fe-Ni
        add_redlich_kister('FCC_A1','FE','NI',0,-18298.8,5.14894)
        add_redlich_kister('FCC_A1','FE','NI',1,14313.6,-7.65979)
        add_redlich_kister('LIQUID','FE','NI',0,-20292.4,5.14137)
        add_redlich_kister('LIQUID','FE','NI',1,11924.4,-6.16329)
        # Cu-Fe
        add_redlich_kister('FCC_A1','CU','FE',0,48206.0,-8.44645)
        add_redlich_kister('FCC_A1','CU','FE',1,-5918.0,5.01725)
        add_redlich_kister('LIQUID','CU','FE',0,34321.3,-1.8577)
        add_redlich_kister('LIQUID','CU','FE',1,-1811.6,1.6401)
        add_redlich_kister('LIQUID','CU','FE',2,7564.6,-2.5857)
        add_redlich_kister('LIQUID','CU','FE',3,-2418.3,2.3472)

        # ternary interaction terms
        db.add_parameter('G(LIQUID,CU,FE,NI;0)', 1, values=[(1, 10000, [-45000,0,0,0,0,0,0])])
        db.add_parameter('G(FCC_A1,CU,FE,NI;0)', 1, values=[(1, 10000, [-35982,-12.0,0,0,0,0,0])])

        # compute reference boundaries
        ref = defaultdict(list)
        x_vals = np.linspace(0.0, 1.0, 21)
        for T in temps:
            for xc in x_vals:
                for xf in x_vals:
                    xn = 1.0 - xc - xf
                    if xn < -1e-8 or xn > 1.0001:
                        continue
                    try:
                        eq = equilibrium(db, ['CU','FE','NI'], ['FCC_A1','LIQUID'],
                                         {v.T: T, v.P: 101325, v.X('CU'): xc, v.X('FE'): xf, v.X('NI'): xn},
                                         verbose=False)
                        phases = eq.Phase.squeeze().values
                        NP = eq.NP.squeeze().values
                        X = eq.X.squeeze().values  # shape (components, phases)
                        for idx, ph_name in enumerate(phases):
                            if NP[idx] < 1e-3:
                                continue
                            comp = X[:, idx]
                            comp_sum = comp.sum()
                            if comp_sum <= 0:
                                continue
                            ref[(T, ph_name)].append(comp / comp_sum)
                    except:
                        pass

        # evaluate match
        total_ref = sum(len(pts) for pts in ref.values())
        total_agent = sum(len(pts) for pts in agent.values())
        if total_ref == 0 and total_agent == 0:
            return 1.0
        if total_ref == 0:
            return 0.0

        recall_match = 0
        for (T, ph), ref_pts in ref.items():
            agent_pts_list = agent.get((T, ph), [])
            if len(agent_pts_list) == 0:
                continue
            agent_arr = np.array(agent_pts_list)
            for rpt in ref_pts:
                dists = np.linalg.norm(agent_arr - rpt, axis=1)
                if np.min(dists) <= tol:
                    recall_match += 1

        precision_match = 0
        for (T, ph), agent_pts in agent.items():
            ref_pts_list = ref.get((T, ph), [])
            if len(ref_pts_list) == 0:
                continue
            ref_arr = np.array(ref_pts_list)
            for apt in agent_pts:
                dists = np.linalg.norm(ref_arr - apt, axis=1)
                if np.min(dists) <= tol:
                    precision_match += 1

        recall = recall_match / total_ref if total_ref > 0 else 0.0
        precision = precision_match / total_agent if total_agent > 0 else 0.0
        return math.sqrt(recall * precision)


_SCORERS = {
    'step_compute_phase_equilibria': score_0,
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
