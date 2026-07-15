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


# === block: score_0 (check id='baseline_properties') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get('gold', {}).get('rows', [])
    tolerances = step.get('tolerances', {})
    numeric_scores = []
    pristine_zz = None
    pristine_am = None
    field_map = {'E': 'youngs_modulus_GPa', 'tau': 'ultimate_tensile_strength_GPa', 'delta': 'critical_failure_strain_pct'}
    tol_map = {'E': 'E_tol', 'tau': 'tau_tol', 'delta': 'delta_tol'}

    for g in gold_rows:
        art = None
        for r in artifact:
            if r.get('model', '').strip() == g['model'] and r.get('direction', '').strip() == g['direction']:
                art = r
                break
        if art is None:
            numeric_scores.extend([0.0, 0.0, 0.0])
            continue
        if g['model'] == 'pristine_hBN':
            try:
                vals = {}
                for k in ['E', 'tau', 'delta']:
                    vals[k] = float(art[field_map[k]])
                if g['direction'] == 'zz':
                    pristine_zz = vals
                else:
                    pristine_am = vals
            except (ValueError, KeyError, TypeError):
                pass
        for field in ['E', 'tau', 'delta']:
            gold_val = g[field]
            tol = tolerances.get(tol_map[field], 0.10)
            try:
                art_val = float(art.get(field_map[field], 0))
            except (ValueError, TypeError):
                numeric_scores.append(0.0)
                continue
            if abs(gold_val) < 1e-9:
                fs = 1.0 if abs(art_val) < 1e-6 else 0.0
            else:
                rel = abs(art_val - gold_val) / abs(gold_val)
                if rel <= tol:
                    fs = 1.0
                else:
                    fs = max(0.0, 1.0 - (rel - tol) / tol)
            numeric_scores.append(fs)

    numeric_avg = sum(numeric_scores) / len(numeric_scores) if numeric_scores else 0.0

    trend_checks = []
    if pristine_zz is not None and pristine_am is not None:
        for k in ['E', 'tau', 'delta']:
            trend_checks.append(1.0 if pristine_zz[k] > pristine_am[k] else 0.0)
    if pristine_zz is not None:
        for g in gold_rows:
            if g['model'].startswith('GB_'):
                art = None
                for r in artifact:
                    if r.get('model', '').strip() == g['model'] and r.get('direction', '').strip() == g['direction']:
                        art = r
                        break
                if art is not None:
                    try:
                        at = float(art.get('ultimate_tensile_strength_GPa', 1e12))
                        trend_checks.append(1.0 if at < pristine_zz['tau'] else 0.0)
                    except (ValueError, TypeError):
                        trend_checks.append(0.0)

    trend_avg = sum(trend_checks) / len(trend_checks) if trend_checks else 0.0
    return 0.7 * numeric_avg + 0.3 * trend_avg


# === block: score_1 (check id='strain_rate_effect') ===
def score_1(artifact, step, ctx):
    gold_uts = step.get('gold', {}).get('uts_by_rate', {})
    tau_tol = step.get('tolerances', {}).get('tau_tol', 0.12)

    uts_values = {}
    for row in artifact:
        try:
            rate = str(row.get('strain_rate_s-1', '')).strip()
            uts = float(row.get('ultimate_tensile_strength_GPa', 0))
            uts_values[rate] = uts
        except (ValueError, TypeError):
            continue

    numeric_scores = []
    for rate_str, gold_val in gold_uts.items():
        if rate_str not in uts_values:
            numeric_scores.append(0.0)
            continue
        art_val = uts_values[rate_str]
        if abs(gold_val) < 1e-9:
            fs = 1.0 if abs(art_val) < 1e-6 else 0.0
        else:
            rel = abs(art_val - gold_val) / abs(gold_val)
            if rel <= tau_tol:
                fs = 1.0
            else:
                fs = max(0.0, 1.0 - (rel - tau_tol) / tau_tol)
        numeric_scores.append(fs)

    numeric_avg = sum(numeric_scores) / len(numeric_scores) if numeric_scores else 0.0

    rates_order = ['1e8', '1e9', '1e10']
    if all(r in uts_values for r in rates_order):
        v8, v9, v10 = uts_values['1e8'], uts_values['1e9'], uts_values['1e10']
        if v8 < v9 < v10:
            trend_score = 1.0
        elif v8 < v10:
            trend_score = 0.5
        else:
            trend_score = 0.0
    else:
        trend_score = 0.0

    return 0.5 * numeric_avg + 0.5 * trend_score


# === block: score_2 (check id='temperature_effect') ===
def score_2(artifact, step, ctx):
    gold_uts = step.get('gold', {}).get('uts_by_temp', {})
    tau_tol = step.get('tolerances', {}).get('tau_tol', 0.12)

    uts_values = {}
    for row in artifact:
        try:
            temp = str(row.get('temperature_K', '')).strip()
            uts = float(row.get('ultimate_tensile_strength_GPa', 0))
            uts_values[temp] = uts
        except (ValueError, TypeError):
            continue

    numeric_scores = []
    for temp_str, gold_val in gold_uts.items():
        if temp_str not in uts_values:
            numeric_scores.append(0.0)
            continue
        art_val = uts_values[temp_str]
        if abs(gold_val) < 1e-9:
            fs = 1.0 if abs(art_val) < 1e-6 else 0.0
        else:
            rel = abs(art_val - gold_val) / abs(gold_val)
            if rel <= tau_tol:
                fs = 1.0
            else:
                fs = max(0.0, 1.0 - (rel - tau_tol) / tau_tol)
        numeric_scores.append(fs)

    numeric_avg = sum(numeric_scores) / len(numeric_scores) if numeric_scores else 0.0

    temps_order = ['1', '300', '1100']
    if all(t in uts_values for t in temps_order):
        v1, v300, v1100 = uts_values['1'], uts_values['300'], uts_values['1100']
        if v1 > v300 > v1100:
            trend_score = 1.0
        elif v1 > v1100:
            trend_score = 0.5
        else:
            trend_score = 0.0
    else:
        trend_score = 0.0

    return 0.5 * numeric_avg + 0.5 * trend_score


_SCORERS = {
    'baseline_properties': score_0,
    'strain_rate_effect': score_1,
    'temperature_effect': score_2,
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
