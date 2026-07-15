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


# === block: score_0 (check id='dispersion_peak_check') ===
def score_0(artifact, step, ctx):
    import math

    groups = {}
    for row in artifact:
        try:
            delta = float(row['delta'])
            temp = float(row['temperature'])
            q = float(row['q'])
            omega = float(row['omega'])
        except (KeyError, ValueError):
            continue
        key = (round(delta, 6), round(temp, 6))
        groups.setdefault(key, []).append((q, omega))

    score = 0.0
    if (round(0.1, 6), round(0.15, 6)) in groups:
        best_q = max(groups[(round(0.1, 6), round(0.15, 6))], key=lambda x: x[1])[0]
        if best_q >= math.pi - 0.02:
            score += 0.5
    if (round(0.6, 6), round(0.15, 6)) in groups:
        best_q = max(groups[(round(0.6, 6), round(0.15, 6))], key=lambda x: x[1])[0]
        if math.pi/2 - 0.1 <= best_q <= math.pi/2 + 0.1:
            score += 0.5
    return score


# === block: score_1 (check id='correlation_oscillation_check') ===
def score_1(artifact, step, ctx):
    import math

    groups = {}
    for row in artifact:
        try:
            delta = float(row['delta'])
            temp = float(row['temperature'])
            l = int(row['separation_l'])
            corr = float(row['correlation'])
        except (KeyError, ValueError):
            continue
        key = (round(delta, 6), round(temp, 6))
        groups.setdefault(key, []).append((l, corr))

    required = [(round(0.24,6), round(0.1,6)), (round(0.24,6), round(0.2,6)), (round(0.24,6), round(0.3,6)),
                (round(0.30,6), round(0.02,6)), (round(0.30,6), round(0.08,6)), (round(0.30,6), round(0.12,6)), (round(0.30,6), round(0.2,6))]
    total = len(required)
    correct = 0
    for key in required:
        if key not in groups:
            continue
        data = groups[key]
        data.sort(key=lambda x: x[0])
        corrs = [c for _, c in data]
        if len(corrs) < 2:
            continue
        is_monotonic = all(corrs[i] >= corrs[i+1] for i in range(len(corrs)-1))
        if key[0] == round(0.24, 6) and is_monotonic:
            correct += 1
        elif key[0] == round(0.30, 6) and not is_monotonic:
            correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_2 (check id='susceptibility_peak_shift_check') ===
def score_2(artifact, step, ctx):
    import math

    groups = {}
    for row in artifact:
        try:
            delta = float(row['delta'])
            temp = float(row['temperature'])
            q = float(row['q'])
            chi = float(row['chi_T'])
        except (KeyError, ValueError):
            continue
        key = (round(delta, 6), round(temp, 6))
        groups.setdefault(key, []).append((q, chi))

    # C1: delta=0.10, all temps (0.1,0.2,0.3) peak at pi
    c1 = 0.0
    c1_cnt = 0
    for t in [0.1, 0.2, 0.3]:
        key = (round(0.10, 6), round(t, 6))
        if key in groups:
            best_q = max(groups[key], key=lambda x: x[1])[0]
            if best_q >= math.pi - 0.02:
                c1 += 1.0
            c1_cnt += 1
    if c1_cnt > 0:
        c1 /= c1_cnt

    # C2: delta=0.30, T=0.1, peak between pi/2 and 0.9pi
    c2 = 0.0
    key = (round(0.30, 6), round(0.1, 6))
    if key in groups:
        best_q = max(groups[key], key=lambda x: x[1])[0]
        if math.pi/2 <= best_q <= 0.9*math.pi:
            c2 = 1.0

    # C3: delta=0.30, temps 0.1,0.2,0.3, q_max non-decreasing
    c3 = 0.0
    qmax = {}
    for t in [0.1, 0.2, 0.3]:
        key = (round(0.30, 6), round(t, 6))
        if key in groups:
            qmax[t] = max(groups[key], key=lambda x: x[1])[0]
    if len(qmax) == 3:
        if qmax[0.2] >= qmax[0.1] and qmax[0.3] >= qmax[0.2]:
            c3 = 1.0

    return 0.3*c1 + 0.3*c2 + 0.4*c3


_SCORERS = {
    'dispersion_peak_check': score_0,
    'correlation_oscillation_check': score_1,
    'susceptibility_peak_shift_check': score_2,
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
