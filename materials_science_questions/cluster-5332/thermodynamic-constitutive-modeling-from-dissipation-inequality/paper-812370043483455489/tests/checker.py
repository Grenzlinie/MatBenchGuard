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
        freqs = [10, 20, 30, 40, 50, 60]
        amps = [0.001, 0.0025, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05]
        expected_combos = [(f, a) for f in freqs for a in amps]
        eps0 = -0.11
        lam0 = 1.0 / (1.0 - eps0)
        params = {
            'mu_eq': 1.86,
            'mu_ov': 10.24,
            'zeta': 421,
            'tau': 1.0,
            'alpha': 0.449,
            'beta': 0.494,
            'b': 51078,
        }
        return {
            'expected_combos': expected_combos,
            'lam0': lam0,
            'params': params,
        }


# === block: score_0 (check id='check_moduli') ===
def score_0(artifact, step, ctx):
        if artifact is None or not isinstance(artifact, list):
            return 0.0
        expected_combos = ctx['expected_combos']
        lam0 = ctx['lam0']
        params = ctx['params']

        def compute_modulus(freq, amp):
            omega = 2 * math.pi * freq
            a_val = 1.0 + (2 * params['b'] / math.pi) * amp * (omega * params['tau']) ** params['alpha']
            omega_zeta_a = omega * params['zeta'] / a_val
            term = omega_zeta_a ** params['beta']
            cos_beta_pi_2 = math.cos(params['beta'] * math.pi / 2)
            sin_beta_pi_2 = math.sin(params['beta'] * math.pi / 2)
            denom = 1.0 + 2 * term * cos_beta_pi_2 + term ** 2
            G_prime = params['mu_eq'] * (lam0**2 + 2.0/lam0) + 3 * params['mu_ov'] * (term**2 + term * cos_beta_pi_2) / denom
            G_double = 3 * params['mu_ov'] * term * sin_beta_pi_2 / denom
            return G_prime, G_double

        correct_combos = set()
        for f, a in expected_combos:
            rows_matching = []
            for row in artifact:
                try:
                    rf = float(row['frequency_Hz'])
                    ra = float(row['strain_amplitude'])
                except (ValueError, KeyError):
                    continue
                if abs(rf - f) < 1e-6 and abs(ra - a) < 1e-6:
                    rows_matching.append(row)
            if not rows_matching:
                continue
            ok = False
            for row in rows_matching:
                try:
                    gp = float(row['G_prime_MPa'])
                    gd = float(row['G_double_prime_MPa'])
                except (ValueError, KeyError):
                    continue
                Gp_exp, Gd_exp = compute_modulus(f, a)
                tol_p = max(1e-4 * abs(Gp_exp), 1e-6)
                tol_d = max(1e-4 * abs(Gd_exp), 1e-6)
                if abs(gp - Gp_exp) <= tol_p and abs(gd - Gd_exp) <= tol_d:
                    ok = True
                    break
            if ok:
                correct_combos.add((f, a))
        if not expected_combos:
            return 0.0
        score = len(correct_combos) / len(expected_combos)
        return score


_SCORERS = {
    'check_moduli': score_0,
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
