import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    class _NumpyFallback:
        @staticmethod
        def array(it):
            return list(it)
        @staticmethod
        def trapz(y, x=None, dx=1.0):
            if x is None:
                x = [i * dx for i in range(len(y))]
            if len(x) != len(y):
                raise ValueError('x and y must have same length')
            area = 0.0
            for i in range(len(x)-1):
                area += (x[i+1] - x[i]) * (y[i] + y[i+1]) / 2.0
            return area
    np = _NumpyFallback


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
    ctx = {}
    for step in spec['steps']:
        if step['id'] == 'check_band_gaps':
            ctx['gold_band_gaps'] = step['gold_band_gaps']
            ctx['tol_bandgap'] = step['tolerance_abs_bandgap_eV']
        elif step['id'] == 'check_absorption':
            ctx['energy_range'] = step['energy_range_eV']
            ctx['min_ratio'] = step['required_ratio_min']
    return ctx


# === block: score_0 (check id='check_band_gaps') ===
def score_0(artifact, step, ctx):
    gold_rows = ctx['gold_band_gaps']
    tol = ctx['tol_bandgap']
    # artifact is list of dicts with keys: strain_percent, bandgap_eV, bandgap_type
    artifacts_by_strain = {}
    for r in artifact:
        sp = float(r['strain_percent'])
        artifacts_by_strain[sp] = r
    correct = 0
    total = len(gold_rows)
    for g in gold_rows:
        sp = float(g['strain_percent'])
        agent = artifacts_by_strain.get(sp)
        if agent is None:
            continue
        try:
            agent_val = float(agent['bandgap_eV'])
            agent_type = str(agent['bandgap_type']).strip().lower()
            gold_val = float(g['bandgap_eV'])
            gold_type = str(g['bandgap_type']).strip().lower()
            if abs(agent_val - gold_val) <= tol and agent_type == gold_type:
                correct += 1
        except (ValueError, KeyError):
            continue
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='check_absorption') ===
def score_1(artifact, step, ctx):
    e_min, e_max = ctx['energy_range']
    min_ratio = ctx['min_ratio']
    # artifact is list of dicts with keys: strain, energy_eV, absorption_cm-1
    strains = set(r['strain'] for r in artifact)
    required_strains = {'0', 'p4'}
    if not required_strains.issubset(strains):
        return 0.0

    def integrate(rows, e_min, e_max):
        pts = []
        for r in rows:
            try:
                e = float(r['energy_eV'])
                a = float(r['absorption_cm-1'])
            except (ValueError, KeyError):
                continue
            if e < e_min or e > e_max:
                continue
            pts.append((e, a))
        if len(pts) < 2:
            return None
        pts.sort(key=lambda x: x[0])
        xs = np.array([p[0] for p in pts])
        ys = np.array([p[1] for p in pts])
        # simple trapezoidal
        return np.trapz(ys, xs)

    area0 = integrate([r for r in artifact if r['strain'] == '0'], e_min, e_max)
    area_p4 = integrate([r for r in artifact if r['strain'] == 'p4'], e_min, e_max)
    if area0 is None or area_p4 is None or area0 <= 0:
        return 0.0
    ratio = area_p4 / area0
    # monotonic: at least min_ratio gives full credit; if below, proportional down to 0
    if ratio >= min_ratio:
        return 1.0
    else:
        return max(0.0, ratio / min_ratio)


_SCORERS = {
    'check_band_gaps': score_0,
    'check_absorption': score_1,
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
