import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, io


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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    gold = step.get("gold", {})
    tolerance = float(step.get("tolerance", 0.3))
    def _get_float(k):
        v = artifact.get(k)
        try:
            f = float(v)
            return f
        except (TypeError, ValueError):
            return None
    v_o1 = _get_float("V_O1")
    v_o3 = _get_float("V_O3")
    v_n1 = _get_float("V_N1")
    v_n3 = _get_float("V_N3")
    if any(v is None for v in (v_o1, v_o3, v_n1, v_n3)):
        return 0.0
    ord_score = 0.0
    if v_o1 < v_o3:
        ord_score += 0.5
    if v_n1 < v_n3:
        ord_score += 0.5
    vals = {"V_O1": v_o1, "V_O3": v_o3, "V_N1": v_n1, "V_N3": v_n3}
    val_score = 0.0
    cnt = 0
    for key in ("V_O1", "V_O3", "V_N1", "V_N3"):
        g = gold.get(key)
        if g is None:
            continue
        a = vals[key]
        cnt += 1
        err = abs(a - g)
        val_score += max(0.0, 1.0 - err / tolerance)
    if cnt > 0:
        val_score /= cnt
    return 0.4 * ord_score + 0.6 * val_score


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    target = step.get("target_position", [2.0455, 2.0455, 0.0])
    threshold = step.get("distance_threshold", 2.0)
    lines = artifact.strip().splitlines()
    if len(lines) < 3:
        return 0.0
    coords = []
    for line in lines[2:]:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        if parts[0].strip().lower() != 'o':
            continue
        try:
            x = float(parts[1]); y = float(parts[2]); z = float(parts[3])
            dist = math.sqrt((x-target[0])**2 + (y-target[1])**2 + (z-target[2])**2)
            coords.append(dist)
        except Exception:
            continue
    if not coords:
        return 0.0
    return 1.0 if min(coords) < threshold else 0.0


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    f = io.StringIO(artifact)
    reader = csv.DictReader(f)
    rows = list(reader)
    if not rows:
        return 0.0
    data = {}
    for row in rows:
        try:
            x = int(row["x"])
            site = row["site"].strip()
            ov = float(row["overpotential [V]"])
        except Exception:
            continue
        data.setdefault(x, []).append((site, ov))
    sorted_x = sorted(data.keys())
    trend_ok = True
    margin_ok = True
    trend_tol = step.get("trend_tolerance", 0.1)
    margin_req = step.get("site_margin", 0.15)
    for i in range(1, len(sorted_x)):
        px = sorted_x[i-1]
        cx = sorted_x[i]
        pmax = max(v for _,v in data[px])
        cmin = min(v for _,v in data[cx])
        if cmin + trend_tol < pmax:
            trend_ok = False
            break
    if 1 in data:
        x1_sites = {s: v for s,v in data[1]}
        if "Ta2" in x1_sites and "Ta3" in x1_sites:
            if x1_sites["Ta2"] - x1_sites["Ta3"] < margin_req:
                margin_ok = False
        else:
            margin_ok = False
    else:
        margin_ok = False
    ref = step.get("reference_overpotentials", [])
    val_score = 0.0
    cnt = 0
    for row in rows:
        try:
            x = int(row["x"])
            site = row["site"].strip()
            ov = float(row["overpotential [V]"])
        except Exception:
            continue
        for r in ref:
            if r["x"] == x and r["site"] == site:
                err = abs(ov - r["value"])
                val_score += max(0.0, 1.0 - err / step.get("value_tolerance", 0.2))
                cnt += 1
                break
    if cnt > 0:
        val_score /= cnt
    score = 0.0
    if trend_ok:
        score += 0.5
    if margin_ok:
        score += 0.3
    score += 0.2 * val_score
    return min(score, 1.0)


# === block: score_3 (check id='step_05') ===
def score_3(artifact, step, ctx):
    f = io.StringIO(artifact)
    reader = csv.DictReader(f)
    rows = list(reader)
    if not rows:
        return 0.0
    data = []
    for row in rows:
        try:
            x = int(row["x"])
            sxx = float(row["sigma_xx [GPa]"])
            syy = float(row["sigma_yy [GPa]"])
            data.append((x, sxx, syy))
        except Exception:
            return 0.0
    data.sort(key=lambda t: t[0])
    tol = step.get("trend_tolerance", 0.1)
    score_xx = 0
    score_yy = 0
    n = len(data)
    for i in range(1, n):
        if data[i][1] <= data[i-1][1] + tol:
            score_xx += 1
        if data[i][2] <= data[i-1][2] + tol:
            score_yy += 1
    transitions = n - 1
    if transitions == 0:
        return 1.0
    return (score_xx + score_yy) / (2 * transitions)


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
    'step_05': score_3,
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
