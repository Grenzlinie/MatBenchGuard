import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, math

def _pip_install(pkg):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', pkg])

try:
    import pandas as pd
except ImportError:
    _pip_install('pandas')
    import pandas as pd

try:
    import numpy as np
except ImportError:
    _pip_install('numpy')
    import numpy as np

try:
    import scipy.stats as sps
except ImportError:
    _pip_install('scipy')
    import scipy.stats as sps


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


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    return 1.0


# === block: score_1 (check id='tc_recompute') ===
def score_1(artifact, step, ctx):
    def mcmillan_tc(lam, wlog, mustar=0.1):
        if lam <= mustar: return 0.0
        expo = -1.04 * (1.0 + lam) / (lam - mustar * (1.0 + 0.62 * lam))
        return (wlog / 1.2) * math.exp(expo)

    rows = artifact
    if not rows: return 0.0
    scores = []
    for r in rows:
        try:
            lam = float(r['lambda'])
            wlog = float(r['omega_log_K'])
            tc_report = float(r['Tc_K'])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        tc_calc = mcmillan_tc(lam, wlog)
        diff = abs(tc_calc - tc_report)
        scores.append(1.0 if diff <= 0.1 else max(0.0, 1.0 - diff))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='param_value_match') ===
def score_2(artifact, step, ctx):
    gold_rows = step.get('target', [])
    tol = step.get('tolerance', {})
    rel_tol = {k: v for k, v in tol.items()}

    def get_param(row, key):
        try:
            return float(row[key])
        except (KeyError, ValueError):
            return None

    scores = []
    for gold in gold_rows:
        compound = gold['compound']
        pressure = gold['pressure_GPa']
        # find matching row
        match = None
        for r in artifact:
            if r.get('compound','').strip() == compound:
                try:
                    p = float(r.get('pressure_GPa', -1))
                    if abs(p - pressure) < 0.001:
                        match = r
                        break
                except:
                    continue
        if match is None:
            scores.append(0.0)
            continue
        for param in ['lambda', 'omega_log_K', 'N_EF_states_per_spin_Ry_unitcell']:
            v = get_param(match, param)
            gv = gold[param]
            if v is None:
                scores.append(0.0)
            else:
                rel_err = abs(v - gv) / (abs(gv) + 1e-12)
                if rel_err <= rel_tol.get(param, 0.1):
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (rel_err - rel_tol.get(param,0.1))*10))
    if not scores: return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='monotonic_trend') ===
def score_3(artifact, step, ctx):
    atomic_map = {
        'LaH': 57, 'CeH': 58, 'PrH': 59, 'NdH': 60, 'PmH': 61,
        'SmH': 62, 'EuH': 63, 'GdH': 64, 'TbH': 65, 'DyH': 66,
        'HoH': 67, 'ErH': 68, 'TmH': 69, 'YbH': 70, 'LuH': 71
    }
    lanthanides = set(atomic_map.keys())
    points = []
    for r in artifact:
        try:
            comp = r.get('compound', '').strip()
            press = float(r['pressure_GPa'])
            tc = float(r['Tc_K'])
        except:
            continue
        if press == 0.0 and comp in lanthanides:
            if comp in ('LaH', 'YbH'):
                continue  # anomalies, excluded
            points.append((atomic_map[comp], tc))
    if len(points) < 2:
        return 0.0
    points.sort()
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    rho, pval = sps.spearmanr(xs, ys)
    if np.isnan(rho): return 0.0
    if rho >= 0.8:
        return 1.0
    else:
        return max(0.0, rho / 0.8)


# === block: score_4 (check id='pressure_doping_trends') ===
def score_4(artifact, step, ctx):
    def get_val(comp, press):
        for r in artifact:
            try:
                c = r['compound'].strip()
                p = float(r['pressure_GPa'])
                tc = float(r['Tc_K'])
                if c == comp and abs(p - press) < 0.001:
                    return tc
            except:
                continue
        return None

    pressures = [0.0, 1.0, 10.0]
    ok = True
    # RS-LuH decreasing
    lu_tcs = [get_val('RS-LuH', p) for p in pressures]
    if None in lu_tcs:
        ok = False
    else:
        if not (lu_tcs[0] > lu_tcs[1] > lu_tcs[2]):
            ok = False
    # Lu4NH3 decreasing
    n_tcs = [get_val('Lu4NH3', p) for p in pressures]
    if None in n_tcs:
        ok = False
    else:
        if not (n_tcs[0] > n_tcs[1] > n_tcs[2]):
            ok = False
    # doping supression at each pressure
    if ok:
        for p in pressures:
            lu_tc = get_val('RS-LuH', p)
            n_tc = get_val('Lu4NH3', p)
            if lu_tc is None or n_tc is None:
                ok = False
                break
            if not (n_tc < lu_tc):
                ok = False
                break
    return 1.0 if ok else 0.0


_SCORERS = {
    'shape_check': score_0,
    'tc_recompute': score_1,
    'param_value_match': score_2,
    'monotonic_trend': score_3,
    'pressure_doping_trends': score_4,
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
