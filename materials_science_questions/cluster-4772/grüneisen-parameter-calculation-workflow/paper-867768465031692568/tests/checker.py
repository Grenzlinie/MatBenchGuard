import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import json


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
    return {
        'conditions': spec['conditions']
    }


# === block: score_0 (check id='eigenenergies') ===
def score_0(artifact, step, ctx):
    c_params = ctx['conditions']

    # single-site operators
    c_up = np.array([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]], dtype=complex)
    c_down = np.array([[0,0,1,0],[0,0,0,-1],[0,0,0,0],[0,0,0,0]], dtype=complex)
    c_up_dag = c_up.T.conj()
    c_down_dag = c_down.T.conj()
    n_up   = c_up_dag @ c_up
    n_down = c_down_dag @ c_down
    n_tot  = n_up + n_down
    n_up_dn = n_up @ n_down
    S_z = 0.5 * (n_up - n_down)
    I4 = np.eye(4, dtype=complex)

    def build_ham(U, H, V, mu):
        H_hop = -1.0 * (np.kron(c_up_dag, c_up) + np.kron(c_up, c_up_dag) + np.kron(c_down_dag, c_down) + np.kron(c_down, c_down_dag))
        H_U = U * (np.kron(n_up_dn, I4) + np.kron(I4, n_up_dn))
        H_mag = -H * (np.kron(S_z, I4) + np.kron(I4, S_z))
        H_elec = -V * (np.kron(n_tot, I4) - np.kron(I4, n_tot))
        H_mu = -mu * (np.kron(n_tot, I4) + np.kron(I4, n_tot))
        return H_hop + H_U + H_mag + H_elec + H_mu

    # parse artifact
    cond_list = artifact['conditions']
    total = 0
    ok = 0
    for c in c_params:
        cond_id = c['id']
        U = c['U']; H = c['H']; E = c['E']; T = c['T']
        V = E / 2.0
        mu = U / 2.0
        Hmat = build_ham(U, H, V, mu)
        evals, _ = np.linalg.eigh(Hmat)
        gold_evals = np.sort(evals.real)
        agent_data = next((x for x in cond_list if x['condition_id'] == cond_id), None)
        if agent_data is None:
            continue
        agent_evals = np.sort(np.array(agent_data['eigenenergies']))
        total += len(gold_evals)
        ok += np.sum(np.isclose(agent_evals, gold_evals, rtol=1e-5, atol=1e-10))
    return ok / total if total > 0 else 0.0


# === block: score_1 (check id='thermo') ===
def score_1(artifact, step, ctx):
    c_params = ctx['conditions']

    # single-site operators (same as in eigenenergies scorer)
    c_up = np.array([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]], dtype=complex)
    c_down = np.array([[0,0,1,0],[0,0,0,-1],[0,0,0,0],[0,0,0,0]], dtype=complex)
    c_up_dag = c_up.T.conj()
    c_down_dag = c_down.T.conj()
    n_up   = c_up_dag @ c_up
    n_down = c_down_dag @ c_down
    n_tot  = n_up + n_down
    n_up_dn = n_up @ n_down
    S_z = 0.5 * (n_up - n_down)
    I4 = np.eye(4, dtype=complex)

    def build_ham(U, H, V, mu):
        H_hop = -1.0 * (np.kron(c_up_dag, c_up) + np.kron(c_up, c_up_dag) + np.kron(c_down_dag, c_down) + np.kron(c_down, c_down_dag))
        H_U = U * (np.kron(n_up_dn, I4) + np.kron(I4, n_up_dn))
        H_mag = -H * (np.kron(S_z, I4) + np.kron(I4, S_z))
        H_elec = -V * (np.kron(n_tot, I4) - np.kron(I4, n_tot))
        H_mu = -mu * (np.kron(n_tot, I4) + np.kron(I4, n_tot))
        return H_hop + H_U + H_mag + H_elec + H_mu

    def compute_thermo(U, H, V, T, mu):
        Hmat = build_ham(U, H, V, mu)
        evals, evecs = np.linalg.eigh(Hmat)
        idx = np.argsort(evals.real)
        evals = evals.real[idx]
        evecs = evecs[:, idx]
        beta = 1.0 / T
        exponentials = np.exp(-beta * evals)
        Z = np.sum(exponentials)
        p = exponentials / Z
        E_mean = np.dot(p, evals)
        S = np.log(Z) + E_mean / T
        C = (np.dot(p, evals**2) - E_mean**2) / (T**2)
        rho = evecs @ np.diag(p) @ evecs.T.conj()
        M_op = np.kron(S_z, I4) + np.kron(I4, S_z)
        M = np.trace(rho @ M_op).real
        P_op = np.kron(n_tot, I4) - np.kron(I4, n_tot)
        P = np.trace(rho @ P_op).real
        return Z.real, S.real, C.real, M, P

    cond_list = artifact['conditions']
    total = 0
    ok = 0
    step = 1e-6
    for c in c_params:
        cond_id = c['id']
        U = c['U']; H = c['H']; E = c['E']; T = c['T']
        V = E / 2.0
        mu = U / 2.0
        _, gold_S, gold_C, gold_M, gold_P = compute_thermo(U, H, V, T, mu)
        # deltaS_MCE: S(H=0, E)
        _, S_H0, _, _, _ = compute_thermo(U, 0.0, V, T, mu)
        gold_deltaS_MCE = S_H0 - gold_S
        # deltaS_ECE: S(H, E=0)
        _, S_E0, _, _, _ = compute_thermo(U, H, 0.0, T, mu)
        gold_deltaS_ECE = S_E0 - gold_S
        # Gruneisen ratios via finite difference
        _, S_plus, _, _, _ = compute_thermo(U, H + step, V, T, mu)
        _, S_minus, _, _, _ = compute_thermo(U, H - step, V, T, mu)
        dS_dH = (S_plus - S_minus) / (2 * step)
        gold_GH = -dS_dH / gold_C
        _, S_ep, _, _, _ = compute_thermo(U, H, (E + step)/2, T, mu)
        _, S_em, _, _, _ = compute_thermo(U, H, (E - step)/2, T, mu)
        dS_dE = (S_ep - S_em) / (2 * step)
        gold_GE = -dS_dE / gold_C
        golds = {
          'entropy': gold_S,
          'specific_heat': gold_C,
          'magnetization': gold_M,
          'polarization': gold_P,
          'deltaS_MCE': gold_deltaS_MCE,
          'deltaS_ECE': gold_deltaS_ECE,
          'magnetic_Gruneisen_ratio': gold_GH,
          'electric_Gruneisen_ratio': gold_GE
        }
        agent_data = next((x for x in cond_list if x['condition_id'] == cond_id), None)
        if agent_data is None:
            continue
        for key, gval in golds.items():
            aval = agent_data.get(key)
            if aval is None:
                continue
            total += 1
            if np.isclose(aval, gval, rtol=1e-4, atol=1e-10) or (abs(gval) < 1e-12 and abs(aval) < 1e-12):
                ok += 1
    return ok / total if total > 0 else 0.0


_SCORERS = {
    'eigenenergies': score_0,
    'thermo': score_1,
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
