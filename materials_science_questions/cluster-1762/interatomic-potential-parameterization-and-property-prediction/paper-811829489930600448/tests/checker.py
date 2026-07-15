import os
import json
import csv


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


# === block: score_0 (check id='lattice_check') ===
def score_0(artifact, step, ctx):
    # lattice_check: compare lattice parameters
    if not isinstance(artifact, dict):
        return 0.0
    expected = step.get("expected", {})
    tolerances = step.get("tolerances", {})
    poly_list = ["monoclinic", "orthorhombic"]
    correct = 0
    total = 0
    for poly in poly_list:
        if poly not in expected or poly not in artifact:
            continue
        exp_poly = expected[poly]
        art_poly = artifact[poly]
        if not isinstance(art_poly, dict):
            continue
        for key, exp_val in exp_poly.items():
            total += 1
            tol = tolerances.get(key, 0.0)
            val = art_poly.get(key)
            if val is not None and isinstance(val, (int, float)) and abs(val - exp_val) <= tol:
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='intrinsic_defect_check') ===
def score_1(artifact, step, ctx):
    # intrinsic_defect_check: numeric comparison + trend checks
    if not isinstance(artifact, dict):
        return 0.0
    expected = step.get("expected", {})
    tolerances = step.get("tolerances", {})
    nw = step.get("numeric_weight", 0.85)
    tw = step.get("trend_weight", 0.15)
    correct = 0
    total = 0
    # numeric
    for poly in ["monoclinic", "orthorhombic"]:
        if poly not in expected or poly not in artifact:
            continue
        exp_poly = expected[poly]
        art_poly = artifact[poly]
        if not isinstance(art_poly, dict):
            continue
        for key, exp_val in exp_poly.items():
            total += 1
            tol = tolerances.get(key, 0.0)
            val = art_poly.get(key)
            if val is not None and isinstance(val, (int, float)) and abs(val - exp_val) <= tol:
                correct += 1
    numeric_score = correct / total if total > 0 else 0.0
    # trend checks
    trends = []
    try:
        if artifact["monoclinic"]["LiMn_antisite"] < artifact["monoclinic"]["Li_Frenkel"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    try:
        if artifact["orthorhombic"]["LiMn_antisite"] < artifact["orthorhombic"]["Li_Frenkel"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    trend_score = sum(trends) / len(trends) if trends else 0.0
    return nw * numeric_score + tw * trend_score


# === block: score_2 (check id='migration_check') ===
def score_2(artifact, step, ctx):
    # migration_check: numeric + trend checks
    if not isinstance(artifact, dict):
        return 0.0
    expected = step.get("expected", {})
    tolerances = step.get("tolerances", {})
    nw = step.get("numeric_weight", 0.7)
    tw = step.get("trend_weight", 0.3)
    correct = 0
    total = 0
    for poly in ["monoclinic", "orthorhombic"]:
        if poly not in expected or poly not in artifact:
            continue
        exp_poly = expected[poly]
        art_poly = artifact[poly]
        if not isinstance(art_poly, dict):
            continue
        for key, exp_val in exp_poly.items():
            total += 1
            tol = tolerances.get(key, 0.0)
            val = art_poly.get(key)
            if val is not None and isinstance(val, (int, float)) and abs(val - exp_val) <= tol:
                correct += 1
    numeric_score = correct / total if total > 0 else 0.0
    # trend checks
    trends = []
    try:
        mono = artifact["monoclinic"]
        # path_B <= path_A
        if mono["path_B"] <= mono["path_A"]:
            trends.append(True)
        else:
            trends.append(False)
        # path_D < path_C
        if mono["path_D"] < mono["path_C"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
        trends.append(False)
    try:
        ortho = artifact["orthorhombic"]
        if ortho["path_X"] < ortho["path_Y"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    # monoclinic min barrier < orthorhombic min barrier
    try:
        mono_min = min(artifact["monoclinic"][k] for k in ["path_A","path_B","path_C","path_D"])
        ortho_min = min(artifact["orthorhombic"][k] for k in ["path_X","path_Y"])
        if mono_min < ortho_min:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    trend_score = sum(trends) / len(trends) if trends else 0.0
    return nw * numeric_score + tw * trend_score


# === block: score_3 (check id='dopant_check') ===
def score_3(artifact, step, ctx):
    # dopant_check: numeric + trend checks
    if not isinstance(artifact, dict):
        return 0.0
    expected = step.get("expected", {})
    tolerances = step.get("tolerances", {})
    nw = step.get("numeric_weight", 0.75)
    tw = step.get("trend_weight", 0.25)
    correct = 0
    total = 0
    # numeric
    for poly in ["monoclinic", "orthorhombic"]:
        if poly not in expected or poly not in artifact:
            continue
        exp_poly = expected[poly]
        art_poly = artifact[poly]
        if not isinstance(art_poly, dict):
            continue
        for dopant in ["Al", "Ga"]:
            if dopant not in exp_poly or dopant not in art_poly:
                continue
            exp_dop = exp_poly[dopant]
            art_dop = art_poly[dopant]
            if not isinstance(art_dop, dict):
                continue
            for site in ["Li_site", "Mn_site", "Si_site"]:
                total += 1
                tol = tolerances.get(site, 0.0)
                val = art_dop.get(site)
                exp_val = exp_dop.get(site)
                if val is not None and isinstance(val, (int, float)) and exp_val is not None and abs(val - exp_val) <= tol:
                    correct += 1
    numeric_score = correct / total if total > 0 else 0.0
    # trend checks
    trends = []
    try:
        # Al Si < Ga Si monoclinic
        if artifact["monoclinic"]["Al"]["Si_site"] < artifact["monoclinic"]["Ga"]["Si_site"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    try:
        if artifact["orthorhombic"]["Al"]["Si_site"] < artifact["orthorhombic"]["Ga"]["Si_site"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    try:
        if artifact["monoclinic"]["Al"]["Mn_site"] < artifact["monoclinic"]["Al"]["Li_site"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    try:
        if artifact["orthorhombic"]["Al"]["Mn_site"] < artifact["orthorhombic"]["Al"]["Li_site"]:
            trends.append(True)
        else:
            trends.append(False)
    except:
        trends.append(False)
    trend_score = sum(trends) / len(trends) if trends else 0.0
    return nw * numeric_score + tw * trend_score


_SCORERS = {
    'lattice_check': score_0,
    'intrinsic_defect_check': score_1,
    'migration_check': score_2,
    'dopant_check': score_3,
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
