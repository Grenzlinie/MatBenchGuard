import os
import json
import csv

# === author imports / helpers ===
import json


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
    return {"spec": spec}


# === block: score_0 (check id='lattice') ===
def score_0(artifact, step, ctx):
    comps = artifact.get("compositions", [])
    gold = step.get("gold", {})
    tols = step.get("tolerances", {})
    fields = step.get("fields", [])
    if not comps or len(comps) == 0:
        return 0.0
    scores = []
    for c in comps:
        x_key = str(c.get("x", None))
        g = gold.get(x_key)
        if g is None:
            continue
        for f in fields:
            val = c.get(f)
            gv = g.get(f)
            if val is None or gv is None:
                scores.append(0.0)
                continue
            tol = tols.get(f, 0.02)
            if abs(gv) > 1e-12:
                rel = abs(val - gv) / abs(gv)
                s = max(0.0, 1.0 - rel / tol)
            else:
                s = 1.0 if abs(val - gv) < tol else 0.0
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='elastic_constants') ===
def score_1(artifact, step, ctx):
    comps = artifact.get("compositions", [])
    gold = step.get("gold", {})
    tols = step.get("tolerances", {})
    fields = step.get("fields", [])
    if not comps or len(comps) == 0:
        return 0.0
    scores = []
    for c in comps:
        x_key = str(c.get("x", None))
        g = gold.get(x_key)
        if g is None:
            continue
        for f in fields:
            val = c.get(f)
            gv = g.get(f)
            if val is None or gv is None:
                scores.append(0.0)
                continue
            tol = tols.get(f, 0.10)
            if abs(gv) > 1e-12:
                rel = abs(val - gv) / abs(gv)
                s = max(0.0, 1.0 - rel / tol)
            else:
                s = 1.0 if abs(val - gv) < tol else 0.0
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='mechanical_moduli') ===
def score_2(artifact, step, ctx):
    comps = artifact.get("compositions", [])
    gold = step.get("gold", {})
    tols = step.get("tolerances", {})
    fields = step.get("fields", [])
    if not comps or len(comps) == 0:
        return 0.0
    scores = []
    for c in comps:
        x_key = str(c.get("x", None))
        g = gold.get(x_key)
        if g is None:
            continue
        for f in fields:
            val = c.get(f)
            gv = g.get(f)
            if val is None or gv is None:
                scores.append(0.0)
                continue
            tol = tols.get(f, 0.10)
            if abs(gv) > 1e-12:
                rel = abs(val - gv) / abs(gv)
                s = max(0.0, 1.0 - rel / tol)
            else:
                s = 1.0 if abs(val - gv) < tol else 0.0
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='electronic') ===
def score_3(artifact, step, ctx):
    comps = artifact.get("compositions", [])
    if not comps:
        return 0.0
    all_pass = True
    for c in comps:
        bg = c.get("band_gap")
        nef = c.get("N_EF")
        if bg is None or nef is None:
            all_pass = False
            continue
        if abs(bg) > 1e-4 or nef <= 0:
            all_pass = False
    return 1.0 if all_pass else 0.0


# === block: score_4 (check id='thermodynamic_structural') ===
def score_4(artifact, step, ctx):
    comps = artifact.get("compositions", [])
    if not comps:
        return 0.0
    gold_debye = step.get("gold_debye_0k", {})
    tol_debye = step.get("tol_debye", 0.10)
    dulong = step.get("dulong_petit", 149.652)
    tol_cv = step.get("tol_cv_600k", 0.20)
    sub_scores = []
    for c in comps:
        x_key = str(c.get("x", None))
        # Debye_0K check
        d0 = c.get("Debye_temperature_0K")
        gd = gold_debye.get(x_key)
        if d0 is not None and gd is not None:
            rel = abs(d0 - gd) / abs(gd) if gd != 0 else abs(d0 - gd)
            sub_scores.append(max(0.0, 1.0 - rel / tol_debye))
        else:
            sub_scores.append(0.0)
        # Cv_0K must be 0
        cv0 = c.get("heat_capacity_Cv_0K")
        if cv0 is None:
            sub_scores.append(0.0)
        else:
            sub_scores.append(1.0 if abs(cv0) < 0.01 else 0.0)
        # Cp > Cv at 300K
        cv300 = c.get("heat_capacity_Cv_300K")
        cp300 = c.get("heat_capacity_Cp_300K")
        if cv300 is not None and cp300 is not None:
            sub_scores.append(1.0 if cp300 > cv300 - 1e-6 else 0.0)
        else:
            sub_scores.append(0.0)
        # Cp > Cv at 600K
        cv600 = c.get("heat_capacity_Cv_600K")
        cp600 = c.get("heat_capacity_Cp_600K")
        if cv600 is not None and cp600 is not None:
            sub_scores.append(1.0 if cp600 > cv600 - 1e-6 else 0.0)
        else:
            sub_scores.append(0.0)
        # Cv_600K close to Dulong-Petit
        if cv600 is not None:
            rel_cv = abs(cv600 - dulong) / dulong
            sub_scores.append(max(0.0, 1.0 - rel_cv / tol_cv))
        else:
            sub_scores.append(0.0)
        # bulk_modulus_0K consistent with B (within 15%)
        bm0 = c.get("bulk_modulus_0K")
        bB = c.get("bulk_modulus_B")
        if bm0 is not None and bB is not None and abs(bB) > 1e-12:
            rel_B = abs(bm0 - bB) / abs(bB)
            sub_scores.append(max(0.0, 1.0 - rel_B / 0.15))
        else:
            sub_scores.append(0.0)
        # bulk_modulus_300K > 0
        bm300 = c.get("bulk_modulus_300K")
        if bm300 is not None:
            sub_scores.append(1.0 if bm300 > 0 else 0.0)
        else:
            sub_scores.append(0.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


# === block: score_5 (check id='trends') ===
def score_5(artifact, step, ctx):
    comps = artifact.get("compositions", [])
    if len(comps) != 3:
        return 0.0
    # sort by x
    comps_sorted = sorted(comps, key=lambda c: c.get("x", 0))
    a_vals = [c.get("a") for c in comps_sorted]
    c_vals = [c.get("c") for c in comps_sorted]
    v_vals = [c.get("V") for c in comps_sorted]
    B_vals = [c.get("bulk_modulus_B") for c in comps_sorted]
    G_vals = [c.get("shear_modulus_G") for c in comps_sorted]
    E_vals = [c.get("Young_modulus_E") for c in comps_sorted]
    nu_vals = [c.get("Poisson_ratio") for c in comps_sorted]
    BG_vals = [c.get("B_G_ratio") for c in comps_sorted]
    checks = []
    # a, c, V decrease
    if all(v is not None for v in a_vals):
        checks.append(1.0 if (a_vals[0] > a_vals[1] > a_vals[2]) else 0.0)
    if all(v is not None for v in c_vals):
        checks.append(1.0 if (c_vals[0] > c_vals[1] > c_vals[2]) else 0.0)
    if all(v is not None for v in v_vals):
        checks.append(1.0 if (v_vals[0] > v_vals[1] > v_vals[2]) else 0.0)
    # B, G, E increase
    if all(v is not None for v in B_vals):
        checks.append(1.0 if (B_vals[0] < B_vals[1] < B_vals[2]) else 0.0)
    if all(v is not None for v in G_vals):
        checks.append(1.0 if (G_vals[0] < G_vals[1] < G_vals[2]) else 0.0)
    if all(v is not None for v in E_vals):
        checks.append(1.0 if (E_vals[0] < E_vals[1] < E_vals[2]) else 0.0)
    # Poisson ratio decrease
    if all(v is not None for v in nu_vals):
        checks.append(1.0 if (nu_vals[0] > nu_vals[1] > nu_vals[2]) else 0.0)
    # B/G ratio decrease
    if all(v is not None for v in BG_vals):
        checks.append(1.0 if (BG_vals[0] > BG_vals[1] > BG_vals[2]) else 0.0)
    if not checks:
        return 0.0
    return sum(checks) / len(checks)


# === block: score_6 (check id='mechanical_stability') ===
def score_6(artifact, step, ctx):
    comps = artifact.get("compositions", [])
    if not comps:
        return 0.0
    all_stable = True
    for c in comps:
        C11 = c.get("C11")
        C12 = c.get("C12")
        C13 = c.get("C13")
        C33 = c.get("C33")
        C44 = c.get("C44")
        if any(v is None for v in [C11, C12, C13, C33, C44]):
            all_stable = False
            continue
        cond1 = C11 > 0
        cond2 = C33 > 0
        cond3 = C44 > 0
        cond4 = (C11 - C12) > 0
        cond5 = (C11 + C12) * C33 > 2 * C13 * C13
        if not (cond1 and cond2 and cond3 and cond4 and cond5):
            all_stable = False
    return 1.0 if all_stable else 0.0


_SCORERS = {
    'lattice': score_0,
    'elastic_constants': score_1,
    'mechanical_moduli': score_2,
    'electronic': score_3,
    'thermodynamic_structural': score_4,
    'trends': score_5,
    'mechanical_stability': score_6,
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
