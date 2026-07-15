import os
import json
import csv

# === author imports / helpers ===
import math
from collections import OrderedDict


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
    targets = {}
    for step in spec.get("steps", []):
        if step["id"] == "check_polarizability":
            targets["polar"] = {
                "targets": step["targets"],
                "tol_percent": step["tolerance_percent"]
            }
        elif step["id"] == "check_absorption_spectrum":
            targets["abs"] = {
                "target_bands": step["target_bands"],
                "n_bands": step["n_bands"]
            }
    return targets


# === block: score_0 (check id='check_polarizability') ===
def score_0(artifact, step, ctx):
    targets = ctx["polar"]["targets"]
    tol = ctx["polar"]["tol_percent"] / 100.0
    if not artifact:
        return 0.0
    rows_by_cluster = {}
    for row in artifact:
        cluster_name = row.get("cluster", "").strip()
        if cluster_name:
            rows_by_cluster[cluster_name] = row
    cluster_scores = []
    for cluster, ref in targets.items():
        if cluster not in rows_by_cluster:
            cluster_scores.append(0.0)
            continue
        row = rows_by_cluster[cluster]
        try:
            mean_alpha = float(row.get("mean_polarizability", 0))
            anisotropy = float(row.get("polarizability_anisotropy", 0))
            mean_gamma = float(row.get("mean_hyperpolarizability", 0))
        except (ValueError, TypeError):
            cluster_scores.append(0.0)
            continue
        ref_alpha = ref["mean_polarizability"]
        ref_aniso = ref["polarizability_anisotropy"]
        ref_gamma = ref["mean_hyperpolarizability"]
        hits = []
        if ref_alpha != 0:
            hits.append(1.0 if abs((mean_alpha - ref_alpha) / ref_alpha) <= tol else 0.0)
        else:
            hits.append(1.0 if mean_alpha == 0.0 else 0.0)
        if ref_aniso != 0:
            hits.append(1.0 if abs((anisotropy - ref_aniso) / ref_aniso) <= tol else 0.0)
        else:
            hits.append(1.0 if anisotropy == 0.0 else 0.0)
        if ref_gamma != 0:
            hits.append(1.0 if abs((mean_gamma - ref_gamma) / ref_gamma) <= tol else 0.0)
        else:
            hits.append(1.0 if mean_gamma == 0.0 else 0.0)
        cluster_scores.append(sum(hits) / len(hits))
    if not cluster_scores:
        return 0.0
    return sum(cluster_scores) / len(cluster_scores)


# === block: score_1 (check id='check_absorption_spectrum') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    target_bands = ctx["abs"]["target_bands"]
    n_bands = ctx["abs"]["n_bands"]
    # Extract data points
    points = []
    for row in artifact:
        try:
            wl = float(row.get("wavelength_nm", 0))
            osc = float(row.get("oscillator_strength", 0))
            points.append((wl, osc))
        except (ValueError, TypeError):
            continue
    if len(points) < n_bands:
        return 0.0
    # Sort by wavelength
    points.sort(key=lambda x: x[0])
    wavelengths = [p[0] for p in points]
    osc_strengths = [p[1] for p in points]
    # Find local maxima (strictly greater than adjacent points)
    local_maxima = []
    n = len(points)
    for i in range(n):
        left = osc_strengths[i-1] if i-1 >= 0 else -float('inf')
        right = osc_strengths[i+1] if i+1 < n else -float('inf')
        if osc_strengths[i] > left and osc_strengths[i] > right:
            local_maxima.append((i, wavelengths[i], osc_strengths[i]))
    if len(local_maxima) < n_bands:
        # fallback: take top by oscillator strength
        sorted_by_osc = sorted(enumerate(points), key=lambda x: x[1][1], reverse=True)
        top_indices = [sorted_by_osc[j][0] for j in range(min(n_bands, len(sorted_by_osc)))]
    else:
        sorted_maxima = sorted(local_maxima, key=lambda x: x[2], reverse=True)
        top_indices = [sorted_maxima[j][0] for j in range(n_bands)]
    # Extract selected points and sort by wavelength descending
    selected = sorted([points[i] for i in top_indices], key=lambda x: x[0], reverse=True)
    if len(selected) < n_bands:
        return 0.0
    matched = 0
    for idx, ref_band in enumerate(target_bands):
        if idx >= len(selected):
            break
        wl_computed = selected[idx][0]
        ref_wl = ref_band["wavelength_reference"]
        tol = ref_band["tolerance_nm"]
        if abs(wl_computed - ref_wl) <= tol:
            matched += 1
    return matched / n_bands


_SCORERS = {
    'check_polarizability': score_0,
    'check_absorption_spectrum': score_1,
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
