import os
import json
import csv

# === author imports / helpers ===
import math

class np:
    @staticmethod
    def log(values):
        return [math.log(v) for v in values]

    @staticmethod
    def polyfit(x, y, deg):
        if deg != 1:
            raise NotImplementedError("Only deg=1 supported")
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_xx = sum(xi * xi for xi in x)
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
        intercept = (sum_y - slope * sum_x) / n
        return [slope, intercept]


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
        required_B = [1.0, 2.0, 4.0, 8.0, 12.0]
        data = {}
        for row in artifact:
            try:
                b = float(row['B'])
                p = float(row['p_over_n'])
                v = float(row['value'])
            except (ValueError, KeyError):
                continue
            if b not in data:
                data[b] = []
            data[b].append((p, v))

        actual_B = set(data.keys())
        n_ok = len(set(required_B).intersection(actual_B))
        if n_ok == 0:
            return 0.0

        # peak check
        peak_score = 0.0
        for b in required_B:
            if b not in data:
                continue
            pts = data[b]
            if not pts:
                continue
            max_p = max(pts, key=lambda x: x[1])[0]
            if abs(max_p - 1.0) < 0.005:
                peak_score += 1.0
        peak_score = peak_score / len(required_B) if len(required_B) > 0 else 0.0

        # slope check at p/n = 1
        slope_score = 0.0
        Bvals = []
        Vvals = []
        for b in required_B:
            if b not in data:
                continue
            for p, v in data[b]:
                if abs(p - 1.0) < 1e-6:
                    Bvals.append(b)
                    Vvals.append(v)
                    break
        if len(Bvals) >= 2:
            logB = np.log(Bvals)
            logV = np.log(Vvals)
            slope, _ = np.polyfit(logB, logV, 1)
            if abs(slope - 2.0) < 0.3:
                slope_score = 1.0
            else:
                slope_score = max(0.0, 1.0 - (abs(slope - 2.0) - 0.3) / 0.7)

        # width monotonicity
        fwhm_list = []
        for b in sorted(required_B):
            if b not in data:
                fwhm_list.append(None)
                continue
            pts = sorted(data[b], key=lambda x: x[0])
            vals = [v for _, v in pts]
            ps = [p for p, _ in pts]
            max_val = max(vals)
            half = max_val / 2.0
            left = None
            right = None
            for i in range(len(pts)):
                if vals[i] >= half:
                    if left is None:
                        left = ps[i]
                    right = ps[i]
            if left is not None and right is not None:
                fwhm = right - left
                if fwhm < 0.0:
                    fwhm = 0.0
            else:
                fwhm = 0.0
            fwhm_list.append(fwhm)

        width_score = 0.0
        monotonic = True
        prev = None
        for f in fwhm_list:
            if f is None:
                continue
            if prev is not None and f > prev + 1e-9:
                monotonic = False
                break
            prev = f
        if monotonic:
            width_score = 1.0

        # penalize missing required B fields
        missing_factor = n_ok / len(required_B)
        total = peak_score * 0.5 + slope_score * 0.3 + width_score * 0.2
        total *= missing_factor
        return min(1.0, max(0.0, total))


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
