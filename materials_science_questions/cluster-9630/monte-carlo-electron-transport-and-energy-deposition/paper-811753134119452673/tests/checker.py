import os
import json
import csv

# === author imports / helpers ===
import json, csv
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


# === block: score_0 (check id='step_depth_dose') ===
def score_0(artifact, step, ctx):
    required_soft = [150, 160, 170, 180, 190]
    required_ulow = [40, 60, 110]
    grouped = {}
    for row in artifact:
        v = int(float(row['voltage_keV']))
        d = float(row['depth_um'])
        dose = float(row['dose_per_electron'])
        if v not in grouped:
            grouped[v] = []
        grouped[v].append((d, dose))
    if not all(v in grouped for v in required_soft + required_ulow):
        return 0.0
    # Helper: check depth coverage
    for v in required_soft + required_ulow:
        pts = sorted(grouped[v], key=lambda x: x[0])
        depths = [p[0] for p in pts]
        if len(pts) < 20 or min(depths) > 0 or max(depths) < 300:
            return 0.1
    # (1) Soft EB monotonic decrease
    soft_mono = []
    for v in required_soft:
        pts = sorted(grouped[v], key=lambda x: x[0])
        doses = [p[1] for p in pts]
        dec = sum(1 for i in range(len(doses)-1) if doses[i+1] <= doses[i] + 1e-12)
        frac = dec / max(1, len(doses)-1)
        soft_mono.append(frac)
    avg_soft_mono = sum(soft_mono) / len(soft_mono) if soft_mono else 0
    # (2) Soft EB energy ordering
    order_scores = []
    for v1, v2 in zip(required_soft[:-1], required_soft[1:]):
        pts1 = sorted(grouped[v1], key=lambda x: x[0])
        pts2 = sorted(grouped[v2], key=lambda x: x[0])
        d1 = {d: dose for d, dose in pts1}
        d2 = {d: dose for d, dose in pts2}
        common = sorted(set(d1.keys()) & set(d2.keys()))
        shallow = deep = total = 0
        for d in common:
            total += 1
            if d <= 50:
                if d1[d] > d2[d]:
                    shallow += 1
            elif d >= 150:
                if d2[d] > d1[d]:
                    deep += 1
        if total:
            order_scores.append((shallow + deep) / total)
    avg_order = sum(order_scores) / len(order_scores) if order_scores else 0
    # (3) Ultra-low EB: near-surface peak and monotonic after peak
    ulow_scores = []
    for v in required_ulow:
        pts = sorted(grouped[v], key=lambda x: x[0])
        doses = [p[1] for p in pts]
        if not doses:
            ulow_scores.append(0.0)
            continue
        max_idx = doses.index(max(doses))
        peak_ok = 1.0 if pts[max_idx][0] <= 30 else 0.0
        after_dec = 1.0
        if max_idx < len(doses)-1:
            after = [(doses[i+1] <= doses[i] + 1e-12) for i in range(max_idx, len(doses)-1)]
            after_dec = sum(after) / len(after)
        ulow_scores.append(0.2*peak_ok + 0.8*after_dec)
    avg_ulow = sum(ulow_scores) / len(ulow_scores) if ulow_scores else 0
    # Weighted sum
    score = 0.3*avg_soft_mono + 0.3*avg_order + 0.3*avg_ulow + 0.1
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='step_transmission') ===
def score_1(artifact, step, ctx):
    thresholds = step.get('params', {}).get('thresholds', {})
    total = 0
    correct = 0
    for key, th in thresholds.items():
        val = artifact.get(key)
        if val is None:
            continue
        total += 1
        ok = True
        if 'min' in th and val < th['min']:
            ok = False
        if 'max' in th and val > th['max']:
            ok = False
        if ok:
            correct += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'step_depth_dose': score_0,
    'step_transmission': score_1,
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
