import os
import json
import csv

# === author imports / helpers ===
import math


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
    return {}  # No special context needed; step target accessed directly in scorer


# === block: score_0 (check id='rayleigh_ritz_check') ===
def score_0(artifact, step, ctx):
    # Reads artifact (list of dicts) of the CSV.
    if artifact is None or len(artifact) == 0:
        return 0.0

    target = step.get('target', {})
    tol = target.get('tolerance', 0.05)
    gold_x = target['field_norm_X_strain']
    gold_y = target['field_norm_Y_strain']
    gold_stress = target['field_norm_X_stress']

    row6 = None
    for r in artifact:
        try:
            p = float(r.get('p_over_h', 999))
        except:
            continue
        if abs(p - 6.0) < 0.05:
            row6 = r
            break

    if row6 is None:
        return 0.0

    try:
        val_x = float(row6['field_norm_X_strain'])
        val_y = float(row6['field_norm_Y_strain'])
        val_s = float(row6['field_norm_X_stress'])
    except:
        return 0.0

    def rel_dev(val, gold):
        if gold == 0:
            return 1.0 if val != 0 else 0.0
        return abs((val - gold) / gold)

    rd_x = rel_dev(val_x, gold_x)
    rd_y = rel_dev(val_y, gold_y)
    rd_s = rel_dev(val_s, gold_stress)

    def score_rd(rd, tol, tol_max=0.2):
        if rd <= tol:
            return 1.0
        if rd >= tol_max:
            return 0.0
        return max(0.0, 1.0 - (rd - tol) / (tol_max - tol))

    sx = score_rd(rd_x, tol)
    sy = score_rd(rd_y, tol)
    ss = score_rd(rd_s, tol)
    numeric_score = (sx + sy + ss) / 3.0

    # Structural checks
    signs_ok = (val_x < 0) and (val_y > 0) and (val_s < 0)
    struct_score = (1.0 if signs_ok else 0.0) * 0.25

    ps, xs, ys, ss_vals = [], [], [], []
    for r in artifact:
        try:
            pv = float(r.get('p_over_h'))
            ps.append(pv)
            xs.append(float(r['field_norm_X_strain']))
            ys.append(float(r['field_norm_Y_strain']))
            ss_vals.append(float(r['field_norm_X_stress']))
        except:
            continue

    if len(ps) >= 10:
        def spearman(a, b):
            n = len(a)
            rank_a = [sorted(a).index(x) for x in a]
            rank_b = [sorted(b).index(x) for x in b]
            mean_ra = sum(rank_a) / n
            mean_rb = sum(rank_b) / n
            num = sum((ra - mean_ra) * (rb - mean_rb) for ra, rb in zip(rank_a, rank_b))
            den = math.sqrt(sum((ra - mean_ra)**2 for ra in rank_a) * sum((rb - mean_rb)**2 for rb in rank_b))
            if den == 0:
                return 1.0 if a == b else 0.0
            return num / den

        corr_x = spearman(ps, xs)
        corr_y = spearman(ps, ys)
        corr_s = spearman(ps, ss_vals)

        def corr_score(corr, expected_sign):
            if expected_sign * corr < 0:
                return 0.0
            abs_c = abs(corr)
            if abs_c >= 0.95:
                return 1.0
            if abs_c <= 0.7:
                return 0.0
            return (abs_c - 0.7) / (0.95 - 0.7)

        s_mx = corr_score(corr_x, -1)
        s_my = corr_score(corr_y, 1)
        s_ms = corr_score(corr_s, -1)
        monotonic_score = (s_mx + s_my + s_ms) / 3.0
        struct_score += monotonic_score * 0.75
    else:
        struct_score = 0.0

    final = 0.8 * numeric_score + 0.2 * struct_score
    return final


_SCORERS = {
    'rayleigh_ritz_check': score_0,
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
