import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os


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
    import json, os, csv
    outputs_dir = os.environ.get('OUTPUTS_DIR','/app/outputs')
    spec_path = '/tests/grading_spec.json'
    with open(spec_path) as f:
        spec = json.load(f)

    gold_step01 = None
    gold_step02 = None
    gold_step04 = None
    for step in spec['steps']:
        if step['id'] == 'step_01':
            gold_step01 = step['target']
        elif step['id'] == 'step_02':
            gold_step02 = step['target']
        elif step['id'] == 'step_04':
            gold_step04 = step['target']

    step04_path = os.path.join(outputs_dir, 'step_04_reaction_rates.csv')
    step04_rows = []
    if os.path.exists(step04_path):
        with open(step04_path, newline='') as f:
            reader = csv.DictReader(f)
            step04_rows = list(reader)

    return {
        'gold_step01': gold_step01,
        'gold_step02': gold_step02,
        'gold_step04': gold_step04,
        'step04_rows': step04_rows
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_step01']
    if not gold:
        return 0.0
    tol_dE = step.get('tolerance', {}).get('deltaE', 0.05)
    tol_Ea = step.get('tolerance', {}).get('Ea', 0.1)
    reactions = ['R1','R2','R3','R4','R5','R6','R7','R8','R9']
    score = 0.0
    n = 0
    for r in reactions:
        if r not in artifact or r not in gold:
            continue
        ag = artifact[r]
        gd = gold[r]
        for field, tol in [('ΔE', tol_dE), ('Ef', tol_Ea), ('Eb', tol_Ea)]:
            val_ag = ag.get(field)
            val_gd = gd.get(field)
            if val_ag is not None and val_gd is not None:
                if abs(float(val_ag) - float(val_gd)) <= tol:
                    score += 1.0
                n += 1
    return score / n if n > 0 else 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold = ctx['gold_step02']
    if not gold:
        return 0.0
    reactions = ['R1','R2','R3','R4','R5','R6','R7','R8','R9']
    score = 0.0
    n = 0
    log_tol = step.get('log_tolerance', 1.0)
    for r in reactions:
        if r not in artifact or r not in gold:
            continue
        ag = artifact[r]
        gd = gold[r]
        for field in ['Af','Ab']:
            a = ag.get(field)
            b = gd.get(field)
            if a is not None and b is not None:
                a = float(a)
                b = float(b)
                if abs(b) < 1e-12:
                    # gold is zero
                    if abs(a) < 1e-10:
                        score += 1.0
                else:
                    try:
                        diff = abs(math.log10(a / b))
                    except (ValueError, ZeroDivisionError):
                        diff = 100
                    if diff <= log_tol:
                        score += 1.0
                    elif diff <= 2 * log_tol:
                        score += max(0.0, 1.0 - (diff - log_tol) / log_tol)
                n += 1
    return score / n if n > 0 else 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    text = artifact if isinstance(artifact, str) else ''
    score = 0.0
    # Keywords for pathway and RDS
    has_dissociative = 'dissociative' in text.lower()
    has_r5 = 'r5' in text.lower() and ('rate-determining' in text.lower() or 'rds' in text.lower())
    pathway_stated = has_dissociative and has_r5
    score += 0.5 if pathway_stated else 0.0

    # Cross-check with step_04 rates: R6 > R9
    rows = ctx.get('step04_rows', [])
    r6_gt_r9 = True
    for T in ['450','475','500']:
        r6_f = None
        r9_f = None
        for row in rows:
            if row.get('Temperature (K)','').strip() == T:
                rxn = row.get('Reaction_number','').strip()
                if rxn == 'R6':
                    try:
                        r6_f = float(row['r_f (s⁻¹)'])
                    except:
                        pass
                elif rxn == 'R9':
                    try:
                        r9_f = float(row['r_f (s⁻¹)'])
                    except:
                        pass
        if r6_f is None or r9_f is None:
            r6_gt_r9 = False
            break
        if r6_f <= r9_f:
            r6_gt_r9 = False
            break
    score += 0.5 if r6_gt_r9 else 0.0
    return score


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    gold = ctx.get('gold_step04', {})
    if not gold:
        return 0.0
    rows = artifact
    score_val = 0.0
    n_val = 0
    factor_tol = step.get('factor_tolerance', 10.0)
    max_log_diff = math.log10(factor_tol)

    # Build list of (T_str, rxn) and gold pairs
    for row in rows:
        T = row.get('Temperature (K)','').strip()
        rxn = row.get('Reaction_number','').strip()
        if not T or not rxn:
            continue
        try:
            rf = float(row.get('r_f (s⁻¹)', '0'))
            rb = float(row.get('r_b (s⁻¹)', '0'))
        except ValueError:
            continue
        # gold lookup
        if T not in gold or rxn not in gold[T]:
            continue
        grf, grb = gold[T][rxn]
        try:
            grf = float(grf)
            grb = float(grb)
        except:
            continue
        # forward tolerance
        if abs(grf) < 1e-12:
            rf_ok = abs(rf) < 1e-10
        else:
            try:
                diff = abs(math.log10(rf / grf))
            except:
                diff = 100
            rf_ok = diff <= max_log_diff
        # backward tolerance
        if abs(grb) < 1e-12:
            rb_ok = abs(rb) < 1e-10
        else:
            try:
                diff = abs(math.log10(rb / grb))
            except:
                diff = 100
            rb_ok = diff <= max_log_diff
        score_val += (1.0 if rf_ok else 0.0)
        score_val += (1.0 if rb_ok else 0.0)
        n_val += 2

    # Relative ordering checks
    temps = set()
    for row in rows:
        T = row.get('Temperature (K)','').strip()
        if T.isdigit():
            temps.add(T)
    ordering_checks = 0
    ordering_passed = 0
    for T in temps:
        rates = {}
        for row in rows:
            if row.get('Temperature (K)','').strip() == T:
                rxn = row.get('Reaction_number','').strip()
                try:
                    rf = float(row.get('r_f (s⁻¹)', '0'))
                    rb = float(row.get('r_b (s⁻¹)', '0'))
                except:
                    continue
                rates[rxn] = (rf, rb)
        # R6 forward > R9 forward
        if 'R6' in rates and 'R9' in rates:
            ordering_checks += 1
            if rates['R6'][0] > rates['R9'][0]:
                ordering_passed += 1
        # R5 forward < R2 forward
        if 'R2' in rates and 'R5' in rates:
            ordering_checks += 1
            if rates['R5'][0] < rates['R2'][0]:
                ordering_passed += 1
        # R5 forward < R6 forward
        if 'R5' in rates and 'R6' in rates:
            ordering_checks += 1
            if rates['R5'][0] < rates['R6'][0]:
                ordering_passed += 1
        # R3 backward must be zero
        if 'R3' in rates:
            ordering_checks += 1
            if abs(rates['R3'][1]) < 1e-10:
                ordering_passed += 1
        # R9 backward must be zero
        if 'R9' in rates:
            ordering_checks += 1
            if abs(rates['R9'][1]) < 1e-10:
                ordering_passed += 1

    val_fraction = score_val / n_val if n_val > 0 else 0.0
    order_fraction = ordering_passed / ordering_checks if ordering_checks > 0 else 1.0
    return 0.8 * val_fraction + 0.2 * order_fraction


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
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
