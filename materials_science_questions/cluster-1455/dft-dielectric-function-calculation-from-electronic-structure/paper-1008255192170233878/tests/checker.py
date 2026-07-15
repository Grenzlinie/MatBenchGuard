import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import json
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
    return {"spec": spec}


# === block: score_0 (check id='hamaker') ===
def score_0(artifact, step, ctx):
    targets = step.get("targets", {})
    tol = step.get("tolerance_abs", 0.0001)
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0

    # build lookup by stoichiometry
    lookup = {}
    for r in rows:
        stoich = r.get("stoichiometry", "").strip()
        try:
            a_nr = float(r.get("A_NR_eV", None))
            a_m0 = float(r.get("A_m0_eV", None))
        except (TypeError, ValueError):
            continue
        lookup[stoich] = {"A_NR_eV": a_nr, "A_m0_eV": a_m0}

    matched = 0
    total_fields = 0
    for stoich, vals in targets.items():
        if stoich not in lookup:
            continue
        agent = lookup[stoich]
        if abs(agent["A_NR_eV"] - vals["A_NR_eV"]) <= tol:
            matched += 1
        if abs(agent["A_m0_eV"] - vals["A_m0_eV"]) <= tol:
            matched += 1
        total_fields += 2
    if total_fields == 0:
        return 0.0
    return matched / total_fields


# === block: score_1 (check id='free_energy') ===
def score_1(artifact, step, ctx):
    checks = step.get("sign_reversal_checks", {})
    if not artifact or not isinstance(artifact, list):
        return 0.0

    # group by stoichiometry
    groups = {}
    for row in artifact:
        stoich = row.get("stoichiometry", "").strip()
        try:
            d = float(row.get("distance_nm", None))
            f = float(row.get("F_retarded_eV", None))
        except (TypeError, ValueError):
            continue
        groups.setdefault(stoich, []).append((d, f))

    passed = 0
    total = 0
    for stoich, check in checks.items():
        pairs = groups.get(stoich, [])
        if not pairs:
            total += 1
            continue
        pairs.sort(key=lambda x: x[0])
        ds = [p[0] for p in pairs]
        fs = [p[1] for p in pairs]
        if check.get("all_negative", False):
            # all F values must be <= 0 (or strictly < 0, allow tiny positive noise?)
            # We'll check that all values are negative (<= -1e-20) to be safe.
            if all(v <= -1e-20 for v in fs):
                passed += 1
        else:
            exp_dist = check["expected_reversal_distance_nm"]
            tol = check.get("tolerance_nm", 0.5)
            neg_to_pos = check.get("negative_to_positive", True)
            # find first distance where sign flips from negative to positive
            sign_change_dist = None
            for i in range(1, len(fs)):
                if neg_to_pos and fs[i-1] <= -1e-20 and fs[i] >= 1e-20:
                    sign_change_dist = ds[i-1] + (ds[i] - ds[i-1]) * (0 - fs[i-1]) / (fs[i] - fs[i-1])
                    break
                elif (not neg_to_pos) and fs[i-1] >= 1e-20 and fs[i] <= -1e-20:
                    sign_change_dist = ds[i-1] + (ds[i] - ds[i-1]) * (0 - fs[i-1]) / (fs[i] - fs[i-1])
                    break
            if sign_change_dist is not None and abs(sign_change_dist - exp_dist) <= tol:
                passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'hamaker': score_0,
    'free_energy': score_1,
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
