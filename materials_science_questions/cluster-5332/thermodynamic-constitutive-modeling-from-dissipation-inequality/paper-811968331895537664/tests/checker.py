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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    GAMMA = step.get('config', {}).get('gamma', 0.2)
    RHO = step.get('config', {}).get('rho', 0.3)
    TOL = step.get('config', {}).get('tolerance_abs', 0.01)
    MIN_PTS = step.get('config', {}).get('min_points', 50)

    if not artifact or len(artifact) < MIN_PTS:
        return 0.0

    ok = 0
    for row in artifact:
        try:
            eta = float(row['eta'])
            n = float(row['n'])
            m = float(row['m'])
        except (ValueError, KeyError):
            continue
        if abs(eta - RHO) < 1e-6:
            # subdifferential segment
            n_tens = GAMMA - (1.0 + RHO) / 2.0
            m_tens = 2.0 * GAMMA * RHO + (1.0 - RHO * RHO) / 2.0
            n_comp = -GAMMA - (1.0 + RHO) / 2.0
            m_comp = -2.0 * GAMMA * RHO + (1.0 - RHO * RHO) / 2.0
            if abs(n_comp - n_tens) < 1e-12:
                ok += 0  # degenerate, skip
                continue
            slope = (m_comp - m_tens) / (n_comp - n_tens)
            intercept = m_tens - slope * n_tens
            expected_m = slope * n + intercept
            n_min = min(n_tens, n_comp)
            n_max = max(n_tens, n_comp)
            if n_min - TOL <= n <= n_max + TOL and abs(m - expected_m) <= TOL:
                ok += 1
        elif eta < RHO:
            exp_n = GAMMA - (1.0 + eta) / 2.0
            exp_m = 2.0 * GAMMA * RHO + (1.0 - eta * eta) / 2.0
            if abs(n - exp_n) <= TOL and abs(m - exp_m) <= TOL:
                ok += 1
        else:
            exp_n = -GAMMA - (1.0 + eta) / 2.0
            exp_m = -2.0 * GAMMA * RHO + (1.0 - eta * eta) / 2.0
            if abs(n - exp_n) <= TOL and abs(m - exp_m) <= TOL:
                ok += 1

    if len(artifact) == 0:
        return 0.0
    score = ok / len(artifact)
    return min(score, 1.0)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    GAMMA = step.get('config', {}).get('gamma', 0.2)
    RHO = step.get('config', {}).get('rho', 0.3)
    TOL = step.get('config', {}).get('tolerance_abs', 0.01)
    MIN_PTS = step.get('config', {}).get('min_points', 50)

    if not artifact or len(artifact) < MIN_PTS:
        return 0.0

    ok = 0
    for row in artifact:
        try:
            eta = float(row['eta'])
            n = float(row['n'])
            m = float(row['m'])
        except (ValueError, KeyError):
            continue
        if abs(eta + RHO) < 1e-6:
            # lower symmetric segment
            n_outer = -(1.0 + (-RHO)) / 2.0 - 2.0 * GAMMA
            m_outer = (1.0 - (-RHO) * (-RHO)) / 2.0
            n_inner = -(1.0 + (-RHO)) / 2.0
            m_inner = (1.0 - (-RHO) * (-RHO)) / 2.0 + 4.0 * GAMMA * RHO
            if abs(n_inner - n_outer) < 1e-12:
                ok += 0
                continue
            slope = (m_inner - m_outer) / (n_inner - n_outer)
            intercept = m_outer - slope * n_outer
            expected_m = slope * n + intercept
            n_min = min(n_outer, n_inner)
            n_max = max(n_outer, n_inner)
            if n_min - TOL <= n <= n_max + TOL and abs(m - expected_m) <= TOL:
                ok += 1
        elif abs(eta - RHO) < 1e-6:
            # upper symmetric segment
            n_inner = -(1.0 + RHO) / 2.0
            m_inner = (1.0 - RHO * RHO) / 2.0 + 4.0 * GAMMA * RHO
            n_outer = -(1.0 + RHO) / 2.0 - 2.0 * GAMMA
            m_outer = (1.0 - RHO * RHO) / 2.0
            if abs(n_outer - n_inner) < 1e-12:
                ok += 0
                continue
            slope = (m_outer - m_inner) / (n_outer - n_inner)
            intercept = m_inner - slope * n_inner
            expected_m = slope * n + intercept
            n_min = min(n_inner, n_outer)
            n_max = max(n_inner, n_outer)
            if n_min - TOL <= n <= n_max + TOL and abs(m - expected_m) <= TOL:
                ok += 1
        elif eta < -RHO:
            exp_n = -(1.0 + eta) / 2.0 - 2.0 * GAMMA
            exp_m = (1.0 - eta * eta) / 2.0
            if abs(n - exp_n) <= TOL and abs(m - exp_m) <= TOL:
                ok += 1
        elif -RHO < eta < RHO:
            exp_n = -(1.0 + eta) / 2.0
            exp_m = (1.0 - eta * eta) / 2.0 + 4.0 * GAMMA * RHO
            if abs(n - exp_n) <= TOL and abs(m - exp_m) <= TOL:
                ok += 1
        else:  # eta > RHO
            exp_n = -(1.0 + eta) / 2.0 - 2.0 * GAMMA
            exp_m = (1.0 - eta * eta) / 2.0
            if abs(n - exp_n) <= TOL and abs(m - exp_m) <= TOL:
                ok += 1

    if len(artifact) == 0:
        return 0.0
    score = ok / len(artifact)
    return min(score, 1.0)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
