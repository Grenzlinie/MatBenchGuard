import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict


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
    target_points = spec['steps'][0]['target_points']
    tolerance = spec['steps'][0]['tolerance']

    def expected_lc(u):
        if u >= 0.4:
            return None  # stable
        A = 0.03333
        return 0.418 * u + A * (1.0 / (0.4 - u) - 2.5)

    def expected_ac(u):
        if u >= 0.4:
            return None
        C = 0.012732
        return 0.579 - C / (0.4**2) + C / ((0.4 - u)**2)

    return {'target_points': target_points, 'tolerance': tolerance, 'expected_lc': expected_lc, 'expected_ac': expected_ac}


# === block: score_0 (check id='critical_lengths_check') ===
def score_0(artifact, step, ctx):
    import math

    tolerance = ctx.get('tolerance', 0.15)
    target_points = ctx.get('target_points', [])

    def _ssy_gold(u, f_r_fp=0.6):
        c = 1.2 / math.pi
        d = 0.4  # 1 - f_r/f_p
        delta = d - u  # (tau0 - tau_r)/tau_p
        if delta <= 0:
            return None
        const = 0.16 / math.pi
        x_min = const / ((delta + c * math.pi / 2) ** 2) if (delta + c * math.pi / 2) != 0 else 0.0
        x_max = const / (delta ** 2) if delta != 0 else 1e10
        best_l = -1.0
        best_x = None
        N = 2000
        for i in range(N):
            x = x_min + (x_max - x_min) * i / (N - 1)
            if x <= 0:
                continue
            arg = math.sqrt(0.16 / (math.pi * x)) - delta
            if arg < 0 or arg > c * math.pi / 2:
                continue
            angle = arg / c
            if angle < 0 or angle > math.pi / 2:
                continue
            l = x * math.sin(angle)
            if l > best_l:
                best_l = l
                best_x = x
        if best_x is None:
            return None
        return best_l, best_x

    agent_map = {}
    for row in artifact:
        try:
            us = float(row.get('understress_normalized', '').strip())
        except (ValueError, TypeError):
            continue
        lc_str = str(row.get('critical_HF_length', '')).strip()
        ac_str = str(row.get('critical_slip_length', '')).strip()
        agent_map[us] = (lc_str, ac_str)

    points_scores = []
    for us in target_points:
        if us not in agent_map:
            points_scores.append(0.0)
            continue
        lc_str, ac_str = agent_map[us]
        if us >= 0.4:
            lc_ok = lc_str == '' or lc_str.lower() == 'stable'
            ac_ok = ac_str == '' or ac_str.lower() == 'stable'
            points_scores.append(1.0 if (lc_ok and ac_ok) else 0.0)
            continue
        gold = _ssy_gold(us)
        if gold is None:
            points_scores.append(0.0)
            continue
        lc_gold, ac_gold = gold
        try:
            lc_val = float(lc_str)
            ac_val = float(ac_str)
        except (ValueError, TypeError):
            points_scores.append(0.0)
            continue
        def _point_score(val, gold):
            if gold == 0.0:
                return 1.0 if abs(val) <= 1e-6 else 0.0
            rel_err = abs(val - gold) / max(abs(gold), 1e-8)
            if rel_err <= tolerance:
                return 1.0
            return max(0.0, 1.0 - (rel_err - tolerance) / tolerance)
        s_lc = _point_score(lc_val, lc_gold)
        s_ac = _point_score(ac_val, ac_gold)
        points_scores.append(0.5 * s_lc + 0.5 * s_ac)

    return sum(points_scores) / len(target_points) if target_points else 0.0


_SCORERS = {
    'critical_lengths_check': score_0,
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
