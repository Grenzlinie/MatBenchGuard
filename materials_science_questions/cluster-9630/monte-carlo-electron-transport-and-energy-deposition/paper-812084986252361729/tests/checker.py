import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    gold = spec.get("gold_values", {})
    tol_abs = spec.get("tolerances", {}).get("deposited_energy_abs_tol", 0.02)
    expected_energies = sorted([float(k) for k in gold.keys()])
    csv_path = os.path.join(outputs_dir, "simulation_results.csv")
    csv_data = None
    if os.path.exists(csv_path):
        try:
            with open(csv_path, newline='') as f:
                csv_data = list(csv.DictReader(f))
        except:
            csv_data = None
    return {"gold": gold, "tol_abs": tol_abs, "expected_energies": expected_energies, "csv_data": csv_data}


# === block: score_0 (check id='simulation_results_csv') ===
def score_0(artifact, step, ctx):
    gold = ctx["gold"]
    tol_abs = ctx["tol_abs"]
    expected_energies = ctx["expected_energies"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    agent = {}
    for row in artifact:
        try:
            e = float(row.get("incident_energy_MeV", None))
            d = float(row.get("mean_deposited_energy_MeV", None))
            agent[e] = d
        except:
            continue
    present = [e for e in expected_energies if e in agent]
    coverage = len(present) / len(expected_energies) if expected_energies else 0.0
    tol_scores = []
    for e in expected_energies:
        gv = gold[str(e)]
        av = agent.get(e)
        if av is None or gv is None:
            tol_scores.append(0.0)
        else:
            diff = abs(av - gv)
            if diff <= tol_abs:
                tol_scores.append(1.0)
            else:
                tol_scores.append(0.0)
    tol_score = sum(tol_scores) / len(tol_scores) if tol_scores else 0.0
    shape_score = 0.0
    max_e = None
    max_v = -1
    for e, v in agent.items():
        if v > max_v:
            max_v = v
            max_e = e
    if max_e is not None and max_e >= 0.3 and max_e <= 0.5 and max_v >= 0.28:
        shape_score += 0.5
    high_energies = sorted([e for e in agent.keys() if e >= 2.0])
    monotonic = True
    for i in range(len(high_energies)-1):
        if agent[high_energies[i+1]] < agent[high_energies[i]] - 1e-5:
            monotonic = False
            break
    if monotonic and len(high_energies) >= 2:
        shape_score += 0.5
    e6 = agent.get(6.0)
    e21 = agent.get(21.0)
    percent_diff_score = 0.0
    if e6 is not None and e21 is not None:
        diff = 100.0 * abs(e6 - e21) / ((e6 + e21) / 2.0)
        if diff <= 0.7:
            percent_diff_score = 1.0
    score = 0.1 * coverage + 0.4 * tol_score + 0.3 * shape_score + 0.2 * percent_diff_score
    return score


# === block: score_1 (check id='summary_json') ===
def score_1(artifact, step, ctx):
    csv_data = ctx.get("csv_data")
    if not isinstance(artifact, dict):
        return 0.0
    required = ["deposited_energy_6MeV", "deposited_energy_21MeV", "percent_difference"]
    for k in required:
        if k not in artifact:
            return 0.0
    json6 = artifact["deposited_energy_6MeV"]
    json21 = artifact["deposited_energy_21MeV"]
    json_diff = artifact["percent_difference"]
    if csv_data is not None and isinstance(csv_data, list) and len(csv_data) > 0:
        agent_csv = {}
        for row in csv_data:
            try:
                e = float(row["incident_energy_MeV"])
                d = float(row["mean_deposited_energy_MeV"])
                agent_csv[e] = d
            except:
                continue
        csv6 = agent_csv.get(6.0)
        csv21 = agent_csv.get(21.0)
        if csv6 is None or csv21 is None:
            return 0.0
        if abs(json6 - csv6) > 1e-4 or abs(json21 - csv21) > 1e-4:
            return 0.0
        computed_diff = 100.0 * abs(csv6 - csv21) / ((csv6 + csv21) / 2.0)
        if abs(json_diff - computed_diff) > 1e-4:
            return 0.0
        return 1.0
    else:
        gold6 = ctx["gold"].get("6.0")
        gold21 = ctx["gold"].get("21.0")
        if gold6 is None or gold21 is None:
            return 0.1
        if abs(json6 - gold6) <= 0.02 and abs(json21 - gold21) <= 0.02 and abs(json_diff) <= 0.7:
            return 0.5
        return 0.0


_SCORERS = {
    'simulation_results_csv': score_0,
    'summary_json': score_1,
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
