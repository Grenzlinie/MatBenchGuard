import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
import json
import csv


def build_J_matrices(J=4):
    """Return Jx, Jy, Jz as matrices for given J."""
    dim = 2 * J + 1
    m_vals = np.arange(J, -J - 1, -1)
    jz = np.diag(m_vals)
    jplus = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        mi = J - i
        if mi < J:
            jplus[i, i + 1] = np.sqrt(J * (J + 1) - mi * (mi + 1))
    jminus = jplus.T.conj()
    jx = 0.5 * (jplus + jminus)
    jy = -0.5j * (jplus - jminus)
    return jx, jy, jz


def build_stevens_operators(jx, jy, jz, J=4):
    """Return Stevens operators O4^0 and O4^4 for given J."""
    jz2 = jz @ jz
    jz4 = jz2 @ jz2
    jj1 = J * (J + 1)
    # O4^0 formula: 35 Jz^4 - (30*J(J+1) - 25) Jz^2 + 3*J^2(J+1)^2 - 6*J(J+1)
    coeff_jz4 = 35.0
    coeff_jz2 = -(30.0 * jj1 - 25.0)
    coeff_id = 3.0 * jj1 * jj1 - 6.0 * jj1
    O4_0 = coeff_jz4 * jz4 + coeff_jz2 * jz2 + coeff_id * np.eye(2 * J + 1)
    # O4^4 = (1/2)(J_+^4 + J_-^4)
    jplus = jx + 1j * jy
    jminus = jplus.T.conj()
    jplus4 = np.linalg.matrix_power(jplus, 4)
    jminus4 = np.linalg.matrix_power(jminus, 4)
    O4_4 = 0.5 * (jplus4 + jminus4)
    return O4_0, O4_4


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    B4_meV = step['parameters']['B4_meV']
    tol_K = step['parameters']['tolerance_K']

    # Corrected angular momentum matrix generation for J=4 (descending m order)
    def _build_J_matrices(J=4):
        dim = 2 * J + 1
        m = np.arange(J, -J - 1, -1)
        jz = np.diag(m)
        jplus = np.zeros((dim, dim), dtype=complex)
        for i in range(1, dim):
            mi = m[i]
            jplus[i - 1, i] = np.sqrt(J * (J + 1) - mi * (mi + 1))
        jminus = jplus.T.conj()
        jx = 0.5 * (jplus + jminus)
        jy = -0.5j * (jplus - jminus)
        return jx, jy, jz

    def _build_O4_0(jz, J=4):
        jj1 = J * (J + 1)
        jz2 = jz @ jz
        jz4 = jz2 @ jz2
        coeff_id = 3.0 * jj1 * jj1 - 6.0 * jj1
        return 35.0 * jz4 - (30.0 * jj1 - 25.0) * jz2 + coeff_id * np.eye(2 * J + 1)

    def _build_O4_4(jplus, jminus):
        jplus4 = np.linalg.matrix_power(jplus, 4)
        jminus4 = np.linalg.matrix_power(jminus, 4)
        return 0.5 * (jplus4 + jminus4)

    # Patch the global build_J_matrices so that step_02 (and any other scorers) use the corrected version
    global build_J_matrices
    build_J_matrices = _build_J_matrices

    # Recompute reference eigenvalues
    jx, jy, jz = _build_J_matrices(4)
    O4_0 = _build_O4_0(jz, J=4)
    jplus = jx + 1j * jy
    jminus = jplus.T.conj()
    O4_4 = _build_O4_4(jplus, jminus)
    H_cef = B4_meV * (O4_0 + 5.0 * O4_4)
    # H_cef is Hermitian; use eigh for real symmetric, or eigvalsh
    eigvals_meV = np.linalg.eigvalsh(H_cef)
    eigvals_K = eigvals_meV * 11.604

    # Sort reference eigenvalues and group non-degenerate states with a small tolerance
    ref_idx = np.argsort(eigvals_K)
    ref_sorted = eigvals_K[ref_idx]

    # Extract agent energies
    if not isinstance(artifact, list) or len(artifact) != 9:
        return 0.0
    agent_energies = np.array([float(it['energy_K']) for it in artifact])
    agent_order = np.argsort(agent_energies)
    agent_sorted = agent_energies[agent_order]

    # Greedy matching within tolerance
    matched_ref = set()
    matched_agent = set()
    matches = 0
    for i_ref, e_ref in enumerate(ref_sorted):
        for i_agent, e_agent in enumerate(agent_sorted):
            if i_agent in matched_agent:
                continue
            if abs(e_agent - e_ref) <= tol_K:
                matches += 1
                matched_agent.add(i_agent)
                matched_ref.add(i_ref)
                break
    energy_score = matches / 9.0

    # Group agent sorted energies using tolerance to check degeneracy pattern
    group_tol = tol_K
    agent_groups = []
    if len(agent_sorted) > 0:
        cur = [agent_sorted[0]]
        for e in agent_sorted[1:]:
            if abs(e - cur[-1]) <= group_tol:
                cur.append(e)
            else:
                agent_groups.append(cur)
                cur = [e]
        agent_groups.append(cur)

    deg_score = 0.0
    expected_irreps = ['Γ1', 'Γ4', 'Γ3', 'Γ5']  # ordering for B4<0
    if len(agent_groups) == 4:
        agent_degs = [len(g) for g in agent_groups]
        if agent_degs == [1, 3, 2, 3]:
            agent_irreps = []
            for g in agent_groups:
                # find items from artifact whose energy falls within this group
                group_items = []
                for idx, it in enumerate(artifact):
                    val = float(it['energy_K'])
                    if any(abs(val - e) <= group_tol for e in g):
                        group_items.append(it)
                if not group_items:
                    break
                deg = int(group_items[0]['degeneracy'])
                irrep = str(group_items[0]['irrep'])
                if deg != len(g) or not all(
                    int(it.get('degeneracy', -1)) == deg and str(it.get('irrep', '')) == irrep
                    for it in group_items
                ):
                    break
                agent_irreps.append(irrep)
            else:
                if agent_irreps == expected_irreps:
                    deg_score = 1.0

    score = 0.8 * energy_score + 0.2 * deg_score
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    params = step['parameters']
    temps = params['temp_points']
    h = params['finite_diff_h']

    # recompute Hamiltonian and derivatives
    jx, jy, jz = build_J_matrices(4)
    O4_0, O4_4 = build_stevens_operators(jx, jy, jz, J=4)
    H0 = params['B4_meV'] * (O4_0 + 5.0 * O4_4)
    M = jx @ jy + jy @ jx
    eta3 = params['eta3_meV']

    def eig_sorted(e_strain):
        H = H0 + e_strain * eta3 * M
        return np.sort(np.linalg.eigvalsh(H))

    e0 = eig_sorted(0.0)
    e_plus = eig_sorted(h)
    e_minus = eig_sorted(-h)
    dE = (e_plus - e_minus) / (2.0 * h)
    d2E = (e_plus - 2.0 * e0 + e_minus) / (h * h)

    kB = 0.0861733  # meV/K
    N = params['N']
    conv = 1.602176634e-31  # meV * m^-3 -> GPa

    # compute C55 for each temperature
    expected_C55 = []
    for T in temps:
        beta = 1.0 / (kB * T)
        exp_factors = np.exp(-beta * e0)
        Z = np.sum(exp_factors)
        sum1 = np.sum(d2E * exp_factors)
        sum2 = np.sum((dE ** 2) * exp_factors)
        deltaC55_meV = (N * (sum1 / Z - beta * sum2 / Z))  # ignoring squared term
        deltaC55_GPa = deltaC55_meV * conv
        # Varshni background
        Cbg = params['C0_GPa'] - params['s_GPa'] / (math.exp(params['TE_K'] / T) - 1.0)
        C55 = Cbg + deltaC55_GPa
        expected_C55.append(C55)

    # extract agent's C55
    agent_mapping = {}
    for row in artifact:
        t = float(row['T_K'])
        agent_mapping[t] = float(row['C55_GPa'])

    if len(agent_mapping) != len(temps):
        return 0.0

    tol_rel = params['tolerance_rel']
    tol_abs = params['tolerance_abs_GPa']
    matches = 0
    for i, T in enumerate(temps):
        if T not in agent_mapping:
            continue
        a = agent_mapping[T]
        e = expected_C55[i]
        if abs(a - e) <= max(tol_rel * abs(e), tol_abs):
            matches += 1
    score = matches / len(temps)
    return score


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
