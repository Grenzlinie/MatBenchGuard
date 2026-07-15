import os
import json
import csv

# === author imports / helpers ===
import math

class _Numpy:
    exp = staticmethod(math.exp)
    isfinite = staticmethod(math.isfinite)

np = _Numpy()

def quad(func, a, b, limit=200):
    if a == b:
        return 0.0, None
    n = 201  # odd number of intervals for Simpson
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n, 2):
        s += 4.0 * func(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2.0 * func(a + i * h)
    return s * h / 3.0, None

R = 8.314462618


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
    steps = spec.get('steps', [])
    ctx = {}
    for step in steps:
        sid = step['id']
        if 'gold' in step:
            ctx[sid + '_gold'] = step['gold']
    return ctx


# === block: score_0 (check id='phonon') ===
def score_0(artifact, step, ctx):
    gold = ctx.get('phonon_gold')
    if gold is None:
        return 0.0
    compounds = ['Bi4Ta2O11', 'Bi7Ta3O18', 'Bi3TaO7']
    mode_names = ['D', 'E1', 'E2', 'E3', 'E4', 'E5']
    tol = 0.05  # 5% relative tolerance
    scores = []
    for comp in compounds:
        if comp not in artifact or comp not in gold:
            scores.append(0.0)
            continue
        agent_modes = artifact[comp]
        gold_modes = gold[comp]
        if not isinstance(agent_modes, list) or len(agent_modes) < 6:
            scores.append(0.0)
            continue
        for i, mn in enumerate(mode_names):
            ag = agent_modes[i]
            gd = gold_modes[i]
            if ag.get('mode') != mn:
                scores.append(0.0)
                continue
            try:
                theta = float(ag['Theta'])
                alpha = float(ag['alpha'])
            except:
                scores.append(0.0)
                continue
            # relative errors
            err_theta = abs(theta - gd['Theta']) / gd['Theta'] if gd['Theta'] != 0 else 0.0
            err_alpha = abs(alpha - gd['alpha']) / gd['alpha'] if gd['alpha'] != 0 else 0.0
            # linear decay: 1 if <= tol, 0 at 2*tol
            sc_theta = max(0.0, 1.0 - max(0.0, err_theta - tol) / tol)
            sc_alpha = max(0.0, 1.0 - max(0.0, err_alpha - tol) / tol)
            scores.append((sc_theta + sc_alpha) / 2)
    return float(sum(scores) / len(scores)) if scores else 0.0


# === block: score_1 (check id='thermo') ===
def score_1(artifact, step, ctx):
    import json, csv, math, sys
    phonon_path = '/app/outputs/phonon_parameters.json'
    try:
        with open(phonon_path) as f:
            phonon = json.load(f)
    except:
        phonon = None
    if phonon is None or not isinstance(phonon, dict):
        return 0.0

    def compute_Cph(T, params):
        total = 0.0
        for mode in params:
            Theta = mode['Theta']
            alpha = mode['alpha']
            deg = mode['degeneracy']
            if mode.get('mode') == 'D':
                if T <= 0.0:
                    continue
                xD = Theta / T
                def integrand(x):
                    if x <= 0:
                        return 0.0
                    ex = np.exp(x)
                    if np.isinf(ex):
                        return 0.0
                    denom = ex - 1.0
                    if denom == 0:
                        return 0.0
                    return x**4 * ex / denom**2
                try:
                    integral, _ = quad(integrand, 0.0, xD, limit=200)
                    C = 9 * R / (1.0 - alpha * T) * (T / Theta)**3 * integral
                    total += deg * C
                except:
                    continue
            else:  # Einstein
                if T <= 0.0:
                    continue
                xE = Theta / T
                exE = np.exp(xE)
                if np.isinf(exE):
                    continue
                denom = exE - 1.0
                if denom == 0:
                    continue
                C = R / (1.0 - alpha * T) * xE**2 * exE / denom**2
                total += deg * C
        return total

    T0 = 298.15
    compounds = ['Bi4Ta2O11', 'Bi7Ta3O18', 'Bi3TaO7']
    if not isinstance(artifact, list):
        return 0.0
    csv_data = {row.get('compound', ''): row for row in artifact if isinstance(row, dict)}
    gold = ctx.get('thermo_gold', {})
    rel_tol = 0.01
    abs_tol_cpm = 5.0
    abs_tol_H = 500.0
    abs_tol_S = 5.0
    scores = []
    for comp in compounds:
        if comp not in phonon or comp not in csv_data:
            scores.append(0.0)
            continue
        params = phonon[comp]
        if not isinstance(params, list) or len(params) < 6:
            scores.append(0.0)
            continue
        try:
            cpm_r = compute_Cph(T0, params)
            H_r, _ = quad(lambda t: compute_Cph(t, params), 0.0, T0, limit=200)
            S_r, _ = quad(lambda t: 0.0 if t == 0.0 else compute_Cph(t, params)/t, 0.0, T0, limit=200)
        except:
            scores.append(0.0)
            continue
        row = csv_data[comp]
        try:
            sub_cpm = float(row.get('Cpm_298', 0))
            sub_H = float(row.get('Hm_minus_H0', 0))
            sub_S = float(row.get('Sm_298', 0))
        except:
            scores.append(0.0)
            continue
        # consistency (sub vs recomputed)
        cons_cpm = max(0.0, 1.0 - max(0.0, abs(sub_cpm - cpm_r) - abs_tol_cpm) / (cpm_r * rel_tol))
        cons_H = max(0.0, 1.0 - max(0.0, abs(sub_H - H_r) - abs_tol_H) / (H_r * rel_tol))
        cons_S = max(0.0, 1.0 - max(0.0, abs(sub_S - S_r) - abs_tol_S) / (S_r * rel_tol))
        # accuracy (recomputed vs gold)
        g = gold.get(comp, {})
        if not g:
            scores.append(0.0)
            continue
        acc_cpm = max(0.0, 1.0 - max(0.0, abs(cpm_r - g['Cpm_298']) - abs_tol_cpm) / (g['Cpm_298'] * rel_tol))
        acc_H = max(0.0, 1.0 - max(0.0, abs(H_r - g['Hm_minus_H0']) - abs_tol_H) / (g['Hm_minus_H0'] * rel_tol))
        acc_S = max(0.0, 1.0 - max(0.0, abs(S_r - g['Sm_298']) - abs_tol_S) / (g['Sm_298'] * rel_tol))
        comp_score = 0.3 * (cons_cpm + cons_H + cons_S) / 3.0 + 0.7 * (acc_cpm + acc_H + acc_S) / 3.0
        scores.append(comp_score)
    return float(np.mean(scores)) if scores else 0.0


# === block: score_2 (check id='hight') ===
def score_2(artifact, step, ctx):
    gold = ctx.get('hight_gold')
    if gold is None:
        return 0.0
    compounds = ['Bi4Ta2O11', 'Bi7Ta3O18', 'Bi3TaO7']
    tol = 0.10  # 10% relative tolerance
    scores = []
    if not isinstance(artifact, list):
        return 0.0
    csv_data = {row.get('compound', ''): row for row in artifact if isinstance(row, dict)}
    for comp in compounds:
        if comp not in csv_data or comp not in gold:
            scores.append(0.0)
            continue
        row = csv_data[comp]
        g = gold[comp]
        try:
            A = float(row.get('A', 0))
            B = float(row.get('B', 0))
            C = float(row.get('C', 0))
        except:
            scores.append(0.0)
            continue
        # relative errors
        err_A = abs(A - g['A']) / abs(g['A']) if g['A'] != 0 else 0.0
        err_B = abs(B - g['B']) / abs(g['B']) if g['B'] != 0 else 0.0
        err_C = abs(C - g['C']) / abs(g['C']) if g['C'] != 0 else 0.0
        sc_A = max(0.0, 1.0 - max(0.0, err_A - tol) / tol)
        sc_B = max(0.0, 1.0 - max(0.0, err_B - tol) / tol)
        sc_C = max(0.0, 1.0 - max(0.0, err_C - tol) / tol)
        scores.append((sc_A + sc_B + sc_C) / 3.0)
    return float(np.mean(scores)) if scores else 0.0


_SCORERS = {
    'phonon': score_0,
    'thermo': score_1,
    'hight': score_2,
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
