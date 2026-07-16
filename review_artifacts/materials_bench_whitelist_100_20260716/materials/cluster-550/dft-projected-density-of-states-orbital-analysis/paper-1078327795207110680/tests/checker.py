import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    reference_coefficients = None
    evaluation_deltas = None
    tolerances = None
    orbitals_weights = None
    gold_energies = {}
    for step in spec.get("steps", []):
        if step.get("id") == "check_molecular_fit":
            params = step.get("params", {})
            reference_coefficients = params.get("reference_coefficients", {})
            evaluation_deltas = params.get("evaluation_deltas", [])
            tolerances = params.get("tolerances", {})
            orbitals_weights = params.get("orbitals_weights", {})
            break
    if reference_coefficients is not None:
        for orbital, coefs in reference_coefficients.items():
            a0, a1, a2, a3 = coefs
            gold_energies[orbital] = [a0 + a1*d + a2*d**2 + a3*d**3 for d in evaluation_deltas]
    ctx = {
        "gold_energies": gold_energies,
        "evaluation_deltas": evaluation_deltas,
        "tolerances": tolerances,
        "orbitals_weights": orbitals_weights
    }
    return ctx


# === block: score_0 (check id='check_pbe_band_gap') ===
def score_0(artifact, step, ctx):
    val = float(artifact.strip())
    target = step.get("target", 0.0)
    tol = step.get("tolerance", 0.0)
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='check_hse06_band_gap') ===
def score_1(artifact, step, ctx):
    val = float(artifact.strip())
    target = step.get("target", 0.0)
    tol = step.get("tolerance", 0.0)
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='check_off_diagonals') ===
def score_2(artifact, step, ctx):
    data = artifact
    fields = step.get("fields", {})
    tol = step.get("tolerance", 0.0)
    pz_ok = abs(data.get("pz_offdiagonal_eV", 0) - fields.get("pz_offdiagonal_eV", 0)) <= tol
    pxpy_ok = abs(data.get("px_py_offdiagonal_eV", 0) - fields.get("px_py_offdiagonal_eV", 0)) <= tol
    return 1.0 if (pz_ok and pxpy_ok) else 0.0


# === block: score_3 (check id='check_molecular_fit') ===
def score_3(artifact, step, ctx):
    data = artifact
    gold_energies = ctx.get("gold_energies", {})
    evaluation_deltas = ctx.get("evaluation_deltas", [])
    tolerances = ctx.get("tolerances", {})
    orbital_weights = ctx.get("orbitals_weights", {})
    orbital_keys = ["sigma_g", "pi_u", "pi_g_star", "sigma_u_star"]
    total_weighted_score = 0.0
    for orb in orbital_keys:
        if orb not in data:
            return 0.0
        coefs = data[orb]
        if not isinstance(coefs, (list, tuple)) or len(coefs) < 4:
            return 0.0
        a0, a1, a2, a3 = coefs[0], coefs[1], coefs[2], coefs[3]
        agent_energies = [a0 + a1*d + a2*d**2 + a3*d**3 for d in evaluation_deltas]
        ref_energies = gold_energies.get(orb, [])
        if len(agent_energies) != len(ref_energies):
            return 0.0
        mae = sum(abs(ae - re) for ae, re in zip(agent_energies, ref_energies)) / len(ref_energies)
        tol = tolerances.get(orb, {})
        full_mae = tol.get("full_mae", 0.05)
        zero_mae = tol.get("zero_mae", 0.15)
        if mae <= full_mae:
            orb_score = 1.0
        elif mae >= zero_mae:
            orb_score = 0.0
        else:
            orb_score = 1.0 - (mae - full_mae) / (zero_mae - full_mae)
        total_weighted_score += orbital_weights.get(orb, 0.0) * orb_score
    return total_weighted_score


_SCORERS = {
    'check_pbe_band_gap': score_0,
    'check_hse06_band_gap': score_1,
    'check_off_diagonals': score_2,
    'check_molecular_fit': score_3,
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
