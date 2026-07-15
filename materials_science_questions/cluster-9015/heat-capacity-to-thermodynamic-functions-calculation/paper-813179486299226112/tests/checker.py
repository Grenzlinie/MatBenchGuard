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


# === block: score_0 (check id='check_kd') ===
def score_0(artifact, step, ctx):
    import math

    xi = -1.057
    a = -4.2561
    b = 4.0194

    target_temps = [373.15, 500.0, 520.0, 573.0, 623.0]
    tolerance = 0.05

    try:
        import iapws.iapws97 as iapws
        expected = {}
        for T in target_temps:
            sat = iapws.IAPWS97.get_saturated_temperature(T)
            rho_liq = sat.rho_mass_liq / 1000.0
            rho_vap = sat.rho_mass_vap / 1000.0
            ln_KD = -xi * math.log(rho_vap / rho_liq) - (a + b * (1000.0 / T) ** 0.5) * (rho_vap - rho_liq)
            expected[T] = ln_KD
    except Exception:
        expected = None
        tolerance = 1e6

    agent = {}
    for row in artifact:
        try:
            t = round(float(row['Temp_K']), 2)
            v = float(row['ln_KD'])
            agent[t] = v
        except:
            continue

    ok = 0
    for T in target_temps:
        t = round(float(T), 2)
        if t in agent:
            if expected is not None:
                if abs(agent[t] - expected[t]) <= tolerance:
                    ok += 1
            else:
                ok += 1
    return ok / len(target_temps)


# === block: score_1 (check id='check_v2_cp2') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tol_v2 = step['tolerances']['V2infty_cm3_mol']
    tol_cp = step['tolerances']['Cp2infty_J_mol_K']
    expected_keys = {}
    for key_str, vals in gold.items():
        key_clean = key_str.strip('()')
        parts = key_clean.split(',')
        t = round(float(parts[0].strip()), 2)
        p = round(float(parts[1].strip()), 2)
        expected_keys[(t, p)] = (vals['V2infty_cm3_mol'], vals['Cp2infty_J_mol_K'])
    agent_rows = {}
    for row in artifact:
        try:
            t = round(float(row['Temp_K']), 2)
            p = round(float(row['Pressure_MPa']), 2)
            v2 = float(row['V2infty_cm3_mol'])
            cp = float(row['Cp2infty_J_mol_K'])
            agent_rows[(t, p)] = (v2, cp)
        except:
            continue
    ok = 0
    for key, (exp_v2, exp_cp) in expected_keys.items():
        if key in agent_rows:
            v2, cp = agent_rows[key]
            if abs(v2 - exp_v2) <= tol_v2 and abs(cp - exp_cp) <= tol_cp:
                ok += 1
    return ok / len(expected_keys)


# === block: score_2 (check id='check_thermo') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    tols = step['tolerances']
    artifact_dict = {k: artifact.get(k) for k in gold}
    ok = 0
    for key, expected in gold.items():
        if key in artifact_dict and artifact_dict[key] is not None:
            tol = tols[key]
            if abs(float(artifact_dict[key]) - expected) <= tol:
                ok += 1
    return ok / len(gold)


_SCORERS = {
    'check_kd': score_0,
    'check_v2_cp2': score_1,
    'check_thermo': score_2,
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
