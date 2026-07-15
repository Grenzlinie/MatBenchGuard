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
    return {}


# === block: score_0 (check id='model_params') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tolerance = step.get('tolerance_rel', 0.10)
    params = artifact
    score_sum = 0.0
    total = len(gold)
    for key, gval in gold.items():
        aval = params.get(key, None)
        if aval is None:
            continue
        try:
            aval = float(aval)
        except:
            continue
        if key == 'chi_squared':
            if aval <= gval:
                score_sum += 1.0
            else:
                rel_err = (aval - gval) / abs(gval)
                if rel_err <= tolerance:
                    score_sum += 1.0
                elif rel_err >= 2 * tolerance:
                    score_sum += 0.0
                else:
                    score_sum += 1.0 - (rel_err - tolerance) / tolerance
            continue
        if abs(gval) < 1e-12:
            if abs(aval) < 1e-9:
                score_sum += 1.0
            else:
                score_sum += 0.0
            continue
        rel_err = abs(aval - gval) / abs(gval)
        if rel_err <= tolerance:
            score_sum += 1.0
        else:
            if rel_err >= 2 * tolerance:
                score_sum += 0.0
            else:
                score_sum += 1.0 - (rel_err - tolerance) / tolerance
    return round(score_sum / total, 6)


# === block: score_1 (check id='elastic_constants') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tolerance = step.get('tolerance_rel', 0.10)
    params = artifact
    score_sum = 0.0
    total = len(gold)
    for key, gval in gold.items():
        aval = params.get(key, None)
        if aval is None:
            continue
        try:
            aval = float(aval)
        except:
            continue
        if abs(gval) < 1e-12:
            if abs(aval) < 1e-9:
                score_sum += 1.0
            else:
                score_sum += 0.0
            continue
        rel_err = abs(aval - gval) / abs(gval)
        if rel_err <= tolerance:
            score_sum += 1.0
        else:
            if rel_err >= 2 * tolerance:
                score_sum += 0.0
            else:
                score_sum += 1.0 - (rel_err - tolerance) / tolerance
    return round(score_sum / total, 6)


# === block: score_2 (check id='dos_histogram') ===
def score_2(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    bins = []
    for r in rows:
        try:
            lo = float(r['frequency_bin_lower'])
            up = float(r['frequency_bin_upper'])
            cnt = int(r['count'])
            bins.append((lo, up, cnt))
        except:
            return 0.0
    if len(bins) != 300:
        return 0.0
    # check bin structure
    score_a = 1.0
    for i, (lo, up, _) in enumerate(bins):
        expected_lo = round(i * 0.02, 6)
        expected_up = round((i + 1) * 0.02, 6)
        if abs(lo - expected_lo) > 1e-6 or abs(up - expected_up) > 1e-6:
            score_a = 0.0
            break
    # TO peak near 2.75
    max_cnt = max(cnt for _, _, cnt in bins)
    to_idx = None
    for idx, (lo, up, cnt) in enumerate(bins):
        if lo >= 2.70 and up <= 2.80:
            if cnt == max_cnt:
                to_idx = idx
                break
    score_b = 1.0 if to_idx is not None else 0.0
    # gap between 2.0 and 2.4
    max_cnt_gap = 0.0
    for lo, up, cnt in bins:
        if lo >= 2.0 and up <= 2.4:
            if cnt > max_cnt_gap:
                max_cnt_gap = cnt
    score_c = 1.0 if max_cnt_gap < 0.05 * max_cnt else 0.0
    return round(0.2 * score_a + 0.4 * score_b + 0.4 * score_c, 6)


_SCORERS = {
    'model_params': score_0,
    'elastic_constants': score_1,
    'dos_histogram': score_2,
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
