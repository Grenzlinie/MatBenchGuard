import os
import json
import csv

# === author imports / helpers ===
import math

def to_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def check_equals(val, ref, rel_tol, abs_tol):
    if val is None:
        return False
    return math.isclose(val, ref, rel_tol=rel_tol, abs_tol=abs_tol)


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
    step = None
    for s in spec.get("steps", []):
        if s["id"] == "step_01":
            step = s
            break
    if step is None:
        return {}
    cfg = step.get("config", {})
    L = cfg["L"]
    T = cfg["T"]
    materials = cfg["materials"]
    tolerances = cfg.get("tolerances", {"input_rel": 1e-6, "input_abs": 1e-6, "output_rel": 1e-4, "output_abs": 1e-5})
    expected = {}
    for mat, vals in materials.items():
        sigma_cm = vals["sigma"]
        alpha_uV = vals["alpha"]
        A_bar = vals["A_bar"]
        sigma_SI = sigma_cm * 100
        kappa_e = L * sigma_SI * T
        kappa_a = 64.0 * (A_bar ** (-1.04))
        kappa_total = kappa_e + kappa_a
        alpha_V = alpha_uV * 1e-6
        ZT = (alpha_V ** 2 * sigma_SI * T) / kappa_total
        expected[mat] = {
            "sigma": sigma_cm,
            "alpha": alpha_uV,
            "kappa_e": kappa_e,
            "kappa_a": kappa_a,
            "kappa_total": kappa_total,
            "ZT": ZT
        }
    return {"expected": expected, "materials": materials, "tolerances": tolerances}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    expected = ctx["expected"]
    materials_info = ctx["materials"]
    tols = ctx["tolerances"]
    L = 2.45e-8
    T = 1000

    material_scores = []
    for mat, exp in expected.items():
        entry = None
        for e in artifact:
            if e.get("material") == mat:
                entry = e
                break
        if entry is None:
            material_scores.append(0.0)
            continue
        checks_parts = []
        # sigma match
        sigma_val = to_float(entry.get("sigma"))
        checks_parts.append(check_equals(sigma_val, exp["sigma"], tols["input_rel"], tols["input_abs"]))
        # alpha match
        alpha_val = to_float(entry.get("alpha"))
        checks_parts.append(check_equals(alpha_val, exp["alpha"], tols["input_rel"], tols["input_abs"]))
        if sigma_val is not None and alpha_val is not None:
            sigma_SI = sigma_val * 100
            alpha_V = alpha_val * 1e-6
            Abar = materials_info[mat]["A_bar"]
            recomp_kappa_e = L * sigma_SI * T
            recomp_kappa_a = 64.0 * (Abar ** (-1.04))
            recomp_kappa_total = recomp_kappa_e + recomp_kappa_a
            recomp_ZT = (alpha_V ** 2 * sigma_SI * T) / recomp_kappa_total
            recompute_ok = True
        else:
            recompute_ok = False
            recomp_kappa_e = recomp_kappa_a = recomp_kappa_total = recomp_ZT = None
        # kappa_e match
        ke_val = to_float(entry.get("kappa_e"))
        checks_parts.append(recompute_ok and check_equals(ke_val, recomp_kappa_e, tols["output_rel"], tols["output_abs"]))
        # kappa_a match
        ka_val = to_float(entry.get("kappa_a"))
        checks_parts.append(recompute_ok and check_equals(ka_val, recomp_kappa_a, tols["output_rel"], tols["output_abs"]))
        # kappa_total match
        kt_val = to_float(entry.get("kappa_total"))
        checks_parts.append(recompute_ok and check_equals(kt_val, recomp_kappa_total, tols["output_rel"], tols["output_abs"]))
        # ZT match
        zt_val = to_float(entry.get("ZT"))
        checks_parts.append(recompute_ok and check_equals(zt_val, recomp_ZT, tols["output_rel"], tols["output_abs"]))
        # inequality from recomputed ZT
        if recompute_ok:
            if mat == "CuI":
                checks_parts.append(recomp_ZT > 0.1)
            else:
                checks_parts.append(recomp_ZT < 0.01)
        else:
            checks_parts.append(False)
        if checks_parts:
            mat_score = sum(checks_parts) / len(checks_parts)
        else:
            mat_score = 0.0
        material_scores.append(mat_score)

    if not material_scores:
        return 0.0
    return sum(material_scores) / len(material_scores)


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
