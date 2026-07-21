import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, re


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


# === block: score_0 (check id='perc_chi0.5') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    def _find_closest_p(rows, target):
        best = None
        best_dist = float('inf')
        for r in rows:
            try:
                d = abs(float(r['p']) - target)
            except (ValueError, KeyError):
                continue
            if d < best_dist:
                best_dist = d
                best = r
        return best, best_dist

    # convert all rows to floats for convenience
    frows = []
    for r in rows:
        try:
            frows.append({k: float(v) for k, v in r.items()})
        except (ValueError, KeyError):
            return 0.0
    frows.sort(key=lambda x: x['p'])

    score = 0.0
    # 1) percolation threshold: at p~0.65, prob_connected_nonhexatic is 0.5 ± tol
    best_r, dist = _find_closest_p(frows, 0.65)
    if best_r is not None and abs(best_r['prob_connected_nonhexatic'] - 0.5) <= 0.05:
        score += 0.4

    # 2) max p behavior: at highest p, prob_connected_nonhexatic >= 0.9, hexatic <= 0.1, largest >= 0.9
    max_p = frows[-1]['p']
    if frows[-1]['prob_connected_nonhexatic'] >= 0.9 and frows[-1]['prob_hexatic_connected'] <= 0.1 and frows[-1]['largest_comp_fraction'] >= 0.9:
        score += 0.3

    # 3) min p behavior: at lowest p, prob_nonhexatic <= 0.05, hexatic >= 0.95, largest <= 0.05
    if frows[0]['prob_connected_nonhexatic'] <= 0.05 and frows[0]['prob_hexatic_connected'] >= 0.95 and frows[0]['largest_comp_fraction'] <= 0.05:
        score += 0.3

    return min(score, 1.0)


# === block: score_1 (check id='perc_chi0.1') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    frows = []
    for r in rows:
        try:
            frows.append({k: float(v) for k, v in r.items()})
        except (ValueError, KeyError):
            return 0.0
    frows.sort(key=lambda x: x['p'])

    score = 0.0
    # 1) at max p, prob_nonhexatic >= 0.8
    if frows[-1]['prob_connected_nonhexatic'] >= 0.8:
        score += 0.5
    # 2) at min p, hexatic >= 0.95
    if frows[0]['prob_hexatic_connected'] >= 0.95:
        score += 0.5
    return min(score, 1.0)


# === block: score_2 (check id='perc_chi0.9') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    frows = []
    for r in rows:
        try:
            frows.append({k: float(v) for k, v in r.items()})
        except (ValueError, KeyError):
            return 0.0

    max_nonhex = max(r['prob_connected_nonhexatic'] for r in frows)
    min_hex = min(r['prob_hexatic_connected'] for r in frows)
    score = 0.0
    # no percolation: max prob_nonhexatic < 0.3
    if max_nonhex < 0.3:
        score += 0.7
    # hexatic stays connected: min hexatic >= 0.9
    if min_hex >= 0.9:
        score += 0.3
    return min(score, 1.0)


# === block: score_3 (check id='fractal_dim') ===
def score_3(artifact, step, ctx):
    text = artifact  # raw string
    if not text:
        return 0.0
    # parse lines: 'Fractal dimension D (bidispersed): <float>' and random
    import re
    match_b = re.search(r'Fractal dimension D \(bidispersed\)\s*:\s*([\d.eE+-]+)', text)
    match_r = re.search(r'Fractal dimension D \(random-site\)\s*:\s*([\d.eE+-]+)', text)
    if not match_b or not match_r:
        return 0.0
    try:
        d_b = float(match_b.group(1))
        d_r = float(match_r.group(1))
    except ValueError:
        return 0.0

    def score_closeness(value, target, tol):
        diff = abs(value - target)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 0.5
        else:
            return 0.0

    s_b = score_closeness(d_b, 1.86, 0.05)
    s_r = score_closeness(d_r, 1.896, 0.05)
    return (s_b + s_r) / 2.0


_SCORERS = {
    'perc_chi0.5': score_0,
    'perc_chi0.1': score_1,
    'perc_chi0.9': score_2,
    'fractal_dim': score_3,
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
