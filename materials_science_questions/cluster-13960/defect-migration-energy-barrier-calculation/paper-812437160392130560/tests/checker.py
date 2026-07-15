import os
import json
import csv

# === author imports / helpers ===
import math

# helper: relative error ramp
def score_quantity(val, ref, tol_rel):
    """Return 0-1, 1 if within tolerance, linear decay beyond."""
    if ref == 0:
        return 1.0 if abs(val) < 1e-12 else 0.0
    rel_err = abs(val - ref) / abs(ref)
    if rel_err <= tol_rel:
        return 1.0
    return max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)

def find_row(rows, temp):
    for r in rows:
        try:
            if abs(float(r["T"]) - temp) < 1e-6:
                return r
        except (KeyError, ValueError):
            continue
    return None


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
    refs = {}
    for step in spec.get("steps", []):
        rid = step.get("id")
        rv = step.get("reference_values", {})
        if rv:
            refs[rid] = rv
    return refs


# === block: score_0 (check id='saddle_plane_probabilities') ===
def score_0(artifact, step, ctx):
    rv = ctx.get("saddle_plane_probabilities", {})
    temps = rv.get("temperatures", [])
    ref_p0 = rv.get("P0", [])
    tol = rv.get("tolerance_relative", 0.35)
    scores = []
    for i, T in enumerate(temps):
        row = find_row(artifact, T)
        if row is None:
            scores.append(0.0)
            continue
        try:
            val = float(row["P0"])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        scores.append(score_quantity(val, ref_p0[i], tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='transmission_coefficients') ===
def score_1(artifact, step, ctx):
    rv = ctx.get("transmission_coefficients", {})
    temps = rv.get("temperatures", [])
    ref_S = rv.get("S", [])
    tol = rv.get("tolerance_relative", 0.4)
    scores = []
    for i, T in enumerate(temps):
        row = find_row(artifact, T)
        if row is None:
            scores.append(0.0)
            continue
        try:
            val = float(row["S"])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        scores.append(score_quantity(val, ref_S[i], tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='migration_results') ===
def score_2(artifact, step, ctx):
    rv = ctx.get("migration_results", {})
    temps = rv.get("temperatures", [])
    ref_p0 = rv.get("P0", [])
    ref_S = rv.get("S", [])
    ref_Gamma = rv.get("Gamma", [])
    ref_nu = rv.get("nu_bar", [])
    tols = {
        "P0": rv.get("tol_P0", 0.35),
        "S": rv.get("tol_S", 0.4),
        "Gamma": rv.get("tol_Gamma", 0.5),
        "nu_bar": rv.get("tol_nu_bar", 0.5)
    }

    # scores for each quantity over temperatures
    quant_scores = {"P0": [], "S": [], "Gamma": [], "nu_bar": []}
    for i, T in enumerate(temps):
        row = find_row(artifact, T)
        if row is None:
            for k in quant_scores:
                quant_scores[k].append(0.0)
            continue
        try:
            p0_val = float(row["P_0_Angstrom_inv"])
            s_val = float(row["transmission_coeff"])
            gamma_val = float(row["Gamma_per_s"])
            nu_val = float(row["nu_bar_1e12_per_s"])
        except (KeyError, ValueError):
            for k in quant_scores:
                quant_scores[k].append(0.0)
            continue
        quant_scores["P0"].append(score_quantity(p0_val, ref_p0[i], tols["P0"]))
        quant_scores["S"].append(score_quantity(s_val, ref_S[i], tols["S"]))
        quant_scores["Gamma"].append(score_quantity(gamma_val, ref_Gamma[i], tols["Gamma"]))
        quant_scores["nu_bar"].append(score_quantity(nu_val, ref_nu[i], tols["nu_bar"]))

    # overall average across quantities and temperatures
    mean_score = sum(sum(v) for v in quant_scores.values()) / (len(temps) * 4) if temps else 0.0

    # Internal consistency bonus: recompute Gamma from P0, S, and effective mass mu
    # using Gamma0 = 2 * sqrt(kB*T/(2*pi*mu)) * P0, Gamma = S * Gamma0
    # Use standard atomic masses and conversion to kg.
    kB = 1.380649e-23  # J/K
    m_O_kg = rv.get("m_O_amu", 15.999) * 1.66053906660e-27
    m_Co_kg = rv.get("m_Co_amu", 58.933) * 1.66053906660e-27
    mu_inv = (2.0/3.0)/m_O_kg + (1.0/3.0)/m_Co_kg
    mu_kg = 1.0 / mu_inv if mu_inv > 0 else 1e-26

    consistency_scores = []
    for i, T in enumerate(temps):
        row = find_row(artifact, T)
        if row is None:
            consistency_scores.append(0.0)
            continue
        try:
            p0_val = float(row["P_0_Angstrom_inv"])
            s_val = float(row["transmission_coeff"])
            gamma_val = float(row["Gamma_per_s"])
        except (KeyError, ValueError):
            consistency_scores.append(0.0)
            continue
        # P0 in Å⁻¹, convert to m⁻¹ by multiplying by 1e10
        p0_si = p0_val * 1e10
        v = math.sqrt(kB * T / (2.0 * math.pi * mu_kg))  # m/s
        gamma0_theo = 2.0 * v * p0_si
        gamma_expected = s_val * gamma0_theo
        if gamma_expected > 0:
            rel_err = abs(gamma_val - gamma_expected) / gamma_expected
            # tight tolerance for internal consistency: 1%
            cs = 1.0 if rel_err <= rv.get("tol_consistency", 0.01) else max(0.0, 1.0 - rel_err*10)
        else:
            cs = 0.0
        consistency_scores.append(cs)

    consistency_mean = sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.0

    # final score: 80% reference match, 20% internal consistency
    final = 0.8 * mean_score + 0.2 * consistency_mean
    return final


_SCORERS = {
    'saddle_plane_probabilities': score_0,
    'transmission_coefficients': score_1,
    'migration_results': score_2,
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
