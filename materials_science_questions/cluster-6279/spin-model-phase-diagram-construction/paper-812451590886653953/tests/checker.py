import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os


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


# === block: score_0 (check id='delta_h2') ===
def score_0(artifact, step, ctx):
    def score_delta_h2(rows):
        A_rows = [r for r in rows if r['model'] == 'A']
        B_rows = [r for r in rows if r['model'] == 'B']
        score = 0.0
        if A_rows:
            xs = [math.log(float(r['L'])) for r in A_rows]
            ys = [float(r['delta_h2']) for r in A_rows]
            n = len(xs)
            if n >= 2:
                x_mean = sum(xs)/n
                y_mean = sum(ys)/n
                num = sum((x - x_mean)*(y - y_mean) for x,y in zip(xs,ys))
                den = sum((x - x_mean)**2 for x in xs)
                slope = num/den if den != 0 else 0.0
                score_A = max(0.0, 1.0 - abs(slope - 0.0406318)/0.01)
            else:
                score_A = 0.0
            score += score_A * 0.5
        else:
            score += 0.5
        if B_rows:
            xs = [math.log(float(r['L'])) for r in B_rows]
            ys = [float(r['delta_h2']) for r in B_rows]
            n = len(xs)
            if n >= 2:
                x_mean = sum(xs)/n
                y_mean = sum(ys)/n
                num = sum((x - x_mean)*(y - y_mean) for x,y in zip(xs,ys))
                den = sum((x - x_mean)**2 for x in xs)
                slope = num/den if den != 0 else 0.0
                if slope <= 0:
                    score_B = 1.0
                else:
                    score_B = max(0.0, 1.0 - slope/0.01)
            else:
                score_B = 0.0
            score += score_B * 0.5
        else:
            score += 0.5
        return score


# === block: score_1 (check id='order_param') ===
def score_1(artifact, step, ctx):
    def score_order_param(rows):
        A_rows = [r for r in rows if r['model'] == 'A']
        B_rows = [r for r in rows if r['model'] == 'B']
        score = 0.0
        if A_rows:
            ts = [float(r['t']) for r in A_rows]
            Ps = [float(r['P']) for r in A_rows]
            chips = [float(r['chi_P']) for r in A_rows]
            if ts:
                min_idx = min(range(len(Ps)), key=lambda i: Ps[i])
                t_min_P = ts[min_idx]
                max_idx = max(range(len(chips)), key=lambda i: chips[i])
                t_max_chi = ts[max_idx]
                score_A_dip = max(0.0, 1.0 - abs(t_min_P - 0.5)/0.1)
                score_A_peak = max(0.0, 1.0 - abs(t_max_chi - 0.5)/0.1)
                high_t_Ps = [Ps[i] for i,t in enumerate(ts) if t >= 1.0]
                high_t_ok = 1.0 if high_t_Ps and max(high_t_Ps) < 0.1 else 0.0
                score_A = 0.4*score_A_dip + 0.4*score_A_peak + 0.2*high_t_ok
            else:
                score_A = 0.0
            score += score_A * 0.5
        else:
            score += 0.5
        if B_rows:
            ts = [float(r['t']) for r in B_rows]
            Ps = [float(r['P']) for r in B_rows]
            chips = [float(r['chi_P']) for r in B_rows]
            if ts:
                min_idx = min(range(len(Ps)), key=lambda i: Ps[i])
                t_min_P = ts[min_idx]
                max_idx = max(range(len(chips)), key=lambda i: chips[i])
                t_max_chi = ts[max_idx]
                score_B_dip = max(0.0, 1.0 - abs(t_min_P - 0.25)/0.1)
                score_B_peak = max(0.0, 1.0 - abs(t_max_chi - 0.25)/0.1)
                high_t_Ps = [Ps[i] for i,t in enumerate(ts) if t >= 1.0]
                high_t_ok = 1.0 if high_t_Ps and max(high_t_Ps) < 0.1 else 0.0
                score_B = 0.4*score_B_dip + 0.4*score_B_peak + 0.2*high_t_ok
            else:
                score_B = 0.0
            score += score_B * 0.5
        else:
            score += 0.5
        return score


# === block: score_2 (check id='roughness_K_X') ===
def score_2(artifact, step, ctx):
    def score_K_X(rows):
        if not rows:
            return 0.0
        ts = [float(r['t']) for r in rows]
        Ks = [float(r['K']) for r in rows]
        Xs = [float(r['X']) for r in rows]
        # 1. K near t=0.5
        near05 = [K for t,K in zip(ts,Ks) if 0.45 <= t <= 0.55]
        if near05:
            avg_K = sum(near05)/len(near05)
            score_K_pr = max(0.0, 1.0 - abs(avg_K - 0.08)/0.02)
        else:
            score_K_pr = 0.0
        # 2. crossing point
        cross_t = None
        for t,K in zip(ts,Ks):
            if K >= 0.2026:
                cross_t = t
                break
        if cross_t is not None:
            score_cross = max(0.0, 1.0 - abs(cross_t - 1.2)/0.2)
        else:
            score_cross = 0.0
        # 3. X peaks
        X_at_05 = None
        X_at_12 = None
        for t,X in zip(ts,Xs):
            if 0.45 <= t <= 0.55:
                X_at_05 = X if X_at_05 is None or X > X_at_05 else X_at_05
            if 1.15 <= t <= 1.25:
                X_at_12 = X if X_at_12 is None or X > X_at_12 else X_at_12
        score_X = 0.0
        if X_at_05 is not None:
            score_X += 0.5 if X_at_05 >= 50 else 0.0
        if X_at_12 is not None:
            score_X += 0.5 if X_at_12 >= 50 else 0.0
        return 0.4*score_K_pr + 0.4*score_cross + 0.2*score_X


_SCORERS = {
    'delta_h2': score_0,
    'order_param': score_1,
    'roughness_K_X': score_2,
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
