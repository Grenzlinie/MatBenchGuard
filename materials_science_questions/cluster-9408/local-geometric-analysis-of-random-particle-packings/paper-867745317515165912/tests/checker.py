import os
import json
import csv

# === author imports / helpers ===
import os
import csv
import math


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


# === block: score_0 (check id='gamma_check') ===
def score_0(artifact, step, ctx):
    import math

    file_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(file_path):
        return 0.0

    rows = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return 0.0
        has_required_cols = ('epsilon' in header) and ('frustrated_mass' in header)
        if has_required_cols:
            col_map = {c: i for i, c in enumerate(header)}
            eps_idx = col_map['epsilon']
            mass_idx = col_map['frustrated_mass']
            for row in reader:
                if len(row) < 2:
                    continue
                try:
                    eps = float(row[eps_idx])
                    mass = float(row[mass_idx])
                    rows.append((eps, mass))
                except:
                    continue
        else:
            # no named header, treat as two numeric columns
            try:
                float(header[0])
                # header is numeric, treat as data
                rows.append((float(header[0]), float(header[1])))
            except:
                pass
            for row in reader:
                if len(row) < 2:
                    continue
                try:
                    eps = float(row[0])
                    mass = float(row[1])
                    rows.append((eps, mass))
                except:
                    continue

    if len(rows) < step['hidden']['min_points']:
        return 0.0

    eps_vals = [r[0] for r in rows]
    mass_vals = [r[1] for r in rows]
    log_eps = [math.log10(v) for v in eps_vals]
    log_mass = [math.log10(v) for v in mass_vals]

    n = len(log_eps)
    mean_x = sum(log_eps) / n
    mean_y = sum(log_mass) / n
    S_xy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(log_eps, log_mass))
    S_xx = sum((xi - mean_x) ** 2 for xi in log_eps)
    S_yy = sum((yi - mean_y) ** 2 for yi in log_mass)

    if S_xx == 0:
        return 0.0

    slope = S_xy / S_xx
    r = 0.0
    if S_yy > 0:
        r = S_xy / math.sqrt(S_xx * S_yy)
    r2 = r * r
    gamma = slope

    tol = step['hidden']['tolerance']
    target = step['hidden']['gamma_target']
    if r2 >= step['hidden']['min_r2'] and abs(gamma - target) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'gamma_check': score_0,
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
