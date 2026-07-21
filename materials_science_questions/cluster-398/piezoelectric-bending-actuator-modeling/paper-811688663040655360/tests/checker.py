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


# === block: score_0 (check id='radial_time_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    late_rows = [r for r in rows if 'time' in r and float(r['time']) >= 23.0]
    finite_ok = True
    for r in rows:
        try:
            wi = float(r['w_inner'])
            wm = float(r['w_middle'])
            wo = float(r['w_outer'])
            if not (np.isfinite(wi) and np.isfinite(wm) and np.isfinite(wo)):
                finite_ok = False
                break
        except (ValueError, KeyError):
            return 0.0
    total_abs = 0.0
    for r in rows:
        if all(k in r for k in ('time','w_inner','w_middle','w_outer')):
            total_abs += abs(float(r['w_inner'])) + abs(float(r['w_middle'])) + abs(float(r['w_outer']))
    nonzero_ok = total_abs > 1e-12
    if len(late_rows) < 5:
        order_ok = False
    else:
        ordered = 0
        for r in late_rows:
            if float(r['w_inner']) > float(r['w_middle']) and float(r['w_middle']) > float(r['w_outer']):
                ordered += 1
        order_ok = (ordered / len(late_rows)) >= 0.6
    score = (int(order_ok) + int(finite_ok) + int(nonzero_ok)) / 3.0
    return score


# === block: score_1 (check id='axial_spatial_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    finite_ok = True
    max_abs = {'u_inner': 0.0, 'u_middle': 0.0, 'u_outer': 0.0}
    for r in rows:
        try:
            ui = float(r['u_inner'])
            um = float(r['u_middle'])
            uo = float(r['u_outer'])
            if not (np.isfinite(ui) and np.isfinite(um) and np.isfinite(uo)):
                finite_ok = False
                break
            max_abs['u_inner'] = max(max_abs['u_inner'], abs(ui))
            max_abs['u_middle'] = max(max_abs['u_middle'], abs(um))
            max_abs['u_outer'] = max(max_abs['u_outer'], abs(uo))
        except (ValueError, KeyError):
            return 0.0
    nonzero_ok = (max_abs['u_inner'] + max_abs['u_middle'] + max_abs['u_outer']) > 1e-12
    order_ok = (max_abs['u_inner'] > max_abs['u_middle']) and (max_abs['u_middle'] > max_abs['u_outer'])
    score = (int(order_ok) + int(finite_ok) + int(nonzero_ok)) / 3.0
    return score


# === block: score_2 (check id='potential_spatial_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    finite_ok = True
    max_abs = {'phi_inner': 0.0, 'phi_middle': 0.0, 'phi_outer': 0.0}
    for r in rows:
        try:
            pi = float(r['phi_inner'])
            pm = float(r['phi_middle'])
            po = float(r['phi_outer'])
            if not (np.isfinite(pi) and np.isfinite(pm) and np.isfinite(po)):
                finite_ok = False
                break
            max_abs['phi_inner'] = max(max_abs['phi_inner'], abs(pi))
            max_abs['phi_middle'] = max(max_abs['phi_middle'], abs(pm))
            max_abs['phi_outer'] = max(max_abs['phi_outer'], abs(po))
        except (ValueError, KeyError):
            return 0.0
    nonzero_ok = (max_abs['phi_inner'] + max_abs['phi_middle'] + max_abs['phi_outer']) > 1e-12
    order_ok = (max_abs['phi_inner'] > max_abs['phi_middle']) and (max_abs['phi_middle'] > max_abs['phi_outer'])
    score = (int(order_ok) + int(finite_ok) + int(nonzero_ok)) / 3.0
    return score


_SCORERS = {
    'radial_time_check': score_0,
    'axial_spatial_check': score_1,
    'potential_spatial_check': score_2,
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
