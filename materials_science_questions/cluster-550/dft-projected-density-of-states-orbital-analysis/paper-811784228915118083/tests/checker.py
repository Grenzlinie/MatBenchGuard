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
    return {}


# === block: score_0 (check id='structure_check') ===
def score_0(artifact, step, ctx):
    expected_compounds = step.get("expected_compounds", [])
    if len(artifact) != len(expected_compounds):
        return 0.0
    set_in_file = set(row["compound"] for row in artifact)
    if set_in_file != set(expected_compounds):
        return 0.0
    # extra check: ensure no duplicate compounds
    if len(set_in_file) != len(artifact):
        return 0.0
    return 1.0


# === block: score_1 (check id='lattice_param_check') ===
def score_1(artifact, step, ctx):
    ref = step.get("reference", {})
    tol = step.get("tolerance_rel", 0.03)
    total = 0
    n = 0
    for row in artifact:
        comp = row["compound"]
        if comp not in ref:
            continue
        for key in ["a0", "c0"]:
            try:
                val = float(row[key])
                target = ref[comp][key]
                if target == 0:
                    err_rel = abs(val - target)
                else:
                    err_rel = abs(val - target) / abs(target)
                if err_rel <= tol:
                    total += 1
            except (ValueError, KeyError):
                pass
            n += 1
    if n == 0:
        return 0.0
    return total / n


# === block: score_2 (check id='elastic_const_check') ===
def score_2(artifact, step, ctx):
    ref = step.get("reference", {})
    tol_rel = step.get("tolerance_rel", 0.15)
    tol_abs_C44 = step.get("tolerance_abs_C44", 10.0)
    total = 0
    n = 0
    for row in artifact:
        comp = row["compound"]
        if comp not in ref:
            continue
        for key in ["C11", "C12", "C13", "C33", "C44"]:
            try:
                val = float(row[key])
                target = ref[comp][key]
                if target == 0:
                    ok = abs(val - target) <= 1e-6
                elif abs(target) < 1e-6:
                    ok = abs(val - target) <= 1e-6
                elif target < 0:
                    # Use absolute tolerance for negative C44
                    ok = abs(val - target) <= tol_abs_C44
                else:
                    ok = (abs(val - target) / target) <= tol_rel
                if ok:
                    total += 1
            except (ValueError, KeyError):
                pass
            n += 1
    if n == 0:
        return 0.0
    return total / n


# === block: score_3 (check id='derived_consistency_check') ===
def score_3(artifact, step, ctx):
    def compute_vrh(row):
        C11 = float(row["C11"]); C12 = float(row["C12"]); C13 = float(row["C13"])
        C33 = float(row["C33"]); C44 = float(row["C44"])
        C66 = (C11 - C12) / 2.0
        M = C11 + C12 + 2*C33 - 4*C13
        C2 = (C11 + C12)*C33 - 2*C13**2
        if M <= 0 or C2 <= 0:
            return None, None, None, None
        BV = (2*(C11 + C12) + 4*C13 + C33) / 9.0
        BR = C2 / M if M != 0 else 0.0
        B = (BV + BR) / 2.0
        GV = (M + 12*C44 + 12*C66) / 30.0
        denom = 3*BV*C44*C66 + C2*(C44 + C66)
        if denom == 0:
            return B, None, None, None
        GR = (5*C2*C44*C66) / (2*denom)
        G = (GV + GR) / 2.0
        denom2 = 3*B + G
        if denom2 == 0:
            return B, G, 0.0, 0.0
        E = 9*B*G / denom2
        nu = (3*B - 2*G) / (2*denom2)
        return B, G, E, nu

    rel_tol = step.get("tolerance_rel", 0.02)
    abs_tol_nu = step.get("tolerance_abs_nu", 0.05)
    stable = step.get("stable_compounds", [])
    n_ok = 0
    for row in artifact:
        comp = row["compound"].strip()
        if comp not in stable:
            continue
        try:
            if float(row.get("C44", "0") or 0) <= 0:
                continue
            Bc, Gc, Ec, nuc = compute_vrh(row)
            Br = float(row.get("B", "0") or 0)
            Gr = float(row.get("G", "0") or 0)
            Er = float(row.get("E", "0") or 0)
            nur = float(row.get("nu", "0") or 0)
            if Bc is None or Gc is None or Ec is None or nuc is None:
                continue
            ok = True
            if Bc == 0:
                ok = ok and abs(Bc - Br) <= 1e-9
            else:
                ok = ok and (abs(Bc - Br) / abs(Bc)) <= rel_tol
            if Gc == 0:
                ok = ok and abs(Gc - Gr) <= 1e-9
            else:
                ok = ok and (abs(Gc - Gr) / abs(Gc)) <= rel_tol
            if Ec == 0:
                ok = ok and abs(Ec - Er) <= 1e-9
            else:
                ok = ok and (abs(Ec - Er) / abs(Ec)) <= rel_tol
            ok = ok and abs(nuc - nur) <= abs_tol_nu
            if ok:
                n_ok += 1
        except Exception:
            pass
    if n_ok == len(stable):
        return 1.0
    return n_ok / max(1, len(stable))


# === block: score_4 (check id='unstable_check') ===
def score_4(artifact, step, ctx):
    unstable = step.get("unstable_compounds", [])
    n_ok = 0
    for row in artifact:
        comp = row["compound"].strip()
        if comp in unstable:
            try:
                c44 = float(row.get("C44", "0") or 0)
                derived_empty = all(str(row.get(f, "")).strip() == "" for f in ["B","G","E","nu","fm","Hv"])
                if c44 < 0 and derived_empty:
                    n_ok += 1
            except (ValueError, KeyError):
                pass
    if n_ok == len(unstable):
        return 1.0
    return n_ok / max(1, len(unstable))


# === block: score_5 (check id='hardness_value_check') ===
def score_5(artifact, step, ctx):
    ref = step.get("reference", {})
    tol_rel = step.get("tolerance_rel", 0.15)
    total = 0
    n = 0
    for row in artifact:
        comp = row["compound"]
        if comp not in ref:
            continue
        try:
            hv = float(row["Hv"])
            target = ref[comp]
            if target == 0:
                ok = abs(hv - target) <= 1e-6
            else:
                ok = (abs(hv - target) / target) <= tol_rel
            if ok:
                total += 1
        except (ValueError, KeyError):
            pass
        n += 1
    if n == 0:
        return 0.0
    return total / n


# === block: score_6 (check id='hardness_ordering_check') ===
def score_6(artifact, step, ctx):
    expected_order = step.get("expected_order", [])
    hv_map = {}
    for row in artifact:
        try:
            hv = float(row["Hv"])
            hv_map[row["compound"].strip()] = hv
        except (ValueError, KeyError):
            pass
    prev_hv = None
    for comp in expected_order:
        hv = hv_map.get(comp)
        if hv is None:
            return 0.0
        if prev_hv is not None and hv >= prev_hv:
            return 0.0
        prev_hv = hv
    return 1.0


_SCORERS = {
    'structure_check': score_0,
    'lattice_param_check': score_1,
    'elastic_const_check': score_2,
    'derived_consistency_check': score_3,
    'unstable_check': score_4,
    'hardness_value_check': score_5,
    'hardness_ordering_check': score_6,
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
