import os
import json
import csv

# === author imports / helpers ===
from collections import defaultdict


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


# === block: score_0 (check id='s02') ===
def score_0(artifact, step, ctx):
    data = {}
    for row in artifact:
        sys = row.get('system', '')
        data[sys] = row
    required = ['pristine', 'V_BrS', 'V']
    if not all(s in data for s in required):
        return 0.0
    try:
        e_vals = {s: float(data[s]['E_ads']) for s in required}
        q_vals = {s: float(data[s]['Bader_charge_on_CO2']) for s in required}
    except (ValueError, KeyError):
        return 0.0
    order_e = e_vals['V'] <= e_vals['V_BrS'] <= e_vals['pristine']
    order_q = q_vals['V'] >= q_vals['V_BrS'] >= q_vals['pristine']
    score_total = 0.0
    if order_e:
        score_total += 0.3
    if order_q:
        score_total += 0.2
    targets = step.get('targets', {})
    e_tol = targets.get('E_ads', {}).get('tolerance', 0.15)
    e_target_pristine = targets.get('E_ads', {}).get('pristine', -2.63)
    e_target_V = targets.get('E_ads', {}).get('V', -2.73)
    q_tol = targets.get('Bader_charge_on_CO2', {}).get('tolerance', 0.1)
    q_target_pristine = targets.get('Bader_charge_on_CO2', {}).get('pristine', 0.46)
    q_target_V = targets.get('Bader_charge_on_CO2', {}).get('V', 1.22)

    # threshold_or_better for V surface: more negative E_ads, higher Bader charge is better
    if e_vals['V'] <= e_target_V:
        score_total += 0.15
    else:
        dev = e_vals['V'] - e_target_V  # positive when less negative (worse)
        if dev <= e_tol:
            score_total += 0.15
        elif dev <= 2 * e_tol:
            score_total += 0.075

    if q_vals['V'] >= q_target_V:
        score_total += 0.15
    else:
        dev = q_target_V - q_vals['V']  # positive when lower (worse)
        if dev <= q_tol:
            score_total += 0.15
        elif dev <= 2 * q_tol:
            score_total += 0.075

    # pristine: symmetric closeness (no "better" direction)
    def closeness(val, targ, tol):
        dev = abs(val - targ)
        if dev <= tol:
            return 1.0
        elif dev <= 2 * tol:
            return 0.5
        return 0.0

    score_total += 0.1 * closeness(e_vals['pristine'], e_target_pristine, e_tol)
    score_total += 0.1 * closeness(q_vals['pristine'], q_target_pristine, q_tol)

    return min(score_total, 1.0)


# === block: score_1 (check id='s03') ===
def score_1(artifact, step, ctx):
    data_by_sys = defaultdict(dict)
    for row in artifact:
        sys = row.get('system', '')
        step_name = row.get('reaction_step', '')
        try:
            energy = float(row.get('free_energy', None))
        except:
            return 0.0
        data_by_sys[sys][step_name] = energy
    required_sys = ['pristine', 'V_BrS', 'V']
    required_steps = ['CO2_gas', '*CO2', '*COOH', '*CO', '*CHO', '*CH2O', '*CH3O', '*CH3OH', 'CH3OH_gas']
    for sys in required_sys:
        if sys not in data_by_sys or not all(s in data_by_sys[sys] for s in required_steps):
            return 0.0
    def barrier(sys, from_step, to_step):
        return data_by_sys[sys][to_step] - data_by_sys[sys][from_step]
    total = 0.0
    bar_checks = step.get('barrier_checks', [])
    for bc in bar_checks:
        from_step = bc['from']
        to_step = bc['to']
        sys = bc['system']
        target = bc['target']
        tol = bc.get('tolerance', 0.2)
        try:
            val = barrier(sys, from_step, to_step)
        except:
            continue
        dev = abs(val - target)
        if dev <= tol:
            total += 0.25
        elif dev <= 2*tol:
            total += 0.125
    exo_checks = step.get('exothermic_checks', [])
    for ec in exo_checks:
        from_step = ec['from']
        to_step = ec['to']
        sys = ec['system']
        expected_sign = ec['expected_sign']
        try:
            dg = barrier(sys, from_step, to_step)
        except:
            continue
        if (expected_sign == 'negative' and dg < 0) or (expected_sign == 'positive' and dg > 0):
            total += 0.15
    try:
        barV = barrier('V', '*COOH', '*CO')
        barP = barrier('pristine', '*COOH', '*CO')
        barVB = barrier('V_BrS', '*COOH', '*CO')
        if barV < barP and barV < barVB:
            total += 0.2
    except:
        pass
    return min(total, 1.0)


_SCORERS = {
    's02': score_0,
    's03': score_1,
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
