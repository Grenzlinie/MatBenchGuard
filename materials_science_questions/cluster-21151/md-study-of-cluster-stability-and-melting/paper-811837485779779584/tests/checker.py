import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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


# === block: score_0 (check id='exafs_check') ===
def score_0(artifact, step, ctx):
    import math

    def count_local_minima(k, chi):
        if len(k) < 3:
            return 0
        dchi = [(chi[i+1]-chi[i])/(k[i+1]-k[i]) if k[i+1]-k[i] != 0 else 0.0 for i in range(len(chi)-1)]
        minima = 0
        for i in range(len(dchi)-1):
            if dchi[i] < 0 and dchi[i+1] > 0:
                minima += 1
        return minima

    def pearson_r(x, y):
        n = len(x)
        if n != len(y) or n < 2:
            return 0.0
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(a*b for a,b in zip(x,y))
        sum_x2 = sum(a*a for a in x)
        sum_y2 = sum(b*b for b in y)
        numerator = n * sum_xy - sum_x * sum_y
        denom_x = n * sum_x2 - sum_x * sum_x
        denom_y = n * sum_y2 - sum_y * sum_y
        if denom_x <= 0 or denom_y <= 0:
            return 0.0
        r = numerator / (math.sqrt(denom_x) * math.sqrt(denom_y))
        return 0.0 if math.isnan(r) else r

    score = 0.0
    try:
        # Cu-K similarity
        cu50_k = artifact['Cu50Zr50_Cu_K']['k']
        cu50_chi = artifact['Cu50Zr50_Cu_K']['chi']
        cu45ag10_k = artifact['Cu45Zr45Ag10_Cu_K']['k']
        cu45ag10_chi = artifact['Cu45Zr45Ag10_Cu_K']['chi']
        if len(cu50_k) == len(cu45ag10_k) and len(cu50_k) > 0:
            r_cu = pearson_r(cu50_chi, cu45ag10_chi)
            if r_cu >= step['target']['cu_corr_min']:
                cu_score = 1.0
            elif r_cu > 0.8:
                cu_score = (r_cu - 0.8) / (step['target']['cu_corr_min'] - 0.8)
            else:
                cu_score = 0.0
        else:
            cu_score = 0.0

        # Zr-K dissimilarity
        zr50_k = artifact['Cu50Zr50_Zr_K']['k']
        zr50_chi = artifact['Cu50Zr50_Zr_K']['chi']
        zr45ag10_k = artifact['Cu45Zr45Ag10_Zr_K']['k']
        zr45ag10_chi = artifact['Cu45Zr45Ag10_Zr_K']['chi']
        if len(zr50_k) == len(zr45ag10_k) and len(zr50_k) > 0:
            r_zr = pearson_r(zr50_chi, zr45ag10_chi)
            if r_zr <= step['target']['zr_corr_max']:
                zr_score = 1.0
            elif r_zr < 0.98:
                zr_score = (0.98 - r_zr) / (0.98 - step['target']['zr_corr_max'])
            else:
                zr_score = 0.0
        else:
            zr_score = 0.0

        # Peak splitting for Cu40Zr40Ag20 Cu-K vs Cu50Zr50 Cu-K (more minima indicates splitting)
        cu40_k = artifact['Cu40Zr40Ag20_Cu_K']['k']
        cu40_chi = artifact['Cu40Zr40Ag20_Cu_K']['chi']
        if len(cu50_k) > 0 and len(cu40_k) > 0:
            minima50 = count_local_minima(cu50_k, cu50_chi)
            minima40 = count_local_minima(cu40_k, cu40_chi)
            peak_score = 1.0 if minima40 > minima50 else 0.0
        else:
            peak_score = 0.0

        # Average of three sub-scores
        score = (cu_score + zr_score + peak_score) / 3.0
    except Exception:
        score = 0.0
    return score


# === block: score_1 (check id='voronoi_check') ===
def score_1(artifact, step, ctx):
    # Compare Cu-centered <0 2 8 1> fraction between Cu50Zr50 and Cu45Zr45Ag10
    # artifact: list of dicts from CSV
    # step: target['delta_fraction']
    import csv
    try:
        frac50 = None
        frac10 = None
        for row in artifact:
            comp = row.get('composition', '').strip()
            center = row.get('center_type', '').strip()
            idx = row.get('voronoi_index', '').strip()
            if center == 'Cu' and idx == '<0 2 8 1>':
                try:
                    f = float(row['fraction'])
                except (ValueError, KeyError):
                    continue
                if comp == 'Cu50Zr50':
                    frac50 = f
                elif comp == 'Cu45Zr45Ag10':
                    frac10 = f
        if frac50 is None or frac10 is None:
            score = 0.0
        else:
            delta = frac10 - frac50
            target_delta = step['target']['delta_fraction']
            if delta >= target_delta:
                score = 1.0
            elif delta > 0:
                score = delta / target_delta
            else:
                score = 0.0
    except Exception:
        score = 0.0
    return score


# === block: score_2 (check id='ag_coord_check') ===
def score_2(artifact, step, ctx):
    # Check average Ag–Ag coordination number exceeds 1.0 for both alloys
    # artifact: dict with keys 'Cu45Zr45Ag10' and 'Cu40Zr40Ag20'
    # step: target['min_ag_ag_coord']
    import json
    try:
        c45 = float(artifact['Cu45Zr45Ag10'])
        c40 = float(artifact['Cu40Zr40Ag20'])
        thr = step['target']['min_ag_ag_coord']
        def single_score(val):
            if val >= thr:
                return 1.0
            else:
                return max(0.0, (val - 0.5) / (thr - 0.5))
        score45 = single_score(c45)
        score40 = single_score(c40)
        score = (score45 + score40) / 2.0
    except Exception:
        score = 0.0
    return score


_SCORERS = {
    'exafs_check': score_0,
    'voronoi_check': score_1,
    'ag_coord_check': score_2,
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
