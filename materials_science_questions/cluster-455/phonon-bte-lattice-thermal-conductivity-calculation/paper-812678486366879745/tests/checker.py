import os
import json
import csv

# === author imports / helpers ===
import math
import statistics
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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    # Step 1: check modulus and TC against Table 1 with tolerance, plus monotonic decreasing

    gold_points = step.get('params', {}).get('gold', [])
    tol_rel = step.get('params', {}).get('tolerance_relative', 0.20)
    mono_fields = step.get('params', {}).get('check_monotonic_decreasing', [])

    # index agent rows by strain_percent
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    agent_by_strain = {}
    for r in rows:
        try:
            s = int(r.get('strain_percent', -1))
        except:
            continue
        if s >= 0:
            agent_by_strain[s] = r

    # count points within tolerance
    n_gold = len(gold_points)
    points_ok = 0.0
    for g in gold_points:
        s = g.get('strain_percent')
        if s is None or s not in agent_by_strain:
            continue
        a = agent_by_strain[s]
        ok = True
        for field in ['elastic_modulus_GPa', 'thermal_conductivity_W_mK']:
            try:
                a_val = float(a.get(field, 0))
                g_val = float(g.get(field, 0))
            except:
                ok = False
                break
            if g_val == 0:
                if a_val != 0:
                    ok = False
                    break
            else:
                rel_err = abs(a_val - g_val) / abs(g_val)
                if rel_err > tol_rel:
                    ok = False
                    break
        if ok:
            points_ok += 1

    point_frac = points_ok / n_gold if n_gold > 0 else 0.0

    # monotonic decreasing
    sorted_rows = sorted(rows, key=lambda r: int(r.get('strain_percent', 999)) if 'strain_percent' in r else 999)
    mono_ok = True
    for i in range(1, len(sorted_rows)):
        for field in mono_fields:
            try:
                v_curr = float(sorted_rows[i].get(field, 0))
                v_prev = float(sorted_rows[i-1].get(field, 0))
            except:
                mono_ok = False
                break
            if v_curr > v_prev:
                mono_ok = False
                break
        if not mono_ok:
            break
    mono_bonus = 1.0 if mono_ok else 0.0

    score = point_frac * 0.7 + mono_bonus * 0.3
    return min(max(score, 0.0), 1.0)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    # Step 2: compute ratio κ_strain/κ_sim, compare trend via Pearson correlation with expected modulus-reduction factor, check monotonic increase with pitch

    rows = artifact
    if not isinstance(rows, list) or len(rows) < 2:
        return 0.0

    # compute ratio per pitch
    ratios = {}
    for r in rows:
        try:
            pitch = int(r['pitch_nm'])
            ks = float(r['kappa_sim'])
            kst = float(r['kappa_strain'])
        except:
            continue
        if ks <= 0:
            continue
        ratios[pitch] = kst / ks

    # expected ratio mapping
    params = step.get('params', {})
    exp = params.get('expected_ratio_sqrt_modulus', {})
    pitches_ref = exp.get('pitch_nm', [])
    exp_ratios = exp.get('expected_ratio', [])
    if len(pitches_ref) == 0 or len(pitches_ref) != len(exp_ratios):
        return 0.0

    # align by common pitches in ascending order
    common = sorted([p for p in pitches_ref if p in ratios])
    if len(common) < 2:
        return 0.0

    x = []
    y = []
    for p in common:
        idx = pitches_ref.index(p)
        x.append(exp_ratios[idx])
        y.append(ratios[p])

    try:
        r = statistics.correlation(x, y)
    except:
        r = 0.0

    # correlation should be strongly positive (both increase with pitch)
    if r < 0.6:
        corr_score = 0.0
    else:
        corr_score = (r - 0.6) / (1.0 - 0.6)

    # check monotonic non-decreasing of y (ratios increase with pitch)
    mono_ok = all(y[i] <= y[i+1] for i in range(len(y)-1))
    mono_score = 1.0 if mono_ok else 0.0

    score = corr_score * 0.8 + mono_score * 0.2
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
