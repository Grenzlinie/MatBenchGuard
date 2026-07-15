import os
import json
import csv


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


# === block: score_0 (check id='mc_simulation_d0') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts
    max_chi = -float('inf')
    tc_found = None
    for row in artifact:
        try:
            t = float(row['T'])
            chi = float(row['susceptibility'])
            if chi > max_chi:
                max_chi = chi
                tc_found = t
        except (ValueError, KeyError):
            continue
    if tc_found is None:
        return 0.0
    target = step['target']
    tol = step['tolerance']
    diff = abs(tc_found - target)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 1.0 - (diff - tol) / tol
    else:
        return 0.0


# === block: score_1 (check id='phase_diagram') ===
def score_1(artifact, step, ctx):
    artifact = artifact  # list of dicts
    target = step['target']
    tol = step['tolerance']
    check_points = step['check_points']
    D0 = target['D0']; Tc0 = target['Tc0']; Dt = target['Dt']; Tct = target['Tct']
    slope = (Tc0 - Tct) / (D0 - Dt)
    def expected_tc(D):
        return Tc0 + slope * D
    scores = []
    for D_check in check_points:
        tc_exp = expected_tc(D_check)
        found = False
        best_diff = None
        for row in artifact:
            try:
                D_val = float(row['D_J'])
                Tc_val = float(row['Tc_J'])
                if abs(D_val - D_check) <= 0.05:
                    found = True
                    diff = abs(Tc_val - tc_exp)
                    if best_diff is None or diff < best_diff:
                        best_diff = diff
            except:
                pass
        if found and best_diff is not None:
            if best_diff <= tol:
                scores.append(1.0)
            elif best_diff <= 2 * tol:
                scores.append(1.0 - (best_diff - tol) / tol)
            else:
                scores.append(0.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='tricritical_point') ===
def score_2(artifact, step, ctx):
    artifact = artifact  # dict
    target = step['target']
    tol = step['tolerance']
    diff_d = abs(artifact.get('D_t_J', 999) - target['D_t_J'])
    diff_t = abs(artifact.get('T_t_J', 999) - target['T_t_J'])
    def score_diff(diff):
        if diff <= tol:
            return 1.0
        elif diff <= 2 * tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0
    s_d = score_diff(diff_d)
    s_t = score_diff(diff_t)
    return (s_d + s_t) / 2.0


_SCORERS = {
    'mc_simulation_d0': score_0,
    'phase_diagram': score_1,
    'tricritical_point': score_2,
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
