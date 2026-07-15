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
    return {
        "r_peak_ref": {
            "EIM2/TFSI-": 4.4,
            "EIM2/Cl-": 4.8,
            "EIM1/TFSI-": 4.4
        },
        "tg_ref": {
            "EIM2/TFSI-": 371,
            "EIM2/Cl-": 436,
            "EIM1/TFSI-": 393
        },
        "E_ref": {
            "EIM2/TFSI-": 1.21,
            "EIM2/Cl-": 1.44,
            "EIM1/TFSI-": 1.05
        },
        "D_ref": {
            "EIM2/TFSI-": 1e-9,
            "EIM2/Cl-": 5e-10,
            "EIM1/TFSI-": 1e-9
        },
        "r_peak_tol": 0.5,
        "tg_tol_frac": 0.5,
        "E_tol_frac": 0.5,
        "D_tol_frac": 0.5
    }


# === block: score_0 (check id='r_peak_check') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    ref = ctx["r_peak_ref"]
    tol = ctx["r_peak_tol"]
    valid = 0
    for row in artifact:
        sys = row["system"].strip()
        if sys in ref:
            val = float(row["r_peak_AA"])
            if abs(val - ref[sys]) <= tol:
                valid += 1
    if len(ref) == 3:
        return valid / 3.0
    else:
        return 0.0


# === block: score_1 (check id='tg_check') ===
def score_1(artifact, step, ctx):
    artifact = artifact
    ref = ctx["tg_ref"]
    tol_frac = ctx["tg_tol_frac"]
    rows_by_sys = {}
    for row in artifact:
        sys = row["system"].strip()
        rows_by_sys[sys] = float(row["Tg_K"])
    def t_trend1():
        return 1.0 if rows_by_sys.get("EIM2/Cl-", -999) > rows_by_sys.get("EIM2/TFSI-", -999) else 0.0
    def t_trend2():
        return 1.0 if rows_by_sys.get("EIM1/TFSI-", -999) > rows_by_sys.get("EIM2/TFSI-", -999) else 0.0
    def magn_score():
        cnt = 0
        for sys, gold in ref.items():
            val = rows_by_sys.get(sys, None)
            if val is not None:
                max_diff = tol_frac * gold
                if abs(val - gold) <= max_diff:
                    cnt += 1
        return cnt / 3.0
    score = 0.4*t_trend1() + 0.4*t_trend2() + 0.2*magn_score()
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='E_check') ===
def score_2(artifact, step, ctx):
    artifact = artifact
    ref = ctx["E_ref"]
    tol_frac = ctx["E_tol_frac"]
    rows_by_sys = {}
    for row in artifact:
        sys = row["system"].strip()
        rows_by_sys[sys] = float(row["E_GPa"])
    def trend_cl_tfsi():
        return 1.0 if rows_by_sys.get("EIM2/Cl-", -999) > rows_by_sys.get("EIM2/TFSI-", -999) else 0.0
    def magn_score():
        cnt = 0
        for sys, gold in ref.items():
            val = rows_by_sys.get(sys, None)
            if val is not None:
                max_diff = tol_frac * gold
                if abs(val - gold) <= max_diff:
                    cnt += 1
        return cnt / 3.0
    score = 0.8*trend_cl_tfsi() + 0.2*magn_score()
    return max(0.0, min(1.0, score))


# === block: score_3 (check id='D_check') ===
def score_3(artifact, step, ctx):
    artifact = artifact
    ref = ctx["D_ref"]
    tol_frac = ctx["D_tol_frac"]
    rows_by_sys = {}
    for row in artifact:
        sys = row["system"].strip()
        rows_by_sys[sys] = float(row["D_cm2s"])
    def trend_cl_tfsi():
        return 1.0 if rows_by_sys.get("EIM2/Cl-", -1) < rows_by_sys.get("EIM2/TFSI-", -1) else 0.0
    def magn_score():
        cnt = 0
        for sys, gold in ref.items():
            val = rows_by_sys.get(sys, None)
            if val is not None:
                max_diff = tol_frac * gold
                if abs(val - gold) <= max_diff:
                    cnt += 1
        return cnt / 3.0
    score = 0.8*trend_cl_tfsi() + 0.2*magn_score()
    return max(0.0, min(1.0, score))


_SCORERS = {
    'r_peak_check': score_0,
    'tg_check': score_1,
    'E_check': score_2,
    'D_check': score_3,
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
