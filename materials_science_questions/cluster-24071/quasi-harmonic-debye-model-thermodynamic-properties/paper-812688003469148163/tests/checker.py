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
    output_dir = "/app/outputs"
    path = os.path.join(output_dir, "thermo_mechanical_properties.csv")
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return {"rows": rows}


# === block: score_0 (check id='thermo_properties') ===
def score_0(artifact, step, ctx):
    rows = ctx.get("rows", [])
    if not rows:
        return 0.0

    T_grid = [100.0, 300.0, 500.0, 700.0, 900.0]
    P_grid = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
    expected_set = {(t, p) for t in T_grid for p in P_grid}
    tp_tuples = set()
    data = {}
    for r in rows:
        try:
            t = float(r["T(K)"])
            p = float(r["P(GPa)"])
        except (KeyError, ValueError):
            return 0.0
        tp_tuples.add((t, p))
        props = {}
        for k in ["lattice_parameter(A)", "bulk_modulus(GPa)", "youngs_modulus(GPa)",
                  "shear_modulus(GPa)", "specific_heat_CV(J/mol.K)", "specific_heat_CP(J/mol.K)"]:
            try:
                props[k] = float(r[k])
            except (KeyError, ValueError):
                pass
        data[(t, p)] = props

    if tp_tuples != expected_set:
        return 0.0

    # Sub-checks with weights
    weights = {
        "ambient": 0.35,
        "lattice_trend": 0.15,
        "bulk_trend": 0.15,
        "elastic_consistency": 0.15,
        "cp_trend": 0.1,
        "pressure_check": 0.1
    }
    scores = {}

    # 1. Ambient values at (300 K, 0 GPa)
    # Young's and shear modulus are NOT checked numerically here because the paper's
    # reported values are inconsistent with the prescribed relation E_Y = 3(1-2*nu)*K_T.
    # The elastic‑consistency sub‑check (below) verifies that the submitted Young's modulus
    # is self-consistent with the submitted bulk modulus and the Poisson ratio derived
    # from Vegard's law (nu=0.314).
    ref = {
        "lattice_parameter(A)": (2.8821, 0.02),
        "bulk_modulus(GPa)": (166.84, 10.0),
        "specific_heat_CP(J/mol.K)": (24.37, 2.0)
    }
    amb_row = data.get((300.0, 0.0), {})
    hits = 0
    for field, (target, tol) in ref.items():
        val = amb_row.get(field)
        if val is not None and abs(val - target) <= tol:
            hits += 1
    scores["ambient"] = hits / len(ref) if ref else 1.0

    # 2. Lattice parameter trend: non‑increasing with pressure (slack 0.002 Å)
    lattice_trend_ok = True
    for t in T_grid:
        vals = []
        for p in P_grid:
            v = data.get((t, p), {}).get("lattice_parameter(A)")
            if v is None:
                lattice_trend_ok = False
                break
            vals.append(v)
        if not lattice_trend_ok:
            break
        for i in range(len(vals)-1):
            if vals[i+1] - vals[i] > 0.002:
                lattice_trend_ok = False
                break
    scores["lattice_trend"] = 1.0 if lattice_trend_ok else 0.0

    # 3. Bulk modulus trend: non‑decreasing with pressure (slack 1.0 GPa)
    bulk_trend_ok = True
    for t in T_grid:
        vals = []
        for p in P_grid:
            v = data.get((t, p), {}).get("bulk_modulus(GPa)")
            if v is None:
                bulk_trend_ok = False
                break
            vals.append(v)
        if not bulk_trend_ok:
            break
        for i in range(len(vals)-1):
            if vals[i+1] < vals[i] - 1.0:
                bulk_trend_ok = False
                break
    scores["bulk_trend"] = 1.0 if bulk_trend_ok else 0.0

    # 4. Elastic consistency: Youngs = 3*(1-2ν)*K_T, ν = 0.6*0.29+0.4*0.35 = 0.314
    C_Fe = 0.6
    C_Al = 0.4
    nu = C_Fe*0.29 + C_Al*0.35
    factor = 3.0 * (1.0 - 2.0*nu)
    elastic_ok = True
    for t, p in tp_tuples:
        bulk = data.get((t,p), {}).get("bulk_modulus(GPa)")
        yg = data.get((t,p), {}).get("youngs_modulus(GPa)")
        if bulk is None or yg is None or yg <= 0:
            continue
        expected_yg = factor * bulk
        if abs(yg - expected_yg) / expected_yg > 0.03:
            elastic_ok = False
            break
    scores["elastic_consistency"] = 1.0 if elastic_ok else 0.0

    # 5. Specific heat CP trend: CP(100 K) < CP(300 K) for each P
    cp_ok = True
    for p in P_grid:
        cp100 = data.get((100.0, p), {}).get("specific_heat_CP(J/mol.K)")
        cp300 = data.get((300.0, p), {}).get("specific_heat_CP(J/mol.K)")
        if cp100 is None or cp300 is None:
            continue
        if cp100 >= cp300:
            cp_ok = False
            break
    scores["cp_trend"] = 1.0 if cp_ok else 0.0

    # 6. High‑pressure anchor: (300K, 10 GPa) lattice ~2.761 Å, bulk ~316.84 GPa
    lattice_high = data.get((300.0, 10.0), {}).get("lattice_parameter(A)")
    bulk_high = data.get((300.0, 10.0), {}).get("bulk_modulus(GPa)")
    pressure_ok = True
    if lattice_high is not None:
        if not (2.70 <= lattice_high <= 2.82):
            pressure_ok = False
    if bulk_high is not None:
        if not (290.0 <= bulk_high <= 340.0):
            pressure_ok = False
    scores["pressure_check"] = 1.0 if pressure_ok else 0.0

    total = 0.0
    for k in weights:
        total += scores.get(k, 0.0) * weights[k]
    return total


_SCORERS = {
    'thermo_properties': score_0,
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
