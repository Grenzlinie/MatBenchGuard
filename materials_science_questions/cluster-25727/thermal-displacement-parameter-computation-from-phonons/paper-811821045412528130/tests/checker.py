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
    import csv, json, os

    def load_csv(path):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    def load_json(path):
        with open(path) as f:
            return json.load(f)

    # Gold barrier heights from paper Tables 1 and 2
    barrier_gold = [
        # SbSI (x=0), Table 1
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':283,'pressure_arb':0.0,'composition_x':0.0,'barrier_V':0.0075},
        {'temperature_K':293,'pressure_arb':0.1,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':283,'pressure_arb':0.1,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':273,'pressure_arb':0.1,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':293,'pressure_arb':0.2,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':283,'pressure_arb':0.2,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':273,'pressure_arb':0.2,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':263,'pressure_arb':0.2,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':253,'pressure_arb':0.2,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':293,'pressure_arb':0.3,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':283,'pressure_arb':0.3,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':273,'pressure_arb':0.3,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':263,'pressure_arb':0.3,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':253,'pressure_arb':0.3,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':241,'pressure_arb':0.3,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':231,'pressure_arb':0.3,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':293,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':283,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':273,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':263,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':253,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':241,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':231,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':223,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':213,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':202,'pressure_arb':0.4,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':283,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':273,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':263,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':253,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':241,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':231,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':223,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':213,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':202,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':183,'pressure_arb':0.5,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':273,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':263,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':253,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':241,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':231,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':223,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':213,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':202,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':183,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':173,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':163,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':150,'pressure_arb':0.6,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':253,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':241,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':231,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':223,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':213,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':202,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':183,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':173,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':163,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':150,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':143,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':133,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':119,'pressure_arb':0.7,'composition_x':0.0,'barrier_V':0.007},
        {'temperature_K':231,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':223,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':213,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.0},
        {'temperature_K':202,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':183,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.001},
        {'temperature_K':173,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':163,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.002},
        {'temperature_K':150,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':143,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.003},
        {'temperature_K':133,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.004},
        {'temperature_K':119,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':113,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.005},
        {'temperature_K':103,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.006},
        {'temperature_K':93,'pressure_arb':0.8,'composition_x':0.0,'barrier_V':0.007},
        # Bi_xSb_{1-x}SI, Table 2 (p=0)
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.0,'barrier_V':0.0070},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.06,'barrier_V':0.004218},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.1,'barrier_V':0.002923},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.18,'barrier_V':0.000965},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.2,'barrier_V':0.000610},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.000226},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.0},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':293,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.06,'barrier_V':0.007001},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.1,'barrier_V':0.004417},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.18,'barrier_V':0.001852},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.2,'barrier_V':0.001389},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.000734},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.000020},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':270,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':250,'pressure_arb':0.0,'composition_x':0.1,'barrier_V':0.007280},
        {'temperature_K':250,'pressure_arb':0.0,'composition_x':0.18,'barrier_V':0.002909},
        {'temperature_K':250,'pressure_arb':0.0,'composition_x':0.2,'barrier_V':0.002208},
        {'temperature_K':250,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.001438},
        {'temperature_K':250,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.000210},
        {'temperature_K':250,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':250,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':248,'pressure_arb':0.0,'composition_x':0.18,'barrier_V':0.003994},
        {'temperature_K':248,'pressure_arb':0.0,'composition_x':0.2,'barrier_V':0.003007},
        {'temperature_K':248,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.001540},
        {'temperature_K':248,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.000255},
        {'temperature_K':248,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':248,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':208,'pressure_arb':0.0,'composition_x':0.18,'barrier_V':0.005767},
        {'temperature_K':208,'pressure_arb':0.0,'composition_x':0.2,'barrier_V':0.004825},
        {'temperature_K':208,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.003600},
        {'temperature_K':208,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.001372},
        {'temperature_K':208,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':208,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':200,'pressure_arb':0.0,'composition_x':0.2,'barrier_V':0.007062},
        {'temperature_K':200,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.004216},
        {'temperature_K':200,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.001672},
        {'temperature_K':200,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.000022},
        {'temperature_K':200,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':176,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.005843},
        {'temperature_K':176,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.002913},
        {'temperature_K':176,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.000281},
        {'temperature_K':176,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':150,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.004525},
        {'temperature_K':150,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.000949},
        {'temperature_K':150,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':150,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':100,'pressure_arb':0.0,'composition_x':0.3,'barrier_V':0.007005},
        {'temperature_K':100,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.003166},
        {'temperature_K':100,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':100,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':50,'pressure_arb':0.0,'composition_x':0.45,'barrier_V':0.007001},
        {'temperature_K':50,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.0},
        {'temperature_K':50,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0},
        {'temperature_K':0,'pressure_arb':0.0,'composition_x':0.6,'barrier_V':0.000340},
        {'temperature_K':0,'pressure_arb':0.0,'composition_x':0.8,'barrier_V':0.0}
    ]

    # Gold T_C values from Tables 1&2 and figures
    # (composition_x, pressure_arb, Tc_K) with Tc = -1 for no transition
    tc_gold = [
        # SbSI pressure sweep (x=0)
        {'composition_x':0.0,'pressure_arb':0.0,'Tc_K':293},
        {'composition_x':0.0,'pressure_arb':0.1,'Tc_K':273},
        {'composition_x':0.0,'pressure_arb':0.2,'Tc_K':253},
        {'composition_x':0.0,'pressure_arb':0.3,'Tc_K':231},
        {'composition_x':0.0,'pressure_arb':0.4,'Tc_K':202},
        {'composition_x':0.0,'pressure_arb':0.5,'Tc_K':183},
        {'composition_x':0.0,'pressure_arb':0.6,'Tc_K':150},
        {'composition_x':0.0,'pressure_arb':0.7,'Tc_K':119},
        {'composition_x':0.0,'pressure_arb':0.8,'Tc_K':93},
        # Bi_xSb_{1-x}SI composition sweep (p=0)
        {'composition_x':0.0,'pressure_arb':0.0,'Tc_K':293},
        {'composition_x':0.06,'pressure_arb':0.0,'Tc_K':270},
        {'composition_x':0.1,'pressure_arb':0.0,'Tc_K':250},
        {'composition_x':0.18,'pressure_arb':0.0,'Tc_K':200},
        {'composition_x':0.2,'pressure_arb':0.0,'Tc_K':200},
        {'composition_x':0.3,'pressure_arb':0.0,'Tc_K':100},
        {'composition_x':0.45,'pressure_arb':0.0,'Tc_K':50},
        {'composition_x':0.6,'pressure_arb':0.0,'Tc_K':50},
        {'composition_x':0.8,'pressure_arb':0.0,'Tc_K':-1}
    ]

    # Load agent artifacts
    barrier_csv = load_csv(os.path.join(outputs_dir, 'step_02_barrier_heights.csv'))
    quartic_json = load_json(os.path.join(outputs_dir, 'step_03_quartic_coefficients.json'))
    tc_csv = load_csv(os.path.join(outputs_dir, 'step_04_Tc_values.csv'))

    return {
        'barrier_gold': barrier_gold,
        'tc_gold': tc_gold,
        'agent_barrier': barrier_csv,
        'agent_quartic': quartic_json,
        'agent_tc': tc_csv
    }


# === block: score_0 (check id='barrier_accuracy') ===
def score_0(artifact, step, ctx):
    gold = ctx['barrier_gold']
    agent = ctx['agent_barrier']
    # Build lookup from agent rows: key = (round(T,2), round(p,2), round(x,6))
    agent_lookup = {}
    for row in agent:
        try:
            t = round(float(row['temperature_K']), 2)
            p = round(float(row['pressure_arb']), 2)
            x = round(float(row['composition_x']), 6)
        except (ValueError, KeyError):
            continue
        agent_lookup[(t, p, x)] = float(row['barrier_V'])

    matched = 0
    total = len(gold)
    if total == 0:
        return 1.0
    for g in gold:
        key = (round(g['temperature_K'],2), round(g['pressure_arb'],2), round(g['composition_x'],6))
        if key not in agent_lookup:
            continue
        agent_val = agent_lookup[key]
        gold_val = g['barrier_V']
        if gold_val == 0.0:
            if abs(agent_val) <= 0.001:
                matched += 1
        else:
            if abs(agent_val - gold_val) <= 0.001:
                matched += 1
    return matched / total


# === block: score_1 (check id='quartic_consistency') ===
def score_1(artifact, step, ctx):
    gold = ctx['barrier_gold']
    agent_bar = ctx['agent_barrier']
    agent_quartic = ctx['agent_quartic']
    # Build lookup for barrier from agent_bar as before
    bar_lookup = {}
    for row in agent_bar:
        try:
            t = round(float(row['temperature_K']), 2)
            p = round(float(row['pressure_arb']), 2)
            x = round(float(row['composition_x']), 6)
        except (ValueError, KeyError):
            continue
        bar_lookup[(t, p, x)] = float(row['barrier_V'])
    # Build lookup for quartic coeffs
    quartic_lookup = {}
    for obj in agent_quartic:
        try:
            t = round(float(obj['temperature_K']), 2)
            p = round(float(obj['pressure_arb']), 2)
            x = round(float(obj['composition_x']), 6)
        except (ValueError, KeyError):
            continue
        quartic_lookup[(t, p, x)] = (float(obj['a']), float(obj['b']), float(obj['c']), float(obj['d']))

    matched = 0
    total = 0
    for g in gold:
        key = (round(g['temperature_K'],2), round(g['pressure_arb'],2), round(g['composition_x'],6))
        if key not in bar_lookup or key not in quartic_lookup:
            continue
        total += 1
        barrier_val = bar_lookup[key]
        a, b, c, d = quartic_lookup[key]
        # Check symmetric double-well conditions: a~0, d~0, b<0, c>0
        if not (abs(a) <= 0.001 and abs(d) <= 0.001 and b < 0 and c > 0):
            continue
        # Compute barrier from quartic
        if c == 0:
            continue
        delta_v = (b * b) / (4.0 * c)
        if barrier_val == 0:
            continue  # avoid division by zero; skip if barrier is zero?
        rel_err = abs(delta_v - barrier_val) / max(abs(barrier_val), 1e-12)
        if rel_err <= 0.01:
            matched += 1

    if total == 0:
        return 0.0
    return matched / total


# === block: score_2 (check id='tc_accuracy') ===
def score_2(artifact, step, ctx):
    gold_tc = ctx['tc_gold']
    agent_tc = ctx['agent_tc']
    # Build lookup from agent Tc rows: key = (composition_x, pressure_arb)
    tc_lookup = {}
    for row in agent_tc:
        try:
            x = round(float(row['composition_x']), 6)
            p = round(float(row['pressure_arb']), 2)
        except (ValueError, KeyError):
            continue
        tc_lookup[(x, p)] = float(row['Tc_K'])

    matched = 0
    total = len(gold_tc)
    if total == 0:
        return 1.0
    for g in gold_tc:
        key = (round(g['composition_x'],6), round(g['pressure_arb'],2))
        if key not in tc_lookup:
            continue
        agent_val = tc_lookup[key]
        gold_val = g['Tc_K']
        if gold_val == -1:
            if agent_val <= 0:  # accept -1 or any non-positive as no transition
                matched += 1
        else:
            if abs(agent_val - gold_val) <= 10.0:
                matched += 1
    return matched / total


_SCORERS = {
    'barrier_accuracy': score_0,
    'quartic_consistency': score_1,
    'tc_accuracy': score_2,
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
