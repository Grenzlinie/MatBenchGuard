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


# === block: score_0 (check id='step_pure_isotherms') ===
def score_0(artifact, step, ctx):
    def _monotonic_score(seq, increasing=True):
        if len(seq) < 2:
            return 0.0
        violations = 0
        for i in range(1, len(seq)):
            if increasing:
                if seq[i] < seq[i-1] - 1e-6:
                    violations += 1
            else:
                if seq[i] > seq[i-1] + 1e-6:
                    violations += 1
        return max(0.0, 1.0 - violations / (len(seq)-1))

    rows = artifact
    # Gate: insufficient variation in absolute loadings
    n_abs_all = [abs(float(r['n_abs'])) for r in rows]
    if max(n_abs_all) - min(n_abs_all) < 1.0:
        return 0.0

    # Group by temperature
    temps = {}
    for r in rows:
        t = float(r['T'])
        p = float(r['P'])
        n_abs = float(r['n_abs'])
        n_ex = float(r['n_ex'])
        temps.setdefault(t, []).append((p, n_abs, n_ex))

    sub_scores = []

    for t, pts in temps.items():
        pts.sort(key=lambda x: x[0])
        ps = [p for p,_,_ in pts]
        nas = [na for _,na,_ in pts]
        nes = [ne for _,_,ne in pts]

        # 1. monotonic absolute loading
        sub_scores.append(_monotonic_score(nas, True))

        # 2. plateau: highest pressure absolute loading near maximum
        max_na = max(nas)
        if max_na > 0:
            ratio = nas[-1] / max_na
            if ratio >= 0.95:
                sub_scores.append(1.0)
            else:
                sub_scores.append(ratio)
        else:
            sub_scores.append(0.0)

        # 3. excess isotherm shape: peak with decline after it
        if len(nes) >= 3:
            max_ne = max(nes)
            if max_ne > 0:
                max_idx = nes.index(max_ne)
                after_peak = nes[max_idx+1:]
                if after_peak:
                    decline_ratio = after_peak[-1] / max_ne
                    if decline_ratio < 0.7:
                        decline_score = 1.0
                    elif decline_ratio < 0.9:
                        decline_score = 0.5
                    else:
                        decline_score = 0.0
                    sub_scores.append(decline_score)
                else:
                    sub_scores.append(0.5)
            else:
                sub_scores.append(0.0)
        else:
            sub_scores.append(0.5)

        # 4. saturation loading within a wide acceptable range
        if 2.5 <= max_na <= 4.5:
            sub_scores.append(1.0)
        else:
            sub_scores.append(0.5)

    # Temperature ordering: colder temperature should yield higher loading at the same pressure
    if len(temps) >= 2:
        temps_sorted = sorted(temps.keys())
        order_violations = 0
        total_pairs = 0
        for i in range(len(temps_sorted)-1):
            colder = temps_sorted[i]
            warmer = temps_sorted[i+1]
            colder_dict = {p:na for p,na,_ in temps[colder]}
            warmer_dict = {p:na for p,na,_ in temps[warmer]}
            common_p = set(colder_dict.keys()) & set(warmer_dict.keys())
            for p in common_p:
                total_pairs += 1
                if colder_dict[p] < warmer_dict[p] + 0.05:
                    order_violations += 1
        if total_pairs > 0:
            sub_scores.append(max(0.0, 1.0 - order_violations / total_pairs))
        else:
            sub_scores.append(0.5)
    else:
        sub_scores.append(0.5)

    if not sub_scores:
        return 1.0
    return sum(sub_scores) / len(sub_scores)


# === block: score_1 (check id='step_pure_qst') ===
def score_1(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    target = params['target_zero_qst']
    tol = params['tolerance_abs']

    # zero‑loading Qst check
    # take the point with smallest n_abs
    if len(rows) == 0:
        return 0.0
    min_n = None
    qst_at_min = None
    for r in rows:
        na = float(r['n_abs'])
        q = float(r['Qst'])
        if min_n is None or na < min_n:
            min_n = na
            qst_at_min = q
    # tolerance check, full credit if within tol
    qst_score = 0.0
    if qst_at_min is not None:
        if abs(qst_at_min - target) <= tol:
            qst_score = 1.0
        else:
            qst_score = max(0.0, 1.0 - (abs(qst_at_min - target) - tol) / (2*tol))

    # trend: increasing then decreasing
    if params.get('qst_trend_check', False):
        qst_vals = [float(r['Qst']) for r in rows]
        n_abs_vals = [float(r['n_abs']) for r in rows]
        # sort by n_abs
        sorted_pairs = sorted(zip(n_abs_vals, qst_vals))
        qst_vals = [q for _,q in sorted_pairs]
        has_peak = False
        for i in range(1, len(qst_vals)-1):
            if qst_vals[i] > qst_vals[i-1] and qst_vals[i] > qst_vals[i+1]:
                has_peak = True
                break
        trend_score = 1.0 if has_peak else 0.0
    else:
        trend_score = 1.0

    return qst_score * 0.7 + trend_score * 0.3


# === block: score_2 (check id='step_mixture_isotherms') ===
def score_2(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    temps = {}
    for r in rows:
        t = float(r['T'])
        p = float(r['P'])
        nb = float(r['n_benzene'])
        nc = float(r['n_CO2'])
        temps.setdefault(t, []).append((p, nb, nc))

    scores = []
    # monotonicity for benzene (decreasing) and CO2 (increasing)
    for t, pts in temps.items():
        pts.sort(key=lambda x: x[0])
        nbs = [nb for _,nb,_ in pts]
        ncs = [nc for _,_,nc in pts]
        # benzene decreasing
        dec_score = 1.0
        for i in range(1, len(nbs)):
            if nbs[i] >= nbs[i-1] * 0.995:  # allow small numerical noise
                dec_score -= 0.2
        dec_score = max(0.0, dec_score)
        # CO2 increasing
        inc_score = 1.0
        for i in range(1, len(ncs)):
            if ncs[i] <= ncs[i-1] * 1.005:
                inc_score -= 0.2
        inc_score = max(0.0, inc_score)
        scores.append(dec_score)
        scores.append(inc_score)

    # positivity
    all_pos = True
    for r in rows:
        if float(r['n_benzene']) < 0 or float(r['n_CO2']) < 0:
            all_pos = False
    scores.append(1.0 if all_pos else 0.0)

    if not scores:
        return 1.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='step_md_diffusion') ===
def score_3(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    d_min = params['d_min']
    d_max = params['d_max']
    ref_d = params['reference_pure_d']

    pts = []
    for r in rows:
        p = float(r['P'])
        d = float(r['D_CO2'])
        pts.append((p, d))
    pts.sort(key=lambda x: x[0])
    p_vals = [p for p,_ in pts]
    d_vals = [d for _,d in pts]

    scores = []
    # range check
    all_in_range = all(d_min <= d <= d_max for d in d_vals)
    scores.append(1.0 if all_in_range else 0.0)

    # at least 10x lower than pure CO2 D
    lower_than_ref = all(d < ref_d for d in d_vals)
    scores.append(1.0 if lower_than_ref else 0.5)

    # increasing trend
    trend_ok = True
    for i in range(1, len(d_vals)):
        if d_vals[i] < d_vals[i-1] * 0.99:
            trend_ok = False
    scores.append(1.0 if trend_ok else 0.0)

    if not scores:
        return 1.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_pure_isotherms': score_0,
    'step_pure_qst': score_1,
    'step_mixture_isotherms': score_2,
    'step_md_diffusion': score_3,
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
