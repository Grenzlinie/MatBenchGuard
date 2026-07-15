import os
import json
import csv

# === author imports / helpers ===
import re


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


# === block: score_0 (check id='step_03_phonon_frequencies') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get("gold_rows", [])
    if not gold_rows:
        return 0.0
    agent_map = {}
    for row in artifact:
        q = row.get("q_point", "").strip()
        mi = row.get("mode_index", "")
        try:
            mi = int(mi)
        except:
            continue
        agent_map[(q, mi)] = row
    total = 0
    passes = 0
    tol_ac = step.get("tolerance_acoustic", 10.0)
    tol_opt = step.get("tolerance_optical", 20.0)
    for gr in gold_rows:
        q = gr["q_point"]
        mi = gr["mode_index"]
        gold_m2 = gr["gold_freq_M2"]
        gold_m8 = gr["gold_freq_M8Dip"]
        key = (q, mi)
        arow = agent_map.get(key)
        if arow is None:
            total += 2
            continue
        # M2
        val = arow.get("frequency_M2")
        if val is not None:
            try:
                val = float(val)
            except:
                total += 1
            else:
                tol = tol_ac if abs(gold_m2) < 1e-6 else tol_opt
                if abs(val - gold_m2) <= tol + 1e-9:
                    passes += 1
                total += 1
        # M8+Dip
        val = arow.get("frequency_M8+Dip")
        if val is not None:
            try:
                val = float(val)
            except:
                total += 1
            else:
                tol = tol_ac if abs(gold_m8) < 1e-6 else tol_opt
                if abs(val - gold_m8) <= tol + 1e-9:
                    passes += 1
                total += 1
    if total == 0:
        return 0.0
    return passes / total


# === block: score_1 (check id='step_04_to_mode') ===
def score_1(artifact, step, ctx):
    gold_m2 = step["gold_freq_M2"]
    gold_m8 = step["gold_freq_M8Dip"]
    gold_char = step["gold_character"]
    tol = step.get("tolerance_freq", 20.0)
    text = artifact  # string
    lines = text.splitlines()
    score = 0.0
    for line in lines:
        line = line.strip()
        if line.startswith("M2:"):
            m = re.search(r"frequency=([-\d.]+)\s*\(cm\^-1\)", line)
            if m:
                freq = float(m.group(1))
                if abs(freq - gold_m2) <= tol:
                    score += 0.4
            if gold_char in line.lower():
                score += 0.1
        elif line.startswith("M8+Dip:"):
            m = re.search(r"frequency=([-\d.]+)\s*\(cm\^-1\)", line)
            if m:
                freq = float(m.group(1))
                if abs(freq - gold_m8) <= tol:
                    score += 0.4
            if gold_char in line.lower():
                score += 0.1
    return min(score, 1.0)


# === block: score_2 (check id='step_05_hysteresis') ===
def score_2(artifact, step, ctx):
    gold_coercive = step["gold_coercive"]
    gold_remanent = step["gold_remanent"]
    tol_coer = step.get("tolerance_coercive", 0.5)
    tol_rem = step.get("tolerance_remanent", 5.0)
    agent_rows = {r["model"].strip(): r for r in artifact}
    total = 4
    passes = 0
    for model in ["M2", "M8+Dip"]:
        row = agent_rows.get(model)
        if row is None:
            continue
        try:
            coer = float(row["coercive_field"])
        except:
            coer = None
        try:
            rem = float(row["remanent_polarization"])
        except:
            rem = None
        gcoer = gold_coercive.get(model)
        grem = gold_remanent.get(model)
        if gcoer is not None and coer is not None and abs(coer - gcoer) <= tol_coer:
            passes += 1
        if grem is not None and rem is not None and abs(rem - grem) <= tol_rem:
            passes += 1
    if total == 0:
        return 0.0
    return passes / total


_SCORERS = {
    'step_03_phonon_frequencies': score_0,
    'step_04_to_mode': score_1,
    'step_05_hysteresis': score_2,
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
