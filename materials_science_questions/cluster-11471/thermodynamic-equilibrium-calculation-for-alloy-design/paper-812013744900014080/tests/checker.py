import os
import json
import csv

# === author imports / helpers ===
import csv, math, statistics


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


# === block: score_0 (check id='compute_gamma_c') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        T_list = step['grid_A_T']
        Cr_list = step['grid_A_Cr']
        Ni_fixed = step['grid_A_Ni']
        T_B = step['grid_B_T']
        Cr_B_list = step['grid_B_Cr']
        Ni_B_list = step['grid_B_Ni']
        cr_tol = step['cr_monotonic_tol']
        ni_tol = step['ni_monotonic_tol']
        uc_Cr_low = step['unit_activity_Cr_low']
        uc_Cr_high = step['unit_activity_Cr_high']
        uc_Ni = step['unit_activity_Ni']
        uc_gamma_low = step['unit_activity_gamma_low_threshold']
        uc_gamma_high = step['unit_activity_gamma_high_threshold']
        uc_std_thresh = step['unit_activity_temp_indep_std_threshold']
        w_comp = step['completeness_weight']
        w_cr = step['cr_mono_weight']
        w_ni = step['ni_mono_weight']
        w_ua = step['unit_activity_weight']

        # Build lookup
        g_dict = {}
        for row in artifact:
            try:
                t = float(row['T_C'])
                cr = float(row['Cr_wt'])
                ni = float(row['Ni_wt'])
                gc = float(row['gamma_C'])
                g_dict[(round(t,2), round(cr,2), round(ni,2))] = gc
            except: pass

        # Completeness
        req_A = [(t,c,Ni_fixed) for t in T_list for c in Cr_list]
        req_B = [(T_B,c,n) for c in Cr_B_list for n in Ni_B_list]
        found_A = sum(1 for key in req_A if key in g_dict)
        found_B = sum(1 for key in req_B if key in g_dict)
        completeness = (found_A + found_B) / (len(req_A) + len(req_B)) if (len(req_A) + len(req_B))>0 else 0.0

        # Cr monotonicity (decreasing)
        cr_pairs_ok = 0
        cr_pairs_total = 0
        for T in T_list:
            cr_vals = []
            for c in sorted(Cr_list):
                key = (round(T,2), round(c,2), round(Ni_fixed,2))
                if key in g_dict:
                    cr_vals.append((c, g_dict[key]))
            if len(cr_vals) < 2: continue
            for i in range(1, len(cr_vals)):
                cr_pairs_total += 1
                if cr_vals[i][1] <= cr_vals[i-1][1] + cr_tol:
                    cr_pairs_ok += 1
        cr_mono_score = cr_pairs_ok / cr_pairs_total if cr_pairs_total > 0 else 0.0

        # Ni monotonicity (increasing)
        ni_pairs_ok = 0
        ni_pairs_total = 0
        for Cr_val in Cr_B_list:
            ni_vals = []
            for n in sorted(Ni_B_list):
                key = (round(T_B,2), round(Cr_val,2), round(n,2))
                if key in g_dict:
                    ni_vals.append((n, g_dict[key]))
            if len(ni_vals) < 2: continue
            for i in range(1, len(ni_vals)):
                ni_pairs_total += 1
                if ni_vals[i][1] >= ni_vals[i-1][1] - ni_tol:
                    ni_pairs_ok += 1
        ni_mono_score = ni_pairs_ok / ni_pairs_total if ni_pairs_total > 0 else 0.0

        # Unit activity point check
        gamma_low = []
        gamma_high = []
        for T in T_list:
            key_low = (round(T,2), round(uc_Cr_low,2), round(uc_Ni,2))
            key_high = (round(T,2), round(uc_Cr_high,2), round(uc_Ni,2))
            if key_low in g_dict and key_high in g_dict:
                gamma_low.append(g_dict[key_low])
                gamma_high.append(g_dict[key_high])
        n_pts = len(gamma_low)
        if n_pts == 0:
            bracket_score = 0.0
            temp_score = 0.0
        else:
            bracket_ok = 0
            for gl, gh in zip(gamma_low, gamma_high):
                if gl >= uc_gamma_low and gh <= uc_gamma_high:
                    bracket_ok += 1
            bracket_score = bracket_ok / n_pts
            # Temperature independence: std of gamma_low and gamma_high
            std_low = statistics.pstdev(gamma_low) if n_pts > 1 else 0.0
            std_high = statistics.pstdev(gamma_high) if n_pts > 1 else 0.0
            avg_std = (std_low + std_high) / 2
            temp_score = max(0.0, 1.0 - avg_std / uc_std_thresh)
        unit_score = 0.5 * bracket_score + 0.5 * temp_score

        final = w_comp * completeness + w_cr * cr_mono_score + w_ni * ni_mono_score + w_ua * unit_score
        return max(0.0, min(1.0, final))


_SCORERS = {
    'compute_gamma_c': score_0,
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
