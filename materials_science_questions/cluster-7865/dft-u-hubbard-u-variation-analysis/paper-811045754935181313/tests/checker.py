import os
import json
import csv

# === author imports / helpers ===
import os
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
    electronic_path = os.path.join(outputs_dir, "electronic_properties.json")
    ctx = {}
    if os.path.exists(electronic_path):
        with open(electronic_path) as f:
            ctx["electronic"] = json.load(f)
    else:
        ctx["electronic"] = None
    return ctx


# === block: score_0 (check id='check_electronic') ===
def score_0(artifact, step, ctx):
    data = artifact
    if isinstance(data, dict):
        data = [data]
    by_u = {}
    for item in data:
        u = item.get("U")
        if u is not None:
            by_u[str(u)] = item

    gold = step["gold"]
    tolerances = step["tolerances"]
    fields = ["E_g_up", "E_g_down", "delta_E_c", "delta_E_v", "N_alpha", "N_beta"]
    passed = 0
    total = 0
    for u_key, expected in gold.items():
        item = by_u.get(u_key)
        if item is None:
            continue
        for f in fields:
            total += 1
            exp_val = expected.get(f)
            if exp_val is None:
                continue
            agent_val = item.get(f)
            if agent_val is None:
                continue
            tol = tolerances.get(f, 0.0)
            if abs(agent_val - exp_val) <= tol:
                passed += 1

    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='check_magnetic') ===
def score_1(artifact, step, ctx):
    data = artifact
    if isinstance(data, dict):
        data = [data]
    by_u = {}
    for item in data:
        u = item.get("U")
        if u is not None:
            by_u[str(u)] = item

    gold = step["gold"]
    tolerances = step["tolerances"]
    fields = ["Mg", "Mn", "O", "Interstitial", "Total"]
    passed = 0
    total = 0
    for u_key, expected in gold.items():
        item = by_u.get(u_key)
        if item is None:
            continue
        for f in fields:
            total += 1
            exp_val = expected.get(f)
            if exp_val is None:
                continue
            agent_val = item.get(f)
            if agent_val is None:
                continue
            tol = tolerances.get(f, 0.0)
            if abs(agent_val - exp_val) <= tol:
                passed += 1

    if total == 0:
        return 0.0
    return passed / total


# === block: score_2 (check id='check_optical') ===
def score_2(artifact, step, ctx):
    cases = []
    reductions = None
    for item in artifact:
        if isinstance(item, dict):
            if "U" in item and "ligand_field" in item:
                cases.append(item)
            elif "reduction_up_U0" in item:
                reductions = item

    gold_cases = step["gold"]["cases"]
    gold_reductions = step["gold"]["reductions"]
    tol_gap = step["tolerances"]["E_g_up"]  # same for down
    tol_red = step["tolerances"]["reduction"]

    # --- gap checking ---
    n_gap = 0
    n_gap_ok = 0
    agent_case_map = {}
    for c in cases:
        key = (c.get("U"), c.get("ligand_field"))
        agent_case_map[key] = c

    for gc in gold_cases:
        key = (gc["U"], gc["ligand_field"])
        ac = agent_case_map.get(key)
        if ac is None:
            n_gap += 2
            continue
        for spin in ("E_g_up", "E_g_down"):
            n_gap += 1
            agent_val = ac.get(spin)
            gold_val = gc[spin]
            if agent_val is not None and abs(agent_val - gold_val) <= tol_gap:
                n_gap_ok += 1

    gap_subscore = (n_gap_ok / n_gap) if n_gap > 0 else 0.0

    # --- reduction recompute from agent's own gaps ---
    agent_gaps = {}
    for c in cases:
        u = c.get("U")
        lf = c.get("ligand_field")
        agent_gaps[(u, lf)] = (c.get("E_g_up"), c.get("E_g_down"))

    red_ok = 0
    red_total = 4

    for u in (0, 6):
        weak_key = (u, "weak")
        strong_key = (u, "strong")
        if weak_key not in agent_gaps or strong_key not in agent_gaps:
            continue
        weak_up, weak_down = agent_gaps[weak_key]
        strong_up, strong_down = agent_gaps[strong_key]
        # up reduction
        if weak_up is not None and weak_up != 0:
            red_up = (weak_up - strong_up) / weak_up * 100 if strong_up is not None else None
        else:
            red_up = None
        if weak_down is not None and weak_down != 0:
            red_down = (weak_down - strong_down) / weak_down * 100 if strong_down is not None else None
        else:
            red_down = None
        for spin, target_key, val in [("up", f"reduction_up_U{u}", red_up), ("down", f"reduction_down_U{u}", red_down)]:
            if val is not None and abs(val - gold_reductions[target_key]) <= tol_red:
                red_ok += 1

    red_subscore = red_ok / red_total if red_total > 0 else 0.0

    # --- consistency: optical gap >= electronic gap ---
    consist_ok = 0
    consist_total = 0
    electronic = ctx.get("electronic")
    if electronic:
        elec_by_u = {}
        for e in electronic:
            u = e.get("U")
            if u is not None:
                elec_by_u[str(u)] = e
        for c in cases:
            u = c.get("U")
            elec = elec_by_u.get(str(u))
            if elec is None:
                continue
            for spin in ("E_g_up", "E_g_down"):
                opt = c.get(spin)
                elec_val = elec.get(spin)
                if opt is not None and elec_val is not None:
                    consist_total += 1
                    if opt >= elec_val - 0.1:
                        consist_ok += 1
    consist_subscore = (consist_ok / consist_total) if consist_total > 0 else 0.0

    step_score = 0.4*gap_subscore + 0.4*red_subscore + 0.2*consist_subscore
    return step_score


_SCORERS = {
    'check_electronic': score_0,
    'check_magnetic': score_1,
    'check_optical': score_2,
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
