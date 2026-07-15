import os
import json
import csv

# === author imports / helpers ===
import csv
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
    return {}


# === block: score_0 (check id='validate_structure') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    required_cols = {'hopping_radius','surface_tension','mcs_per_particle','energy','cluster_count','fractal_dimension'}
    if not required_cols.issubset(rows[0].keys()):
        return 0.0
    groups = defaultdict(list)
    for r in rows:
        key = (r.get('hopping_radius'), r.get('surface_tension'))
        groups[key].append(r)
    if len(groups) < 3:
        return 0.0
    for key, pts in groups.items():
        if len(pts) < 10:
            return 0.0
    return 1.0


# === block: score_1 (check id='cluster_overshoot') ===
def score_1(artifact, step, ctx):
    rows = artifact
    groups = defaultdict(list)
    for r in rows:
        key = (r.get('hopping_radius'), r.get('surface_tension'))
        groups[key].append(r)
    score_per_group = []
    for key, pts in groups.items():
        pts_sorted = sorted(pts, key=lambda x: float(x.get('mcs_per_particle',0)))
        if not pts_sorted:
            continue
        first_cc = int(pts_sorted[0].get('cluster_count',-1))
        if first_cc != 1:
            score_per_group.append(0.0)
            continue
        # region mcs < 1000
        early = [p for p in pts_sorted if float(p.get('mcs_per_particle',0)) < 1000.0]
        if not early:
            early = pts_sorted[:min(10, len(pts_sorted))]
        peak = max(int(p.get('cluster_count',0)) for p in early)
        if peak <= 2:
            score_per_group.append(0.0)
            continue
        final_cc = int(pts_sorted[-1].get('cluster_count',0))
        if final_cc < peak * 0.9:
            score_per_group.append(1.0)
        else:
            score_per_group.append(0.0)
    if not score_per_group:
        return 0.0
    return sum(score_per_group) / len(score_per_group)


# === block: score_2 (check id='hopping_radius_peak_effect') ===
def score_2(artifact, step, ctx):
    rows = artifact
    group_peaks = {}
    for r in rows:
        if float(r.get('surface_tension',0)) != 0.0:
            continue
        hr = int(r.get('hopping_radius',0))
        if hr not in (8, 36):
            continue
        key = hr
        if key not in group_peaks:
            group_peaks[key] = {'early': []}
        mcs = float(r.get('mcs_per_particle',0))
        if mcs < 1000.0:
            group_peaks[key]['early'].append(int(r.get('cluster_count',0)))
    peak_8 = max(group_peaks.get(8,{}).get('early',[0])) if 8 in group_peaks else 0
    peak_36 = max(group_peaks.get(36,{}).get('early',[0])) if 36 in group_peaks else 0
    if peak_8 == 0 or peak_36 == 0:
        return 0.0
    return 1.0 if peak_36 > peak_8 else 0.0


# === block: score_3 (check id='fractal_stability') ===
def score_3(artifact, step, ctx):
    rows = artifact
    groups = defaultdict(list)
    for r in rows:
        key = (r.get('hopping_radius'), r.get('surface_tension'))
        groups[key].append(r)
    score_per_group = []
    for key, pts in groups.items():
        vals = [float(p.get('fractal_dimension',0)) for p in pts]
        if all(1.4 <= v <= 2.0 for v in vals):
            score_per_group.append(1.0)
        else:
            score_per_group.append(0.0)
    if not score_per_group:
        return 0.0
    return sum(score_per_group) / len(score_per_group)


# === block: score_4 (check id='energy_final_thresholds') ===
def score_4(artifact, step, ctx):
    rows = artifact
    groups = defaultdict(list)
    for r in rows:
        if float(r.get('surface_tension',0)) != 0.0:
            continue
        hr = int(r.get('hopping_radius',0))
        if hr not in (8, 36):
            continue
        groups[hr].append(r)
    def score_energy(val, target, penalty_per_unit):
        if val <= target:
            return 1.0
        diff = val - target
        score = max(0.0, 1.0 - diff / penalty_per_unit)
        return score
    scores = []
    for hr, pts in groups.items():
        pts_sorted = sorted(pts, key=lambda x: float(x.get('mcs_per_particle',0)))
        if not pts_sorted:
            continue
        final_e = float(pts_sorted[-1].get('energy',0))
        if hr == 8:
            s = score_energy(final_e, -1.8, 0.5)
        else:  # 36
            s = score_energy(final_e, -2.4, 0.3)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_5 (check id='energy_monotonic') ===
def score_5(artifact, step, ctx):
    rows = artifact
    groups = defaultdict(list)
    for r in rows:
        key = (r.get('hopping_radius'), r.get('surface_tension'))
        groups[key].append(r)
    score_per_group = []
    for key, pts in groups.items():
        pts_sorted = sorted(pts, key=lambda x: float(x.get('mcs_per_particle',0)))
        if len(pts_sorted) < 2:
            score_per_group.append(0.0)
            continue
        start_e = float(pts_sorted[0].get('energy',0))
        end_e = float(pts_sorted[-1].get('energy',0))
        if end_e < start_e:
            score_per_group.append(1.0)
        else:
            score_per_group.append(0.0)
    if not score_per_group:
        return 0.0
    return sum(score_per_group) / len(score_per_group)


_SCORERS = {
    'validate_structure': score_0,
    'cluster_overshoot': score_1,
    'hopping_radius_peak_effect': score_2,
    'fractal_stability': score_3,
    'energy_final_thresholds': score_4,
    'energy_monotonic': score_5,
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
