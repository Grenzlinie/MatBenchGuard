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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    try:
        f_vals = []
        exp_vals = []
        con_vals = []
        for row in artifact:
            f_vals.append(float(row["f"]))
            exp_vals.append(float(row["I_bar_expansion"]))
            con_vals.append(float(row["I_bar_contraction"]))
    except Exception:
        return 0.0

    if not f_vals:
        return 0.0

    def check_curve(f_arr, I_arr, invert_asymmetry):
        # 1. max at f=1 within one step
        max_idx = max(range(len(I_arr)), key=lambda i: I_arr[i])
        if abs(f_arr[max_idx] - 1.0) > 0.001:
            return False
        # 2. monotonic: non-decreasing for f<1, non-increasing for f>1 with tolerance
        idx_lt = [i for i, fv in enumerate(f_arr) if fv < 1.0]
        for a, b in zip(idx_lt, idx_lt[1:]):
            if I_arr[a] > I_arr[b] + 1e-4:
                return False
        idx_gt = [i for i, fv in enumerate(f_arr) if fv > 1.0]
        for a, b in zip(idx_gt, idx_gt[1:]):
            if I_arr[a] < I_arr[b] - 1e-4:
                return False
        # 3. asymmetry: average low vs high
        low_vals = [I_arr[i] for i, fv in enumerate(f_arr) if 0.990 <= fv < 1.0]
        high_vals = [I_arr[i] for i, fv in enumerate(f_arr) if 1.0 < fv <= 1.010]
        if len(low_vals) == 0 or len(high_vals) == 0:
            return False
        mean_low = sum(low_vals) / len(low_vals)
        mean_high = sum(high_vals) / len(high_vals)
        if invert_asymmetry:
            if not (mean_high > mean_low):
                return False
        else:
            if not (mean_low > mean_high):
                return False
        # 4. no local maximum in (0.9, 0.999) other than at f=1
        for i in range(1, len(f_arr) - 1):
            fv = f_arr[i]
            if 0.9 <= fv <= 0.999:
                if I_arr[i] > I_arr[i-1] and I_arr[i] > I_arr[i+1]:
                    return False
        return True

    exp_ok = check_curve(f_vals, exp_vals, invert_asymmetry=False)
    con_ok = check_curve(f_vals, con_vals, invert_asymmetry=True)
    return 1.0 if exp_ok and con_ok else 0.0


_SCORERS = {
    'step_01': score_0,
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
