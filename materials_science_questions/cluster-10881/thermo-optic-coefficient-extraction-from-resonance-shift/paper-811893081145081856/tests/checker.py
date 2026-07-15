import os
import json
import csv

# === author imports / helpers ===
import json
import math
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
import numpy as np


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
    import math, numpy as np
    ctx = {'data': spec['hidden_data']}
    return ctx


# === block: score_0 (check id='residual_recompute') ===
def score_0(artifact, step, ctx):
    try:
        fitted = artifact.get('fitted_parameters', {})
        A1 = float(fitted.get('A1', 0))
        L1 = float(fitted.get('lambda1', 0))
        A2 = float(fitted.get('A2', 0))
        L2 = float(fitted.get('lambda2', 0))
        A3 = float(fitted.get('A3', 0))
        L3 = float(fitted.get('lambda3', 0))
    except Exception:
        return 0.0

    measured = np.array([(d['wavelength_um'], d['refractive_index']) for d in ctx['data']])
    lam = measured[:, 0]
    n_meas = measured[:, 1]

    def sellmeier_n(A1, L1, A2, L2, A3, L3, lam):
        l2 = lam * lam
        t1 = A1 * l2 / (l2 - L1*L1)
        t2 = A2 * l2 / (l2 - L2*L2)
        t3 = A3 * l2 / (l2 - L3*L3)
        return np.sqrt(1.0 + t1 + t2 + t3)

    try:
        n_pred = sellmeier_n(A1, L1, A2, L2, A3, L3, lam)
    except Exception:
        return 0.0

    residuals = np.abs(n_pred - n_meas)
    avg_res = float(np.mean(residuals))

    ref = float(step.get('reference_value', 1.05e-05))
    tol = float(step.get('tolerance_abs', 5.0e-06))
    if avg_res <= ref:
        return 1.0
    else:
        return max(0.0, 1.0 - (avg_res - ref) / tol)


# === block: score_1 (check id='parameter_consistency') ===
def score_1(artifact, step, ctx):
    params_spec = step.get('parameters', {})
    artifact_params = artifact.get('fitted_parameters', {})
    scores = []
    for key, spec in params_spec.items():
        ref = float(spec.get('ref', 0))
        tol_rel = float(spec.get('tol_rel', 0.001))
        agent_val = artifact_params.get(key, None)
        if agent_val is None:
            scores.append(0.0)
            continue
        agent_val = float(agent_val)
        if np.abs(ref) < 1e-12:
            rel_err = np.abs(agent_val - ref)
        else:
            rel_err = np.abs(agent_val - ref) / np.abs(ref)
        sub_score = max(0.0, 1.0 - rel_err / tol_rel)
        scores.append(sub_score)
    if len(scores) == 0:
        return 0.0
    return float(np.mean(scores))


_SCORERS = {
    'residual_recompute': score_0,
    'parameter_consistency': score_1,
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
