import os
import json
import csv

# === author imports / helpers ===
import csv
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


# === block: score_0 (check id='neon_wetting_check') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts with columns: temperature_K, well_depth_D_K, pressure, coverage
    # step contains conditions_expected, wetting_threshold_ratio, nonwetting_threshold_ratio
    if not artifact or len(artifact) == 0:
        return 0.0
    try:
        # parse all coverage values, find overall max
        covs = []
        for row in artifact:
            cov = float(row['coverage'])
            covs.append(cov)
        if not covs:
            return 0.0
        overall_max = max(covs)
        if overall_max == 0:
            return 0.0
        # group by (temperature_K, well_depth_D_K)
        groups = {}
        for row in artifact:
            t = int(row['temperature_K'])
            d = float(row['well_depth_D_K'])
            cov = float(row['coverage'])
            key = (t, d)
            if key not in groups:
                groups[key] = []
            groups[key].append(cov)
        expected = step['conditions_expected']
        wet_thr = step['wetting_threshold_ratio']
        nonwet_thr = step['nonwetting_threshold_ratio']
        correct = 0
        total = len(expected)
        if total == 0:
            return 1.0
        for cond in expected:
            t = cond['temperature_K']
            d = cond['well_depth_D_K']
            key = (t, d)
            if key not in groups:
                continue  # miss
            max_cov = max(groups[key])
            ratio = max_cov / overall_max
            is_wet = cond['expected_wetting']
            if is_wet and ratio >= wet_thr:
                correct += 1
            elif not is_wet and ratio <= nonwet_thr:
                correct += 1
            else:
                # could be borderline, penalize
                pass
        return correct / total
    except Exception as e:
        # any parse/read error yields 0
        return 0.0


# === block: score_1 (check id='hydrogen_jump_check') ===
def score_1(artifact, step, ctx):
    # artifact: list of dicts columns: temperature_K, reduced_chemical_potential, coverage
    # step contains temperature_checks
    if not artifact or len(artifact) == 0:
        return 0.0
    try:
        # group by temperature
        from collections import defaultdict
        groups = defaultdict(list)
        for row in artifact:
            t = int(row['temperature_K'])
            mu = float(row['reduced_chemical_potential'])
            cov = float(row['coverage'])
            groups[t].append( (mu, cov) )
        # compute global maximum coverage across all rows (used for saturation check at 30 K)
        global_max = max(float(row['coverage']) for row in artifact) if artifact else 0.0
        checks = step['temperature_checks']
        if not checks:
            return 1.0
        correct = 0
        for tc in checks:
            t = tc['temperature_K']
            if t not in groups:
                continue
            points = groups[t]
            if len(points) < 2:
                continue
            points.sort(key=lambda x: x[0])  # sort by mu
            cov_values = [c for _, c in points]
            mu_values = [m for m, _ in points]
            min_c = min(cov_values)
            max_c = max(cov_values)
            total_range = max_c - min_c
            if total_range <= 0:
                # all same coverage, can't detect jump
                # for expected_jump False, that might be ok; for True it's wrong
                if tc.get('expected_jump', True):
                    continue  # fail
                else:
                    # flat coverage cannot be continuous growth with saturation; skip
                    continue
            if tc.get('expected_jump', True):
                # find largest absolute jump between consecutive mu points
                max_jump = 0
                jump_idx = 0
                for i in range(1, len(points)):
                    jump = abs(cov_values[i] - cov_values[i-1])
                    if jump > max_jump:
                        max_jump = jump
                        jump_idx = i
                # require that jump is > 80% of total increase
                if max_jump < 0.8 * total_range:
                    continue  # no clear single large jump
                # check that the mu at which jump occurs (we take the start mu of the interval)
                # lies within tolerance of gold interval
                mu_start = mu_values[jump_idx-1]
                mu_end = mu_values[jump_idx]
                gs = tc['jump_interval_mu_start']
                ge = tc['jump_interval_mu_end']
                tol = tc.get('tolerance', 0.02)
                if (mu_start >= gs - tol) and (mu_end <= ge + tol):
                    correct += 1
            else:
                # expected continuous growth (no large jump)
                max_rel_jump = 0
                for i in range(1, len(points)):
                    jump = abs(cov_values[i] - cov_values[i-1])
                    rel = jump / max_c if max_c > 0 else 0
                    if rel > max_rel_jump:
                        max_rel_jump = rel
                max_allowed = tc.get('max_jump_ratio', 0.2)
                if max_rel_jump <= max_allowed:
                    # additionally verify that coverage reaches near-saturation level
                    # (at least 80% of the global maximum coverage across all temperatures)
                    if global_max > 0 and max_c >= 0.8 * global_max:
                        correct += 1
        return correct / len(checks)
    except Exception as e:
        return 0.0


_SCORERS = {
    'neon_wetting_check': score_0,
    'hydrogen_jump_check': score_1,
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
