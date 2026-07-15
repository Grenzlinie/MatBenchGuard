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


# === block: score_0 (check id='shape_and_completeness') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        min_rows = step.get('config', {}).get('min_rows', 800)
        req_cols = step.get('config', {}).get('required_columns', [])
        if not isinstance(artifact, list) or len(artifact) < min_rows:
            return 0.0
        for row in artifact:
            for col in req_cols:
                val = row.get(col)
                if val is None or val == '':
                    return 0.0
                try:
                    float(val)
                except (ValueError, TypeError):
                    return 0.0
        return 1.0


# === block: score_1 (check id='physical_checks') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        cfg = step.get('config', {})
        expected_Tc = cfg['expected_Tc']
        tc_tol = cfg['tc_tolerance_K']
        gap_thresh = cfg['gap_threshold_zero']
        ns_norm_k22 = cfg['ns_normalization_k22']
        ns_norm_tol = cfg['ns_normalization_tolerance']
        ns_norm_T = cfg['ns_normalization_T']
        rc = cfg['reentrance_check']
        data = {}
        for row in artifact:
            try:
                k22 = float(row['k22'])
                beta = int(float(row['beta']))
                T = float(row['T'])
                d1 = float(row['Delta1'])
                d2 = float(row['Delta2'])
                ns = float(row['ns'])
                key = (k22, beta)
                if key not in data:
                    data[key] = []
                data[key].append((T, d1, d2, ns))
            except:
                continue
        tc_scores = []
        for key, pts in data.items():
            pts_sorted = sorted(pts, key=lambda x: x[0])
            Tc = None
            for i in range(len(pts_sorted)-1, -1, -1):
                T, d1, d2, _ = pts_sorted[i]
                if d1 > gap_thresh or d2 > gap_thresh:
                    Tc = T
                    break
            if Tc is None:
                tc_scores.append(0.0)
            else:
                diff = abs(Tc - expected_Tc)
                if diff <= tc_tol:
                    tc_scores.append(1.0)
                elif diff <= 2 * tc_tol:
                    tc_scores.append(0.5)
                else:
                    tc_scores.append(0.0)
        tc_avg = sum(tc_scores) / len(tc_scores) if tc_scores else 0.0
        ns_norm_score = 0.0
        lookup_key = (ns_norm_k22, 1)
        if lookup_key in data:
            pts_norm = data[lookup_key]
            best = min(pts_norm, key=lambda p: abs(p[0] - ns_norm_T))
            ns_val = best[3]
            if abs(ns_val - 1.0) <= ns_norm_tol:
                ns_norm_score = 1.0
        rc_score = 0.0
        rc_key = (rc['k22'], rc['beta'])
        if rc_key in data:
            pts_rc = sorted(data[rc_key], key=lambda x: x[0])
            def ns_at(T_target):
                best_pt = min(pts_rc, key=lambda p: abs(p[0] - T_target))
                return best_pt[3]
            ns_low = ns_at(rc['T_low'])
            ns_mid = ns_at(rc['T_mid'])
            ns_high = ns_at(rc['T_high'])
            if ns_low >= rc['ns_low_min'] and ns_mid <= rc['ns_mid_max'] and ns_high >= rc['ns_high_min']:
                rc_score = 1.0
        sub_scores = [tc_avg, ns_norm_score, rc_score]
        return sum(sub_scores) / len(sub_scores)


# === block: score_2 (check id='plausible_ranges') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        cfg = step.get('config', {})
        d_min = cfg['Delta_min']
        d_max = cfg['Delta_max']
        ns_min = cfg['ns_min']
        ns_max = cfg['ns_max']
        total = 0
        ok = 0
        for row in artifact:
            try:
                d1 = float(row['Delta1'])
                d2 = float(row['Delta2'])
                ns = float(row['ns'])
                if d_min <= d1 <= d_max and d_min <= d2 <= d_max and ns_min <= ns <= ns_max:
                    ok += 1
                total += 1
            except:
                pass
        if total == 0:
            return 0.0
        return ok / total


_SCORERS = {
    'shape_and_completeness': score_0,
    'physical_checks': score_1,
    'plausible_ranges': score_2,
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
