import os
import json
import csv
import math

# ----------------------------------------------------------------------
#  imports with pure‑Python fallback for numpy / scipy
# ----------------------------------------------------------------------
try:
    import numpy as np
    from scipy.stats import linregress as _scipy_linregress
    def linregress(x, y):
        return _scipy_linregress(x, y)
except ImportError:
    from collections import namedtuple

    def linregress(x, y):
        n = len(x)
        if n < 2:
            return namedtuple('LR', 'slope intercept rvalue pvalue stderr')(0, 0, 0, 0, 0)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xx = sum(xi*xi for xi in x)
        sum_xy = sum(xi*yi for xi, yi in zip(x, y))
        denom = n * sum_xx - sum_x * sum_x
        if abs(denom) < 1e-20:
            return namedtuple('LR', 'slope intercept rvalue pvalue stderr')(0, 0, 0, 0, 0)
        slope = (n * sum_xy - sum_x * sum_y) / denom
        intercept = (sum_y - slope * sum_x) / n
        mean_y = sum_y / n
        ss_tot = sum((yi - mean_y) ** 2 for yi in y)
        ss_res = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
        if ss_tot > 0 and ss_tot > ss_res:
            r = math.sqrt(1 - ss_res / ss_tot)
        else:
            r = 0.0
        r_value = r if slope >= 0 else -r
        if n > 2:
            var_y = ss_res / (n - 2)
        else:
            var_y = 0.0
        std_err = math.sqrt(var_y / denom) if denom > 0 else 0.0
        LR = namedtuple('LR', 'slope intercept rvalue pvalue stderr')
        return LR(slope, intercept, r_value, 0.0, std_err)

    class _np_fallback:
        @staticmethod
        def array(iterable):
            return list(iterable)

    np = _np_fallback()


# ----------------------------------------------------------------------
#  output contract validation (kept identical to original grading)
# ----------------------------------------------------------------------
def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = os.path.join(out_dir, base)
        if not os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = json.load(open(path))
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
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((csv.reader(_f, delimiter=delim).__next__() or []))
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
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        json.dump({"output_contract_violations": violations}, _f, indent=2)
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
    path = os.path.join(outputs_dir, 'Sk_curves.csv')
    if not os.path.exists(path):
        return {'alphas': {}}
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    # group by distribution
    dist_data = {}
    for r in rows:
        dist = r['distribution'].strip()
        k = float(r['k'])
        S_val = float(r['S'])
        if k <= 0 or S_val <= 0:
            continue
        dist_data.setdefault(dist, []).append((math.log10(k), math.log10(S_val)))
    alphas = {}
    for dist, points in dist_data.items():
        if len(points) < 4:
            continue
        points.sort(key=lambda x: x[0])
        n_tail = max(5, int(len(points) * 0.2))
        tail = points[-n_tail:]
        logk = np.array([p[0] for p in tail])
        logS = np.array([p[1] for p in tail])
        slope, intercept, r, p, std_err = linregress(logk, logS)
        alphas[dist] = -slope
    return {'alphas': alphas}


# ---------------------------
#  HARD‑CODED GOLD VALUES
# ---------------------------
GOLD_ALPHA_TARGETS = {
    "1:0:0:0": {"target": 3.8, "tolerance": 0.2, "type": "range"},
    "3:3:3:1": {"constraint": "lt_3"},
    "0:1:1:0": {"constraint": "lt_3"},
    "2:0:1:0": {"constraint": "gt_3"},
}

GOLD_MEAN_N = {
    "1": 3.333333333333333,
    "2": 3.6363636363636362,
    "3": 3.75,
    "4": 3.8095238095238093,
}


# === block: score_0 (check id='compute_sk') ===
def score_0(artifact, step, ctx):
    alphas = ctx.get('alphas', {})
    if not alphas:
        return 0.0
    scores = []
    for dist, rule in GOLD_ALPHA_TARGETS.items():
        alpha = alphas.get(dist)
        if alpha is None:
            scores.append(0.0)
            continue
        if rule.get('type') == 'range':
            target = rule['target']
            tol = rule.get('tolerance', 0.0)
            if target - tol <= alpha <= target + tol:
                scores.append(1.0)
            else:
                scores.append(0.0)
        elif rule.get('constraint') == 'lt_3':
            scores.append(1.0 if alpha < 3.0 else 0.0)
        elif rule.get('constraint') == 'gt_3':
            scores.append(1.0 if alpha > 3.0 else 0.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='extract_alpha') ===
def score_1(artifact, step, ctx):
    alphas = ctx.get('alphas', {})
    if not artifact or not alphas:
        return 0.0
    tol_rel = step.get('tol_rel', 0.3)
    per_dist = []
    for row in artifact:
        dist = row['distribution'].strip()
        try:
            agent_alpha = float(row['alpha'])
        except:
            continue
        ctx_alpha = alphas.get(dist)
        if ctx_alpha is None or ctx_alpha == 0:
            continue
        rel_diff = abs(agent_alpha - ctx_alpha) / ctx_alpha
        per_dist.append(1.0 if rel_diff < tol_rel else 0.0)
    if not per_dist:
        return 0.0
    return sum(per_dist) / len(per_dist)


# === block: score_2 (check id='derive_relation') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    correct = 0
    total = 0
    for row in artifact:
        w_str = str(row['W']).strip()
        if w_str in GOLD_MEAN_N:
            try:
                val = float(row['mean_n'])
            except:
                continue
            if abs(val - GOLD_MEAN_N[w_str]) < 1e-4:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'compute_sk': score_0,
    'extract_alpha': score_1,
    'derive_relation': score_2,
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