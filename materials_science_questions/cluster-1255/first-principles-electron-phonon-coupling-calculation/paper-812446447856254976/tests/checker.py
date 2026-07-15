import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='completeness') ===
def score_0(artifact, step, ctx):
    rows = artifact
    conds = step['required_conditions']
    expected = []
    for g in conds['gamma_at_delta0']:
        expected.append((round(g,10), 0.0))
    for scan in [conds['gamma0_delta_scan'], conds['gamma1_delta_scan']]:
        gamma = scan['gamma']
        d = scan['delta_range'][0]
        dmax = scan['delta_range'][1]
        while d <= dmax + 1e-9:
            expected.append((round(gamma,10), round(d,10)))
            d += scan['step']
    present = set()
    for row in rows:
        try:
            g = float(row['gamma'])
            d = float(row['delta'])
            present.add((round(g,10), round(d,10)))
        except:
            pass
    if not expected:
        return 1.0
    matched = sum(1 for e in expected if e in present)
    return matched / len(expected)


# === block: score_1 (check id='key_values') ===
def score_1(artifact, step, ctx):
    rows = artifact
    check_points = step.get('check_points', [])
    lookup = {}
    for row in rows:
        try:
            g = float(row['gamma'])
            d = float(row['delta'])
            tc = float(row['Tc'])
            alpha = float(row['alpha'])
            lookup[(round(g,10), round(d,10))] = (tc, alpha)
        except:
            continue
    scores = []
    for cp in check_points:
        key = (round(cp['gamma'],10), round(cp['delta'],10))
        if key not in lookup:
            scores.append(0.0)
            continue
        tc, alpha = lookup[key]
        tc_ok = abs(tc - cp['Tc']) <= cp['Tc_tolerance']
        alpha_ok = abs(alpha - cp['alpha']) <= cp['alpha_tolerance']
        scores.append((0.5 if tc_ok else 0.0) + (0.5 if alpha_ok else 0.0))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='trends') ===
def score_2(artifact, step, ctx):
    rows = artifact
    groups = defaultdict(list)
    for row in rows:
        try:
            g = float(row['gamma'])
            d = float(row['delta'])
            tc = float(row['Tc'])
            alpha = float(row['alpha'])
            groups[round(g,10)].append((d, tc, alpha))
        except:
            continue
    checks = step.get('trend_checks', {})
    total, passed = 0, 0

    if checks.get('gamma0_Tc_peak'):
        total += 1
        g0 = groups.get(0.0, [])
        if g0:
            tc_at_0 = next((tc for d, tc, _ in g0 if abs(d)<1e-9), None)
            if tc_at_0 is not None:
                max_tc = max(tc for _, tc, _ in g0)
                if tc_at_0 >= max_tc - 1e-9:
                    passed += 1

    if checks.get('gamma0_alpha_min'):
        total += 1
        g0 = groups.get(0.0, [])
        if g0:
            alpha_at_0 = next((a for d, _, a in g0 if abs(d)<1e-9), None)
            if alpha_at_0 is not None:
                min_alpha = min(a for _, _, a in g0)
                if alpha_at_0 <= min_alpha + 1e-9:
                    passed += 1

    if checks.get('gamma1_Tc_constant'):
        total += 1
        g1 = groups.get(1.0, [])
        if g1:
            tcs = [tc for _, tc, _ in g1]
            if tcs:
                avg = sum(tcs)/len(tcs)
                max_dev = max(abs(tc-avg) for tc in tcs)
                if max_dev <= 0.5:
                    passed += 1

    if checks.get('gamma1_alpha_constant'):
        total += 1
        g1 = groups.get(1.0, [])
        if g1:
            alphas = [a for _, _, a in g1]
            if alphas:
                avg_a = sum(alphas)/len(alphas)
                max_dev = max(abs(a-avg_a) for a in alphas)
                if max_dev <= 0.02:
                    passed += 1
    return passed / total if total > 0 else 0.0


_SCORERS = {
    'completeness': score_0,
    'key_values': score_1,
    'trends': score_2,
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
