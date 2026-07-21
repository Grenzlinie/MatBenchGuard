import os
import json
import csv

# === author imports / helpers ===
import csv, io, math


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


# === block: score_0 (check id='tc_curve') ===
def score_0(artifact, step, ctx):
    import csv, io, math

    def read_csv_artifact(artifact):
        # artifact is whatever load_artifact returned; handle both dict rows and list rows
        if not artifact:
            return None, None
        c_vals = []
        tc_vals = []
        if isinstance(artifact[0], dict):
            # header present
            for row in artifact:
                try:
                    c_vals.append(float(row['c']))
                    tc_vals.append(float(row['Tc_K']))
                except (KeyError, ValueError):
                    # ignore problematic rows
                    pass
        elif isinstance(artifact[0], (list, tuple)):
            # headerless
            for row in artifact:
                if len(row) < 2:
                    continue
                try:
                    c_vals.append(float(row[0]))
                    tc_vals.append(float(row[1]))
                except ValueError:
                    pass
        else:
            return None, None
        return c_vals, tc_vals

    def gold_tc(c):
        return 1200.0 * math.sin(math.pi * c / 2.0)

    c_vals, tc_vals = read_csv_artifact(artifact)
    if not c_vals or len(c_vals) < 10:
        return 0.0

    # sort by c
    pairs = sorted(zip(c_vals, tc_vals), key=lambda x: x[0])
    cs = [p[0] for p in pairs]
    tcs = [p[1] for p in pairs]

    # pointwise score
    pointwise = []
    for ci, ti in zip(cs, tcs):
        gold = gold_tc(ci)
        diff = abs(ti - gold)
        if diff <= 150.0:
            pointwise.append(1.0)
        else:
            # linearly decay from 150 to 300
            rel = (diff - 150.0) / 150.0
            score_i = max(0.0, 1.0 - rel)
            pointwise.append(score_i)
    pointwise_score = sum(pointwise) / len(pointwise) if pointwise else 0.0

    # structural checks
    # find peak index
    peak_idx = max(range(len(tcs)), key=lambda i: tcs[i])
    peak_c = cs[peak_idx]

    struct_score = 0.0
    # peak location near c=1.0
    if 0.9 <= peak_c <= 1.1:
        struct_score += 0.2
    # monotonic increase before peak
    inc_ok = True
    for i in range(1, peak_idx+1):
        if tcs[i] < tcs[i-1] - 1e-6:
            inc_ok = False
            break
    if inc_ok:
        struct_score += 0.1
    # monotonic decrease after peak
    dec_ok = True
    for i in range(peak_idx+1, len(tcs)):
        if tcs[i] > tcs[i-1] + 1e-6:
            dec_ok = False
            break
    if dec_ok:
        struct_score += 0.1
    # Tc near c=2.0 small (< 80 K)
    # find point closest to c=2.0
    idx_c2 = min(range(len(cs)), key=lambda i: abs(cs[i] - 2.0))
    if abs(tcs[idx_c2]) < 80.0:
        struct_score += 0.1

    overall = pointwise_score * 0.5 + struct_score
    return max(0.0, min(1.0, overall))


_SCORERS = {
    'tc_curve': score_0,
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
