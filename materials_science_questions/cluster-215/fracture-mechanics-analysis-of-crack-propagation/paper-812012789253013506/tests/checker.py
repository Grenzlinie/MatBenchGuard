import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    ctx = {}
    return ctx


# === block: score_0 (check id='check_results_values') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    gold = step["gold"]
    tolerances = step["tolerances"]
    rocks = ["shale", "malmstone", "liparite"]
    cases = ["case1", "case2", "case3"]
    fields = [
        "stress_wave_energy",
        "cutoff_frequency_lower_rad_s",
        "cutoff_frequency_upper_rad_s",
        "energy_dissipation_ratio_analytical_pct",
        "energy_dissipation_ratio_discrete_pct"
    ]
    total = 0
    correct = 0
    for rock in rocks:
        agent_rock = artifact.get(rock, {})
        gold_rock = gold.get(rock, {})
        for case in cases:
            agent_case = agent_rock.get(case, {})
            gold_case = gold_rock.get(case, {})
            for field in fields:
                a_val = agent_case.get(field)
                g_val = gold_case.get(field)
                total += 1
                if a_val is None or g_val is None or g_val == 0:
                    continue
                rel_err = abs(a_val - g_val) / abs(g_val)
                tol = tolerances.get(field, 0.01)
                if rel_err <= tol:
                    correct += 1
    score = correct / total if total else 0.0
    return score


# === block: score_1 (check id='check_results_consistency') ===
def score_1(artifact, step, ctx):
    artifact = artifact
    rocks = ["shale", "malmstone", "liparite"]
    cases = ["case1", "case2", "case3"]
    # The paper's own analytical and discrete dissipation ratios differ by up to ~0.6%.
    # A consistent implementation will agree within 1% relative difference.
    tol = 0.01
    for rock in rocks:
        agent_rock = artifact.get(rock, {})
        for case in cases:
            agent_case = agent_rock.get(case, {})
            anal = agent_case.get("energy_dissipation_ratio_analytical_pct")
            disc = agent_case.get("energy_dissipation_ratio_discrete_pct")
            if anal is None or disc is None:
                return 0.0
            denom = abs(anal) + abs(disc) + 1e-12
            diff = 2 * abs(anal - disc) / denom
            if diff > tol:
                return 0.0
    return 1.0


# === block: score_2 (check id='check_spectrum_recompute') ===
def score_2(artifact, step, ctx):
    data = artifact
    omega = np.array([float(row["frequency_rad_s"]) for row in data])
    amp_sq = np.array([float(row["amplitude_squared"]) for row in data])
    idx = np.argsort(omega)
    omega = omega[idx]
    amp_sq = amp_sq[idx]
    params = step.get("spectrum_params", {})
    sigma = params["sigma"]
    tau = params["tau"]
    R = params["R"]
    gammaE_over_C = sigma * sigma * tau / R
    threshold = gammaE_over_C / omega
    below_contrib = np.where(amp_sq < threshold, amp_sq, 0.0)
    # manual trapezoidal integration to avoid deprecated np.trapz
    total = 0.5 * np.sum((amp_sq[1:] + amp_sq[:-1]) * np.diff(omega))
    below = 0.5 * np.sum((below_contrib[1:] + below_contrib[:-1]) * np.diff(omega))
    if total == 0:
        return 0.0
    ratio = below / total * 100.0
    ref = step["reference_value"]
    tol = step["tolerance_relative"]
    relerr = abs(ratio - ref) / max(abs(ref), 1e-12)
    if relerr <= tol:
        score = 1.0
    else:
        score = max(0.0, (2 * tol - relerr) / tol)
    return score


_SCORERS = {
    'check_results_values': score_0,
    'check_results_consistency': score_1,
    'check_spectrum_recompute': score_2,
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
