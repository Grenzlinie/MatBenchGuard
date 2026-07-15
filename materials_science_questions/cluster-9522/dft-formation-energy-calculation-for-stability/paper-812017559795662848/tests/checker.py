import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import minimize
import csv

def cef_gibbs(y, energies, R, T):
    yI, yII, yIII = y[0], y[1], y[2]
    yI_Hf = 1.0 - yI
    yII_Hf = 1.0 - yII
    yIII_Hf = 1.0 - yIII
    G = (yI_Hf * yII_Hf * yIII_Hf * energies[0] +
         yI * yII_Hf * yIII_Hf * energies[1] +
         yI_Hf * yII * yIII_Hf * energies[2] +
         yI_Hf * yII_Hf * yIII * energies[3] +
         yI * yII * yIII_Hf * energies[4] +
         yI * yII_Hf * yIII * energies[5] +
         yI_Hf * yII * yIII * energies[6] +
         yI * yII * yIII * energies[7])
    S_conf = (0.111 * (yI_Hf * np.log(max(yI_Hf, 1e-30)) + yI * np.log(max(yI, 1e-30))) +
              0.222 * (yII_Hf * np.log(max(yII_Hf, 1e-30)) + yII * np.log(max(yII, 1e-30))) +
              0.222 * (yIII_Hf * np.log(max(yIII_Hf, 1e-30)) + yIII * np.log(max(yIII, 1e-30))))
    return G - T * R * S_conf

def solve_cef(x_target, energies, R, T):
    cons = {'type': 'eq', 'fun': lambda y: y[0] + 2*y[1] + 2*y[2] - x_target}
    bounds = [(0, 1), (0, 1), (0, 1)]
    y0 = np.array([x_target/5.0, x_target/5.0, x_target/5.0])
    result = minimize(cef_gibbs, y0, args=(energies, R, T), bounds=bounds, constraints=cons, method='SLSQP')
    if not result.success:
        raise RuntimeError(f"CEF minimization failed for x={x_target}")
    return result.x[0], result.x[1], result.x[2]


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
    def cef_gibbs(y, energies, R, T):
        yI, yII, yIII = y[0], y[1], y[2]
        yI_Hf = 1.0 - yI
        yII_Hf = 1.0 - yII
        yIII_Hf = 1.0 - yIII
        # end-member products
        G = (yI_Hf * yII_Hf * yIII_Hf * energies[0] +
             yI * yII_Hf * yIII_Hf * energies[1] +
             yI_Hf * yII * yIII_Hf * energies[2] +
             yI_Hf * yII_Hf * yIII * energies[3] +
             yI * yII * yIII_Hf * energies[4] +
             yI * yII_Hf * yIII * energies[5] +
             yI_Hf * yII * yIII * energies[6] +
             yI * yII * yIII * energies[7])
        # configurational entropy (0.111, 0.222, 0.222 correspond to sublattice multiplicities 1/9, 2/9, 2/9)
        S_conf = (0.111 * (yI_Hf * np.log(max(yI_Hf, 1e-30)) + yI * np.log(max(yI, 1e-30))) +
                  0.222 * (yII_Hf * np.log(max(yII_Hf, 1e-30)) + yII * np.log(max(yII, 1e-30))) +
                  0.222 * (yIII_Hf * np.log(max(yIII_Hf, 1e-30)) + yIII * np.log(max(yIII, 1e-30))))
        return G - T * R * S_conf

    def solve_cef(x_target, energies, R, T):
        """
        x_target: composition index (number of Nb atoms per formula unit, 0 <= x_target <= 5)
        Returns site fractions (yI, yII, yIII)
        """
        # Constraint: yI + 2*yII + 2*yIII = x_target
        cons = {'type': 'eq', 'fun': lambda y: y[0] + 2*y[1] + 2*y[2] - x_target}
        bounds = [(0, 1), (0, 1), (0, 1)]
        # initial guess: start with equal distribution
        y0 = np.array([x_target/5.0, x_target/5.0, x_target/5.0])
        result = minimize(cef_gibbs, y0, args=(energies, R, T), bounds=bounds, constraints=cons, method='SLSQP')
        if not result.success:
            raise RuntimeError(f"CEF minimization failed for x={x_target}")
        return result.x[0], result.x[1], result.x[2]

    # Energy data: order (Hf:Hf:Hf:Ge), (Nb:Hf:Hf:Ge), (Hf:Nb:Hf:Ge), (Hf:Hf:Nb:Ge), (Nb:Nb:Hf:Ge), (Nb:Hf:Nb:Ge), (Hf:Nb:Nb:Ge), (Nb:Nb:Nb:Ge)
    energies_setA = np.array([0.00, 0.14, 5.22, 18.18, 8.00, 19.58, 27.08, 30.54])  # kJ/mol
    energies_setB = np.array([0.00, 0.41, 6.70, 18.18, 7.11, 18.59, 24.88, 25.29])  # kJ/mol
    R_kJ = 8.314462618e-3  # kJ/(mol*K)
    T = 1673.0

    ctx = {
        'energies_setA': energies_setA,
        'energies_setB': energies_setB,
        'R': R_kJ,
        'T': T,
    }
    return ctx


# === block: score_0 (check id='step_seta') ===
def score_0(artifact, step, ctx):
        import numpy as _np
        from scipy.optimize import minimize as _minimize
        globals()['np'] = _np
        globals()['minimize'] = _minimize

        def cef_gibbs(y, energies, R, T):
            yI, yII, yIII = y[0], y[1], y[2]
            yI_Hf = 1.0 - yI
            yII_Hf = 1.0 - yII
            yIII_Hf = 1.0 - yIII
            G = (yI_Hf * yII_Hf * yIII_Hf * energies[0] +
                 yI * yII_Hf * yIII_Hf * energies[1] +
                 yI_Hf * yII * yIII_Hf * energies[2] +
                 yI_Hf * yII_Hf * yIII * energies[3] +
                 yI * yII * yIII_Hf * energies[4] +
                 yI * yII_Hf * yIII * energies[5] +
                 yI_Hf * yII * yIII * energies[6] +
                 yI * yII * yIII * energies[7])
            S_conf = (0.111 * (yI_Hf * np.log(max(yI_Hf, 1e-30)) + yI * np.log(max(yI, 1e-30))) +
                      0.222 * (yII_Hf * np.log(max(yII_Hf, 1e-30)) + yII * np.log(max(yII, 1e-30))) +
                      0.222 * (yIII_Hf * np.log(max(yIII_Hf, 1e-30)) + yIII * np.log(max(yIII, 1e-30))))
            return G - T * R * S_conf

        def solve_cef(x_target, energies, R, T):
            cons = {'type': 'eq', 'fun': lambda y: y[0] + 2*y[1] + 2*y[2] - x_target}
            bounds = [(0, 1), (0, 1), (0, 1)]
            y0 = np.array([x_target/5.0, x_target/5.0, x_target/5.0])
            result = minimize(cef_gibbs, y0, args=(energies, R, T), bounds=bounds, constraints=cons, method='SLSQP')
            if not result.success:
                raise RuntimeError(f"CEF minimization failed for x={x_target}")
            return result.x[0], result.x[1], result.x[2]

        globals()['cef_gibbs'] = cef_gibbs
        globals()['solve_cef'] = solve_cef

        try:
            rows = artifact
            if not rows or not all(col in rows[0] for col in ['x', 'y_Nb_I', 'y_Nb_II', 'y_Nb_III']):
                return 0.0
            energies = ctx['energies_setA']
            R = ctx['R']
            T = ctx['T']
            tol = float(step.get('tolerance', 0.05))
            ok = 0
            total = 0
            for row in rows:
                x_val = float(row['x'])
                yI_agent = float(row['y_Nb_I'])
                yII_agent = float(row['y_Nb_II'])
                yIII_agent = float(row['y_Nb_III'])
                yI_ref, yII_ref, yIII_ref = solve_cef(x_val, energies, R, T)
                if (abs(yI_agent - yI_ref) <= tol and
                    abs(yII_agent - yII_ref) <= tol and
                    abs(yIII_agent - yIII_ref) <= tol):
                    ok += 1
                total += 1
            return ok / float(total) if total > 0 else 0.0
        except Exception:
            return 0.0


# === block: score_1 (check id='step_setb') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            rows = artifact
            if not rows or not all(col in rows[0] for col in ['x', 'y_Nb_I', 'y_Nb_II', 'y_Nb_III']):
                return 0.0
            energies = ctx['energies_setB']
            R = ctx['R']
            T = ctx['T']
            tol = float(step.get('tolerance', 0.05))
            ok = 0
            total = 0
            for row in rows:
                x_val = float(row['x'])
                yI_agent = float(row['y_Nb_I'])
                yII_agent = float(row['y_Nb_II'])
                yIII_agent = float(row['y_Nb_III'])
                yI_ref, yII_ref, yIII_ref = solve_cef(x_val, energies, R, T)
                if (abs(yI_agent - yI_ref) <= tol and
                    abs(yII_agent - yII_ref) <= tol and
                    abs(yIII_agent - yIII_ref) <= tol):
                    ok += 1
                total += 1
            return ok / float(total) if total > 0 else 0.0
        except Exception:
            return 0.0


_SCORERS = {
    'step_seta': score_0,
    'step_setb': score_1,
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
