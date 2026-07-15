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
    gold_table = spec.get("gold_table", {})
    phases = gold_table.get("phases", [])
    gold_by_phase = {}
    pd_frac_by_phase = {}
    for p in phases:
        gold_by_phase[p["phase"]] = p
        pd_frac_by_phase[p["phase"]] = p.get("pd_mole_fraction", None)
    return {"gold_by_phase": gold_by_phase, "phases_list": phases, "pd_frac_by_phase": pd_frac_by_phase}


# === block: score_0 (check id='properties_tolerance') ===
def score_0(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        rows = {row.get("phase",""): row for row in artifact}
        phases_gold = ctx.get("phases_list", [])
        if not phases_gold:
            return 0.0
        total_score = 0.0
        count = 0
        for gold_entry in phases_gold:
            phase = gold_entry["phase"]
            row = rows.get(phase)
            if not row:
                continue
            sub_scores = []
            gold_fe = gold_entry["formation_energy_eV_atom"]
            try:
                fe = float(row.get("formation_energy_eV_atom"))
            except:
                fe = None
            if fe is not None:
                err = fe - gold_fe
                fp_floor = 0.01
                tol_abs = 0.1
                if err <= fp_floor:
                    sub_scores.append(1.0)
                else:
                    sub_scores.append(max(0.0, 1.0 - (err - fp_floor) / (tol_abs - fp_floor)))
            else:
                sub_scores.append(0.0)
            for lat_key, gold_lat in [("a_A", gold_entry["a_A"]), ("b_A", gold_entry["b_A"]), ("c_A", gold_entry["c_A"])]:
                try:
                    lat_val = float(row.get(lat_key))
                except:
                    sub_scores.append(0.0)
                    continue
                if gold_lat == 0:
                    sub_scores.append(1.0 if abs(lat_val) < 1e-6 else 0.0)
                    continue
                rel_diff = abs(lat_val - gold_lat) / abs(gold_lat)
                tol_rel = 0.02
                max_rel = 0.05
                if rel_diff <= tol_rel:
                    sub_scores.append(1.0)
                elif rel_diff <= max_rel:
                    sub_scores.append(max(0.0, 1.0 - (rel_diff - tol_rel) / (max_rel - tol_rel)))
                else:
                    sub_scores.append(0.0)
            gold_bulk = gold_entry["bulk_modulus_GPa"]
            try:
                bulk = float(row.get("bulk_modulus_GPa"))
            except:
                sub_scores.append(0.0)
            else:
                if gold_bulk == 0:
                    sub_scores.append(1.0 if abs(bulk) < 1e-6 else 0.0)
                else:
                    rel_diff = abs(bulk - gold_bulk) / abs(gold_bulk)
                    tol_rel = 0.10
                    max_rel = 0.20
                    if rel_diff <= tol_rel:
                        sub_scores.append(1.0)
                    elif rel_diff <= max_rel:
                        sub_scores.append(max(0.0, 1.0 - (rel_diff - tol_rel) / (max_rel - tol_rel)))
                    else:
                        sub_scores.append(0.0)
            phase_score = sum(sub_scores) / len(sub_scores) if sub_scores else 0.0
            total_score += phase_score
            count += 1
        if count == 0:
            return 0.0
        return total_score / count


# === block: score_1 (check id='convex_hull') ===
def score_1(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        pd_frac_by_phase = ctx.get("pd_frac_by_phase", {})
        points = []
        for row in artifact:
            phase = row.get("phase")
            if phase in pd_frac_by_phase:
                try:
                    fe = float(row.get("formation_energy_eV_atom"))
                except:
                    continue
                x = pd_frac_by_phase[phase]
                points.append((x, fe))
        if len(points) < 2:
            return 1.0
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        pts = sorted(points, key=lambda p: (p[0], p[1]))
        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        eps = 0.01
        hull_len = len(lower)
        if hull_len == 1:
            hull_y = lower[0][1]
            for x, y in points:
                if y > hull_y + eps:
                    return 0.0
            return 1.0
        for (x, y) in points:
            hull_y_val = None
            for i in range(hull_len-1):
                x1, y1 = lower[i]
                x2, y2 = lower[i+1]
                if x1 <= x <= x2 or x2 <= x <= x1:
                    if x2 == x1:
                        hull_y_val = max(y1, y2)
                    else:
                        t = (x - x1) / (x2 - x1)
                        hull_y_val = y1 + t * (y2 - y1)
                    break
            if hull_y_val is not None and y > hull_y_val + eps:
                return 0.0
        return 1.0


_SCORERS = {
    'properties_tolerance': score_0,
    'convex_hull': score_1,
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
