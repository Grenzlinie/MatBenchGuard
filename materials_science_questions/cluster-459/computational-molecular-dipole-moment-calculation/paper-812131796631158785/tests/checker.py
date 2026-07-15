import os
import json
import csv

# === author imports / helpers ===
import csv
import math

class _np:
    @staticmethod
    def array(x, dtype=float):
        return list(x)
    
    @staticmethod
    def diff(a):
        if not isinstance(a, list):
            a = list(a)
        return [a[i+1] - a[i] for i in range(len(a)-1)]
    
    @staticmethod
    def interp(x, xp, fp, left=None, right=None):
        xs = list(xp)
        ys = list(fp)
        out = []
        if left is None and xs:
            left = ys[0]
        if right is None and xs:
            right = ys[-1]
        for ix in x:
            if ix <= xs[0]:
                out.append(left)
            elif ix >= xs[-1]:
                out.append(right)
            else:
                for j in range(len(xs)-1):
                    if xs[j] <= ix <= xs[j+1]:
                        t = (ix - xs[j]) / (xs[j+1] - xs[j])
                        out.append(ys[j] + t * (ys[j+1] - ys[j]))
                        break
        return out
    
    @staticmethod
    def mean(arr):
        v = list(arr)
        return sum(v) / len(v) if len(v) > 0 else 0.0
    
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
    
    @staticmethod
    def max(arr):
        return max(arr)
    
    @staticmethod
    def min(arr):
        return min(arr)
    
    @staticmethod
    def any(arr):
        return any(arr)

np = _np()


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
    step = spec['steps'][0]  # assume single step
    ref_wavenums = np.array(step['reference_wavenumbers'], dtype=float)
    ref_abs = np.array(step['reference_absorption'], dtype=float)
    return {'ref_wavenums': ref_wavenums, 'ref_abs': ref_abs, 'nrmse_full': step['nrmse_full'], 'nrmse_zero': step['nrmse_zero']}


# === block: score_0 (check id='step_final') ===
def score_0(artifact, step, ctx):
    import csv
    artifact_path = os.path.join('/app/outputs', 'absorption_spectrum_195K.csv')
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows or 'wavenumber' not in rows[0] or 'absorption_coefficient' not in rows[0]:
            return 0.0
        wnums = []
        abss = []
        for r in rows:
            w = float(r['wavenumber'])
            a = float(r['absorption_coefficient'])
            if a < 0:
                return 0.0
            wnums.append(w)
            abss.append(a)
        wnums = np.array(wnums)
        abss = np.array(abss)
        # validate monotonic and step size
        dw = np.diff(wnums)
        if np.any(dw <= 0) or np.max(dw) > 2.0:
            return 0.0
        # interpolate onto reference grid
        ref_w = ctx['ref_wavenums']
        interp_abs = np.interp(ref_w, wnums, abss, left=0.0, right=0.0)
        # compute NRMSE (range normalization)
        rmse = np.sqrt(np.mean((interp_abs - ctx['ref_abs'])**2))
        ref_range = np.max(ctx['ref_abs']) - np.min(ctx['ref_abs'])
        if ref_range == 0:
            nrmse = 0.0 if rmse == 0 else 1.0
        else:
            nrmse = rmse / ref_range
        full = ctx['nrmse_full']
        zero = ctx['nrmse_zero']
        if nrmse <= full:
            score = 1.0
        elif nrmse >= zero:
            score = 0.0
        else:
            score = 1.0 - (nrmse - full) / (zero - full)
        return max(0.0, min(1.0, float(score)))
    except Exception:
        return 0.0


_SCORERS = {
    'step_final': score_0,
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
