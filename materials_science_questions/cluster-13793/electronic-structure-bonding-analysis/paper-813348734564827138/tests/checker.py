import os
import json
import csv

# === author imports / helpers ===
import math

def try_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def in_tolerance(agent_val, gold_val, abs_tol, rel_tol):
    f = try_float(agent_val)
    if f is None:
        return False
    return abs(f - gold_val) <= max(abs_tol, rel_tol * abs(gold_val))


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
    tol = {"lattice_abs": 0.05, "lattice_rel": 0.02, "volume_abs": 5.0, "volume_rel": 0.02}
    gold_by_step = {}
    for step in spec["steps"]:
        gold_by_step[step["id"]] = step["gold"]

    def score_lattice_row(artifact, system, n, gold, tol):
        # Find matching row
        row = None
        for r in artifact:
            if r.get("system") == system and try_float(r.get("n")) == n:
                row = r
                break
        if row is None:
            return 0.0

        expected_converged = gold.get("converged")
        agent_converged_str = row.get("converged", "").strip().lower()
        agent_converged = agent_converged_str == "true"

        # Special case n=12 LaFeO3 (only convergence flag matter)
        if n == 12 and system == "LaFeO3":
            return 1.0 if agent_converged == expected_converged else 0.0

        # For other rows, convergence must be True to score lattice params
        if agent_converged != expected_converged:
            return 0.0

        # Score lattice parameters
        passed = 0
        for key in ["a", "b", "c"]:
            if in_tolerance(row.get(key), gold[key], tol["lattice_abs"], tol["lattice_rel"]):
                passed += 1
        if in_tolerance(row.get("volume"), gold["volume"], tol["volume_abs"], tol["volume_rel"]):
            passed += 1
        return passed / 4.0

    ctx = {"score_lattice_row": score_lattice_row, "gold_by_step": gold_by_step, "tol": tol}
    return ctx


# === block: score_0 (check id='LaFeO3_n0') ===
def score_0(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaFeO3", 0, ctx["gold_by_step"]["LaFeO3_n0"], ctx["tol"])


# === block: score_1 (check id='LaFeO3_n3') ===
def score_1(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaFeO3", 3, ctx["gold_by_step"]["LaFeO3_n3"], ctx["tol"])


# === block: score_2 (check id='LaFeO3_n6') ===
def score_2(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaFeO3", 6, ctx["gold_by_step"]["LaFeO3_n6"], ctx["tol"])


# === block: score_3 (check id='LaFeO3_n9') ===
def score_3(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaFeO3", 9, ctx["gold_by_step"]["LaFeO3_n9"], ctx["tol"])


# === block: score_4 (check id='LaFeO3_n12') ===
def score_4(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaFeO3", 12, ctx["gold_by_step"]["LaFeO3_n12"], ctx["tol"])


# === block: score_5 (check id='LaCrO3_n0') ===
def score_5(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaCrO3", 0, ctx["gold_by_step"]["LaCrO3_n0"], ctx["tol"])


# === block: score_6 (check id='LaCrO3_n3') ===
def score_6(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaCrO3", 3, ctx["gold_by_step"]["LaCrO3_n3"], ctx["tol"])


# === block: score_7 (check id='LaCrO3_n6') ===
def score_7(artifact, step, ctx):
    return ctx["score_lattice_row"](artifact, "LaCrO3", 6, ctx["gold_by_step"]["LaCrO3_n6"], ctx["tol"])


_SCORERS = {
    'LaFeO3_n0': score_0,
    'LaFeO3_n3': score_1,
    'LaFeO3_n6': score_2,
    'LaFeO3_n9': score_3,
    'LaFeO3_n12': score_4,
    'LaCrO3_n0': score_5,
    'LaCrO3_n3': score_6,
    'LaCrO3_n6': score_7,
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
