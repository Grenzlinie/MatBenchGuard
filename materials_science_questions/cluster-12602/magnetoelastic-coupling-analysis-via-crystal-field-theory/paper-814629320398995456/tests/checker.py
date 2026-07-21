import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='schottky') ===
def score_0(artifact, step, ctx):
    temps = []; cms = []
    for r in artifact:
        t = float(r['T_K']); cm = float(r['Cm_J_per_mol_K'])
        temps.append(t); cms.append(cm)
    if len(temps) < 3: return 0.0
    idx = max(range(len(cms)), key=lambda i: cms[i])
    t_peak = temps[idx]
    cm_peak = cms[idx]
    target_T = 11.0; tol_T = 1.5
    target_mag = 1.5; tol_mag = 0.3
    sT = max(0.0, 1.0 - abs(t_peak - target_T) / (2 * tol_T))
    sM = max(0.0, 1.0 - abs(cm_peak - target_mag) / (2 * tol_mag))
    return 0.5 * sT + 0.5 * sM


# === block: score_1 (check id='suscept') ===
def score_1(artifact, step, ctx):
    T = []; chi = []
    for r in artifact:
        t = float(r['T_K'])
        if t < 150 or t > 300: continue
        T.append(t); chi.append(float(r['chi_inv_per_mol_emu']))
    if len(T) < 10: return 0.0
    A = np.vstack([T, np.ones_like(T)]).T
    slope, _ = np.linalg.lstsq(A, chi, rcond=None)[0]
    if slope <= 0: return 0.0
    p_eff = (8.0 / slope) ** 0.5
    target = 3.58; tol = 0.18
    return max(0.0, 1.0 - abs(p_eff - target) / (2 * tol))


# === block: score_2 (check id='elastic') ===
def score_2(artifact, step, ctx):
    T = []; c44 = []; c12 = []
    for r in artifact:
        T.append(float(r['T_K']))
        c44.append(float(r['c44_10^11_dyn_per_cm2']))
        c12.append(float(r['c11_c12_10^11_dyn_per_cm2']))
    if len(T) < 3: return 0.0
    i44 = int(np.argmin(c44)); i12 = int(np.argmin(c12))
    t44 = T[i44]; t12 = T[i12]
    c44_100 = c44[-1]; c12_100 = c12[-1]
    delta44 = (c44_100 - c44[i44]) / c44_100 if c44_100 != 0 else 0
    delta12 = (c12_100 - c12[i12]) / c12_100 if c12_100 != 0 else 0
    # c44
    tt_arg = 20.0; tt_tol = 3.0; dt_arg = 0.025; dt_tol = 0.005
    sT44 = max(0.0, 1.0 - abs(t44 - tt_arg) / (2 * tt_tol))
    sD44 = max(0.0, 1.0 - abs(delta44 - dt_arg) / (2 * dt_tol))
    # shoulder check: after the c44 minimum there must be a recovery forming a shoulder
    shoulder_ratio = 0.0
    if i44 < len(c44) - 2:
        # maximum value occurring after the minimum temperature
        post_c44 = c44[i44:]
        post_T = T[i44:]
        max_idx = int(np.argmax(post_c44))
        shoulder_ratio = (post_c44[max_idx] - c44[i44]) / c44_100 if c44_100 != 0 else 0
    shoulder_thresh = 0.003   # minimal relative rise that constitutes a shoulder
    sShoulder = 1.0 if shoulder_ratio >= shoulder_thresh else 0.0
    sC44 = (sT44 + sD44 + sShoulder) / 3.0
    # c12
    tt_arg2 = 15.0; tt_tol2 = 3.0; dt_arg2 = 0.015; dt_tol2 = 0.003
    sT12 = max(0.0, 1.0 - abs(t12 - tt_arg2) / (2 * tt_tol2))
    sD12 = max(0.0, 1.0 - abs(delta12 - dt_arg2) / (2 * dt_tol2))
    sC12 = 0.5 * sT12 + 0.5 * sD12
    return 0.5 * sC44 + 0.5 * sC12


_SCORERS = {
    'schottky': score_0,
    'suscept': score_1,
    'elastic': score_2,
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