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
    def prepare(outputs_dir, spec):
        stiffness_gold = None
        stiffness_tol = 10.0
        harvester_targets = {}
        harvester_tol = 15.0
        for step in spec.get("steps", []):
            cfg = step.get("config", {})
            if step["id"] == "stiffness_check":
                stiffness_gold = cfg.get("gold_rows")
                stiffness_tol = cfg.get("tolerance", 10.0)
            elif step["id"] == "harvester_relative_increase":
                harvester_targets = cfg.get("target_increases", {})
                harvester_tol = cfg.get("tolerance_pct", 15.0)
        return {
            "stiffness_gold": stiffness_gold,
            "stiffness_tol": stiffness_tol,
            "harvester_targets": harvester_targets,
            "harvester_tol": harvester_tol
        }


# === block: score_0 (check id='stiffness_check') ===
def score_0(artifact, step, ctx):
        coeff_cols = ["C11","C12","C13","C33","C44","C66"]
        gold_rows = ctx["stiffness_gold"]
        tolerance = ctx["stiffness_tol"]
        if not gold_rows or not artifact:
            return 0.0
        agent_map = {}
        for row in artifact:
            try:
                p = int(row["porosity"])
                m = {col: float(row[col]) for col in coeff_cols}
                agent_map[p] = m
            except:
                continue
        sorted_por = sorted(agent_map.keys())
        mono_ok = 0
        mono_total = 0
        for col in coeff_cols:
            prev = None
            for p in sorted_por:
                val = agent_map[p].get(col)
                if val is None: continue
                if prev is not None:
                    mono_total += 1
                    if val <= prev:
                        mono_ok += 1
                prev = val
        mono_score = mono_ok / mono_total if mono_total > 0 else 0.0
        value_ok = 0
        value_total = 0
        for g in gold_rows:
            p = g["porosity"]
            if p not in agent_map: continue
            for col in coeff_cols:
                gold_val = g[col]
                agent_val = agent_map[p].get(col)
                if agent_val is None: continue
                value_total += 1
                if abs(agent_val - gold_val) <= tolerance:
                    value_ok += 1
        if value_total == 0:
            value_score = 0.0
        else:
            value_score = value_ok / value_total
        return 0.3 * mono_score + 0.7 * value_score


# === block: score_1 (check id='harvester_relative_increase') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        targets = ctx["harvester_targets"]
        tol = ctx["harvester_tol"]
        if not artifact:
            return 0.0
        mode_data = {"d31": {}, "d33": {}}
        for row in artifact:
            try:
                m = row["mode"]
                p = int(row["porosity"])
                V = float(row["max_voltage"])
                P = float(row["max_power"])
                mode_data[m][p] = (V, P)
            except:
                continue
        def rel_inc(v0, vT):
            if v0 == 0: return None
            return (vT - v0) / v0 * 100.0
        scores = []
        if "d31" in mode_data and 0 in mode_data["d31"] and 10 in mode_data["d31"]:
            V0, _ = mode_data["d31"][0]
            V10, _ = mode_data["d31"][10]
            inc = rel_inc(V0, V10)
            if inc is not None:
                s = max(0.0, 1.0 - abs(inc - targets["d31_voltage"]) / tol)
                scores.append(s)
            else:
                scores.append(0.0)
        else:
            scores.append(0.0)
        if "d33" in mode_data and 0 in mode_data["d33"] and 10 in mode_data["d33"]:
            V0, _ = mode_data["d33"][0]
            V10, _ = mode_data["d33"][10]
            inc = rel_inc(V0, V10)
            if inc is not None:
                s = max(0.0, 1.0 - abs(inc - targets["d33_voltage"]) / tol)
                scores.append(s)
            else:
                scores.append(0.0)
        else:
            scores.append(0.0)
        if "d31" in mode_data and 0 in mode_data["d31"] and 5 in mode_data["d31"]:
            _, P0 = mode_data["d31"][0]
            _, P5 = mode_data["d31"][5]
            inc = rel_inc(P0, P5)
            if inc is not None:
                s = max(0.0, 1.0 - abs(inc - targets["d31_power"]) / tol)
                scores.append(s)
            else:
                scores.append(0.0)
        else:
            scores.append(0.0)
        if "d33" in mode_data and 0 in mode_data["d33"] and 5 in mode_data["d33"]:
            _, P0 = mode_data["d33"][0]
            _, P5 = mode_data["d33"][5]
            inc = rel_inc(P0, P5)
            if inc is not None:
                s = max(0.0, 1.0 - abs(inc - targets["d33_power"]) / tol)
                scores.append(s)
            else:
                scores.append(0.0)
        else:
            scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='harvester_peak_porosity') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        mode_data = {"d31": {}, "d33": {}}
        for row in artifact:
            try:
                m = row["mode"]
                p = int(row["porosity"])
                V = float(row["max_voltage"])
                P = float(row["max_power"])
                mode_data[m][p] = (V, P)
            except:
                continue
        conds = 8
        passed = 0
        if "d31" in mode_data and 5 in mode_data["d31"] and 10 in mode_data["d31"] and 15 in mode_data["d31"]:
            V5 = mode_data["d31"][5][0]
            V10 = mode_data["d31"][10][0]
            V15 = mode_data["d31"][15][0]
            if V10 > V5: passed += 1
            if V10 > V15: passed += 1
        if "d33" in mode_data and 5 in mode_data["d33"] and 10 in mode_data["d33"] and 15 in mode_data["d33"]:
            V5 = mode_data["d33"][5][0]
            V10 = mode_data["d33"][10][0]
            V15 = mode_data["d33"][15][0]
            if V10 > V5: passed += 1
            if V10 > V15: passed += 1
        if "d31" in mode_data and 0 in mode_data["d31"] and 5 in mode_data["d31"] and 10 in mode_data["d31"]:
            P0 = mode_data["d31"][0][1]
            P5 = mode_data["d31"][5][1]
            P10 = mode_data["d31"][10][1]
            if P5 > P0: passed += 1
            if P5 > P10: passed += 1
        if "d33" in mode_data and 0 in mode_data["d33"] and 5 in mode_data["d33"] and 10 in mode_data["d33"]:
            P0 = mode_data["d33"][0][1]
            P5 = mode_data["d33"][5][1]
            P10 = mode_data["d33"][10][1]
            if P5 > P0: passed += 1
            if P5 > P10: passed += 1
        return passed / conds if conds > 0 else 0.0


_SCORERS = {
    'stiffness_check': score_0,
    'harvester_relative_increase': score_1,
    'harvester_peak_porosity': score_2,
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
