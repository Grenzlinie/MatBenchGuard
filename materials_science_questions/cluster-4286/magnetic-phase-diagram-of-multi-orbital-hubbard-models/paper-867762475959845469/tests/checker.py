import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from collections import defaultdict
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
    return {}


# === block: score_0 (check id='magnetization_curves_check') ===
def score_0(artifact, step, ctx):
    REF_POINTS = {
        0.175: [(0.005,0.82), (0.010,0.82), (0.015,0.40), (0.020,0.10), (0.025,0.02), (0.030,0.00)],
        0.2:   [(0.005,0.82), (0.010,0.82), (0.020,0.50), (0.030,0.10), (0.040,0.02), (0.050,0.00)],
        0.25:  [(0.005,0.82), (0.010,0.82), (0.020,0.82), (0.030,0.60), (0.035,0.10), (0.040,0.02), (0.050,0.00)],
        0.3:   [(0.005,0.82), (0.010,0.82), (0.020,0.82), (0.030,0.82), (0.035,0.55), (0.040,0.10), (0.050,0.01), (0.060,0.00)],
        0.35:  [(0.005,0.82), (0.010,0.82), (0.020,0.82), (0.030,0.82), (0.035,0.72), (0.040,0.45), (0.045,0.10), (0.050,0.01), (0.060,0.00)],
        0.4:   [(0.005,0.82), (0.010,0.82), (0.020,0.82), (0.030,0.82), (0.035,0.78), (0.040,0.60), (0.045,0.30), (0.050,0.10), (0.060,0.01)]
    }
    TOL = 0.12

    rows = [r for r in artifact if r.get('x') is not None and r.get('T') is not None and r.get('M') is not None]
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            x = float(r['x'])
            t = float(r['T'])
            m = float(r['M'])
        except (ValueError, KeyError):
            continue
        data.setdefault(x, []).append((t, m))

    scores = []
    for x, pts in data.items():
        if x not in REF_POINTS:
            continue
        pts.sort(key=lambda p: p[0])
        T_agent = np.array([p[0] for p in pts])
        M_agent = np.array([p[1] for p in pts])
        if len(T_agent) < 2:
            scores.append(0.0)
            continue
        ref_list = REF_POINTS[x]
        doping_score = 0.0
        for T_ref, M_ref in ref_list:
            if T_ref < T_agent[0] or T_ref > T_agent[-1]:
                point_score = 0.0
            else:
                M_interp = np.interp(T_ref, T_agent, M_agent)
                err = abs(M_interp - M_ref)
                point_score = max(0.0, 1.0 - max(0.0, err - TOL) / TOL)
            doping_score += point_score
        doping_score /= len(ref_list)
        scores.append(doping_score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='phase_diagram_check') ===
def score_1(artifact, step, ctx):
    rows = [r for r in artifact if r.get('x') is not None and r.get('Tc') is not None]
    if not rows:
        return 0.0
    agent = {}
    for r in rows:
        try:
            x = float(r['x'])
            tc = float(r['Tc'])
            agent[x] = tc
        except (ValueError, KeyError):
            continue
    if not agent:
        return 0.0

    # Gold Tc values from paper Fig. 4 (E1=-0.125 eV, E2=-0.25 eV, t=0.3 eV) in eV/k_B
    gold = {0.175: 0.015, 0.2: 0.025, 0.25: 0.033, 0.3: 0.040, 0.35: 0.048, 0.4: 0.055}
    abstol = 0.02
    reltol = 0.05

    scores = []
    for x, ref in gold.items():
        val = agent.get(x)
        if val is None:
            scores.append(0.0)
            continue
        err = abs(val - ref)
        tol = max(abstol, reltol * abs(ref))
        if err <= tol:
            scores.append(1.0)
        elif err > 2 * tol:
            scores.append(0.0)
        else:
            scores.append(1.0 - (err - tol) / tol)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='zener_fraction_check') ===
def score_2(artifact, step, ctx):
    rows = [r for r in artifact if r.get('T') is not None and r.get('p_f') is not None]
    if not rows:
        return 0.0

    pts = []
    for r in rows:
        try:
            T_val = float(r['T'])
            p_f = float(r['p_f'])
        except (ValueError, KeyError):
            continue
        pts.append((T_val, p_f))

    if not pts:
        return 0.0

    pts.sort(key=lambda p: p[0])
    T_agent = np.array([p[0] for p in pts])
    P_agent = np.array([p[1] for p in pts])

    # Basic range gate
    if np.any(P_agent < -0.01) or np.any(P_agent > 1.01):
        return 0.0

    # Hidden reference (T, p_f) points from the paper's Fig.4 inset for x=0.3
    REF_POINTS = [
        (0.01, 0.85),
        (0.035, 0.5),
        (0.045, 0.02)
    ]
    TOL = 0.30

    scores = []
    for T_ref, P_ref in REF_POINTS:
        if T_ref < T_agent[0] or T_ref > T_agent[-1]:
            scores.append(0.0)
        else:
            P_interp = np.interp(T_ref, T_agent, P_agent)
            err = abs(P_interp - P_ref)
            point_score = max(0.0, 1.0 - err / TOL)
            scores.append(point_score)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='cross_consistency_check') ===
def score_3(artifact, step, ctx):
    # This scorer uses the magnetization_curves.csv artifact passed by the framework.
    # It also reads phase_diagram.csv from /app/outputs/.
    pd_path = '/app/outputs/phase_diagram.csv'
    if not os.path.exists(pd_path):
        return 0.0
    pd_rows = []
    with open(pd_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pd_rows.append(row)
    if not pd_rows:
        return 0.0
    phase_tc = {}
    for r in pd_rows:
        try:
            x = float(r['x'])
            tc = float(r['Tc'])
            phase_tc[x] = tc
        except (ValueError, KeyError):
            continue
    if not phase_tc:
        return 0.0
    # group magnetization data
    data = defaultdict(list)
    for r in artifact:
        try:
            x = float(r['x'])
            T = float(r['T'])
            M = float(r['M'])
            data[x].append((T, M))
        except (ValueError, KeyError):
            continue
    match_count = 0
    total = 0
    for x, pts in data.items():
        if x not in phase_tc:
            continue
        total += 1
        pts.sort(key=lambda p: p[0])
        T_vals = np.array([p[0] for p in pts])
        M_vals = np.array([p[1] for p in pts])
        if len(T_vals) < 3:
            continue
        dM = -np.gradient(M_vals, T_vals)
        idx = np.argmax(dM)
        tc_est = T_vals[idx]
        if abs(tc_est - phase_tc[x]) < 0.01:
            match_count += 1
    if total == 0:
        return 0.0
    return match_count / total


_SCORERS = {
    'magnetization_curves_check': score_0,
    'phase_diagram_check': score_1,
    'zener_fraction_check': score_2,
    'cross_consistency_check': score_3,
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
