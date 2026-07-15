import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='step_dispersion') ===
def score_0(artifact, step, ctx):
    # step_dispersion scorer body
    c11 = 1.68e12
    c12 = 1.21e12
    c44 = 0.75e12
    rho = 8.96
    a_ang = 3.61
    a_cm = a_ang * 1e-8
    eps = c11 - c12 - 2*c44

    # prefactors (apply a_cm)
    factor8 = 8.0 / (rho * a_cm * a_cm)
    factor2 = 2.0 / (rho * a_cm * a_cm)

    import math

    def expected_freq(direction, mode, k):
        """Return expected frequency in 10^13 rad/s for given direction, mode, k (1/Å)."""
        # k is in 1/Å; a_ang in Å, arguments are a_ang * k / factor
        arg_100 = a_ang * k / (2.0 * 1.4142135623730951)  # 2*sqrt(2)
        arg_110 = a_ang * k / 4.0
        arg_111 = a_ang * k / 2.449489742783178   # sqrt(6)
        sin_sq = None
        bracket = None
        if direction == '100':
            sin_sq = math.sin(arg_100)**2
            if mode == 'L':
                bracket = c11
            elif mode in ('T1', 'T2'):
                bracket = c44
            else:
                return None
            factor = factor8
        elif direction == '110':
            sin_sq = math.sin(arg_110)**2
            if mode == 'L':
                bracket = 2*c11 - eps - (2*c11 - c44 - eps) * sin_sq
            elif mode == 'T1':
                bracket = eps + 2*c44 - (c44 + eps) * sin_sq
            elif mode == 'T2':
                bracket = 2*c44 - (2*c44 - c11) * sin_sq
            else:
                return None
            factor = factor8
        elif direction == '111':
            sin_sq = math.sin(arg_111)**2
            if mode == 'L':
                bracket = (3*c11 - 2*eps) * sin_sq
            elif mode in ('T1', 'T2'):
                bracket = (3*c44 + eps) * sin_sq
            else:
                return None
            factor = factor2
        else:
            return None
        omega_sq = factor * bracket
        if omega_sq < 0:
            return 0.0
        omega = math.sqrt(omega_sq)
        return omega / 1e13

    errors = []
    for row in artifact:
        if not isinstance(row, dict):
            continue
        # Normalize keys to lower case for robustness
        norm = {k.lower().strip(): v for k, v in row.items()}
        d = norm.get('direction', '').strip()
        m = norm.get('mode', '').strip().upper()
        k_str = norm.get('k', '').strip()
        freq_str = norm.get('frequency', '').strip()
        if not d or not m or k_str == '' or freq_str == '':
            continue
        try:
            k_val = float(k_str)
            freq_val = float(freq_str)
        except (ValueError, TypeError):
            continue
        exp_freq = expected_freq(d, m, k_val)
        if exp_freq is None:
            continue
        err = freq_val - exp_freq
        errors.append(err * err)

    if not errors:
        return 0.0
    rmse = math.sqrt(sum(errors) / len(errors))
    tol_full = 0.1
    tol_zero = 0.5
    if rmse <= tol_full:
        return 1.0
    if rmse >= tol_zero:
        return 0.0
    return 1.0 - (rmse - tol_full) / (tol_zero - tol_full)


_SCORERS = {
    'step_dispersion': score_0,
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
