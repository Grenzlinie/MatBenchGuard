import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, sys, math

try:
    from pycalphad import Database, equilibrium, variables as v
    import pycalphad
except ImportError:
    # Verifier sandbox lacks pycalphad; provide dummy stubs so the checker
    # can still load and run the thermo_params scorer.  The phase_boundaries
    # scorer will gracefully return 0 when it receives a non‑functional db.
    class _FakeDatabase:
        @staticmethod
        def from_string(s):
            return _FakeResult()
    class _FakeResult:
        def __init__(self):
            self.phase = []
            self.X = _FakeX()
    class _FakeX:
        def __init__(self):
            pass
        @property
        def values(self):
            return []
    Database = _FakeDatabase
    equilibrium = None
    v = None
    pycalphad = None


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
        # load agent thermodynamic parameters
        params_path = os.path.join(outputs_dir, 'thermodynamic_parameters.json')
        with open(params_path) as f:
            agent_params = json.load(f)
        # extract gold references from grading spec (needed regardless of database availability)
        gold_boundaries = spec['steps'][1]['reference_boundaries']
        # if pycalphad is not available, return a context with db=None so that the
        # thermo_params scorer can still run while phase_boundaries will safely score 0
        if pycalphad is None or equilibrium is None:
            return {
                'db': None,
                'gold_boundaries': gold_boundaries,
                'consistency_tol': spec['steps'][1].get('consistency_tolerance_at_frac', 0.01),
                'gold_tol': spec['steps'][1].get('gold_tolerance_at_frac', 0.015),
                'penalty': spec['steps'][1].get('consistency_penalty', 0.5)
            }
        # locate pycalphad elements database
        elements_path = os.path.join(os.path.dirname(pycalphad.__file__), 'elements.dat')
        with open(elements_path) as f:
            elements_tdb = f.read()
        # build TDB snippet from agent parameters
        lines = ["System Ni-Os", ""]
        # Liquid
        l_L0 = agent_params['Liquid']['L0']
        a_l, b_l = l_L0[0], l_L0[1]
        if b_l == 0:
            param_str_l = str(a_l)
        else:
            param_str_l = f"{a_l} + {b_l}*T"
        lines.append(f"Parameter L(LIQUID,NI,OS;0) 298.15 {param_str_l}; 6000 N !")
        # Fcc
        f_L0 = agent_params['Fcc']['L0']
        a_f, b_f = f_L0[0], f_L0[1]
        lines.append(f"Parameter L(FCC_A1,NI,OS;0) 298.15 {a_f} + {b_f}*T; 6000 N !")
        tc = agent_params['Fcc']['Tc_interaction']
        if isinstance(tc, list):
            tc = tc[0]
        lines.append(f"Parameter TC(FCC_A1,NI,OS;0) 298.15 {tc}; 6000 N !")
        beta = agent_params['Fcc']['beta_interaction']
        if isinstance(beta, list):
            beta = beta[0]
        lines.append(f"Parameter BMAGN(FCC_A1,NI,OS;0) 298.15 {beta}; 6000 N !")
        # Hcp
        h_L0 = agent_params['Hcp']['L0']
        a_h, b_h = h_L0[0], h_L0[1]
        lines.append(f"Parameter L(HCP_A3,NI,OS;0) 298.15 {a_h} + {b_h}*T; 6000 N !")
        system_tdb = "\n".join(lines)
        full_tdb = elements_tdb + "\n" + system_tdb
        # build pycalphad Database
        db = Database.from_string(full_tdb)
        return {
            'db': db,
            'gold_boundaries': gold_boundaries,
            'consistency_tol': spec['steps'][1].get('consistency_tolerance_at_frac', 0.01),
            'gold_tol': spec['steps'][1].get('gold_tolerance_at_frac', 0.015),
            'penalty': spec['steps'][1].get('consistency_penalty', 0.5)
        }


# === block: score_0 (check id='thermo_params') ===
def score_0(artifact, step, ctx):
        gold = step['reference']
        tolerances = step['tolerances']
        def score_param(val, gval, tol):
            diff = abs(val - gval)
            if diff <= tol:
                return 1.0
            return max(0.0, 1.0 - (diff - tol) / tol)
        scores = []
        # Liquid L0
        al = artifact['Liquid']['L0']; gl = gold['Liquid']['L0']
        scores.append(score_param(al[0], gl[0], tolerances['L0_a']))
        scores.append(score_param(al[1], gl[1], tolerances['L0_b']))
        # Fcc L0
        af = artifact['Fcc']['L0']; gf = gold['Fcc']['L0']
        scores.append(score_param(af[0], gf[0], tolerances['L0_a']))
        scores.append(score_param(af[1], gf[1], tolerances['L0_b']))
        # Tc
        atc = artifact['Fcc']['Tc_interaction']
        if isinstance(atc, list):
            atc = atc[0]
        gtc = gold['Fcc']['Tc_interaction'][0]
        scores.append(score_param(atc, gtc, tolerances['Tc_interaction']))
        # beta
        abeta = artifact['Fcc']['beta_interaction']
        if isinstance(abeta, list):
            abeta = abeta[0]
        gbeta = gold['Fcc']['beta_interaction'][0]
        scores.append(score_param(abeta, gbeta, tolerances['beta_interaction']))
        # Hcp L0
        ah = artifact['Hcp']['L0']; gh = gold['Hcp']['L0']
        scores.append(score_param(ah[0], gh[0], tolerances['L0_a']))
        scores.append(score_param(ah[1], gh[1], tolerances['L0_b']))
        return sum(scores) / len(scores)


# === block: score_1 (check id='phase_boundaries') ===
def score_1(artifact, step, ctx):
        db = ctx['db']
        gold = ctx['gold_boundaries']
        consistency_tol = ctx['consistency_tol']
        gold_tol = ctx['gold_tol']
        penalty = ctx['penalty']
        # recompute equilibrium compositions from agent's database
        recomputed = {}
        for entry in gold:
            T = entry['temperature_K']
            phase = entry['phase']
            if phase == 'liquid':
                x_os_overall = 0.3
                result = equilibrium(db, ['NI', 'OS'], 'LIQUID,FCC_A1,HCP_A3',
                                     {v.T: T, v.P: 101325, v.N: 1, v.X('OS'): x_os_overall})
                try:
                    liq_idx = result.phase.values.tolist().index('LIQUID')
                except ValueError:
                    # fallback: assume liquid not stable; set to None
                    recomputed[(T, phase)] = None
                    continue
                # Os mole fraction (second component, index 1)
                liq_comp = result.X.values[0, liq_idx, 1]
                recomputed[(T, phase)] = liq_comp
            else:
                # fcc or hcp solvus
                x_os_overall = 0.4
                result = equilibrium(db, ['NI', 'OS'], 'FCC_A1,HCP_A3',
                                     {v.T: T, v.P: 101325, v.N: 1, v.X('OS'): x_os_overall})
                if phase == 'fcc_solvus':
                    try:
                        idx = result.phase.values.tolist().index('FCC_A1')
                    except ValueError:
                        recomputed[(T, phase)] = None
                        continue
                else:  # hcp_solvus
                    try:
                        idx = result.phase.values.tolist().index('HCP_A3')
                    except ValueError:
                        recomputed[(T, phase)] = None
                        continue
                comp = result.X.values[0, idx, 1]
                recomputed[(T, phase)] = comp
        # score against gold (ignore None)
        deviations = []
        for entry in gold:
            key = (entry['temperature_K'], entry['phase'])
            if recomputed.get(key) is not None:
                deviations.append(abs(recomputed[key] - entry['composition_Os_at_frac']))
        if not deviations:
            recompute_score = 0.0
        else:
            max_dev = max(deviations)
            if max_dev <= gold_tol:
                recompute_score = 1.0
            else:
                recompute_score = max(0.0, 1.0 - (max_dev - gold_tol) / gold_tol)
        # consistency with submitted CSV
        matched = 0
        csv_dev = 0.0
        for entry in gold:
            target_phase = entry['phase']
            target_T = entry['temperature_K']
            key = (target_T, target_phase)
            rec_val = recomputed.get(key)
            if rec_val is None:
                continue
            found = None
            for row in artifact:
                # safeguard: convert keys/values
                rphase = str(row.get('phase', '')).strip()
                rtemp = float(row.get('temperature_K', 0.0))
                if rphase == target_phase and abs(rtemp - target_T) < 1e-3:
                    found = float(row.get('composition_Os_at_frac', 0.0))
                    break
            if found is not None:
                csv_dev = max(csv_dev, abs(found - rec_val))
                matched += 1
        if matched < len(gold) or csv_dev > consistency_tol:
            consistency_factor = penalty
        else:
            consistency_factor = 1.0
        return recompute_score * consistency_factor


_SCORERS = {
    'thermo_params': score_0,
    'phase_boundaries': score_1,
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
