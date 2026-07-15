import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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


# === block: score_0 (check id='trapped_charge_5keV') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 5:
            return 0.0
        try:
            vals = [float(row['net_charge_density']) for row in artifact]
        except Exception:
            return 0.0
        # smooth with moving average window size 5
        smoothed = []
        for i in range(len(vals)):
            start = max(0, i-2)
            end = min(len(vals), i+3)
            smoothed.append(sum(vals[start:end]) / (end - start))
        vals = smoothed
        signs = []
        for v in vals:
            if v > 1e-12:
                signs.append(1)
            elif v < -1e-12:
                signs.append(-1)
            else:
                signs.append(0)
        sign_changes = 0
        last_nonzero = None
        for s in signs:
            if s == 0:
                continue
            if last_nonzero is not None and last_nonzero != s:
                sign_changes += 1
            last_nonzero = s
        first_nonzero = next((s for s in signs if s != 0), None)
        first_positive = (first_nonzero == 1)
        params = step.get('params', {})
        min_changes = params.get('min_sign_changes', 4)
        require_pos = params.get('require_first_positive', True)
        if sign_changes >= min_changes and (not require_pos or first_positive):
            return 1.0
        else:
            return 0.0


# === block: score_1 (check id='surface_potential_5keV') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 10:
            return 0.0
        times = []
        pots = []
        for row in artifact:
            try:
                times.append(float(row['time_ms']))
                pots.append(float(row['surface_potential_V']))
            except Exception:
                return 0.0
        v_final = pots[-1]
        params = step.get('params', {})
        target_min = params.get('target_min', -5000)
        target_max = params.get('target_max', -2000)
        range_ok = (v_final >= target_min and v_final <= target_max)
        n = len(pots)
        frac = 0.1
        start_idx = max(0, n - int(n * frac))
        recent_pots = pots[start_idx:]
        if len(recent_pots) < 2:
            return 1.0 if range_ok else 0.0
        total_range = max(pots) - min(pots)
        if total_range == 0:
            total_range = 1e-6
        recent_range = max(recent_pots) - min(recent_pots)
        convergence_ratio = recent_range / abs(total_range)
        threshold_ratio = params.get('convergence_threshold_ratio', 0.01)
        converged = convergence_ratio <= threshold_ratio
        range_weight = params.get('range_weight', 0.9)
        conv_weight = params.get('convergence_weight', 0.1)
        score = 0.0
        if range_ok:
            score += range_weight
        if converged:
            score += conv_weight
        return score


# === block: score_2 (check id='trapped_charge_10keV') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 5:
            return 0.0
        try:
            vals = [float(row['net_charge_density']) for row in artifact]
        except Exception:
            return 0.0
        smoothed = []
        for i in range(len(vals)):
            start = max(0, i-2)
            end = min(len(vals), i+3)
            smoothed.append(sum(vals[start:end]) / (end - start))
        vals = smoothed
        signs = []
        for v in vals:
            if v > 1e-12:
                signs.append(1)
            elif v < -1e-12:
                signs.append(-1)
            else:
                signs.append(0)
        sign_changes = 0
        last_nonzero = None
        for s in signs:
            if s == 0:
                continue
            if last_nonzero is not None and last_nonzero != s:
                sign_changes += 1
            last_nonzero = s
        first_nonzero = next((s for s in signs if s != 0), None)
        first_positive = (first_nonzero == 1)
        params = step.get('params', {})
        min_changes = params.get('min_sign_changes', 4)
        require_pos = params.get('require_first_positive', True)
        if sign_changes >= min_changes and (not require_pos or first_positive):
            return 1.0
        else:
            return 0.0


# === block: score_3 (check id='surface_potential_10keV') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 10:
            return 0.0
        times = []
        pots = []
        for row in artifact:
            try:
                times.append(float(row['time_ms']))
                pots.append(float(row['surface_potential_V']))
            except Exception:
                return 0.0
        v_final = pots[-1]
        params = step.get('params', {})
        target_min = params.get('target_min', -10000)
        target_max = params.get('target_max', -5000)
        range_ok = (v_final >= target_min and v_final <= target_max)
        n = len(pots)
        frac = 0.1
        start_idx = max(0, n - int(n * frac))
        recent_pots = pots[start_idx:]
        if len(recent_pots) < 2:
            return 1.0 if range_ok else 0.0
        total_range = max(pots) - min(pots)
        if total_range == 0:
            total_range = 1e-6
        recent_range = max(recent_pots) - min(recent_pots)
        convergence_ratio = recent_range / abs(total_range)
        threshold_ratio = params.get('convergence_threshold_ratio', 0.01)
        converged = convergence_ratio <= threshold_ratio
        range_weight = params.get('range_weight', 0.9)
        conv_weight = params.get('convergence_weight', 0.1)
        score = 0.0
        if range_ok:
            score += range_weight
        if converged:
            score += conv_weight
        return score


_SCORERS = {
    'trapped_charge_5keV': score_0,
    'surface_potential_5keV': score_1,
    'trapped_charge_10keV': score_2,
    'surface_potential_10keV': score_3,
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
