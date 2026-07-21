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
    def prepare(outputs_dir, spec):
        steps = spec.get("steps", spec.get("checks", []))
        ctx = {}
        for step in steps:
            if "gold" in step and "rows" in step["gold"]:
                ctx[step["id"]] = step["gold"]["rows"]
            ctx[step["id"] + "_tolerances"] = step.get("tolerances", {})
        return ctx


# === block: score_0 (check id='step4') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        rows = artifact
        gold_rows = ctx.get("step4", [])
        tols = ctx.get("step4_tolerances", {})
        rel_tol = float(tols.get("rel", 0.10))
        abs_tol = float(tols.get("abs", 0.001))
        expected_map = {}
        for r in gold_rows:
            try:
                expected_map[float(r["T_star"])] = r
            except (KeyError, TypeError, ValueError):
                continue
        def score_single(actual, expected, rel, ab):
            if expected is None:
                return 0.0
            try:
                actual = float(actual)
                expected = float(expected)
            except (TypeError, ValueError):
                return 0.0
            if expected == 0.0:
                return 1.0 if abs(actual) <= ab else 0.0
            err = abs(actual - expected)
            tol = max(rel * abs(expected), ab)
            if err <= tol:
                return 1.0
            elif err <= 5.0 * tol:
                return max(0.0, 1.0 - (err - tol) / (4.0 * tol))
            else:
                return 0.0
        total = 0.0
        cnt = 0
        for row in rows:
            try:
                T_star = float(row.get("T_star"))
            except (TypeError, ValueError):
                continue
            expected = expected_map.get(T_star)
            if expected is None:
                continue
            total += score_single(row.get("w1", 0), expected.get("w1", None), rel_tol, abs_tol)
            total += score_single(row.get("w2", 0), expected.get("w2", None), rel_tol, abs_tol)
            total += score_single(row.get("w3", 0), expected.get("w3", None), rel_tol, abs_tol)
            cnt += 3
        if cnt == 0:
            return 0.0
        return total / cnt


# === block: score_1 (check id='step5') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        gold_rows = ctx.get("step5", [])
        tols = ctx.get("step5_tolerances", {})
        rel_tol = float(tols.get("rel", 0.10))
        abs_tol = float(tols.get("abs", 0.001))
        expected_map = {}
        for r in gold_rows:
            expected_map[float(r["T_star"])] = r
        def score_single(actual, expected, rel, ab):
            if expected is None:
                return 0.0
            actual = float(actual)
            expected = float(expected)
            if expected == 0.0:
                return 1.0 if abs(actual) <= ab else 0.0
            err = abs(actual - expected)
            tol = max(rel * abs(expected), ab)
            if err <= tol:
                return 1.0
            elif err <= 5.0 * tol:
                return max(0.0, 1.0 - (err - tol) / (4.0 * tol))
            else:
                return 0.0
        total = 0.0
        cnt = 0
        for row in rows:
            T_star = float(row.get("T_star"))
            expected = expected_map.get(T_star)
            if expected is None:
                continue
            total += score_single(row.get("w1", 0), expected.get("w1", None), rel_tol, abs_tol)
            total += score_single(row.get("w2", 0), expected.get("w2", None), rel_tol, abs_tol)
            total += score_single(row.get("w3", 0), expected.get("w3", None), rel_tol, abs_tol)
            cnt += 3
        if cnt == 0:
            return 0.0
        return total / cnt


# === block: score_2 (check id='step6') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        gold_rows = ctx.get("step6", [])
        tols = ctx.get("step6_tolerances", {})
        rel_tol = float(tols.get("rel_w1", 0.10))
        abs_tol = float(tols.get("abs_w1", 0.001))
        beta_tol = float(tols.get("beta_tol", 0.02))
        expected_w1 = {}
        expected_beta = None
        for r in gold_rows:
            desc = r.get("description", "")
            if desc == "w1_at_Tc":
                expected_w1[int(r["L"])] = float(r["value"])
            elif desc == "beta_over_nu":
                expected_beta = float(r["value"])
        def score_single(actual, expected, rel, ab):
            if expected is None:
                return 0.0
            actual = float(actual)
            expected = float(expected)
            if expected == 0.0:
                return 1.0 if abs(actual) <= ab else 0.0
            err = abs(actual - expected)
            tol = max(rel * abs(expected), ab)
            if err <= tol:
                return 1.0
            elif err <= 5.0 * tol:
                return max(0.0, 1.0 - (err - tol) / (4.0 * tol))
            else:
                return 0.0
        total = 0.0
        cnt = 0
        for row in rows:
            desc = row.get("description", "")
            if desc == "w1_at_Tc":
                L = int(row.get("L", 0))
                exp = expected_w1.get(L)
                if exp is not None:
                    total += score_single(row.get("value", 0), exp, rel_tol, abs_tol)
                    cnt += 1
            elif desc == "beta_over_nu":
                exp = expected_beta
                if exp is not None:
                    actual = float(row.get("value", 0))
                    err = abs(actual - exp)
                    if err <= beta_tol:
                        total += 1.0
                    elif err <= 5.0 * beta_tol:
                        total += max(0.0, 1.0 - (err - beta_tol) / (4.0 * beta_tol))
                    else:
                        total += 0.0
                    cnt += 1
        if cnt == 0:
            return 0.0
        return total / cnt


_SCORERS = {
    'step4': score_0,
    'step5': score_1,
    'step6': score_2,
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
