import os
import json
import csv

# === author imports / helpers ===
import json, os, csv, math


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


# === block: score_0 (check id='step_01_critical_expansion') ===
def score_0(artifact, step, ctx):
    d_target = step["target"]["critical_delta_d_d0"]["value"]
    d_tol = step["target"]["critical_delta_d_d0"]["tolerance_abs"]
    v_target = step["target"]["critical_delta_V_V0"]["value"]
    v_tol = step["target"]["critical_delta_V_V0"]["tolerance_abs"]
    val_d = artifact.get("critical_delta_d_d0")
    val_v = artifact.get("critical_delta_V_V0")
    s1 = 1.0 if (val_d is not None and abs(val_d - d_target) <= d_tol) else 0.0
    s2 = 1.0 if (val_v is not None and abs(val_v - v_target) <= v_tol) else 0.0
    return (s1 + s2) / 2.0


# === block: score_1 (check id='step_02_wavefunction_distribution') ===
def score_1(artifact, step, ctx):
        rows = artifact  # list of dict objects from CSV
        params = step.get("params", {})
        required_states = params.get("required_states", [])
        required_deltas = params.get("required_deltas", [])
        relaxed_z_range = params.get("relaxed_z_range", [1,10])
        opposite_z_range = params.get("opposite_z_range", [91,100])
        thresholds = params.get("thresholds", {})

        # Convert rows to typed tuples (state, z, delta, prob)
        typed_rows = []
        for r in rows:
            try:
                state = r.get("state", "").strip()
                z = int(r["z_BL"])
                delta = float(r["delta_d_d0"])
                prob = float(r["prob"])
                typed_rows.append((state, z, delta, prob))
            except (ValueError, KeyError):
                continue

        def prob_sum(state, delta, z_list):
            return sum(p for s, z, d, p in typed_rows if s == state and abs(d - delta) < 1e-6 and z in z_list)

        relaxed_z = list(range(relaxed_z_range[0], relaxed_z_range[1]+1))
        opposite_z = list(range(opposite_z_range[0], opposite_z_range[1]+1))

        scores = []

        # Condition for delta = 0.002 (below critical): probability on both surfaces > 0.1
        th_002 = thresholds.get("delta_0_002", {})
        min_rel_002 = th_002.get("min_prob_relaxed", 0.1)
        min_opp_002 = th_002.get("min_prob_opposite", 0.1)
        for state in required_states:
            p_rel = prob_sum(state, 0.002, relaxed_z)
            p_opp = prob_sum(state, 0.002, opposite_z)
            scores.append(1.0 if p_rel > min_rel_002 and p_opp > min_opp_002 else 0.0)

        # Condition for delta = 0.03 (above critical): relaxed side < 0.01, opposite side > 0.1
        th_03 = thresholds.get("delta_0_03", {})
        max_rel_03 = th_03.get("max_prob_relaxed", 0.01)
        min_opp_03 = th_03.get("min_prob_opposite", 0.1)
        for state in required_states:
            p_rel = prob_sum(state, 0.03, relaxed_z)
            p_opp = prob_sum(state, 0.03, opposite_z)
            scores.append(1.0 if p_rel < max_rel_03 and p_opp > min_opp_03 else 0.0)

        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='step_03_spatial_spectrum') ===
def score_2(artifact, step, ctx):
    target = step.get("target", {})
    sub_weights = step.get("sub_weights", {"blocking_ratio_100BL": 1.0})
    score_total = 0.0

    # blocking_ratio
    ratio = artifact.get("blocking_ratio_100BL")
    if ratio is not None and "blocking_ratio_100BL" in target:
        t = target["blocking_ratio_100BL"]
        if abs(ratio - t["value"]) <= t["tolerance_abs"]:
            score_total += sub_weights.get("blocking_ratio_100BL", 0.0)

    # relaxed peak weight
    rpw = artifact.get("surface_peak_weight_relaxed")
    if rpw is not None and "surface_peak_weight_relaxed" in target:
        t = target["surface_peak_weight_relaxed"]
        if abs(rpw - t["value"]) <= t["tolerance_abs"]:
            score_total += sub_weights.get("surface_peak_weight_relaxed", 0.0)

    # unrelaxed peak weight
    upw = artifact.get("surface_peak_weight_unrelaxed")
    if upw is not None and "surface_peak_weight_unrelaxed" in target:
        t = target["surface_peak_weight_unrelaxed"]
        if abs(upw - t["value"]) <= t["tolerance_abs"]:
            score_total += sub_weights.get("surface_peak_weight_unrelaxed", 0.0)

    return score_total


_SCORERS = {
    'step_01_critical_expansion': score_0,
    'step_02_wavefunction_distribution': score_1,
    'step_03_spatial_spectrum': score_2,
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
