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
    return {}


# === block: score_0 (check id='tbc_op') ===
def score_0(artifact, step, ctx):
    rows = artifact
    temps = [float(r['temperature']) for r in rows]
    ops = [float(r['Op']) for r in rows]
    idx = sorted(range(len(temps)), key=lambda i: temps[i])
    temps = [temps[i] for i in idx]
    ops = [ops[i] for i in idx]
    low_T_high_Op = any(t <= 0.10 and op >= 0.7 for t, op in zip(temps, ops))
    high_T_low_Op = any(t >= 0.12 and op <= 0.3 for t, op in zip(temps, ops))
    score = 0.0
    if low_T_high_Op:
        score += 0.3
    if high_T_low_Op:
        score += 0.3
    if low_T_high_Op and high_T_low_Op:
        T_low = max(t for t, op in zip(temps, ops) if op <= 0.3)
        T_high = min(t for t, op in zip(temps, ops) if op >= 0.7)
        if T_high - T_low <= 0.03:
            score += 0.4
    return score


# === block: score_1 (check id='tbc_cv') ===
def score_1(artifact, step, ctx):
    rows = artifact
    temps = [float(r['temperature']) for r in rows]
    cvs = [float(r['c_V']) for r in rows]
    idx = sorted(range(len(temps)), key=lambda i: temps[i])
    temps = [temps[i] for i in idx]
    cvs = [cvs[i] for i in idx]
    peaks = []
    for i in range(1, len(temps)-1):
        if cvs[i] > cvs[i-1] and cvs[i] > cvs[i+1]:
            if cvs[i] > 0:
                peaks.append((temps[i], cvs[i]))
    peaks_filtered = [(t,c) for t,c in peaks if 0.09 <= t <= 0.16]
    if len(peaks_filtered) == 2:
        t_peaks = sorted([p[0] for p in peaks_filtered])
        if t_peaks[1] - t_peaks[0] > 0.02:
            return 1.0
    return 0.0


# === block: score_2 (check id='sbc_op') ===
def score_2(artifact, step, ctx):
    rows = artifact
    temps = [float(r['temperature']) for r in rows]
    ops = [float(r['Op']) for r in rows]
    idx = sorted(range(len(temps)), key=lambda i: temps[i])
    temps = [temps[i] for i in idx]
    ops = [ops[i] for i in idx]
    max_op = max(ops)
    score = 0.0
    if max_op < 0.6:
        score += 0.3
    sharp = False
    for i in range(len(temps)):
        for j in range(i+1, len(temps)):
            if temps[j] - temps[i] < 0.02 and abs(ops[j] - ops[i]) > 0.3:
                sharp = True
                break
        if sharp:
            break
    if not sharp:
        score += 0.4
    target = 0.12
    idx12 = min(range(len(temps)), key=lambda i: abs(temps[i] - target))
    if ops[idx12] <= 0.25:
        score += 0.15
    target06 = 0.06
    idx06 = min(range(len(temps)), key=lambda i: abs(temps[i] - target06))
    if ops[idx06] >= 0.3:
        score += 0.15
    return score


# === block: score_3 (check id='sbc_cv') ===
def score_3(artifact, step, ctx):
    rows = artifact
    temps = [float(r['temperature']) for r in rows]
    cvs = [float(r['c_V']) for r in rows]
    idx = sorted(range(len(temps)), key=lambda i: temps[i])
    temps = [temps[i] for i in idx]
    cvs = [cvs[i] for i in idx]
    peaks = []
    for i in range(1, len(temps)-1):
        if cvs[i] > cvs[i-1] and cvs[i] > cvs[i+1]:
            if cvs[i] > 0:
                peaks.append((temps[i], cvs[i]))
    peaks_filtered = [(t,c) for t,c in peaks if 0.09 <= t <= 0.14]
    if len(peaks_filtered) == 1:
        return 1.0
    return 0.0


_SCORERS = {
    'tbc_op': score_0,
    'tbc_cv': score_1,
    'sbc_op': score_2,
    'sbc_cv': score_3,
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
