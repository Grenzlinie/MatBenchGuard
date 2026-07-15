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


# === block: score_0 (check id='cp_trend_al_monotonic') ===
def score_0(artifact, step, ctx):
    # Filter Al rows and sort by T_Tm descending (supercooled direction).
    al_rows = [r for r in artifact if r.get('system', '').strip() == 'Al']
    if len(al_rows) < 3:
        return 0.0

    try:
        parsed = [(float(r['T_Tm']), float(r['Cp_kB'])) for r in al_rows]
    except (ValueError, KeyError, TypeError):
        return 0.0

    parsed.sort(key=lambda x: x[0], reverse=True)  # high T first
    cp_vals = [v[1] for v in parsed]
    n_pairs = len(cp_vals) - 1

    # 1. Monotonicity: non-decreasing with tolerance 0.05
    violations = 0
    for i in range(1, len(cp_vals)):
        if cp_vals[i] < cp_vals[i-1] - 0.05:
            violations += 1
    mono_score = max(0.0, 1.0 - violations / n_pairs) if n_pairs > 0 else 0.0

    # 2. Meaningful overall increase from high T to low T
    overall_increase = cp_vals[-1] - cp_vals[0]
    inc_score = min(1.0, max(0.0, overall_increase / 0.3))

    # 3. Physical sanity: Cp in [0.5, 8.0]
    n_ok = sum(1 for v in cp_vals if 0.5 <= v <= 8.0)
    sanity_score = n_ok / len(cp_vals) if len(cp_vals) > 0 else 0.0

    return 0.7 * mono_score + 0.15 * inc_score + 0.15 * sanity_score


# === block: score_1 (check id='cp_trend_rb_nonmonotonic') ===
def score_1(artifact, step, ctx):
    # Filter Rb rows and sort by T_Tm ascending.
    rb_rows = [r for r in artifact if r.get('system', '').strip() == 'Rb']
    if len(rb_rows) < 5:
        return 0.0

    try:
        parsed = [(float(r['T_Tm']), float(r['Cp_kB'])) for r in rb_rows]
    except (ValueError, KeyError, TypeError):
        return 0.0

    parsed.sort(key=lambda x: x[0])  # ascending T
    T = [v[0] for v in parsed]
    Cp = [v[1] for v in parsed]

    # Find global minimum
    min_idx = min(range(len(Cp)), key=lambda i: Cp[i])
    min_T = T[min_idx]
    min_Cp = Cp[min_idx]

    # 1. Minimum T_Tm in [0.45, 0.85] (paper says ~0.65; allow ±0.2 window)
    loc_score = 1.0 if 0.45 <= min_T <= 0.85 else 0.0

    # 2. Highest-T Cp > minimum Cp (decrease from Tm)
    hi_gt_score = 1.0 if Cp[-1] > min_Cp + 0.05 else 0.0

    # 3. Lowest-T Cp > minimum Cp (rise near Tg)
    lo_gt_score = 1.0 if Cp[0] > min_Cp + 0.05 else 0.0

    # 4. Left side (T < min_T): Cp decreasing as T increases toward min
    left_decr = True
    for i in range(1, min_idx + 1):
        if Cp[i] > Cp[i-1] + 0.1:
            left_decr = False
            break
    left_score = 1.0 if left_decr else 0.0

    # 5. Right side (T > min_T): Cp increasing as T increases from min
    right_incr = True
    for i in range(min_idx + 1, len(Cp)):
        if Cp[i] < Cp[i-1] - 0.1:
            right_incr = False
            break
    right_score = 1.0 if right_incr else 0.0

    # 6. Physical sanity
    n_ok = sum(1 for v in Cp if 0.5 <= v <= 8.0)
    sanity_score = n_ok / len(Cp) if len(Cp) > 0 else 0.0

    return 0.35 * loc_score + 0.15 * hi_gt_score + 0.15 * lo_gt_score + 0.15 * left_score + 0.15 * right_score + 0.05 * sanity_score


_SCORERS = {
    'cp_trend_al_monotonic': score_0,
    'cp_trend_rb_nonmonotonic': score_1,
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
