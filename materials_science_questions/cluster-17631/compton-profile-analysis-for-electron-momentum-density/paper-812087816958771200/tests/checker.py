import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math, cmath


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
    grading = spec
    scattering_gold = grading.get('scattering_factors_gold', [])
    compton_gold = grading.get('compton_profiles_gold', [])
    jzero_axis = grading.get('jzero_axis', {})
    return {
        'scattering_gold': scattering_gold,
        'compton_gold': compton_gold,
        'jzero_axis': jzero_axis
    }


# === block: score_0 (check id='scattering_factors') ===
def score_0(artifact, step, ctx):
    import math
    def score(artifact, step, ctx):
        tol = float(step.get('tolerance', 5e-4))
        gold_rows = ctx.get('scattering_gold', [])
        if not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        if not all(col in artifact[0] for col in ['s', 'F_x_N', 'F_y_N', 'F_z_N']):
            return 0.0
        art_map = {}
        for row in artifact:
            try:
                s_val = float(row['s'])
                art_map[s_val] = row
            except:
                continue
        if len(art_map) < len(gold_rows):
            return 0.0
        compare_cols = ['F_x_N', 'F_y_N', 'F_z_N']
        total = len(gold_rows) * len(compare_cols)
        good = 0
        for gr in gold_rows:
            s_gold = gr['s']
            if s_gold not in art_map:
                continue
            art_row = art_map[s_gold]
            for col in compare_cols:
                try:
                    val = float(art_row.get(col, ''))
                except:
                    continue
                gold = gr[col]
                if gold == 0:
                    if abs(val) < 1e-12:
                        good += 1
                else:
                    err = abs(val - gold) / max(abs(gold), 1e-12)
                    if err <= tol:
                        good += 1
        return min(1.0, good / total) if total > 0 else 0.0


# === block: score_1 (check id='compton_profiles') ===
def score_1(artifact, step, ctx):
    import math
    def score(artifact, step, ctx):
        tol = float(step.get('tolerance', 5e-4))
        gold_rows = ctx.get('compton_gold', [])
        if not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        required = ['q', 'J_x', 'J_y', 'J_z', 'J_iso']
        if not all(col in artifact[0] for col in required):
            return 0.0
        art_map = {}
        for row in artifact:
            try:
                q_val = float(row['q'])
                art_map[q_val] = row
            except:
                continue
        if len(art_map) < len(gold_rows):
            return 0.0
        compare_cols = ['J_x', 'J_y', 'J_z', 'J_iso']
        total = len(gold_rows) * len(compare_cols)
        good = 0
        for gr in gold_rows:
            q_gold = gr['q']
            if q_gold not in art_map:
                continue
            art_row = art_map[q_gold]
            for col in compare_cols:
                try:
                    val = float(art_row.get(col, ''))
                except:
                    continue
                gold = gr[col]
                if gold == 0:
                    if abs(val) < 1e-12:
                        good += 1
                else:
                    err = abs(val - gold) / max(abs(gold), 1e-12)
                    if err <= tol:
                        good += 1
        return min(1.0, good / total) if total > 0 else 0.0


# === block: score_2 (check id='jzero_surface') ===
def score_2(artifact, step, ctx):
    import math, cmath
    def score(artifact, step, ctx):
        axis = ctx.get('jzero_axis', {})
        J_x = axis.get('J_x', 17.964)
        J_y = axis.get('J_y', 17.546)
        J_z = axis.get('J_z', 17.735)
        tol = 5e-4
        if not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        required = ['theta_deg', 'phi_deg', 'J0']
        if not all(col in artifact[0] for col in required):
            return 0.0
        rows = []
        for r in artifact:
            try:
                theta = float(r['theta_deg'])
                phi = float(r['phi_deg'])
                j0 = float(r['J0'])
                rows.append((theta, phi, j0))
            except:
                pass
        if len(rows) < 100:
            return 0.0

        # Axis checks
        found_z = False
        found_x = False
        found_y = False
        for theta, phi, j0 in rows:
            if abs(theta) < 1e-6:
                if abs(j0 - J_z) / max(abs(J_z), 1e-12) <= tol:
                    found_z = True
            if abs(theta - 90.0) < 1e-6:
                if abs(phi) < 1e-6 and abs(j0 - J_x) / max(abs(J_x), 1e-12) <= tol:
                    found_x = True
                if abs(phi - 90.0) < 1e-6 and abs(j0 - J_y) / max(abs(J_y), 1e-12) <= tol:
                    found_y = True
        axis_score = sum([found_z, found_x, found_y]) / 3.0

        # Flat region (theta <= 30)
        flat_vals = [j0 for theta, phi, j0 in rows if theta <= 30.0]
        flat_score = 0.0
        if flat_vals:
            mean_val = sum(flat_vals) / len(flat_vals)
            std_val = (sum((v - mean_val)**2 for v in flat_vals) / len(flat_vals)) ** 0.5
            if abs(mean_val - J_z) < 0.2 and std_val < 0.3:
                flat_score = 1.0

        # Sixfold pattern at theta = 90
        theta90_vals = {}
        for theta, phi, j0 in rows:
            if abs(theta - 90.0) < 1e-6:
                theta90_vals[phi] = j0
        sixfold_score = 0.0
        if theta90_vals:
            phis = sorted(theta90_vals.keys())
            if len(phis) >= 12:
                N = len(phis)
                F6 = 0.0
                for phi in phis:
                    F6 += theta90_vals[phi] * cmath.exp(1j * 6 * math.radians(phi))
                F6 /= N
                power_total = 0.0
                for k in range(1, 13):
                    Fk = 0.0
                    for phi in phis:
                        Fk += theta90_vals[phi] * cmath.exp(1j * k * math.radians(phi))
                    Fk /= N
                    power_total += abs(Fk) ** 2
                if power_total > 0:
                    ratio = abs(F6)**2 / power_total
                    if ratio > 0.5:
                        sixfold_score = 1.0

        return 0.4 * axis_score + 0.3 * flat_score + 0.3 * sixfold_score


_SCORERS = {
    'scattering_factors': score_0,
    'compton_profiles': score_1,
    'jzero_surface': score_2,
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
