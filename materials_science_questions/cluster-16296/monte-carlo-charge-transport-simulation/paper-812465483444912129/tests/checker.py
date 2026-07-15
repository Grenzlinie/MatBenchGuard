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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        # Build lookup
        lookup = {}
        required_points = []
        eta_grid = step.get('params', {}).get('eta_grid', [])
        eps_vals = step.get('params', {}).get('epsilon_t_values', [0, 1, 10])
        for eta in eta_grid:
            for eps in eps_vals:
                required_points.append((eta, eps))
        # Check existence of all required points
        for point in artifact:
            try:
                eta = float(point['eta'])
                eps = float(point['epsilon_t'])
                f = float(point['F'])
                lookup[(eta, eps)] = f
            except (KeyError, TypeError, ValueError):
                continue
        missing = []
        for eta, eps in required_points:
            if (eta, eps) not in lookup:
                missing.append((eta, eps))
        # Points existence sub-score
        points_ok = (len(missing) == 0)
        # Check specific points
        eta0_eps0_range = step.get('params', {}).get('criterion_eta0_eps0_range', [0.6, 1.2])
        eta0_eps10_range = step.get('params', {}).get('criterion_eta0_eps10_range', [50, 200])
        ratio_range = step.get('params', {}).get('criterion_ratio_range', [50, 200])
        f00 = lookup.get((0.0, 0))
        f010 = lookup.get((0.0, 10))
        specific_ok = (f00 is not None and eta0_eps0_range[0] <= f00 <= eta0_eps0_range[1] and
                       f010 is not None and eta0_eps10_range[0] <= f010 <= eta0_eps10_range[1] and
                       f010 / f00 >= ratio_range[0] and f010 / f00 <= ratio_range[1])
        # Monotonic in eta for each epsilon_t
        eta_mono_ok = True
        for eps in eps_vals:
            pairs = [(eta, lookup[(eta, eps)]) for eta in eta_grid if (eta, eps) in lookup]
            pairs.sort(key=lambda x: x[0])
            for i in range(len(pairs)-1):
                if pairs[i+1][1] < pairs[i][1] - 1e-9 * max(abs(pairs[i][1]), abs(pairs[i+1][1])):
                    eta_mono_ok = False
                    break
            if not eta_mono_ok:
                break
        # Monotonic in epsilon_t for each eta
        eps_mono_ok = True
        for eta in eta_grid:
            f0 = lookup.get((eta, 0))
            f1 = lookup.get((eta, 1))
            f10 = lookup.get((eta, 10))
            if f0 is None or f1 is None or f10 is None:
                continue
            if not (f0 <= f1 + 1e-9 and f1 <= f10 + 1e-9):
                eps_mono_ok = False
                break
        # Compute total score
        total = 0.0
        if points_ok and specific_ok:
            total += 0.3
        if eta_mono_ok:
            total += 0.3
        if eps_mono_ok:
            total += 0.4
        return total


_SCORERS = {
    'step_01': score_0,
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
