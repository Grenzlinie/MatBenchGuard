import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
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
    def prepare(output_dir, spec):
        steps = spec.get("steps", [])
        ctx = {}
        for step in steps:
            if step.get("output_file") == "step_01_formation_enthalpies.csv":
                ctx["formation_gold_rows"] = step.get("gold_rows", [])
                ctx["enthalpy_tol"] = step.get("tolerance_abs_eV", 0.15)
            if step.get("output_file") == "step_02_defect_level_pressure_coefficients.json":
                ctx["coeff_gold"] = step.get("gold_coefficients", {})
                ctx["coeff_tol"] = step.get("tolerance_abs_meV_GPa", 0.5)
        return ctx


# === block: score_0 (check id='formation_enthalpies') ===
def score_0(artifact, step, ctx):
    # defensive check: artifact must be a list/tuple
    if not isinstance(artifact, (list, tuple)):
        return 0.0

    gold_rows = ctx.get("formation_gold_rows", [])
    tol = ctx.get("enthalpy_tol", 0.15)

    # build gold map
    gold_map = {}
    for r in gold_rows:
        try:
            key = (float(r["pressure_GPa"]), r["defect"], int(r["charge"]))
            gold_map[key] = float(r["H_f_eV_gold"])
        except (ValueError, KeyError, TypeError):
            pass

    total = len(gold_map)
    if total == 0:
        return 0.0

    agent_map = {}
    matched = 0

    for row in artifact:
        if not isinstance(row, dict):
            continue
        try:
            p_raw = row.get("pressure_GPa")
            d_raw = row.get("defect")
            c_raw = row.get("charge")
            v_raw = row.get("H_f_eV")
            # skip if any required field is missing (None)
            if p_raw is None or d_raw is None or c_raw is None or v_raw is None:
                continue
            p = float(p_raw)
            d = str(d_raw).strip()
            c = int(float(c_raw))       # handle float-like charge e.g. "0.0"
            val = float(v_raw)
            key = (p, d, c)
            if key in gold_map and abs(val - gold_map[key]) <= tol:
                matched += 1
            agent_map[key] = val
        except (ValueError, KeyError, TypeError, AttributeError):
            continue

    accuracy = matched / total if total > 0 else 0.0

    # monotonicity checks
    monotonic_score = 1.0
    groups = defaultdict(list)
    for key, val in agent_map.items():
        p, d, c = key
        groups[(d, c)].append((p, val))

    n_groups = 0
    for (d, c), points in groups.items():
        if len(points) < 2:
            continue
        n_groups += 1
        points.sort(key=lambda x: x[0])
        vals = [v for _, v in points]
        if d == "C_B":
            # C_B formation enthalpies should be non-increasing with pressure
            for i in range(len(vals)-1):
                if vals[i+1] > vals[i]:
                    monotonic_score -= 0.1 / max(1, n_groups) / max(1, len(vals)-1)
        elif d == "C_N":
            # C_N formation enthalpies should be non-decreasing with pressure
            for i in range(len(vals)-1):
                if vals[i+1] < vals[i]:
                    monotonic_score -= 0.1 / max(1, n_groups) / max(1, len(vals)-1)

    monotonic_score = max(0.0, min(1.0, monotonic_score))
    return 0.7 * accuracy + 0.3 * monotonic_score


# === block: score_1 (check id='defect_level_pressure_coefficients') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx.get("coeff_gold", {})
        tol = ctx.get("coeff_tol", 0.5)
        required_keys = ["C_B^+1", "C_B^0", "C_B^-1", "C_N^+1", "C_N^0", "C_N^-1"]
        if not isinstance(artifact, dict):
            return 0.0
        passed = 0
        for key in required_keys:
            obj = artifact.get(key)
            if not isinstance(obj, dict):
                continue
            coeff = obj.get("pressure_coefficient_meV_GPa")
            if coeff is None:
                continue
            try:
                coeff = float(coeff)
            except (TypeError, ValueError):
                continue
            gold_val = gold.get(key)
            if gold_val is None:
                continue
            # tolerance check
            if abs(coeff - gold_val) <= tol:
                # sign checks
                sign_ok = True
                if key == "C_B^+1" and coeff <= 0:
                    sign_ok = False
                if key == "C_N^-1" and coeff >= 0:
                    sign_ok = False
                # others should have |coeff| <= 0.5 already covered by tolerance, but verify
                if sign_ok:
                    passed += 1
        return passed / len(required_keys) if required_keys else 1.0


_SCORERS = {
    'formation_enthalpies': score_0,
    'defect_level_pressure_coefficients': score_1,
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
