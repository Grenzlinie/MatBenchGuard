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
            params = spec.get("parameters", {})
            S = float(params.get("S", 0.0027))
            R = float(params.get("R", 1.035))
            theta_th = float(params.get("θ_th", 102.0))
            T_j = float(params.get("T_j", 353.0))
            theta_a = float(params.get("θ_a", 50.0))
            Q = float(params.get("Q", 0.5))

            def compute_theta_thv(I):
                Tc = T_j - theta_a * Q
                dT = theta_th * (S * I * Tc - 0.5 * I**2 * R - Q)
                P_tec = S * I * dT + I**2 * R
                if I == 0:
                    return None
                num = (P_tec / (I**2) - R) * theta_th
                denom = (P_tec / (I**2) - R) + (0.5 * S * I * R - S**2 * Tc) * theta_th
                return num / denom if denom != 0 else None

            currents = [round(i * 0.1, 2) for i in range(1, 16)]  # 0.1 .. 1.5
            gold_curve = {}
            for I in currents:
                tv = compute_theta_thv(I)
                gold_curve[I] = tv

            # find minimum
            min_I = min(gold_curve, key=lambda k: gold_curve[k])
            ctx = {
                "gold_curve": gold_curve,
                "expected_min_val": gold_curve[min_I],
                "expected_min_current": min_I
            }
            return ctx


# === block: score_0 (check id='step_compute_curve') ===
def score_0(artifact, step, ctx):
            rows = artifact  # list of dicts
            ctx_gold = ctx["gold_curve"]
            tol = 0.05
            expected_currents = set(ctx_gold.keys())
            agent_currents = set()
            try:
                for row in rows:
                    I = float(row["I_tec"])
                    agent_currents.add(round(I, 2))
            except Exception:
                return 0.0
            if agent_currents != expected_currents:
                return 0.0
            matched = 0
            total = 0
            for row in rows:
                I = round(float(row["I_tec"]), 2)
                tv = float(row["theta_thv"])
                gold_val = ctx_gold[I]
                total += 1
                if abs(tv - gold_val) <= tol:
                    matched += 1
            score = matched / total if total > 0 else 0.0
            return score


# === block: score_1 (check id='step_find_minimum') ===
def score_1(artifact, step, ctx):
            min_json = artifact
            exp_min_val = ctx["expected_min_val"]
            exp_min_cur = ctx["expected_min_current"]
            tol_val = 0.1
            tol_cur = 0.05
            if not isinstance(min_json, dict):
                return 0.0
            try:
                min_val = float(min_json.get("minimum_value", None))
                min_cur = float(min_json.get("current_at_minimum", None))
            except (TypeError, ValueError):
                return 0.0
            if abs(min_val - exp_min_val) <= tol_val and abs(min_cur - exp_min_cur) <= tol_cur:
                return 1.0
            return 0.0


_SCORERS = {
    'step_compute_curve': score_0,
    'step_find_minimum': score_1,
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
