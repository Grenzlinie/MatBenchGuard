import os
import json
import csv


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
    import json, os
    data_path = os.path.join(outputs_dir, "step_01_results.json")
    data = None
    if os.path.exists(data_path):
        with open(data_path) as f:
            data = json.load(f)
    return {"data": data}


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    def score_formation(artifact, step, ctx):
        data = ctx.get("data")
        if data is None:
            return 0.0
        te = data.get("total_energies", {})
        if not isinstance(te, dict):
            return 0.0
        mg = te.get("Mg_hcp")
        si = te.get("Si_diamond")
        al = te.get("Al_fcc")
        beta_e = te.get("beta_phase")
        bpp_e = te.get("beta_prime_prime_phase")
        u1_e = te.get("U1_phase")
        u2_e = te.get("U2_phase")
        if any(v is None for v in [mg, si, al, beta_e, bpp_e, u1_e, u2_e]):
            return 0.0
        # stoichiometries (atoms per conventional cell)
        n_beta, x_mg_beta, x_si_beta, x_al_beta = 12, 8, 4, 0
        n_bpp, x_mg_bpp, x_si_bpp, x_al_bpp = 11, 5, 6, 0
        n_u1, x_mg_u1, x_si_u1, x_al_u1 = 5, 1, 2, 2
        n_u2, x_mg_u2, x_si_u2, x_al_u2 = 12, 4, 4, 4

        def form_E(comp_e, n, x_mg, x_si, x_al):
            dh_eV = (comp_e - (x_mg * mg + x_si * si + x_al * al)) / n
            return dh_eV * 1000.0 / 13.605698  # eV -> mRy/atom

        f_beta = form_E(beta_e, n_beta, x_mg_beta, x_si_beta, x_al_beta)
        f_bpp  = form_E(bpp_e,  n_bpp,  x_mg_bpp,  x_si_bpp,  x_al_bpp)
        f_u1   = form_E(u1_e,   n_u1,   x_mg_u1,   x_si_u1,   x_al_u1)
        f_u2   = form_E(u2_e,   n_u2,   x_mg_u2,   x_si_u2,   x_al_u2)

        ref = step["reference"]
        tol = step["tolerance_mRy_per_atom"]

        def comp(val, target):
            diff = abs(val - target)
            if diff <= tol:
                return 1.0
            elif diff <= 2 * tol:
                return 0.5
            else:
                return 0.0

        scores = [
            comp(f_beta, ref["beta"]),
            comp(f_bpp,  ref["beta_prime_prime"]),
            comp(f_u1,   ref["U1"]),
            comp(f_u2,   ref["U2"])
        ]
        return sum(scores) / len(scores)

    return score_formation(artifact, step, ctx)


# === block: score_1 (check id='bulk_moduli') ===
def score_1(artifact, step, ctx):
    def score_bulk_moduli(artifact, step, ctx):
        data = ctx.get("data")
        if data is None:
            return 0.0
        bm = data.get("bulk_moduli", {})
        if not isinstance(bm, dict):
            return 0.0
        ref = step["reference"]
        tol = step["tolerance_GPa"]
        keys = ["beta_phase", "beta_prime_prime_phase", "U1_phase", "U2_phase"]
        scores = []
        for k in keys:
            val = bm.get(k)
            if val is None:
                return 0.0
            diff = abs(val - ref[k])
            if diff <= tol:
                scores.append(1.0)
            elif diff <= 2 * tol:
                scores.append(0.5)
            else:
                scores.append(0.0)
        return sum(scores) / len(scores)


# === block: score_2 (check id='band_gap') ===
def score_2(artifact, step, ctx):
    def score_band_gap(artifact, step, ctx):
        data = ctx.get("data")
        if data is None:
            return 0.0
        gap = data.get("band_gap_beta")
        if gap is None:
            return 0.0
        ref = step["reference"]
        tol = step["tolerance_eV"]
        diff = abs(gap - ref)
        if diff <= tol:
            return 1.0
        elif diff <= 2 * tol:
            return 0.5
        else:
            return 0.0


_SCORERS = {
    'formation_energies': score_0,
    'bulk_moduli': score_1,
    'band_gap': score_2,
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
