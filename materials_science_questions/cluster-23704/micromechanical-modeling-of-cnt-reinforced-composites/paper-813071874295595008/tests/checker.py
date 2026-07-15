import os
import json
import csv

# === author imports / helpers ===
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
    import math
    gold = {}
    # chitosan
    sig_m_ch = 69.1
    B_ch = 86.4
    B_max_ch = (1 + 80/15) * math.log(25000 / sig_m_ch)
    gold['chitosan'] = {'B': B_ch, 'B_max': B_max_ch, 'B_I': B_max_ch, 'B_N': B_ch - B_max_ch}
    # polysilsesquioxane
    sig_m_po = 75.0
    B_po = 132.9
    B_max_po = (1 + 80/15) * math.log(25000 / sig_m_po)
    gold['polysilsesquioxane'] = {'B': B_po, 'B_max': B_max_po, 'B_I': B_max_po, 'B_N': B_po - B_max_po}
    # PVA
    B_pva = 17.18
    gold['PVA'] = {'B': B_pva, 'B_max': 0.0, 'B_I': B_pva/2, 'B_N': B_pva/2}
    # PET
    B_pet = 33.34
    gold['PET'] = {'B': B_pet, 'B_max': 0.0, 'B_I': B_pet/2, 'B_N': B_pet/2}
    # sweep grids
    alpha_vals = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    N_vals = [100, 200, 300, 400, 500]
    phi_f = 0.02; sig_m = 40.0; sig_N_MPa = 40000.0; B_I = 10.0
    ln_ratio = math.log(sig_N_MPa / sig_m)
    alpha_N_expected = {}
    for a in alpha_vals:
        for n in N_vals:
            b_n = a * n / 100000.0 * ln_ratio
            sig_r = (1 - phi_f) / (1 + 2.5 * phi_f) * math.exp((B_I + b_n) * phi_f)
            alpha_N_expected[(a, n)] = (b_n, sig_r)
    phi_p_vals = [0.001, 0.002, 0.003, 0.004, 0.005]
    sig_N_GPa_vals = [20, 30, 40, 50, 60]
    N = 300
    phi_sigmaN_expected = {}
    for phi_p in phi_p_vals:
        for sig_N_GPa in sig_N_GPa_vals:
            sig_N_MPa2 = sig_N_GPa * 1000.0
            ln_ratio2 = math.log(sig_N_MPa2 / sig_m)
            b_n = (2.2 * N) / (100000.0 * phi_p) * ln_ratio2
            sig_r = (1 - phi_f) / (1 + 2.5 * phi_f) * math.exp((B_I + b_n) * phi_f)
            phi_sigmaN_expected[(phi_p, sig_N_GPa)] = (b_n, sig_r)
    return {'gold': gold, 'alpha_N_exp': alpha_N_expected, 'phi_sigmaN_exp': phi_sigmaN_expected}


# === block: score_0 (check id='fit_B') ===
def score_0(artifact, step, ctx):
    gold_all = ctx['gold']
    if not isinstance(artifact, dict):
        return 0.0
    systems = ['chitosan', 'polysilsesquioxane', 'PVA', 'PET']
    sys_scores = []
    for sys in systems:
        g = gold_all[sys]
        a = artifact.get(sys, {})
        if a is None:
            a = {}
        B = a.get('B')
        B_max = a.get('B_max')
        B_I = a.get('B_I')
        B_N = a.get('B_N')
        if B is None:
            sys_scores.append(0.0)
            continue
        rel_tol_B = 0.05
        rel_tol_B_max = 0.01
        rel_tol_B_N = 0.05
        sB = 1.0 if abs(B - g['B']) / g['B'] <= rel_tol_B else 0.0
        sBmax = 0.0
        if B_max is not None:
            if g['B_max'] == 0.0:
                if abs(B_max) < 1e-9:
                    sBmax = 1.0
            else:
                if abs(B_max - g['B_max']) / g['B_max'] <= rel_tol_B_max:
                    sBmax = 1.0
        sBI = 0.0
        if B_max is not None and B_I is not None:
            if abs(B_max) > 1e-12:
                if abs(B_I - B_max) / abs(B_max) <= 0.01:
                    sBI = 1.0
            else:
                if abs(B_I) < 1e-9:
                    sBI = 1.0
        sBN = 0.0
        if B is not None and B_max is not None and B_N is not None:
            exp_BN = B - B_max
            if abs(exp_BN) > 1e-12:
                if abs(B_N - exp_BN) / abs(exp_BN) <= rel_tol_B_N:
                    sBN = 1.0
            else:
                if abs(B_N) < 1e-9:
                    sBN = 1.0
        sys_score = (sB + sBmax + sBI + sBN) / 4.0
        sys_scores.append(sys_score)
    return sum(sys_scores) / len(sys_scores)


# === block: score_1 (check id='sweep_alpha_N') ===
def score_1(artifact, step, ctx):
    expected = ctx['alpha_N_exp']
    total = len(expected)
    if not isinstance(artifact, list) or total == 0:
        return 0.0
    row_map = {}
    for row in artifact:
        try:
            a = int(row['alpha'])
            n = int(row['N'])
            b_n = float(row['B_N'])
            sig_r = float(row['sigma_R'])
            row_map[(a, n)] = (b_n, sig_r)
        except:
            pass
    correct = 0
    for key, (exp_bn, exp_sr) in expected.items():
        got = row_map.get(key)
        if got is None:
            continue
        if abs(got[0] - exp_bn) < 1e-6 and abs(got[1] - exp_sr) < 1e-6:
            correct += 1
    return correct / total


# === block: score_2 (check id='sweep_phi_sigmaN') ===
def score_2(artifact, step, ctx):
    expected = ctx['phi_sigmaN_exp']
    total = len(expected)
    if not isinstance(artifact, list) or total == 0:
        return 0.0
    row_map = {}
    for row in artifact:
        try:
            phi_p = float(row['phi_p'])
            sig_N = float(row['sigma_N'])
            b_n = float(row['B_N'])
            sig_r = float(row['sigma_R'])
            row_map[(phi_p, sig_N)] = (b_n, sig_r)
        except:
            pass
    correct = 0
    for key, (exp_bn, exp_sr) in expected.items():
        got = row_map.get(key)
        if got is None:
            continue
        if abs(got[0] - exp_bn) < 1e-6 and abs(got[1] - exp_sr) < 1e-6:
            correct += 1
    return correct / total


_SCORERS = {
    'fit_B': score_0,
    'sweep_alpha_N': score_1,
    'sweep_phi_sigmaN': score_2,
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
