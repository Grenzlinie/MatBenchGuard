import os
import json
import csv

# === author imports / helpers ===
import json, os


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
        mono_path = os.path.join(outputs_dir, "monolayer_results.json")
        three_path = os.path.join(outputs_dir, "three_layer_results.json")
        mono = {}
        three = {}
        if os.path.exists(mono_path):
            with open(mono_path) as f:
                mono = json.load(f)
        if os.path.exists(three_path):
            with open(three_path) as f:
                three = json.load(f)
        return {"monolayer": mono, "three_layer": three}


# === block: score_0 (check id='monolayer_analysis') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        bond_lengths = artifact.get("bond_lengths", {})
        bond_angles = artifact.get("bond_angles", {})
        tilt_angles = artifact.get("tilt_angles", {})
        displacements = artifact.get("displacements", [])
        electron_densities = artifact.get("electron_densities", {})

        expected_bl = [
            ("C1-1", 1.950, 0.05), ("C2-1", 1.936, 0.05), ("C2-1'", 1.951, 0.05),
            ("C3-1'", 1.903, 0.05), ("C3-C3", 1.534, 0.05), ("C1-H", 1.135, 0.05)
        ]
        expected_ba = [
            ("C3C31'", 143.4, 5.0), ("C31'C2", 122.8, 5.0), ("1C11", 134.2, 5.0), ("HC1H", 96.4, 5.0)
        ]
        expected_ta = [
            ("HC1H", 0.0, 5.0), ("HC2H", 0.89, 5.0), ("HC3H", 18.57, 5.0)
        ]
        disp_map = {
            "1":   (0.124, -0.018), "1'":  (0.374, 0.098),
            "2":   (0.043, -0.072), "2'":  (0.091, 0.034),
            "3":   (0.0,   -0.063), "3''": (0.0,   0.094),
            "4":   (0.0,   -0.049), "4''": (0.0,   0.040)
        }
        disp_tol = 0.10
        ed_map = {
            "C1C2C3": 4.016, "1 1'": 3.893, "2 2'": 4.089,
            "3 3' 3''": 3.993, "4 4' 4''": 3.972
        }
        ed_tol = 0.15

        total = 0
        passed = 0

        for label, exp, tol in expected_bl:
            total += 1
            val = bond_lengths.get(label)
            if val is not None and abs(val - exp) <= tol:
                passed += 1
        for label, exp, tol in expected_ba:
            total += 1
            val = bond_angles.get(label)
            if val is not None and abs(val - exp) <= tol:
                passed += 1
        for label, exp, tol in expected_ta:
            total += 1
            val = tilt_angles.get(label)
            if val is not None and abs(val - exp) <= tol:
                passed += 1

        disp_dict = {}
        for d in displacements:
            atom = d.get("atom", "")
            disp_dict[atom] = (d.get("dx"), d.get("dz"))
        for atom, (exp_dx, exp_dz) in disp_map.items():
            total += 2
            if atom in disp_dict:
                dx, dz = disp_dict[atom]
                if dx is not None and abs(dx - exp_dx) <= disp_tol:
                    passed += 1
                if dz is not None and abs(dz - exp_dz) <= disp_tol:
                    passed += 1

        for layer, exp in ed_map.items():
            total += 1
            val = electron_densities.get(layer)
            if val is not None and abs(val - exp) <= ed_tol:
                passed += 1

        # trend 1: displacement 1' dz > 0 and dz > dz(1)
        total += 1
        if "1'" in disp_dict and "1" in disp_dict:
            dz1p = disp_dict["1'"][1]
            dz1 = disp_dict["1"][1]
            if dz1p is not None and dz1 is not None and dz1p > 0 and dz1p > dz1:
                passed += 1
        # trend 3: electron density 2 2' > 1 1'
        total += 1
        val1 = electron_densities.get("1 1'")
        val2 = electron_densities.get("2 2'")
        if val1 is not None and val2 is not None and val2 > val1:
            passed += 1

        score = passed / total if total > 0 else 0.0
        return score


# === block: score_1 (check id='threelayer_analysis') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        bond_lengths = artifact.get("bond_lengths", {})
        bond_angles = artifact.get("bond_angles", {})
        tilt_angles = artifact.get("tilt_angles", {})
        displacements = artifact.get("displacements", [])
        electron_densities = artifact.get("electron_densities", {})

        expected_bl = [
            ("C11", 1.927, 0.05), ("C3C3", 1.614, 0.05), ("Si1C4", 1.874, 0.05),
            ("C21", 1.911, 0.05), ("Si2C4", 1.889, 0.05), ("C21'", 1.972, 0.05),
            ("Si2C5", 1.847, 0.05), ("C31'", 1.912, 0.05), ("Si3C5", 1.855, 0.05),
            ("Si1C1", 2.164, 0.05), ("Si3C6", 1.838, 0.05), ("Si2C2", 2.122, 0.05),
            ("C6H", 1.126, 0.05), ("Si3C3", 2.207, 0.05)
        ]
        expected_ba = [
            ("C3C31'", 142.4, 5.0), ("C31'C2", 124.3, 5.0), ("1C11", 134.5, 5.0),
            ("Si1C1Si1", 130.6, 5.0), ("C4Si1C4", 118.4, 5.0), ("Si1C4Si2", 122.5, 5.0),
            ("C4Si2C5", 112.6, 5.0), ("Si2C5Si3", 116.7, 5.0), ("C5Si3C6", 111.2, 5.0),
            ("Si3C6Si3", 87.3, 5.0), ("HC6H", 96.9, 5.0)
        ]
        expected_ta = [
            ("Si1C1Si1", 0.0, 5.0), ("Si2C2Si2", 11.9, 5.0), ("Si3C3Si3", 29.1, 5.0)
        ]
        disp_map = {
            "1":   (0.143, 0.024), "1'":  (0.402, 0.270),
            "2":   (0.037, -0.134), "2'":  (0.088, 0.023),
            "3":   (0.0,   -0.063), "3''": (0.0,   0.094),
            "4":   (0.0,   -0.049), "4''": (0.0,   0.040)
        }
        disp_tol = 0.10
        ed_map = {
            "C4C5C6": 4.201, "Si1Si2Si3": 3.590, "C1C2C3": 4.240,
            "1 1'": 3.454, "2 2'": 4.603, "3 3' 3''": 3.891, "4 4' 4''": 4.051
        }
        ed_tol = 0.15

        total = 0
        passed = 0

        for label, exp, tol in expected_bl:
            total += 1
            val = bond_lengths.get(label)
            if val is not None and abs(val - exp) <= tol:
                passed += 1
        for label, exp, tol in expected_ba:
            total += 1
            val = bond_angles.get(label)
            if val is not None and abs(val - exp) <= tol:
                passed += 1
        for label, exp, tol in expected_ta:
            total += 1
            val = tilt_angles.get(label)
            if val is not None and abs(val - exp) <= tol:
                passed += 1

        disp_dict = {}
        for d in displacements:
            atom = d.get("atom", "")
            disp_dict[atom] = (d.get("dx"), d.get("dz"))
        for atom, (exp_dx, exp_dz) in disp_map.items():
            total += 2
            if atom in disp_dict:
                dx, dz = disp_dict[atom]
                if dx is not None and abs(dx - exp_dx) <= disp_tol:
                    passed += 1
                if dz is not None and abs(dz - exp_dz) <= disp_tol:
                    passed += 1

        for layer, exp in ed_map.items():
            total += 1
            val = electron_densities.get(layer)
            if val is not None and abs(val - exp) <= ed_tol:
                passed += 1

        # trend 1: 1' dz > 0 and dz > dz(1)
        total += 1
        if "1'" in disp_dict and "1" in disp_dict:
            dz1p = disp_dict["1'"][1]
            dz1 = disp_dict["1"][1]
            if dz1p is not None and dz1 is not None and dz1p > 0 and dz1p > dz1:
                passed += 1

        # trend 2: C3-C3 bond length in three-layer > monolayer
        mono_data = ctx.get("monolayer", {})
        mono_bl = mono_data.get("bond_lengths", {}) if isinstance(mono_data, dict) else {}
        mono_c3c3 = mono_bl.get("C3-C3")
        three_c3c3 = bond_lengths.get("C3C3")
        total += 1
        if mono_c3c3 is not None and three_c3c3 is not None and three_c3c3 > mono_c3c3:
            passed += 1

        # trend 3: electron density 2 2' > 1 1'
        total += 1
        val1 = electron_densities.get("1 1'")
        val2 = electron_densities.get("2 2'")
        if val1 is not None and val2 is not None and val2 > val1:
            passed += 1

        score = passed / total if total > 0 else 0.0
        return score


_SCORERS = {
    'monolayer_analysis': score_0,
    'threelayer_analysis': score_1,
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
