import os
import json
import csv

# === author imports / helpers ===
import json
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
    ctx = {}
    ctx['spec'] = spec
    return ctx


# === block: score_0 (check id='geometrical_contribution_recompute_std') ===
def score_0(artifact, step, ctx):
    try:
        counts = artifact.get("histogram_counts")
        edges = artifact.get("histogram_bin_edges")
        if not isinstance(counts, list) or not isinstance(edges, list) or len(edges) < 2:
            return 0.0
        if len(counts) != len(edges) - 1:
            return 0.0
        total = sum(counts)
        if total == 0:
            return 0.0
        centers = [(edges[i] + edges[i+1]) / 2.0 for i in range(len(edges)-1)]
        mean_w = sum(c * w for c, w in zip(centers, counts)) / total
        variance = sum(counts[i] * (centers[i] - mean_w) ** 2 for i in range(len(centers))) / total
        recomputed_std = math.sqrt(variance)
        ctx['_recomputed_std'] = recomputed_std
    except Exception:
        return 0.0
    target = step.get("target", 340.0)
    tolerance = step.get("tolerance_abs", 20.0)
    diff = abs(recomputed_std - target)
    if diff <= tolerance:
        score = 1.0
    else:
        decay = max(0.0, 1.0 - (diff - tolerance) / (3.0 * tolerance))
        score = decay
    return score


# === block: score_1 (check id='geometrical_contribution_internal_consistency') ===
def score_1(artifact, step, ctx):
    try:
        recomputed_std = ctx.get('_recomputed_std')
        if recomputed_std is None:
            counts = artifact.get("histogram_counts")
            edges = artifact.get("histogram_bin_edges")
            if not isinstance(counts, list) or not isinstance(edges, list) or len(edges) < 2:
                return 0.0
            if len(counts) != len(edges) - 1:
                return 0.0
            total = sum(counts)
            if total == 0:
                return 0.0
            centers = [(edges[i] + edges[i+1]) / 2.0 for i in range(len(edges)-1)]
            mean_w = sum(c * w for c, w in zip(centers, counts)) / total
            variance = sum(counts[i] * (centers[i] - mean_w) ** 2 for i in range(len(centers))) / total
            recomputed_std = math.sqrt(variance)
    except Exception:
        return 0.0
    reported_std = artifact.get("standard_deviation")
    if reported_std is None:
        return 0.0
    diff = abs(recomputed_std - reported_std)
    tol = step.get("tolerance_abs", 2.0)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_2 (check id='geometrical_contribution_shape_sanity') ===
def score_2(artifact, step, ctx):
    try:
        counts = artifact.get("histogram_counts")
        edges = artifact.get("histogram_bin_edges")
        if not isinstance(counts, list) or not isinstance(edges, list):
            return 0.0
        if len(counts) == 0 or sum(counts) == 0:
            return 0.0
        if any(el < 0 for el in counts):
            return 0.0
        if any(edges[i] >= edges[i+1] for i in range(len(edges)-1)):
            return 0.0
        max_idx = max(range(len(counts)), key=lambda i: counts[i])
        peak_center = (edges[max_idx] + edges[max_idx+1]) / 2.0
        low = step.get("expected_peak_low", 49800)
        high = step.get("expected_peak_high", 50200)
        if peak_center < low or peak_center > high:
            return 0.0
        return 1.0
    except Exception:
        return 0.0


_SCORERS = {
    'geometrical_contribution_recompute_std': score_0,
    'geometrical_contribution_internal_consistency': score_1,
    'geometrical_contribution_shape_sanity': score_2,
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
