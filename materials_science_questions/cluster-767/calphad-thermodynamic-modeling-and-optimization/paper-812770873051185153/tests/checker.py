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


# === block: score_0 (check id='assessed_parameters_score') ===
def score_0(artifact, step, ctx):
        import math
        tests = step.get("parameter_tests", {})
        if not isinstance(artifact, dict) or not tests:
            return 0.0
        safe_ns = {"__builtins__": {}, "T": None, "ln": math.log, "exp": math.exp, "sqrt": math.sqrt, "pi": math.pi, "e": math.e}
        tol_rel = step.get("tolerance_relative", 0.05)
        total = 0.0
        count = 0
        for param_key, test_list in tests.items():
            agent_expr = artifact.get(param_key)
            if not isinstance(agent_expr, str):
                continue
            for test in test_list:
                T = test.get("T")
                gold_expr = test.get("expression")
                if T is None or gold_expr is None:
                    continue
                safe_ns["T"] = T
                try:
                    agent_val = eval(agent_expr, safe_ns, {})
                    gold_val = eval(gold_expr, safe_ns, {})
                except Exception:
                    continue
                if not isinstance(agent_val, (int, float)) or not isinstance(gold_val, (int, float)):
                    continue
                if abs(gold_val) < 1e-12:
                    continue
                agent_val = float(agent_val)
                gold_val = float(gold_val)
                rel_err = abs(agent_val - gold_val) / abs(gold_val)
                sc = max(0.0, 1.0 - rel_err / tol_rel)
                total += sc
                count += 1
        if count == 0:
            return 0.0
        return total / count


# === block: score_1 (check id='isothermal_700_score') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import math
        holdout = step.get("holdout_points", [])
        if not holdout or not isinstance(artifact, list) or not artifact:
            return 0.0
        points_by_phase = collections.defaultdict(list)
        for row in artifact:
            if not all(k in row for k in ("phase1","phase2","composition_U_at_frac","composition_Nb_at_frac","T_C")):
                continue
            try:
                u = float(row["composition_U_at_frac"])
                nb = float(row["composition_Nb_at_frac"])
                zr = 1.0 - u - nb
                if u < 0 or nb < 0 or zr < 0 or u > 1 or nb > 1:
                    continue
            except (ValueError, TypeError):
                continue
            key = (row["phase1"].strip().lower(), row["phase2"].strip().lower())
            points_by_phase[key].append((u, nb, zr))
        tol = step.get("distance_tolerance", 0.03)
        total = 0.0
        n = 0
        for hp in holdout:
            try:
                h_u = float(hp["composition_U_at_frac"])
                h_nb = float(hp["composition_Nb_at_frac"])
            except (ValueError, TypeError):
                continue
            h_zr = 1.0 - h_u - h_nb
            if h_zr < 0:
                continue
            key = (hp.get("phase1","").strip().lower(), hp.get("phase2","").strip().lower())
            candidate = points_by_phase.get(key, [])
            if not candidate:
                continue
            min_dist = min(math.sqrt((h_u - u)**2 + (h_nb - nb)**2 + (h_zr - zr)**2) for u, nb, zr in candidate)
            sc = max(0.0, 1.0 - min_dist / tol)
            total += sc
            n += 1
        if n == 0:
            return 0.0
        return total / n


_SCORERS = {
    'assessed_parameters_score': score_0,
    'isothermal_700_score': score_1,
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
