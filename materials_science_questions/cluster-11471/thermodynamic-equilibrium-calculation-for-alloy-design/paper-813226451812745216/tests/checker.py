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


# === block: score_0 (check id='step_01_femnc') ===
def score_0(artifact, step, ctx):
        gold_velocities = {
            823.15: 1.0e-10,
            818.15: 1.0e-10,
            813.15: 1.0e-10,
            808.15: 1.0e-10,
            803.15: 1.0e-10,
            798.15: 1.0e-10,
            793.15: 1.0e-10,
            788.15: 1.0e-10,
            783.15: 1.0e-10,
            778.15: 1.0e-10,
            773.15: 1.0e-10,
            768.15: 1.0e-10,
            763.15: 1.0e-10,
            758.15: 1.0e-10,
            753.15: 1.0e-10,
            748.15: 1.0e-10,
            743.15: 1.0e-10,
            738.15: 1.05e-10,
            733.15: 1.4e-10,
            728.15: 3.0e-10,
            723.15: 8.0e-10,
            718.15: 2.5e-9,
            713.15: 6.5e-9,
            708.15: 5.0e-8,
            703.15: 3.0e-7,
            698.15: 8.0e-7,
            693.15: 1.2e-6,
            688.15: 1.45e-6,
            683.15: 1.5e-6,
            678.15: 1.5e-6,
            673.15: 1.5e-6,
        }
        tol_log = 0.5
        agent = {}
        for row in artifact:
            try:
                agent[float(row["temperature_K"])] = float(row["velocity_m_s"])
            except:
                pass
        if not agent:
            return 0.0
        total = len(gold_velocities)
        passed = 0
        for T, vg in gold_velocities.items():
            va = agent.get(T)
            if va is None:
                closest = None
                min_diff = None
                for t, v2 in agent.items():
                    if abs(t - T) <= 1.0:
                        if min_diff is None or abs(t - T) < min_diff:
                            min_diff = abs(t - T)
                            closest = v2
                if closest is None:
                    continue
                va = closest
            if va <= 0:
                continue
            log_diff = abs(math.log10(va) - math.log10(vg))
            if log_diff <= tol_log:
                passed += 1
        fraction = passed / total if total else 0.0
        max_T = max(agent.keys())
        min_T = min(agent.keys())
        v_start = agent[max_T]
        v_end = agent[min_T]
        struct_ok = (v_start < 1e-8 and (v_end / max(v_start, 1e-20)) > 100)
        return 0.8 * fraction + 0.2 * (1.0 if struct_ok else 0.0)


# === block: score_1 (check id='step_02_femnsic') ===
def score_1(artifact, step, ctx):
        temps = []
        vels = []
        for row in artifact:
            try:
                T = float(row["temperature_K"])
                v = float(row["velocity_m_s"])
                if v > 0:
                    temps.append(T)
                    vels.append(v)
            except:
                pass
        if len(temps) < 2:
            return 0.0
        pairs = sorted(zip(temps, vels), reverse=True)  # descending T
        max_T, v_start = pairs[0]
        min_T, v_end = pairs[-1]
        stagnant_ok = v_start < 1e-9
        fast_ok = v_end > 5e-7
        monotonic = all(pairs[i][1] <= pairs[i+1][1] for i in range(len(pairs)-1))
        score = 0.0
        if stagnant_ok:
            score += 0.25
        if fast_ok:
            score += 0.25
        if monotonic:
            score += 0.5
        return min(score, 1.0)


_SCORERS = {
    'step_01_femnc': score_0,
    'step_02_femnsic': score_1,
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
