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
        return {
            "saturation_target": 34.0,
            "saturation_tol": 2.0,
            "threshold_frac": 0.9,
            "min_derivative": 5.0,
        }


# === block: score_0 (check id='check_low_current_monotonic') ===
def score_0(artifact, step, ctx):
        nd_order = [0.0, 1e16, 1e17, 1e18]
        groups = {nd: [] for nd in nd_order}
        for row in artifact:
            try:
                nd_val = float(row["N_D"])
            except Exception:
                continue
            j = float(row["current_density"])
            de = float(row["dE_E_dp"])
            # assign to the nearest expected N_D
            diff = min( (abs(nd_val - ref), ref) for ref in nd_order )
            if diff[0] < 0.1 * min(abs(r) for r in nd_order if r != 0):  # tolerance: 10% of smallest non-zero
                groups[diff[1]].append((j, de))
        de_at_min = []
        for nd in nd_order:
            if not groups[nd]:
                return 0.0
            pts = sorted(groups[nd], key=lambda x: x[0])
            de_at_min.append(pts[0][1])
        for i in range(1, len(de_at_min)):
            if de_at_min[i] <= de_at_min[i-1]:
                return 0.0
        return 1.0


# === block: score_1 (check id='check_saturation') ===
def score_1(artifact, step, ctx):
        sat = ctx.get("saturation_target", 34.0)
        tol = ctx.get("saturation_tol", 2.0)
        groups = {}
        for row in artifact:
            nd = int(round(float(row["N_D"])))
            j = float(row["current_density"])
            de = float(row["dE_E_dp"])
            groups.setdefault(nd, []).append((j, de))
        nd_order = [0, 10000000000000000, 100000000000000000, 1000000000000000000]
        for nd in nd_order:
            if nd not in groups:
                return 0.0
            pts = sorted(groups[nd], key=lambda x: x[0])
            max_de = pts[-1][1]
            if not (sat - tol <= max_de <= sat + tol):
                return 0.0
        return 1.0


# === block: score_2 (check id='check_saturation_current_threshold') ===
def score_2(artifact, step, ctx):
        sat = ctx.get("saturation_target", 34.0)
        frac = ctx.get("threshold_frac", 0.9)
        target_de = sat * frac
        groups = {}
        for row in artifact:
            nd = int(round(float(row["N_D"])))
            j = float(row["current_density"])
            de = float(row["dE_E_dp"])
            groups.setdefault(nd, []).append((j, de))
        nd_order = [0, 10000000000000000, 100000000000000000, 1000000000000000000]
        threshold_currents = []
        for nd in nd_order:
            if nd not in groups:
                return 0.0
            pts = sorted(groups[nd], key=lambda x: x[0])
            found = False
            for j, de in pts:
                if de >= target_de:
                    threshold_currents.append(j)
                    found = True
                    break
            if not found:
                return 0.0
        for i in range(1, len(threshold_currents)):
            if threshold_currents[i] >= threshold_currents[i-1]:
                return 0.0
        return 1.0


# === block: score_3 (check id='check_steplike_derivative') ===
def score_3(artifact, step, ctx):
        import math
        min_der = ctx.get("min_derivative", 5.0)
        groups = {}
        for row in artifact:
            nd = int(round(float(row["N_D"])))
            j = float(row["current_density"])
            de = float(row["dE_E_dp"])
            groups.setdefault(nd, []).append((j, de))
        nd_order = [0, 10000000000000000, 100000000000000000, 1000000000000000000]
        passes = 0
        for nd in nd_order:
            if nd not in groups:
                continue
            pts = sorted(groups[nd], key=lambda x: x[0])
            if len(pts) < 3:
                continue
            max_der = 0.0
            for i in range(1, len(pts)):
                dj = math.log10(pts[i][0]) - math.log10(pts[i-1][0])
                if dj == 0:
                    continue
                der = (pts[i][1] - pts[i-1][1]) / dj
                if der > max_der:
                    max_der = der
            if max_der >= min_der:
                passes += 1
        return passes / max(1, len(nd_order))


_SCORERS = {
    'check_low_current_monotonic': score_0,
    'check_saturation': score_1,
    'check_saturation_current_threshold': score_2,
    'check_steplike_derivative': score_3,
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
