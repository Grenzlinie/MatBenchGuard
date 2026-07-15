import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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


# === block: score_0 (check id='frequencies_check') ===
def score_0(artifact, step, ctx):
    paper_reported_keys = {
        'X/TA1': 1.25,
        'X/TA2': 1.25,
        'X/LA': 4.67,
        'X/TO1': 5.51,
        'X/TO2': 5.51,
        'X/LO': 4.67,
        'Γ/TA1': 0.0,
        'Γ/TA2': 0.0,
        'Γ/LA': 0.0,
    }
    tol_x = 0.05
    tol_zero = 1e-3

    if not isinstance(artifact, list) or not artifact:
        return 0.0
    total = 0
    match = 0
    for row in artifact:
        try:
            q = row['q_point'].strip()
            b = row['branch_label'].strip()
            freq = float(row['frequency'])
        except (KeyError, ValueError):
            continue
        key = f'{q}/{b}'
        if key not in paper_reported_keys:
            continue
        total += 1
        expected = paper_reported_keys[key]
        if key.startswith('Γ'):
            if abs(freq - expected) <= tol_zero:
                match += 1
        else:
            if abs(freq - expected) <= tol_x:
                match += 1
    return match / total if total > 0 else 0.0


# === block: score_1 (check id='dos_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    ok_positive = True
    integral = 0.0
    for row in artifact:
        try:
            f_l = float(row['freq_low'])
            f_h = float(row['freq_high'])
            g = float(row['g_nu'])
        except (KeyError, ValueError):
            return 0.0
        if g < -1e-9:
            ok_positive = False
        integral += g * (f_h - f_l)
    return 1.0 if (ok_positive and 5.5 <= integral <= 6.5) else 0.0


# === block: score_2 (check id='debye_check') ===
def score_2(artifact, step, ctx):
    targets = step['params']['target_points']
    tol = step['params']['tolerance']
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    rows = []
    for row in artifact:
        try:
            T = float(row['T'])
            th = float(row['theta_D'])
        except (KeyError, ValueError):
            continue
        rows.append((T, th))
    if not rows:
        return 0.0
    ok = 0
    for tgt_t, tgt_th in targets:
        best = None
        best_dist = None
        for T, th in rows:
            d = abs(T - tgt_t)
            if best_dist is None or d < best_dist:
                best_dist = d
                best = th
        if best is not None and abs(best - tgt_th) <= tol:
            ok += 1
    return ok / len(targets)


# === block: score_3 (check id='compressibility_check') ===
def score_3(artifact, step, ctx):
    text = artifact if isinstance(artifact, str) else ''
    if not text.strip():
        return 0.0
    try:
        val = float(text.strip().split()[0])
    except (ValueError, IndexError):
        return 0.0
    expected = step['params']['expected']
    tol_rel = step['params']['tolerance_rel']
    return 1.0 if abs(val - expected) / expected <= tol_rel else 0.0


_SCORERS = {
    'frequencies_check': score_0,
    'dos_check': score_1,
    'debye_check': score_2,
    'compressibility_check': score_3,
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
