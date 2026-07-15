import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict

class _np:
    @staticmethod
    def array(lst):
        return list(lst)
    @staticmethod
    def polyfit(x, y, deg):
        if deg != 1:
            raise ValueError('only linear')
        n = len(x)
        sumx = sum(x)
        sumy = sum(y)
        sumx2 = sum([xi*xi for xi in x])
        sumxy = sum([xi*yi for xi, yi in zip(x, y)])
        denom = n * sumx2 - sumx * sumx
        if denom == 0:
            return (0.0, sumy / n) if deg == 1 else [0.0]
        slope = (n * sumxy - sumx * sumy) / denom
        intercept = (sumy - slope * sumx) / n
        return (slope, intercept) if deg == 1 else [intercept]
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
    k_B = 8.617333262145e-5  # eV/K

    def fit_arrhenius(points):
        # points: list of (T, D)
        xs = np.array([1.0/T for T, D in points])
        ys = np.array([math.log(D) for T, D in points])
        slope, intercept = np.polyfit(xs, ys, 1)
        U = -slope * k_B
        D0 = math.exp(intercept)
        return U, D0

    def load_csv(outputs_dir):
        path = os.path.join(outputs_dir, 'diffusion_constants.csv')
        rows = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
        return rows

    gold = spec.get('gold', {})
    rows = load_csv(outputs_dir)

    system_points = defaultdict(list)
    for r in rows:
        sys = r.get('system', '').strip()
        T = float(r['temperature_K'])
        D = float(r['D_cm2_per_s'])
        if D <= 0:
            continue
        system_points[sys].append((T, D))

    refit = {}
    for sys in ['Pd', 'Nb']:
        pts = system_points.get(sys, [])
        if len(pts) >= 3:  # need at least 3 points for a fit
            U, D0 = fit_arrhenius(pts)
            refit[sys] = {'U': U, 'D0': D0}
        else:
            refit[sys] = None

    ctx = { 'gold': gold, 'refit': refit }
    return ctx


# === block: score_0 (check id='step3_diffusion_refit') ===
def score_0(artifact, step, ctx):
    systems = ['Pd', 'Nb']
    tolerances = step.get('tolerances', {})
    U_rel_tol = tolerances.get('U_relative', 0.10)
    D0_factor = tolerances.get('D0_factor', 2.0)
    total_score = 0.0
    for sys in systems:
        ref = ctx['refit'].get(sys)
        gold_val = ctx['gold'].get(sys, {})
        if not ref or not gold_val:
            continue
        ref_U, ref_D0 = ref['U'], ref['D0']
        gold_U, gold_D0 = gold_val['U'], gold_val['D0']
        U_ok = abs(ref_U - gold_U) / gold_U <= U_rel_tol if gold_U != 0 else False
        D0_ok = (gold_D0 / D0_factor <= ref_D0 <= gold_D0 * D0_factor) if gold_D0 != 0 else False
        # each parameter for each system contributes 0.25 to total (since there are 4 parameters overall)
        sys_score = (0.5 if U_ok else 0.0) + (0.5 if D0_ok else 0.0)
        total_score += sys_score / len(systems)
    return total_score


# === block: score_1 (check id='step4_consistency') ===
def score_1(artifact, step, ctx):
    artifact = artifact  # the loaded JSON dict (arrhenius_params.json)
    refit = ctx['refit']
    rel_tol = step.get('tolerances', {}).get('relative', 1e-4)
    systems = ['Pd', 'Nb']
    total_score = 0.0
    for sys in systems:
        agent = artifact.get(sys, {})
        ref = refit.get(sys)
        if not ref or not agent:
            continue
        U_ok = abs(agent.get('U', float('nan')) - ref['U']) / ref['U'] <= rel_tol
        D0_ok = abs(agent.get('D0', float('nan')) - ref['D0']) / ref['D0'] <= rel_tol
        # both fields must be ok for the system to score 1
        sys_pass = U_ok and D0_ok
        total_score += (1.0 if sys_pass else 0.0) / len(systems)
    return total_score


_SCORERS = {
    'step3_diffusion_refit': score_0,
    'step4_consistency': score_1,
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
