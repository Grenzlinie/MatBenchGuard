import os
import json
import csv

# === author imports / helpers ===
import os
import csv
import re
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
    gold = {}
    for step in spec.get("steps", []):
        if step.get("output_file") == "phase_transition_D.txt":
            gold["dc"] = step.get("gold", {})
            gold["dc_tol"] = step.get("tolerance", 0.1)
            break
    return gold


# === block: score_0 (check id='step_adw') ===
def score_0(artifact, step, ctx):
    rows = artifact   # already loaded as list of dicts; artifact must be non-empty
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    # expected U values from -6.0 to -0.5 step 0.5
    required_u = [round(-6.0 + i*0.5, 1) for i in range(12)]
    found_u = {}
    malformed = False
    for r in rows:
        try:
            u = float(r.get("U", None))
            m = float(r.get("M_ADW", None))
            z = float(r.get("Z", None))
            found_u[u] = (m, z)
        except (TypeError, ValueError):
            malformed = True
            break
    if malformed or set(required_u) != set(found_u.keys()):
        return 0.0
    points = [(abs(u), m, z) for u, (m, z) in found_u.items()]
    points.sort(key=lambda x: x[0])
    # monotonic non-decreasing M_ADW with |U|
    prev = points[0][1]
    mono_ok = True
    for _, mval, _ in points[1:]:
        if mval < prev - 1e-9:
            mono_ok = False
            break
        prev = mval
    # bounds
    bounds_ok = True
    for absu, mval, zval in points:
        if not (0.0 <= mval <= 1.0):
            bounds_ok = False
        if absu >= 4.0 and mval < 0.9:
            bounds_ok = False
        if absu <= 1.0 and mval > 0.5:
            bounds_ok = False
    # Z stability: all Z between 0.8 and 1.2
    z_ok = all(0.8 <= zval <= 1.2 for _, _, zval in points)
    score = 0.0
    if mono_ok:
        score += 0.4
    if bounds_ok:
        score += 0.4
    if z_ok:
        score += 0.2
    return score


# === block: score_1 (check id='step_af') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    # expected U values from 0.5 to 6.0 step 0.5
    required_u = [round(0.5 + i*0.5, 1) for i in range(12)]
    found_u = {}
    malformed = False
    for r in rows:
        try:
            u = float(r.get("U", None))
            m = float(r.get("M_AF", None))
            z = float(r.get("Z", None))
            found_u[u] = (m, z)
        except (TypeError, ValueError):
            malformed = True
            break
    if malformed or set(required_u) != set(found_u.keys()):
        return 0.0
    points = [(u, m, z) for u, (m, z) in found_u.items()]
    points.sort(key=lambda x: x[0])
    # monotonic non-decreasing M_AF with U (positive U increasing)
    prev = points[0][1]
    mono_ok = True
    for _, mval, _ in points[1:]:
        if mval < prev - 1e-9:
            mono_ok = False
            break
        prev = mval
    # bounds
    bounds_ok = True
    for uval, mval, zval in points:
        if not (0.0 <= mval <= 1.0):
            bounds_ok = False
        if uval >= 4.0 and mval < 0.9:
            bounds_ok = False
        if uval <= 1.0 and mval > 0.5:
            bounds_ok = False
    # Z stability
    z_ok = all(0.8 <= zval <= 1.2 for _, _, zval in points)
    score = 0.0
    if mono_ok:
        score += 0.4
    if bounds_ok:
        score += 0.4
    if z_ok:
        score += 0.2
    return score


# === block: score_2 (check id='step_dc') ===
def score_2(artifact, step, ctx):
    import re
    text = artifact   # string
    if not isinstance(text, str):
        return 0.0
    gold_att = ctx.get("dc", {}).get("D_c_attractive", 1.27)
    gold_rep = ctx.get("dc", {}).get("D_c_repressive", 1.46)
    tol = ctx.get("dc_tol", 0.1)
    pat1 = re.search(r'D_c_attractive\s*=\s*([0-9]*\.?[0-9]+)', text)
    pat2 = re.search(r'D_c_repressive\s*=\s*([0-9]*\.?[0-9]+)', text)
    if pat1 is None or pat2 is None:
        return 0.0
    val_att = float(pat1.group(1))
    val_rep = float(pat2.group(1))
    def score_single(val, gold):
        err = abs(val - gold)
        if err <= tol:
            return 1.0
        # partial credit beyond tolerance: linear decay with a scaling factor of 0.5
        return max(0.0, 1.0 - (err - tol) / 0.5)
    s_att = score_single(val_att, gold_att)
    s_rep = score_single(val_rep, gold_rep)
    return 0.5 * s_att + 0.5 * s_rep


_SCORERS = {
    'step_adw': score_0,
    'step_af': score_1,
    'step_dc': score_2,
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
