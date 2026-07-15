import os
import json
import csv

# === author imports / helpers ===
import csv, os, math

# Helper: linear interpolation of a sorted list of (x,y) points at target x.
def interpolate(pts, x):
    if len(pts) == 0:
        return None
    xi = [p[0] for p in pts]
    yi = [p[1] for p in pts]
    if x <= xi[0]:
        return yi[0]
    if x >= xi[-1]:
        return yi[-1]
    for i in range(len(xi)-1):
        if xi[i] <= x <= xi[i+1]:
            t = (x - xi[i]) / (xi[i+1] - xi[i])
            return yi[i] + t * (yi[i+1] - yi[i])
    return None


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
    return {"spec": spec}


# === block: score_0 (check id='step_power') ===
def score_0(artifact, step, ctx):
        step = ctx["spec"]["steps"][0]  # assumes step_power is first
        gold = step["probe_points"]
        rel_tol = step["relative_tolerance"]
        rows = artifact
        if not rows:
            return 0.0
        # extract Te and P from csv rows (cast to float)
        te_vals = []
        p_vals = []
        for r in rows:
            try:
                te = float(r["electron_temperature_K"])
                p = float(r["power_per_electron_W"])
                te_vals.append(te)
                p_vals.append(p)
            except (KeyError, ValueError):
                return 0.0
        # sort by Te
        pts = sorted(zip(te_vals, p_vals), key=lambda t: t[0])
        scores = []
        for te_str, gold_p in gold.items():
            te = float(te_str)
            agent_p = interpolate(pts, te)
            if agent_p is None or gold_p == 0.0:
                scores.append(0.0)
                continue
            err = abs(agent_p - gold_p) / max(abs(gold_p), 1e-15)
            scores.append(1.0 if err <= rel_tol else 0.0)
        return sum(scores) / len(scores)


# === block: score_1 (check id='step_velocity') ===
def score_1(artifact, step, ctx):
        step = ctx["spec"]["steps"][1]  # assumes step_velocity is second
        densities = step["densities"]
        probe_fields = step["probe_fields_kV_cm"]
        gold_vel = step["gold_velocities"]
        rel_tol_high = step["relative_tolerance_high"]
        high_thresh = step["high_velocity_threshold"]
        abs_tol_low = step["absolute_tolerance_low"]
        struct_w = step["structural_weights"]
        rows = artifact
        if not rows:
            return 0.0
        # parse rows
        data = []
        for r in rows:
            try:
                d = float(r["density_cm3"])
                f = float(r["field_kV_cm"])
                v = float(r["drift_velocity_cm_s"])
                data.append((d, f, v))
            except (KeyError, ValueError):
                return 0.0
        # group by density
        from collections import defaultdict
        density_groups = defaultdict(list)
        for d, f, v in data:
            density_groups[d].append((f, v))
        # accuracy score: for each density, interpolate at probe fields and compare
        point_scores = []
        for dens in densities:
            if dens not in density_groups:
                # missing density => score 0 for all its probe points
                point_scores.extend([0.0]*len(probe_fields))
                continue
            pts = sorted(density_groups[dens], key=lambda t: t[0])
            dens_key = f"{dens:.0e}"  # for gold lookup; normalize to e.g. '1e+18'
            if dens_key not in gold_vel:
                return 0.0
            gold_d = gold_vel[dens_key]
            for f in probe_fields:
                agent_v = interpolate(pts, f)
                if agent_v is None:
                    point_scores.append(0.0)
                    continue
                gold_v = float(gold_d[str(f)])
                if gold_v > high_thresh:
                    ok = (abs(agent_v - gold_v) / gold_v) <= rel_tol_high
                else:
                    ok = abs(agent_v - gold_v) <= abs_tol_low
                point_scores.append(1.0 if ok else 0.0)
        accuracy_score = sum(point_scores) / max(len(point_scores), 1)
        # monotonic with field: for each density, check velocity non-decreasing (allow small noise)
        monotonic_scores = []
        for dens in densities:
            if dens not in density_groups:
                monotonic_scores.append(0.0)
                continue
            pts = sorted(density_groups[dens], key=lambda t: t[0])
            velocities = [v for _, v in pts]
            non_decreasing = True
            for i in range(len(velocities)-1):
                if velocities[i+1] < velocities[i] - 1e5:  # tolerate 1e5 decrease
                    non_decreasing = False
                    break
            monotonic_scores.append(1.0 if non_decreasing else 0.0)
        monotonic_score = sum(monotonic_scores) / max(len(monotonic_scores), 1)
        # density ordering: at max probe field (250 kV/cm), higher density should have <= velocity
        max_field = probe_fields[-1]
        dens_vel = {}
        for dens in densities:
            if dens in density_groups:
                pts = sorted(density_groups[dens], key=lambda t: t[0])
                v = interpolate(pts, max_field)
                if v is not None:
                    dens_vel[dens] = v
        # check non-increasing with density
        order_ok = True
        sorted_dens = sorted(densities)
        for i in range(len(sorted_dens)-1):
            d1 = sorted_dens[i]
            d2 = sorted_dens[i+1]
            if d1 in dens_vel and d2 in dens_vel:
                if dens_vel[d2] > dens_vel[d1] + 1e5:  # tolerate small increase
                    order_ok = False
                    break
        density_order_score = 1.0 if order_ok else 0.0
        return struct_w["accuracy"] * accuracy_score + struct_w["monotonic_field"] * monotonic_score + struct_w["density_ordering"] * density_order_score


_SCORERS = {
    'step_power': score_0,
    'step_velocity': score_1,
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
