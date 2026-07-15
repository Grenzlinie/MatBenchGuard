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


# === block: score_0 (check id='gap_check') ===
def score_0(artifact, step, ctx):
    artifact_text = artifact.strip()
    try:
        value = float(artifact_text)
    except:
        return 0.0
    target = step.get('target', 0.0)
    tolerance = step.get('tolerance', 0.0)
    return 1.0 if abs(value - target) <= tolerance else 0.0


# === block: score_1 (check id='transport_check') ===
def score_1(artifact, step, ctx):
    import math
    rows = artifact
    if not rows:
        return 0.0
    # structural checks
    struct_score = 0.0
    checks = 0
    try:
        # helper: group by material
        def group_rows(mat):
            return sorted([r for r in rows if r.get('material','') == mat], key=lambda r: int(r.get('temperature', 0)))
        pristine = group_rows('pristine')
        sm8 = group_rows('Sm8')
        sm17 = group_rows('Sm17')
        # 1) all Seebeck < 0
        if all(float(r.get('Seebeck', 0)) < 0 for r in rows):
            struct_score += 1.0
        checks += 1
        # 2) pristine |S| strictly decreasing with T
        ok = True
        if len(pristine) >= 2:
            v0 = abs(float(pristine[0].get('Seebeck', 0)))
            for i in range(1, len(pristine)):
                vi = abs(float(pristine[i].get('Seebeck', 0)))
                if vi >= v0:
                    ok = False
                    break
                v0 = vi
        struct_score += 1.0 if ok else 0.0
        checks += 1
        # 3) pristine sigma_over_tau increases
        ok = True
        if len(pristine) >= 2:
            v0 = float(pristine[0].get('sigma_over_tau', 0))
            for i in range(1, len(pristine)):
                vi = float(pristine[i].get('sigma_over_tau', 0))
                if vi <= v0:
                    ok = False
                    break
                v0 = vi
        struct_score += 1.0 if ok else 0.0
        checks += 1
        # 4) Sm8 sigma_over_tau decreases
        ok = True
        if len(sm8) >= 2:
            v0 = float(sm8[0].get('sigma_over_tau', 0))
            for i in range(1, len(sm8)):
                vi = float(sm8[i].get('sigma_over_tau', 0))
                if vi >= v0:
                    ok = False
                    break
                v0 = vi
        struct_score += 1.0 if ok else 0.0
        checks += 1
        # 5) Sm17 sigma_over_tau decreases
        ok = True
        if len(sm17) >= 2:
            v0 = float(sm17[0].get('sigma_over_tau', 0))
            for i in range(1, len(sm17)):
                vi = float(sm17[i].get('sigma_over_tau', 0))
                if vi >= v0:
                    ok = False
                    break
                v0 = vi
        struct_score += 1.0 if ok else 0.0
        checks += 1
        # 6) ZT increases for each material
        for mat_rows in [pristine, sm8, sm17]:
            ok = True
            if len(mat_rows) >= 2:
                v0 = float(mat_rows[0].get('ZT', 0))
                for i in range(1, len(mat_rows)):
                    vi = float(mat_rows[i].get('ZT', 0))
                    if vi <= v0:
                        ok = False
                        break
                    v0 = vi
            struct_score += 1.0 if ok else 0.0
            checks += 1
        # 7) ZT ordering at each temperature: Sm17 > pristine > Sm8
        for i in range(6):
            try:
                z8 = float(sm8[i].get('ZT', 0))
                zp = float(pristine[i].get('ZT', 0))
                z17 = float(sm17[i].get('ZT', 0))
                if z17 > zp > z8:
                    struct_score += 1.0
                checks += 1
            except:
                struct_score += 0.0
                checks += 1
        struct_score = struct_score / checks if checks > 0 else 0.0
    except:
        struct_score = 0.0

    # numeric tolerance check
    gold_rows = step.get('gold_rows', [])
    tolerances = step.get('tolerances', {})
    if not gold_rows:
        return 0.0

    agent_lookup = {}
    for r in rows:
        try:
            key = (int(r.get('temperature')), r.get('material',''))
            agent_lookup[key] = r
        except:
            continue

    fields = ['Seebeck', 'sigma_over_tau', 'kappa_over_tau', 'ZT']
    total_cells = len(gold_rows) * len(fields)
    correct_cells = 0
    for gr in gold_rows:
        mat = gr.get('material', '')
        temp = gr.get('temperature')
        key = (int(temp), mat)
        ar = agent_lookup.get(key)
        if ar is None:
            continue
        for f in fields:
            gold_val = float(gr.get(f, 0.0))
            try:
                agent_val = float(ar.get(f, 0.0))
            except:
                continue
            tol_cfg = tolerances.get(f, {})
            if 'absolute' in tol_cfg and 'relative' in tol_cfg:
                limit = max(tol_cfg['relative'] * abs(gold_val), tol_cfg['absolute'])
                if abs(agent_val - gold_val) <= limit:
                    correct_cells += 1
            elif 'absolute' in tol_cfg:
                if abs(agent_val - gold_val) <= tol_cfg['absolute']:
                    correct_cells += 1
            elif 'relative' in tol_cfg:
                if abs(agent_val - gold_val) <= tol_cfg['relative'] * abs(gold_val):
                    correct_cells += 1
            else:
                correct_cells += 1  # no tolerance, always passes
    if total_cells == 0:
        numeric_score = 0.0
    else:
        numeric_score = correct_cells / total_cells

    return 0.3 * struct_score + 0.7 * numeric_score


_SCORERS = {
    'gap_check': score_0,
    'transport_check': score_1,
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
