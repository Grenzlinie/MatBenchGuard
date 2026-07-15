import os
import json
import csv

# === author imports / helpers ===
import math
import json
import csv

# Constants for dynamic enthalpy calculation
_kB_eV_K = 8.617333262145e-5
_nu = 5e13          # s^-1
_L_Y = 14.4         # nm
_b = 0.2851         # nm
_nu_star_ps = _nu * (_L_Y / _b) * 1e-12  # convert to ps^-1, approximately 2525 ps^-1
_Delta_tau = 30.0   # MPa
_mu = 35000.0       # MPa
_eps_dot = 1.5e-5   # ps^-1
_tau_dot_0 = _mu * _eps_dot  # MPa/ps


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
    spec_steps = spec.get('steps', [])
    static_ref = []
    for step in spec_steps:
        if step.get('id') == 'static_enthalpy_ref_check':
            for cp in step.get('check_points', []):
                static_ref.append((float(cp['stress_MPa']), float(cp['enthalpy_eV'])))
            break
    static_ref.sort(key=lambda x: x[0])  # sort by stress
    def static_enthalpy_interp(stress):
        # linear interpolation; extrapolate constant
        if not static_ref:
            return 0.0
        points = static_ref
        if stress <= points[0][0]:
            return points[0][1]
        if stress >= points[-1][0]:
            return points[-1][1]
        for i in range(len(points)-1):
            s0, h0 = points[i]
            s1, h1 = points[i+1]
            if s0 <= stress <= s1:
                ratio = (stress - s0) / (s1 - s0)
                return h0 + ratio * (h1 - h0)
        return points[-1][1]
    return {'static_ref': static_ref, 'static_enthalpy_interp': static_enthalpy_interp, 'nu_star_ps': _nu_star_ps, 'Delta_tau': _Delta_tau, 'tau_dot_0': _tau_dot_0}


# === block: score_0 (check id='flexible_bc_std_check') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts with 'strain','stress_MPa'
    stresses = []
    for row in rows:
        try:
            strain = float(row['strain'])
            stress = float(row['stress_MPa'])
        except (ValueError, KeyError):
            continue
        if 0.0025 <= strain <= 0.007:
            stresses.append(stress)
    if not stresses:
        return 0.0
    n = len(stresses)
    mean = sum(stresses)/n
    std = math.sqrt(sum((s-mean)**2 for s in stresses)/n)
    if std <= 50.0:
        return 1.0
    else:
        # linear decay, 0 at 100 MPa
        return max(0.0, 1.0 - (std - 50.0)/50.0)


# === block: score_1 (check id='static_enthalpy_ref_check') ===
def score_1(artifact, step, ctx):
    rows = artifact  # list of dicts
    # build mapping of stress -> enthalpy from artifact
    ref_points = step['check_points']
    tol = step.get('tolerance_abs', 0.06)
    if not ref_points:
        return 0.0
    correct = 0
    total = len(ref_points)
    for rp in ref_points:
        stress_target = float(rp['stress_MPa'])
        enthalpy_target = float(rp['enthalpy_eV'])
        best_dev = None
        for row in rows:
            try:
                s = float(row['stress_MPa'])
                h = float(row['enthalpy_eV'])
            except (ValueError, KeyError):
                continue
            if abs(s - stress_target) < 1.0:  # consider same stress point
                dev = abs(h - enthalpy_target)
                if best_dev is None or dev < best_dev:
                    best_dev = dev
        if best_dev is not None and best_dev <= tol:
            correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_2 (check id='peierls_ref_check') ===
def score_2(artifact, step, ctx):
    try:
        val = float(artifact.get('peierls_stress_MPa'))
    except (ValueError, TypeError, KeyError):
        return 0.0
    target = float(step['target'])
    tol = float(step.get('tolerance_abs', 100.0))
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='dynamic_enthalpy_consistency_check') ===
def score_3(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    nu_star = ctx['nu_star_ps']
    Delta = ctx['Delta_tau']
    tau_dot = ctx['tau_dot_0']
    static_interp = ctx['static_enthalpy_interp']
    ratio = nu_star * Delta / tau_dot
    ln_ratio = math.log(ratio)
    self_consistent_weight = 0.2
    static_agree_weight = 0.8
    self_scores = []
    static_scores = []
    for row in rows:
        try:
            T = float(row['temperature_K'])
            avg_stress = float(row['avg_jump_stress_MPa'])
            reported_H = float(row['enthalpy_eV'])
        except (ValueError, KeyError):
            continue
        H_calc = _kB_eV_K * T * ln_ratio
        # self-consistency (tight)
        if abs(H_calc - reported_H) < 0.001:
            self_scores.append(1.0)
        else:
            self_scores.append(0.0)
        # static agreement at avg_stress
        expected_H = static_interp(avg_stress)
        dev = abs(H_calc - expected_H)
        if dev <= 0.05:
            static_scores.append(1.0)
        else:
            static_scores.append(max(0.0, 1.0 - (dev - 0.05)/0.1))  # linear decay to 0 at 0.15 dev
    if not self_scores:
        return 0.0
    avg_self = sum(self_scores)/len(self_scores)
    avg_static = sum(static_scores)/len(static_scores)
    total_score = self_consistent_weight * avg_self + static_agree_weight * avg_static
    return total_score


_SCORERS = {
    'flexible_bc_std_check': score_0,
    'static_enthalpy_ref_check': score_1,
    'peierls_ref_check': score_2,
    'dynamic_enthalpy_consistency_check': score_3,
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
