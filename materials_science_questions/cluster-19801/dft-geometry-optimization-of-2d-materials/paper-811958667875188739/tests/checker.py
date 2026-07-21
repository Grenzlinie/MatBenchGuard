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
    steps = spec.get("steps", spec.get("checks", []))
    gold_table = None
    for s in steps:
        if s.get("id") == "value_compare":
            gold_table = s.get("gold_table", [])
            break
    return {"gold_table": gold_table}


# === block: score_0 (check id='value_compare') ===
def score_0(artifact, step, ctx):
    gold_table = ctx.get("gold_table", [])
    if not isinstance(artifact, list) or not gold_table:
        return 0.0
    total = len(gold_table)
    row_scores = []
    tol_angle = step.get("tolerance_angle_deg", 2.0)
    tol_len = step.get("tolerance_length_A", 0.05)
    max_dev_angle = step.get("max_dev_angle_deg", 10.0)
    max_dev_len = step.get("max_dev_length_A", 0.20)
    for entry in gold_table:
        cfg = entry["configuration"]
        chg = entry["charge_state"]
        gold_ang = entry["angle_deg"]
        gold_len = entry["length_A"]
        matching = [r for r in artifact if r.get("configuration","").strip() == cfg and r.get("charge_state","").strip() == chg]
        if not matching:
            row_scores.append(0.0)
            continue
        row = matching[0]
        try:
            rep_ang = float(row.get("buckling_angle_deg", 0.0))
            rep_len = float(row.get("bond_length_A", 0.0))
        except (ValueError, TypeError):
            row_scores.append(0.0)
            continue
        diff_ang = abs(rep_ang - gold_ang)
        if diff_ang <= tol_angle:
            ang_score = 1.0
        else:
            ang_score = max(0.0, 1.0 - (diff_ang - tol_angle) / (max_dev_angle - tol_angle))
        diff_len = abs(rep_len - gold_len)
        if diff_len <= tol_len:
            len_score = 1.0
        else:
            len_score = max(0.0, 1.0 - (diff_len - tol_len) / (max_dev_len - tol_len))
        row_scores.append((ang_score + len_score) / 2.0)
    return sum(row_scores) / total


# === block: score_1 (check id='trend_validate') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    def get_row(cfg, chg):
        for r in artifact:
            if r.get("configuration","").strip() == cfg and r.get("charge_state","").strip() == chg:
                try:
                    ang = float(r.get("buckling_angle_deg", 0.0))
                    leng = float(r.get("bond_length_A", 0.0))
                    return ang, leng
                except (ValueError, TypeError):
                    return None, None
        return None, None
    hd1_angles = {}
    hd1_lengths = {}
    for chg in ["Ne-1","Ne","Ne+1","Ne+2"]:
        a, l = get_row("HD1", chg)
        if a is None or l is None:
            return 0.0
        hd1_angles[chg] = a
        hd1_lengths[chg] = l
    trend_ok = True
    if not (hd1_angles["Ne-1"] > hd1_angles["Ne"] > hd1_angles["Ne+1"] > hd1_angles["Ne+2"]):
        trend_ok = False
    if not (hd1_lengths["Ne-1"] < hd1_lengths["Ne"] < hd1_lengths["Ne+1"] < hd1_lengths["Ne+2"]):
        trend_ok = False
    hd2_angles = []
    hd2_lengths = []
    for chg in ["Ne","Ne+1","Ne+2"]:
        a, l = get_row("HD2", chg)
        if a is None or l is None:
            return 0.0
        hd2_angles.append(a)
        hd2_lengths.append(l)
    if len(hd2_angles) == 3:
        if max(hd2_angles) - min(hd2_angles) > step.get("hd2_angle_max_variation", 1.0):
            trend_ok = False
        if max(hd2_lengths) - min(hd2_lengths) > step.get("hd2_length_max_variation", 0.01):
            trend_ok = False
    else:
        trend_ok = False
    return 1.0 if trend_ok else 0.0


_SCORERS = {
    'value_compare': score_0,
    'trend_validate': score_1,
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
