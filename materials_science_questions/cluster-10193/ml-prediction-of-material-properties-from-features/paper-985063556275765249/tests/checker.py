import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
        mae_num = 0.0
        mse_num = 0.0
        n = 0
        values = []
        for row in artifact:
            try:
                t = float(row.get("true_segregation_energy", 0))
                p = float(row.get("predicted_segregation_energy", 0))
            except:
                continue
            diff = t - p
            mae_num += abs(diff)
            mse_num += diff * diff
            values.append(t)
            values.append(p)
            n += 1
        if n == 0:
            return 0.0
        mae = mae_num / n
        mse = mse_num / n

        target = step.get("target", {})
        mae_full = target.get("mae_full", 0.07)
        mae_max = target.get("mae_max", 0.15)
        if mae <= mae_full:
            mae_score = 1.0
        else:
            mae_score = max(0.0, 1.0 - (mae - mae_full) / (mae_max - mae_full))

        mse_full = target.get("mse_full", 0.01)
        mse_max = target.get("mse_max", 0.05)
        if mse <= mse_full:
            mse_score = 1.0
        else:
            mse_score = max(0.0, 1.0 - (mse - mse_full) / (mse_max - mse_full))

        # distribution span score
        if values:
            vmin = min(values)
            vmax = max(values)
            span = vmax - vmin
            span_min = target.get("span_min", 0.5)
            span_max = target.get("span_max", 1.5)
            if span_min <= span <= span_max:
                span_score = 1.0
            elif span < span_min:
                span_score = max(0.0, span / span_min)
            else:
                span_score = max(0.0, 1.0 - (span - span_max) / span_max)
        else:
            span_score = 0.0

        w_mae = 0.4
        w_mse = 0.4
        w_span = 0.2
        return w_mae * mae_score + w_mse * mse_score + w_span * span_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
        correct = 0
        total = 0
        for row in artifact:
            try:
                ts = int(float(row.get("true_state", -1)))
                ps = int(float(row.get("predicted_state", -1)))
            except:
                continue
            if ts == ps and ts in (0,1):
                correct += 1
            total += 1
        if total == 0:
            return 0.0
        acc = correct / total
        target = step.get("target", {})
        acc_full = target.get("acc_full", 0.89)
        acc_zero = target.get("acc_zero", 0.80)
        if acc >= acc_full:
            return 1.0
        else:
            return max(0.0, (acc - acc_zero) / (acc_full - acc_zero))


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
        correct = 0
        total = 0
        for row in artifact:
            try:
                ts = int(float(row.get("true_state", -1)))
                ps = int(float(row.get("predicted_state", -1)))
            except:
                continue
            if ts == ps and ts in (0,1):
                correct += 1
            total += 1
        if total == 0:
            return 0.0
        acc = correct / total
        target = step.get("target", {})
        acc_full = target.get("acc_full", 0.86)
        acc_zero = target.get("acc_zero", 0.75)
        if acc >= acc_full:
            return 1.0
        else:
            return max(0.0, (acc - acc_zero) / (acc_full - acc_zero))


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
