import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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


# === block: score_0 (check id='phase_energies_check') ===
def score_0(artifact, step, ctx):
    expected = step["gold"]["phase_expected"]
    u_to_min_phases = {}
    for row in artifact:
        u = float(row["U_over_t"])
        phase = row["phase"].strip()
        energy = float(row["energy_per_site"])
        key = str(int(u))
        if key not in u_to_min_phases:
            u_to_min_phases[key] = (energy, [phase])
        else:
            curr_min, curr_phases = u_to_min_phases[key]
            if energy < curr_min - 1e-12:
                u_to_min_phases[key] = (energy, [phase])
            elif abs(energy - curr_min) < 1e-12:
                curr_phases.append(phase)
                u_to_min_phases[key] = (curr_min, curr_phases)
    total = len(expected)
    correct = 0
    for u_str, accepted in expected.items():
        if u_str in u_to_min_phases:
            _, agent_phases = u_to_min_phases[u_str]
            if any(p in accepted for p in agent_phases):
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='crossover_values_check') ===
def score_1(artifact, step, ctx):
    gold = step["gold"]
    v_gold = gold["vertical_to_diagonal_crossover_U_over_t"]["target"]
    v_tol = gold["vertical_to_diagonal_crossover_U_over_t"]["tolerance"]
    d_gold = gold["diagonal_to_polaron_crossover_U_over_t"]["target"]
    d_tol = gold["diagonal_to_polaron_crossover_U_over_t"]["tolerance"]

    v_agent = float(artifact.get("vertical_to_diagonal_crossover_U_over_t"))
    d_agent = float(artifact.get("diagonal_to_polaron_crossover_U_over_t"))

    score = 0.0
    if abs(v_agent - v_gold) <= v_tol:
        score += 0.5
    if abs(d_agent - d_gold) <= d_tol:
        score += 0.5
    return score


# === block: score_2 (check id='collinearity_check') ===
def score_2(artifact, step, ctx):
    collinear = artifact.get("collinear_for_U_t_le_20")
    max_dev = artifact.get("max_angular_deviation_degrees")
    if collinear is True and float(max_dev) < 5.0:
        return 1.0
    return 0.0


_SCORERS = {
    'phase_energies_check': score_0,
    'crossover_values_check': score_1,
    'collinearity_check': score_2,
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
