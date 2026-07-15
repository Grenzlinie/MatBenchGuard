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


# === block: score_0 (check id='hydrazine_tensors_scorer') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact; tol = step.get('config',{}).get('zero_tolerance',0.005); row = None
    max_a_xx = 0.0
    max_kappa_xx_Na = 0.0
    for r in artifact_rows:
        try:
            v = abs(float(r['a_xx']))
            if v > max_a_xx: max_a_xx = v
        except: pass
        try:
            v = abs(float(r['kappa_xx_Na']))
            if v > max_kappa_xx_Na: max_kappa_xx_Na = v
        except: pass
        try:
            p = float(r['phi_deg'])
            if abs(p - 90.0) < 1e-6:
                row = r
        except: pass
    if row is None or max_a_xx < 0.1 or max_kappa_xx_Na < 0.02:
        return 0.0
    checks = 0
    passed = 0
    def check_val(col, tol):
        try:
            return abs(float(row[col])) <= tol
        except:
            return False
    for col in ['a_xx','a_zz','a_bar']:
        checks += 1
        if check_val(col, tol):
            passed += 1
    for col in ['kappa_xx_Na','kappa_yy_Na','kappa_zz_Na','kappa_bar_Na']:
        checks += 1
        if check_val(col, tol):
            passed += 1
    for col in ['kappa_xx_355','kappa_yy_355','kappa_zz_355','kappa_bar_355']:
        checks += 1
        if check_val(col, tol):
            passed += 1
    try:
        a_xx = float(row['a_xx']); a_yy = float(row['a_yy']); a_zz = float(row['a_zz']);
        computed_a_bar = (a_xx + a_yy + a_zz)/3.0
        if abs(computed_a_bar - float(row['a_bar'])) < 1e-6:
            passed += 1
        checks += 1
    except: pass
    try:
        kxx = float(row['kappa_xx_Na']); kyy = float(row['kappa_yy_Na']); kzz = float(row['kappa_zz_Na']);
        computed_k_bar_Na = (kxx + kyy + kzz)/3.0
        if abs(computed_k_bar_Na - float(row['kappa_bar_Na'])) < 1e-6:
            passed += 1
        checks += 1
    except: pass
    try:
        kxx = float(row['kappa_xx_355']); kyy = float(row['kappa_yy_355']); kzz = float(row['kappa_zz_355']);
        computed_k_bar_355 = (kxx + kyy + kzz)/3.0
        if abs(computed_k_bar_355 - float(row['kappa_bar_355'])) < 1e-6:
            passed += 1
        checks += 1
    except: pass
    if checks == 0:
        return 0.0
    return passed / checks


# === block: score_1 (check id='boranylborane_tensors_scorer') ===
def score_1(artifact, step, ctx):
    tol_a_yy = step.get('config',{}).get('a_yy_tolerance',0.01); tol_kappa = step.get('config',{}).get('kappa_zero_tolerance',0.005); a_yy_max = 0.0; row_90 = None
    for r in artifact:
        try:
            p = float(r['phi_deg'])
        except:
            continue
        if 10 <= p <= 170:
            try:
                a_yy = abs(float(r['a_yy']))
                if a_yy > a_yy_max:
                    a_yy_max = a_yy
            except:
                pass
        if abs(p - 90.0) < 1e-6:
            row_90 = r
    a_yy_pass = 1.0 if a_yy_max <= tol_a_yy else 0.0
    kappa_pass = 1.0
    if row_90 is None:
        kappa_pass = 0.0
    else:
        for col in ['kappa_xx_Na','kappa_yy_Na','kappa_zz_Na','kappa_bar_Na','kappa_xx_355','kappa_yy_355','kappa_zz_355','kappa_bar_355']:
            try:
                if abs(float(row_90[col])) > tol_kappa:
                    kappa_pass = 0.0
                    break
            except:
                kappa_pass = 0.0
                break
    consistency_pass = 1.0
    if row_90 is not None:
        try:
            a_xx = float(row_90['a_xx']); a_yy = float(row_90['a_yy']); a_zz = float(row_90['a_zz'])
            if abs((a_xx+a_yy+a_zz)/3.0 - float(row_90['a_bar'])) > 1e-6:
                consistency_pass = 0.0
        except:
            consistency_pass = 0.0
        try:
            kxx = float(row_90['kappa_xx_Na']); kyy = float(row_90['kappa_yy_Na']); kzz = float(row_90['kappa_zz_Na'])
            if abs((kxx+kyy+kzz)/3.0 - float(row_90['kappa_bar_Na'])) > 1e-6:
                consistency_pass = 0.0
        except:
            consistency_pass = 0.0
        try:
            kxx = float(row_90['kappa_xx_355']); kyy = float(row_90['kappa_yy_355']); kzz = float(row_90['kappa_zz_355'])
            if abs((kxx+kyy+kzz)/3.0 - float(row_90['kappa_bar_355'])) > 1e-6:
                consistency_pass = 0.0
        except:
            consistency_pass = 0.0
    return a_yy_pass * 0.5 + kappa_pass * 0.4 + consistency_pass * 0.1


# === block: score_2 (check id='ethane_tensors_scorer') ===
def score_2(artifact, step, ctx):
    min_nonzero_tol = step.get('config',{}).get('min_nonzero_tol',0.001); phi_target = step.get('config',{}).get('phi_30_target',30.0); row_30 = None
    for r in artifact:
        try:
            p = float(r['phi_deg'])
            if abs(p - phi_target) < 1e-6:
                row_30 = r
                break
        except:
            pass
    spurious_zero_found = False
    for r in artifact:
        try:
            p = float(r['phi_deg'])
        except:
            continue
        if abs(p) < 1e-6 or abs(p - 60.0) < 1e-6:
            continue
        for col in ['a_xx','a_yy','a_zz','a_bar','kappa_xx_Na','kappa_yy_Na','kappa_zz_Na','kappa_bar_Na','kappa_xx_355','kappa_yy_355','kappa_zz_355','kappa_bar_355']:
            try:
                if abs(float(r[col])) <= min_nonzero_tol:
                    spurious_zero_found = True
                    break
            except:
                pass
        if spurious_zero_found:
            break
    no_spurious_zero_pass = 0.0 if spurious_zero_found else 1.0
    kappa_Na_nonzero_pass = 0.0
    if row_30 is not None:
        try:
            if abs(float(row_30['kappa_bar_Na'])) > min_nonzero_tol:
                kappa_Na_nonzero_pass = 1.0
        except:
            pass
    consistency_pass = 1.0
    if row_30 is not None:
        try:
            a_xx = float(row_30['a_xx']); a_yy = float(row_30['a_yy']); a_zz = float(row_30['a_zz'])
            if abs((a_xx+a_yy+a_zz)/3.0 - float(row_30['a_bar'])) > 1e-6:
                consistency_pass = 0.0
        except:
            consistency_pass = 0.0
        try:
            kxx = float(row_30['kappa_xx_Na']); kyy = float(row_30['kappa_yy_Na']); kzz = float(row_30['kappa_zz_Na'])
            if abs((kxx+kyy+kzz)/3.0 - float(row_30['kappa_bar_Na'])) > 1e-6:
                consistency_pass = 0.0
        except:
            consistency_pass = 0.0
        try:
            kxx = float(row_30['kappa_xx_355']); kyy = float(row_30['kappa_yy_355']); kzz = float(row_30['kappa_zz_355'])
            if abs((kxx+kyy+kzz)/3.0 - float(row_30['kappa_bar_355'])) > 1e-6:
                consistency_pass = 0.0
        except:
            consistency_pass = 0.0
    return no_spurious_zero_pass * 0.6 + kappa_Na_nonzero_pass * 0.3 + consistency_pass * 0.1


_SCORERS = {
    'hydrazine_tensors_scorer': score_0,
    'boranylborane_tensors_scorer': score_1,
    'ethane_tensors_scorer': score_2,
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
