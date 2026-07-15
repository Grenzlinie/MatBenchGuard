import os
import json
import csv

# === author imports / helpers ===
import math
import csv
from pathlib import Path


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


# === block: score_0 (check id='sigma13_check') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            pre = float(artifact.get("pre_relaxation_energy"))
            rel = float(artifact.get("relaxed_energy"))
        except (TypeError, ValueError, KeyError):
            return 0.0
        pre_target = float(step["hidden"]["pre_relaxation_target"])
        rel_target = float(step["hidden"]["relaxed_energy_target"])
        pre_tol = float(step["hidden"]["pre_tolerance_relative"])
        rel_tol = float(step["hidden"]["rel_tolerance_relative"])
        self_thresh = float(step["hidden"]["self_consistency_threshold"])

        pre_err = abs(pre - pre_target) / (pre_tol * pre_target) if pre_target != 0 else 1e9
        rel_err = abs(rel - rel_target) / (rel_tol * rel_target) if rel_target != 0 else 1e9

        pre_score = max(0.0, 1.0 - pre_err)
        rel_score = max(0.0, 1.0 - rel_err)

        if rel == 0:
            self_score = 0.0
        else:
            self_ok = (abs(pre - rel) / abs(rel)) <= self_thresh
            self_score = 1.0 if self_ok else 0.0

        return (pre_score + rel_score + self_score) / 3.0


# === block: score_1 (check id='energy_curve_check') ===
def score_1(artifact, step, ctx):
    def score(artifact_rows, step, ctx):
        if not artifact_rows:
            return 0.0
        try:
            angles = []
            relaxed = []
            pre = []
            for row in artifact_rows:
                ang = float(row["misorientation_angle_deg"])
                rel = float(row["relaxed_energy"])
                pre_e = float(row["pre_relaxation_energy"])
                if not (0 <= ang <= 180 and rel > 0 and pre_e > 0):
                    return 0.0
                angles.append(ang)
                relaxed.append(rel)
                pre.append(pre_e)
        except (KeyError, ValueError):
            return 0.0

        # sort by angle
        sorted_idx = sorted(range(len(angles)), key=lambda i: angles[i])
        angles = [angles[i] for i in sorted_idx]
        relaxed = [relaxed[i] for i in sorted_idx]
        pre = [pre[i] for i in sorted_idx]

        # find index of max relaxed energy
        max_rel = max(relaxed)
        max_idx = relaxed.index(max_rel)

        max_range = step["hidden"]["max_angle_range"]
        max_angle_ok = 1.0 if max_range[0] <= angles[max_idx] <= max_range[1] else 0.0

        def monotonic_convex(lst):
            if max_idx == 0 or max_idx == len(lst) - 1:
                return 0.0
            # increasing up to max_idx (allow equal)
            for i in range(max_idx):
                if lst[i] > lst[i+1] + 1e-9:
                    return 0.0
            # decreasing after max_idx
            for i in range(max_idx, len(lst)-1):
                if lst[i] < lst[i+1] - 1e-9:
                    return 0.0
            return 1.0

        relaxed_convex = monotonic_convex(relaxed)
        pre_convex = monotonic_convex(pre)

        total = (max_angle_ok + relaxed_convex + pre_convex) / 3.0
        return total


_SCORERS = {
    'sigma13_check': score_0,
    'energy_curve_check': score_1,
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
