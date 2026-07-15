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


# === block: score_0 (check id='check_shape') ===
def score_0(artifact, step, ctx):
    required = ['K_Bi2Se3','K_Bi2S3','pK1','min_partial_pressures','K_R']
    if not all(k in artifact for k in required):
        return 0.0
    return 1.0


# === block: score_1 (check id='check_K_Bi2Se3') ===
def score_1(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    temps = list(gold.keys())
    actual = artifact.get('K_Bi2Se3')
    if not isinstance(actual, dict):
        return 0.0
    ok = 0
    for T in temps:
        v = actual.get(str(T))
        if v is None:
            continue
        try:
            vf = float(v)
        except:
            continue
        exp = gold[T]
        if abs(exp) < 1e-70:
            if abs(vf) < 1e-70:
                ok += 1
            continue
        rel = abs(vf - exp) / abs(exp)
        if rel <= tol:
            ok += 1
    return ok / len(temps) if temps else 0.0


# === block: score_2 (check id='check_K_Bi2S3') ===
def score_2(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    temps = list(gold.keys())
    actual = artifact.get('K_Bi2S3')
    if not isinstance(actual, dict):
        return 0.0
    ok = 0
    for T in temps:
        v = actual.get(str(T))
        if v is None:
            continue
        try:
            vf = float(v)
        except:
            continue
        exp = gold[T]
        if abs(exp) < 1e-70:
            if abs(vf) < 1e-70:
                ok += 1
            continue
        rel = abs(vf - exp) / abs(exp)
        if rel <= tol:
            ok += 1
    return ok / len(temps) if temps else 0.0


# === block: score_3 (check id='check_pK1') ===
def score_3(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    actual = artifact.get('pK1')
    if not isinstance(actual, list):
        return 0.0
    ok = 0
    N = len(gold)
    for exp_item in gold:
        found = [a for a in actual if a.get('x') == exp_item['x'] and a.get('T') == exp_item['T']]
        if not found:
            continue
        ag = found[0].get('pK1_value')
        if ag is None:
            continue
        try:
            ag_f = float(ag)
        except:
            continue
        exp = exp_item['pK1_value']
        if abs(exp) < 1e-12:
            if abs(ag_f) < 1e-12:
                ok += 1
            continue
        rel = abs(ag_f - exp) / abs(exp)
        if rel <= tol:
            ok += 1
    return ok / N if N else 0.0


# === block: score_4 (check id='check_min_partial') ===
def score_4(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    actual = artifact.get('min_partial_pressures')
    if not isinstance(actual, list):
        return 0.0
    ok = 0
    N = len(gold)
    for exp_item in gold:
        found = [a for a in actual if a.get('x') == exp_item['x']]
        if not found:
            continue
        ag_pS2 = found[0].get('pS2_min')
        ag_pSe2 = found[0].get('pSe2_min')
        if ag_pS2 is None or ag_pSe2 is None:
            continue
        try:
            ag_pS2_f = float(ag_pS2)
            ag_pSe2_f = float(ag_pSe2)
        except:
            continue
        expS2 = exp_item['pS2_min']
        expSe2 = exp_item['pSe2_min']
        if abs(expS2) < 1e-20 and abs(expSe2) < 1e-20:
            if abs(ag_pS2_f) < 1e-20 and abs(ag_pSe2_f) < 1e-20:
                ok += 1
            continue
        rel1 = abs(ag_pS2_f - expS2) / abs(expS2) if abs(expS2) > 1e-20 else 0
        rel2 = abs(ag_pSe2_f - expSe2) / abs(expSe2) if abs(expSe2) > 1e-20 else 0
        if rel1 <= tol and rel2 <= tol:
            ok += 1
    return ok / N if N else 0.0


# === block: score_5 (check id='check_K_R') ===
def score_5(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    actual = artifact.get('K_R')
    if not isinstance(actual, list):
        return 0.0
    ok = 0
    N = len(gold)
    for exp_item in gold:
        found = [a for a in actual if a.get('sample_no') == exp_item['sample_no'] and a.get('T2') == exp_item['T2']]
        if not found:
            continue
        ag_N = found[0].get('N')
        ag_KR = found[0].get('K_R')
        if ag_N is None or ag_KR is None:
            continue
        try:
            ag_N_f = float(ag_N)
            ag_KR_f = float(ag_KR)
        except:
            continue
        expN = exp_item['N']
        expKR = exp_item['K_R']
        if abs(expN) < 1e-40 and abs(expKR) < 1e-70:
            if abs(ag_N_f) < 1e-40 and abs(ag_KR_f) < 1e-70:
                ok += 1
            continue
        relN = abs(ag_N_f - expN) / abs(expN) if abs(expN) > 1e-40 else 0
        relKR = abs(ag_KR_f - expKR) / abs(expKR) if abs(expKR) > 1e-70 else 0
        if relN <= tol and relKR <= tol:
            ok += 1
    return ok / N if N else 0.0


_SCORERS = {
    'check_shape': score_0,
    'check_K_Bi2Se3': score_1,
    'check_K_Bi2S3': score_2,
    'check_pK1': score_3,
    'check_min_partial': score_4,
    'check_K_R': score_5,
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
