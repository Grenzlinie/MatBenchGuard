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


# === block: score_0 (check id='size_effect_overlap') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        try:
            tol = float(step.get('tolerance', 0.05))
        except (ValueError, TypeError):
            tol = 0.05
        vals_500 = {}
        vals_2000 = {}
        try:
            for row in artifact:
                if row is None:
                    continue
                if not isinstance(row, dict):
                    continue
                size = row.get('system_size')
                ang = row.get('angle_alpha')
                val = row.get('poisson_ratio')
                if size is None or ang is None or val is None:
                    continue
                try:
                    size = int(size)
                    ang = float(ang)
                    val = float(val)
                except (ValueError, TypeError):
                    continue
                if size == 500:
                    vals_500[ang] = val
                elif size == 2000:
                    vals_2000[ang] = val
        except Exception:
            return 0.0
        if not vals_500 or not vals_2000:
            return 0.0
        max_diff = 0.0
        for ang in vals_500:
            if ang in vals_2000:
                diff = abs(vals_500[ang] - vals_2000[ang])
                if diff > max_diff:
                    max_diff = diff
        if max_diff <= tol:
            return 1.0
        elif max_diff <= 2*tol:
            return 1.0 - (max_diff - tol) / tol
        else:
            return 0.0


# === block: score_1 (check id='concentration_effect') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = {}
        for row in artifact:
            c = float(row['concentration'])
            v = float(row['poisson_ratio'])
            rows[c] = v
        def get_val(target, tolerance=0.2):
            best = None
            for c, v in rows.items():
                if abs(c - target) < tolerance:
                    if best is None or abs(c - target) < abs(best[0] - target):
                        best = (c, v)
            return None if best is None else best[1]
        c0 = get_val(0.0)
        c5 = get_val(5.0)
        c14 = get_val(14.0)
        if None in (c0, c5, c14):
            return 0.0
        score = 0.0
        if -0.20 <= c0 <= -0.10:
            score += 0.3
        if -0.34 <= c14 <= -0.24:
            score += 0.3
        if c0 >= c5 and c5 >= c14:
            score += 0.4
        return score


_SCORERS = {
    'size_effect_overlap': score_0,
    'concentration_effect': score_1,
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
