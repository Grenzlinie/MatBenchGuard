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
    gold = {}
    for step in spec["steps"]:
        step_id = step["id"]
        config = step.get("config", {})
        gold[step_id] = config.get("gold", {})
    return {"gold": gold}


# === block: score_0 (check id='bond_lengths_angles') ===
def score_0(artifact, step, ctx):
    gold_table = ctx["gold"]["bond_lengths_angles"]
    if not gold_table:
        return 0.0
    lookup = {k: (v["value"], v["tolerance"]) for k, v in gold_table.items()}
    scores = []
    for row in artifact:
        param = row.get("parameter", "").strip()
        val_str = row.get("value", "")
        if param not in lookup or val_str == "":
            continue
        try:
            val = float(val_str)
        except ValueError:
            scores.append(0.0)
            continue
        gold_val, tol = lookup[param]
        diff = abs(val - gold_val)
        if diff <= tol:
            scores.append(1.0)
        else:
            # linear decay: 0 at diff >= 2*tol
            if tol > 0:
                scores.append(max(0.0, 1.0 - (diff - tol) / tol))
            else:
                scores.append(1.0 if diff == 0.0 else 0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='rumpling') ===
def score_1(artifact, step, ctx):
    gold_table = ctx["gold"]["rumpling"]
    if not gold_table:
        return 0.0
    scores = []
    for row in artifact:
        pos_str = str(row.get("position", "")).strip()
        if pos_str not in gold_table:
            continue
        try:
            oop = float(row["out_of_plane_rumpling"])
            ip = float(row["in_plane_rumpling"])
        except (ValueError, KeyError):
            scores.append(0.0)
            continue
        exp = gold_table[pos_str]
        tol = exp["tolerance"]
        # out-of-plane
        diff_oop = abs(oop - exp["out_of_plane"])
        if diff_oop <= tol:
            score_oop = 1.0
        else:
            score_oop = max(0.0, 1.0 - (diff_oop - tol) / tol) if tol > 0 else (1.0 if diff_oop == 0.0 else 0.0)
        # in-plane
        diff_ip = abs(ip - exp["in_plane"])
        if diff_ip <= tol:
            score_ip = 1.0
        else:
            score_ip = max(0.0, 1.0 - (diff_ip - tol) / tol) if tol > 0 else (1.0 if diff_ip == 0.0 else 0.0)
        scores.append(0.5 * score_oop + 0.5 * score_ip)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_energies') ===
def score_2(artifact, step, ctx):
    gold_table = ctx["gold"]["step_energies"]
    if not gold_table:
        return 0.0
    scores = []
    for row in artifact:
        etype = str(row.get("energy_type", "")).strip().lower()
        gamma_str = row.get("gamma", "")
        if etype not in gold_table or gamma_str == "":
            continue
        try:
            gamma = float(gamma_str)
        except ValueError:
            scores.append(0.0)
            continue
        gold_val = gold_table[etype]["value"]
        tol = gold_table[etype]["tolerance"]
        diff = abs(gamma - gold_val)
        if diff <= tol:
            scores.append(1.0)
        else:
            if tol > 0:
                scores.append(max(0.0, 1.0 - (diff - tol) / tol))
            else:
                scores.append(1.0 if diff == 0.0 else 0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'bond_lengths_angles': score_0,
    'rumpling': score_1,
    'step_energies': score_2,
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
