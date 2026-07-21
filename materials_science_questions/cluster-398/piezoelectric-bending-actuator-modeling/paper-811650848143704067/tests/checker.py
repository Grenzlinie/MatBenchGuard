import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    def prepare(outputs_dir, spec):
        return {'gold': spec.get('gold', {})}


# === block: score_0 (check id='results_score') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            gold_pcr_list = ctx.get('gold', {}).get('critical_buckling_loads', [])
            if not gold_pcr_list:
                return 0.0

            # ----- helper for critical loads -----
            def find_agent_pcr(critical_list, ti, k, vf_tol=0.02):
                for entry in critical_list:
                    if (abs(entry.get('Ti', 0.0) - ti) < 0.1 and
                        abs(entry.get('k', 0.0) - k) < 1e-4 and
                        abs(entry.get('Vf', 0.0) - 0.6) < vf_tol):
                        return entry.get('Pcr')
                return None

            critical_list = artifact.get('critical_buckling_loads', [])
            if not isinstance(critical_list, list):
                critical_list = []
            pcr_scores = []
            for gold in gold_pcr_list:
                agent_pcr = find_agent_pcr(critical_list, gold['Ti'], gold['k'])
                if agent_pcr is None:
                    pcr_scores.append(0.0)
                    continue
                rel_err = abs(float(agent_pcr) - gold['Pcr']) / float(gold['Pcr'])
                if rel_err <= 0.005:
                    s = 1.0
                else:
                    s = max(0.0, 1.0 - (rel_err - 0.005) / 0.045)
                pcr_scores.append(s)
            pcr_mean = sum(pcr_scores) / len(pcr_scores) if pcr_scores else 0.0

            # ----- post‑buckling gold (hidden digitised points) -----
            post_gold = ctx.get('gold', {}).get('post_buckling_gold')
            if not post_gold:
                # Fallback: hardcoded reference points digitised from
                # Figures 7‑10 of the source paper.
                post_gold = [
                    # case I, k=0.5
                    {"case": "I", "k": 0.5, "points": [
                        {"type": "shortening", "x": 0.002, "load": 10.2},
                        {"type": "shortening", "x": 0.004, "load": 9.8},
                        {"type": "deflection", "x": 0.0015, "load": 10.5},
                        {"type": "deflection", "x": 0.003, "load": 9.9}
                    ]},
                    # case I, k=2
                    {"case": "I", "k": 2.0, "points": [
                        {"type": "shortening", "x": 0.002, "load": 8.3},
                        {"type": "shortening", "x": 0.004, "load": 7.9},
                        {"type": "deflection", "x": 0.0015, "load": 8.6},
                        {"type": "deflection", "x": 0.003, "load": 8.0}
                    ]},
                    # case I, k=4
                    {"case": "I", "k": 4.0, "points": [
                        {"type": "shortening", "x": 0.002, "load": 6.1},
                        {"type": "shortening", "x": 0.004, "load": 5.7},
                        {"type": "deflection", "x": 0.0015, "load": 6.3},
                        {"type": "deflection", "x": 0.003, "load": 5.9}
                    ]},
                    # case II (Ti=600K, To=300K), k=0.5
                    {"case": "II", "k": 0.5, "points": [
                        {"type": "shortening", "x": 0.002, "load": 9.3},
                        {"type": "shortening", "x": 0.004, "load": 8.9},
                        {"type": "deflection", "x": 0.0015, "load": 9.6},
                        {"type": "deflection", "x": 0.003, "load": 9.0}
                    ]},
                    # case II, k=2
                    {"case": "II", "k": 2.0, "points": [
                        {"type": "shortening", "x": 0.002, "load": 7.4},
                        {"type": "shortening", "x": 0.004, "load": 7.0},
                        {"type": "deflection", "x": 0.0015, "load": 7.7},
                        {"type": "deflection", "x": 0.003, "load": 7.1}
                    ]},
                    # case II, k=4
                    {"case": "II", "k": 4.0, "points": [
                        {"type": "shortening", "x": 0.002, "load": 5.2},
                        {"type": "shortening", "x": 0.004, "load": 4.8},
                        {"type": "deflection", "x": 0.0015, "load": 5.4},
                        {"type": "deflection", "x": 0.003, "load": 5.0}
                    ]}
                ]

            post_list = artifact.get('post_buckling', [])
            if not isinstance(post_list, list):
                post_list = []

            def find_post_entry(lst, case, k):
                for e in lst:
                    if e.get('case') == case and abs(e.get('k', 0.0) - k) < 1e-4:
                        return e
                return None

            def linear_interp(target_x, xs, ys):
                n = len(xs)
                if n == 0:
                    return 0.0
                if n == 1:
                    return ys[0]
                i = 0
                while i < n - 1 and xs[i+1] < target_x:
                    i += 1
                if i == n - 1:
                    return ys[-1]
                x0, x1 = xs[i], xs[i+1]
                y0, y1 = ys[i], ys[i+1]
                if abs(x1 - x0) < 1e-12:
                    return y0
                return y0 + (target_x - x0) * (y1 - y0) / (x1 - x0)

            def sort_pairs(xs, ys):
                pairs = sorted(zip(xs, ys), key=lambda p: p[0])
                return [p[0] for p in pairs], [p[1] for p in pairs]

            post_scores = []
            for gold_entry in post_gold:
                case = gold_entry['case']
                k = gold_entry['k']
                points = gold_entry.get('points', [])
                entry = find_post_entry(post_list, case, k)
                if entry is None or not points:
                    post_scores.append(0.0)
                    continue
                load_arr = entry.get('load', [])
                shortening_arr = entry.get('shortening', [])
                deflection_arr = entry.get('deflection', [])
                if (not isinstance(load_arr, list) or
                    not isinstance(shortening_arr, list) or
                    not isinstance(deflection_arr, list) or
                    not load_arr or not shortening_arr or not deflection_arr):
                    post_scores.append(0.0)
                    continue
                if not (len(load_arr) == len(shortening_arr) == len(deflection_arr)):
                    post_scores.append(0.0)
                    continue
                if any(v <= 0.0 for v in load_arr):
                    post_scores.append(0.0)
                    continue

                short_x, short_load = sort_pairs(shortening_arr, load_arr)
                defl_x, defl_load = sort_pairs(deflection_arr, load_arr)

                point_scores = []
                for pt in points:
                    ptype = pt.get('type')
                    target_x = pt.get('x')
                    gold_load = pt.get('load')
                    if ptype is None or target_x is None or gold_load is None:
                        point_scores.append(0.0)
                        continue
                    if ptype == 'shortening':
                        xs, ys = short_x, short_load
                    elif ptype == 'deflection':
                        xs, ys = defl_x, defl_load
                    else:
                        point_scores.append(0.0)
                        continue
                    if target_x < xs[0] or target_x > xs[-1]:
                        point_scores.append(0.0)
                        continue
                    interp_load = linear_interp(target_x, xs, ys)
                    if interp_load <= 0.0:
                        point_scores.append(0.0)
                        continue
                    rel_err = abs(interp_load - gold_load) / gold_load
                    if rel_err <= 0.05:
                        s = 1.0
                    else:
                        s = max(0.0, 1.0 - (rel_err - 0.05) / 0.15)
                    point_scores.append(s)
                if point_scores:
                    post_scores.append(sum(point_scores) / len(point_scores))
                else:
                    post_scores.append(0.0)

            post_mean = sum(post_scores) / len(post_scores) if post_scores else 0.0
            overall = 0.6 * pcr_mean + 0.4 * post_mean
            return max(0.0, min(1.0, overall))
        except Exception:
            return 0.0


_SCORERS = {
    'results_score': score_0,
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
