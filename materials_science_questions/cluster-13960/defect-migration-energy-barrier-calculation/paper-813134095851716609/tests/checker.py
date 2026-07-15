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
    return {}


# === block: score_0 (check id='check_formation_energies') ===
def score_0(artifact, step, ctx):
    def get_all_energies(system_data):
        energies = []
        for orient, comps in system_data.items():
            for comp, e in comps.items():
                if isinstance(e, (int, float)):
                    energies.append((orient, comp, e))
        return energies

    params = step.get("params", {})
    expected_lowest = params.get("expected_lowest_systems", {})
    diff_checks = params.get("diff_checks", [])
    checks = {}

    for sys_key, exp_comp in expected_lowest.items():
        sys_data = artifact.get(sys_key)
        if not isinstance(sys_data, dict):
            continue
        all_es = get_all_energies(sys_data)
        if not all_es:
            checks[f"global_min_{sys_key}"] = False
            continue
        all_es.sort(key=lambda x: x[2])
        lowest_comp = all_es[0][1]
        checks[f"global_min_{sys_key}"] = (lowest_comp == exp_comp)

    ni3fe_100 = artifact.get("Ni3Fe", {}).get("<100>", {})
    order_NiFe_100 = ["Ni-Ni", "Ni-Fe", "Fe-Ni", "Fe-Fe"]
    if all(k in ni3fe_100 for k in order_NiFe_100):
        vals = [ni3fe_100[k] for k in order_NiFe_100]
        checks["ordering_NiFe_100"] = all(vals[i] < vals[i+1] for i in range(len(vals)-1))
    else:
        checks["ordering_NiFe_100"] = False

    for chk in diff_checks:
        system = chk["system"]
        orient = chk["orientation"]
        comp1 = chk["comp1"]
        comp2 = chk["comp2"]
        min_val = chk.get("min_diff")
        max_val = chk.get("max_diff")
        sys_data = artifact.get(system, {}).get(orient, {})
        e1 = sys_data.get(comp1)
        e2 = sys_data.get(comp2)
        if e1 is None or e2 is None:
            checks[f"diff_{system}_{comp1}_{comp2}"] = False
            continue
        diff = e2 - e1
        min_ok = (min_val is None or diff >= min_val)
        max_ok = (max_val is None or diff <= max_val)
        checks[f"diff_{system}_{comp1}_{comp2}"] = min_ok and max_ok

    sub_weights = {
        "global_min_Ni": 0.2,
        "global_min_Ni3Fe": 0.2,
        "global_min_Ni3Co": 0.2,
        "ordering_NiFe_100": 0.2,
        "diff_Ni3Fe_Ni-Ni_Ni-Fe": 0.1,
        "diff_Ni3Co_Ni-Co_Co-Co": 0.1,
    }
    total_w = sum(sub_weights.get(k, 0) for k in checks)
    score = sum(sub_weights.get(k, 0) for k, v in checks.items() if v) / total_w if total_w else 0.0
    return score


# === block: score_1 (check id='check_migration_barriers') ===
def score_1(artifact, step, ctx):
    params = step.get("params", {})
    barrier_checks = params.get("barrier_checks", [])
    score = 0.0
    total = 0
    for chk in barrier_checks:
        system = chk["system"]
        path = chk["path"]
        target = chk["target"]
        tol = chk["tolerance"]
        sys_data = artifact.get(system, {})
        val = sys_data.get(path)
        if val is None:
            continue
        if abs(val - target) <= tol:
            score += 1.0
        total += 1
    if total > 0:
        return score / total
    else:
        return 0.0


_SCORERS = {
    'check_formation_energies': score_0,
    'check_migration_barriers': score_1,
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
