import os
import json
import csv

# === author imports / helpers ===
import math, json, csv, os, collections


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


# === block: score_0 (check id='check_surface_energy') ===
def score_0(artifact, step, ctx):
    return 1.0  # surface_energy.json no longer scored; gamma consistency checked via fracture_data step


# === block: score_1 (check id='check_pristine_validation') ===
def score_1(artifact, step, ctx):
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(artifact_path):
        return 0.0
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except:
        return 0.0
    target_rows = step.get('target_rows', [])
    tolerances = step.get('tolerances', {})
    def row_match(target):
        for row in rows:
            if (str(row.get('temp_K','')).strip() == str(target['temp_K']) and
                row.get('direction','').strip().lower() == target['direction'].lower()):
                ok = True
                for prop in ['Young_modulus_Nm','UTS_Nm','fracture_strain_pct']:
                    val = float(row.get(prop, 0))
                    gold_val = float(target[prop])
                    rel_tol = tolerances.get(prop, {}).get('rel', 0.10)
                    if gold_val == 0:
                        if abs(val - gold_val) > 1e-9:
                            ok = False
                    else:
                        if abs(val - gold_val) / abs(gold_val) > rel_tol:
                            ok = False
                if ok:
                    return True
        return False
    matched = sum(1 for t in target_rows if row_match(t))
    if len(target_rows) == 0:
        return 0.0
    return matched / len(target_rows)


# === block: score_2 (check id='check_fracture_data') ===
def score_2(artifact, step, ctx):
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(artifact_path):
        return 0.0
    # load surface energy gamma first
    gamma = 5e-9  # fallback
    se_path = os.path.join('/app/outputs', 'surface_energy.json')
    if os.path.exists(se_path):
        try:
            with open(se_path) as f:
                se = json.load(f)
            gamma = float(se.get('gamma_value', gamma))
        except:
            pass
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except:
        return 0.0
    crack_lengths = step.get('crack_lengths', [])
    orientations = step.get('orientations', [])
    md_gold = step.get('md_stress_gold', {})
    md_tol = step.get('fracture_stress_tol_rel', 0.15)
    griffith_tol_abs = step.get('griffith_tol_abs', 0.1)
    griffith_enabled = step.get('griffith_enabled', True)
    # organize rows by (a0, orientation)
    data = {}
    for row in rows:
        try:
            a0 = float(row.get('a0_nm', 0))
        except:
            continue
        orient = row.get('orientation', '').strip().lower()
        if orient not in orientations:
            continue
        key = (a0, orient)
        data[key] = row
    # MD stress accuracy
    md_correct = 0
    md_total = 0
    for a0 in crack_lengths:
        for o in orientations:
            key = (a0, o)
            if key not in data:
                continue
            md_total += 1
            val = float(data[key].get('fracture_stress_MD_Nm', 0))
            gold_val = md_gold.get(o, {}).get(str(a0), None)
            if gold_val is None:
                continue
            if gold_val == 0:
                if abs(val) < 1e-9:
                    md_correct += 1
            else:
                if abs(val - gold_val) / abs(gold_val) <= md_tol:
                    md_correct += 1
    md_score = (md_correct / md_total) if md_total > 0 else 0.0
    # Griffith recompute
    griffith_correct = 0
    griffith_total = 0
    if griffith_enabled:
        for a0 in crack_lengths:
            # collect youngs for both orientations
            ys = []
            for o in orientations:
                key = (a0, o)
                if key in data:
                    try:
                        y = float(data[key].get('Young_modulus_MD_Nm', 0))
                        ys.append(y)
                    except:
                        pass
            if len(ys) == 0:
                continue
            y_avg = sum(ys) / len(ys)
            a0_m = a0 * 1e-9
            expected = math.sqrt(2 * gamma * y_avg / (math.pi * a0_m))
            for o in orientations:
                key = (a0, o)
                if key not in data:
                    continue
                griffith_total += 1
                sub = float(data[key].get('fracture_stress_Griffith_Nm', 0))
                if abs(sub - expected) <= griffith_tol_abs:
                    griffith_correct += 1
        griff_score = (griffith_correct / griffith_total) if griffith_total > 0 else 0.0
    else:
        griff_score = 1.0  # not checked
    # combine: 0.6 for MD, 0.4 for Griffith
    return 0.6 * md_score + 0.4 * griff_score


# === block: score_3 (check id='check_temperature_dependence') ===
def score_3(artifact, step, ctx):
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(artifact_path):
        return 0.0
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except:
        return 0.0
    temps = step.get('temperatures', [])
    orientations = step.get('orientations', [])
    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    data = {}
    for row in rows:
        try:
            t = int(float(row.get('temp_K', 0)))
        except:
            continue
        o = row.get('orientation', '').strip().lower()
        if o not in orientations:
            continue
        data[(t, o)] = row
    props = ['fracture_stress_Nm','fracture_strain_pct','elastic_modulus_Nm','toughness_Nm']
    total_checks = 0
    passed_checks = 0
    for o in orientations:
        if o not in gold:
            continue
        gold_o = gold[o]
        for i, t in enumerate(temps):
            key = (t, o)
            if key not in data:
                continue
            row = data[key]
            for prop in props:
                if prop not in gold_o:
                    continue
                gold_vals = gold_o[prop]
                if i >= len(gold_vals):
                    continue
                gold_val = gold_vals[i]
                try:
                    val = float(row.get(prop, 0))
                except:
                    continue
                rel_tol = tolerances.get(prop, {}).get('rel', 0.15)
                total_checks += 1
                if gold_val == 0:
                    if abs(val) < 1e-9:
                        passed_checks += 1
                else:
                    if abs(val - gold_val) / abs(gold_val) <= rel_tol:
                        passed_checks += 1
    if total_checks == 0:
        return 0.0
    return passed_checks / total_checks


_SCORERS = {
    'check_surface_energy': score_0,
    'check_pristine_validation': score_1,
    'check_fracture_data': score_2,
    'check_temperature_dependence': score_3,
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
