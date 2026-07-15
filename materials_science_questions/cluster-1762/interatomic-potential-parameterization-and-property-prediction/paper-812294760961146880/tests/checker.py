import os
import json
import csv

# === author imports / helpers ===
import csv
from io import StringIO


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
        import csv
        from io import StringIO
        inline_data = spec['inline_ion_data']
        f = StringIO(inline_data)
        reader = csv.DictReader(f)
        rows = list(reader)
        def fit_group(group_rows):
            xs = []
            ys = []
            for r in group_rows:
                z = float(r['charge_z'])
                radius = float(r['radius_r_angstrom'])
                V = float(r['V_ion_cc_per_mol'])
                x_val = z ** 2 / (radius ** 4)
                y_val = V / (radius ** 3)
                xs.append(x_val)
                ys.append(y_val)
            n = len(xs)
            if n < 2:
                return 0.0, 0.0
            sum_x = sum(xs)
            sum_y = sum(ys)
            sum_xy = sum(x * y for x, y in zip(xs, ys))
            sum_xx = sum(x * x for x in xs)
            denom = n * sum_xx - sum_x * sum_x
            if denom == 0:
                return None, None
            S = (n * sum_xy - sum_x * sum_y) / denom
            A = (sum_y - S * sum_x) / n
            B = -S
            return A, B
        cations = [r for r in rows if r['ion_type'] == 'cation']
        anions = [r for r in rows if r['ion_type'] == 'anion']
        cation_A, cation_B = fit_group(cations)
        anion_A, anion_B = fit_group(anions)
        ctx = {
            'expected': {
                'cation_A': cation_A,
                'cation_B': cation_B,
                'anion_A': anion_A,
                'anion_B': anion_B
            }
        }
        return ctx


# === block: score_0 (check id='step_02_fit_constants') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is the loaded dict from constants.json
        expected = ctx['expected']
        tolerance = step.get('tolerance', {})
        abs_tol = tolerance.get('abs_tol', 0.5)
        rel_tol = tolerance.get('rel_tol', 0.10)
        fields = step.get('fields', ['cation_A', 'cation_B', 'anion_A', 'anion_B'])
        total = 0.0
        N = len(fields)
        for field in fields:
            if field not in artifact or field not in expected:
                continue
            val = float(artifact[field])
            exp = float(expected[field])
            diff = abs(val - exp)
            # use whichever tolerance is larger: absolute or relative
            allowed = max(abs_tol, rel_tol * max(abs(exp), 1e-6))
            if diff <= allowed:
                total += 1.0
        return total / N if N > 0 else 0.0


_SCORERS = {
    'step_02_fit_constants': score_0,
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
