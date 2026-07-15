import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    gold_absorption = spec.get("gold_absorption_pct", {})
    agent_absorption = {}
    try:
        with open(os.path.join(outputs_dir, "step_01_energy_absorption.csv"), newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                kv = int(row["beam_voltage_kV"])
                pct = float(row["energy_absorbed_pct"])
                agent_absorption[kv] = pct
    except FileNotFoundError:
        pass
    expected_mpp = {}
    base_pct = agent_absorption.get(62, None)
    if base_pct is not None and base_pct != 0:
        for kv, pct in agent_absorption.items():
            expected_mpp[kv] = 97.8 * pct / base_pct
    return {"gold_absorption": gold_absorption, "expected_mpp": expected_mpp}


# === block: score_0 (check id='step_01_energy_absorption_check') ===
def score_0(artifact, step, ctx):
    gold_raw = ctx.get("gold_absorption", {})
    # Convert keys to int and keep only beam voltages actually tabulated in the paper (62-180 kV)
    valid_voltages = {62, 80, 100, 120, 140, 160, 180}
    gold = {}
    for k, v in gold_raw.items():
        try:
            kv = int(k)
        except (ValueError, TypeError):
            continue
        if kv in valid_voltages:
            gold[kv] = v
    if not gold or not artifact:
        return 0.0
    scores = []
    tol = float(step.get("tolerance", 0.2))
    for row in artifact:
        try:
            kv = int(row["beam_voltage_kV"])
            pct = float(row["energy_absorbed_pct"])
        except (ValueError, KeyError):
            continue
        g = gold.get(kv)
        if g is None:
            continue
        rel_err = abs(pct - g) / max(g, 1e-8)
        s = max(0.0, 1.0 - rel_err / tol)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02_mpp_check') ===
def score_1(artifact, step, ctx):
    expected_mpp = ctx.get("expected_mpp", {})
    if not expected_mpp or not artifact:
        return 0.0
    consistency_scores = []
    for row in artifact:
        try:
            kv = int(row["beam_voltage_kV"])
            mpp = float(row["simulated_mpp_nW"])
        except (ValueError, KeyError):
            continue
        e = expected_mpp.get(kv)
        if e is None:
            continue
        diff = abs(mpp - e)
        consistency_scores.append(1.0 if diff < 1e-4 else 0.0)
    sorted_volts = sorted(expected_mpp.keys())
    mpp_list = []
    for kv in sorted_volts:
        r = next((r for r in artifact if int(r["beam_voltage_kV"]) == kv), None)
        if r:
            mpp_list.append(float(r["simulated_mpp_nW"]))
        else:
            mpp_list.append(None)
    trend_scores = []
    for i in range(1, len(mpp_list)):
        if mpp_list[i-1] is not None and mpp_list[i] is not None:
            trend_scores.append(1.0 if mpp_list[i] <= mpp_list[i-1] else 0.0)
    consistency_avg = sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.0
    trend_avg = sum(trend_scores) / len(trend_scores) if trend_scores else 0.0
    return consistency_avg * 0.6 + trend_avg * 0.4


_SCORERS = {
    'step_01_energy_absorption_check': score_0,
    'step_02_mpp_check': score_1,
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
