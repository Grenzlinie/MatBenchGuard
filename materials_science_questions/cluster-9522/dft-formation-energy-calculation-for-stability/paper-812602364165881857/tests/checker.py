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


# === block: score_0 (check id='bond_lengths') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0
    gold = step.get("gold", {})
    tol = step.get("tolerance", 2.0)
    agent = {}
    for r in rows:
        try:
            metal, bond = r["metal"], r["bond"]
            length = float(r["length"])
            agent[(metal, bond)] = length
        except (KeyError, ValueError):
            continue

    correct = 0
    total_bonds = 0
    for metal_str in gold:
        for bond in gold[metal_str]:
            total_bonds += 1
            gval = gold[metal_str][bond]
            aval = agent.get((metal_str, bond))
            if aval is not None and abs(aval - gval) <= tol:
                correct += 1
    frac_correct = correct / max(total_bonds, 1)

    # monotonic M-F trend
    metals_order = ["Fe","Co","Ni","Cu"]
    mf1_vals = [agent.get((m,"M-F1")) for m in metals_order]
    mf2_vals = [agent.get((m,"M-F2")) for m in metals_order]
    mono = True
    try:
        for i in range(len(mf1_vals)-1):
            if mf1_vals[i] is not None and mf1_vals[i+1] is not None and mf1_vals[i] >= mf1_vals[i+1]:
                mono = False
            if mf2_vals[i] is not None and mf2_vals[i+1] is not None and mf2_vals[i] >= mf2_vals[i+1]:
                mono = False
    except:
        mono = False

    score = frac_correct * (1.0 if mono else 0.5)
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='spin_states') ===
def score_1(artifact, step, ctx):
    gold = step.get("gold", {})
    if not isinstance(artifact, list):
        return 0.0
    correct = 0
    for metal_str, mult in gold.items():
        for r in artifact:
            if r.get("metal") == metal_str:
                try:
                    if int(r["ground_state_multiplicity"]) == mult:
                        correct += 1
                        break
                except (ValueError, KeyError):
                    pass
    return correct / max(len(gold), 1)


# === block: score_2 (check id='planarity') ===
def score_2(artifact, step, ctx):
    gold = step.get("gold", {})
    tol = step.get("tolerance", 2.0)
    if not isinstance(artifact, list):
        return 0.0
    agent = {}
    for r in artifact:
        try:
            metal, site = r["metal"], r["site"]
            val = float(r["sum_angles_deg"])
            agent[(metal, site)] = val
        except (KeyError, ValueError):
            continue
    correct = 0
    total = 0
    for metal_str in gold:
        for site in gold[metal_str]:
            total += 1
            gval = gold[metal_str][site]
            aval = agent.get((metal_str, site))
            if aval is not None and abs(aval - gval) <= tol:
                correct += 1
    return correct / max(total, 1)


# === block: score_3 (check id='thermodynamics') ===
def score_3(artifact, step, ctx):
    gold = step.get("gold", {})
    tol_dH_G = step.get("tolerance_delta_H_G", {"relative":0.05,"absolute":10.0})
    tol_S = step.get("tolerance_S", 10.0)
    if not isinstance(artifact, list):
        return 0.0

    def get_tol(val, tol_cfg):
        rel = tol_cfg["relative"] * abs(val)
        abs_tol = tol_cfg["absolute"]
        return max(rel, abs_tol)

    correct = 0
    total_entries = len(gold) * 3  # each metal has delta_H, delta_G, S
    for r in artifact:
        try:
            metal = r["metal"]
            if metal not in gold:
                continue
            g = gold[metal]
            # delta_H
            h = float(r["delta_H"])
            if abs(h - g["delta_H"]) <= get_tol(g["delta_H"], tol_dH_G):
                correct += 1
            # delta_G
            g_val = float(r["delta_G"])
            if abs(g_val - g["delta_G"]) <= get_tol(g["delta_G"], tol_dH_G):
                correct += 1
            # S
            s_val = float(r["S"])
            if abs(s_val - g["S"]) <= tol_S:
                correct += 1
        except (KeyError, ValueError):
            continue

    return correct / max(total_entries, 1)


_SCORERS = {
    'bond_lengths': score_0,
    'spin_states': score_1,
    'planarity': score_2,
    'thermodynamics': score_3,
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
