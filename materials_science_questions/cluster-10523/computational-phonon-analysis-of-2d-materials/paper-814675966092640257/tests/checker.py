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


# === block: score_0 (check id='grain_series') ===
def score_0(artifact, step, ctx):
    rows = artifact  # artifact is a list of dicts from CSV
    settings = step.get('settings', {})
    cond = settings.get('conditions', {})
    strain_cond = float(cond.get('strain', 0))
    temp_cond = float(cond.get('temperature_K', 300))
    gold = settings.get('gold', {})
    grain_sizes = settings.get('grain_sizes', [])
    abstol = settings.get('abs_tolerance', 0.10)
    mono_required = settings.get('monotonicity_required', True)
    # collect reported values
    reported = {}
    for row in rows:
        try:
            gs = float(row.get('grain_size_nm'))
            s = float(row.get('strain'))
            t = float(row.get('temperature_K'))
            val = float(row.get('normalized_K'))
        except (TypeError, ValueError):
            continue
        if abs(s - strain_cond) < 1e-6 and abs(t - temp_cond) < 1e-6:
            reported[gs] = val

    # point accuracy
    point_scores = []
    for gs in grain_sizes:
        gold_val = float(gold.get(str(gs), None))
        if gold_val is None or gs not in reported:
            point_scores.append(0.0)
        else:
            err = abs(reported[gs] - gold_val)
            point_scores.append(1.0 if err <= abstol else 0.0)
    avg_acc = sum(point_scores) / max(len(point_scores), 1)

    # monotonicity: poly grains only (gs > 0) sorted ascending
    poly_gs = sorted([g for g in grain_sizes if g > 0])
    poly_vals = [reported[g] for g in poly_gs if g in reported]
    mono_ok = True
    if mono_required and len(poly_vals) >= 2:
        for i in range(1, len(poly_vals)):
            if poly_vals[i] < poly_vals[i-1] - 1e-9:
                mono_ok = False
                break
    factor = 1.0 if mono_ok else 0.5
    return avg_acc * factor


# === block: score_1 (check id='strain_series') ===
def score_1(artifact, step, ctx):
    rows = artifact
    settings = step.get('settings', {})
    cond = settings.get('conditions', {})
    temp_cond = float(cond.get('temperature_K', 300))
    groups = settings.get('groups', {})
    strain_vals = settings.get('strain_values', [])
    gold = settings.get('gold', {})
    reltol = settings.get('rel_tolerance', 0.20)
    mono_required = settings.get('monotonicity_required', True)

    # build reported dict: group_key -> list of values per strain in order
    reported = {}
    for row in rows:
        try:
            gs = float(row.get('grain_size_nm'))
            s = float(row.get('strain'))
            t = float(row.get('temperature_K'))
            val = float(row.get('normalized_K'))
        except (TypeError, ValueError):
            continue
        if abs(t - temp_cond) > 1e-6:
            continue
        # match group
        for gkey, gcfg in groups.items():
            if 'grain_size_nm' in gcfg and abs(gs - gcfg['grain_size_nm']) < 1e-6:
                reported.setdefault(gkey, {})[s] = val
                break

    point_scores = []
    mono_all = True
    for gkey in groups:
        gvals = reported.get(gkey, {})
        gold_vals = gold.get(gkey, [])
        for idx, s in enumerate(strain_vals):
            if s in gvals and idx < len(gold_vals):
                gv = gold_vals[idx]
                rv = gvals[s]
                if gv > 0:
                    err_ratio = abs(rv - gv) / gv
                else:
                    err_ratio = abs(rv - gv)
                point_scores.append(1.0 if err_ratio <= reltol else 0.0)
            else:
                point_scores.append(0.0)
        # monotonicity: non-increasing with strain
        if mono_required:
            sorted_vals = [gvals[s] for s in sorted(gvals.keys())]
            if len(sorted_vals) >= 2:
                for i in range(1, len(sorted_vals)):
                    if sorted_vals[i] > sorted_vals[i-1] + 1e-9:
                        mono_all = False
                        break

    avg_acc = sum(point_scores) / max(len(point_scores), 1)
    factor = 1.0 if mono_all else 0.7
    return avg_acc * factor


# === block: score_2 (check id='temp_series') ===
def score_2(artifact, step, ctx):
    rows = artifact
    settings = step.get('settings', {})
    cond = settings.get('conditions', {})
    strain_cond = float(cond.get('strain', 0.0))
    groups = settings.get('groups', {})
    temp_vals = settings.get('temp_values', [])
    gold = settings.get('gold', {})
    reltol = settings.get('rel_tolerance', 0.20)
    mono_required = settings.get('monotonicity_required', True)

    reported = {}
    for row in rows:
        try:
            gs = float(row.get('grain_size_nm'))
            s = float(row.get('strain'))
            t = float(row.get('temperature_K'))
            val = float(row.get('normalized_K'))
        except (TypeError, ValueError):
            continue
        if abs(s - strain_cond) > 1e-6:
            continue
        for gkey, gcfg in groups.items():
            if 'grain_size_nm' in gcfg and abs(gs - gcfg['grain_size_nm']) < 1e-6:
                reported.setdefault(gkey, {})[t] = val
                break

    point_scores = []
    mono_all = True
    for gkey in groups:
        gvals = reported.get(gkey, {})
        gold_vals = gold.get(gkey, [])
        for idx, t in enumerate(temp_vals):
            if t in gvals and idx < len(gold_vals):
                gv = gold_vals[idx]
                rv = gvals[t]
                if gv > 0:
                    err_ratio = abs(rv - gv) / gv
                else:
                    err_ratio = abs(rv - gv)
                point_scores.append(1.0 if err_ratio <= reltol else 0.0)
            else:
                point_scores.append(0.0)
        # monotonicity: for SC and 10nm, non-increasing; 2.5nm can be constant-ish
        if mono_required:
            sorted_vals = [gvals[t] for t in sorted(gvals.keys())]
            if len(sorted_vals) >= 2:
                if gkey == 'grain_2.5':
                    # allow slight variation, no strict monotonic demand
                    if max(sorted_vals) - min(sorted_vals) > 0.05:
                        mono_all = False
                else:
                    for i in range(1, len(sorted_vals)):
                        if sorted_vals[i] > sorted_vals[i-1] + 1e-9:
                            mono_all = False
                            break

    avg_acc = sum(point_scores) / max(len(point_scores), 1)
    factor = 1.0 if mono_all else 0.8
    return avg_acc * factor


_SCORERS = {
    'grain_series': score_0,
    'strain_series': score_1,
    'temp_series': score_2,
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
