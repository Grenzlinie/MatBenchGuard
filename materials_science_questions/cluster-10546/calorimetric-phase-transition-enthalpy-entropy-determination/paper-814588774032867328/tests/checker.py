import os
import json
import csv

# === author imports / helpers ===
import math


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
    import math

    required_rows = [
        (298.15, "α"),
        (400.0, "α"),
        (400.0, "β"),
        (500.0, "β"),
        (600.0, "β"),
        (700.0, "β"),
        (800.0, "β"),
        (900.0, "β"),
        (1000.0, "β"),
        (1100.0, "β"),
        (1200.0, "β"),
        (1300.0, "β"),
        (1400.0, "β"),
    ]

    T0 = 298.15
    S0 = 125.5
    T_tr = 400.0
    dH_tr = 6570.0

    def Cp_alpha(T):
        return 58.6 + 0.0774 * T

    def H_alpha(T):
        if T == T0:
            return 0.0
        return 58.6 * (T - T0) + 0.0387 * (T**2 - T0**2)

    def S_alpha(T):
        if T == T0:
            return S0
        return S0 + 58.6 * math.log(T / T0) + 0.0774 * (T - T0)

    gold = {}

    # alpha at 400 to compute initial beta values
    H_a400 = H_alpha(T_tr)
    S_a400 = S_alpha(T_tr)
    Cp_beta = 82.9

    # beta at 400
    H_b400 = H_a400 + dH_tr
    S_b400 = S_a400 + dH_tr / T_tr

    for T, phase in required_rows:
        if phase == "α":
            if T == 298.15:
                H = 0.0
                S = S0
                Cp = Cp_alpha(T)
            else:
                H = H_alpha(T)
                S = S_alpha(T)
                Cp = Cp_alpha(T)
            Phi = S - H / T
        else:  # β
            if T == 400.0:
                H = H_b400
                S = S_b400
                Cp = Cp_beta
            else:
                H = H_b400 + Cp_beta * (T - T_tr)
                S = S_b400 + Cp_beta * math.log(T / T_tr)
                Cp = Cp_beta
            Phi = S - H / T
        gold[(T, phase)] = {"Cp": Cp, "H": H, "S": S, "Phi": Phi}

    phi_alpha_400_gold = gold[(400.0, "α")]["Phi"]
    phi_beta_400_gold = gold[(400.0, "β")]["Phi"]

    return {"gold": gold, "phi_alpha_400": phi_alpha_400_gold, "phi_beta_400": phi_beta_400_gold}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = ctx["gold"]
    tolerances = {"Cp": 0.5, "H": 20.0, "S": 0.5, "Phi": 0.2}

    # build index from artifact
    artifact_rows = {}
    for row in artifact:
        try:
            t = float(row["T"])
            phase = row["Phase"].strip()
        except:
            continue
        artifact_rows[(t, phase)] = row

    good = 0
    total = 0
    for key, gold_vals in gold.items():
        row = artifact_rows.get(key)
        if row is None:
            total += 1
            continue
        total += 1
        ok = True
        for field in ["Cp", "H", "S", "Phi"]:
            try:
                val = float(row[field])
            except:
                ok = False
                break
            if abs(val - gold_vals[field]) > tolerances[field]:
                ok = False
                break
        if ok:
            good += 1

    score = good / total if total > 0 else 0.0
    return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    phi_a_gold = ctx["phi_alpha_400"]
    phi_b_gold = ctx["phi_beta_400"]

    phi_alpha = artifact.get("phi_alpha_400")
    phi_beta = artifact.get("phi_beta_400")
    match_val = artifact.get("match")

    if phi_alpha is None or phi_beta is None or match_val is None:
        return 0.0

    try:
        phi_alpha = float(phi_alpha)
        phi_beta = float(phi_beta)
    except:
        return 0.0

    if match_val != True:
        return 0.0
    if abs(phi_alpha - phi_beta) > 0.1:
        return 0.0
    if abs(phi_alpha - phi_a_gold) > 0.1 or abs(phi_beta - phi_b_gold) > 0.1:
        return 0.0
    return 1.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
