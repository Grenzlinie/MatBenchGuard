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
    ctx = {}
    for step in spec["steps"]:
        ctx[step["id"]] = step.get("gold", {})
    return ctx


# === block: score_0 (check id='step05_dft_results') ===
def score_0(artifact, step, ctx):
    gold = ctx[step["id"]]
    systems_gold = gold["systems"]
    tol = gold["tolerances"]
    wt = gold["weights"]
    # artifact is list of dicts
    agent_map = {}
    for entry in artifact:
        sys = entry.get("system")
        if sys:
            agent_map[sys] = entry
    n_sys = len(systems_gold)
    if n_sys == 0:
        return 1.0 if artifact else 0.0
    scores = []
    for sys, g in systems_gold.items():
        if sys not in agent_map:
            scores.append(0.0)
            continue
        ae = agent_map[sys]
        sub = 0.0
        # magnetic moment
        mm_gold = g["magnetic_moment"]
        mm_agent = ae.get("magnetic_moment", 0.0)
        mm_diff = abs(mm_agent - mm_gold)
        mm_tol = tol["magnetic_moment"]
        if mm_diff <= mm_tol:
            mm_score = 1.0
        elif mm_diff <= 2*mm_tol:
            mm_score = 0.5
        else:
            mm_score = 0.0
        sub += mm_score * wt["magnetic_moment"]
        # epsilon
        eps_gold = g["epsilon"]
        eps_agent = ae.get("epsilon", 0.0)
        eps_diff = abs(eps_agent - eps_gold)
        eps_tol = tol["epsilon"] if eps_gold != 0 else tol["epsilon_zero_tol"]
        if eps_diff <= eps_tol:
            eps_score = 1.0
        elif eps_diff <= 2*eps_tol:
            eps_score = 0.5
        else:
            eps_score = 0.0
        sub += eps_score * wt["epsilon"]
        # binding energy
        be_gold = g.get("binding_energy")
        if be_gold is not None:
            be_agent = ae.get("binding_energy", 0.0)
            be_diff = abs(be_agent - be_gold)
            be_tol = tol["binding_energy"]
            if be_diff <= be_tol:
                be_score = 1.0
            elif be_diff <= 2*be_tol:
                be_score = 0.5
            else:
                be_score = 0.0
            sub += be_score * wt["binding_energy"]
        else:
            sub += 1.0 * wt["binding_energy"]  # missing gold -> full credit
        scores.append(sub)
    return sum(scores) / n_sys


# === block: score_1 (check id='step07_strain_results') ===
def score_1(artifact, step, ctx):
    gold = ctx[step["id"]]
    sys_gold = gold["systems"]
    eps_tol = gold.get("strain_tolerance", 20.0)
    expected_strains = [0, 5, 10, 15]
    data = {}
    for entry in artifact:
        sys = entry.get("system")
        strain = entry.get("strain")
        eps = entry.get("epsilon")
        if sys and strain is not None and eps is not None:
            data.setdefault(sys, []).append((strain, eps))
    sys_scores = {}
    for sys_name, base_gold in sys_gold.items():
        if sys_name not in data:
            sys_scores[sys_name] = 0.0
            continue
        entries = sorted(data[sys_name], key=lambda x: x[0])
        # baseline at strain 0
        base_score = 1.0
        found0 = False
        for strain, eps in entries:
            if strain == 0:
                found0 = True
                diff = abs(eps - base_gold["epsilon_0"])
                if diff <= eps_tol:
                    base_score = 1.0
                elif diff <= 2*eps_tol:
                    base_score = 0.5
                else:
                    base_score = 0.0
                break
        if not found0:
            base_score = 0.0
        # extract eps for expected strains, preserving order
        eps_map = {s: e for s, e in entries if s in expected_strains}
        eps_list = [eps_map[s] for s in expected_strains if s in eps_map]
        if not eps_list:
            mono_score = 0.0
        else:
            # positivity
            if not all(e >= -1.0 for e in eps_list):
                mono_score = 0.0
            else:
                # monotonic non-decrease with small tolerance
                mono = all(eps_list[i+1] >= eps_list[i] - 0.5 for i in range(len(eps_list)-1))
                if mono:
                    mono_score = 1.0
                else:
                    violations = sum(1 for i in range(len(eps_list)-1) if eps_list[i+1] < eps_list[i] - 0.5)
                    mono_score = max(0.0, 1.0 - 0.3 * violations)
        sys_scores[sys_name] = 0.3 * base_score + 0.7 * mono_score
    n_sys = len(sys_scores)
    if n_sys == 0:
        return 0.0
    return sum(sys_scores.values()) / n_sys


_SCORERS = {
    'step05_dft_results': score_0,
    'step07_strain_results': score_1,
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
