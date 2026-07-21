import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math

def compute_matrix(A_prime, M0_mass, A_host, B_host, r0, e_esu, M_neighbor_mass):
    signs = [(1,1,1), (-1,-1,-1), (-1,1,1), (1,-1,-1), (1,-1,1), (-1,1,-1), (1,1,-1), (-1,-1,1)]
    n_atoms = 9
    pos = np.zeros((n_atoms, 3))
    for l, (sx,sy,sz) in enumerate(signs, start=1):
        pos[l] = np.array([sx, sy, sz]) * r0
    D = np.zeros((27,27))
    unit_short = e_esu**2 / (8 * r0**3)
    M0 = M0_mass
    M_n = M_neighbor_mass
    for i in range(n_atoms):
        qi = -1 if i==0 else 1
        Mi = M0 if i==0 else M_n
        for j in range(i+1, n_atoms):
            qj = -1 if j==0 else 1
            Mj = M0 if j==0 else M_n
            r_vec = pos[j] - pos[i]
            dist = np.linalg.norm(r_vec)
            if dist < 1e-20:
                continue
            factor = - (qi * qj * e_esu**2) / (dist**3)
            mass_scale = 1.0 / math.sqrt(Mi * Mj)
            block_c = np.zeros((3,3))
            for a in range(3):
                for b in range(3):
                    term = (r_vec[a] * r_vec[b] / dist**2) - (1 if a==b else 0)
                    block_c[a,b] = mass_scale * factor * term
            D[3*i:3*i+3, 3*j:3*j+3] += block_c
            D[3*j:3*j+3, 3*i:3*i+3] += block_c.T
    if M0 > 0:
        central_diag = (1.0 / M0) * unit_short * (8.0/3.0) * (A_prime + 2*B_host)
    else:
        central_diag = 0.0
    for a in range(3):
        D[3*0+a, 3*0+a] += central_diag
    D0l_blocks = []
    for l in range(1,9):
        r_vec = pos[l] - pos[0]
        dist = np.linalg.norm(r_vec)
        block = np.zeros((3,3))
        mass_scale = 1.0 / math.sqrt(M0 * M_n)
        factor = - mass_scale * unit_short
        for a in range(3):
            for b in range(3):
                term = (A_prime - B_host) * (r_vec[a] * r_vec[b] / dist**2) + B_host * (1 if a==b else 0)
                block[a,b] = factor * term
        D0l_blocks.append(block)
        D[0:3, 3*l:3*l+3] += block
        D[3*l:3*l+3, 0:3] += block.T
    for l in range(1,9):
        diag_n = (1.0 / M_n) * unit_short * (1.0/3.0) * (A_prime + 7*A_host + 16*B_host)
        for a in range(3):
            D[3*l+a, 3*l+a] += diag_n
    for l_idx, l in enumerate(range(1,9)):
        block = D0l_blocks[l_idx]
        for a in range(3):
            for b in range(a+1,3):
                val = - math.sqrt(M_n / M0) * block[a,b]
                D[3*l+a, 3*l+b] += val
                D[3*l+b, 3*l+a] += val
    return D


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


# === block: score_0 (check id='check_frequencies') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    r0 = 2.282e-8
    K_bulk = 1.441e11
    e_esu = 4.803e-10
    alpha = 1.7627
    M_neighbor_u = 132.9
    u_to_g = 1.660539e-24
    A_host = 3 * r0 * K_bulk * (8 * r0**3 / e_esu**2) + 2*alpha/(3*math.sqrt(3))
    B_host = -alpha/(3*math.sqrt(3))
    M_neighbor_g = M_neighbor_u * u_to_g
    A_prime_list = [4.7452, 4.0, 3.0, 2.0, 1.0, 0.5]
    impurities = ['H', 'D']
    mass_map = {'H':1.0, 'D':2.0}
    expected = []
    for a in A_prime_list:
        for imp in impurities:
            expected.append((a, imp))
    def get_frequency(A_prime, M0_u):
        M0_g = M0_u * u_to_g
        D = compute_matrix(A_prime, M0_g, A_host, B_host, r0, e_esu, M_neighbor_g)
        eigvals = np.linalg.eigvalsh(D)
        omega2 = np.max(eigvals)
        omega = math.sqrt(omega2)
        freq_13 = omega / 1e13
        return freq_13
    tolerance_rel = step.get("tolerance_relative", 0.001)
    passed = 0
    for a, imp in expected:
        row = None
        for r in rows:
            try:
                if abs(float(r.get("A_prime", 0)) - a) < 1e-8 and str(r.get("impurity", "")).strip().upper() == imp.upper():
                    row = r
                    break
            except:
                pass
        if row is None:
            continue
        try:
            freq_reported = float(row["frequency"])
        except:
            continue
        expected_freq = get_frequency(a, mass_map[imp])
        rel_diff = abs(freq_reported - expected_freq) / expected_freq if expected_freq > 0 else 1.0
        if rel_diff <= tolerance_rel:
            passed += 1
    score = passed / len(expected) if expected else 0.0
    return score


_SCORERS = {
    'check_frequencies': score_0,
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
