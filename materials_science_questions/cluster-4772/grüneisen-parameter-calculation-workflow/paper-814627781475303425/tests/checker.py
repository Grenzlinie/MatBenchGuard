import os
import json
import csv

# === author imports / helpers ===
import os, json, csv
try:
    import numpy as np
except ImportError:
    class _Array(list):
        def __sub__(self, other):
            if isinstance(other, (int, float)):
                return [x - other for x in self]
            return NotImplemented
        def __rsub__(self, other):
            return [other - x for x in self]
    class _DummyNumpy:
        @staticmethod
        def array(data):
            return _Array(data)
        @staticmethod
        def abs(x):
            return [abs(v) for v in x]
        @staticmethod
        def argmin(x):
            return min(range(len(x)), key=lambda i: x[i])
    np = _DummyNumpy()


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
    systems = ['si', 'hsi', 'ge', 'hge']
    for sys in systems:
        path = os.path.join(outputs_dir, f'{sys}_thermo.csv')
        rows = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
        T = np.array([float(r['T']) for r in rows])
        B2D = np.array([float(r['B2D']) for r in rows])
        B2D_star = np.array([float(r['B2D_star']) for r in rows])
        idx300 = np.argmin(np.abs(T - 300))
        if idx300 > 0 and idx300 < len(T)-1:
            dT = T[idx300+1] - T[idx300-1]
            if dT > 0:
                slope_B2D = (B2D[idx300+1] - B2D[idx300-1]) / dT
                slope_B2D_star = (B2D_star[idx300+1] - B2D_star[idx300-1]) / dT
            else:
                slope_B2D = 0.0
                slope_B2D_star = 0.0
        else:
            slope_B2D = 0.0
            slope_B2D_star = 0.0
        ctx[f'{sys}_slope_B2D'] = slope_B2D
        ctx[f'{sys}_slope_B2D_star'] = slope_B2D_star
    return ctx


# === block: score_0 (check id='si_struct') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) < 20:
        return 0.0
    try:
        Ts = [float(r['T']) for r in artifact]
    except:
        return 0.0
    if min(Ts) > 10 or max(Ts) < 590:
        return 0.0
    return 1.0


# === block: score_1 (check id='hsi_struct') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) < 20:
        return 0.0
    try:
        Ts = [float(r['T']) for r in artifact]
    except:
        return 0.0
    if min(Ts) > 10 or max(Ts) < 590:
        return 0.0
    return 1.0


# === block: score_2 (check id='ge_struct') ===
def score_2(artifact, step, ctx):
    if not artifact or len(artifact) < 20:
        return 0.0
    try:
        Ts = [float(r['T']) for r in artifact]
    except:
        return 0.0
    if min(Ts) > 10 or max(Ts) < 590:
        return 0.0
    return 1.0


# === block: score_3 (check id='hge_struct') ===
def score_3(artifact, step, ctx):
    if not artifact or len(artifact) < 20:
        return 0.0
    try:
        Ts = [float(r['T']) for r in artifact]
    except:
        return 0.0
    if min(Ts) > 10 or max(Ts) < 590:
        return 0.0
    return 1.0


# === block: score_4 (check id='slope_consistency') ===
def score_4(artifact, step, ctx):
    gold = step.get('gold_slope_diff', {})
    target_si = gold.get('Si_B2D_increase', 5.0e-5)
    target_ge = gold.get('Ge_B2D_increase', 2.4e-5)
    delta_si_B2D = ctx['hsi_slope_B2D'] - ctx['si_slope_B2D']
    delta_ge_B2D = ctx['hge_slope_B2D'] - ctx['ge_slope_B2D']
    delta_si_B2D_star = ctx['hsi_slope_B2D_star'] - ctx['si_slope_B2D_star']
    delta_ge_B2D_star = ctx['hge_slope_B2D_star'] - ctx['ge_slope_B2D_star']
    s1 = max(0.0, 1.0 - abs(delta_si_B2D - target_si) / (0.15 * target_si)) if target_si else 0.0
    s2 = max(0.0, 1.0 - abs(delta_ge_B2D - target_ge) / (0.15 * target_ge)) if target_ge else 0.0
    s3 = 0.5 if delta_si_B2D_star > 0 else 0.0
    s4 = 0.5 if delta_ge_B2D_star > 0 else 0.0
    return (s1 + s2 + s3 + s4) / 4.0


# === block: score_5 (check id='anharm_check') ===
def score_5(artifact, step, ctx):
    gold = step.get('gold_values', {})
    tol = step.get('tolerance', 2.0)
    keys = ['si_a_dB2D_star_da', 'hsi_a_dB2D_star_da', 'ge_a_dB2D_star_da', 'hge_a_dB2D_star_da']
    scores = []
    for k in keys:
        ref = gold.get(k)
        if ref is None or k not in artifact:
            scores.append(0.0)
        else:
            diff = abs(artifact[k] - ref)
            scores.append(1.0 if diff <= tol else 0.0)
    return sum(scores) / len(scores)


_SCORERS = {
    'si_struct': score_0,
    'hsi_struct': score_1,
    'ge_struct': score_2,
    'hge_struct': score_3,
    'slope_consistency': score_4,
    'anharm_check': score_5,
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
