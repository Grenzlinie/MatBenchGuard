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


# === block: score_0 (check id='structural_crossover') ===
def score_0(artifact, step, ctx):
    import math, statistics, itertools

    # helper: linear interpolation at a list of evaluation points
    def _interp(x_eval, xp, fp):
        """xp and fp are sorted by xp; x_eval is a list."""
        n = len(xp)
        res = []
        for x in x_eval:
            if x <= xp[0]:
                res.append(fp[0])
            elif x >= xp[-1]:
                res.append(fp[-1])
            else:
                for i in range(n - 1):
                    if xp[i] <= x <= xp[i+1]:
                        t = (x - xp[i]) / (xp[i+1] - xp[i])
                        val = fp[i] + t * (fp[i+1] - fp[i])
                        res.append(val)
                        break
        return res

    # build lookup: (H0, L) -> (R_list, Tc_list)
    data_by_H0 = {}
    for row in artifact:
        L = int(row['L'])
        H0 = float(row['H0'])
        R = float(row['R'])
        Tc = float(row['Tc'])
        h0_dict = data_by_H0.setdefault(H0, {})
        lr, ltc = h0_dict.setdefault(L, ([], []))
        lr.append(R)
        ltc.append(Tc)

    # find Rc for each H0 by minimizing variance of interpolated Tc across L
    Rc_dict = {}
    for H0, h0_data in data_by_H0.items():
        if len(h0_data) < 2:
            continue
        # collect all R values across L
        all_R_set = set()
        for L, (r_list, _) in h0_data.items():
            all_R_set.update(r_list)
        R_grid = sorted(all_R_set)
        if len(R_grid) == 0:
            continue
        # interpolate each L's Tc to common grid
        interp_Tc = {}
        L_keys = []
        for L, (r_list, tc_list) in h0_data.items():
            # sort by R
            pairs = sorted(zip(r_list, tc_list))
            r_sorted = [p[0] for p in pairs]
            tc_sorted = [p[1] for p in pairs]
            interp_Tc[L] = _interp(R_grid, r_sorted, tc_sorted)
            L_keys.append(L)
        # compute variance across L at each grid point
        nL = len(L_keys)
        min_var = float('inf')
        best_R = None
        for i, R in enumerate(R_grid):
            vals = [interp_Tc[L][i] for L in L_keys]
            if len(vals) < 2:
                continue
            mean = sum(vals) / nL
            variance = sum((v - mean)**2 for v in vals) / nL
            if variance < min_var:
                min_var = variance
                best_R = R
        if best_R is not None:
            Rc_dict[H0] = best_R

    # Sub-score a: H0=0.0 accuracy
    score_a = 0.0
    if 0.0 in Rc_dict:
        gold = step['params']['H0_0_Rc_gold']
        tol = step['params']['H0_0_Rc_tolerance']
        diff = abs(Rc_dict[0.0] - gold)
        score_a = max(0.0, 1.0 - diff / tol)

    # Sub-score b: monotonic trend for each H0
    trend_scores = []
    for H0, h0_data in data_by_H0.items():
        Ls_in = sorted(h0_data.keys())
        if len(Ls_in) < 2:
            continue
        Rc = Rc_dict.get(H0)
        if Rc is None:
            continue
        # collect all R values present in this H0
        all_R = set()
        for L in Ls_in:
            all_R.update(h0_data[L][0])
        correct = 0
        total = 0
        for R in all_R:
            # collect Tc at this R for each L (use exact match)
            tc_by_L = []
            for L in Ls_in:
                r_list, tc_list = h0_data[L]
                idx = i if (i := (list(r_list).index(R) if R in r_list else None)) is not None else None
                for j, val in enumerate(r_list):
                    if val == R:
                        tc_by_L.append((L, tc_list[j]))
                        break
            if len(tc_by_L) < 2:
                continue
            tc_by_L.sort()  # sort by L
            L_vals = [t[0] for t in tc_by_L]
            Tc_vals = [t[1] for t in tc_by_L]
            flag = True
            for k in range(len(L_vals)-1):
                dL = L_vals[k+1] - L_vals[k]
                dTc = Tc_vals[k+1] - Tc_vals[k]
                if (R < Rc and dTc * dL <= 0) or (R > Rc and dTc * dL >= 0):
                    flag = False
                    break
            if flag:
                correct += 1
            total += 1
        if total > 0:
            trend_scores.append(correct / total)
    score_b = sum(trend_scores) / len(trend_scores) if trend_scores else 0.0

    # Sub-score c: slow variation between H0=0.0 and H0=0.5
    score_c = 0.0
    if 0.0 in Rc_dict and 0.5 in Rc_dict:
        diff_var = abs(Rc_dict[0.5] - Rc_dict[0.0])
        tol_var = step['params']['slow_variation_tolerance']
        score_c = max(0.0, 1.0 - diff_var / tol_var)

    final_score = 0.4 * score_a + 0.3 * score_b + 0.3 * score_c
    return float(final_score)


_SCORERS = {
    'structural_crossover': score_0,
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
