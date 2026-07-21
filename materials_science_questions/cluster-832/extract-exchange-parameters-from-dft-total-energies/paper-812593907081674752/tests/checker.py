import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def _lambda_k(kx):
    # In-plane structure factor for hexagonal (001) lattice with a=1, k_y=0.
    return 2.0 * (np.cos(kx) + 2.0 * np.cos(kx / 2.0))

def _build_eigenvalues(kx, S, Jb, Js, JI, Dpar, Dperp, npar, nperp, nup):
    """Return sorted positive magnon eigenvalues (Kelvin) for a single kx."""
    lck = _lambda_k(kx)
    lck_prime = 1.0  # inter-layer factor for kz=0
    Ak = 2.0 * S * Dpar   # omit dipolar (omega_M=0)
    Bk = 2.0 * S * (Js * (npar - lck) + Jb * nperp + JI * nup + Dperp)
    Ck = 2.0 * Jb * S * ((npar - lck) + 2.0 * nperp)
    Dk = -Jb * S * lck_prime
    Ek = -JI * S * lck_prime
    DE = Dk + 2.0 * Ek
    n = 8
    # Top-left block: -(A_k+B_k)I - C_k * T where T is tridiag with 1 on off-diags
    TL = -(Ak + Bk) * np.eye(n) - Ck * (np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1))
    TR = -DE * np.eye(n)
    BL = DE * np.eye(n)
    BR = (Ak + Bk) * np.eye(n)
    M = np.block([[TL, TR], [BL, BR]])
    vals = np.linalg.eigvals(M)
    # Take real part, drop small imaginary components, and sort
    vals = np.real(vals)
    pos_vals = sorted([v for v in vals if v > 1e-12])
    # Should yield exactly 8 positive eigenvalues
    if len(pos_vals) != n:
        # In case of numerical noise, take the 8 largest positive real parts
        pos_vals = sorted(vals[vals > 0])[-n:]
    return np.array(pos_vals)


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
        'S': 0.78,
        'Jb': 120.0,
        'Js': 70.0,
        'JI': 0.01,
        'Dpar': 0.6,
        'Dperp': 0.0,
        'npar': 6,
        'nperp': 3,
        'nup': 3,
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import numpy as np
    from collections import defaultdict

    artifacts = artifact  # list of dicts
    ctx_data = ctx  # constants dict

    if not isinstance(artifacts, list) or len(artifacts) == 0:
        return 0.0

    # Group by k_x
    kx_groups = defaultdict(list)
    for entry in artifacts:
        kx = float(entry['k_x'])
        b = int(entry['branch_index'])
        e = float(entry['energy'])
        kx_groups[kx].append((b, e))

    kxs = sorted(kx_groups.keys())
    if not kxs:
        return 0.0

    # Shape check: every k_x must have exactly 8 entries with branch indices 1..8
    shape_ok = True
    for kx, entries in kx_groups.items():
        branches = set(b for b, _ in entries)
        if len(entries) != 8 or branches != set(range(1, 9)):
            shape_ok = False
            break

    shape_score = 1.0 if shape_ok else 0.0

    # Acoustic mode check: lowest k_x (should be ~0) must have min energy <= 0.5 K
    acoustic_score = 0.0
    if shape_ok:
        min_kx = min(kxs)
        if min_kx <= 0.001:
            entries_at_0 = kx_groups[min_kx]
            min_energy = min(e for _, e in entries_at_0)
            if min_energy <= 0.5:
                acoustic_score = 1.0
        # If no zero kx, acoustic check fails; but we still may give partial if shape ok?
        # We'll keep at 0.

    # RMS deviation computation
    S, Jb, Js, JI = ctx_data['S'], ctx_data['Jb'], ctx_data['Js'], ctx_data['JI']
    Dpar, Dperp = ctx_data['Dpar'], ctx_data['Dperp']
    npar, nperp, nup = ctx_data['npar'], ctx_data['nperp'], ctx_data['nup']

    errs = []
    for kx in kxs:
        # Agent's energies sorted (we trust branch_index ordering but sort to be safe)
        agent_energies = sorted([e for _, e in kx_groups[kx]])
        # Reference eigenvalues
        ref_vals = _build_eigenvalues(kx, S, Jb, Js, JI, Dpar, Dperp, npar, nperp, nup)
        if len(agent_energies) != len(ref_vals):
            shape_score = 0.0  # inconsistent count
            break
        diff = np.array(agent_energies) - np.array(ref_vals)
        errs.extend(diff)

    rms = np.sqrt(np.mean(np.array(errs)**2)) if errs else float('inf')

    # RMS score: full credit if rms <= 2.0 K, linear decay to 0 at 10.0 K
    if rms <= 2.0:
        rms_score = 1.0
    else:
        rms_score = max(0.0, (10.0 - rms) / 8.0)

    # Combine with weights
    final_score = 0.1 * shape_score + 0.1 * acoustic_score + 0.8 * rms_score
    return float(final_score)


_SCORERS = {
    'step_01': score_0,
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
