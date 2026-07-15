import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess

def _ensure_pkg(pkg_name, import_name=None):
    if import_name is None:
        import_name = pkg_name
    try:
        __import__(import_name)
    except ModuleNotFoundError:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir',
            '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', pkg_name
        ])

_ensure_pkg('numpy')
_ensure_pkg('pycalphad')

from pycalphad import Database, equilibrium, variables as v
import numpy as np
import tempfile, os, shutil, re


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
    return {"spec": spec}


# === block: score_0 (check id='rey_check') ===
def score_0(artifact, step, ctx):
    import pycalphad
    import numpy as np
    import tempfile, os, shutil
    gold = step['gold']
    content = artifact
    tmpd = tempfile.mkdtemp()
    tdb_path = os.path.join(tmpd, 'rey.tdb')
    with open(tdb_path, 'w') as f:
        f.write(content)
    try:
        db = pycalphad.Database(tdb_path)
        comps = ['RE','Y','VA']
        def eq_at(T, x_Y):
            conds = {v.N: 1, v.P: 101325, v.T: T, v.X('Y'): x_Y, v.X('RE'): 1-x_Y}
            return pycalphad.equilibrium(db, comps, sorted(conds.keys()), conds)
        eut_T = gold['eutectic_T_K']
        tol_T = gold['tol_T']
        x_Y = gold['eutectic_comp_Y']
        best_T = None
        for T in np.arange(2000, 1500-1, -10):
            eq = eq_at(T, x_Y)
            phases = eq.Phase.values
            if 'LIQUID' in phases:
                liq_idx = list(phases).index('LIQUID')
                NP_T = eq.NP.values[liq_idx]
                if np.isclose(NP_T, 1.0, rtol=1e-3):
                    best_T = T
                else:
                    break
            else:
                break
        if best_T is None:
            score_eut_T = 0.0
        else:
            score_eut_T = 1.0 if abs(best_T - eut_T) <= tol_T else 0.0
        eq = eq_at(eut_T, gold['eutectic_comp_Y'])
        phases = eq.Phase.values
        liquid_comp = None
        if 'LIQUID' in phases:
            liq_idx = list(phases).index('LIQUID')
            liquid_comp = eq.X.sel(component='Y').values[liq_idx]
        if liquid_comp is not None:
            score_eut_comp = 1.0 if abs(liquid_comp - gold['eutectic_comp_Y']) <= gold['tol_comp'] else 0.0
        else:
            score_eut_comp = 0.0
        peri_T = gold['peritectic_T_K']
        tol_T = gold['tol_T']
        x_Re2Y = 1/3
        peri_T_found = None
        for T in np.arange(3000, 2500-1, -10):
            eq = eq_at(T, x_Re2Y)
            if 'RE2Y' in eq.Phase.values:
                peri_T_found = T
                break
        if peri_T_found is None:
            score_peri_T = 0.0
        else:
            score_peri_T = 1.0 if abs(peri_T_found - peri_T) <= tol_T else 0.0
        eq = eq_at(peri_T, x_Re2Y)
        liquid_comp = None
        if 'LIQUID' in eq.Phase.values:
            liq_idx = list(eq.Phase.values).index('LIQUID')
            liquid_comp = eq.X.sel(component='Y').values[liq_idx]
        if liquid_comp is not None:
            score_peri_comp = 1.0 if abs(liquid_comp - gold['peritectic_comp_Y']) <= gold['tol_comp'] else 0.0
        else:
            score_peri_comp = 0.0
        total = (score_eut_T + score_eut_comp + score_peri_T + score_peri_comp) / 4.0
        return total
    finally:
        shutil.rmtree(tmpd)


# === block: score_1 (check id='nire_check') ===
def score_1(artifact, step, ctx):
    import re
    gold = step['gold']
    content = artifact
    tol_A = gold['tol_A']
    tol_B = gold['tol_B']
    params_found = {
        'liquid_L0': None,
        'hcp_L0': None,
        'fcc_L0': None,
        'fcc_L1': None,
        'bcc_L0': None
    }
    def extract_param(phase, order):
        pattern = rf'PARAMETER\s+G\({phase},NI,RE;{order}\)\s+\d+\.\d+\s+([^;]+)'
        m = re.search(pattern, content)
        if not m:
            return None
        expr = m.group(1).strip()
        try:
            val = float(expr)
            return (val, 0.0)
        except:
            pass
        pat = r'([-+]?\d+\.?\d*)\s*([+-])\s*([-+]?\d+\.?\d*)\s*\*T'
        m2 = re.match(pat, expr)
        if m2:
            A = float(m2.group(1))
            sign = m2.group(2)
            B = float(m2.group(3))
            if sign == '-':
                B = -B
            return (A, B)
        return None
    params_found['liquid_L0'] = extract_param('LIQUID', 0)
    params_found['hcp_L0'] = extract_param('HCP_A3', 0)
    params_found['fcc_L0'] = extract_param('FCC_A1', 0)
    params_found['fcc_L1'] = extract_param('FCC_A1', 1)
    params_found['bcc_L0'] = extract_param('BCC_A2', 0)
    def check_param(p, A_gold, B_gold):
        if p is None:
            return 0.0
        A, B = p
        if abs(A - A_gold) <= tol_A and abs(B - B_gold) <= tol_B:
            return 1.0
        return 0.0
    score = 0.0
    count = 0
    if params_found['liquid_L0'] is not None:
        count += 1
        A, B = params_found['liquid_L0']
        if abs(A - gold['liquid_L0']) <= 0.1 and B == 0:
            score += 1
    if params_found['hcp_L0'] is not None:
        count += 1
        if check_param(params_found['hcp_L0'], gold['hcp_L0_A'], gold['hcp_L0_B']):
            score += 1
    if params_found['fcc_L0'] is not None:
        count += 1
        if check_param(params_found['fcc_L0'], gold['fcc_L0_A'], gold['fcc_L0_B']):
            score += 1
    if params_found['fcc_L1'] is not None:
        count += 1
        if check_param(params_found['fcc_L1'], gold['fcc_L1_A'], 0.0):
            score += 1
    if params_found['bcc_L0'] is not None:
        count += 1
        if check_param(params_found['bcc_L0'], gold['bcc_L0'], 0.0):
            score += 1
    if count == 0:
        return 0.0
    return score / count


# === block: score_2 (check id='nirey_check') ===
def score_2(artifact, step, ctx):
    import pycalphad
    import numpy as np
    import tempfile, os, shutil
    gold = step['gold']
    content = artifact
    tmpd = tempfile.mkdtemp()
    tdb_y_path = os.path.join(tmpd, 'nirey.tdb')
    with open(tdb_y_path, 'w') as f:
        f.write(content)
    nire_path = os.path.join('/app/outputs', 'Ni_Re.tdb')
    score_binary = 0.0
    try:
        db_y = pycalphad.Database(tdb_y_path)
        comps = ['NI','RE','Y','VA']
        T_range = np.arange(3300, 2500, -10)
        liquidus_T_y = None
        for T in T_range:
            conds = {v.N: 1, v.P: 101325, v.T: T, v.X('NI'): 0.5, v.X('RE'): 0.5, v.X('Y'): 0.0}
            eq = pycalphad.equilibrium(db_y, comps, sorted(conds.keys()), conds)
            phases = eq.Phase.values
            if 'LIQUID' in phases:
                liq_idx = list(phases).index('LIQUID')
                if eq.NP.values[liq_idx] > 0.999:
                    liquidus_T_y = T
                else:
                    break
            else:
                break
        if os.path.exists(nire_path):
            with open(nire_path) as f:
                nire_content = f.read()
            tmpd2 = tempfile.mkdtemp()
            nire_tdb_path = os.path.join(tmpd2, 'nire.tdb')
            with open(nire_tdb_path, 'w') as f:
                f.write(nire_content)
            db_nire = pycalphad.Database(nire_tdb_path)
            liquidus_T_nire = None
            for T in T_range:
                conds = {v.N: 1, v.P: 101325, v.T: T, v.X('NI'): 0.5, v.X('RE'): 0.5}
                eq = pycalphad.equilibrium(db_nire, ['NI','RE','VA'], sorted(conds.keys()), conds)
                phases = eq.Phase.values
                if 'LIQUID' in phases:
                    liq_idx = list(phases).index('LIQUID')
                    if eq.NP.values[liq_idx] > 0.999:
                        liquidus_T_nire = T
                    else:
                        break
                else:
                    break
            shutil.rmtree(tmpd2)
            if liquidus_T_y is not None and liquidus_T_nire is not None:
                if abs(liquidus_T_y - liquidus_T_nire) < 1.0:
                    score_binary = 1.0
        found = False
        for x_Y in gold['grid_x_Y']:
            for x_Re in gold['grid_x_Re']:
                x_Ni = 1 - x_Y - x_Re
                if x_Ni <= 0:
                    continue
                conds = {v.N: 1, v.P: 101325, v.T: gold['test_T_K'], v.X('NI'): x_Ni, v.X('RE'): x_Re, v.X('Y'): x_Y}
                eq = pycalphad.equilibrium(db_y, comps, sorted(conds.keys()), conds)
                phases = set(eq.Phase.values)
                if 'FCC_A1' in phases and 'HCP_A3' in phases and 'NI17Y2' in phases:
                    found = True
                    break
            if found:
                break
        score_three = 1.0 if found else 0.0
    finally:
        shutil.rmtree(tmpd)
    return 0.5 * score_binary + 0.5 * score_three


_SCORERS = {
    'rey_check': score_0,
    'nire_check': score_1,
    'nirey_check': score_2,
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
