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
    return {}


# === block: score_0 (check id='rates_check') ===
def score_0(artifact, step, ctx):
    import csv

    rows = list(csv.DictReader(open('/app/outputs/rates_R095.csv')))
    header = rows[0].keys()
    expected_cols = ["T(K)", "R_H", "R_H2", "R_CH4", "R_C2H2", "R_C2H", "R_H2O", "R_CO2", "R_CO", "R_Cs"]
    if not all(c in header for c in expected_cols):
        return 0.0

    # Build lookup keyed by integer temperature
    data = {}
    for row in rows:
        try:
            t = int(float(row["T(K)"]))
            data[t] = row
        except:
            pass

    gold_temps = step["params"]["gold_temperatures"]
    gold_rates = step["params"]["gold_rates"]
    tolerances = step["params"]["tolerances"]

    numeric_passes = 0
    total_checks = 0
    for t in gold_temps:
        t_str = str(t)
        gold = gold_rates.get(t_str)
        if gold is None:
            continue
        agent_row = data.get(t)
        if agent_row is None:
            continue
        for sp in ["R_H", "R_H2", "R_CH4", "R_C2H2", "R_C2H", "R_H2O", "R_CO2", "R_CO", "R_Cs"]:
            try:
                agent_val = float(agent_row[sp])
                gold_val = float(gold[sp])
            except:
                continue
            if gold_val == 0.0:
                # For zero gold (R_Cs at 3500K), allow small absolute value
                if abs(agent_val) <= 1e4:
                    numeric_passes += 1
                total_checks += 1
                continue
            rel_err = abs(agent_val - gold_val) / abs(gold_val)
            if rel_err <= tolerances.get(sp, 0.3):
                numeric_passes += 1
            total_checks += 1

    numeric_score = numeric_passes / max(total_checks, 1)

    # Trend checks
    trend_checks = step["params"]["trend_checks"]
    trend_passes = 0
    for tc in trend_checks:
        cond = tc["condition"]  # e.g. "T>=900"
        assert_sp = tc["assert"]  # e.g. "R_CO > R_H2O"
        try:
            sp1, op, sp2 = assert_sp.split()
            # evaluate for all rows meeting condition
            ok = True
            for row in rows:
                try:
                    t = float(row["T(K)"])
                    # eval condition (simple)
                    if not eval(cond.replace("T", str(t))):
                        continue
                    v1 = float(row[sp1])
                    v2 = float(row[sp2])
                    if op == ">" and not (v1 > v2):
                        ok = False
                        break
                    elif op == "<" and not (v1 < v2):
                        ok = False
                        break
                except:
                    pass
            if ok:
                trend_passes += 1
        except:
            pass

    trend_score = trend_passes / max(len(trend_checks), 1)

    numeric_weight = step["params"]["numeric_weight"]
    trend_weight = step["params"]["trend_weight"]
    return numeric_weight * numeric_score + trend_weight * trend_score


# === block: score_1 (check id='phase_boundary_check') ===
def score_1(artifact, step, ctx):
    import csv

    rows = list(csv.DictReader(open('/app/outputs/deposition_phase_boundary.csv')))
    header = rows[0].keys()
    if "O/C_ratio" not in header or "T_boundary(K)" not in header:
        return 0.0

    # Parse rows
    points = []
    for row in rows:
        try:
            oc = float(row["O/C_ratio"])
            Tb = float(row["T_boundary(K)"])
            points.append((oc, Tb))
        except:
            pass
    if len(points) < 2:
        return 0.0

    # Sort by O/C ratio
    points.sort(key=lambda x: x[0])

    # Monotonic check: T_boundary should decrease as O/C increases
    monotonic = True
    for i in range(1, len(points)):
        if points[i][1] > points[i-1][1] + 10.0:  # allow 10 K upward
            monotonic = False
            break

    # Check gold points
    gold_points = step["params"]["gold_points"]
    gold_point_weight = step["params"]["gold_point_weight"]
    monotonic_weight = step["params"]["monotonic_weight"]

    point_score = 0.0
    if gold_points:
        pass_count = 0
        for gp in gold_points:
            target_oc = gp["oc"]
            target_T = gp["T"]
            tol = gp["tol"]
            # find closest oc
            best_diff = None
            best_T = None
            for oc, Tb in points:
                d = abs(oc - target_oc)
                if best_diff is None or d < best_diff:
                    best_diff = d
                    best_T = Tb
            if best_T is not None and abs(best_T - target_T) <= tol:
                pass_count += 1
        point_score = pass_count / len(gold_points)

    monotonic_score = 1.0 if monotonic else 0.0

    return monotonic_weight * monotonic_score + gold_point_weight * point_score


_SCORERS = {
    'rates_check': score_0,
    'phase_boundary_check': score_1,
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
