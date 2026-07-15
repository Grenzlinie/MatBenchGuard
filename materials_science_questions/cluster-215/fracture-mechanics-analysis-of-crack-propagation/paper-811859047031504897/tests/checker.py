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


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
        rows = artifact
        floors = []
        for r in rows:
            try:
                floor = int(r['floor'])
                td = float(r['total_displacement_mm'])
                ed = float(r['effective_deflection_mm'])
                floors.append((floor, td, ed))
            except:
                continue
        floors.sort(key=lambda x: x[0])
        eff1 = None
        for f in floors:
            if f[0] == 1:
                eff1 = f[2]
        if eff1 is None:
            return 0.0
        target = 1.3
        tol = 0.3
        diff = abs(eff1 - target)
        if diff <= tol:
            score_def = 1.0
        else:
            score_def = max(0.0, 1.0 - (diff - tol) / tol)
        total_seq = [f[1] for f in floors]
        inc = all(total_seq[i] < total_seq[i+1] for i in range(len(total_seq)-1))
        nondec = all(total_seq[i] <= total_seq[i+1] for i in range(len(total_seq)-1))
        score_mono = 1.0 if inc else (0.5 if nondec else 0.0)
        return 0.6 * score_def + 0.4 * score_mono


# === block: score_1 (check id='step3') ===
def score_1(artifact, step, ctx):
        rows = artifact
        from collections import defaultdict
        expected_lambdas = {89,133,178,200,300,400,800,1200,1600}
        groups = defaultdict(list)
        for r in rows:
            try:
                lc = float(r['lambda_ch_mm'])
                u = float(r['u_mm'])
                w = float(r['w_max_mm'])
                groups[lc].append((u, w))
            except:
                continue
        def lin_slope(x, y):
            n = len(x)
            if n < 2:
                return None
            xm = sum(x)/n
            ym = sum(y)/n
            num = sum((xi-xm)*(yi-ym) for xi,yi in zip(x,y))
            den = sum((xi-xm)**2 for xi in x)
            if den == 0:
                return None
            return num/den
        TARGET_LOW = 0.52
        TARGET_HIGH = 0.78
        TOL = 0.10
        group_scores = []
        for lc in expected_lambdas:
            points = groups.get(lc, [])
            if not points:
                group_scores.append(0.0)
                continue
            points.sort(key=lambda p: p[0])
            u_vals = [p[0] for p in points]
            w_vals = [p[1] for p in points]
            start = -1
            for i, w in enumerate(w_vals):
                if w > 1e-6:
                    start = i
                    break
            if start == -1:
                group_scores.append(0.0)
                continue
            u_post = u_vals[start:]
            w_post = w_vals[start:]
            if lc < 400:
                slope = lin_slope(u_post, w_post)
                if slope is None:
                    group_scores.append(0.0)
                else:
                    dif = abs(slope - TARGET_LOW)
                    score = max(0.0, 1.0 - dif / TOL)
                    group_scores.append(score)
            else:
                jump_idx = None
                for i in range(1, len(w_post)):
                    if w_post[i] > 2 * w_post[i-1] and w_post[i-1] > 1e-6:
                        jump_idx = i
                        break
                if jump_idx is not None:
                    u_after = u_post[jump_idx:]
                    w_after = w_post[jump_idx:]
                    slope = lin_slope(u_after, w_after)
                    if slope is None:
                        group_scores.append(0.0)
                    else:
                        dif = abs(slope - TARGET_HIGH)
                        score = max(0.0, 1.0 - dif / TOL)
                        group_scores.append(score)
                else:
                    slope = lin_slope(u_post, w_post)
                    if slope is None:
                        group_scores.append(0.0)
                    else:
                        dif = abs(slope - TARGET_LOW)
                        score = max(0.0, 1.0 - dif / TOL)
                        group_scores.append(score)
        if not group_scores:
            return 0.0
        return sum(group_scores) / len(group_scores)


_SCORERS = {
    'step2': score_0,
    'step3': score_1,
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
