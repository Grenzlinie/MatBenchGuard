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
    return {}


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    params = step.get("params", {})
    tol = step.get("tolerance_rel", 1e-3)

    def compute_eps(row, B, K, mu, f):
        d_mm = float(row["d_mm"])
        R = float(row["R"])
        d = d_mm * 1e-3
        term = math.sqrt(1 + mu**2) - mu - R * (mu + math.sqrt(1 + mu**2))
        if term <= 0:
            return None
        return (B * K**3) / (f * d**1.5 * term)

    row_scores = []
    rows_minus10_fresh = []
    rows_minus10_saline = []
    rows_minus40 = []
    for row in artifact:
        try:
            mat = row["material"].strip().lower()
            temp = float(row["temperature_C"])
            eps = float(row["epsilon_t_1_per_s"])
        except (KeyError, ValueError):
            return 0.0
        if temp == -10.0:
            if mat == "fresh":
                B = params["fresh_minus10"]["B"]
                K = params["fresh_minus10"]["K_Ic"]
                mu = params["fresh_minus10"]["mu"]
                f = params["fresh_minus10"]["f"]
            elif mat == "saline":
                B = params["saline_minus10"]["B"]
                K = params["saline_minus10"]["K_Ic"]
                mu = params["saline_minus10"]["mu"]
                f = params["saline_minus10"]["f"]
            else:
                continue
            exp = compute_eps(row, B, K, mu, f)
            if exp is None:
                row_scores.append(0.0)
                continue
            if exp == 0:
                ok = abs(eps) < 1e-20
            else:
                ok = abs(eps - exp) <= tol * max(exp, 1e-20)
            row_scores.append(1.0 if ok else 0.0)
            if mat == "fresh":
                rows_minus10_fresh.append(row)
            else:
                rows_minus10_saline.append(row)
        elif temp == -40.0 and mat == "fresh":
            # Only structural checks, no numeric comparison because B unknown
            rows_minus40.append(row)
        else:
            # unexpected condition, ignore
            pass

    if row_scores:
        numeric_score = sum(row_scores) / len(row_scores)
    else:
        numeric_score = 1.0  # no -10°C rows, but that's unlikely

    trend_score = 1.0
    checks = 0
    satisfied = 0

    # Helper to group by material/temp
    from collections import defaultdict

    def monotonic_decrease_with_d(rows):
        # returns 1 if eps decreases as d increases for each R
        by_R = defaultdict(list)
        for r in rows:
            by_R[float(r["R"])].append((float(r["d_mm"]), float(r["epsilon_t_1_per_s"])))
        ok = True
        for R_val, vals in by_R.items():
            vals.sort(key=lambda x: x[0])
            for i in range(len(vals)-1):
                if vals[i][1] < vals[i+1][1] - 1e-20:
                    ok = False
                    break
        return 1.0 if ok else 0.0

    def monotonic_increase_with_R(rows):
        by_d = defaultdict(list)
        for r in rows:
            by_d[float(r["d_mm"])].append((float(r["R"]), float(r["epsilon_t_1_per_s"])))
        ok = True
        for d_val, vals in by_d.items():
            vals.sort(key=lambda x: x[0])
            for i in range(len(vals)-1):
                if vals[i][1] > vals[i+1][1] + 1e-20:
                    ok = False
                    break
        return 1.0 if ok else 0.0

    # d scaling check for -10°C groups
    if rows_minus10_fresh:
        checks += 1
        satisfied += monotonic_decrease_with_d(rows_minus10_fresh)
    if rows_minus10_saline:
        checks += 1
        satisfied += monotonic_decrease_with_d(rows_minus10_saline)

    # R scaling check
    if rows_minus10_fresh:
        checks += 1
        satisfied += monotonic_increase_with_R(rows_minus10_fresh)
    if rows_minus10_saline:
        checks += 1
        satisfied += monotonic_increase_with_R(rows_minus10_saline)

    # Saline/fresh factor >=5 for same d,R at -10°C
    # build dictionary keyed by (d,R) for each
    fresh_dict = {}
    for r in rows_minus10_fresh:
        key = (float(r["d_mm"]), float(r["R"]))
        fresh_dict[key] = float(r["epsilon_t_1_per_s"])
    saline_dict = {}
    for r in rows_minus10_saline:
        key = (float(r["d_mm"]), float(r["R"]))
        saline_dict[key] = float(r["epsilon_t_1_per_s"])
    common_keys = set(fresh_dict.keys()) & set(saline_dict.keys())
    if common_keys:
        checks += 1
        ok_saline = True
        for k in common_keys:
            if saline_dict[k] < 5.0 * fresh_dict[k] - 1e-20:
                ok_saline = False
                break
        satisfied += (1.0 if ok_saline else 0.0)

    # -40°C ratio < 0.1 relative to -10°C fresh for same d,R
    if rows_minus40 and rows_minus10_fresh:
        fresh_minus10_dict = {}
        for r in rows_minus10_fresh:
            key = (float(r["d_mm"]), float(r["R"]))
            fresh_minus10_dict[key] = float(r["epsilon_t_1_per_s"])
        checks += 1
        ok_temp = True
        for r in rows_minus40:
            key = (float(r["d_mm"]), float(r["R"]))
            if key in fresh_minus10_dict:
                ratio = float(r["epsilon_t_1_per_s"]) / fresh_minus10_dict[key]
                if ratio > 0.1 + 1e-20:
                    ok_temp = False
                    break
            # if missing comparison, skip
        satisfied += (1.0 if ok_temp else 0.0)

    if checks > 0:
        trend_score = satisfied / checks
    else:
        trend_score = 1.0

    # Also check that -40°C eps are positive (implicit in ratio check) but do explicit:
    if rows_minus40:
        all_pos = all(float(r["epsilon_t_1_per_s"]) > 0 for r in rows_minus40)
        if not all_pos:
            trend_score = 0.0

    final = 0.6 * numeric_score + 0.4 * trend_score
    return min(max(final, 0.0), 1.0)


_SCORERS = {
    'step01': score_0,
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
