import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='step_05') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    wl = []
    I_fund = []
    I_ov = {2:[], 3:[], 4:[], 5:[]}
    for row in artifact:
        wl.append(float(row['wavelength_nm']))
        I_fund.append(float(row['intensity_fundamental']))
        I_ov[2].append(float(row['intensity_overtone_2']))
        I_ov[3].append(float(row['intensity_overtone_3']))
        I_ov[4].append(float(row['intensity_overtone_4']))
        I_ov[5].append(float(row['intensity_overtone_5']))
    dip_range = step.get('check_dip_range_nm', [210,220])
    dip_ratio_thresh = step.get('dip_ratio_threshold', 0.5)
    peak_ratio_thresh = step.get('peak_ratio_threshold', 0.7)
    # fundamental min and max
    min_val = float('inf')
    min_idx = -1
    max_val = -float('inf')
    for i, v in enumerate(I_fund):
        if v > max_val:
            max_val = v
        if v < min_val:
            min_val = v
            min_idx = i
    if max_val == 0:
        return 0.0
    wl_dip = wl[min_idx]
    score_a = 0.3 if (dip_range[0] <= wl_dip <= dip_range[1]) and (min_val / max_val < dip_ratio_thresh) else 0.0
    # two peaks
    left_has = False
    right_has = False
    for i, w in enumerate(wl):
        if w < wl_dip - 2.0 and I_fund[i] > peak_ratio_thresh * max_val:
            left_has = True
        elif w > wl_dip + 2.0 and I_fund[i] > peak_ratio_thresh * max_val:
            right_has = True
    score_b = 0.2 if (left_has and right_has) else 0.0
    # overtone deeper dips
    ratio_fund = min_val / max_val
    score_c = 0.0
    for v in [2,3,4,5]:
        if len(I_ov[v]) == 0:
            continue
        min_ov = min(I_ov[v])
        max_ov = max(I_ov[v])
        if max_ov == 0:
            continue
        if (min_ov / max_ov) < ratio_fund:
            score_c += 0.125
    return min(1.0, score_a + score_b + score_c)


_SCORERS = {
    'step_05': score_0,
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
