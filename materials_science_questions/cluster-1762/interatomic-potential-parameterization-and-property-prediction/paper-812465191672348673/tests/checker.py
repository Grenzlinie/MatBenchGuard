import os
import json
import csv

# === author imports / helpers ===
import json
import csv
import os

def load_json(path):
    with open(path) as f:
        return json.load(f)

def load_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


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
    outputs_dir = "/app/outputs"
    ctx = {}
    # lattice
    lat_path = os.path.join(outputs_dir, "lattice_constants.json")
    if os.path.exists(lat_path):
        ctx['lat'] = load_json(lat_path)
    else:
        ctx['lat'] = None

    # helper to find lambda for a target temp
    def get_lambda_around(rows, target, tolerance=5.0):
        for row in rows:
            try:
                t = float(row['Temperature'])
            except:
                continue
            if abs(t - target) <= tolerance:
                try:
                    return float(row['Lambda_c'])
                except:
                    return None
        return None

    # wurtzite
    wurtz_path = os.path.join(outputs_dir, "thermal_conductivity_wurtzite.csv")
    if os.path.exists(wurtz_path):
        wurtz_rows = load_csv(wurtz_path)
        ctx['lambda_wurtz_282'] = get_lambda_around(wurtz_rows, 282.0)
        ctx['lambda_wurtz_1130'] = get_lambda_around(wurtz_rows, 1130.0)
    else:
        ctx['lambda_wurtz_282'] = None
        ctx['lambda_wurtz_1130'] = None

    # vacancy
    vac_path = os.path.join(outputs_dir, "thermal_conductivity_vacancy.csv")
    if os.path.exists(vac_path):
        vac_rows = load_csv(vac_path)
        # find row with Defect containing 'Al' and temp near 298
        ctx['lambda_vac'] = None
        for row in vac_rows:
            if 'Al' in str(row.get('Defect','')):
                try:
                    t = float(row['Temperature'])
                except:
                    continue
                if 290 <= t <= 310:
                    try:
                        ctx['lambda_vac'] = float(row['Lambda_c'])
                        break
                    except:
                        pass
    else:
        ctx['lambda_vac'] = None

    # zincblende
    zb_path = os.path.join(outputs_dir, "thermal_conductivity_zincblende.csv")
    if os.path.exists(zb_path):
        zb_rows = load_csv(zb_path)
        ctx['lambda_zb'] = get_lambda_around(zb_rows, 268.0)
    else:
        ctx['lambda_zb'] = None

    return ctx


# === block: score_0 (check id='lattice_constants') ===
def score_0(artifact, step, ctx):
    import math

    if not isinstance(artifact, dict):
        return 0.0

    values = {
        'a': artifact.get('a'),
        'c': artifact.get('c'),
        'bulk_modulus': artifact.get('bulk_modulus')
    }
    gold = {'a': 3.06, 'c': 4.90, 'bulk_modulus': 2.08e11}

    # tolerances as specified in hidden grading spec: 5% for a,c; 10% for B
    tol = {'a': 0.05, 'c': 0.05, 'bulk_modulus': 0.10}

    scores = []
    for key in ['a', 'c', 'bulk_modulus']:
        v = values[key]
        g = gold[key]
        if v is None or g is None or g == 0:
            s = 0.0
        else:
            rel = abs(v - g) / g
            if rel <= tol[key]:
                s = 1.0
            elif rel <= 2 * tol[key]:
                s = 0.5
            else:
                s = 0.0
        scores.append(s)

    # enforce that c/a equals the experimental ratio used during fitting
    a = values['a']
    c = values['c']
    if a is not None and c is not None and a != 0:
        ratio = c / a
        expected_ratio = 1.601
        if abs(ratio - expected_ratio) <= 0.003:
            scores.append(1.0)
        else:
            scores.append(0.0)
    else:
        scores.append(0.0)

    return sum(scores) / len(scores)


# === block: score_1 (check id='wurtzite_thermal') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    target_gold = {282.0: 697.0, 1130.0: 34.2}
    tol = 0.30
    row_scores = []
    for t_target, gold in target_gold.items():
        row = None
        for r in artifact:
            try:
                t = float(r['Temperature'])
            except:
                continue
            if abs(t - t_target) <= 5.0:
                row = r
                break
        if row is None:
            row_scores.append(0.0)
            continue
        try:
            lam = float(row['Lambda_c'])
        except:
            row_scores.append(0.0)
            continue
        if gold > 0:
            rel_err = abs(lam - gold) / gold
            if rel_err <= tol:
                s = 1.0
            elif rel_err <= 2*tol:
                s = 0.5
            else:
                s = 0.0
        else:
            s = 1.0 if abs(lam - gold) < 1e-9 else 0.0
        row_scores.append(s)
    return sum(row_scores) / len(row_scores) if row_scores else 0.0


# === block: score_2 (check id='vacancy_thermal') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    gold = 8.3
    tol = 0.30
    for row in artifact:
        if 'Al' in str(row.get('Defect','')):
            try:
                t = float(row['Temperature'])
            except:
                continue
            if 290 <= t <= 310:
                try:
                    lam = float(row['Lambda_c'])
                except:
                    return 0.0
                if gold > 0:
                    rel_err = abs(lam - gold) / gold
                    if rel_err <= tol:
                        return 1.0
                    elif rel_err <= 2*tol:
                        return 0.5
                return 0.0
        # if no matching row found
        return 0.0
    return 0.0


# === block: score_3 (check id='zincblende_thermal') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    target_t = 268.0
    gold = 142.0
    tol = 0.30
    for row in artifact:
        try:
            t = float(row['Temperature'])
        except:
            continue
        if abs(t - target_t) <= 5.0:
            try:
                lam = float(row['Lambda_c'])
            except:
                return 0.0
            if gold > 0:
                rel_err = abs(lam - gold) / gold
                if rel_err <= tol:
                    return 1.0
                elif rel_err <= 2*tol:
                    return 0.5
            return 0.0
    return 0.0


# === block: score_4 (check id='ordering') ===
def score_4(artifact, step, ctx):
    l282 = ctx.get('lambda_wurtz_282')
    l1130 = ctx.get('lambda_wurtz_1130')
    lvac = ctx.get('lambda_vac')
    lzb = ctx.get('lambda_zb')
    checks = []
    # (condition, description) where condition is true => pass
    if l282 is not None and lzb is not None:
        checks.append(1.0 if lzb < l282 else 0.0)
    else:
        checks.append(0.0)
    if l282 is not None and lvac is not None:
        checks.append(1.0 if lvac < l282 else 0.0)
    else:
        checks.append(0.0)
    if l282 is not None and l1130 is not None:
        checks.append(1.0 if l1130 < l282 else 0.0)
    else:
        checks.append(0.0)
    if checks:
        return sum(checks)/len(checks)
    return 0.0


_SCORERS = {
    'lattice_constants': score_0,
    'wurtzite_thermal': score_1,
    'vacancy_thermal': score_2,
    'zincblende_thermal': score_3,
    'ordering': score_4,
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
