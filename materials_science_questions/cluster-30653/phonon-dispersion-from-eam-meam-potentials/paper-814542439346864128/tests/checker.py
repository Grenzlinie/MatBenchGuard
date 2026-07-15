import os
import json
import csv

# === author imports / helpers ===
import json


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
    steps = spec.get("steps", [])
    acc_step = next((s for s in steps if s["id"] == "accuracy"), None)
    expected = acc_step["expected_entries"] if acc_step else []
    tolerances = acc_step["tolerances"] if acc_step else {}
    return {"expected_entries": expected, "tolerances": tolerances}


# === block: score_0 (check id='accuracy') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    expected = ctx["expected_entries"]
    tolerances = ctx["tolerances"]
    agent_map = {item.get("cluster"): item for item in artifact if isinstance(item, dict)}
    total_checks = 0
    passed = 0
    for exp in expected:
        cluster = exp["cluster"]
        agent = agent_map.get(cluster)
        if agent is None:
            total_checks += 2
            continue
        # migration barrier
        exp_mbar = exp["migration_barrier"]
        agent_mbar = agent.get("migration_barrier")
        total_checks += 1
        if agent_mbar is not None and isinstance(agent_mbar, (int, float)):
            abs_tol = max(tolerances["migration_barrier"]["abs"], tolerances["migration_barrier"]["rel"] * abs(exp_mbar))
            if abs(agent_mbar - exp_mbar) <= abs_tol:
                passed += 1
        # dissolution energy
        exp_diss = exp.get("dissolution_energy")
        agent_diss = agent.get("dissolution_energy")
        total_checks += 1
        if exp_diss is None:
            if agent_diss is None:
                passed += 1
        else:
            if agent_diss is not None and isinstance(agent_diss, (int, float)):
                abs_tol_d = tolerances["dissolution_energy"]["abs"]
                if abs(agent_diss - exp_diss) <= abs_tol_d:
                    passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='trends') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    agent_map = {item.get("cluster"): item for item in artifact if isinstance(item, dict)}
    pure_order = ["1He", "2He", "3He", "4He"]
    barriers = []
    for c in pure_order:
        v = agent_map.get(c, {}).get("migration_barrier")
        if v is not None and isinstance(v, (int, float)):
            barriers.append(v)
        else:
            barriers.append(None)
    total_checks = 3  # three comparisons for monotonic
    passed = 0
    if all(b is not None for b in barriers):
        if barriers[1] > barriers[0] + 1e-9 and barriers[2] > barriers[1] + 1e-9 and barriers[3] > barriers[2] + 1e-9:
            passed += 3
        else:
            if barriers[1] > barriers[0] + 1e-9:
                passed += 1
            if barriers[2] > barriers[1] + 1e-9:
                passed += 1
            if barriers[3] > barriers[2] + 1e-9:
                passed += 1
    mixed_pairs = [
        ("1He-1H", "1He"),
        ("1He-2H", "1He"),
        ("2He-1H", "2He"),
        ("2He-2H", "2He"),
        ("3He-1H", "3He")
    ]
    for mixed, pure in mixed_pairs:
        mbar = agent_map.get(mixed, {}).get("migration_barrier")
        pbar = agent_map.get(pure, {}).get("migration_barrier")
        if mbar is not None and pbar is not None and isinstance(mbar, (int, float)) and isinstance(pbar, (int, float)):
            if mbar > pbar + 1e-9:
                passed += 1
    total_checks += len(mixed_pairs)
    if total_checks == 0:
        return 0.0
    return passed / total_checks


_SCORERS = {
    'accuracy': score_0,
    'trends': score_1,
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
