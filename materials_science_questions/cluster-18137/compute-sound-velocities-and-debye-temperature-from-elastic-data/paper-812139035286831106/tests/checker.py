import os
import json
import csv

# === author imports / helpers ===
from scipy.integrate import quad
from scipy.special import gamma, zeta
import numpy as np

R = 1.987
I_inf = {}
for n in [0.5, 1, 3]:
    I_inf[n] = gamma(n+1) * zeta(n+1)

def I_n(n, y, eps=1e-12):
    if y <= 0:
        return 0.0
    if y > 20:
        return I_inf[n]
    res, _ = quad(lambda x: x**n / (np.exp(x) - 1.0), 0, y, limit=200, epsabs=eps, epsrel=eps)
    return res

def D_n(n, y):
    if y <= 0:
        return np.nan
    Iy = I_n(n, y)
    term1 = n * (n+1) * y**(-n) * Iy
    term2 = n * y / (np.exp(y) - 1.0)
    return term1 - term2

def cV_modified(T, Theta3s, Theta1s, Theta3b, Theta1b):
    y1s = Theta1s / T
    y3s = Theta3s / T
    D1_1s = D_n(1, y1s)
    D3_3s = D_n(3, y3s)
    D1_3s = D_n(1, y3s)
    cV_s = R * (D1_1s + (Theta3s / Theta1s) * (D3_3s - D1_3s))
    y1b = Theta1b / T
    y3b = Theta3b / T
    D12_1b = D_n(0.5, y1b)
    D3_3b = D_n(3, y3b)
    D12_3b = D_n(0.5, y3b)
    cV_b = 2.0 * R * (D12_1b + (Theta3b / Theta1b)**0.5 * (D3_3b - D12_3b))
    return cV_s + cV_b


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


# === block: score_0 (check id='score_csv_main') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact
        if not rows or not isinstance(rows, list) or len(rows) == 0:
            return 0.0
        T_vals = []
        for r in rows:
            try:
                t = int(r.get('T', ''))
            except:
                return 0.0
            T_vals.append(t)
        if len(T_vals) != 200 or T_vals != list(range(1, 201)):
            return 0.0

        # Sub‑check C: file shape (weight 0.1)
        shape_ok = 1.0
        required = ['T','exp_cV','Debye_cV','Debye_dev_percent','Tarasov_cV','Tarasov_dev_percent','Modified_cV','Modified_dev_percent']
        for r in rows:
            if any(col not in r for col in required):
                shape_ok = 0.0
                break

        # Sub‑check A: verify agent's Modified_dev_percent against recomputed model (weight 0.6)
        gold = step.get('gold', {})
        checkpoints_raw = gold.get('checkpoints', {})
        checkpoints = {int(k): v for k, v in checkpoints_raw.items()}
        row_by_T = {int(r['T']): r for r in rows}
        tol_cv_exp = gold.get('tolerance_cv_exp', 0.001)
        tol_dev = 0.5   # tolerance matching grading_spec.json tolerance_dev
        matches = 0
        total_cp = len(checkpoints)
        Theta3s, Theta1s = 996.6, 996.9
        Theta3b, Theta1b = 188.7, 910.9
        for T_cp, cp_info in checkpoints.items():
            row = row_by_T.get(T_cp)
            if row is None:
                continue
            try:
                exp_cv_agent = float(row['exp_cV'])
                agent_dev = float(row['Modified_dev_percent'])
            except:
                continue
            # verify that agent's experimental data matches paper's reference
            if abs(exp_cv_agent - cp_info['cv_exp']) > tol_cv_exp:
                continue
            try:
                cV_mod_check = cV_modified(T_cp, Theta3s, Theta1s, Theta3b, Theta1b)
            except:
                continue
            expected_dev = 100.0 * (cV_mod_check - exp_cv_agent) / exp_cv_agent
            if abs(agent_dev - expected_dev) <= tol_dev:
                matches += 1
        score_A = matches / total_cp if total_cp > 0 else 0.0

        # Sub‑check B: structural superiority (weight 0.3)
        try:
            T_range = list(range(50, 201))
            mod_devs = [abs(float(row_by_T[t]['Modified_dev_percent'])) for t in T_range if t in row_by_T]
            deb_devs = [abs(float(row_by_T[t]['Debye_dev_percent'])) for t in T_range if t in row_by_T]
            tar_devs = [abs(float(row_by_T[t]['Tarasov_dev_percent'])) for t in T_range if t in row_by_T]
            if mod_devs and deb_devs and tar_devs:
                max_mod = max(mod_devs)
                max_deb = max(deb_devs)
                max_tar = max(tar_devs)
                structural_ok = 1.0 if (max_mod < max_deb and max_mod < max_tar) else 0.0
            else:
                structural_ok = 0.0
        except:
            structural_ok = 0.0

        total_score = 0.6 * score_A + 0.3 * structural_ok + 0.1 * shape_ok
        return total_score
    except Exception:
        return 0.0


_SCORERS = {
    'score_csv_main': score_0,
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
