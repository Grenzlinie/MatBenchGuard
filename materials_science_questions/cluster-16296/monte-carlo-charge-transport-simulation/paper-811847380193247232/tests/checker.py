import os
import json
import csv

# === author imports / helpers ===
from collections import defaultdict
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


# === block: score_0 (check id='chk_file_shape') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) < 16:
        return 0.0
    required = {'mechanism','position_V','energy_eV','rate_s_1'}
    first = artifact[0]
    if not required.issubset(first.keys()):
        return 0.0
    return 1.0


# === block: score_1 (check id='chk_energy_range') ===
def score_1(artifact, step, ctx):
    min_e = float(step.get('min_energy', 0.0))
    max_e = float(step.get('max_energy', 0.5))
    max_step_allowed = float(step.get('max_step', 0.01))
    energies = sorted({float(r['energy_eV']) for r in artifact})
    if not energies:
        return 0.0
    if energies[0] > min_e + 1e-9 or energies[-1] < max_e - 1e-9:
        return 0.0
    steps = [energies[i+1]-energies[i] for i in range(len(energies)-1)]
    if any(s > max_step_allowed + 1e-9 for s in steps):
        return 0.0
    return 1.0


# === block: score_2 (check id='chk_nonnegative') ===
def score_2(artifact, step, ctx):
    for r in artifact:
        if float(r['rate_s_1']) < 0.0:
            return 0.0
    return 1.0


# === block: score_3 (check id='chk_source_drain') ===
def score_3(artifact, step, ctx):
    mechs = step.get('mechanisms', [])
    if not mechs:
        return 0.0
    groups = defaultdict(list)
    for r in artifact:
        pos = float(r['position_V'])
        if pos in (0.0, 0.6):
            groups[(r['mechanism'], pos)].append(float(r['rate_s_1']))
    score = 0.0
    ok = 0
    for mech in mechs:
        src = groups.get((mech, 0.6), [])
        drn = groups.get((mech, 0.0), [])
        if not src or not drn:
            continue
        if sum(src)/len(src) > sum(drn)/len(drn):
            ok += 1
    if ok == len(mechs):
        return 1.0
    return ok / len(mechs)


# === block: score_4 (check id='chk_thresholds') ===
def score_4(artifact, step, ctx):
    thresholds = {
        "POP_1to1_abs": {"first_positive_min": 0.0, "first_positive_max": 0.01},
        "POP_1to1_emi": {"first_positive_min": 0.03, "first_positive_max": 0.05},
        "POP_1to2_abs": {"first_positive_min": 0.0, "first_positive_max": 0.01},
        "POP_1to2_emi": {"first_positive_min": 0.06, "first_positive_max": 0.08}
    }
    if not thresholds:
        return 1.0
    groups = defaultdict(list)
    for r in artifact:
        if r.get('mechanism') in thresholds:
            groups[r['mechanism']].append((float(r['energy_eV']), float(r['rate_s_1'])))
    score = 0.0
    count = 0
    for mech, entries in groups.items():
        th = thresholds.get(mech)
        if not th:
            continue
        entries.sort(key=lambda x:x[0])
        first_pos = None
        for e, v in entries:
            if v > 0:
                first_pos = e
                break
        if first_pos is None:
            continue
        lo = float(th.get('first_positive_min', 0.0))
        hi = float(th.get('first_positive_max', 100))
        count += 1
        if lo - 1e-9 <= first_pos <= hi + 1e-9:
            score += 1.0
    if count == 0:
        return 0.0
    return score / count


# === block: score_5 (check id='chk_magnitude_ordering') ===
def score_5(artifact, step, ctx):
    pop_mechs = step.get('pop_mechanisms', [])
    ap_mechs = step.get('ap_mechanisms', [])
    ii_mechs = step.get('ii_mechanisms', [])
    maxes = {}
    for r in artifact:
        mech = r['mechanism']
        v = float(r['rate_s_1'])
        maxes[mech] = max(maxes.get(mech, 0), v)
    def max_of(mech_list):
        return max((maxes.get(m, 0) for m in mech_list), default=0)
    pop_max = max_of(pop_mechs)
    ap_max = max_of(ap_mechs)
    ii_max = max_of(ii_mechs)
    if pop_max == 0 or ap_max == 0 or ii_max == 0:
        return 0.0
    if pop_max > ap_max and pop_max > ii_max:
        return 1.0
    return 0.0


_SCORERS = {
    'chk_file_shape': score_0,
    'chk_energy_range': score_1,
    'chk_nonnegative': score_2,
    'chk_source_drain': score_3,
    'chk_thresholds': score_4,
    'chk_magnitude_ordering': score_5,
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
