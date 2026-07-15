import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
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
    import numpy as np
    from scipy.integrate import quad

    R = 8.314
    A_e1_K = 1000.15
    s_cem_m = 25e-9
    D0_alpha = 1.1e-6
    Q_alpha = 87500.0
    D0_gamma = 2.3e-5
    Q_gamma = 137700.0

    def D_gamma_T(T):
        return D0_gamma * np.exp(-Q_gamma / (R * T))
    def D_alpha_T(T):
        return D0_alpha * np.exp(-Q_alpha / (R * T))

    temps_C = [750, 800, 850, 900]
    temps_K = [t + 273.15 for t in temps_C]

    # reference D per temperature based on expected best-fit candidate
    ref_D = {}
    for idx, T_C in enumerate(temps_C):
        T_K = temps_K[idx]
        if T_C == 750:
            # D_mixed
            Dg_avg, _ = quad(lambda x: D_gamma_T(x), A_e1_K, T_K)
            Dg_avg /= (T_K - A_e1_K)
            Da_avg, _ = quad(lambda x: D_alpha_T(x), A_e1_K, T_K)
            Da_avg /= (T_K - A_e1_K)
            ref_D[T_C] = (Dg_avg + Da_avg) / 2.0
        elif T_C == 800:
            ref_D[T_C] = D_gamma_T(T_K)
        else:  # 850, 900
            Dg_avg, _ = quad(lambda x: D_gamma_T(x), A_e1_K, T_K)
            Dg_avg /= (T_K - A_e1_K)
            ref_D[T_C] = Dg_avg

    # load reference tau points from step config
    step_config = spec['steps'][0].get('hidden_config', {})
    ref_tau = np.array(step_config['reference_tau_points'])

    # compute reference f values
    ref_f = {}
    for idx, T_C in enumerate(temps_C):
        T_K = temps_K[idx]
        D_val = ref_D[T_C]
        f_vals = (T_K / A_e1_K - 1.0) * np.sqrt(D_val * ref_tau) / s_cem_m
        ref_f[T_C] = f_vals

    ctx = {
        'temps_C': temps_C,
        'temps_K': temps_K,
        'ref_tau': ref_tau,
        'ref_f': ref_f,
        'expected_best': step_config['expected_best']
    }


# === block: score_0 (check id='best_candidate_shift') ===
def score_0(artifact, step, ctx):
    import numpy as np
    from scipy.interpolate import interp1d

    # prepare function not returning ctx? guard against None
    if ctx is None:
        return 0.0

    # artifact is list of dicts from CSV reader
    curves = {}
    for row in artifact:
        t = float(row['T_max_C'])
        d = row['D_candidate']
        tau = float(row['tau_s'])
        f = float(row['f_p_gamma'])
        curves.setdefault(t, {}).setdefault(d, []).append((tau, f))

    temps = ctx['temps_C']
    ref_tau = ctx['ref_tau']
    ref_f = ctx['ref_f']
    expected = ctx['expected_best']

    correct_count = 0
    for t in temps:
        if t not in ref_f:
            continue
        candidate_rmse = {}
        for d in ['Dγ_avg', 'Dγ_Tmax', 'Dα_avg', 'Dα_Tmax', 'D_mixed']:
            if t not in curves or d not in curves[t]:
                candidate_rmse[d] = float('inf')
                continue
            points = curves[t][d]
            points.sort(key=lambda x: x[0])
            tau_vals = np.array([p[0] for p in points])
            f_vals = np.array([p[1] for p in points])
            # guard against too few points
            if len(tau_vals) < 2:
                candidate_rmse[d] = float('inf')
                continue
            interp = interp1d(tau_vals, f_vals, kind='linear', fill_value='extrapolate')
            f_pred = interp(ref_tau)
            rmse = np.sqrt(np.mean((f_pred - ref_f[t])**2))
            candidate_rmse[d] = rmse
        if candidate_rmse:
            best = min(candidate_rmse, key=lambda d: candidate_rmse[d])
            if expected.get(str(t)) == best:
                correct_count += 1

    total = len(temps)
    score = correct_count / total if total else 0.0
    return min(score, 1.0)


_SCORERS = {
    'best_candidate_shift': score_0,
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
