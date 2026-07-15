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
    cooling_order = ["gamma1", "gamma2", "gamma3", "gamma4", "gamma5", "gamma6"]
    return {"cooling_order": cooling_order}


# === block: score_0 (check id='verify_trends') ===
def score_0(artifact, step, ctx):
    cooling_order = ctx["cooling_order"]
    # artifact is list of dicts with keys cooling_rate, T, pair_index, fraction
    rows_by_pair = {}
    for row in artifact:
        pid = row["pair_index"]
        rows_by_pair.setdefault(pid, []).append(row)

    def rank_values(vals):
        # compute ranks (average of ties)
        sorted_vals = sorted((v,i) for i,v in enumerate(vals))
        ranks = [0]*len(vals)
        n = len(vals)
        i = 0
        while i < n:
            j = i
            while j < n and sorted_vals[j][0] == sorted_vals[i][0]:
                j += 1
            avg_rank = (i + j + 1)/2.0
            for k in range(i, j):
                ranks[sorted_vals[k][1]] = avg_rank
            i = j
        return ranks

    def spearman(x, y):
        n = len(x)
        if n < 2:
            return 0.0
        rx = rank_values(x)
        ry = rank_values(y)
        d2 = sum((rx[i]-ry[i])**2 for i in range(n))
        return 1.0 - 6.0*d2/(n*(n*n-1))

    def score_pair_type(pair_index, target_trend, tol_adj=0.5, ratio_lim=0.03, rho_abs_lim=0.5):
        # get fractions ordered by cooling_rate
        pair_rows = rows_by_pair.get(pair_index, [])
        if len(pair_rows) != 6:
            return 0.0
        # sort by cooling_order index
        idx_map = {cr: i for i, cr in enumerate(cooling_order)}
        try:
            sorted_rows = sorted(pair_rows, key=lambda r: idx_map[r["cooling_rate"]])
        except KeyError:
            return 0.0
        fracs = [float(r["fraction"]) for r in sorted_rows]
    
        if target_trend == "decrease":
            # check adjacent non-increasing (diff >= -tol_adj)
            ok = all(fracs[i] - fracs[i+1] >= -tol_adj for i in range(len(fracs)-1))
            if ok:
                return 1.0
            # fallback: Spearman with cooling order (ordinal 0..5)
            rho = spearman(list(range(6)), fracs)
            if rho <= -0.9:
                return 0.7
            elif rho <= -0.8:
                return 0.5
            else:
                return 0.0
        elif target_trend == "increase":
            ok = all(fracs[i+1] - fracs[i] >= -tol_adj for i in range(len(fracs)-1))
            if ok:
                return 1.0
            rho = spearman(list(range(6)), fracs)
            if rho >= 0.9:
                return 0.7
            elif rho >= 0.8:
                return 0.5
            else:
                return 0.0
        elif target_trend == "independent":
            max_v = max(fracs)
            min_v = min(fracs)
            mean_v = sum(fracs)/len(fracs)
            ratio = (max_v - min_v) / mean_v if mean_v != 0 else 1.0
            rho = spearman(list(range(6)), fracs)
            if ratio <= ratio_lim and abs(rho) < rho_abs_lim:
                return 1.0
            elif ratio <= 2*ratio_lim and abs(rho) < 0.6:
                return 0.5
            else:
                return 0.0
        else:
            return 0.0

    score_1551 = score_pair_type("1551", "decrease")
    score_1422 = score_pair_type("1422", "increase")
    score_1541 = score_pair_type("1541", "independent")
    score_1431 = score_pair_type("1431", "independent")
    score_1421 = score_pair_type("1421", "independent")
    total = (score_1551 + score_1422 + score_1541 + score_1431 + score_1421) / 5.0
    return total


_SCORERS = {
    'verify_trends': score_0,
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
