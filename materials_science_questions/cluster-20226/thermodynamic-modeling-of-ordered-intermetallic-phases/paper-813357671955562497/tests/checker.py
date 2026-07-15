import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='step1_u0') ===
def score_0(artifact, step, ctx):
    # Check U0_fcc and U0_bcc crossing
    if not artifact or not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    try:
        concs = [float(r['concentration']) for r in artifact]
        u0_fcc = [float(r['U0_fcc']) for r in artifact]
        u0_bcc = [float(r['U0_bcc']) for r in artifact]
    except (KeyError, ValueError):
        return 0.0
    # endpoints should cover near 0 and 1
    if min(concs) > 0.1 or max(concs) < 0.9:
        return 0.0
    # sign condition: fcc > bcc at low c, fcc < bcc at high c
    low_idx = concs.index(min(concs))
    high_idx = concs.index(max(concs))
    if u0_fcc[low_idx] <= u0_bcc[low_idx] or u0_fcc[high_idx] >= u0_bcc[high_idx]:
        return 0.0
    # optional smoothness ceiling
    max_diff = 0.0
    for i in range(1, len(concs)):
        diff = abs(u0_fcc[i] - u0_fcc[i-1])
        if diff > max_diff: max_diff = diff
        diff = abs(u0_bcc[i] - u0_bcc[i-1])
        if diff > max_diff: max_diff = diff
    if max_diff > 10.0:
        return 0.0
    return 1.0


# === block: score_1 (check id='step2_v') ===
def score_1(artifact, step, ctx):
    # Check V2_beta / V1_beta ratio
    if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    try:
        v1_beta = [float(r['V1_beta']) for r in artifact]
        v2_beta = [float(r['V2_beta']) for r in artifact]
    except (KeyError, ValueError):
        return 0.0
    all_valid = True
    valid_count = 0
    for v1, v2 in zip(v1_beta, v2_beta):
        if v1 == 0:
            continue
        ratio = v2 / v1
        if ratio < 0.0 or ratio > 0.6667:
            all_valid = False
            break
        valid_count += 1
    if valid_count == 0:
        return 0.0
    return 1.0 if all_valid else 0.0


# === block: score_2 (check id='step3_phase') ===
def score_2(artifact, step, ctx):
    # Check phase diagram topology
    if not artifact or not isinstance(artifact, dict) or 'boundaries' not in artifact:
        return 0.0
    boundaries = artifact['boundaries']
    if not isinstance(boundaries, list):
        return 0.0
    required = step.get('params', {}).get('required_features', [])
    if not required:
        return 1.0
    # correct c_range for alpha_prime_L12 (paper shows L1_2 near 75% B)
    corrected_c_range = {'alpha_prime_L12': [0.7, 0.85]}
    def match_phases(bnd, phases_set):
        p1 = bnd.get('phase1', '').strip().lower()
        p2 = bnd.get('phase2', '').strip().lower()
        return set([p1, p2]) == set([phases_set[0].lower(), phases_set[1].lower()])
    points_by_feature = {f['name']: [] for f in required}
    for bnd in boundaries:
        for feat in required:
            if 'phases' not in feat:
                continue
            if match_phases(bnd, feat['phases']):
                # use corrected c_range for known features, else use the (already fixed) param
                c_range = corrected_c_range.get(feat['name'], feat.get('c_range'))
                for pt in bnd.get('points', []):
                    try:
                        T = float(pt.get('T', 0))
                        c = float(pt.get('c', 0))
                        if c_range:
                            lo, hi = c_range
                            if lo <= c <= hi:
                                points_by_feature[feat['name']].append((T, c))
                        else:
                            points_by_feature[feat['name']].append((T, c))
                    except (ValueError, TypeError):
                        pass
    score = 0.0
    num_features = 0
    for feat in required:
        name = feat['name']
        if name == 'high_temperature':
            max_T = 0.0
            for bnd in boundaries:
                for pt in bnd.get('points', []):
                    try:
                        T = float(pt.get('T', 0))
                        if T > max_T: max_T = T
                    except: pass
            if max_T >= feat.get('min_T', 0):
                score += 1.0
            num_features += 1
        else:
            pts = points_by_feature.get(name, [])
            min_pts = feat.get('min_points', 1)
            if len(pts) >= min_pts:
                score += 1.0
            num_features += 1
    if num_features == 0:
        return 1.0
    return score / num_features


_SCORERS = {
    'step1_u0': score_0,
    'step2_v': score_1,
    'step3_phase': score_2,
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
