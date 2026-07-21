import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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


# === block: score_0 (check id='step_02_reaction_kinetics') ===
def score_0(artifact, step, ctx):
    ref_curves = step['target_value']['reference_curves']

    def interp(x, xs, ys):
        if x <= xs[0]: return ys[0]
        if x >= xs[-1]: return ys[-1]
        i = 0
        while i < len(xs)-1 and xs[i+1] < x:
            i += 1
        if i == len(xs)-1: return ys[-1]
        t = (x - xs[i]) / (xs[i+1] - xs[i])
        return ys[i] + t * (ys[i+1] - ys[i])

    def rankdata(a):
        n = len(a)
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(a))
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j < n and sorted_pairs[j][0] == sorted_pairs[i][0]:
                j += 1
            avg_rank = (i + j + 1) / 2.0  # 1‑based average
            for k in range(i, j):
                ranks[sorted_pairs[k][1]] = avg_rank
            i = j
        return ranks

    def spearmanr(x, y):
        n = len(x)
        if n <= 1:
            return 0.0
        rx = rankdata(x)
        ry = rankdata(y)
        mean_x = sum(rx) / n
        mean_y = sum(ry) / n
        num = sum((rx[i] - mean_x) * (ry[i] - mean_y) for i in range(n))
        denom_x = math.sqrt(sum((rx[i] - mean_x) ** 2 for i in range(n)))
        denom_y = math.sqrt(sum((ry[i] - mean_y) ** 2 for i in range(n)))
        if denom_x == 0.0 or denom_y == 0.0:
            return 0.0
        return num / (denom_x * denom_y)

    agent = {}
    for row in artifact:
        cond = row.get('condition', '').strip()
        agent.setdefault(cond, []).append(row)

    conditions = ['flat', 'rough_T500_spillover', 'rough_T500_no_spillover']
    tol_window = 0.05
    tol_peak = 0.05

    scores = []
    for cond in conditions:
        rows = agent.get(cond, [])
        if not rows:
            scores.append(0.0)
            continue
        rows.sort(key=lambda r: float(r['YA']))
        ya_a = [float(r['YA']) for r in rows]
        aA = [float(r['theta_A']) for r in rows]
        aB = [float(r['theta_B']) for r in rows]
        aR = [float(r['reaction_rate']) for r in rows]
        ref = ref_curves[cond]
        rYA = ref['YA']
        rA = ref['theta_A']
        rB = ref['theta_B']
        rR = ref['reaction_rate']

        fine_ya = [i / 100.0 for i in range(101)]
        aAf = [interp(y, ya_a, aA) for y in fine_ya]
        aBf = [interp(y, ya_a, aB) for y in fine_ya]
        aRf = [interp(y, ya_a, aR) for y in fine_ya]
        rAf = [interp(y, rYA, rA) for y in fine_ya]
        rBf = [interp(y, rYA, rB) for y in fine_ya]
        rRf = [interp(y, rYA, rR) for y in fine_ya]

        corrA = max(0.0, spearmanr(aAf, rAf))
        corrB = max(0.0, spearmanr(aBf, rBf))

        ref_indices = [i for i, val in enumerate(rRf) if val > 1e-6]
        if not ref_indices:
            r_start = r_end = r_peak = 0.0
        else:
            r_start = fine_ya[ref_indices[0]]
            r_end = fine_ya[ref_indices[-1]]
            peak_idx = ref_indices[max(range(len(ref_indices)), key=lambda i: rRf[ref_indices[i]])]
            r_peak = fine_ya[peak_idx]

        a_indices = [i for i, val in enumerate(aRf) if val > 1e-6]
        if not a_indices:
            rate_score = 0.0
        else:
            a_start = fine_ya[a_indices[0]]
            a_end = fine_ya[a_indices[-1]]
            a_peak_idx = a_indices[max(range(len(a_indices)), key=lambda i: aRf[a_indices[i]])]
            a_peak = fine_ya[a_peak_idx]

            def lin_score(diff, tol):
                return max(0.0, 1.0 - diff / tol)

            score_start = lin_score(abs(a_start - r_start), tol_window)
            score_end = lin_score(abs(a_end - r_end), tol_window)
            score_peak = lin_score(abs(a_peak - r_peak), tol_peak)
            window_score = (score_start + score_end) / 2.0
            rate_score = 0.5 * window_score + 0.5 * score_peak

        cond_score = (corrA + corrB + rate_score) / 3.0
        scores.append(cond_score)

    return sum(scores) / len(scores)


# === block: score_1 (check id='step_03_no_spillover_shape') ===
def score_1(artifact, step, ctx):
    total = 0
    heights = []
    for row in artifact:
        h = int(row['height'])
        total += h
        heights.append(h)
    if total != 4410:
        return 0.0

    nonzero = [h for h in heights if h > 0]
    n = len(nonzero)
    if n == 0:
        return 0.0
    mean_h = sum(nonzero) / n
    var = sum((h - mean_h)**2 for h in nonzero) / n
    std_dev = math.sqrt(var)

    score = 0.0
    if mean_h >= 10.5:
        score += 0.4
    if std_dev >= 2.0:
        score += 0.6
    return score


_SCORERS = {
    'step_02_reaction_kinetics': score_0,
    'step_03_no_spillover_shape': score_1,
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
