import os
import json
import csv

# === author imports / helpers ===
import math

def invert_3x3(M):
    a,b,c = M[0][0], M[0][1], M[0][2]
    d,e,f = M[1][0], M[1][1], M[1][2]
    g,h,i = M[2][0], M[2][1], M[2][2]
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    if abs(det) < 1e-15:
        raise ValueError("Singular matrix")
    inv_det = 1.0/det
    return [
        [(e*i - f*h)*inv_det, -(b*i - c*h)*inv_det,  (b*f - c*e)*inv_det],
        [-(d*i - f*g)*inv_det, (a*i - c*g)*inv_det, -(a*f - c*d)*inv_det],
        [(d*h - e*g)*inv_det, -(a*h - b*g)*inv_det, (a*e - b*d)*inv_det]
    ]

def vr_bulk_from_elastic(C):
    C11,C12,C13,C22,C23,C33,_,_,_ = C
    B_V = (C11 + C22 + C33 + 2*(C12 + C13 + C23)) / 9.0
    mat = [[C11, C12, C13],
           [C12, C22, C23],
           [C13, C23, C33]]
    inv = invert_3x3(mat)
    S11, S12, S13 = inv[0][0], inv[0][1], inv[0][2]
    S22, S23, S33 = inv[1][1], inv[1][2], inv[2][2]
    B_R = 1.0 / (S11 + S22 + S33 + 2*(S12 + S13 + S23))
    return (B_V + B_R) / 2.0


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
    ref = spec.get("reference_data", {})
    return {"ref": ref}


# === block: score_0 (check id='numeric_accuracy') ===
def score_0(artifact, step, ctx):
    ref = ctx["ref"]
    compounds_order = ["C2N2(NH)", "Si2N2(NH)", "Ge2N2(NH)", "Sn2N2(NH)"]
    if not set(compounds_order).issubset(artifact.keys()):
        return 0.0
    lattice_abs = 0.05
    elastic_rel = 0.20
    band_gap_abs = 0.2
    dielectric_abs = 0.3
    bulk_rel = 0.10
    count_ok = 0
    total = 0
    for compound in compounds_order:
        comp_data = artifact[compound]
        ref_data = ref[compound]
        # lattice
        lat_art = comp_data.get("lattice_constants", {})
        lat_ref = ref_data["lattice"]
        for axis in ["a", "b", "c"]:
            total += 1
            v_art = lat_art.get(axis)
            v_ref = lat_ref[axis]
            if v_art is not None and abs(v_art - v_ref) <= lattice_abs:
                count_ok += 1
        # elastic
        elas_art = comp_data.get("elastic_constants", {})
        elas_ref = ref_data["elastic"]
        for key in ["C11","C12","C13","C22","C23","C33","C44","C55","C66"]:
            total += 1
            v_ref = elas_ref[key]
            v_art = elas_art.get(key)
            if v_art is not None and v_ref != 0:
                if abs(v_art - v_ref) <= elastic_rel * abs(v_ref):
                    count_ok += 1
        # band_gap_value
        bg_art = comp_data.get("band_gap_value")
        bg_ref = ref_data["band_gap_value"]
        total += 1
        if bg_art is not None and abs(bg_art - bg_ref) <= band_gap_abs:
            count_ok += 1
        # band_gap_type
        bg_type_art = comp_data.get("band_gap_type")
        bg_type_ref = ref_data["band_gap_type"]
        total += 1
        if bg_type_art is not None and bg_type_art == bg_type_ref:
            count_ok += 1
        # dielectric
        dielec_art = comp_data.get("static_dielectric_constants", {})
        dielec_ref = ref_data["dielectric"]
        for key in ["epsilon_parallel_a","epsilon_parallel_b","epsilon_parallel_c","epsilon_0"]:
            total += 1
            v_art = dielec_art.get(key)
            v_ref = dielec_ref[key]
            if v_art is not None and abs(v_art - v_ref) <= dielectric_abs:
                count_ok += 1
        # bulk_modulus (recompute reference VRH from paper elastic constants)
        bulk_art = comp_data.get("bulk_modulus")
        if bulk_art is not None:
            total += 1
            elas = [elas_ref["C11"], elas_ref["C12"], elas_ref["C13"],
                    elas_ref["C22"], elas_ref["C23"], elas_ref["C33"],
                    elas_ref["C44"], elas_ref["C55"], elas_ref["C66"]]
            expected_bulk = vr_bulk_from_elastic(elas)
            if expected_bulk != 0 and abs(bulk_art - expected_bulk) <= bulk_rel * abs(expected_bulk):
                count_ok += 1
    if total == 0:
        return 0.0
    return count_ok / total


# === block: score_1 (check id='born_stability') ===
def score_1(artifact, step, ctx):
    required = ["C2N2(NH)", "Si2N2(NH)", "Ge2N2(NH)", "Sn2N2(NH)"]
    for c in required:
        if c not in artifact:
            return 0.0
        if not artifact[c].get("born_stable", False):
            return 0.0
    return 1.0


# === block: score_2 (check id='bulk_trend') ===
def score_2(artifact, step, ctx):
    required = ["C2N2(NH)", "Si2N2(NH)", "Ge2N2(NH)", "Sn2N2(NH)"]
    bulks = []
    for c in required:
        if c not in artifact:
            return 0.0
        b = artifact[c].get("bulk_modulus")
        if b is None:
            return 0.0
        bulks.append(b)
    if all(bulks[i] > bulks[i+1] for i in range(3)):
        return 1.0
    return 0.0


_SCORERS = {
    'numeric_accuracy': score_0,
    'born_stability': score_1,
    'bulk_trend': score_2,
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
