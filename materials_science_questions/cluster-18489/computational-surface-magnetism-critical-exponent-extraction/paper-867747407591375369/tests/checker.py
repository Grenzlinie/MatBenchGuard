import os
import json
import csv

# === author imports / helpers ===
import csv
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
    return {}


# === block: score_0 (check id='step_01_radial_profile') ===
def score_0(artifact, step, ctx):
    # radial profile structural scoring
    from collections import defaultdict
    float_rows = []
    for row in artifact:
        try:
            temp = row['reduced_temperature']
            r = float(row['radial_bin'])
            m = float(row['local_magnetization'])
            float_rows.append((temp, r, m))
        except:
            continue
    groups = defaultdict(list)
    for temp, r, m in float_rows:
        groups[temp].append((r, m))
    expected = {'very_low','intermediate','near_critical'}
    missing = expected - set(groups.keys())
    if missing:
        return 0.0
    centre_surface_ok = 0
    monotonic_ok = 0
    means = {}
    drops = {}
    for temp in expected:
        data = sorted(groups[temp], key=lambda x: x[0])
        if len(data) < 2:
            continue
        # centre > surface
        if data[0][1] > data[-1][1]:
            centre_surface_ok += 1
        # monotonic non-increasing (tolerance 0.02)
        mono = True
        for i in range(1, len(data)):
            if data[i][1] > data[i-1][1] + 0.02:
                mono = False
                break
        if mono:
            monotonic_ok += 1
        # mean magnetisation
        means[temp] = sum((m for _, m in data)) / len(data)
        # drop centre-to-surface
        drops[temp] = data[0][1] - data[-1][1]
    comp_centre_surface = centre_surface_ok / 3.0
    comp_monotonic = monotonic_ok / 3.0
    comp_ordering = 1.0 if (means.get('very_low',0) > means.get('intermediate',0) > means.get('near_critical',0)) else 0.0
    comp_drop_order = 1.0 if (drops.get('very_low',0) < drops.get('intermediate',0) < drops.get('near_critical',0)) else 0.0
    score = 0.2*comp_centre_surface + 0.2*comp_monotonic + 0.3*comp_ordering + 0.3*comp_drop_order
    return score


# === block: score_1 (check id='step_02_thermal_magnetization') ===
def score_1(artifact, step, ctx):
    # thermal magnetisation structural scoring
    from collections import defaultdict
    data = {}
    for row in artifact:
        try:
            size = int(row['particle_size'])
            tau = float(row['reduced_temperature'])
            core = float(row['core_magnetization'])
            surf = float(row['surface_magnetization'])
            mean = float(row['mean_magnetization'])
            if size not in data:
                data[size] = []
            data[size].append((tau, core, surf, mean))
        except:
            continue
    if 909 not in data or 3766 not in data:
        return 0.0
    # sort each size by tau
    for size in data:
        data[size].sort(key=lambda x: x[0])

    def closest(rows, target_tau):
        best = None
        best_diff = float('inf')
        for tau, core, surf, mean in rows:
            diff = abs(tau - target_tau)
            if diff < best_diff:
                best = (tau, core, surf, mean)
                best_diff = diff
        return best

    # 1. core >= surface everywhere
    n_total = sum(len(v) for v in data.values())
    if n_total == 0:
        return 0.0
    core_surf_ok = 0
    for rows in data.values():
        for tau, core, surf, mean in rows:
            if core >= surf - 0.01:
                core_surf_ok += 1
    comp_core_surf = core_surf_ok / n_total

    # 2. surface decays early: at smallest tau where surface < 0.3, core > 0.6
    passed_surf = 0
    for size in [909,3766]:
        rows = data[size]
        for tau, core, surf, mean in rows:
            if surf < 0.3:
                if core > 0.6:
                    passed_surf += 1
                break
    comp_surf_early = passed_surf / 2.0

    # 3. surface negligible at tau 0.5
    passed_ratio = 0
    for size in [909,3766]:
        row = closest(data[size], 0.5)
        if row is not None:
            core, surf = row[1], row[2]
            if core > 0 and surf / core < 0.1:
                passed_ratio += 1
    comp_ratio = passed_ratio / 2.0

    # 4. core size dependence: core_3766 < core_909 at tau=0.7 (larger particle has lower core magnetisation)
    row909 = closest(data[909], 0.7)
    row3766 = closest(data[3766], 0.7)
    comp_core_size = 0.0
    if row909 and row3766:
        core909 = row909[1]
        core3766 = row3766[1]
        if core3766 < core909:
            comp_core_size = 1.0

    score = 0.3*comp_core_surf + 0.2*comp_surf_early + 0.2*comp_ratio + 0.3*comp_core_size
    return score


_SCORERS = {
    'step_01_radial_profile': score_0,
    'step_02_thermal_magnetization': score_1,
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
