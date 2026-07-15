import os
import json
import csv

# === author imports / helpers ===
import json
import math

# Physical constants
k_B = 1.380649e-23          # J/K

# Atomic masses (amu)
M_Ti = 47.867
M_Ni = 58.693
M_Sn = 118.71
M_Al = 26.9815386

# Composition average masses
M_Ti_avg = 0.97*M_Ti + 0.03*M_Al
M_pure = (M_Ti + M_Ni + M_Sn) / 3.0
M_doped = (M_Ti_avg + M_Ni + M_Sn) / 3.0
n_atoms = 3

def compute_intrinsic_kappa(a0_angstrom, Theta_D_K, gamma, M, T):
    """Compute intrinsic lattice thermal conductivity via Morelli‑Slack (eqn 2).
    a0_angstrom: lattice parameter in Angstrom.
    Theta_D_K: Debye temperature in K.
    gamma: Gruneisen parameter.
    M: average atomic mass in amu.
    T: temperature in K.
    Returns kappa in W m^-1 K^-1."""
    V_cell = a0_angstrom**3            # Angstrom^3
    delta = V_cell / n_atoms            # volume per atom, Angstrom^3
    A = 2.43e-8 / (1.0 - 0.514/gamma + 0.228/(gamma**2))
    kappa = 100.0 * A * (M * (Theta_D_K**3) * (delta**(1.0/3.0))) / ((gamma**2) * (n_atoms**(2.0/3.0)) * T)
    return kappa

def compute_with_inclusions(kappa_intrinsic, a0_angstrom, vs, x=0.05, R=1e-9):
    """Apply inclusion scattering to obtain effective kappa.
    kappa_intrinsic: from eqn (2).
    a0_angstrom: lattice parameter (Angstrom), used to get volume per atom.
    vs: average sound velocity (m/s).
    x: inclusion volume fraction (0.05).
    R: inclusion radius (1 nm).
    Returns kappa_with_inclusions in W m^-1 K^-1."""
    V_cell_m3 = a0_angstrom**3 * 1e-30          # m^3
    delta_m3 = V_cell_m3 / n_atoms              # m^3
    C_v = 3.0 * k_B / delta_m3                  # J m^-3 K^-1
    tau_incl_inv = (3.0/2.0) * (x / R) * vs     # 1/s
    tau_matrix_inv = (C_v * vs**2) / (3.0 * kappa_intrinsic)
    tau_eff_inv = tau_matrix_inv + tau_incl_inv
    kappa_with = (1.0/3.0) * C_v * vs**2 / tau_eff_inv
    return kappa_with


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
    import os
    artifact_path = os.path.join(outputs_dir, 'lattice_thermal_conductivity_results.json')
    with open(artifact_path) as f:
        data = json.load(f)
    dft = data.get('DFT_parameters', {})
    params_pure = dft.get('TiNiSn', {})
    params_doped = dft.get('Ti0.97Al0.03NiSn', {})

    recomputed = {}
    def add_kappa(prefix, params, M):
        a0 = params['a0_angstrom']
        Theta = params['Theta_D_K']
        gamma = params['gamma']
        vs = params['vs_m_per_s']
        for T, label in [(300, '300K'), (700, '700K')]:
            k_int = compute_intrinsic_kappa(a0, Theta, gamma, M, T)
            k_with = compute_with_inclusions(k_int, a0, vs)
            recomputed[f'{prefix}_intrinsic_{label}'] = k_int
            recomputed[f'{prefix}_with_inclusions_{label}'] = k_with

    add_kappa('TiNiSn', params_pure, M_pure)
    add_kappa('Ti0.97Al0.03NiSn', params_doped, M_doped)

    ctx = {'recomputed': recomputed}
    return ctx


# === block: score_0 (check id='kappa_gold') ===
def score_0(artifact, step, ctx):
    gold = {
        'TiNiSn_intrinsic_300K': 19.9,
        'TiNiSn_intrinsic_700K': 8.5,
        'TiNiSn_with_inclusions_300K': 13.1,
        'TiNiSn_with_inclusions_700K': 7.0,
        'Ti0.97Al0.03NiSn_intrinsic_300K': 18.7,
        'Ti0.97Al0.03NiSn_intrinsic_700K': 8.0,
        'Ti0.97Al0.03NiSn_with_inclusions_300K': 12.5,
        'Ti0.97Al0.03NiSn_with_inclusions_700K': 6.6
    }
    recomputed = ctx['recomputed']
    scores = []
    for key, ref in gold.items():
        val = recomputed.get(key)
        if val is None:
            return 0.0
        err = abs(val - ref) / ref
        score = max(0.0, 1.0 - err / 0.3)
        scores.append(score)
    return sum(scores) / len(scores)


# === block: score_1 (check id='kappa_ordering') ===
def score_1(artifact, step, ctx):
    recomputed = ctx['recomputed']
    checks = []
    # intrinsic > with_inclusions for each composition and temperature
    for comp in ['TiNiSn', 'Ti0.97Al0.03NiSn']:
        for T in ['300K', '700K']:
            k_int = recomputed[f'{comp}_intrinsic_{T}']
            k_with = recomputed[f'{comp}_with_inclusions_{T}']
            checks.append(1.0 if k_int > k_with else 0.0)
    # reduction due to doping larger than for pure (mass-fluctuation effect)
    for T in ['300K', '700K']:
        red_pure = recomputed['TiNiSn_intrinsic_'+T] - recomputed['TiNiSn_with_inclusions_'+T]
        red_doped = recomputed['Ti0.97Al0.03NiSn_intrinsic_'+T] - recomputed['Ti0.97Al0.03NiSn_with_inclusions_'+T]
        checks.append(1.0 if red_doped > red_pure else 0.0)
    return sum(checks) / len(checks)


_SCORERS = {
    'kappa_gold': score_0,
    'kappa_ordering': score_1,
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
