import os
import json
import csv

# === author imports / helpers ===
import math

def compute_moduli(C11, C22, C12, C66):
    """Return dict with min/max of Young, shear, Poisson from 2D orthorhombic stiffness."""
    D = C11 * C22 - C12 * C12
    if abs(D) < 1e-12:
        return None
    S11 = C22 / D
    S22 = C11 / D
    S12 = -C12 / D
    S66 = 1.0 / C66
    Y_min = float('inf')
    Y_max = -float('inf')
    G_min = float('inf')
    G_max = -float('inf')
    nu_min = float('inf')
    nu_max = -float('inf')
    for i in range(361):
        theta = math.radians(i)
        c = math.cos(theta)
        s = math.sin(theta)
        c2 = c * c
        s2 = s * s
        # transformed compliances
        S11p = S11 * c2 * c2 + (2.0 * S12 + S66) * c2 * s2 + S22 * s2 * s2
        if S11p <= 1e-12:
            continue
        E = 1.0 / S11p
        Y_min = min(Y_min, E)
        Y_max = max(Y_max, E)
        # Shear modulus
        S66p = S66 * (c2 - s2)*(c2 - s2) + 2.0 * (S11 + S22 - 2.0 * S12 - S66) * c2 * s2
        if S66p <= 1e-12:
            continue
        G = 1.0 / S66p
        G_min = min(G_min, G)
        G_max = max(G_max, G)
        # Poisson's ratio
        S12p = (S11 + S22 - S66) * c2 * s2 + S12 * (c2 * c2 + s2 * s2)
        nu = -S12p / S11p
        nu_min = min(nu_min, nu)
        nu_max = max(nu_max, nu)
    return {
        "Y_min": Y_min, "Y_max": Y_max,
        "G_min": G_min, "G_max": G_max,
        "nu_min": nu_min, "nu_max": nu_max
    }


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


# === block: score_0 (check id='step_final') ===
def score_0(artifact, step, ctx):
        expected = step.get("expected", {})
        sub_weights = step.get("sub_weights", {})
        # helper scoring functions
        def score_abs_err(val, gold, tol):
            return max(0.0, 1.0 - abs(val - gold) / tol)
        def score_rel_err(val, gold, rel_tol):
            return max(0.0, 1.0 - abs(val - gold) / (rel_tol * abs(gold)))
        # collect raw scores per property
        raw_scores = {}
        # 1) relaxed_a
        val = artifact.get("relaxed_a")
        raw_scores["relaxed_a"] = score_abs_err(val, expected["relaxed_a"]["gold"], expected["relaxed_a"]["tol"]) if val is not None else 0.0
        # 2) relaxed_b
        val = artifact.get("relaxed_b")
        raw_scores["relaxed_b"] = score_abs_err(val, expected["relaxed_b"]["gold"], expected["relaxed_b"]["tol"]) if val is not None else 0.0
        # 3) cohesive_energy
        val = artifact.get("cohesive_energy")
        raw_scores["cohesive_energy"] = score_abs_err(val, expected["cohesive_energy"]["gold"], expected["cohesive_energy"]["tol"]) if val is not None else 0.0
        # 4) electronic_band_gap
        gap_val = artifact.get("electronic_band_gap")
        if gap_val is not None:
            tol_abs = expected["electronic_band_gap"].get("tol_abs", 0.05)
            decay = expected["electronic_band_gap"].get("decay", 0.2)
            if gap_val <= tol_abs:
                raw_scores["electronic_band_gap"] = 1.0
            else:
                raw_scores["electronic_band_gap"] = max(0.0, 1.0 - (gap_val - tol_abs) / decay)
        else:
            raw_scores["electronic_band_gap"] = 0.0
        # 5) elastic constants C11, C22, C12, C66
        for key in ["C11", "C22", "C12", "C66"]:
            val = artifact.get(key)
            gold = expected[key]["gold"]
            rel_tol = expected[key]["rel_tol"]
            raw_scores[key] = score_rel_err(val, gold, rel_tol) if val is not None else 0.0
        # 6) recompute mechanical moduli from elastic constants
        C11 = artifact.get("C11")
        C22 = artifact.get("C22")
        C12 = artifact.get("C12")
        C66 = artifact.get("C66")
        if all(v is not None for v in [C11, C22, C12, C66]):
            moduli = compute_moduli(C11, C22, C12, C66)
            if moduli is None:
                for key in ["Young_min", "Young_max", "shear_min", "shear_max", "Poisson_min", "Poisson_max"]:
                    raw_scores[key] = 0.0
            else:
                raw_scores["Young_min"] = score_rel_err(moduli["Y_min"], expected["Young_min"]["gold"], expected["Young_min"]["rel_tol"])
                raw_scores["Young_max"] = score_rel_err(moduli["Y_max"], expected["Young_max"]["gold"], expected["Young_max"]["rel_tol"])
                raw_scores["shear_min"] = score_rel_err(moduli["G_min"], expected["shear_min"]["gold"], expected["shear_min"]["rel_tol"])
                raw_scores["shear_max"] = score_rel_err(moduli["G_max"], expected["shear_max"]["gold"], expected["shear_max"]["rel_tol"])
                # Poisson ratio uses absolute tolerance
                raw_scores["Poisson_min"] = score_abs_err(moduli["nu_min"], expected["Poisson_min"]["gold"], expected["Poisson_min"]["abs_tol"])
                raw_scores["Poisson_max"] = score_abs_err(moduli["nu_max"], expected["Poisson_max"]["gold"], expected["Poisson_max"]["abs_tol"])
        else:
            for key in ["Young_min", "Young_max", "shear_min", "shear_max", "Poisson_min", "Poisson_max"]:
                raw_scores[key] = 0.0
        # 7) phonon stability
        phonon_val = artifact.get("phonon_imaginary_frequencies")
        if isinstance(phonon_val, bool):
            raw_scores["phonon_imaginary_frequencies"] = 1.0 if phonon_val is False else 0.0
        else:
            raw_scores["phonon_imaginary_frequencies"] = 0.0
        # 8) optical absorption
        for key in ["absorption_xx_at_0_8eV", "absorption_yy_at_2_3eV"]:
            val = artifact.get(key)
            gold = expected[key]["gold"]
            tol = expected[key]["abs_tol"]
            raw_scores[key] = score_abs_err(val, gold, tol) if val is not None else 0.0
        # weighted aggregation
        total_weight = sum(sub_weights[k] for k in raw_scores if k in sub_weights)
        weighted = 0.0
        for k, score in raw_scores.items():
            w = sub_weights.get(k, 0.0)
            weighted += score * w
        final_score = weighted / total_weight if total_weight > 0 else 0.0
        return final_score


_SCORERS = {
    'step_final': score_0,
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
