import os
import json
import csv

# === author imports / helpers ===
import os
import json
import csv
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
        ctx = {}
        path = os.path.join(outputs_dir, "vertical_energies.csv")
        if os.path.exists(path):
            with open(path, newline='') as f:
                reader = csv.DictReader(f)
                ctx["vertical_data"] = [dict(row) for row in reader]
        return ctx


# === block: score_0 (check id='lateral_check') ===
def score_0(artifact, step, ctx):
        import csv
        import math
        # Load CSV
        artifact_path = os.path.join("/app/outputs", step.get("output_file", ""))
        if not os.path.exists(artifact_path):
            return 0.0
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            return 0.0
        # Extract data
        data = []
        for r in rows:
            try:
                fld = float(r["field_lateral_kV_per_cm"])
                en = float(r["energy_eV"])
                es = float(r["electron_shift_meV"])
                hs = float(r["hole_shift_meV"])
                data.append((fld, en, es, hs))
            except (KeyError, ValueError):
                continue
        if not data:
            return 0.0
        data.sort(key=lambda x: x[0])
        # Sub-scores
        s1 = 0.0  # gold 150 kV/cm
        found_150 = False
        for fld, en, es, hs in data:
            if abs(fld - 150.0) < 1e-6:
                found_150 = True
                # energy check
                gold_en = float(step.get("gold_lateral_150_energy_eV", 3.69))
                tol_en = float(step.get("tol_energy_eV", 0.03))
                if abs(en - gold_en) <= tol_en:
                    s1 += 0.3
                else:
                    s1 += max(0.0, 1.0 - (abs(en - gold_en) - tol_en) / tol_en) * 0.3
                # total shift check (electron + hole)
                total_shift = es + hs
                gold_shift = float(step.get("gold_lateral_150_total_shift_meV", 20.0))
                tol_shift = float(step.get("tol_shift_meV", 5.0))
                if abs(total_shift - gold_shift) <= tol_shift:
                    s1 += 0.3
                else:
                    s1 += max(0.0, 1.0 - (abs(total_shift - gold_shift) - tol_shift) / tol_shift) * 0.3
                break
        if not found_150:
            s1 = 0.0
        # Structural: energy monotonically decreasing with field
        energies = [en for fld, en, es, hs in data if fld >= 0]
        mono = all(energies[i] >= energies[i+1] - 1e-6 for i in range(len(energies)-1))
        s2 = 0.2 if mono else 0.0
        # Structural: shifts positive and increasing
        e_shifts = [es for fld, en, es, hs in data if fld > 0]
        h_shifts = [hs for fld, en, es, hs in data if fld > 0]
        shift_ok = (all(s >= -1e-6 for s in e_shifts) and all(s >= -1e-6 for s in h_shifts) and
                    all(e_shifts[i] <= e_shifts[i+1] + 1e-3 for i in range(len(e_shifts)-1)) and
                    all(h_shifts[i] <= h_shifts[i+1] + 1e-3 for i in range(len(h_shifts)-1)))
        s3 = 0.2 if shift_ok else 0.0
        return min(1.0, s1 + s2 + s3)


# === block: score_1 (check id='vertical_check') ===
def score_1(artifact, step, ctx):
        import csv
        import math
        artifact_path = os.path.join("/app/outputs", step.get("output_file", ""))
        if not os.path.exists(artifact_path):
            return 0.0
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            return 0.0
        data = []
        for r in rows:
            try:
                fld = float(r["field_vertical_kV_per_cm"])
                en = float(r["energy_eV"])
                data.append((fld, en))
            except (KeyError, ValueError):
                continue
        if not data:
            return 0.0
        data.sort(key=lambda x: x[0])
        # Find 0 and 300
        base_en = None
        en_300 = None
        for fld, en in data:
            if abs(fld - 0.0) < 1e-6:
                base_en = en
            if abs(fld - 300.0) < 1e-6:
                en_300 = en
        s1 = 0.0
        if base_en is not None and en_300 is not None:
            shift_mev = (en_300 - base_en) * 1000.0  # eV to meV
            gold_shift = float(step.get("gold_vertical_300_shift_meV", 30.0))
            tol_shift = float(step.get("tol_shift_meV", 5.0))
            if abs(shift_mev - gold_shift) <= tol_shift:
                s1 = 0.6
            else:
                s1 = max(0.0, 1.0 - (abs(shift_mev - gold_shift) - tol_shift) / tol_shift) * 0.6
        # Structural: energy monotonically increasing with field
        energies = [en for fld, en in data if fld >= 0]
        mono = all(energies[i] <= energies[i+1] + 1e-6 for i in range(len(energies)-1))
        s2 = 0.4 if mono else 0.0
        return min(1.0, s1 + s2)


# === block: score_2 (check id='angle_check') ===
def score_2(artifact, step, ctx):
        import csv
        import math
        artifact_path = os.path.join("/app/outputs", step.get("output_file", ""))
        if not os.path.exists(artifact_path):
            return 0.0
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            return 0.0
        data = []
        for r in rows:
            try:
                tfld = float(r["total_field_kV_per_cm"])
                ang = float(r["angle_rad"])
                en = float(r["energy_eV"])
                data.append((tfld, ang, en))
            except (KeyError, ValueError):
                continue
        if not data:
            return 0.0
        # Group by total_field
        by_field = {}
        for tfld, ang, en in data:
            by_field.setdefault(tfld, []).append((ang, en))
        # Structural: for each field, energy monotonically decreasing with angle
        s1 = 0.0
        fields_ok = 0
        total_fields = len(by_field)
        for tfld, pts in by_field.items():
            pts.sort(key=lambda x: x[0])
            energies = [en for _, en in pts]
            if all(energies[i] >= energies[i+1] - 1e-6 for i in range(len(energies)-1)):
                fields_ok += 1
        if total_fields > 0:
            s1 = (fields_ok / total_fields) * 0.5
        # Cross-check with vertical_energies.csv at angle=0
        s2 = 0.0
        vert_data = ctx.get("vertical_data")
        if vert_data is not None:
            vert_by_field = {}
            for vrow in vert_data:
                try:
                    vf = float(vrow["field_vertical_kV_per_cm"])
                    ven = float(vrow["energy_eV"])
                    vert_by_field[vf] = ven
                except (KeyError, ValueError):
                    continue
            match_count = 0
            total_angle0 = 0
            for tfld, pts in by_field.items():
                angle0_pts = [en for ang, en in pts if abs(ang) < 1e-9]
                if not angle0_pts:
                    continue
                total_angle0 += 1
                vert_en = vert_by_field.get(tfld)
                if vert_en is not None and abs(angle0_pts[0] - vert_en) <= 0.01:
                    match_count += 1
            if total_angle0 > 0:
                s2 = (match_count / total_angle0) * 0.5
        return min(1.0, s1 + s2)


# === block: score_3 (check id='fit_check') ===
def score_3(artifact, step, ctx):
        import json
        import math
        artifact_path = os.path.join("/app/outputs", step.get("output_file", ""))
        if not os.path.exists(artifact_path):
            return 0.0
        with open(artifact_path) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return 0.0
        if not isinstance(data, dict):
            return 0.0
        w = 1.0 / 3.0
        score = 0.0
        # dipole
        val = data.get("permanent_dipole_eA")
        if isinstance(val, (int, float)):
            gold = float(step.get("gold_dipole_eA", 1.26))
            tol = float(step.get("tol_dipole_eA", 0.2))
            if abs(val - gold) <= tol:
                score += w
            else:
                score += max(0.0, 1.0 - (abs(val - gold) - tol) / tol) * w
        # polarizability
        val = data.get("polarizability_meV_per_MVcm2")
        if isinstance(val, (int, float)):
            gold = float(step.get("gold_pol", 95.28))
            tol = float(step.get("tol_pol", 5.0))
            if abs(val - gold) <= tol:
                score += w
            else:
                score += max(0.0, 1.0 - (abs(val - gold) - tol) / tol) * w
        # internal field
        val = data.get("internal_piezoelectric_field_MV_per_cm")
        if isinstance(val, (int, float)):
            gold = float(step.get("gold_int_field_MVcm", 0.7))
            tol = float(step.get("tol_int_field_MVcm", 0.1))
            if abs(val - gold) <= tol:
                score += w
            else:
                score += max(0.0, 1.0 - (abs(val - gold) - tol) / tol) * w
        return min(1.0, score)


_SCORERS = {
    'lateral_check': score_0,
    'vertical_check': score_1,
    'angle_check': score_2,
    'fit_check': score_3,
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
