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
        step = spec['steps'][0]  # single step task
        targets = step.get('hidden_targets', {})
        return {'targets': targets, 'tol_rel': step.get('tolerance_relative', 0.05)}


# === block: score_0 (check id='bubble_calculation_score') ===
def score_0(artifact, step, ctx):
        import math
        sigma = 1.200
        n_s0_mol_pct = 2.20e-3
        n_s0 = n_s0_mol_pct / 100.0
        epsilon_eV = 0.6027
        p0 = 1.0
        T = 300.0
        N_total = 2.0e23
        rho_bub = 1.0e13
        nu = 0.5
        kB_J = 1.380649e-23
        kB_eV = 8.617333262145e-5
        kT_eV = kB_eV * T
        kT_J = kB_J * T
        num = 3.0 * (nu**2) * n_s0 * (kT_eV**nu) * math.exp(-epsilon_eV / kT_eV)
        den = 64.0 * math.pi * (p0**nu) * (sigma**(1.0 - nu))
        frac = num / den
        r_b_star_m = 2.0 * (frac ** (1.0 / (nu + 2.0)))
        r_b_star_um = r_b_star_m * 1.0e6
        nb_star = (8.0 * math.pi / 3.0) * (sigma / kT_J) * (r_b_star_m ** 2)
        nt_star_per_bubble = ((nu + 2.0) / (nu**2)) * nb_star
        N_t_star = rho_bub * nt_star_per_bubble
        Delta = (N_total - N_t_star) / N_t_star
        c1 = nu / (nu + 2.0)
        c2 = 2.0 / (nu + 2.0)
        def f(x):
            return (Delta + 1.0) - c1 * (x**2) - c2 * (x**(-nu))
        lo = 1.0
        hi = 1.0
        while f(hi) > 0:
            hi *= 2.0
        for _ in range(200):
            mid = (lo + hi) / 2.0
            if f(mid) > 0:
                lo = mid
            else:
                hi = mid
        x_ref = (lo + hi) / 2.0
        r_eq_um_ref = x_ref * r_b_star_um
        tol_rel = 0.05
        def rel_score(val, ref, tol):
            if val is None or ref is None:
                return 0.0
            if abs(ref) < 1e-12:
                return 1.0 if abs(val) < 1e-12 else 0.0
            err = abs(val - ref) / abs(ref)
            return 1.0 if err <= tol else max(0.0, 1.0 - (err - tol) / (4 * tol))
        s_rb = rel_score(artifact.get('r_b_star_um'), r_b_star_um, tol_rel)
        s_rat = rel_score(artifact.get('ratio_r_eq_over_r_b_star'), x_ref, tol_rel)
        s_req = rel_score(artifact.get('r_eq_um'), r_eq_um_ref, tol_rel)
        return (s_rb + s_rat + s_req) / 3.0


_SCORERS = {
    'bubble_calculation_score': score_0,
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
