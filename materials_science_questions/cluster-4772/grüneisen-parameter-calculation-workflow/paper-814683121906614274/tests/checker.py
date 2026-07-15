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


# === block: score_0 (check id='step_04_cte') ===
def score_0(artifact, step, ctx):
    # artifact: list of dicts with keys 'T(K)', 'a(\u00c5)', 'c(\u00c5)'
    if len(artifact) < 2:
        return 0.0
    # Convert to sorted lists
    rows = []
    for row in artifact:
        try:
            T = float(row['T(K)'])
            a = float(row['a(\u00c5)'])
            c = float(row['c(\u00c5)'])
            rows.append((T, a, c))
        except (KeyError, ValueError, TypeError):
            return 0.0
    rows.sort(key=lambda r: r[0])
    Ts = [r[0] for r in rows]
    a_vals = [r[1] for r in rows]
    c_vals = [r[2] for r in rows]

    def finite_difference_alpha(x, T):
        n = len(T)
        alphas = [0.0] * n
        if n < 2:
            return alphas
        # central difference
        for i in range(1, n-1):
            dT = T[i+1] - T[i-1]
            if dT == 0.0:
                return [0.0]*n
            alphas[i] = ((x[i+1] - x[i-1]) / dT) / x[i] if x[i] != 0.0 else 0.0
        # forward
        dT_f = T[1] - T[0]
        alphas[0] = ((x[1] - x[0]) / dT_f) / x[0] if dT_f != 0.0 and x[0] != 0.0 else 0.0
        # backward
        dT_b = T[-1] - T[-2]
        alphas[-1] = ((x[-1] - x[-2]) / dT_b) / x[-1] if dT_b != 0.0 and x[-1] != 0.0 else 0.0
        return alphas

    alpha_c = finite_difference_alpha(c_vals, Ts)
    alpha_a = finite_difference_alpha(a_vals, Ts)

    # averaging windows
    c_idx = [i for i, T in enumerate(Ts) if 0 <= T <= 42]
    a_idx_10 = [i for i, T in enumerate(Ts) if 0 <= T <= 10]
    a_idx_42 = [i for i, T in enumerate(Ts) if 0 <= T <= 42]  # same as c_idx

    if not c_idx or not a_idx_10:
        return 0.0

    def mean(vals, indices):
        return sum(vals[i] for i in indices) / len(indices)

    alpha_c_avg = mean(alpha_c, c_idx)
    alpha_a_avg_10 = mean(alpha_a, a_idx_10)
    alpha_a_avg_42 = mean(alpha_a, a_idx_42)
    alpha_V_calc = 2.0 * alpha_a_avg_42 + alpha_c_avg

    targets = step.get('targets', {})
    ref_c = targets.get('alpha_c', -1.67e-6)
    ref_a = targets.get('alpha_a', -3.0e-7)
    ref_V = targets.get('alpha_V', 3.43e-6)

    # Score alpha_c: monotonic (more negative is better)
    if alpha_c_avg < 0:
        ratio_c = alpha_c_avg / ref_c  # both negative; ratio >= 1 if more negative
        score_c = min(1.0, max(0.0, ratio_c))
    else:
        score_c = 0.0

    # Score alpha_a (0-10 K)
    if alpha_a_avg_10 < 0:
        ratio_a = alpha_a_avg_10 / ref_a
        score_a = min(1.0, max(0.0, ratio_a))
    else:
        score_a = 0.0

    # Score alpha_V: absolute relative tolerance (tol=0.5 for 50%)
    if ref_V > 0:
        rel_err = abs(alpha_V_calc - ref_V) / ref_V
        score_V = 1.0 if rel_err <= 0.5 else 0.0
    else:
        score_V = 0.0

    # Weighted sub-scores
    score_cte = 0.4 * score_c + 0.3 * score_a + 0.3 * score_V
    return float(score_cte)


# === block: score_1 (check id='step_05_gruneisen') ===
def score_1(artifact, step, ctx):
    # artifact: dict with keys 'E_u', 'E_g', 'A_2u', 'A_2g'
    targets = step.get('targets', {})
    tol = step.get('tolerance', 0.3)
    score_total = 0.0
    count = 0
    for key in ['E_u', 'E_g', 'A_2u', 'A_2g']:
        if key not in artifact:
            continue
        ref = targets.get(key)
        if ref is None:
            count += 1
            # missing target, skip but still count for average? We'll skip weighting
            continue
        val = artifact[key]
        if ref == 0.0:
            # avoid division by zero
            ok = abs(val) < 1e-9
            score = 1.0 if ok else 0.0
        else:
            rel_err = abs(val - ref) / abs(ref)
            score = 1.0 if rel_err <= tol else 0.0
        score_total += score
        count += 1
    if count == 0:
        return 0.0
    return score_total / count


_SCORERS = {
    'step_04_cte': score_0,
    'step_05_gruneisen': score_1,
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
