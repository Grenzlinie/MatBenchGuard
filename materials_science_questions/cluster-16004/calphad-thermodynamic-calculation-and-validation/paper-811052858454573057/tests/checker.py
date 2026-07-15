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


# === block: score_0 (check id='phase_diagram') ===
def score_0(artifact, step, ctx):
    rows = artifact

    def score_val(val, gold, tol):
        diff = abs(val - gold)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0

    # 1) congruent melting point: max T among rows with phase exactly 'B2'
    melt = None
    for r in rows:
        T = float(r['T'])
        phase_str = r['phase'].strip()
        if phase_str == 'B2':
            if melt is None or T > melt:
                melt = T
    if melt is None:
        s_melt = 0.0
    else:
        s_melt = score_val(melt, 1585.0, 10.0)

    # 2) Ti‑rich boundary at 1400 K: minimum x_Ni among rows at the temperature closest to 1400 K
    cand = [(float(r['T']), float(r['x_Ni'])) for r in rows if 'B2' in r['phase']]
    if not cand:
        s_solub = 0.0
    else:
        # find temperature nearest to 1400 K
        best_T = min(cand, key=lambda x: abs(x[0]-1400.0))[0]
        # select rows at that temperature
        xs = [x for t,x in cand if abs(t-best_T) < 1e-6]
        if not xs:
            s_solub = 0.0
        else:
            x_min = min(xs)
            s_solub = score_val(x_min, 0.495, 0.005)

    return (s_melt + s_solub) / 2.0


# === block: score_1 (check id='t0') ===
def score_1(artifact, step, ctx):
    rows = artifact
    points = [(float(r['x_Ni']), float(r['T0'])) for r in rows]
    def nearest(target):
        best = min(points, key=lambda p: abs(p[0]-target))
        return best[1]
    def score_val(val, gold, tol):
        diff = abs(val - gold)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0
    s1 = score_val(nearest(0.50), 366.5, 5.0)
    s2 = score_val(nearest(0.505), 340.0, 10.0)
    return (s1 + s2) / 2.0


# === block: score_2 (check id='ms') ===
def score_2(artifact, step, ctx):
    rows = artifact
    points = [(float(r['x_Ni']), float(r['Ms'])) for r in rows]
    def nearest(target):
        best = min(points, key=lambda p: abs(p[0]-target))
        return best[1]
    def score_val(val, gold, tol):
        diff = abs(val - gold)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0
    s1 = score_val(nearest(0.50), 333.0, 5.0)
    s2 = score_val(nearest(0.506), 230.0, 15.0)
    return (s1 + s2) / 2.0


# === block: score_3 (check id='enthalpy') ===
def score_3(artifact, step, ctx):
    rows = artifact
    points = [(float(r['x_Ni']), float(r['dH'])) for r in rows]
    def nearest(target):
        best = min(points, key=lambda p: abs(p[0]-target))
        return best[1]
    def score_val(val, gold, tol):
        diff = abs(val - gold)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0
    return score_val(nearest(0.50), 1672.0, 50.0)


# === block: score_4 (check id='stress_rate') ===
def score_4(artifact, step, ctx):
    rows = artifact
    points = [(float(r['x_Ni']), float(r['dsigma_dT_6pct'])) for r in rows]
    def nearest(target):
        best = min(points, key=lambda p: abs(p[0]-target))
        return best[1]
    def score_val(val, gold, tol):
        diff = abs(val - gold)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0
    return score_val(nearest(0.498), 6.3, 0.5)


_SCORERS = {
    'phase_diagram': score_0,
    't0': score_1,
    'ms': score_2,
    'enthalpy': score_3,
    'stress_rate': score_4,
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
