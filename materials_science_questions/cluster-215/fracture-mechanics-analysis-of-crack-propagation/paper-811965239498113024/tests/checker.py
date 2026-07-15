import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    def prepare(outputs_dir, spec):
        import numpy as np
        import math
        # ----- helper functions -----
        def C_b():
            return np.array([[10,4,2.5,0,0,0],[4,10,2.5,0,0,0],[2.5,2.5,6,0,0,0],[0,0,0,2,0,0],[0,0,0,0,2,0],[0,0,0,0,0,3]])

        def generalized_effective(Cb, h_f, k):
            c11b = Cb[0,0]; c12b = Cb[0,1]; c13b = Cb[0,2]
            c22b = Cb[1,1]; c23b = Cb[1,2]; c33b = Cb[2,2]
            c44b = Cb[3,3]; c55b = Cb[4,4]; c66b = Cb[5,5]
            denom = c11b * h_f + c33b * k - c33b * h_f * k
            c11 = (c11b * c33b * k) / denom
            c22 = h_f*k*(c22b - c23b**2/c33b) + (1-h_f)*(c22b - c12b**2/c11b) + (c11b*c33b*k*((c12b*(1-h_f)/c11b + c23b*h_f/c33b)**2)) / denom
            c33 = h_f*k*(c11b - c13b**2/c33b) + (1-h_f)*(c33b - c13b**2/c11b) + (c11b*c33b*k*((c13b*(1-h_f)/c11b + c13b*h_f/c33b)**2)) / denom
            c12 = (c12b*c33b*k + c11b*c23b*h_f*k - c12b*c33b*h_f*k) / denom
            c13 = (c13b*k*(c33b + c11b*h_f - c33b*h_f)) / denom
            term_c23_1 = h_f*k*(c12b - c13b*c23b/c33b)
            term_c23_2 = (1-h_f)*(c23b - c12b*c13b/c11b)
            term_c23_3 = (c11b*c33b*k*((c13b*(1-h_f)/c11b + c13b*h_f/c33b)*(c12b*(1-h_f)/c11b + c23b*h_f/c33b))) / denom
            c23 = term_c23_1 + term_c23_2 + term_c23_3
            c44 = c44b - c44b*h_f + c66b*h_f*k
            c55 = (c55b*k) / (h_f + k - h_f*k)
            c66 = (c66b*c44b*k) / (c66b*h_f + c44b*k - c44b*h_f*k)
            return np.array([[c11,c12,c13,0,0,0],[c12,c22,c23,0,0,0],[c13,c23,c33,0,0,0],[0,0,0,c44,0,0],[0,0,0,0,c55,0],[0,0,0,0,0,c66]])

        def tensor_from_voigt(C):
            T = np.zeros((3,3,3,3))
            voigt = [(0,0),(1,1),(2,2),(1,2),(0,2),(0,1)]
            for i in range(6):
                a,b = voigt[i]
                for j in range(6):
                    c,d = voigt[j]
                    T[a,b,c,d] = C[i,j]
            return T

        def rotate_stiffness(C, R):
            T = tensor_from_voigt(C)
            Trot = np.zeros((3,3,3,3))
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            s = 0.0
                            for p in range(3):
                                for q in range(3):
                                    for r in range(3):
                                        for s2 in range(3):
                                            s += R[i,p]*R[j,q]*R[k,r]*R[l,s2]*T[p,q,r,s2]
                            Trot[i,j,k,l] = s
            voigt = [(0,0),(1,1),(2,2),(1,2),(0,2),(0,1)]
            Crot = np.zeros((6,6))
            for i in range(6):
                a,b = voigt[i]
                for j in range(6):
                    c,d = voigt[j]
                    Crot[i,j] = Trot[a,b,c,d]
            return Crot

        def apply_horizontal_linear_slip(Cb_horiz, Z):
            # Cb_horiz is 6x6 stiffness for background with horizontal fractures (x3 depth)
            M = np.array([[Cb_horiz[0,0], Cb_horiz[0,1], Cb_horiz[0,5]],
                          [Cb_horiz[0,1], Cb_horiz[1,1], Cb_horiz[1,5]],
                          [Cb_horiz[0,5], Cb_horiz[1,5], Cb_horiz[5,5]]])
            N = np.array([[Cb_horiz[2,2], Cb_horiz[2,3], Cb_horiz[2,4]],
                          [Cb_horiz[2,3], Cb_horiz[3,3], Cb_horiz[3,4]],
                          [Cb_horiz[2,4], Cb_horiz[3,4], Cb_horiz[4,4]]])
            P = np.array([[Cb_horiz[0,2], Cb_horiz[0,3], Cb_horiz[0,4]],
                          [Cb_horiz[1,2], Cb_horiz[1,3], Cb_horiz[1,4]],
                          [Cb_horiz[5,2], Cb_horiz[5,3], Cb_horiz[5,4]]])
            N_inv = np.linalg.inv(N)
            Ne_inv = np.linalg.inv(N) + Z
            Ne = np.linalg.inv(Ne_inv)
            Pe = P @ N_inv @ Ne
            Me = M - P @ N_inv @ P.T + P @ N_inv @ Ne @ N_inv @ P.T
            Ceff = np.zeros((6,6))
            # assemble
            Ceff[0,0]=Me[0,0]; Ceff[0,1]=Me[0,1]; Ceff[0,5]=Me[0,2]
            Ceff[1,1]=Me[1,1]; Ceff[1,5]=Me[1,2]; Ceff[5,5]=Me[2,2]
            Ceff[2,2]=Ne[0,0]; Ceff[2,3]=Ne[0,1]; Ceff[2,4]=Ne[0,2]
            Ceff[3,3]=Ne[1,1]; Ceff[3,4]=Ne[1,2]; Ceff[4,4]=Ne[2,2]
            Ceff[0,2]=Pe[0,0]; Ceff[0,3]=Pe[0,1]; Ceff[0,4]=Pe[0,2]
            Ceff[1,2]=Pe[1,0]; Ceff[1,3]=Pe[1,1]; Ceff[1,4]=Pe[1,2]
            Ceff[5,2]=Pe[2,0]; Ceff[5,3]=Pe[2,1]; Ceff[5,4]=Pe[2,2]
            # symmetrize upper/lower
            for i in range(6):
                for j in range(i+1,6):
                    Ceff[j,i] = Ceff[i,j]
            return Ceff

        def linear_slip_effective_x1(Cb, h_f, k):
            # rotate so that x1 becomes x3 (fractures become horizontal)
            R = np.array([[0,1,0],[0,0,1],[1,0,0]])
            Cb_rot = rotate_stiffness(Cb, R)
            # Z = (h_f/k) * N_b_rot^{-1}
            c33p = Cb_rot[2,2]; c44p = Cb_rot[3,3]; c55p = Cb_rot[4,4]
            N_inv = np.diag([1/c33p, 1/c44p, 1/c55p])
            Z = (h_f/k) * N_inv
            Ceff_rot = apply_horizontal_linear_slip(Cb_rot, Z)
            # rotate back
            Ceff = rotate_stiffness(Ceff_rot, R.T)
            return Ceff

        # ----- compute gold tables -----
        cb = C_b()
        gold_err = {}
        gold_slow = {}
        steps = spec.get('steps', [])
        for step in steps:
            if step.get('output_file') == 'step_01_err_data.csv':
                for tp in step.get('test_points', []):
                    sc = tp['scenario']
                    pv = tp['parameter_value']
                    if sc == 'vary_k':
                        h_f = 1e-5; k_val = pv
                    elif sc == 'vary_hf':
                        k_val = 1e-5; h_f = pv
                    elif sc == 'cumul_Z10':
                        k_val = pv; h_f = k_val/10.0
                    elif sc == 'cumul_Z1':
                        k_val = pv; h_f = k_val
                    elif sc == 'cumul_Z05':
                        k_val = pv; h_f = k_val/0.5
                    else:
                        continue
                    C_eff = generalized_effective(cb, h_f, k_val)
                    C_l_eff = linear_slip_effective_x1(cb, h_f, k_val)
                    Delta_l = cb - C_l_eff
                    Delta = cb - C_eff
                    err_val = 100.0 * np.linalg.norm((Delta_l - Delta).ravel()) / np.linalg.norm(Delta_l.ravel())
                    gold_err[(sc, pv)] = err_val
            elif step.get('output_file') == 'step_02_slowness_surfaces.csv':
                k_val = h_f = 0.04
                C_eff = generalized_effective(cb, h_f, k_val)
                T = tensor_from_voigt(C_eff)
                for tp in step.get('test_points',[]):
                    plane = tp['plane']; wave = tp['wave_type']
                    ang = math.radians(tp['angle_degrees'])
                    if plane == 'x3x1':
                        n = np.array([math.sin(ang), 0.0, math.cos(ang)])
                    elif plane == 'x3x2':
                        n = np.array([0.0, math.sin(ang), math.cos(ang)])
                    elif plane == 'x1x2':
                        n = np.array([math.sin(ang), math.cos(ang), 0.0])
                    else:
                        continue
                    Gamma = np.zeros((3,3))
                    for i in range(3):
                        for kk in range(3):
                            s = 0.0
                            for j in range(3):
                                for l in range(3):
                                    s += T[i,j,kk,l] * n[j] * n[l]
                            Gamma[i,kk] = s
                    eigvals = np.linalg.eigvalsh(Gamma)
                    eigvals_sorted = np.sort(eigvals)[::-1]
                    slown = 1.0/np.sqrt(np.maximum(eigvals_sorted, 1e-12))
                    # assign qP (fastest -> smallest slowness), qS1, qS2
                    if wave == 'qP':
                        val = slown[0]
                    elif wave == 'qS1':
                        val = slown[1]
                    else:
                        val = slown[2]
                    gold_slow[(plane, wave, tp['angle_degrees'])] = val
        return {'gold_err': gold_err, 'gold_slow': gold_slow}


# === block: score_0 (check id='step_01_errdata') ===
def score_0(artifact, step, ctx):
        if not artifact:
            return 0.0
        gold_err = ctx['gold_err']
        lookup = {}
        for row in artifact:
            try:
                if not all(k in row for k in ('scenario','parameter_value','err_percent')):
                    continue
                # Guard against None / missing values
                pv = row['parameter_value']
                err = row['err_percent']
                if pv is None or err is None or pv == '' or err == '':
                    continue
                key = (row['scenario'], float(pv))
                lookup[key] = float(err)
            except (ValueError, TypeError):
                # Skip malformed rows
                continue
        test_points = step.get('test_points', [])
        if not test_points:
            return 1.0
        tol_rel = step.get('tolerance_relative', 1e-3)
        tol_abs = step.get('tolerance_absolute', 1e-12)
        total = 0.0
        for tp in test_points:
            key = (tp['scenario'], tp['parameter_value'])
            expected = gold_err.get(key)
            if expected is None:
                continue
            agent = lookup.get(key)
            if agent is None:
                continue
            if abs(expected) < 1e-15:
                diff = abs(agent - expected)
                if diff <= tol_abs:
                    total += 1.0
                else:
                    total += max(0.0, 1.0 - diff/(10.0*tol_abs))
            else:
                rel_err = abs(agent - expected)/abs(expected)
                if rel_err <= tol_rel:
                    total += 1.0
                else:
                    total += max(0.0, 1.0 - (rel_err - tol_rel)/(10.0*tol_rel))
        if total == 0.0:
            return 0.0
        return min(1.0, total/len(test_points))


# === block: score_1 (check id='step_02_slowness') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        gold_slow = ctx['gold_slow']
        lookup = {}
        for row in artifact:
            if not all(k in row for k in ('plane','wave_type','angle_degrees','slowness_s_per_km')):
                continue
            lookup[(row['plane'], row['wave_type'], float(row['angle_degrees']))] = float(row['slowness_s_per_km'])
        test_points = step.get('test_points', [])
        if not test_points:
            return 1.0
        tol_rel = step.get('tolerance_relative', 1e-3)
        tol_abs = step.get('tolerance_absolute', 1e-12)
        total = 0.0
        for tp in test_points:
            key = (tp['plane'], tp['wave_type'], tp['angle_degrees'])
            expected = gold_slow.get(key)
            if expected is None:
                continue
            agent = lookup.get(key)
            if agent is None:
                continue
            if abs(expected) < 1e-15:
                diff = abs(agent - expected)
                if diff <= tol_abs:
                    total += 1.0
                else:
                    total += max(0.0, 1.0 - diff/(10.0*tol_abs))
            else:
                rel_err = abs(agent - expected)/abs(expected)
                if rel_err <= tol_rel:
                    total += 1.0
                else:
                    total += max(0.0, 1.0 - (rel_err - tol_rel)/(10.0*tol_rel))
        if total == 0.0:
            return 0.0
        return min(1.0, total/len(test_points))


_SCORERS = {
    'step_01_errdata': score_0,
    'step_02_slowness': score_1,
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
