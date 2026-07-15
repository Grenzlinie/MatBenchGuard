import os
import json
import csv

# === author imports / helpers ===
import csv, os, re, math


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


# === block: score_0 (check id='02_efficiency_grid') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact
    if not isinstance(artifact_rows, list):
        return 0.0
    gold_rows = step["config"]["gold_rows"]
    tol_pct = step["config"]["tolerance_pct"] / 100.0
    tol_abs = step["config"]["tolerance_abs"]

    # build gold lookup
    gold_lookup = {}
    for gr in gold_rows:
        try:
            key = (float(gr["T_ph"]), float(gr["kappa_sigma"]))
            gold_lookup[key] = float(gr["eta_max"])
        except:
            continue

    # parse agent rows
    agent_points = {}
    for row in artifact_rows:
        try:
            t = float(row.get("T_ph", 0))
            k = float(row.get("kappa_sigma", 0))
            eta = float(row.get("eta_max", 0))
            agent_points[(t, k)] = eta
        except:
            continue

    # compute value score per gold point
    scores = []
    for gkey, gval in gold_lookup.items():
        if gkey in agent_points:
            aval = agent_points[gkey]
            diff = abs(aval - gval)
            limit = max(tol_pct * gval, tol_abs)
            if diff <= limit:
                scores.append(1.0)
            elif diff <= 2 * limit:
                scores.append(0.5)
            else:
                scores.append(0.0)
        else:
            scores.append(0.0)

    value_score = sum(scores) / len(scores) if scores else 0.0

    # structural checks
    str_score = 0.0
    try:
        # monotonic decrease per T_ph
        monos = []
        for T in [350, 400, 450]:
            ks_points = [(k, eta) for (t, k), eta in agent_points.items() if t == T]
            ks_sorted = sorted(ks_points, key=lambda x: x[0])
            etas = [eta for _, eta in ks_sorted]
            if len(etas) >= 2 and all(etas[i] >= etas[i+1] for i in range(len(etas)-1)):
                monos.append(1.0)
            else:
                monos.append(0.0)
        # slope positive at kappa=0: eta(450,0) > eta(350,0)
        eta_350_0 = agent_points.get((350, 0), None)
        eta_450_0 = agent_points.get((450, 0), None)
        slope_pos = 1.0 if eta_350_0 is not None and eta_450_0 is not None and eta_450_0 > eta_350_0 else 0.0
        # slope negative at kappa=0.00316227766: eta(450,k) < eta(350,k)
        k_big = 0.00316227766
        eta_350_k = agent_points.get((350, k_big), None)
        eta_450_k = agent_points.get((450, k_big), None)
        slope_neg = 1.0 if eta_350_k is not None and eta_450_k is not None and eta_450_k < eta_350_k else 0.0
        str_score = (sum(monos)/len(monos) + slope_pos + slope_neg) / 3.0
    except:
        str_score = 0.0

    return 0.85 * value_score + 0.15 * str_score


# === block: score_1 (check id='03_analytic_bound') ===
def score_1(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 2:
        return 0.0
    line1 = lines[0].strip()
    line2 = lines[1].strip()
    expected_line1 = step["config"]["expected_line1"]
    expected_num = step["config"]["expected_numerical_bound"]
    tol = step["config"]["numeric_tolerance"]

    score1 = 1.0 if line1 == expected_line1 else 0.0
    try:
        num = float(line2)
        score2 = 1.0 if abs(num - expected_num) <= tol else 0.0
    except:
        score2 = 0.0
    return 0.5 * score1 + 0.5 * score2


# === block: score_2 (check id='04_candidate_check') ===
def score_2(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    expected = step["config"]["expected_lines"]
    if len(lines) != len(expected):
        return 0.0
    matches = 0
    for i, exp in enumerate(expected):
        if lines[i].strip() == exp:
            matches += 1
    return matches / len(expected) if expected else 0.0


_SCORERS = {
    '02_efficiency_grid': score_0,
    '03_analytic_bound': score_1,
    '04_candidate_check': score_2,
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
