import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    return {"outputs_dir": outputs_dir}


# === block: score_0 (check id='check_n_ef_value') ===
def score_0(artifact, step, ctx):
        try:
            val = float(artifact.strip())
        except:
            return 0.0
        target = step["target"]
        abs_tol = step.get("tolerance_abs", 5.0)
        rel_tol = step.get("tolerance_rel", 0.15)
        tol = max(abs_tol, rel_tol * abs(target))
        diff = abs(val - target)
        if diff <= tol:
            return 1.0
        # partial credit beyond tolerance: degrade linearly to 0 at 2*tol
        if diff <= 2 * tol:
            return max(0.0, 1.0 - (diff - tol) / tol)
        return 0.0


# === block: score_1 (check id='check_dos_curve_sanity') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) < 2:
            return 0.0
        required_cols = step.get("required_columns", ["energy_relative", "dos_total"])
        if not all(col in artifact[0] for col in required_cols):
            return 0.0
        # check that energy_relative = 0 is approximately present
        eps = 1e-3
        has_ef = any(abs(float(row["energy_relative"])) <= eps for row in artifact)
        return 1.0 if has_ef else 0.0


# === block: score_2 (check id='check_n_ef_consistency') ===
def score_2(artifact, step, ctx):
        try:
            val_nef = float(artifact.strip())
        except:
            return 0.0
        dos_path = os.path.join(ctx["outputs_dir"], "dos_curve.csv")
        if not os.path.exists(dos_path):
            return 0.0
        dos_rows = []
        with open(dos_path, newline='') as f:
            reader = csv.DictReader(f)
            if 'energy_relative' not in reader.fieldnames or 'dos_total' not in reader.fieldnames:
                return 0.0
            dos_rows = list(reader)
        # find closest point to E=0
        best_diff = float('inf')
        dos_ef = None
        for row in dos_rows:
            e = float(row["energy_relative"])
            d = abs(e)
            if d < best_diff:
                best_diff = d
                dos_ef = float(row["dos_total"])
        if dos_ef is None or best_diff > 1e-3:
            return 0.0
        if abs(val_nef - dos_ef) <= step.get("consistency_tolerance", 1e-3):
            return 1.0
        return 0.0


# === block: score_3 (check id='check_fermi_peak_structure') ===
def score_3(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) < 2:
            return 0.0
        # compute N(EF) from dos at E=0
        best_diff = float('inf')
        dos_ef = None
        for row in artifact:
            e = float(row["energy_relative"])
            if abs(e) < best_diff:
                best_diff = abs(e)
                dos_ef = float(row["dos_total"])
        if dos_ef is None or best_diff > 1e-3:
            return 0.0
        max_window = step.get("max_energy_window_ry", 0.1)
        rising_window = step.get("rising_window_ry", 0.003)
        # find max dos in (0, max_window]
        peak_dos = -float('inf')
        for row in artifact:
            e = float(row["energy_relative"])
            if 0 < e <= max_window:
                peak_dos = max(peak_dos, float(row["dos_total"]))
        if peak_dos <= dos_ef:
            return 0.0
        # check rising in [0, rising_window]
        rising = True
        prev_dos = dos_ef
        # sort by energy to check monotonic increase
        points = sorted([row for row in artifact if 0 < float(row["energy_relative"]) <= rising_window], key=lambda r: float(r["energy_relative"]))
        for row in points:
            cur = float(row["dos_total"])
            if cur <= prev_dos:
                rising = False
                break
            prev_dos = cur
        return 1.0 if rising else 0.0


# === block: score_4 (check id='check_vs_LuNi2B2C') ===
def score_4(artifact, step, ctx):
        try:
            val = float(artifact.strip())
        except:
            return 0.0
        threshold = step.get("compare_threshold", 45.71)
        return 1.0 if val <= threshold else 0.0


_SCORERS = {
    'check_n_ef_value': score_0,
    'check_dos_curve_sanity': score_1,
    'check_n_ef_consistency': score_2,
    'check_fermi_peak_structure': score_3,
    'check_vs_LuNi2B2C': score_4,
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
