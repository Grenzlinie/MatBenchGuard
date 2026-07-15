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
    gold = None
    for step in spec.get('steps', []):
        if step.get('id') == 'step03':
            gold = step.get('gold', {})
            break
    return {'gold': gold}


# === block: score_0 (check id='step03') ===
def score_0(artifact, step, ctx):
    G_obj = artifact.get('G', {})
    PG_obj = artifact.get('PG', {})
    gold = ctx['gold']

    # detachment boolean check
    score_det = 1.0 if (G_obj.get('detachment') is False and PG_obj.get('detachment') is True) else 0.0

    # t_d tolerance score
    t_d_score = 0.0
    if PG_obj.get('detachment') and PG_obj.get('t_d') is not None:
        t_d = float(PG_obj['t_d'])
        target = gold['t_d_target_ps']
        tol = gold['t_d_tol_ps']
        err = abs(t_d - target)
        if err <= tol:
            t_d_score = 1.0
        else:
            t_d_score = max(0.0, 1.0 - (err - tol) / tol)

    # v_d range score
    v_d_score = 0.0
    if PG_obj.get('detachment') and PG_obj.get('v_d') is not None:
        v_d = float(PG_obj['v_d'])
        v_min = gold['v_d_min']
        v_max = gold['v_d_max']
        v_d_score = 1.0 if v_min <= v_d <= v_max else 0.0

    # energy ratio scores
    dE_CuCu_ratio_score = 0.0
    E_CCu_ratio_score = 0.0
    try:
        g_dE = abs(float(G_obj.get('dE_CuCu', 0)))
        pg_dE = abs(float(PG_obj.get('dE_CuCu', 0)))
        if g_dE > 0:
            de_ratio = pg_dE / g_dE
            de_min = gold['dE_CuCu_ratio_min']
            dE_CuCu_ratio_score = min(1.0, de_ratio / de_min)
        g_E = abs(float(G_obj.get('E_CCu', 0)))
        pg_E = abs(float(PG_obj.get('E_CCu', 0)))
        if g_E > 0:
            e_ratio = pg_E / g_E
            e_max = gold['E_CCu_ratio_max']
            if e_ratio <= e_max:
                E_CCu_ratio_score = 1.0
            else:
                E_CCu_ratio_score = max(0.0, 1.0 - (e_ratio - e_max) / e_max)
    except Exception:
        pass

    total = score_det * 0.1 + t_d_score * 0.4 + v_d_score * 0.2 + dE_CuCu_ratio_score * 0.15 + E_CCu_ratio_score * 0.15
    return min(1.0, max(0.0, total))


_SCORERS = {
    'step03': score_0,
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
