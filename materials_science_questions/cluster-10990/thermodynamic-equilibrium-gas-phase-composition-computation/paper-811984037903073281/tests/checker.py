import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve
import csv
import io


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
    spec_steps = spec.get("steps", [])
    step_conf = {}
    for st in spec_steps:
        if st.get("id") == "solve_equilibrium":
            step_conf = st.get("config", {})
            break
    hidden_points = step_conf.get("hidden_test_points", [])
    species_order = step_conf["species_list"]

    # thermochemical data
    species_names = species_order
    data = {
        "NbOCl3": (-166.46, 112.2),
        "NbCl4":  (-114.92, 121.8),
        "NbCl5":  (-144.62, 145.2),
        "TeOCl2": (-31.00, 101.0),
        "TeCl2":  (-5.10, 86.0),
        "TeCl4":  (-32.45, 119.0),
        "TeO2":   (-6.20, 82.6),
        "TeO":    (22.82, 69.5),
        "Te2":    (46.44, 74.7),
        "Te":     (50.39, 49.7),
        "Cl2":    (6.06, 63.7),
        "Cl":     (32.73, 45.9),
        "O2":     (5.39, 58.2),
        "NbO2_f": (-177.20, 34.2),
    }
    idx = {name: i for i, name in enumerate(species_names)}

    reactions = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 1],  # (1)
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 1],  # (2)
        [0, -1, 1, 0, 0, 0, 0, 0, 0, 0, -0.5, 0, 0],  # (3)
        [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 1, 0, 0],  # (4)
        [0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, -0.5],  # (5)
        [0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1, 0, -1],  # (6)
        [0, 0, 0, 0, 0, 0, -1, 0, 0.5, 0, 0, 0, 1],  # (7)
        [0, 0, 0, 0, 0, 0, 0, -1, 0.5, 0, 0, 0, 0.5],  # (8)
        [0, 0, 0, 0, 0, 0, 0, 0, -1, 2, 0, 0, 0],  # (9)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 2, 0],  # (10)
    ]
    solid_coeff_vs_react = [2, 1, 0, 0, 0, 0, 0, 0, 0, 0]

    def compute_K(T):
        K = np.zeros(10)
        for i, coeffs in enumerate(reactions):
            dH_gas = sum(coeff * data[species_names[j]][0] for j, coeff in enumerate(coeffs))
            dS_gas = sum(coeff * data[species_names[j]][1] for j, coeff in enumerate(coeffs))
            if solid_coeff_vs_react[i] != 0:
                dH_s = solid_coeff_vs_react[i] * data["NbO2_f"][0]
                dS_s = solid_coeff_vs_react[i] * data["NbO2_f"][1]
                dH_R = dH_gas - dH_s
                dS_R = dS_gas - dS_s
            else:
                dH_R = dH_gas
                dS_R = dS_gas
            lgK = dS_R / 4.574 - dH_R / (4.574 * T)
            K[i] = 10 ** lgK
        return K

    def constraint_func(p, T, pO2_target):
        K = compute_K(T)
        eqs = np.zeros(13)
        i_NbOCl3 = idx["NbOCl3"]; i_NbCl4 = idx["NbCl4"]; i_NbCl5 = idx["NbCl5"]
        i_TeOCl2 = idx["TeOCl2"]; i_TeCl2 = idx["TeCl2"]; i_TeCl4 = idx["TeCl4"]
        i_TeO2 = idx["TeO2"]; i_TeO = idx["TeO"]; i_Te2 = idx["Te2"]; i_Te = idx["Te"]
        i_Cl2 = idx["Cl2"]; i_Cl = idx["Cl"]; i_O2 = idx["O2"]
        eqs[0] = p[i_NbOCl3]**2 * p[i_O2] - K[0] * p[i_Cl2]**3
        eqs[1] = p[i_NbCl4] * p[i_O2] - K[1] * p[i_Cl2]**2
        eqs[2] = p[i_NbCl5] - K[2] * p[i_NbCl4] * p[i_Cl2]**0.5
        eqs[3] = p[i_TeCl2] * p[i_Cl2] - K[3] * p[i_TeCl4]
        eqs[4] = p[i_TeOCl2] - K[4] * p[i_TeCl2] * p[i_O2]**0.5
        eqs[5] = p[i_TeO2] * p[i_Cl2] - K[5] * p[i_TeCl2] * p[i_O2]
        eqs[6] = p[i_Te2]**0.5 * p[i_O2] - K[6] * p[i_TeO2]
        eqs[7] = p[i_Te2]**0.5 * p[i_O2]**0.5 - K[7] * p[i_TeO]
        eqs[8] = p[i_Te]**2 - K[8] * p[i_Te2]
        eqs[9] = p[i_Cl]**2 - K[9] * p[i_Cl2]
        eqs[10] = sum(p) - 1.0
        pCl_star = (3*p[i_NbOCl3] + 4*p[i_NbCl4] + 5*p[i_NbCl5] +
                    2*p[i_TeOCl2] + 2*p[i_TeCl2] + 4*p[i_TeCl4] +
                    2*p[i_Cl2] + 1*p[i_Cl])
        pTe_star = (1*p[i_TeOCl2] + 1*p[i_TeCl2] + 1*p[i_TeCl4] +
                    1*p[i_TeO2] + 1*p[i_TeO] + 2*p[i_Te2] + 1*p[i_Te])
        eqs[11] = pCl_star - 4.0 * pTe_star
        eqs[12] = p[i_O2] - pO2_target
        return eqs

    def solve_composition(T, pO2_target):
        guess = np.zeros(13)
        guess[idx["NbOCl3"]] = 0.35
        guess[idx["Te2"]] = 0.4
        guess[idx["Te"]] = 0.1
        guess[idx["O2"]] = pO2_target
        guess[idx["Cl2"]] = 0.01
        guess[idx["Cl"]] = 0.01
        guess[idx["NbCl4"]] = 0.005
        guess[idx["NbCl5"]] = 0.005
        guess[idx["TeCl2"]] = 0.005
        guess[idx["TeCl4"]] = 0.005
        guess[idx["TeOCl2"]] = 0.005
        guess[idx["TeO2"]] = 0.005
        guess[idx["TeO"]] = 0.005
        s = sum(guess)
        guess = guess / s
        sol = fsolve(lambda p: constraint_func(p, T, pO2_target), guess, maxfev=2000, xtol=1e-12)
        sol[sol < 0] = 1e-30
        return sol.tolist()

    boundary_params = {
        "upper": (11.5965, 37452),
        "lower": (10.1624, 38951)
    }

    expected = {}
    for pt in hidden_points:
        T = pt["T"]
        b = pt["boundary"]
        A, B = boundary_params[b]
        log10_pO2 = A - B / T
        pO2 = 10 ** log10_pO2
        pres = solve_composition(T, pO2)
        expected[(T, b)] = pres

    return {
        "expected": expected,
        "species_order": species_order,
        "valid_points": hidden_points
    }


# === block: score_0 (check id='solve_equilibrium') ===
def score_0(artifact, step, ctx):
    expected_lookup = ctx["expected"]
    species_order = ctx["species_order"]
    valid_points = ctx["valid_points"]

    agent_lookup = {}
    for row in artifact:
        try:
            T = int(row["T"])
            boundary = str(row["boundary"]).strip()
            species = str(row["species"]).strip()
            p = float(row["p"])
            agent_lookup.setdefault((T, boundary), {})[species] = p
        except (ValueError, KeyError):
            continue

    for pt in valid_points:
        key = (pt["T"], pt["boundary"])
        if key not in agent_lookup:
            return 0.0

    total_rel_error = 0.0
    count = 0
    dominance_hits = 0
    floor = 1e-10

    for pt in valid_points:
        T = pt["T"]; b = pt["boundary"]
        key = (T, b)
        agent_dict = agent_lookup[key]
        gold_pres = expected_lookup.get(key)
        if gold_pres is None:
            return 0.0
        max_species = max(agent_dict.items(), key=lambda x: x[1])[0]
        if max_species in ("NbOCl3", "Te2", "Te"):
            dominance_hits += 1
        for sp_name, p_agent in agent_dict.items():
            if sp_name not in species_order:
                continue
            idx_s = species_order.index(sp_name)
            p_gold = gold_pres[idx_s]
            if p_gold < floor:
                continue
            rel_err = abs(p_agent - p_gold) / p_gold
            total_rel_error += rel_err
            count += 1

    if count == 0:
        return 0.0

    avg_rel_error = total_rel_error / count
    pressure_score = max(0.0, 1.0 - avg_rel_error / 0.05)
    dominance_score = dominance_hits / len(valid_points)
    return 0.8 * pressure_score + 0.2 * dominance_score


_SCORERS = {
    'solve_equilibrium': score_0,
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
