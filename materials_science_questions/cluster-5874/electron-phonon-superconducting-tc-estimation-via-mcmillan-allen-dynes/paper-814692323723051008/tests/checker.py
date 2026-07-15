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
    def prepare(outputs_dir, spec):
        theta_D = 80.0
        theta_bp = 3000.0
        systems = {
            'K3C60': {'lambda_ph0': 0.2575, 'lambda_bp0': 0.1609, 'A': 0.14091, 'pressures': [0.0, 0.08, 0.33, 0.68, 1.02, 2.33]},
            'Rb3C60': {'lambda_ph0': 0.4355, 'lambda_bp0': 0.1715, 'A': 0.1936, 'pressures': [0.0, 0.18, 0.58, 1.03, 1.50, 1.92]}
        }
        ln_ratio = math.log(theta_bp / theta_D)
        expected = {}
        for sys, cfg in systems.items():
            for P in cfg['pressures']:
                lp = cfg['lambda_ph0'] * math.exp(-cfg['A'] * P)
                lb = cfg['lambda_bp0'] * math.exp(-cfg['A'] * P)
                lb_star = lb / (1 - lb * ln_ratio)
                Tc = 1.14 * theta_D * math.exp(-1.0 / (lb_star + lp))
                alpha = 0.5 * (1 - (1 + lp * math.log(Tc / (1.14 * theta_D)))**2)
                beta = 4.0 / (1.14 - Tc / theta_D)
                dTc = -cfg['A'] * Tc * (math.log(1.14 * theta_D / Tc) + (1 - 2 * alpha) * ln_ratio)
                expected[(sys, P)] = {'Tc_K': Tc, 'alpha': alpha, 'beta': beta, 'dTc_dP_K_GPa': dTc}
        return {'expected': expected}


# === block: score_0 (check id='step_calc') ===
def score_0(artifact, step, ctx):
        expected = ctx['expected']
        tolerance_Tc = step.get('params', {}).get('tolerance_Tc', 0.005)
        tolerance_alpha = step.get('params', {}).get('tolerance_alpha', 0.005)
        tolerance_beta = step.get('params', {}).get('tolerance_beta', 0.005)
        tolerance_dTc = step.get('params', {}).get('tolerance_dTc_dP', 0.01)
        total_expected = len(expected)
        if not artifact or not total_expected:
            return 0.0
        if not all(k in artifact[0] for k in ['system', 'pressure_GPa', 'Tc_K', 'alpha', 'beta', 'dTc_dP_K_GPa']):
            return 0.0
        artifact_map = {}
        for row in artifact:
            try:
                sys = str(row.get('system', '')).strip()
                p_str = row.get('pressure_GPa')
                if p_str is None:
                    continue
                p = float(p_str)
                key = (sys, round(p, 2))
                artifact_map[key] = row
            except (ValueError, TypeError):
                continue
        rows_good = 0
        for (sys, p), exp_row in expected.items():
            key = (sys, round(p, 2))
            act = artifact_map.get(key)
            if not act:
                continue
            good = True
            try:
                v_Tc = act.get('Tc_K')
                if v_Tc is None:
                    good = False
                else:
                    v_Tc = float(v_Tc)
                    if abs(v_Tc - exp_row['Tc_K']) > tolerance_Tc * abs(exp_row['Tc_K']):
                        good = False
                if good:
                    v_alpha = act.get('alpha')
                    if v_alpha is None:
                        good = False
                    else:
                        v_alpha = float(v_alpha)
                        if abs(v_alpha - exp_row['alpha']) > tolerance_alpha * abs(exp_row['alpha']):
                            good = False
                if good:
                    v_beta = act.get('beta')
                    if v_beta is None:
                        good = False
                    else:
                        v_beta = float(v_beta)
                        if abs(v_beta - exp_row['beta']) > tolerance_beta * abs(exp_row['beta']):
                            good = False
                if good:
                    v_dTc = act.get('dTc_dP_K_GPa')
                    if v_dTc is None:
                        good = False
                    else:
                        v_dTc = float(v_dTc)
                        if abs(v_dTc - exp_row['dTc_dP_K_GPa']) > tolerance_dTc * abs(exp_row['dTc_dP_K_GPa']):
                            good = False
            except (ValueError, TypeError):
                good = False
            if good:
                rows_good += 1
        return rows_good / total_expected if total_expected > 0 else 0.0


_SCORERS = {
    'step_calc': score_0,
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
