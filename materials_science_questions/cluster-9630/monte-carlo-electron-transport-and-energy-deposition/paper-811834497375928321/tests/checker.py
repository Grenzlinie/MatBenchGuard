import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import json
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
    import math

    def dose_expected(t, v):
        if abs(v - 1.0) < 1e-9:
            if t <= 0:
                return 0.0
            return 0.5 * (t / 3.0) * math.exp(1 - t / 3.0)
        else:
            return max(0.0, 0.6 - 0.1 * v)

    return {"optimum_thickness": 3.0, "expected_dose": dose_expected}


# === block: score_0 (check id='dose_vs_thickness_check') ===
def score_0(artifact, step, ctx):
    ctx_expected = ctx["expected_dose"]
    rows = artifact
    expected_opt = ctx["optimum_thickness"]
    tol_rel = 0.2

    # classify rows
    thickness_rows = [row for row in rows if abs(float(row["voltage_MV"]) - 1.0) < 1e-9]
    voltage_rows = [row for row in rows if abs(float(row["foil_thickness_um"]) - expected_opt) < 1e-6]

    # sort for trend checks
    thickness_rows.sort(key=lambda r: float(r["foil_thickness_um"]))
    voltage_rows.sort(key=lambda r: float(r["voltage_MV"]))

    # ---- pointwise tolerance ----
    ok_th = 0
    total_th = len(thickness_rows)
    for row in thickness_rows:
        t = float(row["foil_thickness_um"])
        v = float(row["voltage_MV"])
        expected = ctx_expected(t, v)
        reported = float(row["dose_per_electron_MeV"])
        if expected == 0:
            if reported == 0:
                ok_th += 1
            continue
        if abs(reported - expected) / abs(expected) <= tol_rel:
            ok_th += 1

    ok_volt = 0
    total_volt = len(voltage_rows)
    for row in voltage_rows:
        t = float(row["foil_thickness_um"])
        v = float(row["voltage_MV"])
        expected = ctx_expected(t, v)
        reported = float(row["dose_per_electron_MeV"])
        if expected == 0:
            if reported == 0:
                ok_volt += 1
            continue
        if abs(reported - expected) / abs(expected) <= tol_rel:
            ok_volt += 1

    pointwise_score = 0.0
    if total_th + total_volt > 0:
        pointwise_score = (ok_th + ok_volt) / (total_th + total_volt)
    else:
        pointwise_score = 0.0

    # ---- trend checks ----
    shape_score = 0.0

    if total_th >= 2:
        try:
            doses = [float(r["dose_per_electron_MeV"]) for r in thickness_rows]
            max_idx = max(range(len(doses)), key=lambda i: doses[i])
            inc_ok = all(doses[i] <= doses[i+1] + 1e-9 for i in range(max_idx))
            dec_ok = all(doses[i] >= doses[i+1] - 1e-9 for i in range(max_idx, len(doses)-1))
            if inc_ok and dec_ok:
                shape_score += 0.5
        except:
            pass

    if total_volt >= 2:
        try:
            doses_v = [float(r["dose_per_electron_MeV"]) for r in voltage_rows]
            dec_ok = all(doses_v[i] >= doses_v[i+1] - 1e-9 for i in range(len(doses_v)-1))
            if dec_ok:
                shape_score += 0.5
        except:
            pass

    shape_score = min(1.0, shape_score)

    return 0.6 * pointwise_score + 0.4 * shape_score


# === block: score_1 (check id='optimum_thickness_check') ===
def score_1(artifact, step, ctx):
    import re
    try:
        val = float(artifact.strip())
    except:
        return 0.0
    target = ctx["optimum_thickness"]
    if abs(val - target) <= 0.1:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'dose_vs_thickness_check': score_0,
    'optimum_thickness_check': score_1,
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
