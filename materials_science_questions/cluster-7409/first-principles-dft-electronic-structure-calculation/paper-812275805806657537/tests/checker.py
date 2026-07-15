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


# === block: score_0 (check id='band_gaps') ===
def score_0(artifact, step, ctx):
    def score_band_gaps(artifact, step, ctx):
        perfect_gap = artifact.get("perfect_gap_ev")
        defect_gap = artifact.get("defect_gap_ev")
        if perfect_gap is None or defect_gap is None:
            return 0.0
        try:
            perfect_gap = float(perfect_gap)
            defect_gap = float(defect_gap)
        except (TypeError, ValueError):
            return 0.0
        target_perfect = step["target_perfect_gap_ev"]
        tol_perf = step["tolerance_perfect_gap_ev"]
        target_defect = step["target_defect_gap_ev"]
        tol_def = step["tolerance_defect_gap_ev"]
        def score_val(value, target, tol):
            abs_err = abs(value - target)
            if abs_err <= tol:
                return 1.0
            excess = abs_err - tol
            return max(0.0, 1.0 - excess / tol)
        s1 = score_val(perfect_gap, target_perfect, tol_perf)
        s2 = score_val(defect_gap, target_defect, tol_def)
        return (s1 + s2) / 2.0


# === block: score_1 (check id='in_gap_state') ===
def score_1(artifact, step, ctx):
    def score_in_gap_state(artifact, step, ctx):
        energy = artifact.get("in_gap_state_energy_ev")
        if energy is None:
            return 0.0
        try:
            energy = float(energy)
        except (TypeError, ValueError):
            return 0.0
        target = step["target_in_gap_state_energy_ev"]
        tol = step["tolerance_in_gap_state_ev"]
        abs_err = abs(energy - target)
        if abs_err <= tol:
            return 1.0
        excess = abs_err - tol
        return max(0.0, 1.0 - excess / tol)


# === block: score_2 (check id='absorption_peaks') ===
def score_2(artifact, step, ctx):
    def score_absorption_peaks(artifact, step, ctx):
        peaks = artifact.get("peaks")
        if not isinstance(peaks, list) or len(peaks) != 7:
            return 0.0
        if not all(isinstance(p, (int, float)) for p in peaks):
            return 0.0
        if sorted(peaks) != list(peaks):
            return 0.0
        target = step["target_peaks"]
        max_dev = max(abs(float(p) - float(t)) for p, t in zip(peaks, target))
        if max_dev <= 0.1:
            return 1.0
        if max_dev >= 0.3:
            return 0.0
        return (0.3 - max_dev) / 0.2


_SCORERS = {
    'band_gaps': score_0,
    'in_gap_state': score_1,
    'absorption_peaks': score_2,
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
