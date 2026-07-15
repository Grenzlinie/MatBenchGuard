import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, importlib

try:
    import numpy as np
    import scipy.optimize
except (ImportError, ModuleNotFoundError):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy', 'scipy'])
    import numpy as np
    import scipy.optimize

import csv
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
        params = spec['steps'][0]['params']
        alloy_inputs = params['alloy_inputs']
        tolerances = params['tolerances']
        R = params['R']
        N = params['N']
        Phi0 = params['Phi0']
        mu_star = params['mu_star']
        fields = ['xi_GL_A', 'lambda_GL_A', 'k_GL', 'H_c_mT', 'theta_D_K', 'lambda_e_ph']

        expected = {}
        for alloy, inp in alloy_inputs.items():
            Tc = inp['Tc']
            Hc1_mT = inp['Hc1_mT']
            Hc2_T = inp['Hc2_T']
            gamma = inp['gamma_n_mJ_per_mol_K2'] * 1e-3
            beta = inp['beta_mJ_per_mol_K4'] * 1e-3

            pi = math.pi
            Hc1_T = Hc1_mT * 1e-3

            xi_m = math.sqrt(Phi0 / (2 * pi * Hc2_T))
            xi_A = xi_m * 1e10

            def eq(lambda_m):
                return (Phi0 / (4 * pi * lambda_m**2)) * (np.log(lambda_m / xi_m) + 0.12) - Hc1_T

            sol = scipy.optimize.root(eq, xi_m * 10, method='hybr')
            if not sol.success:
                sol = scipy.optimize.root(eq, xi_m * 10, method='lm')
            lambda_m = float(sol.x[0])
            lambda_A = lambda_m * 1e10

            k_GL = lambda_A / xi_A
            Hc_T = math.sqrt(Hc1_T * Hc2_T / math.log(k_GL))
            Hc_mT = Hc_T * 1000.0

            theta_D = (12 * pi**4 * R * N / (5 * beta)) ** (1/3)

            ln_arg = math.log(theta_D / (1.45 * Tc))
            num = 1.04 + mu_star * ln_arg
            den = (1 - 0.62 * mu_star) * ln_arg - 1.04
            lambda_eph = num / den

            expected[alloy] = {
                'xi_GL_A': xi_A,
                'lambda_GL_A': lambda_A,
                'k_GL': k_GL,
                'H_c_mT': Hc_mT,
                'theta_D_K': theta_D,
                'lambda_e_ph': lambda_eph
            }

        return {'expected': expected, 'tolerances': tolerances, 'fields': fields}


# === block: score_0 (check id='compute-params') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        expected = ctx['expected']
        tolerances = ctx['tolerances']
        fields = ctx['fields']
        n_fields = len(fields)
        n_alloys = len(expected)
        total = n_alloys * n_fields
        if total == 0:
            return 0.0
        passes = 0
        for row in artifact:
            alloy = row.get('alloy', '').strip()
            if alloy not in expected:
                continue
            exp = expected[alloy]
            for fld in fields:
                if fld not in row:
                    continue
                try:
                    val = float(row[fld])
                except (ValueError, TypeError):
                    continue
                ref = exp[fld]
                rel_tol = tolerances.get(fld, 0.01)
                denom = max(abs(ref), 1e-12)
                if abs(val - ref) / denom <= rel_tol:
                    passes += 1
        return min(1.0, passes / total) if total > 0 else 0.0


_SCORERS = {
    'compute-params': score_0,
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
