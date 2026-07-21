import os
import json
import csv

# === author imports / helpers ===
import csv, math, json, os


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
    gold_lookup = {}
    for step in spec.get('steps', []):
        gv = step.get('gold_values')
        if gv is not None:
            gold_lookup[step['id']] = gv
    return gold_lookup


# === block: score_0 (check id='angular_width_static_check') ===
def score_0(artifact, step, ctx):
    try:
        artifact_path = os.path.join('/app/outputs', step['output_file'])
        energies_gold = ctx.get('gold_values', {})
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        agent_vals = {}
        for row in rows:
            e = row['incidence_energy_eV'].strip()
            agent_vals[e] = float(row['angular_width_deg'])
        tol_specs = step.get('tolerances', {}).get('spec', [])
        tol_map = {str(s['energy']): s['tol_abs'] for s in tol_specs}
        n = 0
        passed = 0
        for e_str, gold in energies_gold.items():
            if e_str not in agent_vals:
                continue
            agent = agent_vals[e_str]
            tol = tol_map.get(e_str, 2.0)
            if abs(agent - gold) <= tol:
                passed += 1
            n += 1
        point_score = passed / n if n > 0 else 0.0
        trend_ok = False
        if '0.5' in agent_vals and '1.0' in agent_vals and '10.0' in agent_vals:
            v05 = agent_vals['0.5']
            v1 = agent_vals['1.0']
            v10 = agent_vals['10.0']
            if v1 <= v05 and v1 <= v10:
                trend_ok = True
        w_trend = step.get('trend_check', {}).get('weight_in_check', 0.0)
        score = (1 - w_trend) * point_score + w_trend * (1.0 if trend_ok else 0.0)
        return score
    except Exception as e:
        return 0.0


# === block: score_1 (check id='angular_width_600K_check') ===
def score_1(artifact, step, ctx):
    try:
        artifact_path = os.path.join('/app/outputs', step['output_file'])
        energies_gold = ctx.get('gold_values', {})
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        agent_vals = {}
        for row in rows:
            e = row['incidence_energy_eV'].strip()
            agent_vals[e] = float(row['angular_width_deg'])
        tol_specs = step.get('tolerances', {}).get('spec', [])
        tol_map = {str(s['energy']): s['tol_abs'] for s in tol_specs}
        n = 0
        passed = 0
        for e_str, gold in energies_gold.items():
            if e_str not in agent_vals:
                continue
            agent = agent_vals[e_str]
            tol = tol_map.get(e_str, 2.0)
            if abs(agent - gold) <= tol:
                passed += 1
            n += 1
        point_score = passed / n if n > 0 else 0.0
        trend_ok = False
        if '0.5' in agent_vals and '1.0' in agent_vals and '10.0' in agent_vals:
            v05 = agent_vals['0.5']
            v1 = agent_vals['1.0']
            v10 = agent_vals['10.0']
            if v1 <= v05 and v1 <= v10:
                trend_ok = True
        w_trend = step.get('trend_check', {}).get('weight_in_check', 0.0)
        score = (1 - w_trend) * point_score + w_trend * (1.0 if trend_ok else 0.0)
        return score
    except Exception as e:
        return 0.0


# === block: score_2 (check id='sticking_probability_600K_check') ===
def score_2(artifact, step, ctx):
    try:
        artifact_path = os.path.join('/app/outputs', step['output_file'])
        energies_gold = ctx.get('gold_values', {})
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        agent_vals = {}
        for row in rows:
            e = row['incidence_energy_eV'].strip()
            agent_vals[e] = float(row['sticking_probability'])
        rel = step['tolerances'].get('rel', 0.15)
        abs_cap = step['tolerances'].get('abs_cap', 0.1)
        n = 0
        passed = 0
        for e_str, gold in energies_gold.items():
            if e_str not in agent_vals:
                continue
            agent = agent_vals[e_str]
            tol = max(rel * gold, abs_cap)
            if abs(agent - gold) <= tol:
                passed += 1
            n += 1
        point_score = passed / n if n > 0 else 0.0
        trend_ok = True
        ordered = ['0.03','0.1','0.5','1.0','10.0','100.0']
        for i in range(len(ordered)-1):
            e1 = ordered[i]
            e2 = ordered[i+1]
            if e1 in agent_vals and e2 in agent_vals:
                v1 = agent_vals[e1]
                v2 = agent_vals[e2]
                if float(e2) <= 1.0:
                    if v1 < v2:
                        trend_ok = False
                        break
                elif float(e1) >= 10.0:
                    if v1 > v2:
                        trend_ok = False
                        break
        w_trend = step.get('trend_check', {}).get('weight_in_check', 0.0)
        score = (1 - w_trend) * point_score + w_trend * (1.0 if trend_ok else 0.0)
        return score
    except Exception as e:
        return 0.0


_SCORERS = {
    'angular_width_static_check': score_0,
    'angular_width_600K_check': score_1,
    'sticking_probability_600K_check': score_2,
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
