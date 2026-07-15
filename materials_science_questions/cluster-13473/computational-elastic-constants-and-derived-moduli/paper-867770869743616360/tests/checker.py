import os
import json
import csv

# === author imports / helpers ===
import os, sys, subprocess
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np
import re
import csv
import json


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
    return {"output_dir": "/app/outputs"}


# === block: score_0 (check id='elastic_data_structure') ===
def score_0(artifact, step, ctx):
    output_dir = ctx["output_dir"]
    path = os.path.join(output_dir, "elastic_data.csv")
    if not os.path.exists(path):
        return 0.0
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if len(rows) != 3:
        return 0.0
    required = {"d_nm", "phi_core", "E_overall_GPa"}
    for row in rows:
        if not required.issubset(row.keys()):
            return 0.0
        try:
            phi = float(row["phi_core"])
            e = float(row["E_overall_GPa"])
        except Exception:
            return 0.0
        if not (0.5 < phi < 1.0) or not (50 < e < 150):
            return 0.0
    return 1.0


# === block: score_1 (check id='elastic_data_recompute') ===
def score_1(artifact, step, ctx):
    output_dir = ctx["output_dir"]
    path = os.path.join(output_dir, "elastic_data.csv")
    target_ratio = step.get("target_ratio", 0.2739726)
    tol = step.get("tolerance_window", 0.1)
    max_dev = step.get("max_deviation", 0.3)
    try:
        rows = []
        with open(path, newline='') as f:
            for r in csv.DictReader(f):
                rows.append(r)
        if len(rows) < 3:
            return 0.0
        phis = np.array([float(r["phi_core"]) for r in rows])
        Es = np.array([float(r["E_overall_GPa"]) for r in rows])
        y = 1.0 / Es
        A = np.column_stack([phis, np.ones_like(phis)])
        coeff, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b = coeff[0], coeff[1]
        if b <= 0 or (a + b) <= 0:
            return 0.0
        E_GB = 1.0 / b
        E_core = 1.0 / (a + b)
        ratio = E_GB / E_core
    except Exception:
        return 0.0

    diff = abs(ratio - target_ratio)
    if diff <= tol:
        return 1.0
    score = 1.0 - (diff - tol) / (max_dev - tol)
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='reuss_fit_params') ===
def score_2(artifact, step, ctx):
    output_dir = ctx["output_dir"]
    txt_path = os.path.join(output_dir, "reuss_fit_params.txt")
    csv_path = os.path.join(output_dir, "elastic_data.csv")
    max_diff = step.get("max_diff_gpa", 10.0)

    E_core_txt = None
    E_GB_txt = None
    if os.path.exists(txt_path):
        with open(txt_path) as f:
            content = f.read()
        m1 = re.search(r'E_core_GPa\s*=\s*([\d.]+)', content)
        m2 = re.search(r'E_GB_GPa\s*=\s*([\d.]+)', content)
        if m1 and m2:
            E_core_txt = float(m1.group(1))
            E_GB_txt = float(m2.group(1))
    if E_core_txt is None or E_GB_txt is None:
        return 0.0

    try:
        rows = list(csv.DictReader(open(csv_path)))
        if len(rows) < 3:
            return 0.0
        phis = np.array([float(r["phi_core"]) for r in rows])
        Es = np.array([float(r["E_overall_GPa"]) for r in rows])
        y = 1.0 / Es
        A = np.column_stack([phis, np.ones_like(phis)])
        coeff, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b = coeff[0], coeff[1]
        if b <= 0 or (a + b) <= 0:
            return 0.0
        E_core_fit = 1.0 / (a + b)
        E_GB_fit = 1.0 / b
    except Exception:
        return 0.0

    diff1 = abs(E_core_txt - E_core_fit)
    diff2 = abs(E_GB_txt - E_GB_fit)
    max_d = max(diff1, diff2)
    if max_d <= max_diff:
        return 1.0
    score = max(0.0, 1.0 - (max_d - max_diff) / 20.0)
    return min(1.0, score)


# === block: score_3 (check id='ratio') ===
def score_3(artifact, step, ctx):
    output_dir = ctx["output_dir"]
    ratio_path = os.path.join(output_dir, "ratio.txt")
    csv_path = os.path.join(output_dir, "elastic_data.csv")
    max_diff_ratio = step.get("max_diff_ratio", 0.05)
    decay_range = step.get("decay_range", 0.15)
    try:
        with open(ratio_path) as f:
            ratio_txt = float(f.read().strip())
    except Exception:
        return 0.0

    try:
        rows = list(csv.DictReader(open(csv_path)))
        if len(rows) < 3:
            return 0.0
        phis = np.array([float(r["phi_core"]) for r in rows])
        Es = np.array([float(r["E_overall_GPa"]) for r in rows])
        y = 1.0 / Es
        A = np.column_stack([phis, np.ones_like(phis)])
        coeff, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b = coeff[0], coeff[1]
        if b <= 0 or (a + b) <= 0:
            return 0.0
        ratio_fit = (1.0 / b) / (1.0 / (a + b))
    except Exception:
        return 0.0

    diff = abs(ratio_txt - ratio_fit)
    if diff <= max_diff_ratio:
        return 1.0
    score = max(0.0, 1.0 - (diff - max_diff_ratio) / decay_range)
    return min(1.0, score)


_SCORERS = {
    'elastic_data_structure': score_0,
    'elastic_data_recompute': score_1,
    'reuss_fit_params': score_2,
    'ratio': score_3,
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
