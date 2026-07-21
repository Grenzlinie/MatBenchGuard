import os
import json
import csv

# === author imports / helpers ===
import os
import json

def _get_value(dft, site, metric):
    if site not in dft:
        return None
    entry = dft[site]
    if not isinstance(entry, dict):
        return None
    return entry.get(metric)

def check_numeric(dft, site, metric, expected, tol):
    val = _get_value(dft, site, metric)
    if val is None:
        return 0.0
    try:
        diff = abs(float(val) - expected)
        return 1.0 if diff <= tol else 0.0
    except (TypeError, ValueError):
        return 0.0

def check_rule(dft, rule_id):
    try:
        be_atop_210 = float(dft['Ir210_atop']['binding_energy_eV'])
        be_bridge_210 = float(dft['Ir210_bridge']['binding_energy_eV'])
        be_atop_110 = float(dft['Ir110_atop']['binding_energy_eV'])
        be_bridge_110 = float(dft['Ir110_bridge']['binding_energy_eV'])
        be_atop_311 = float(dft['Ir311_atop']['binding_energy_eV'])
        be_bridge_311 = float(dft['Ir311_bridge']['binding_energy_eV'])
        freq_atop_210 = float(dft['Ir210_atop']['frequency_cm-1'])
        freq_bridge_210 = float(dft['Ir210_bridge']['frequency_cm-1'])
        freq_atop_110 = float(dft['Ir110_atop']['frequency_cm-1'])
        freq_bridge_110 = float(dft['Ir110_bridge']['frequency_cm-1'])
        freq_atop_311 = float(dft['Ir311_atop']['frequency_cm-1'])
        freq_bridge_311 = float(dft['Ir311_bridge']['frequency_cm-1'])
    except (KeyError, TypeError, ValueError):
        return 0.0

    if rule_id == 'rule_a':
        return 1.0 if be_atop_210 > be_bridge_210 else 0.0
    elif rule_id == 'rule_b':
        return 1.0 if abs(be_atop_110 - be_bridge_110) <= 0.2 else 0.0
    elif rule_id == 'rule_c':
        return 1.0 if be_bridge_311 > be_atop_311 else 0.0
    elif rule_id == 'rule_d_210':
        return 1.0 if freq_atop_210 > freq_bridge_210 else 0.0
    elif rule_id == 'rule_d_110':
        return 1.0 if freq_atop_110 > freq_bridge_110 else 0.0
    elif rule_id == 'rule_d_311':
        return 1.0 if freq_atop_311 > freq_bridge_311 else 0.0
    return 0.0


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
    dft_path = os.path.join(outputs_dir, 'dft_results.json')
    dft = {}
    if os.path.exists(dft_path):
        with open(dft_path) as f:
            dft = json.load(f)
    return {'dft': dft}


# === block: score_0 (check id='ir210_atop_be') ===
def score_0(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 0.5)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'binding_energy_eV', expected, tol)


# === block: score_1 (check id='ir210_atop_freq') ===
def score_1(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 100)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'frequency_cm-1', expected, tol)


# === block: score_2 (check id='ir210_bridge_be') ===
def score_2(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 0.5)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'binding_energy_eV', expected, tol)


# === block: score_17 (check id='ir210_bridge_freq') ===
def score_17(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 100)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'frequency_cm-1', expected, tol)


# === block: score_3 (check id='ir110_atop_be') ===
def score_3(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 0.5)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'binding_energy_eV', expected, tol)


# === block: score_4 (check id='ir110_atop_freq') ===
def score_4(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 100)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'frequency_cm-1', expected, tol)


# === block: score_5 (check id='ir110_bridge_be') ===
def score_5(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 0.5)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'binding_energy_eV', expected, tol)


# === block: score_6 (check id='ir110_bridge_freq') ===
def score_6(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 100)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'frequency_cm-1', expected, tol)


# === block: score_7 (check id='ir311_atop_be') ===
def score_7(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 0.5)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'binding_energy_eV', expected, tol)


# === block: score_8 (check id='ir311_atop_freq') ===
def score_8(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 100)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'frequency_cm-1', expected, tol)


# === block: score_9 (check id='ir311_bridge_be') ===
def score_9(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 0.5)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'binding_energy_eV', expected, tol)


# === block: score_10 (check id='ir311_bridge_freq') ===
def score_10(artifact, step, ctx):
    step_info = step
    site = step_info.get('surface_site', '')
    expected = step_info.get('expected', None)
    tol = step_info.get('tolerance', 100)
    dft = ctx.get('dft', {})
    return check_numeric(dft, site, 'frequency_cm-1', expected, tol)


# === block: score_11 (check id='rule_a') ===
def score_11(artifact, step, ctx):
    dft = ctx.get('dft', {})
    return check_rule(dft, 'rule_a')


# === block: score_12 (check id='rule_b') ===
def score_12(artifact, step, ctx):
    dft = ctx.get('dft', {})
    return check_rule(dft, 'rule_b')


# === block: score_13 (check id='rule_c') ===
def score_13(artifact, step, ctx):
    dft = ctx.get('dft', {})
    return check_rule(dft, 'rule_c')


# === block: score_14 (check id='rule_d_210') ===
def score_14(artifact, step, ctx):
    dft = ctx.get('dft', {})
    return check_rule(dft, 'rule_d_210')


# === block: score_15 (check id='rule_d_110') ===
def score_15(artifact, step, ctx):
    dft = ctx.get('dft', {})
    return check_rule(dft, 'rule_d_110')


# === block: score_16 (check id='rule_d_311') ===
def score_16(artifact, step, ctx):
    dft = ctx.get('dft', {})
    return check_rule(dft, 'rule_d_311')


_SCORERS = {
    'ir210_atop_be': score_0,
    'ir210_atop_freq': score_1,
    'ir210_bridge_be': score_2,
    'ir210_bridge_freq': score_17,
    'ir110_atop_be': score_3,
    'ir110_atop_freq': score_4,
    'ir110_bridge_be': score_5,
    'ir110_bridge_freq': score_6,
    'ir311_atop_be': score_7,
    'ir311_atop_freq': score_8,
    'ir311_bridge_be': score_9,
    'ir311_bridge_freq': score_10,
    'rule_a': score_11,
    'rule_b': score_12,
    'rule_c': score_13,
    'rule_d_210': score_14,
    'rule_d_110': score_15,
    'rule_d_311': score_16,
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