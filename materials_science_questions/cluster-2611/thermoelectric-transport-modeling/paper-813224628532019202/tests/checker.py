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
    return {}


# === block: score_0 (check id='s2') ===
def score_0(artifact, step, ctx):
    up_dos = None
    down_dos = None
    for row in artifact:
        spin = str(row.get("spin", "")).strip().lower()
        try:
            dos = float(row["dos_f"])
        except (KeyError, ValueError, TypeError):
            return 0.0
        if spin == "up":
            up_dos = dos
        elif spin == "down":
            down_dos = dos

    if up_dos is None or down_dos is None:
        return 0.0

    threshold = step.get("params", {}).get("minority_dos_threshold", 0.5)
    up_ok = up_dos > 0
    down_ok = abs(down_dos) < threshold

    if up_ok and down_ok:
        return 1.0
    elif up_ok or down_ok:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='s3') ===
def score_1(artifact, step, ctx):
    try:
        gap = float(artifact.strip())
    except (ValueError, AttributeError):
        return 0.0

    params = step.get("params", {})
    min_gap = params.get("min_gap", 0.05)
    max_gap = params.get("max_gap", 3.0)

    if gap > min_gap and gap < max_gap:
        return 1.0
    elif gap > 0 and gap <= min_gap:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='s4') ===
def score_2(artifact, step, ctx):
    params = step.get("params", {})

    # Seebeck_at_EF
    s_params = params.get("Seebeck_at_EF", {})
    s_target = s_params.get("target", 150)
    s_tol = s_params.get("tolerance_factor", 5.0)
    s_sign = s_params.get("sign_required", "positive")

    try:
        s = float(artifact.get("Seebeck_at_EF", 0))
    except (ValueError, TypeError):
        s = 0.0

    s_score = 0.0
    if s_sign == "positive" and s <= 0:
        s_score = 0.0
    elif s > 0:
        if s_target / s_tol <= s <= s_target * s_tol:
            s_score = 1.0
        elif s_target / (s_tol * 3) <= s <= s_target * (s_tol * 3):
            s_score = 0.5
        else:
            s_score = 0.2

    # sigma_over_tau_at_EF
    sig_params = params.get("sigma_over_tau_at_EF", {})
    sig_target_log10 = sig_params.get("target_log10", 13)
    sig_tol = sig_params.get("tolerance_log10", 1.5)

    try:
        sig = float(artifact.get("sigma_over_tau_at_EF", 0))
    except (ValueError, TypeError):
        sig = 0.0

    sig_score = 0.0
    if sig > 0:
        log_sig = math.log10(sig)
        diff = abs(log_sig - sig_target_log10)
        if diff <= sig_tol:
            sig_score = 1.0
        elif diff <= sig_tol * 2:
            sig_score = 0.5
        else:
            sig_score = 0.2

    # Seebeck_max
    smax_params = params.get("Seebeck_max", {})
    smax_target = smax_params.get("target", 1186)
    smax_rtol = smax_params.get("relative_tolerance", 0.6)

    try:
        smax = float(artifact.get("Seebeck_max", 0))
    except (ValueError, TypeError):
        smax = 0.0

    smax_score = 0.0
    if smax > 0:
        rel_diff = abs(smax - smax_target) / smax_target
        if rel_diff <= smax_rtol:
            smax_score = 1.0
        elif rel_diff <= smax_rtol * 1.5:
            smax_score = 0.5
        else:
            smax_score = 0.2

    # Seebeck_max_mu
    smu_params = params.get("Seebeck_max_mu", {})
    smu_target = smu_params.get("target", 0.07)
    smu_atol = smu_params.get("absolute_tolerance", 0.15)

    try:
        smu = float(artifact.get("Seebeck_max_mu", 0))
    except (ValueError, TypeError):
        smu = 0.0

    smu_score = 0.0
    diff_mu = abs(smu - smu_target)
    if smu < -0.05:
        smu_score = 0.0
    elif diff_mu <= smu_atol:
        smu_score = 1.0
    elif diff_mu <= smu_atol * 2:
        smu_score = 0.5
    else:
        smu_score = 0.2

    return (s_score + sig_score + smax_score + smu_score) / 4.0


_SCORERS = {
    's2': score_0,
    's3': score_1,
    's4': score_2,
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
