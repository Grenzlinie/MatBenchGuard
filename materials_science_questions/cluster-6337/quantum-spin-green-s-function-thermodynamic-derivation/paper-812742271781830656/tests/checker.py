import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy import integrate
import csv
import os


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
    def compute_gold():
        gold = {}
        # 1D analytic values
        sqrt2 = np.sqrt(2.0)
        pi = np.pi
        gold['linear_chain'] = {
            'energy': sqrt2/pi - 0.75,
            'occupation': 'Inf',
            'correlation': -sqrt2/(6.0*pi),
            'squared_magnetization': None   # not scored
        }

        # helper functions for 2D/3D
        def compute_lattice_obs(z, get_S_k, n_dims, nk):
            """Compute energy, occupation, correlation, squared_mag by discrete k-sum."""
            if n_dims == 2:
                ks = np.linspace(-np.pi, np.pi, nk, endpoint=False)
                KX, KY = np.meshgrid(ks, ks, indexing='ij')
                S = get_S_k(KX, KY)
                dk = (2*np.pi/nk)**2
                vol = (2*np.pi)**2
            else:  # 3D
                ks = np.linspace(-np.pi, np.pi, nk, endpoint=False)
                KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
                S = get_S_k(KX, KY, KZ)
                dk = (2*np.pi/nk)**3
                vol = (2*np.pi)**3

            # avoid division by zero or sqrt negative; small S deviations safe
            mask = S <= 2*z  # safe
            S_safe = S[mask]
            sqrt_term = np.sqrt(np.maximum(1.0 - S_safe / z, 0.0))

            # energy per site
            I1 = np.sum(sqrt_term) * dk / vol
            energy = -z/8.0 + (z/4.0) * (I1 - 1.0)

            # occupation: n = (1/N) sum sinh^2 u_k, cosh^2 u = (1/2)(1/sqrt(1 - S/(2z)))
            denom = 1.0 - S_safe/(2.0*z)
            denom = np.maximum(denom, 1e-15)
            sinh2 = 0.5 * (1.0/np.sqrt(denom) - 1.0)
            n_val = np.sum(sinh2) * dk / vol

            # out-of-plane nearest-neighbor correlation
            corr = np.sum(S_safe * sqrt_term) * dk / vol / (4.0 * z)

            # squared magnetization: (n - 0.5)^2
            sq_mag = (n_val - 0.5)**2

            return {'energy': energy, 'occupation': n_val,
                    'correlation': corr, 'squared_magnetization': sq_mag}

        # square lattice z=4, S(k) = 2*(cos kx + cos ky)
        def S_k_sq(kx, ky):
            return 2.0*(np.cos(kx) + np.cos(ky))
        obs_sq = compute_lattice_obs(4, S_k_sq, 2, nk=300)
        gold['square_lattice'] = obs_sq

        # simple cubic z=6, S(k) = 2*(cos kx + cos ky + cos kz)
        def S_k_cu(kx, ky, kz):
            return 2.0*(np.cos(kx) + np.cos(ky) + np.cos(kz))
        obs_cu = compute_lattice_obs(6, S_k_cu, 3, nk=200)
        gold['simple_cubic'] = obs_cu

        return {'gold': gold, 'tolerance': 1e-4}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import numpy as np

    COL_MAP = {
        'energy': 'energy_per_site',
        'occupation': 'occupation_number',
        'correlation': 'out_of_plane_correlation',
        'squared_magnetization': 'squared_magnetization',
    }

    def _compute_gold():
        gold = {}
        # 1D linear chain: numerical integration with fine k-grid
        def _compute_1d(nk=200000):
            ks = np.linspace(-np.pi, np.pi, nk, endpoint=False)
            S = 2 * np.cos(ks)
            sqrt_term = np.sqrt(np.maximum(1.0 - S/2, 0.0))
            I1 = np.mean(sqrt_term - 1.0)   # (1/N) Σ [√(1 - S/z) - 1]
            energy = -0.25 + 0.5 * I1        # -z/8 + (z/4)*I1, z=2
            corr = (1.0 / 8.0) * np.mean(S * sqrt_term)  # (1/(4z N)) Σ S√(1 - S/z), z=2
            return energy, corr
        en, corr = _compute_1d()
        gold['linear_chain'] = {
            'energy': en,
            'occupation': 'Inf',
            'correlation': corr,
            'squared_magnetization': None
        }

        def _compute_lattice(z, get_S, ndim, nk):
            if ndim == 2:
                ks = np.linspace(-np.pi, np.pi, nk, endpoint=False)
                KX, KY = np.meshgrid(ks, ks, indexing='ij')
                S = get_S(KX, KY)
                dk = (2*np.pi/nk)**2
                vol = (2*np.pi)**2
                mask = (S < 2*z - 1e-12)
                S_safe = S[mask]
            elif ndim == 3:
                ks = np.linspace(-np.pi, np.pi, nk, endpoint=False)
                KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
                S = get_S(KX, KY, KZ)
                dk = (2*np.pi/nk)**3
                vol = (2*np.pi)**3
                mask = (S < 2*z - 1e-12)
                S_safe = S[mask]

            sqrt_term = np.sqrt(np.maximum(1.0 - S_safe/z, 0.0))
            I1 = np.sum(sqrt_term) * dk / vol
            energy = -z/8.0 + (z/4.0)*(I1 - 1.0)

            t = (S_safe/(2*z)) / (1.0 - S_safe/(2*z))
            cosh2u = 1.0 / np.sqrt(np.maximum(1.0 - t*t, 1e-30))
            sinh2 = 0.5*(cosh2u - 1.0)
            n_val = np.sum(sinh2) * dk / vol

            corr = np.sum(S_safe * sqrt_term) * dk / vol / (4.0*z)
            sq_mag = (n_val - 0.5)**2
            return {
                'energy': energy,
                'occupation': n_val,
                'correlation': corr,
                'squared_magnetization': sq_mag,
            }

        def S2d(kx, ky):
            return 2.0*(np.cos(kx) + np.cos(ky))
        gold['square_lattice'] = _compute_lattice(4, S2d, 2, nk=400)

        def S3d(kx, ky, kz):
            return 2.0*(np.cos(kx) + np.cos(ky) + np.cos(kz))
        gold['simple_cubic'] = _compute_lattice(6, S3d, 3, nk=150)

        return gold

    GOLD = _compute_gold()
    TOL = 1e-4

    rows = artifact
    if not rows:
        return 0.0

    if any(c not in rows[0] for c in ['lattice', 'energy_per_site', 'occupation_number', 'out_of_plane_correlation', 'squared_magnetization']):
        return 0.0

    def is_inf(val):
        return isinstance(val, str) and val.strip().lower() == 'inf'

    comparisons = [
        ('linear_chain', 'energy', float),
        ('linear_chain', 'occupation', 'Inf'),
        ('linear_chain', 'correlation', float),
        ('square_lattice', 'energy', float),
        ('square_lattice', 'occupation', float),
        ('square_lattice', 'correlation', float),
        ('square_lattice', 'squared_magnetization', float),
        ('simple_cubic', 'energy', float),
        ('simple_cubic', 'occupation', float),
        ('simple_cubic', 'correlation', float),
        ('simple_cubic', 'squared_magnetization', float),
    ]

    passed = 0
    total = len(comparisons)

    for lat, qty, expected_type in comparisons:
        row = None
        for r in rows:
            if r.get('lattice', '').strip().lower() == lat:
                row = r
                break
        if row is None:
            continue

        gold_lat = GOLD[lat]
        gold_val = gold_lat[qty]
        csv_col = COL_MAP[qty]
        agent_val_str = row.get(csv_col, '').strip()

        if expected_type == 'Inf':
            if is_inf(agent_val_str):
                passed += 1
            continue

        try:
            agent_val = float(agent_val_str)
            if np.isinf(agent_val) or np.isnan(agent_val):
                continue
            if abs(agent_val - gold_val) <= TOL:
                passed += 1
        except (ValueError, TypeError):
            continue

    return passed / total if total > 0 else 0.0


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
