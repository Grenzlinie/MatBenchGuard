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


# === block: score_0 (check id='recompute_critical_strain') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact.get('critical_strain_data', [])
        required_x = step.get('required_x_values', [])
        tol = step.get('tolerance_abs', 0.001)
        if not required_x or not data:
            return 0.0
        xs = {item['x']: item for item in data}
        A = 4 * math.pi * (1 - math.sqrt(3) / 2)
        eps_ok = 0
        delta_ok = 0
        for x in required_x:
            if x not in xs:
                continue
            item = xs[x]
            u = x * x + 2 * x
            sqrt_u = math.sqrt(u)
            xp1 = x + 1.0
            g = sqrt_u / xp1
            dNdx_denom = sqrt_u * xp1 * xp1 * (1 - g) * (1 - g)
            dNdx = A / dNdx_denom
            delta_x_C_true = 1.0 / (2 * dNdx)
            eps_crit_true = 3 * delta_x_C_true / (2 * x)
            if abs(item.get('epsilon_V_crit', 0) - eps_crit_true) <= tol:
                eps_ok += 1
            if abs(item.get('delta_x_C', 0) - delta_x_C_true) <= tol:
                delta_ok += 1
        N = len(required_x)
        eps_rate = eps_ok / N
        delta_rate = delta_ok / N
        return 0.7 * eps_rate + 0.3 * delta_rate


# === block: score_1 (check id='compare_glass_transition') ===
def score_1(artifact, step, ctx):
        gt = artifact.get('glass_transition', {})
        if not isinstance(gt, dict):
            return 0.0
        targets = step.get('targets', {})
        tolerances = step.get('tolerances_relative', {})
        tg_target = targets.get('T_g_K', 652.0)
        tol_tg = tolerances.get('T_g_K', 0.02)
        score_tg = 0.0
        tg = gt.get('T_g_K', None)
        if tg is not None and tg_target != 0:
            if abs(tg - tg_target) / tg_target <= tol_tg:
                score_tg = 1.0
        eps_crit = (6 * math.sqrt(3) - 9) / (8 * math.pi)
        k_B_eV_K = 8.617333262145e-5
        OmegaK = k_B_eV_K * tg_target / (2 * eps_crit * eps_crit)
        expected_Ea = 0.312 * OmegaK
        tol_ea = tolerances.get('E_a_eV', 0.03)
        score_ea = 0.0
        ea = gt.get('E_a_eV', None)
        if ea is not None and expected_Ea != 0:
            if abs(ea - expected_Ea) / expected_Ea <= tol_ea:
                score_ea = 1.0
        return (score_tg + score_ea) / 2.0


_SCORERS = {
    'recompute_critical_strain': score_0,
    'compare_glass_transition': score_1,
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
