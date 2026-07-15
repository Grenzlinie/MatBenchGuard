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


# === block: score_0 (check id='energies_check') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold_energies', {})
    if not isinstance(artifact, dict):
        return 0.0
    tolerance = step.get('tolerance_abs', 2.0)
    total = 0
    ok = 0
    for path, path_data in gold.items():
        act = path_data.get('activation', {})
        react = path_data.get('reaction', {})
        agent_path = artifact.get(path)
        if not isinstance(agent_path, dict):
            continue
        agent_act = agent_path.get('activation', {})
        agent_react = agent_path.get('reaction', {})
        for key in ['delta_E0_dagger', 'delta_H298_dagger', 'delta_G298_dagger']:
            total += 1
            if key in agent_act and abs(agent_act[key] - act.get(key, 0)) <= tolerance:
                ok += 1
        for key in ['delta_E0', 'delta_H298', 'delta_G298']:
            total += 1
            if key in agent_react and abs(agent_react[key] - react.get(key, 0)) <= tolerance:
                ok += 1
    return ok / total if total > 0 else 0.0


# === block: score_1 (check id='rates_reference') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold_rates', {})
    if not isinstance(artifact, list):
        return 0.0
    factor = step.get('tolerance_factor', 5.0)
    checks = 0
    passes = 0
    for row in artifact:
        if row.get('pathway') != 'R1->P1':
            continue
        pbar = float(row.get('pressure_bar', 1.0))
        if abs(pbar - 1.0) > 1e-6:
            continue
        temp = str(float(row.get('temperature_C', 0)))
        tst = float(row.get('TST_rate', 0))
        rrkm = float(row.get('RRKM_rate', 0))
        if temp in gold:
            gtst = gold[temp]['TST_rate']
            grrkm = gold[temp]['RRKM_rate']
            checks += 1
            if (tst / gtst > 1/factor and tst / gtst < factor) and (rrkm / grrkm > 1/factor and rrkm / grrkm < factor):
                passes += 1
    return passes / checks if checks > 0 else 0.0


# === block: score_2 (check id='rates_falloff') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    max_p_below = -1.0
    has_below = False
    for row in artifact:
        if row.get('pathway') != 'R1->P1':
            continue
        p = float(row.get('pressure_bar', -1))
        if p < 0:
            continue
        tst = float(row.get('TST_rate', 0))
        rrkm = float(row.get('RRKM_rate', 0))
        if rrkm <= 0:
            continue
        ratio = tst / rrkm
        if ratio < 0.9:
            has_below = True
            if p > max_p_below:
                max_p_below = p
    if has_below and max_p_below <= 1e-4:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='falloff_summary') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    falloff = artifact.get('pathway1_falloff', False)
    breakdown = artifact.get('breakdown_pressure_bar', None)
    if not falloff or breakdown is None:
        return 0.0
    return 1.0 if (isinstance(breakdown, (int, float)) and breakdown <= 1e-4) else 0.0


_SCORERS = {
    'energies_check': score_0,
    'rates_reference': score_1,
    'rates_falloff': score_2,
    'falloff_summary': score_3,
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
