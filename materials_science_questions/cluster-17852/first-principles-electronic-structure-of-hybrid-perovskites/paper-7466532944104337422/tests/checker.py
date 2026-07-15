import os
import json
import csv

# === author imports / helpers ===
import csv, math, json


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
    gold = json.loads(json.dumps(spec.get('gold', {})))
    return {'gold': gold, 'tol_E': 0.01, 'tol_g': 0.05}


# === block: score_0 (check id='score_g_factors') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or not all(col in rows[0] for col in ['n','E_eff','E_exc','g_e_ab','g_e_c','g_h_ab','g_h_c']):
        return 0.0
    gold = ctx['gold']
    tol_E = ctx['tol_E']
    tol_g = ctx['tol_g']
    score_sum = 0.0
    count = 0
    for row in rows:
        try:
            n = int(row['n'])
        except:
            continue
        if n < 1 or n > 8:
            continue
        gold_row = gold.get(str(n))
        if gold_row is None:
            continue
        # energy scores
        try:
            diff_E_eff = abs(float(row['E_eff']) - gold_row['E_eff'])
            if diff_E_eff <= tol_E:
                s_E_eff = 1.0
            else:
                s_E_eff = max(0.0, 1.0 - (diff_E_eff - tol_E) / tol_E)
        except:
            s_E_eff = 0.0
        try:
            diff_E_exc = abs(float(row['E_exc']) - gold_row['E_exc'])
            if diff_E_exc <= tol_E:
                s_E_exc = 1.0
            else:
                s_E_exc = max(0.0, 1.0 - (diff_E_exc - tol_E) / tol_E)
        except:
            s_E_exc = 0.0
        # g-factor scores
        try:
            diff_g_e_ab = abs(float(row['g_e_ab']) - gold_row['g_e_ab'])
            if diff_g_e_ab <= tol_g:
                s_g_e_ab = 1.0
            else:
                s_g_e_ab = max(0.0, 1.0 - (diff_g_e_ab - tol_g) / tol_g)
        except:
            s_g_e_ab = 0.0
        try:
            diff_g_e_c = abs(float(row['g_e_c']) - gold_row['g_e_c'])
            if diff_g_e_c <= tol_g:
                s_g_e_c = 1.0
            else:
                s_g_e_c = max(0.0, 1.0 - (diff_g_e_c - tol_g) / tol_g)
        except:
            s_g_e_c = 0.0
        try:
            diff_g_h_ab = abs(float(row['g_h_ab']) - gold_row['g_h_ab'])
            if diff_g_h_ab <= tol_g:
                s_g_h_ab = 1.0
            else:
                s_g_h_ab = max(0.0, 1.0 - (diff_g_h_ab - tol_g) / tol_g)
        except:
            s_g_h_ab = 0.0
        try:
            diff_g_h_c = abs(float(row['g_h_c']) - gold_row['g_h_c'])
            if diff_g_h_c <= tol_g:
                s_g_h_c = 1.0
            else:
                s_g_h_c = max(0.0, 1.0 - (diff_g_h_c - tol_g) / tol_g)
        except:
            s_g_h_c = 0.0
        # structural check
        try:
            struct = 1.0 if (float(row['g_e_c']) > float(row['g_e_ab']) and float(row['g_h_c']) < float(row['g_h_ab'])) else 0.0
        except:
            struct = 0.0
        row_score = (s_E_eff + s_E_exc + s_g_e_ab + s_g_e_c + s_g_h_ab + s_g_h_c + struct) / 7.0
        score_sum += row_score
        count += 1
    if count == 0:
        return 0.0
    return score_sum / count


_SCORERS = {
    'score_g_factors': score_0,
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
