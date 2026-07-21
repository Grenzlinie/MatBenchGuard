import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from collections import namedtuple

_Result = namedtuple('LinregressResult', ['slope', 'intercept', 'rvalue', 'pvalue', 'stderr'])

def linregress(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    n = len(x)
    if n < 2:
        return _Result(np.nan, np.nan, np.nan, np.nan, np.nan)
    xm = np.mean(x)
    ym = np.mean(y)
    ssxm = np.sum((x - xm) ** 2)
    if ssxm == 0:
        return _Result(np.nan, ym, np.nan, np.nan, np.nan)
    slope = np.sum((x - xm) * (y - ym)) / ssxm
    intercept = ym - slope * xm
    rvalue = np.corrcoef(x, y)[0, 1] if n > 1 else np.nan
    return _Result(slope, intercept, rvalue, np.nan, np.nan)


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
    return {
        'x_m_bulk': (3 - np.sqrt(5)) / 4,
        'x_m_surf': 0.5,
        'eta_e_bulk': 2.2,
        'eta_e_surf': 2.5
    }


# === block: score_0 (check id='bulk_spin_check') ===
def score_0(artifact, step, ctx):
    tau = np.array([float(r['tau']) for r in artifact])
    G = np.array([float(r['G_bulk']) for r in artifact])
    valid = G > 0
    if not np.any(valid):
        return 0.0
    tau = tau[valid]
    G = G[valid]
    srt = np.argsort(tau)
    tau = tau[srt]
    G = G[srt]
    n = len(tau)
    if n < 4:
        return 0.0
    start = n // 2
    tau_asym = tau[start:]
    G_asym = G[start:]
    xm = ctx['x_m_bulk']
    y = G_asym ** (-1.0 / (2 * xm))
    logt = np.log(tau_asym)
    res = linregress(logt, y)
    slope = res.slope
    r2 = res.rvalue ** 2
    slope_score = max(0.0, 1.0 - abs(slope - 1.0) / 0.1)
    r2_score = min(1.0, r2 / 0.95) if r2 >= 0.0 else 0.0
    return 0.5 * slope_score + 0.5 * r2_score


# === block: score_1 (check id='surface_spin_check') ===
def score_1(artifact, step, ctx):
    tau = np.array([float(r['tau']) for r in artifact])
    G = np.array([float(r['G_surf']) for r in artifact])
    valid = G > 0
    if not np.any(valid):
        return 0.0
    tau = tau[valid]
    G = G[valid]
    srt = np.argsort(tau)
    tau = tau[srt]
    G = G[srt]
    n = len(tau)
    if n < 4:
        return 0.0
    start = n // 2
    tau_asym = tau[start:]
    G_asym = G[start:]
    xm = ctx['x_m_surf']
    y = G_asym ** (-1.0 / (2 * xm))
    logt = np.log(tau_asym)
    res = linregress(logt, y)
    slope = res.slope
    r2 = res.rvalue ** 2
    slope_score = max(0.0, 1.0 - abs(slope - 1.0) / 0.1)
    r2_score = min(1.0, r2 / 0.95) if r2 >= 0.0 else 0.0
    return 0.5 * slope_score + 0.5 * r2_score


# === block: score_2 (check id='bulk_energy_check') ===
def score_2(artifact, step, ctx):
    tau = np.array([float(r['tau']) for r in artifact])
    G = np.array([float(r['G_bulk_e']) for r in artifact])
    valid = (tau > 0) & (G > 0)
    if not np.any(valid):
        return 0.0
    tau = tau[valid]
    G = G[valid]
    srt = np.argsort(tau)
    tau = tau[srt]
    G = G[srt]
    n = len(tau)
    if n < 4:
        return 0.0
    start = n // 2
    tau_asym = tau[start:]
    G_asym = G[start:]
    logt = np.log(tau_asym)
    logG = np.log(G_asym)
    res = linregress(logt, logG)
    slope = res.slope
    r2 = res.rvalue ** 2
    eta_fit = -slope
    eta_gold = ctx['eta_e_bulk']
    eta_score = max(0.0, 1.0 - abs(eta_fit - eta_gold) / 0.3)
    r2_score = min(1.0, r2 / 0.9) if r2 >= 0.0 else 0.0
    return 0.5 * eta_score + 0.5 * r2_score


# === block: score_3 (check id='surface_energy_check') ===
def score_3(artifact, step, ctx):
    tau = np.array([float(r['tau']) for r in artifact])
    G = np.array([float(r['G_surf_e']) for r in artifact])
    valid = (tau > 0) & (G > 0)
    if not np.any(valid):
        return 0.0
    tau = tau[valid]
    G = G[valid]
    srt = np.argsort(tau)
    tau = tau[srt]
    G = G[srt]
    n = len(tau)
    if n < 4:
        return 0.0
    start = n // 2
    tau_asym = tau[start:]
    G_asym = G[start:]
    logt = np.log(tau_asym)
    logG = np.log(G_asym)
    res = linregress(logt, logG)
    slope = res.slope
    r2 = res.rvalue ** 2
    eta_fit = -slope
    eta_gold = ctx['eta_e_surf']
    eta_score = max(0.0, 1.0 - abs(eta_fit - eta_gold) / 0.3)
    r2_score = min(1.0, r2 / 0.9) if r2 >= 0.0 else 0.0
    return 0.5 * eta_score + 0.5 * r2_score


_SCORERS = {
    'bulk_spin_check': score_0,
    'surface_spin_check': score_1,
    'bulk_energy_check': score_2,
    'surface_energy_check': score_3,
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
