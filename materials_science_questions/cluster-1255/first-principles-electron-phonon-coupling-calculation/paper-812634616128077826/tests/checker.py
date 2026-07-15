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


# === block: score_0 (check id='step_01_csv') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact
        if not rows:
            return 0.0
        import math
        T = [float(r.get('T', 0)) for r in rows]
        eps = [float(r.get('epsilon', 0)) for r in rows]
        chi = [float(r.get('chi', 0)) for r in rows]
        C = [float(r.get('C', 0)) for r in rows]
        gold = step.get('config', {})
        Tm_gold = gold.get('Tm_gold', 21.0)
        Tm_tol = gold.get('Tm_tol', 2.0)
        delta_chi_gold = gold.get('chi_drop_gold', 4e-05)
        delta_chi_tol = gold.get('chi_drop_tol', 2e-05)
        delta_C_gold = gold.get('C_jump_gold', 0.4)
        delta_C_tol = gold.get('C_jump_tol', 0.1)
        ok_rows = 1 if len(rows) >= 20 else 0
        T_min = min(T)
        T_max = max(T)
        ok_range = 1 if (T_min <= 0.0 + 1e-09 and T_max >= 50.0 - 1e-09) else 0
        high_T_mask = [t > Tm_gold + Tm_tol for t in T]
        if not any(high_T_mask):
            ok_eps_high = 0
        else:
            eps_high = [e for e, h in zip(eps, high_T_mask) if h]
            ok_eps_high = 1 if all(abs(e) < 1e-09 for e in eps_high) else 0
        pairs = list(zip(T, chi))
        pairs.sort(key=lambda x: x[0])
        T_sorted = [p[0] for p in pairs]
        chi_sorted = [p[1] for p in pairs]
        idx_below = None
        idx_above = None
        for i, t in enumerate(T_sorted):
            if t <= Tm_gold:
                idx_below = i
            if t >= Tm_gold and idx_above is None:
                idx_above = i
        if idx_below is None or idx_above is None:
            ok_chi_drop = 0
        else:
            delta_chi = chi_sorted[idx_above] - chi_sorted[idx_below]
            ok_chi_drop = 1 if abs(delta_chi - delta_chi_gold) <= delta_chi_tol else 0
        pairsC = list(zip(T, C))
        pairsC.sort(key=lambda x: x[0])
        T_sortedC = [p[0] for p in pairsC]
        C_sorted = [p[1] for p in pairsC]
        idx_belowC = None
        idx_aboveC = None
        for i, t in enumerate(T_sortedC):
            if t <= Tm_gold:
                idx_belowC = i
            if t >= Tm_gold and idx_aboveC is None:
                idx_aboveC = i
        if idx_belowC is None or idx_aboveC is None:
            ok_C_jump = 0
        else:
            delta_C = C_sorted[idx_aboveC] - C_sorted[idx_belowC]
            ok_C_jump = 1 if abs(delta_C - delta_C_gold) <= delta_C_tol else 0
        checks = [ok_rows, ok_range, ok_eps_high, ok_chi_drop, ok_C_jump]
        return sum(checks) / float(len(checks))
    except Exception:
        return 0.0


# === block: score_1 (check id='step_02_json') ===
def score_1(artifact, step, ctx):
    try:
        artifact = artifact or {}
        gold = step.get('config', {})
        fields = [
            ('epsilon_0', gold.get('epsilon_0_gold', 0.0029), gold.get('epsilon_0_tol', 0.0005)),
            ('Tm', gold.get('Tm_gold', 21.0), gold.get('Tm_tol', 2.0)),
            ('dchi_dT_at_Tm', gold.get('dchi_dT_gold', 0.032), gold.get('dchi_dT_tol', 0.005)),
            ('Delta_Cv', gold.get('Delta_Cv_gold', 0.4), gold.get('Delta_Cv_tol', 0.1)),
        ]
        scores = []
        for field, gval, tol in fields:
            val = artifact.get(field)
            if val is None or not isinstance(val, (int, float)):
                scores.append(0.0)
            else:
                ok = abs(float(val) - gval) <= tol
                scores.append(1.0 if ok else 0.0)
        return sum(scores) / float(len(scores))
    except Exception:
        return 0.0


_SCORERS = {
    'step_01_csv': score_0,
    'step_02_json': score_1,
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
