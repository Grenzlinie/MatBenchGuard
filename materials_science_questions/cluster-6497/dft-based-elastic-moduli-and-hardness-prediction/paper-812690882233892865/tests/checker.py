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
    return {"spec": spec}


# === block: score_0 (check id='results') ===
def score_0(artifact, step, ctx):
        fields = step.get("fields", {})
        sub_weights = step.get("sub_weights", {})
        if not isinstance(artifact, dict):
            return 0.0
        def getv(k):
            return artifact.get(k)
        def score_abs(val, target, tol):
            if val is None:
                return 0.0
            diff = abs(val - target)
            if diff < tol:
                return 1.0
            elif diff < 2*tol:
                return 0.5
            else:
                return 0.0
        lc_score = score_abs(getv("lattice_constant_A"), fields["lattice_constant_A"]["target"], fields["lattice_constant_A"]["tolerance_abs"])
        c11_score = score_abs(getv("C11"), fields["C11"]["target"], fields["C11"]["tolerance_abs"])
        c12_score = score_abs(getv("C12"), fields["C12"]["target"], fields["C12"]["tolerance_abs"])
        c44_score = score_abs(getv("C44"), fields["C44"]["target"], fields["C44"]["tolerance_abs"])
        C11_v = getv("C11")
        C12_v = getv("C12")
        C44_v = getv("C44")
        if C11_v is None or C12_v is None or C44_v is None:
            bv_score = gv_score = k_score = hv_score = 0.0
        else:
            B_V_re = (C11_v + 2*C12_v) / 3.0
            G_V_re = (C11_v - C12_v + 3*C44_v) / 5.0
            k_re = G_V_re / B_V_re if B_V_re != 0 else 0.0
            try:
                H_V_re = 2.0 * ( (k_re**2) * G_V_re )**0.585 - 3.0
            except:
                H_V_re = -999
            def score_rel(val, target, tol_rel):
                if val is None or target == 0:
                    return 0.0
                rel_diff = abs(val - target) / target
                if rel_diff < tol_rel:
                    return 1.0
                elif rel_diff < 2*tol_rel:
                    return 0.5
                else:
                    return 0.0
            bv_score = score_rel(B_V_re, fields["B_V"]["target"], fields["B_V"]["tolerance_rel"])
            gv_score = score_rel(G_V_re, fields["G_V"]["target"], fields["G_V"]["tolerance_rel"])
            k_score = score_abs(k_re, fields["k"]["target"], fields["k"]["tolerance_abs"])
            hv_score = score_abs(H_V_re, fields["H_V"]["target"], fields["H_V"]["tolerance_abs"])
        total = 0.0
        for key, w in sub_weights.items():
            if key == "lattice_constant_A":
                s = lc_score
            elif key == "C11":
                s = c11_score
            elif key == "C12":
                s = c12_score
            elif key == "C44":
                s = c44_score
            elif key == "B_V":
                s = bv_score
            elif key == "G_V":
                s = gv_score
            elif key == "k":
                s = k_score
            elif key == "H_V":
                s = hv_score
            else:
                s = 0.0
            total += w * s
        return total


# === block: score_1 (check id='stress_strain_curves') ===
def score_1(artifact, step, ctx):
        modes = step.get("modes", [])
        min_tensile_gold = step.get("min_tensile_gold")
        min_shear_gold = step.get("min_shear_gold")
        tol_rel_down = step.get("tol_rel_down", 0.05)
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        if not all(c in artifact[0] for c in ("deformation_mode","strain","stress")):
            return 0.0
        mode_data = {m: [] for m in modes}
        for row in artifact:
            m = row.get("deformation_mode")
            if m in mode_data:
                try:
                    strain = float(row["strain"])
                    stress = float(row["stress"])
                    mode_data[m].append((strain, stress))
                except:
                    pass
        for m in mode_data:
            mode_data[m].sort(key=lambda x: x[0])
        epsilon = 0.1
        monotonic_count = 0
        peak_stresses = {}
        for m, data in mode_data.items():
            if not data:
                continue
            stresses = [p[1] for p in data]
            max_idx = stresses.index(max(stresses))
            inc = True
            for i in range(1, max_idx+1):
                if stresses[i] < stresses[i-1] - epsilon:
                    inc = False
                    break
            dec = True
            for i in range(max_idx+1, len(stresses)):
                if stresses[i] > stresses[i-1] + epsilon:
                    dec = False
                    break
            if inc and dec:
                monotonic_count += 1
            peak_stresses[m] = max(stresses)
        monotonic_score = monotonic_count / len(modes) if len(modes) > 0 else 1.0
        tensile_modes = ["tensile_100","tensile_110","tensile_111"]
        shear_modes = ["shear_110_001","shear_100_010","shear_111_11-2"]
        tensile_peaks = [peak_stresses.get(m, -1) for m in tensile_modes if m in peak_stresses]
        shear_peaks = [peak_stresses.get(m, -1) for m in shear_modes if m in peak_stresses]
        if not tensile_peaks:
            min_tensile_score = 0.0
        else:
            min_tensile = min(tensile_peaks)
            threshold_tensile = min_tensile_gold * (1 - tol_rel_down) if min_tensile_gold else 0
            if min_tensile >= threshold_tensile:
                min_tensile_score = 1.0
            elif min_tensile >= 0.8 * min_tensile_gold:
                min_tensile_score = min_tensile / (0.8 * min_tensile_gold)
            else:
                min_tensile_score = 0.0
        if not shear_peaks:
            min_shear_score = 0.0
        else:
            min_shear = min(shear_peaks)
            threshold_shear = min_shear_gold * (1 - tol_rel_down) if min_shear_gold else 0
            if min_shear >= threshold_shear:
                min_shear_score = 1.0
            elif min_shear >= 0.8 * min_shear_gold:
                min_shear_score = min_shear / (0.8 * min_shear_gold)
            else:
                min_shear_score = 0.0
        total = 0.1 * monotonic_score + 0.45 * min_tensile_score + 0.45 * min_shear_score
        return total


_SCORERS = {
    'results': score_0,
    'stress_strain_curves': score_1,
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
