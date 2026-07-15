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
    k_B = 8.617333262145e-5
    nu = 25e12
    beta = 1.0
    E_diff = 0.18

    def solve_T_max(E_de):
        if E_de <= 0:
            return None
        lo, hi = 50.0, 2000.0
        for _ in range(80):
            mid = 0.5*(lo+hi)
            lhs = E_de/(k_B*mid*mid)
            rhs = (nu/beta)*math.exp(-E_de/(k_B*mid))
            if lhs > rhs:
                lo = mid
            else:
                hi = mid
        return (lo+hi)/2

    pure_V_seq = spec["steps"][2]["pure_V_trapping_sequence"]
    pure_V_Tmax = {}
    for n, Etrap in pure_V_seq:
        E_de = -Etrap + E_diff
        T = solve_T_max(E_de)
        pure_V_Tmax[n] = T

    Re1_V_Tmax = pure_V_Tmax

    ctx = {
        "gold_trapping": spec["steps"][0]["gold_values"],
        "gold_multiH": spec["steps"][1]["gold_values"],
        "max_retained_gold": spec["steps"][2]["max_number_retained_gold"],
        "pure_V_Tmax": pure_V_Tmax,
        "Re1_V_Tmax": Re1_V_Tmax,
        "k_B": k_B,
        "nu": nu,
        "beta": beta,
        "E_diff": E_diff,
        "solve_T_max": solve_T_max
    }
    return ctx


# === block: score_0 (check id='check_trapping_energies') ===
def score_0(artifact, step, ctx):
    tolerance = step.get("tolerance_eV", 0.2)
    gold = ctx["gold_trapping"]
    score = 0.0
    total = len(gold)
    if total == 0:
        return 1.0
    for g in gold:
        m = g["m"]
        row = None
        for r in artifact:
            if int(r.get("m", -1)) == m:
                row = r
                break
        if row is None:
            continue
        try:
            t = float(row["trapping_energy_eV"])
        except:
            continue
        try:
            mc = float(row["MC_eV"])
        except:
            continue
        try:
            ec = float(row["EC_eV"])
        except:
            continue
        if abs(t - g["trapping"]) <= tolerance and abs(mc - g["MC"]) <= tolerance and abs(ec - g["EC"]) <= tolerance:
            score += 1.0
    return score / total


# === block: score_1 (check id='check_multiH_Re4V') ===
def score_1(artifact, step, ctx):
    tolerance = step.get("tolerance_eV", 0.2)
    gold = ctx["gold_multiH"]
    score = 0.0
    total = len(gold)
    if total == 0:
        return 1.0
    for g in gold:
        n = g["n"]
        row = None
        for r in artifact:
            if int(r.get("n", -1)) == n:
                row = r
                break
        if row is None:
            continue
        try:
            t = float(row["trapping_energy_eV"])
        except:
            continue
        if abs(t - g["trapping"]) <= tolerance:
            score += 1.0
    row_max = None
    for r in artifact:
        if int(r.get("n", -1)) == 8:
            row_max = r
            break
    if row_max is not None:
        try:
            if float(row_max["trapping_energy_eV"]) > 0:
                score += 1.0
                total += 1
        except:
            pass
    return score / total


# === block: score_2 (check id='check_retention') ===
def score_2(artifact, step, ctx):
    re4v_file = os.path.join("/app/outputs", "multiH_Re4V_trapping_energies.csv")
    re4v_energies = {}
    if os.path.exists(re4v_file):
        with open(re4v_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                n = int(row["n"])
                e = float(row["trapping_energy_eV"])
                re4v_energies[n] = e

    def expected_Tmax(sys, n):
        if sys == "pure_V":
            return ctx["pure_V_Tmax"].get(n)
        elif sys == "Re1_V":
            return ctx["Re1_V_Tmax"].get(n)
        elif sys == "Re4_V":
            if n in re4v_energies:
                E_de = -re4v_energies[n] + ctx["E_diff"]
                return ctx["solve_T_max"](E_de)
            else:
                return None
        else:
            return None

    TOL = 50.0
    total_entries = 0
    ok = 0
    for row in artifact:
        sys = row.get("system", "").strip()
        n = int(row.get("n", -1))
        try:
            tmax = float(row.get("T_max_K", 0))
        except:
            tmax = None
        try:
            retained = str(row.get("retained_at_RT", "")).lower() in ["true", "1", "yes"]
        except:
            retained = False
        expected = expected_Tmax(sys, n)
        if expected is None:
            continue
        total_entries += 1
        if tmax is not None:
            correct_tmax = abs(tmax - expected) <= TOL
            correct_flag = (tmax > 300.0) == retained
        else:
            correct_tmax = False
            correct_flag = False
        if correct_tmax and correct_flag:
            ok += 1
    if total_entries == 0:
        return 0.0
    return ok / total_entries


_SCORERS = {
    'check_trapping_energies': score_0,
    'check_multiH_Re4V': score_1,
    'check_retention': score_2,
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
