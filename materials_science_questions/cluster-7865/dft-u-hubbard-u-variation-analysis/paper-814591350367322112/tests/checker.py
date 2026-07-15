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
    def prepare(outputs_dir, spec):
        # find the step with id 'exchange_couplings'
        step = None
        for s in spec.get('steps', []):
            if s['id'] == 'exchange_couplings':
                step = s
                break
        if step is None:
            raise ValueError('Missing grading step exchange_couplings')
        fields = step['fields']
        return {'fields': fields}


# === block: score_0 (check id='exchange_couplings') ===
def score_0(artifact, step, ctx):
    import numpy as np

    def score(artifact, step, ctx):
        fields = ctx.get('fields', [])
        if not isinstance(artifact, dict):
            return 0.0
        n_total = len(fields)
        if n_total == 0:
            return 1.0
        # Gold match
        n_correct = 0
        for f in fields:
            name = f['name']
            gold = f['gold']
            tol = f['tolerance']
            val = artifact.get(name)
            if val is None:
                continue
            try:
                val = float(val)
            except (ValueError, TypeError):
                continue
            if abs(val - gold) <= tol:
                n_correct += 1
        gold_frac = n_correct / n_total

        # Spin-wave stability check
        # Lattice constants (conventional cell)
        a = 4.421
        c = 2.918

        # Read J values
        J1 = artifact.get('J1', 0.0)
        J2 = artifact.get('J2', 0.0)
        J3 = artifact.get('J3', 0.0)
        J4 = artifact.get('J4', 0.0)
        J5 = artifact.get('J5', 0.0)
        J6 = artifact.get('J6', 0.0)
        J7_l = artifact.get('J7_less', 0.0)
        J7_g = artifact.get('J7_greater', 0.0)
        J8_l = artifact.get('J8_less', 0.0)
        J8_g = artifact.get('J8_greater', 0.0)

        # Intra-sublattice shells (J, multiplicity, (dx,dy,dz) in conv. frac. coords)
        intra_shells = [
            (J1, 4, (1,0,0)),
            (J3, 4, (1,1,0)),
            (J4, 2, (0,0,1)),
            (J5, 4, (2,0,0)),
            (J6, 4, (2,2,0)),
        ]
        # Inter-sublattice shells
        inter_shells = [
            (J2, 8, (0.5,0.5,0.5)),
            (J7_l, 4, (0.5,0.5,1.5)),
            (J7_g, 4, (0.5,0.5,2.5)),
            (J8_l, 4, (0.5,0.5,-0.5)),
            (J8_g, 4, (0.5,0.5,-1.5)),
        ]

        def J11_q(h,k,l, shells):
            s = 0.0
            for J, mult, (dx,dy,dz) in shells:
                s += J * mult * np.cos(2*np.pi*(dx*h + dy*k + dz*l))
            return s

        def J12_q(h,k,l, shells):
            s = 0.0 + 0.0j
            for J, mult, (dx,dy,dz) in shells:
                phase = 2*np.pi*(dx*h + dy*k + dz*l)
                s += J * mult * np.exp(1j*phase)
            return s

        def J0_val(intra, inter):
            s = 0.0
            for J, mult, _ in intra:
                s += J * mult
            for J, mult, _ in inter:
                s += J * mult
            return s

        # q-point grid (high symmetry + sampling)
        q_points = []
        for h in np.linspace(0, 0.5, 20):
            q_points.append((h, 0.0, 0.0))
        for k in np.linspace(0, 0.5, 20):
            q_points.append((0.5, k, 0.0))
        for l in np.linspace(0, 0.5, 20):
            q_points.append((0.5, 0.5, l))
        for t in np.linspace(0,1,20):
            q_points.append((0.5*(1-t), 0.5*(1-t), 0.5))
        for h in [0.2,0.4,0.6,0.8]:
            for k in [0.2,0.4,0.6,0.8]:
                for l in [0.2,0.4,0.6,0.8]:
                    q_points.append((h,k,l))

        J00 = J0_val(intra_shells, inter_shells)

        # Original J set
        eigenvals = []
        for h,k,l in q_points:
            J11 = J11_q(h,k,l, intra_shells)
            J12 = J12_q(h,k,l, inter_shells)
            M = np.array([[J11 - J00, J12], [np.conj(J12), J11 - J00]])
            w = np.linalg.eigvalsh(M)
            eigenvals.extend(w.tolist())
        has_instability = any(w < -1e-6 for w in eigenvals)

        # With ΔJ2 correction
        J2_prime = J2 + 17.81
        inter_prime = [
            (J2_prime, 8, (0.5,0.5,0.5)),
            (J7_l, 4, (0.5,0.5,1.5)),
            (J7_g, 4, (0.5,0.5,2.5)),
            (J8_l, 4, (0.5,0.5,-0.5)),
            (J8_g, 4, (0.5,0.5,-1.5)),
        ]
        J00_prime = J0_val(intra_shells, inter_prime)
        eigenvals_prime = []
        for h,k,l in q_points:
            J11 = J11_q(h,k,l, intra_shells)
            J12 = J12_q(h,k,l, inter_prime)
            M = np.array([[J11 - J00_prime, J12], [np.conj(J12), J11 - J00_prime]])
            w = np.linalg.eigvalsh(M)
            eigenvals_prime.extend(w.tolist())
        stability_achieved = all(w >= -1e-6 for w in eigenvals_prime)

        spinwave_ok = has_instability and stability_achieved

        # Combine: 80% J_i match, 20% spin-wave check
        final_score = 0.8 * gold_frac + 0.2 * (1.0 if spinwave_ok else 0.0)
        return final_score


_SCORERS = {
    'exchange_couplings': score_0,
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
