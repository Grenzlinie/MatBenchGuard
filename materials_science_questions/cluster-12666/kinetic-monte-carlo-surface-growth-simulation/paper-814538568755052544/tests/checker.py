import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    import numpy as np
import csv
import os
import json
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
    ctx = {}
    for step in spec.get("steps", []):
        if "gold_points" in step:
            pts = step["gold_points"]
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            sorted_pairs = sorted(zip(xs, ys))
            xs_sorted, ys_sorted = zip(*sorted_pairs)
            ctx[f"{step['id']}_gold_x"] = np.array(xs_sorted, dtype=float)
            ctx[f"{step['id']}_gold_y"] = np.array(ys_sorted, dtype=float)
    return ctx


# === block: score_0 (check id='d2d_check') ===
def score_0(artifact, step, ctx):
    value_str = artifact.strip()
    try:
        val = float(value_str)
    except Exception:
        return 0.0

    # Fix numpy trapz removal for subsequent scorers (runs first)
    import sys
    _np_mod = sys.modules.get('numpy')
    if _np_mod is not None and not hasattr(_np_mod, 'trapz') and hasattr(_np_mod, 'trapezoid'):
        _np_mod.trapz = _np_mod.trapezoid

    target = step.get("target", 0.20)
    tol = step.get("tolerance_abs", 0.02)
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='hist_homog') ===
def score_1(artifact, step, ctx):
    step_id = step["id"]
    gold_x = ctx[f"{step_id}_gold_x"]
    gold_y = ctx[f"{step_id}_gold_y"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    # parse agent csv
    agent_x = np.array([float(row["displacement_nm"]) for row in artifact])
    agent_y = np.array([float(row["probability"]) for row in artifact])
    sort_idx = np.argsort(agent_x)
    agent_x = agent_x[sort_idx]
    agent_y = agent_y[sort_idx]
    # normalize gold by its integral (area under curve)
    trapz_norm = np.trapz(gold_y, gold_x)
    if trapz_norm > 0:
        gold_y_norm = gold_y / trapz_norm
    else:
        gold_y_norm = gold_y
    # interpolate agent histogram onto gold x grid
    agent_y_interp = np.interp(gold_x, agent_x, agent_y, left=0.0, right=0.0)
    # compute mean relative error where gold is significant
    eps = 1e-12
    mask = gold_y_norm > 1e-6
    if np.sum(mask) == 0:
        return 1.0
    rel_err = np.abs(agent_y_interp[mask] - gold_y_norm[mask]) / (gold_y_norm[mask] + eps)
    avg_rel_err = float(np.mean(rel_err))
    thresh = step.get("error_threshold", 0.30)
    score = max(0.0, 1.0 - avg_rel_err / thresh)
    return score


# === block: score_2 (check id='hist_hex') ===
def score_2(artifact, step, ctx):
    step_id = step["id"]
    gold_x = ctx[f"{step_id}_gold_x"]
    gold_y = ctx[f"{step_id}_gold_y"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    agent_x = np.array([float(row["displacement_nm"]) for row in artifact])
    agent_y = np.array([float(row["probability"]) for row in artifact])
    sort_idx = np.argsort(agent_x)
    agent_x = agent_x[sort_idx]
    agent_y = agent_y[sort_idx]
    trapz_norm = np.trapz(gold_y, gold_x)
    if trapz_norm > 0:
        gold_y_norm = gold_y / trapz_norm
    else:
        gold_y_norm = gold_y
    agent_y_interp = np.interp(gold_x, agent_x, agent_y, left=0.0, right=0.0)
    eps = 1e-12
    mask = gold_y_norm > 1e-6
    if np.sum(mask) == 0:
        return 1.0
    rel_err = np.abs(agent_y_interp[mask] - gold_y_norm[mask]) / (gold_y_norm[mask] + eps)
    avg_rel_err = float(np.mean(rel_err))
    thresh = step.get("error_threshold", 0.30)
    score = max(0.0, 1.0 - avg_rel_err / thresh)
    return score


_SCORERS = {
    'd2d_check': score_0,
    'hist_homog': score_1,
    'hist_hex': score_2,
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
