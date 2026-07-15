import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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


# === block: score_0 (check id='step_geom_opt') ===
def score_0(artifact, step, ctx):
    targets = step['targets']
    tol = step['tolerance']
    found = set()
    total_fields = 0
    matches = 0
    for row in artifact:
        comp = row['compound'].strip()
        if comp not in targets:
            continue
        found.add(comp)
        for field in ['a','c','X_B_distance','B_B_distance']:
            if field not in targets[comp] or field not in row:
                continue
            val = float(row[field])
            ref = targets[comp][field]
            if abs(val - ref) <= tol[field]:
                matches += 1
            total_fields += 1
    if total_fields == 0:
        return 0.0
    return matches / total_fields


# === block: score_1 (check id='step_gamma_freq') ===
def score_1(artifact, step, ctx):
    targets = step['targets']
    tol = step['tolerance']
    total_vals = 0
    matches = 0
    for row in artifact:
        comp = row['compound'].strip()
        if comp not in targets:
            continue
        for field in ['E1u','A2u','B1g','E2g']:
            if field not in row or field not in targets[comp]:
                continue
            val = float(row[field])
            if abs(val - targets[comp][field]) <= tol:
                matches += 1
            total_vals += 1
    if total_vals == 0:
        return 0.0
    return matches / total_vals


# === block: score_2 (check id='step_thermo') ===
def score_2(artifact, step, ctx):
    zpe = step['zero_point_energy']
    etol = step['energy_tolerance']
    dplim = step['dulong_petit_limit']
    dpfrac = step['dulong_tolerance_frac']
    target_T = step['eval_temp_k']
    compounds = list(zpe.keys())
    def find_row(data, comp, target_temp, delta=1e-3):
        best = None
        best_diff = float('inf')
        for row in data:
            if row['compound'].strip() != comp:
                continue
            try:
                t = float(row['T_K'])
            except:
                continue
            diff = abs(t - target_temp)
            if diff < best_diff:
                best_diff = diff
                best = row
        return best

    def monotonic_score(data, comp):
        rows = [(float(r['T_K']), float(r['entropy_meV_per_K'])) for r in data if r['compound'].strip()==comp]
        rows.sort()
        for i in range(1, len(rows)):
            if rows[i][1] + 1e-8 < rows[i-1][1]:
                return 0
        return 1

    def linearity_score(data, comp):
        rows = [(float(r['T_K']), float(r['internal_energy_meV_per_cell'])) for r in data if r['compound'].strip()==comp and float(r['T_K'])>300.0]
        if len(rows)<3:
            return 0
        n = len(rows)
        sumx = sum(r[0] for r in rows)
        sumy = sum(r[1] for r in rows)
        sumxy = sum(r[0]*r[1] for r in rows)
        sumx2 = sum(r[0]*r[0] for r in rows)
        sumy2 = sum(r[1]*r[1] for r in rows)
        denom = math.sqrt((n*sumx2 - sumx*sumx)*(n*sumy2 - sumy*sumy))
        if denom == 0:
            return 0
        r = (n*sumxy - sumx*sumy)/denom
        if r < 0:
            return 0
        r2 = r*r
        return 1.0 if r2>=0.99 else 0.0

    scores_u0 = []
    scores_f0 = []
    scores_cv = []
    scores_smono = []
    scores_ulin = []
    for comp in compounds:
        row0 = find_row(artifact, comp, 0.0)
        if row0 is not None:
            u0 = float(row0.get('internal_energy_meV_per_cell', 0))
            f0 = float(row0.get('free_energy_meV_per_cell', 0))
            ref = zpe[comp]
            scores_u0.append(1 if abs(u0-ref)<=etol else 0)
            scores_f0.append(1 if abs(f0-ref)<=etol else 0)
        else:
            scores_u0.append(0)
            scores_f0.append(0)
        rowT = find_row(artifact, comp, target_T, delta=5.0)
        if rowT is not None:
            cv = float(rowT.get('heat_capacity_meV_per_K', 0))
            scores_cv.append(1 if abs(cv-dplim)<=dpfrac*dplim else 0)
        else:
            scores_cv.append(0)
        scores_smono.append(monotonic_score(artifact, comp))
        scores_ulin.append(linearity_score(artifact, comp))

    avg = lambda lst: sum(lst)/len(lst) if lst else 0.0
    sub_scores = [avg(scores_u0), avg(scores_f0), avg(scores_cv), avg(scores_smono), avg(scores_ulin)]
    sub_weights = [0.2, 0.2, 0.3, 0.15, 0.15]
    total = sum(w*s for w,s in zip(sub_weights, sub_scores))
    return min(1.0, max(0.0, total))


_SCORERS = {
    'step_geom_opt': score_0,
    'step_gamma_freq': score_1,
    'step_thermo': score_2,
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
