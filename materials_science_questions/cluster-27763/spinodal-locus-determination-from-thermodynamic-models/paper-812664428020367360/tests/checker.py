import os
import json
import csv

# === author imports / helpers ===
import json, math


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
        "N_exp": 1000,
        "u_exp": 0.1,
        "tol_rel": 1e-3,
        "tol_phi_coil": 1e-6,
        "tol_nphi_self": 1e-4,
        "tol_equal": 1e-2
    }


# === block: score_0 (check id='step_01_binodal') ===
def score_0(artifact, step, ctx):
    import math

    def NPhi_flower(phi, a, U):
        return math.log(1000 * math.pi / 2.0) + 0.5 * math.log(1.0 - phi*phi) + 2.0*a*a/(1.0-phi) + U*(1.0-phi)/2.0

    def NPhi_coil_exact(a, U):
        return -math.log(max(math.erf(a), 1e-300)) + U

    def find_z0_star_true(N, u):
        U = u * N
        Rg = math.sqrt(N/6.0)
        def delta(a):
            # flower min
            best_phi = 0.0
            best_val = float('inf')
            for i in range(200):
                phi = -0.999 + i * 1.998/199
                val = NPhi_flower(phi, a, U)
                if val < best_val:
                    best_val = val
                    best_phi = phi
            # refine
            for _ in range(5):
                lo = max(-0.999, best_phi - 0.05)
                hi = min(0.999, best_phi + 0.05)
                best = best_val
                for j in range(200):
                    phi = lo + j*(hi-lo)/199
                    val = NPhi_flower(phi, a, U)
                    if val < best:
                        best = val
                        best_phi = phi
                best_val = best
            val_coil = NPhi_coil_exact(a, U)
            return best_val - val_coil
        a_lo, a_hi = 0.01, 10.0
        d_lo = delta(a_lo)
        d_hi = delta(a_hi)
        while d_lo*d_hi > 0:
            if d_lo < 0:
                a_lo = a_hi
                a_hi *= 2.0
                d_lo = d_hi
                d_hi = delta(a_hi)
            else:
                a_hi = a_lo
                a_lo *= 0.5
                d_hi = d_lo
                d_lo = delta(a_lo)
        for _ in range(80):
            a_mid = (a_lo + a_hi)/2.0
            d_mid = delta(a_mid)
            if abs(d_mid) < 1e-12:
                a_star = a_mid
                break
            if d_lo * d_mid < 0:
                a_hi = a_mid
                d_hi = d_mid
            else:
                a_lo = a_mid
                d_lo = d_mid
        else:
            a_star = (a_lo + a_hi)/2.0
        z0_star = a_star * 2 * Rg
        return z0_star

    art = artifact  # artifact is the parsed dict from binodal_result.json
    ctx_params = ctx

    expected_N = ctx_params['N_exp']
    expected_u = ctx_params['u_exp']
    tol_rel = ctx_params['tol_rel']
    tol_phi_coil = ctx_params['tol_phi_coil']
    tol_nphi_self = ctx_params['tol_nphi_self']
    tol_equal = ctx_params['tol_equal']

    score_N = 0.0
    score_u = 0.0
    if art.get('N') == expected_N:
        score_N = 0.02
    else:
        score_N = 0.0
    if abs(art.get('u', float('nan')) - expected_u) < 1e-9:
        score_u = 0.03
    else:
        score_u = 0.0

    # compute true binodal
    N_art = art.get('N')
    u_art = art.get('u')
    try:
        z0_true = find_z0_star_true(N_art, u_art) if (N_art and u_art is not None) else float('nan')
    except Exception:
        z0_true = float('nan')

    z0_agent = art.get('z0_star')
    score_z0 = 0.0
    if z0_agent is not None and math.isfinite(z0_true):
        err_rel = abs(z0_agent - z0_true) / (abs(z0_true) + 1e-12)
        if err_rel <= tol_rel:
            score_z0 = 0.6
        else:
            # linear decay
            score_z0 = max(0.0, 0.6 * (1.0 - (err_rel - tol_rel) / (10*tol_rel)))
    else:
        score_z0 = 0.0

    # coil minimum consistency
    coil = art.get('coil_minimum', {})
    score_coil = 0.0
    if isinstance(coil, dict) and 'phi' in coil and 'NPhi' in coil:
        phi_c = coil.get('phi')
        nphi_c = coil.get('NPhi')
        if phi_c is not None and abs(phi_c - (-1.0)) < tol_phi_coil:
            try:
                a = (z0_agent) / (2 * math.sqrt(N_art/6.0)) if z0_agent else 0.0
                U = u_art * N_art
                nphi_calc = NPhi_coil_exact(a, U)
                if abs(nphi_c - nphi_calc) / (abs(nphi_calc)+1e-12) < tol_nphi_self:
                    score_coil = 0.1
            except Exception:
                pass

    # flower minimum consistency
    flower = art.get('flower_minimum', {})
    score_flower = 0.0
    if isinstance(flower, dict) and 'phi' in flower and 'NPhi' in flower:
        phi_f = flower.get('phi')
        nphi_f = flower.get('NPhi')
        if phi_f is not None and phi_f > 0.0:
            try:
                a = (z0_agent) / (2 * math.sqrt(N_art/6.0)) if z0_agent else 0.0
                U = u_art * N_art
                nphi_calc = NPhi_flower(phi_f, a, U)
                if abs(nphi_f - nphi_calc) / (abs(nphi_calc)+1e-12) < tol_nphi_self:
                    score_flower = 0.1
            except Exception:
                pass

    # equality of minima depths
    score_equal = 0.0
    if isinstance(coil, dict) and isinstance(flower, dict) and 'NPhi' in coil and 'NPhi' in flower:
        nphi_c = coil.get('NPhi')
        nphi_f = flower.get('NPhi')
        if nphi_c is not None and nphi_f is not None:
            if abs(nphi_c - nphi_f) / (abs(nphi_c)+1e-12) < tol_equal:
                score_equal = 0.05

    total = score_N + score_u + score_z0 + score_coil + score_flower + score_equal
    return min(total, 1.0)


_SCORERS = {
    'step_01_binodal': score_0,
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
