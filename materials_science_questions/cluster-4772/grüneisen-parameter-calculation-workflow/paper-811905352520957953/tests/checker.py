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
    import json, csv, os
    ctx = {"paths": {}}
    out_dir = outputs_dir
    for f in ["fitted_potential_params.json", "soecs_and_aggregates.csv", "toecs.csv", "pressure_derivatives.csv", "mode_gruneisen_params.csv", "gamma_L_and_delta.json"]:
        path = os.path.join(out_dir, f)
        if not os.path.exists(path):
            ctx["paths"][f] = None
            continue
        if f.endswith(".json"):
            with open(path) as fp:
                ctx["paths"][f] = json.load(fp)
        else:
            with open(path, newline="") as fp:
                ctx["paths"][f] = list(csv.DictReader(fp))
    return ctx


# === block: score_0 (check id='step1_fit_params') ===
def score_0(artifact, step, ctx):
    params = artifact
    if not isinstance(params, dict):
        return 0.0
    gold = step["gold"]
    tols = step["tolerance_abs"]
    total = len(gold)
    if total == 0:
        return 0.0
    score_sum = 0.0
    for key, exp in gold.items():
        got = params.get(key)
        if got is None:
            continue
        tol = tols.get(key)
        if tol is None or tol <= 0:
            continue
        diff = abs(got - exp)
        if diff >= tol:
            continue
        score_sum += 1.0 - diff / tol
    return score_sum / total


# === block: score_1 (check id='step2_soecs') ===
def score_1(artifact, step, ctx):
    gold = step["gold"]
    tols = step["tolerance_abs"]
    if not isinstance(artifact, list): return 0.0
    row_by_prop = {row["property"]: row for row in artifact}
    total = len(gold)
    passed = 0
    for prop, exp in gold.items():
        row = row_by_prop.get(prop)
        if row is None: continue
        try:
            val = float(row["value_GPa_or_dimensionless"])
        except (ValueError, KeyError):
            continue
        if abs(val - exp) <= tols[prop]:
            passed += 1
    return passed / total


# === block: score_2 (check id='step3_toecs') ===
def score_2(artifact, step, ctx):
    gold = step["gold"]
    tols = step["tolerance_abs"]
    if not isinstance(artifact, list): return 0.0
    row_by_const = {row["constant"]: row for row in artifact}
    total = len(gold)
    passed = 0
    for cst, exp in gold.items():
        row = row_by_const.get(cst)
        if row is None: continue
        try:
            val = float(row["value_TPa"])
        except (ValueError, KeyError):
            continue
        if abs(val - exp) <= tols[cst]:
            passed += 1
    return passed / total


# === block: score_3 (check id='step4_pressure_deriv') ===
def score_3(artifact, step, ctx):
    # recompute pressure derivatives from soecs and toecs
    soecs_file = ctx["paths"].get("soecs_and_aggregates.csv")
    toecs_file = ctx["paths"].get("toecs.csv")
    if not soecs_file or not isinstance(soecs_file, list): return 0.0
    if not toecs_file or not isinstance(toecs_file, list): return 0.0
    # extract SOECs
    soec = {}
    for row in soecs_file:
        try:
            soec[row["property"]] = float(row["value_GPa_or_dimensionless"])
        except:
            continue
    if not all(k in soec for k in ["C11","C12","C44"]): return 0.0
    # extract TOECs in TPa, convert to GPa as needed? The paper's formulas use TPa units and yield dimensionless derivatives.
    toec = {}
    for row in toecs_file:
        try:
            toec[row["constant"]] = float(row["value_TPa"])
        except:
            continue
    if not all(k in toec for k in ["C111","C112","C123","C144","C155"]): return 0.0
    C11 = soec["C11"]
    C12 = soec["C12"]
    C44 = soec["C44"]
    C111 = toec["C111"]
    C112 = toec["C112"]
    C123 = toec["C123"]
    C144 = toec["C144"]
    C155 = toec["C155"]
    denom = C11 + 2*C12
    if denom == 0: return 0.0
    # formula (14a-c)
    dC11dp = -(C111 + 2*C112 + 2*C11 + 2*C12) / denom
    dC12dp = -(C123 + 2*C112 - C11 - C12) / denom
    dC44dp = -(C144 + 2*C155 + C11 + 2*C12 + C44) / denom
    expected = {"dC11_dp": dC11dp, "dC12_dp": dC12dp, "dC44_dp": dC44dp}
    # compare to agent's submitted derivatives
    if not isinstance(artifact, list): return 0.0
    agent = {}
    for row in artifact:
        try:
            agent[row["derivative"]] = float(row["value"])
        except:
            continue
    if not all(k in agent for k in ["dC11_dp","dC12_dp","dC44_dp"]): return 0.0
    # tolerance
    TOL = 0.1
    passed = 0
    for key in ["dC11_dp","dC12_dp","dC44_dp"]:
        if abs(agent[key] - expected[key]) <= TOL:
            passed += 1
    return passed / 3.0


# === block: score_4 (check id='step5_mode_gruneisen') ===
def score_4(artifact, step, ctx):
    anchor_points = step["anchor_points"]
    tol = step["tolerance_abs"]
    if not isinstance(artifact, list): return 0.0
    # index rows by (direction, angle_deg, mode)
    index = {}
    for row in artifact:
        try:
            d = row["direction"]
            a = float(row["angle_deg"])
            m = row["mode"]
            g = float(row["gamma"])
            key = (d, a, m)
            # keep first occurrence; might be multiple matches per direction (like (010) 0 qT2)
            index[key] = g
        except:
            continue
    total = len(anchor_points)
    passed = 0
    for pt in anchor_points:
        key = (pt["direction"], float(pt["angle_deg"]), pt["mode"])
        got = index.get(key)
        if got is None: continue
        if abs(got - pt["gamma"]) <= tol:
            passed += 1
    return passed / total if total > 0 else 0.0


# === block: score_5 (check id='step6_gamma_l_delta') ===
def score_5(artifact, step, ctx):
    if not isinstance(artifact, dict): return 0.0
    gold = step["gold"]
    tols = step["tolerance_abs"]
    # recompute delta from SOECs/TOECs
    soecs_file = ctx["paths"].get("soecs_and_aggregates.csv")
    toecs_file = ctx["paths"].get("toecs.csv")
    if not soecs_file or not isinstance(soecs_file, list): return 0.0
    if not toecs_file or not isinstance(toecs_file, list): return 0.0
    soec = {}
    for row in soecs_file:
        try:
            soec[row["property"]] = float(row["value_GPa_or_dimensionless"])
        except: continue
    toec = {}
    for row in toecs_file:
        try:
            toec[row["constant"]] = float(row["value_TPa"])
        except: continue
    # compute delta using (20)
    if all(k in soec for k in ["C11","C12"]) and all(k in toec for k in ["C111","C112","C123"]):
        C11 = soec["C11"]
        C12 = soec["C12"]
        C111 = toec["C111"]
        C112 = toec["C112"]
        C123 = toec["C123"]
        denom = 3*C11 + 2*C12
        if denom != 0:
            delta_recomp = -1.0 - (C111 + 6*C112 + 2*C123) / denom
        else:
            delta_recomp = None
    else:
        delta_recomp = None
    # score gamma_L: reference match
    gamma_L_ok = 0.0
    if "gamma_L" in artifact:
        if abs(artifact["gamma_L"] - gold["gamma_L"]) <= tols["gamma_L"]:
            gamma_L_ok = 1.0
    # score delta: if we could recompute, cross-check; else rely on reference match
    delta_ok = 0.0
    if delta_recomp is not None:
        if abs(artifact.get("delta", 9999) - delta_recomp) <= tols["delta"]:
            delta_ok = 1.0
    else:
        if abs(artifact.get("delta", 9999) - gold["delta"]) <= tols["delta"]:
            delta_ok = 1.0
    return 0.5 * gamma_L_ok + 0.5 * delta_ok


_SCORERS = {
    'step1_fit_params': score_0,
    'step2_soecs': score_1,
    'step3_toecs': score_2,
    'step4_pressure_deriv': score_3,
    'step5_mode_gruneisen': score_4,
    'step6_gamma_l_delta': score_5,
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
