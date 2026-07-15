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
    step_01 = load_artifact(os.path.join(outputs_dir, "step_01_probability_amplitudes.json"))
    step_02 = load_artifact(os.path.join(outputs_dir, "step_02_entanglement_entropy.json"))
    step_03 = load_artifact(os.path.join(outputs_dir, "step_03_U_over_t.json"))
    step_04 = load_artifact(os.path.join(outputs_dir, "step_04_full_curves.json"))
    return {"step_01": step_01, "step_02": step_02, "step_03": step_03, "step_04": step_04}


# === block: score_0 (check id='score_amplitudes') ===
def score_0(artifact, step, ctx):
    amp = ctx["step_01"]
    if amp is None:
        return 0.0
    ee = amp.get("amplitude_ee_squared", {})
    oo = amp.get("amplitude_oo_squared", {})
    separations = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0]
    total = 0
    passed = 0
    for sep in separations:
        key = str(sep)
        for orient in ["100", "110"]:
            e = ee.get(key, {}).get(orient)
            o = oo.get(key, {}).get(orient)
            if e is None or o is None:
                continue
            total += 1
            if abs(e + o - 1.0) < 1e-6 and 0 <= e <= 1 and 0 <= o <= 1:
                passed += 1
    return passed / total if total > 0 else 0.0


# === block: score_1 (check id='score_entropy') ===
def score_1(artifact, step, ctx):
    amp = ctx["step_01"]
    ent = ctx["step_02"]
    if amp is None or ent is None:
        return 0.0
    ee = amp.get("amplitude_ee_squared", {})
    oo = amp.get("amplitude_oo_squared", {})
    separations = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0]
    total = 0
    correct = 0
    for sep in separations:
        key = str(sep)
        for orient in ["100", "110"]:
            e = ee.get(key, {}).get(orient)
            o = oo.get(key, {}).get(orient)
            expected = ent.get(key, {}).get(orient)
            if e is None or o is None or expected is None:
                continue
            total += 1
            s = 0.0
            if e > 0:
                s -= e * math.log2(e)
            if o > 0:
                s -= o * math.log2(o)
            if abs(s - expected) < 1e-6:
                correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_2 (check id='score_u_over_t') ===
def score_2(artifact, step, ctx):
    amp = ctx["step_01"]
    ut = ctx["step_03"]
    if amp is None or ut is None:
        return 0.0
    ee = amp.get("amplitude_ee_squared", {})
    oo = amp.get("amplitude_oo_squared", {})
    separations = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0]
    total = 0
    correct = 0
    for sep in separations:
        key = str(sep)
        for orient in ["100", "110"]:
            e = ee.get(key, {}).get(orient)
            o = oo.get(key, {}).get(orient)
            expected = ut.get(key, {}).get(orient)
            if e is None or o is None or expected is None or e == 0:
                continue
            total += 1
            alpha = o / e
            u_over_t = 2.0 * (1.0 / alpha - 1.0)
            if abs(u_over_t - expected) < 1e-6:
                correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_3 (check id='score_full_curves') ===
def score_3(artifact, step, ctx):
    step_04 = ctx["step_04"]
    if step_04 is None:
        return 0.0

    # Hidden gold curves (S for each orientation and separation, digitized from paper's theoretical predictions)
    gold_S = {
        "100": [
            {"separation": 2.0, "value": 0.18}, {"separation": 2.2, "value": 0.38},
            {"separation": 2.4, "value": 0.56}, {"separation": 2.6, "value": 0.70},
            {"separation": 2.8, "value": 0.81}, {"separation": 3.0, "value": 0.88},
            {"separation": 3.2, "value": 0.93}, {"separation": 3.4, "value": 0.96},
            {"separation": 3.5, "value": 0.975}, {"separation": 3.6, "value": 0.985},
            {"separation": 3.8, "value": 0.995}, {"separation": 4.0, "value": 0.998}
        ],
        "110": [
            {"separation": 2.0, "value": 0.10}, {"separation": 2.2, "value": 0.26},
            {"separation": 2.4, "value": 0.42}, {"separation": 2.6, "value": 0.56},
            {"separation": 2.8, "value": 0.68}, {"separation": 3.0, "value": 0.77},
            {"separation": 3.2, "value": 0.84}, {"separation": 3.4, "value": 0.90},
            {"separation": 3.5, "value": 0.92}, {"separation": 3.6, "value": 0.94},
            {"separation": 3.8, "value": 0.97}, {"separation": 4.0, "value": 0.99}
        ]
    }

    def S_to_U_over_t(S):
        if S <= 0:
            return 0.0
        lo, hi = 0.0, 1e6
        for _ in range(100):
            mid = (lo + hi) / 2.0
            if mid == 0.0:
                break
            p = 1.0 / (1.0 + mid)
            s_val = -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)
            if s_val < S:
                lo = mid
            else:
                hi = mid
        alpha = (lo + hi) / 2.0
        if alpha <= 0:
            return 0.0
        return 2.0 * (1.0 / alpha - 1.0)

    gold_U = {}
    for orient in ["100", "110"]:
        gold_U[orient] = []
        for pt in gold_S[orient]:
            sep = pt["separation"]
            s = pt["value"]
            gold_U[orient].append({"separation": sep, "value": S_to_U_over_t(s)})

    agent_S = step_04.get("S", {})
    agent_U = step_04.get("U_over_t", {})

    def compare_curves(agent_curves, gold_curves):
        total = 0
        correct = 0
        for orient in ["100", "110"]:
            agent_pts = agent_curves.get(orient, [])
            gold_pts = gold_curves.get(orient, [])
            gold_dict = {}
            for gp in gold_pts:
                sep = gp.get("separation")
                if sep is not None:
                    gold_dict[str(sep)] = gp.get("value")
            for ap in agent_pts:
                sep = ap.get("separation")
                val = ap.get("value")
                if sep is None or val is None:
                    continue
                key = str(sep)
                if key not in gold_dict:
                    continue
                gold_val = gold_dict[key]
                rel_err = abs(val - gold_val) / (abs(gold_val) + 1e-12)
                total += 1
                if rel_err <= 0.20:
                    correct += 1
        return total, correct

    total_S, correct_S = compare_curves(agent_S, gold_S)
    total_U, correct_U = compare_curves(agent_U, gold_U)
    total_all = total_S + total_U
    if total_all == 0:
        return 0.0
    return (correct_S + correct_U) / total_all


_SCORERS = {
    'score_amplitudes': score_0,
    'score_entropy': score_1,
    'score_u_over_t': score_2,
    'score_full_curves': score_3,
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
