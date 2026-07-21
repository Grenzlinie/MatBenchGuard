import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os


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


# === block: score_0 (check id='step_csv') ===
def score_0(artifact, step, ctx):
        required = {"coefficient_of_velocity", "coefficient_of_dimension", "delta_N_N_max", "ratio_v_to_v0"}
        if not artifact or not isinstance(artifact, list) or not artifact:
            return 0.0
        if not set(artifact[0].keys()).issuperset(required):
            return 0.0

        # Build data structures
        from collections import defaultdict
        data = defaultdict(list)
        for row in artifact:
            try:
                cv = float(row["coefficient_of_velocity"])
                cd = float(row["coefficient_of_dimension"])
                dn = float(row["delta_N_N_max"])
                rv = float(row["ratio_v_to_v0"])
            except (ValueError, KeyError):
                return 0.0
            data[cd].append((cv, dn, rv))

        # 1. Flatness check: for each coefficient_of_dimension, find row with velocity=4.0
        #    and check that for larger velocities the delta_N_N_max stays within 1% relative change.
        flatness_ok = True
        for cd, rows in data.items():
            # Find the row with coefficient_of_velocity == 4.0 (within 1e-6)
            ref_val = None
            for cv, dn, rv in rows:
                if abs(cv - 4.0) < 1e-6:
                    ref_val = dn
                    break
            if ref_val is None:
                flatness_ok = False
                break
            if ref_val == 0.0:
                # can't compute fractional change; skip
                continue
            # Check all rows with coefficient_of_velocity >= 4.0
            for cv, dn, rv in rows:
                if cv >= 4.0 - 1e-9:
                    if abs(dn - ref_val) / abs(ref_val) > 0.01:
                        flatness_ok = False
                        break
            if not flatness_ok:
                break

        # 2. Worst‑case ratio at velocity=4:
        #    find the minimum ratio_v_to_v0 among all dimension coefficients at velocity=4,
        #    verify that the minimum occurs at coefficient_of_dimension == 1.0,
        #    and that the minimum value is within [0.83, 0.87].
        min_ratio = float('inf')
        min_dim = None
        for cd, rows in data.items():
            for cv, dn, rv in rows:
                if abs(cv - 4.0) < 1e-6:
                    if rv < min_ratio - 1e-12:
                        min_ratio = rv
                        min_dim = cd
                    elif abs(rv - min_ratio) < 1e-12 and cd != min_dim:
                        # tie not allowed
                        pass
        worst_ok = True
        if min_dim is None or min_ratio == float('inf'):
            worst_ok = False
        else:
            # Check dimension is 1.0 (tolerance 0.001)
            if abs(min_dim - 1.0) > 0.001:
                worst_ok = False
            # Check ratio magnitude
            if not (0.83 <= min_ratio <= 0.87):
                worst_ok = False
            # Ensure it is strictly the minimum (no other dimension has smaller ratio)
            for cd, rows in data.items():
                if abs(cd - 1.0) < 0.001:
                    continue
                for cv, dn, rv in rows:
                    if abs(cv - 4.0) < 1e-6:
                        if rv <= min_ratio - 1e-12:
                            worst_ok = False
                            break
                if not worst_ok:
                    break

        score = 0.0
        if flatness_ok:
            score += 0.5
        if worst_ok:
            score += 0.5
        return score


# === block: score_1 (check id='step_txt') ===
def score_1(artifact, step, ctx):
        import re
        if not isinstance(artifact, str):
            return 0.0
        lines = artifact.strip().split('\n')
        if len(lines) < 2:
            return 0.0
        m1 = re.search(r'threshold\s*=\s*([0-9.]+)', lines[0])
        m2 = re.search(r'worst_case_reduction\s*=\s*([0-9.]+)', lines[1])
        if not m1 or not m2:
            return 0.0
        try:
            threshold_val = float(m1.group(1))
            worst_case_val = float(m2.group(1))
        except ValueError:
            return 0.0
        tol_th = step.get("threshold_tolerance_abs", 0.1)
        tol_wc = step.get("reduction_tolerance_abs", 0.02)
        target_th = step.get("target_threshold", 4.0)
        target_wc = step.get("target_worst_case_reduction", 0.85)
        score = 0.0
        if abs(threshold_val - target_th) <= tol_th:
            score += 0.5
        if abs(worst_case_val - target_wc) <= tol_wc:
            score += 0.5
        return score


_SCORERS = {
    'step_csv': score_0,
    'step_txt': score_1,
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
