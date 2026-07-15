import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess
import importlib

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
                           "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    np = importlib.import_module("numpy")


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
    ctx = {
        "gibbs_slope_gold": 0.0024,
        "gibbs_slope_tol": 0.00024,
        "K_5at_gold": 0.1024,
        "K_5at_tol": 0.03,
        "K_10at_gold": 0.2389,
        "K_10at_tol": 0.03,
        "psd_peak_5at_gold": 2.7,
        "psd_peak_5at_tol": 0.54,
        "psd_peak_10at_gold": 3.5,
        "psd_peak_10at_tol": 0.7,
    }
    return ctx


# === block: score_0 (check id='gibbs_thomson_slope') ===
def score_0(artifact, step, ctx):
    data = artifact.get("gibbs_thomson", [])
    if len(data) < 2:
        return 0.0
    x = np.array([d["curvature_1_nm"] for d in data])
    y = np.array([d["delta_cp"] for d in data])
    A = np.vstack([x, np.ones(len(x))]).T
    slope, _ = np.linalg.lstsq(A, y, rcond=None)[0]
    gold = step.get("target")
    tol = step.get("tolerance")
    if gold is None or tol is None:
        return 0.0
    diff = abs(slope - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_1 (check id='coarsening_K_5at') ===
def score_1(artifact, step, ctx):
    data = artifact.get("coarsening_5at", [])
    if len(data) < 3:
        return 0.0
    t = np.array([d["time_s"] for d in data])
    r = np.array([d["mean_radius_nm"] for d in data])
    r3 = r**3
    A = np.vstack([t, np.ones(len(t))]).T
    K, _ = np.linalg.lstsq(A, r3, rcond=None)[0]
    gold = ctx["K_5at_gold"]
    tol = ctx["K_5at_tol"]
    diff = abs(K - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_2 (check id='coarsening_K_10at') ===
def score_2(artifact, step, ctx):
    data = artifact.get("coarsening_10at", [])
    if len(data) < 3:
        return 0.0
    t = np.array([d["time_s"] for d in data])
    r = np.array([d["mean_radius_nm"] for d in data])
    r3 = r**3
    A = np.vstack([t, np.ones(len(t))]).T
    K, _ = np.linalg.lstsq(A, r3, rcond=None)[0]
    gold = ctx["K_10at_gold"]
    tol = ctx["K_10at_tol"]
    diff = abs(K - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_3 (check id='psd_peak_5at') ===
def score_3(artifact, step, ctx):
    data = artifact.get("PSD_5at_end", [])
    if not data:
        return 0.0
    max_count = -1
    peak_radius = None
    for entry in data:
        r = entry["radius_nm"]
        cnt = entry["count"]
        if cnt > max_count:
            max_count = cnt
            peak_radius = r
    if peak_radius is None:
        return 0.0
    gold = ctx["psd_peak_5at_gold"]
    tol = ctx["psd_peak_5at_tol"]
    diff = abs(peak_radius - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_4 (check id='psd_peak_10at') ===
def score_4(artifact, step, ctx):
    data = artifact.get("PSD_10at_end", [])
    if not data:
        return 0.0
    max_count = -1
    peak_radius = None
    for entry in data:
        r = entry["radius_nm"]
        cnt = entry["count"]
        if cnt > max_count:
            max_count = cnt
            peak_radius = r
    if peak_radius is None:
        return 0.0
    gold = ctx["psd_peak_10at_gold"]
    tol = ctx["psd_peak_10at_tol"]
    diff = abs(peak_radius - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


_SCORERS = {
    'gibbs_thomson_slope': score_0,
    'coarsening_K_5at': score_1,
    'coarsening_K_10at': score_2,
    'psd_peak_5at': score_3,
    'psd_peak_10at': score_4,
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
