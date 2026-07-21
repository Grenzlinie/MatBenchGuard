import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    gold_data = {
        "coronene": {"Eg": 7.36, "HOMO": -7.20, "LUMO": 0.16},
        "Al-coronene": {"Eg": 6.85, "HOMO": -6.86, "LUMO": -0.01},
        "A1_EF0": {"E_ads": -47.71, "Eg": 6.39, "delta_Eg_percent": -6.72, "QT": -0.22, "HOMO": -6.24, "LUMO": 0.15, "d": 1.99},
        "T1_EF0": {"E_ads": -42.63, "Eg": 6.04, "delta_Eg_percent": -11.82, "QT": -0.32, "HOMO": -6.03, "LUMO": 0.01, "d": 1.91},
        "G1_EF0": {"E_ads": -53.19, "Eg": 6.37, "delta_Eg_percent": -7.01, "QT": -0.22, "HOMO": -5.73, "LUMO": 0.64, "d": 1.88},
        "C1_EF0": {"E_ads": -51.69, "Eg": 5.63, "delta_Eg_percent": -17.81, "QT": -0.33, "HOMO": -5.94, "LUMO": -0.31, "d": 1.89},
        "A1_EF1e-2": {"E_ads": -63.39, "Eg": 6.30, "delta_Eg_percent": -3.82, "QT": -0.34, "HOMO": -6.28, "LUMO": 0.02, "d": 1.95},
        "T1_EF1e-2": {"E_ads": -67.36, "Eg": 5.93, "delta_Eg_percent": -9.47, "QT": -0.39, "HOMO": -6.12, "LUMO": -0.19, "d": 1.86},
        "G1_EF1e-2": {"E_ads": -68.98, "Eg": 6.23, "delta_Eg_percent": -4.89, "QT": -0.43, "HOMO": -5.85, "LUMO": 0.38, "d": 1.82},
        "C1_EF1e-2": {"E_ads": -67.11, "Eg": 5.55, "delta_Eg_percent": -15.27, "QT": -0.39, "HOMO": -5.31, "LUMO": 0.24, "d": 1.85},
        "A1_EF2e-2": {"E_ads": -87.79, "Eg": 5.15, "delta_Eg_percent": -19.15, "QT": -0.45, "HOMO": -6.05, "LUMO": -0.90, "d": 1.92},
        "T1_EF2e-2": {"E_ads": -89.66, "Eg": 5.58, "delta_Eg_percent": -12.40, "QT": -0.42, "HOMO": -6.23, "LUMO": -0.65, "d": 1.82},
        "G1_EF2e-2": {"E_ads": -89.08, "Eg": 5.20, "delta_Eg_percent": -18.37, "QT": -0.48, "HOMO": -4.71, "LUMO": -0.49, "d": 1.80},
        "C1_EF2e-2": {"E_ads": -89.56, "Eg": 5.39, "delta_Eg_percent": -15.38, "QT": -0.47, "HOMO": -5.98, "LUMO": -0.59, "d": 1.81}
    }
    tolerances = {
        "E_ads": 5.0,   # kcal/mol
        "Eg": 0.5,      # eV
        "QT": 0.1,      # e
        "delta_Eg_percent": 5.0,  # percentage points
        "d": 0.5         # Å
    }
    return {"gold_data": gold_data, "tolerances": tolerances}


# === block: score_0 (check id='systems_present') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts
    required = set(ctx["gold_data"].keys())
    present = set()
    for item in artifact:
        if isinstance(item, dict) and "system" in item:
            present.add(item["system"])
    missing = len(required - present)
    extra = len(present - required)
    score = max(0.0, 1.0 - 0.1 * missing - 0.05 * extra)
    return score


# === block: score_1 (check id='E_ads_proximity') ===
def score_1(artifact, step, ctx):
    gold = ctx["gold_data"]
    tol = ctx["tolerances"]["E_ads"]
    complex_systems = [k for k in gold if "EF" in k]
    scores = []
    for sys in complex_systems:
        agent_item = next((it for it in artifact if it.get("system") == sys), None)
        if agent_item is None or agent_item.get("E_ads") is None:
            scores.append(0.0)
            continue
        agent_val = float(agent_item["E_ads"])
        gold_val = float(gold[sys]["E_ads"])
        # more negative is better
        if agent_val <= gold_val:
            scores.append(1.0)
        else:
            diff = agent_val - gold_val  # positive, worse
            scores.append(max(0.0, 1.0 - diff / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='Eg_proximity') ===
def score_2(artifact, step, ctx):
    gold = ctx["gold_data"]
    tol = ctx["tolerances"]["Eg"]
    systems = list(gold.keys())
    scores = []
    for sys in systems:
        agent_item = next((it for it in artifact if it.get("system") == sys), None)
        if agent_item is None or agent_item.get("Eg") is None:
            scores.append(0.0)
            continue
        agent_val = float(agent_item["Eg"])
        gold_val = float(gold[sys]["Eg"])
        # lower is better
        if agent_val <= gold_val:
            scores.append(1.0)
        else:
            diff = agent_val - gold_val
            scores.append(max(0.0, 1.0 - diff / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='QT_proximity') ===
def score_3(artifact, step, ctx):
    gold = ctx["gold_data"]
    tol = ctx["tolerances"]["QT"]
    complex_systems = [k for k in gold if "EF" in k]
    scores = []
    for sys in complex_systems:
        agent_item = next((it for it in artifact if it.get("system") == sys), None)
        if agent_item is None or agent_item.get("QT") is None:
            scores.append(0.0)
            continue
        agent_val = abs(float(agent_item["QT"]))
        gold_val = abs(float(gold[sys]["QT"]))
        # higher |QT| is better
        if agent_val >= gold_val:
            scores.append(1.0)
        else:
            diff = gold_val - agent_val
            scores.append(max(0.0, 1.0 - diff / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_4 (check id='delta_Eg_percent_proximity') ===
def score_4(artifact, step, ctx):
    gold = ctx["gold_data"]
    tol = ctx["tolerances"]["delta_Eg_percent"]
    complex_systems = [k for k in gold if "EF" in k]
    scores = []
    for sys in complex_systems:
        agent_item = next((it for it in artifact if it.get("system") == sys), None)
        if agent_item is None or agent_item.get("delta_Eg_percent") is None:
            scores.append(0.0)
            continue
        agent_val = abs(float(agent_item["delta_Eg_percent"]))
        gold_val = abs(float(gold[sys]["delta_Eg_percent"]))
        # larger absolute change is better
        if agent_val >= gold_val:
            scores.append(1.0)
        else:
            diff = gold_val - agent_val
            scores.append(max(0.0, 1.0 - diff / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_5 (check id='d_proximity') ===
def score_5(artifact, step, ctx):
    gold = ctx["gold_data"]
    tol = ctx["tolerances"]["d"]
    complex_systems = [k for k in gold if "EF" in k]
    scores = []
    for sys in complex_systems:
        agent_item = next((it for it in artifact if it.get("system") == sys), None)
        if agent_item is None or agent_item.get("d") is None:
            scores.append(0.0)
            continue
        agent_val = float(agent_item["d"])
        gold_val = float(gold[sys]["d"])
        diff = abs(agent_val - gold_val)
        if diff <= tol:
            scores.append(1.0)
        else:
            # linearly decay beyond tolerance
            scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_6 (check id='homo_lumo_sanity') ===
def score_6(artifact, step, ctx):
    errors = 0
    total = 0
    for item in artifact:
        if not isinstance(item, dict):
            continue
        homo = item.get("HOMO")
        lumo = item.get("LUMO")
        if homo is None or lumo is None:
            errors += 1
            total += 1
            continue
        if float(homo) < float(lumo):
            total += 1
        else:
            errors += 1
            total += 1
    return 1.0 - errors / total if total > 0 else 0.0


# === block: score_7 (check id='trends') ===
def score_7(artifact, step, ctx):
    gold = ctx["gold_data"]
    # Sub-score 1: field-strength monotonicity for each nucleobase (more negative with field)
    fields = ["EF0", "EF1e-2", "EF2e-2"]
    nbs = ["A1", "T1", "G1", "C1"]
    mono_correct = 0
    for nb in nbs:
        ads = []
        for field in fields:
            sys = f"{nb}_{field}"
            agent_item = next((it for it in artifact if it.get("system") == sys), None)
            if agent_item and agent_item.get("E_ads") is not None:
                ads.append(float(agent_item["E_ads"]))
            else:
                ads.append(None)
        if any(v is None for v in ads):
            continue
        # check strictly decreasing (more negative): ads[0] > ads[1] > ads[2]
        if ads[0] > ads[1] > ads[2]:
            mono_correct += 1
    sub_score1 = mono_correct / len(nbs) if nbs else 1.0

    # Sub-score 2: ordering among NBs at EF0 (G < C < A < T numerically)
    expected_order = ["G1_EF0", "C1_EF0", "A1_EF0", "T1_EF0"]
    vals = []
    for sys in expected_order:
        agent_item = next((it for it in artifact if it.get("system") == sys), None)
        if agent_item and agent_item.get("E_ads") is not None:
            vals.append(float(agent_item["E_ads"]))
        else:
            vals.append(None)
    if any(v is None for v in vals):
        sub_score2 = 0.0
    else:
        # expected ordering: vals[0] < vals[1] < vals[2] < vals[3]
        if vals[0] < vals[1] < vals[2] < vals[3]:
            sub_score2 = 1.0
        else:
            # count inversions; partial credit
            inv = sum(1 for i in range(len(vals)) for j in range(i+1, len(vals)) if vals[i] > vals[j])
            max_inv = 6  # total pairs
            sub_score2 = max(0.0, 1.0 - inv / max_inv)

    # Sub-score 3: band gap reduction for all 12 complexes (Eg complex < Eg Al-coronene)
    ref_eg = gold["Al-coronene"]["Eg"]
    complex_systems = [k for k in gold if "EF" in k]
    eg_ok = 0
    for sys in complex_systems:
        agent_item = next((it for it in artifact if it.get("system") == sys), None)
        if agent_item and agent_item.get("Eg") is not None:
            if float(agent_item["Eg"]) < ref_eg:
                eg_ok += 1
    sub_score3 = eg_ok / len(complex_systems) if complex_systems else 1.0

    # Combine sub-scores
    return 0.4 * sub_score1 + 0.3 * sub_score2 + 0.3 * sub_score3


_SCORERS = {
    'systems_present': score_0,
    'E_ads_proximity': score_1,
    'Eg_proximity': score_2,
    'QT_proximity': score_3,
    'delta_Eg_percent_proximity': score_4,
    'd_proximity': score_5,
    'homo_lumo_sanity': score_6,
    'trends': score_7,
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
