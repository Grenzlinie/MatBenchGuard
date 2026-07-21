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


# === block: score_0 (check id='nsd_monotonic') ===
def score_0(artifact, step, ctx):
    import csv
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    try:
        entries = []
        for r in rows:
            nsd = float(r['nsd_nm2'])
            por = float(r['porosity'])
            entries.append((nsd, por))
        entries.sort(key=lambda x: x[0])
        for i in range(1, len(entries)):
            if entries[i][1] >= entries[i-1][1]:  # strict decrease
                return 0.0
        return 1.0
    except:
        return 0.0


# === block: score_1 (check id='nsd_magnitudes') ===
def score_1(artifact, step, ctx):
    try:
        nsd_vals = [float(r['nsd_nm2']) for r in artifact]
        por_vals = [float(r['porosity']) for r in artifact]
        if len(nsd_vals) < 2:
            return 0.0
        min_idx = nsd_vals.index(min(nsd_vals))
        max_idx = nsd_vals.index(max(nsd_vals))
        low_ok = (nsd_vals[min_idx] < 1.0 and por_vals[min_idx] > 0.2)
        high_ok = (nsd_vals[max_idx] > 4.0 and por_vals[max_idx] < 0.1)
        return 1.0 if low_ok and high_ok else 0.0
    except:
        return 0.0


# === block: score_2 (check id='x_monotonic') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    try:
        entries = [(float(r['x']), float(r['porosity'])) for r in rows]
        entries.sort(key=lambda x: x[0])
        for i in range(1, len(entries)):
            if entries[i][1] <= entries[i-1][1]:  # strict increase
                return 0.0
        return 1.0
    except:
        return 0.0


# === block: score_3 (check id='x_magnitudes') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    try:
        rows_by_x = {}
        for r in rows:
            x_val = float(r['x'])
            rows_by_x[x_val] = r
        if 0.0 not in rows_by_x or 2.0 not in rows_by_x:
            return 0.0
        por0 = float(rows_by_x[0.0]['porosity'])
        por2 = float(rows_by_x[2.0]['porosity'])
        if por0 < 0.05 and por2 > 0.1:
            return 1.0
        else:
            return 0.0
    except:
        return 0.0


# === block: score_4 (check id='nsd_svr_monotonic') ===
def score_4(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    try:
        entries = []
        for r in rows:
            nsd = float(r['nsd_nm2'])
            svr = float(r['surface_volume_ratio'])
            entries.append((nsd, svr))
        entries.sort(key=lambda x: x[0])
        for i in range(1, len(entries)):
            if entries[i][1] <= entries[i-1][1]:  # strict increase
                return 0.0
        return 1.0
    except:
        return 0.0


# === block: score_5 (check id='x_svr_positive') ===
def score_5(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    try:
        for r in rows:
            svr = float(r['surface_volume_ratio'])
            if svr <= 0.0:
                return 0.0
        return 1.0
    except:
        return 0.0


_SCORERS = {
    'nsd_monotonic': score_0,
    'nsd_magnitudes': score_1,
    'x_monotonic': score_2,
    'x_magnitudes': score_3,
    'nsd_svr_monotonic': score_4,
    'x_svr_positive': score_5,
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