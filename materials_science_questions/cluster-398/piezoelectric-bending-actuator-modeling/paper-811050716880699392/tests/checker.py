import os
import json
import csv


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
    import json, os

    def prepare(outputs_dir, spec):
        results_path = os.path.join(outputs_dir, "results.json")
        if not os.path.exists(results_path):
            return {"results_val": None, "gold": {
                "center_displacement_um": 53.74,
                "optimal_r2_r1": 0.85,
                "optimal_tpzt_tp": 0.67,
                "pressure_rise_kPa": 9.87,
                "tol_center_um": 2.0,
                "tol_r2r1": 0.02,
                "tol_tpzttp": 0.05,
                "tol_pressure_kPa": 0.5,
            }}
        with open(results_path) as f:
            results_val = json.load(f)
        gold = {
            "center_displacement_um": 53.74,
            "optimal_r2_r1": 0.85,
            "optimal_tpzt_tp": 0.67,
            "pressure_rise_kPa": 9.87,
            "tol_center_um": 2.0,
            "tol_r2r1": 0.02,
            "tol_tpzttp": 0.05,
            "tol_pressure_kPa": 0.5,
        }
        return {"results_val": results_val, "gold": gold}


# === block: score_0 (check id='check_deflection_profile') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not isinstance(rows, list) or len(rows) != 20:
            return 0.0
        if not all("r_mm" in row and "w_um" in row for row in rows):
            return 0.0
        r = [float(row["r_mm"]) for row in rows]
        w = [float(row["w_um"]) for row in rows]
        checks = []
        # 1. r first 0, last 15
        checks.append(abs(r[0]) < 1e-9 and abs(r[-1] - 15.0) < 1e-6)
        # 2. monotonic decreasing deflection
        monotonic = all(w[i] >= w[i+1] for i in range(19))
        checks.append(monotonic)
        # 3. edge near zero (clamped)
        checks.append(abs(w[-1]) < 1e-3)
        # 4. cross-check center displacement with results
        if ctx.get("results_val") is not None:
            center_results = ctx["results_val"].get("center_displacement_um")
            if center_results is not None:
                checks.append(abs(w[0] - center_results) <= 1.0)
            else:
                checks.append(False)
        else:
            checks.append(False)
        return sum(checks) / len(checks)


# === block: score_1 (check id='check_results') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx.get("gold", {})
        if not gold:
            return 0.0
        res = artifact
        if not isinstance(res, dict):
            return 0.0
        required = ["center_displacement_um", "optimal_r2_r1", "optimal_tpzt_tp", "pressure_rise_kPa"]
        if not all(k in res for k in required):
            return 0.0
        scores = []
        c = float(res["center_displacement_um"])
        scores.append(1.0 if abs(c - gold["center_displacement_um"]) <= gold["tol_center_um"] else 0.0)
        r2r1 = float(res["optimal_r2_r1"])
        scores.append(1.0 if abs(r2r1 - gold["optimal_r2_r1"]) <= gold["tol_r2r1"] else 0.0)
        tpzttp = float(res["optimal_tpzt_tp"])
        scores.append(1.0 if abs(tpzttp - gold["optimal_tpzt_tp"]) <= gold["tol_tpzttp"] else 0.0)
        p = float(res["pressure_rise_kPa"])
        scores.append(1.0 if abs(p - gold["pressure_rise_kPa"]) <= gold["tol_pressure_kPa"] else 0.0)
        return sum(scores) / len(scores)


_SCORERS = {
    'check_deflection_profile': score_0,
    'check_results': score_1,
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
