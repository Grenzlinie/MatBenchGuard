import os
import json
import csv

# === author imports / helpers ===
import csv, os


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
    import csv, os
    artifact_path = os.path.join(outputs_dir, 'elastic_constants_pressure.csv')
    rows = []
    if os.path.exists(artifact_path):
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    return {'elastic_data': rows}


# === block: score_0 (check id='s2') ===
def score_0(artifact, step, ctx):
    rows = artifact
    data = []
    for r in rows:
        try:
            p = float(r['pressure (GPa)'])
            c11 = float(r['C11 (GPa)'])
            c12 = float(r['C12 (GPa)'])
            c44 = float(r['C44 (GPa)'])
            cp = float(r['Cprime (GPa)'])
        except (ValueError, KeyError):
            continue
        data.append((p, c44, cp))
    data.sort(key=lambda x: x[0])

    # positivity and reasonable upper bound
    all_ok = all(c44 > 0 and c44 < 200 for _, c44, _ in data)
    score_pos = 1.0 if all_ok else 0.0

    # zero‑pressure check
    zero_c44 = None
    for p, c44, _ in data:
        if abs(p) < 0.1:
            zero_c44 = c44
            break
    score_zero = 1.0 if (zero_c44 is not None and 10 <= zero_c44 <= 40) else 0.0

    def mean_c44(pmin, pmax):
        vals = [c44 for p, c44, _ in data if pmin <= p <= pmax]
        return sum(vals)/len(vals) if vals else 0.0

    low1 = mean_c44(20, 50)
    high1 = mean_c44(100, 150)
    score_soft1 = 1.0 if low1 > high1 else 0.0

    low2 = mean_c44(275, 300)
    high2 = mean_c44(350, 400)
    score_soft2 = 1.0 if low2 > high2 else 0.0

    def mean_cp(pmin, pmax):
        vals = [cp for p, _, cp in data if pmin <= p <= pmax]
        return sum(vals)/len(vals) if vals else 0.0

    low1_cp = mean_cp(20, 50)
    high1_cp = mean_cp(100, 150)
    score_cp = 1.0 if low1_cp > high1_cp else 0.0

    final = 0.1*score_pos + 0.1*score_zero + 0.3*score_soft1 + 0.2*score_soft2 + 0.3*score_cp
    return final


# === block: score_1 (check id='s3') ===
def score_1(artifact, step, ctx):
    rows = artifact
    data = {}
    for r in rows:
        try:
            p = float(r['Pressure (GPa)'])
            a = float(r['A'])
        except (ValueError, KeyError):
            continue
        data[p] = a

    required = [0, 60, 100]
    if all(k in data for k in required):
        ok = (data[60] < data[0] and data[60] < data[100])
        score = 1.0 if ok else 0.0
    else:
        score = 0.0
    return score


# === block: score_2 (check id='s4') ===
def score_2(artifact, step, ctx):
    rows = artifact
    met = 0
    total = 0
    for r in rows:
        try:
            c0 = float(r['C44_0K (GPa)'])
            c1000 = float(r['C44_1000K (GPa)'])
            c2000 = float(r['C44_2000K (GPa)'])
        except (ValueError, KeyError):
            continue
        ok1 = c1000 >= c0
        ok2 = c2000 >= c0
        met += (1 if ok1 else 0) + (1 if ok2 else 0)
        total += 2
    return met / total if total else 0.0


# === block: score_3 (check id='s6') ===
def score_3(artifact, step, ctx):
    rh_rows = artifact
    ectx = ctx.get('elastic_data', [])
    c44_dict = {}
    for r in ectx:
        try:
            p = float(r['pressure (GPa)'])
            c44 = float(r['C44 (GPa)'])
        except (ValueError, KeyError):
            continue
        c44_dict[p] = c44
    matched = 0
    total = 0
    for r in rh_rows:
        try:
            p = float(r['Pressure (GPa)'])
            crh1 = float(r['C_RH1 (GPa)'])
            crh2 = float(r['C_RH2 (GPa)'])
        except (ValueError, KeyError):
            continue
        if p in c44_dict:
            c44 = c44_dict[p]
            if c44 > 0:
                mean_val = (crh1 + crh2) / 2.0
                if abs(mean_val - c44) / c44 < 0.5:
                    matched += 1
            total += 1
    return matched / total if total else 0.0


_SCORERS = {
    's2': score_0,
    's3': score_1,
    's4': score_2,
    's6': score_3,
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
