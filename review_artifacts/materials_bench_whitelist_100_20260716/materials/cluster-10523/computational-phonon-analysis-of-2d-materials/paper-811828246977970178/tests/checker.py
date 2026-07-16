import os
import json
import csv

# === author imports / helpers ===
import math
import collections


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


# === block: score_0 (check id='fundamentals_existence') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    ribbons = ['7-AGNR', '15-AGNR', '4-ZGNR', '12-ZGNR']
    for r in ribbons:
        # all rows for this ribbon
        ribbon_rows = [row for row in rows if row['system'] == r]
        # fundamentals: k_perp == 0.0 and mode_label in expected set
        expected = {'LO','TO','ZO','LA','TA','ZA'}
        fund = [row for row in ribbon_rows
                if row['mode_label'] in expected and float(row['k_perp']) == 0.0]
        if len(fund) != 6:
            return 0.0
    return 1.0


# === block: score_1 (check id='lo_to_splitting') ===
def score_1(artifact, step, ctx):
    rows = artifact
    target = step['target_splittings']
    tol_abs = step['tolerance_abs']
    tol_rel = step['tolerance_rel']
    sc = 0.0
    for ribbon in ['7-AGNR', '15-AGNR']:
        ribbon_rows = [row for row in rows if row['system'] == ribbon]
        lo_freq = None
        to_freq = None
        for row in ribbon_rows:
            if row['mode_label'] == 'LO' and float(row['k_perp']) == 0.0:
                lo_freq = float(row['frequency'])
            if row['mode_label'] == 'TO' and float(row['k_perp']) == 0.0:
                to_freq = float(row['frequency'])
        if lo_freq is None or to_freq is None:
            continue
        splitting = abs(to_freq - lo_freq)
        gold = target[ribbon]
        allowed = max(tol_rel * gold, tol_abs)
        diff = abs(splitting - gold)
        if diff <= allowed:
            sc += 1.0
        else:
            sc += max(0.0, 1.0 - (diff - allowed) / allowed)
    return sc / 2.0


# === block: score_2 (check id='overtone_rmse') ===
def score_2(artifact, step, ctx):
    rows = artifact
    graphene_rows = [row for row in rows if row['system'] == 'graphene']
    # build graphene lookup: branch -> list of (k, freq) sorted by k
    graphene_map = collections.defaultdict(list)
    for row in graphene_rows:
        branch = row['mode_label']
        if branch in ['LO','TO','LA','TA','ZO','ZA']:
            k = float(row['k_perp'])
            f = float(row['frequency'])
            graphene_map[branch].append((k, f))
    for b in graphene_map:
        graphene_map[b].sort(key=lambda x: x[0])

    def interp_graphene(branch, k):
        pts = graphene_map[branch]
        if not pts:
            return None
        ks = [p[0] for p in pts]
        fs = [p[1] for p in pts]
        if k <= ks[0]:
            return fs[0]
        if k >= ks[-1]:
            return fs[-1]
        for i in range(len(ks)-1):
            if ks[i] <= k <= ks[i+1]:
                t = (k - ks[i]) / (ks[i+1] - ks[i])
                return fs[i] + t * (fs[i+1] - fs[i])
        return fs[-1]

    target = step['target_rmse']
    factor = step['factor']
    sc = 0.0
    for ribbon in ['7-AGNR', '15-AGNR']:
        ribbon_rows = [row for row in rows if row['system'] == ribbon]
        sq_errors = []
        for row in ribbon_rows:
            mode = row['mode_label']
            # overtone pattern: numeric prefix + hyphen + branch letter
            import re
            m = re.match(r'^(\d+)-(LO|TO|LA|TA|ZO|ZA)$', mode)
            if not m:
                continue
            order = int(m.group(1))
            branch = m.group(2)
            k = float(row['k_perp'])
            freq = float(row['frequency'])
            gf = interp_graphene(branch, k)
            if gf is not None:
                sq_errors.append((freq - gf) ** 2)
        if not sq_errors:
            continue
        rmse = math.sqrt(sum(sq_errors) / len(sq_errors))
        threshold = target[ribbon] * factor
        if rmse <= threshold:
            sc += 1.0
        else:
            # partial: degrade linearly beyond threshold up to 2*threshold
            sc += max(0.0, 1.0 - (rmse - threshold) / threshold)
    return sc / 2.0


# === block: score_3 (check id='ch_modes_check') ===
def score_3(artifact, step, ctx):
    rows = artifact
    ribbons = ['7-AGNR', '15-AGNR', '4-ZGNR', '12-ZGNR']
    expected = step['expected_freqs']
    tol_rel = step['tolerance_rel']
    sc = 0.0
    for ribbon in ribbons:
        ribbon_rows = [row for row in rows if row['system'] == ribbon]
        ch_rows = [row for row in ribbon_rows if row['mode_label'] == 'C-H']
        if len(ch_rows) < 6:
            continue
        all_ok = True
        for row in ch_rows:
            freq = float(row['frequency'])
            ok = False
            for ref in expected:
                if abs(freq - ref) <= ref * tol_rel:
                    ok = True
                    break
            if not ok:
                all_ok = False
                break
        if all_ok:
            sc += 1.0
    return sc / len(ribbons)


# === block: score_4 (check id='graphene_dispersion') ===
def score_4(artifact, step, ctx):
    rows = artifact
    graphene_rows = [row for row in rows if row['system'] == 'graphene']
    branches = set()
    max_k = -1.0
    for row in graphene_rows:
        b = row['mode_label']
        if b in ['LO','TO','LA','TA','ZO','ZA']:
            branches.add(b)
            k = float(row['k_perp'])
            if k > max_k:
                max_k = k
    if len(branches) < 6 or max_k < 2.5:
        return 0.0
    return 1.0


_SCORERS = {
    'fundamentals_existence': score_0,
    'lo_to_splitting': score_1,
    'overtone_rmse': score_2,
    'ch_modes_check': score_3,
    'graphene_dispersion': score_4,
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
