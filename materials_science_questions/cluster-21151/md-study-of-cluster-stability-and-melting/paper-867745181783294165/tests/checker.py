import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    ctx = {}
    for step in spec['steps']:
        if step.get('output_file') == 'transition_energy.txt':
            ctx['gold_transition_energy'] = step['target_value']
            ctx['transition_tol'] = step['tolerance']
            break
    return ctx


# === block: score_0 (check id='step_01_heating_caloric_curve') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0
    energies = []
    temps = []
    fccs = []
    try:
        for r in artifact:
            energies.append(float(r['total_energy']))
            temps.append(float(r['temperature']))
            fccs.append(int(r['num_fcc_atoms']))
    except (KeyError, ValueError, TypeError):
        return 0.0

    # 1. solid low energy
    min_idx = min(range(len(energies)), key=lambda i: abs(energies[i] - (-3.83)))
    score1 = 1.0 if fccs[min_idx] >= 300 else 0.0

    # 2. liquid high energy
    max_idx = min(range(len(energies)), key=lambda i: abs(energies[i] - (-3.755)))
    score2 = 1.0 if fccs[max_idx] <= 50 else 0.0

    # 3. monotonic temperature
    mono = all(temps[i] >= temps[i-1] - 1e-6 for i in range(1, len(temps)))
    score3 = 1.0 if mono else 0.0

    # 4. transition present
    transition = False
    for i in range(1, len(energies)):
        if (temps[i] - temps[i-1] > 15.0) and (abs(fccs[i] - fccs[i-1]) > 100) and (-3.78 <= energies[i] <= -3.76):
            transition = True
            break
    score4 = 1.0 if transition else 0.0

    return 0.25*score1 + 0.25*score2 + 0.25*score3 + 0.25*score4


# === block: score_1 (check id='step_02_cooling_caloric_curve') ===
def score_1(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0
    rows = []
    try:
        for r in artifact:
            rows.append((float(r['total_energy']), float(r['temperature']), int(r['num_fcc_atoms'])))
    except (KeyError, ValueError, TypeError):
        return 0.0
    if len(rows) == 0:
        return 0.0
    rows.sort(key=lambda x: x[0])
    energies = [r[0] for r in rows]
    temps = [r[1] for r in rows]
    fccs = [r[2] for r in rows]

    # low energy solid
    min_energy = min(energies)
    min_idx = energies.index(min_energy)
    score1 = 1.0 if fccs[min_idx] >= 500 else 0.0

    # high energy liquid
    max_energy = max(energies)
    max_idx = energies.index(max_energy)
    score2 = 1.0 if fccs[max_idx] <= 50 else 0.0

    # temperature monotonic with total energy (cooling: T increases as E increases)
    mono = all(temps[i] >= temps[i-1] - 1e-6 for i in range(1, len(temps)))
    score3 = 1.0 if mono else 0.0

    return 0.4*score1 + 0.4*score2 + 0.2*score3


# === block: score_2 (check id='step_03_transition_energy') ===
def score_2(artifact, step, ctx):
    import csv, os
    path = '/app/outputs/heating_caloric_curve.csv'
    if not os.path.exists(path):
        return 0.0
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return 0.0
    energies = []
    temps = []
    fccs = []
    try:
        for r in rows:
            energies.append(float(r['total_energy']))
            temps.append(float(r['temperature']))
            fccs.append(int(r['num_fcc_atoms']))
    except (KeyError, ValueError):
        return 0.0
    transition_energy = None
    for i in range(1, len(energies)):
        if (temps[i] - temps[i-1] > 15.0) and (abs(fccs[i] - fccs[i-1]) > 100) and (-3.78 <= energies[i] <= -3.76):
            transition_energy = energies[i]
            break
    if transition_energy is None:
        return 0.0
    gold = ctx['gold_transition_energy']
    tol = ctx['transition_tol']
    if abs(transition_energy - gold) <= tol:
        return 1.0
    return 0.0


_SCORERS = {
    'step_01_heating_caloric_curve': score_0,
    'step_02_cooling_caloric_curve': score_1,
    'step_03_transition_energy': score_2,
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
