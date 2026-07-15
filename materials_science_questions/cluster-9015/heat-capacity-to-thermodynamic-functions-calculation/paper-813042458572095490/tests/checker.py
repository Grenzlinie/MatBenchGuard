import os
import json
import csv

# === author imports / helpers ===
import math

# Physical constants (CODATA 2018)
R = 8.314462618   # J/(mol*K)
k = 1.380649e-23  # J/K
h = 6.62607015e-34 # J*s
c = 299792458     # m/s
N_A = 6.02214076e23 # 1/mol

def recompute_thermo(mol_params, T):
    mass = mol_params['mass_kg']
    I_prod = mol_params['I_product_SI']
    sigma = mol_params['sigma']
    freqs = mol_params['frequencies_cm_1']
    degs = mol_params['degeneracies']

    # translational
    q_trans = (2 * math.pi * mass * k * T / h**2) ** 1.5 * (k * T / 1e5)
    S_trans = R * (math.log(q_trans) - math.log(N_A) + 2.5)
    Cp_trans = 2.5 * R
    H_trans = 2.5 * R * T

    # rotational
    rot_factor = (8 * math.pi**2 * k * T) / (h**2)
    q_rot = (math.sqrt(math.pi) / sigma) * rot_factor ** 1.5 * math.sqrt(I_prod)
    S_rot = R * (math.log(q_rot) + 1.5)
    Cp_rot = 1.5 * R
    H_rot = 1.5 * R * T

    # vibrational
    S_vib = 0.0
    Cp_vib = 0.0
    H_vib = 0.0
    hc_over_k = h * c * 100.0 / k
    for nu, d in zip(freqs, degs):
        theta = nu * hc_over_k
        x = theta / T
        exp_x = math.exp(x)
        expm1_x = exp_x - 1.0
        U_diff = R * theta / expm1_x
        S_mode = d * R * (x / expm1_x - math.log(1.0 - math.exp(-x)))
        C_mode = d * R * (x**2) * exp_x / (expm1_x**2)
        H_vib += d * U_diff
        S_vib += S_mode
        Cp_vib += C_mode

    S = S_trans + S_rot + S_vib
    Cp = Cp_trans + Cp_rot + Cp_vib
    H_total = H_trans + H_rot + H_vib   # J/mol
    H_kJ = H_total / 1e3
    Phi = S - H_total / T               # J/(mol*K)
    return {'Cp': Cp, 'S': S, 'Phi': Phi, 'H_minus_H0': H_kJ}


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
    constants = spec.get('constants', {})
    tolerances = spec.get('tolerances', {})
    temps = spec.get('temperature_points', [])
    return {'constants': constants, 'tolerances': tolerances, 'temps': temps}


# === block: score_0 (check id='compute_thermo') ===
def score_0(artifact, step, ctx):
    tol = ctx['tolerances']
    temps = ctx['temps']
    consts = ctx['constants']
    mol_names = ['YF3', 'Y2F6']
    total_fields = len(temps) * len(mol_names) * 4
    correct = 0
    row_map = {}
    for row in artifact:
        mol = row.get('molecule', '').strip()
        try:
            T = float(row.get('T'))
        except (ValueError, TypeError):
            continue
        key = (mol, T)
        if key not in row_map:
            row_map[key] = row
    for mol in mol_names:
        mp = consts[mol]
        for T in temps:
            expected = recompute_thermo(mp, T)
            key = (mol, T)
            if key not in row_map:
                continue
            row = row_map[key]
            for col, ref in expected.items():
                agent_str = row.get(col)
                if agent_str is None:
                    continue
                try:
                    agent_val = float(agent_str)
                except:
                    continue
                t = tol.get(col, 0.2 if col != 'H_minus_H0' else 0.05)
                if abs(agent_val - ref) <= t:
                    correct += 1
    score = correct / total_fields if total_fields > 0 else 0.0
    return score


_SCORERS = {
    'compute_thermo': score_0,
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
