import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
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
    return {}


# === block: score_0 (check id='step_03_postprocess') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tolerances = step["tolerances"]

    def build_stiffness_matrix(C, phase):
        if phase == 'alpha':
            C11 = C['C11']
            C44 = C['C44']
            C12 = C['C12']
            C_mat = np.zeros((6, 6))
            C_mat[0,0] = C_mat[1,1] = C_mat[2,2] = C11
            C_mat[0,1] = C_mat[0,2] = C_mat[1,0] = C_mat[1,2] = C_mat[2,0] = C_mat[2,1] = C12
            C_mat[3,3] = C_mat[4,4] = C_mat[5,5] = C44
            return C_mat
        else:  # beta hexagonal
            C11 = C['C11']
            C33 = C['C33']
            C44 = C['C44']
            C12 = C['C12']
            C13 = C['C13']
            C66 = (C11 - C12) / 2.0
            C_mat = np.zeros((6, 6))
            C_mat[0,0] = C_mat[1,1] = C11
            C_mat[2,2] = C33
            C_mat[0,1] = C_mat[1,0] = C12
            C_mat[0,2] = C_mat[1,2] = C_mat[2,0] = C_mat[2,1] = C13
            C_mat[3,3] = C_mat[4,4] = C44
            C_mat[5,5] = C66
            return C_mat

    def compute_derived_moduli(C_mat):
        S = np.linalg.inv(C_mat)
        B_V = (C_mat[0,0] + C_mat[1,1] + C_mat[2,2] + 2*(C_mat[0,1] + C_mat[0,2] + C_mat[1,2])) / 9.0
        B_R = 1.0 / (S[0,0] + S[1,1] + S[2,2] + 2*(S[0,1] + S[0,2] + S[1,2]))
        B_VRH = (B_V + B_R) / 2.0
        G_V = (C_mat[0,0] + C_mat[1,1] + C_mat[2,2] - (C_mat[0,1] + C_mat[0,2] + C_mat[1,2]) + 3*(C_mat[3,3] + C_mat[4,4] + C_mat[5,5])) / 15.0
        G_R = 15.0 / (4*(S[0,0] + S[1,1] + S[2,2]) - 4*(S[0,1] + S[0,2] + S[1,2]) + 3*(S[3,3] + S[4,4] + S[5,5]))
        G_VRH = (G_V + G_R) / 2.0
        E_mod = 9.0 * B_VRH * G_VRH / (3.0 * B_VRH + G_VRH)
        nu = (3.0 * B_VRH - 2.0 * G_VRH) / (2.0 * (3.0 * B_VRH + G_VRH))
        k = G_VRH / B_VRH
        Hv = 2.0 * (k**2 * G_VRH)**0.585 - 3.0
        return {'B_VRH': B_VRH, 'G_VRH': G_VRH, 'E': E_mod, 'Poisson_ratio': nu, 'Vickers_hardness': Hv}

    scored = {}
    for phase in ['alpha', 'beta']:
        if phase not in artifact:
            return 0.0
        phase_data = artifact[phase]
        if 'elastic_constants' not in phase_data:
            return 0.0
        C = phase_data['elastic_constants']
        C_mat = build_stiffness_matrix(C, phase)
        derived = compute_derived_moduli(C_mat)
        scored[phase] = derived

    passed = 0
    total = 0
    for phase in ['alpha', 'beta']:
        g = gold[phase]
        d = scored[phase]
        for key in ['B_VRH', 'G_VRH', 'E', 'Poisson_ratio', 'Vickers_hardness']:
            tol = tolerances.get(key, 0.0)
            if abs(d[key] - g[key]) <= tol:
                passed += 1
            total += 1

    return passed / total if total > 0 else 0.0


_SCORERS = {
    'step_03_postprocess': score_0,
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
