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
    steps = spec.get("steps", spec.get("checks", []))
    for step in steps:
        step_id = step.get("id")
        if step_id == "effective_masses":
            ctx["eff_masses_ref"] = step.get("config", {}).get("reference", {})
            ctx["eff_masses_tol"] = step.get("config", {}).get("rel_tolerance", 0.2)
        elif step_id == "COHP_summary":
            ctx["cohp_config"] = step.get("config", {})
    return ctx


# === block: score_0 (check id='effective_masses') ===
def score_0(artifact, step, ctx):
    ref = ctx["eff_masses_ref"]
    tol = ctx["eff_masses_tol"]
    masses = []
    for cond in ["unstrained", "strained"]:
        ref_cond = ref.get(cond, {})
        agent_cond = artifact.get(cond, {})
        if not isinstance(agent_cond, dict):
            # fill missing scores as 0
            masses.extend([0.0]*4)
            continue
        for key in ["a_star", "b_star", "c_star", "conductivity"]:
            r = ref_cond.get(key)
            a = agent_cond.get(key)
            if r is None or a is None or not isinstance(a, (int, float)):
                masses.append(0.0)
                continue
            if r == 0:
                if abs(a) < 1e-9:
                    masses.append(1.0)
                else:
                    masses.append(0.0)
            else:
                rel_err = abs(a - r) / abs(r)
                if rel_err <= tol:
                    score = 1.0
                else:
                    score = max(0.0, 1.0 - (rel_err - tol) / 0.5)
                masses.append(score)
    return sum(masses) / len(masses) if masses else 0.0


# === block: score_1 (check id='COHP_summary') ===
def score_1(artifact, step, ctx):
    cfg = ctx["cohp_config"]
    score = 0.0
    gao = artifact.get("total_COHP_GaO_integrated_VBM")
    oo = artifact.get("total_COHP_OO_integrated_VBM")
    # 0.2 for O-O negativity and dominance
    if isinstance(gao, (int,float)) and isinstance(oo, (int,float)):
        if oo < 0 and abs(oo) > abs(gao):
            score += 0.2
    # Gamma pair 0.15 + COHP value 0.1
    gamma_pair = artifact.get("dominant_pair_at_Gamma", {})
    if isinstance(gamma_pair, dict):
        if gamma_pair.get("pair") == cfg["pair_gamma"]["pair"] and gamma_pair.get("orbitals") == cfg["pair_gamma"]["orbitals"]:
            score += 0.15
            g_val = gamma_pair.get("COHP_value")
            if isinstance(g_val, (int,float)) and g_val < 0 and abs(g_val - cfg["cohp_gamma_ref"]) <= cfg["tol_cohp"]:
                score += 0.1
    # I pair 0.15 + COHP value 0.1
    i_pair = artifact.get("dominant_pair_at_I", {})
    if isinstance(i_pair, dict):
        if i_pair.get("pair") == cfg["pair_I"]["pair"] and i_pair.get("orbitals") == cfg["pair_I"]["orbitals"]:
            score += 0.15
            i_val = i_pair.get("COHP_value")
            if isinstance(i_val, (int,float)) and i_val < 0 and abs(i_val - cfg["cohp_I_ref"]) <= cfg["tol_cohp"]:
                score += 0.1
    # integrated values tolerance 0.15 each
    if isinstance(gao, (int,float)) and abs(gao - cfg["integrated_gao_ref"]) <= cfg["tol_integrated"]:
        score += 0.15
    if isinstance(oo, (int,float)) and abs(oo - cfg["integrated_oo_ref"]) <= cfg["tol_integrated"]:
        score += 0.15
    return min(score, 1.0)


_SCORERS = {
    'effective_masses': score_0,
    'COHP_summary': score_1,
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
