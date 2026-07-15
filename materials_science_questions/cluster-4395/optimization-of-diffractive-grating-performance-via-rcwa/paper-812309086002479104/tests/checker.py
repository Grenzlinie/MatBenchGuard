import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict


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
    for step in spec.get('steps', []):
        if step.get('id') == 'r_value_match':
            ctx = {'ref_values': step.get('reference_values', [])}
            break
    else:
        ctx = {'ref_values': []}
    return ctx


# === block: score_0 (check id='r_value_match') ===
def score_0(artifact, step, ctx):
    ref_values = ctx.get('ref_values', [])
    if not ref_values:
        return 0.0

    ref_by_key = {}
    for rv in ref_values:
        try:
            key = (int(rv['delta_mm']), float(rv['wavelength_mm']))
            ref_by_key[key] = float(rv['R'])
        except (KeyError, ValueError):
            continue

    computed_vals = []
    ref_vals = []
    for row in artifact:
        try:
            d = int(row['delta_mm'])
            w = float(row['wavelength_mm'])
            R_val = float(row['R'])
        except (KeyError, ValueError):
            continue
        ref_R = ref_by_key.get((d, w))
        if ref_R is not None:
            computed_vals.append(R_val)
            ref_vals.append(ref_R)

    n = len(computed_vals)
    if n < 2:
        return 0.0

    # Spearman rank correlation
    def _rankdata(arr):
        idx = sorted(range(n), key=lambda i: arr[i])
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j < n and arr[idx[j]] == arr[idx[i]]:
                j += 1
            rval = (i + j - 1) / 2.0 + 1.0
            for k in range(i, j):
                ranks[idx[k]] = rval
            i = j
        return ranks

    comp_ranks = _rankdata(computed_vals)
    ref_ranks = _rankdata(ref_vals)

    mean_c = sum(comp_ranks) / n
    mean_r = sum(ref_ranks) / n
    cov = sum((cr - mean_c) * (rr - mean_r) for cr, rr in zip(comp_ranks, ref_ranks))
    std_c = math.sqrt(sum((cr - mean_c) ** 2 for cr in comp_ranks))
    std_r = math.sqrt(sum((rr - mean_r) ** 2 for rr in ref_ranks))
    if std_c < 1e-15 or std_r < 1e-15:
        rho = 0.0
    else:
        rho = cov / (std_c * std_r)

    # Map rho from [0.5, 1.0] linearly to [0.0, 1.0]
    score = max(0.0, min(1.0, (rho - 0.5) / 0.5))
    return score


# === block: score_1 (check id='r_monotonicity') ===
def score_1(artifact, step, ctx):
    groups = defaultdict(list)
    for row in artifact:
        try:
            d = int(row['delta_mm'])
            w = float(row['wavelength_mm'])
            R_val = float(row['R'])
            groups[d].append((w, R_val))
        except (KeyError, ValueError):
            continue
    all_deltas_passed = 0
    total_deltas = len(groups)
    if total_deltas == 0:
        return 0.0
    for d, pairs in groups.items():
        pairs.sort(key=lambda x: x[0])
        Rs = [p[1] for p in pairs]
        # must be strictly decreasing (within small float noise)
        monotonic = all(Rs[i] > Rs[i+1] - 1e-12 for i in range(len(Rs)-1))
        if monotonic:
            all_deltas_passed += 1
    return all_deltas_passed / total_deltas


_SCORERS = {
    'r_value_match': score_0,
    'r_monotonicity': score_1,
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
