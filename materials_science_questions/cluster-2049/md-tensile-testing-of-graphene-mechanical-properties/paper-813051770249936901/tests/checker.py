import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='ambient_elastic_constants') ===
def score_0(artifact, step, ctx):
    try:
        lines = artifact.strip().splitlines()
        if len(lines) < 2:
            return 0.0
        C11 = float(lines[0].strip())
        C12 = float(lines[1].strip())
    except:
        return 0.0

    tol = step.get('tolerance_relative', 0.15)
    exp_C11 = step['expected_C11']
    exp_C12 = step['expected_C12']

    def check(val, expected):
        if expected == 0:
            return abs(val) <= 1e-9
        return abs(val - expected) / abs(expected) <= tol

    score = 0.0
    if check(C11, exp_C11):
        score += 1.0
    if check(C12, exp_C12):
        score += 1.0
    return score / 2.0


# === block: score_1 (check id='mechanical_stability_thresholds') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0

    agent_dict = {}
    for row in rows:
        lt = row.get('loading_type', '').strip().lower()
        if lt not in ('zigzag', 'armchair', 'biaxial'):
            continue
        vals = {}
        for col in ['compressive_stability_limit_Nm', 'tensile_stability_limit_Nm', 'compressive_failure_stress_Nm']:
            raw = row.get(col, '').strip()
            if raw == '' or raw is None:
                vals[col] = None
            else:
                try:
                    vals[col] = float(raw)
                except:
                    vals[col] = None
        agent_dict[lt] = vals

    expected_rows = step.get('expected_rows', [])
    tol = step.get('tolerance_absolute', 10.0)

    total_checks = 0
    passed_checks = 0

    for exp in expected_rows:
        lt = exp['loading_type']
        if lt not in agent_dict:
            total_checks += 3  # penalize missing row entirely
            continue
        agent_vals = agent_dict[lt]
        for col in ['compressive_stability_limit_Nm', 'tensile_stability_limit_Nm', 'compressive_failure_stress_Nm']:
            exp_val = exp.get(col)
            if exp_val is None:
                total_checks += 1
                if agent_vals.get(col) is None:
                    passed_checks += 1
                # else missing expected non-value counts as fail (but we do not increment passed)
            else:
                total_checks += 1
                agent_v = agent_vals.get(col)
                if agent_v is not None and abs(agent_v - exp_val) <= tol:
                    passed_checks += 1

    if total_checks == 0:
        return 0.0
    return passed_checks / total_checks


# === block: score_2 (check id='ultimate_tensile_strength') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0

    agent_dict = {}
    for row in rows:
        lt = row.get('loading_type', '').strip().lower()
        if lt not in ('zigzag', 'armchair', 'biaxial'):
            continue
        try:
            val = float(row.get('UTS_Nm', ''))
        except:
            continue
        agent_dict[lt] = val

    expected_rows = step.get('expected_rows', [])
    tol = step.get('tolerance_absolute', 2.0)

    correct = 0
    total = 0
    for exp in expected_rows:
        total += 1
        lt = exp['loading_type']
        expected = exp['UTS_Nm']
        if lt in agent_dict and abs(agent_dict[lt] - expected) <= tol:
            correct += 1

    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='band_gap_vs_stress') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0

    # parse agent data into list of (loading_type, stress, gap)
    agent_points = []
    for row in rows:
        lt = row.get('loading_type', '').strip().lower()
        if lt not in ('zigzag', 'armchair', 'biaxial'):
            continue
        try:
            stress = float(row.get('stress_Nm', ''))
            gap = float(row.get('band_gap_eV', ''))
        except:
            continue
        agent_points.append((lt, stress, gap))

    expected_points = step.get('expected_points', [])
    tol_stress = step.get('tolerance_stress', 15.0)
    tol_gap = step.get('tolerance_gap', 0.2)

    total = len(expected_points)
    if total == 0:
        return 0.0

    matched = 0
    for exp in expected_points:
        elt = exp['loading_type']
        es = exp['stress_Nm']
        eg = exp['band_gap_eV']
        # check if any agent point matches
        for apt in agent_points:
            alt, as_, ag = apt
            if alt == elt and abs(as_ - es) <= tol_stress:
                # gap tolerance
                if abs(ag - eg) <= tol_gap:
                    matched += 1
                    break
                # also handle metallic case: if expected gap 0, also accept very small gap (<0.1)
                if eg == 0 and abs(ag - 0) <= tol_gap:
                    matched += 1
                    break

    return matched / total


# === block: score_4 (check id='charge_analysis') ===
def score_4(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0

    atom = artifact.get('max_charge_density_atom', '').strip()
    val = artifact.get('max_charge_density_value')

    try:
        val = float(val)
    except (TypeError, ValueError):
        return 0.0

    exp_atom = step.get('expected_atom', 'C')
    min_val = step.get('min_density_value', 7.0)

    score = 0.0
    if atom == exp_atom:
        score += 0.5
    if val >= min_val:
        score += 0.5
    return score


_SCORERS = {
    'ambient_elastic_constants': score_0,
    'mechanical_stability_thresholds': score_1,
    'ultimate_tensile_strength': score_2,
    'band_gap_vs_stress': score_3,
    'charge_analysis': score_4,
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
