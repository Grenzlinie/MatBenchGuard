import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    step = next(s for s in spec['steps'] if s['id'] == 'step03_compute_results')
    gold = { (r['phi'], r['alpha'], r['y']): r for r in step['gold_rows'] }
    return {'gold': gold, 'tolerance': step['tolerance']}


# === block: score_0 (check id='step03_compute_results') ===
def score_0(artifact, step, ctx):
    import json, math
    def score(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        gold = ctx['gold']
        tol = ctx['tolerance']
        rho_abs = tol.get('rho_abs', 0.001)
        ub_rel = tol.get('Ub_rel', 0.001)
        delta_abs = tol.get('delta_ud_abs', 0.001)
        atol_ub = 1e-5
        atol_rho = 1e-5
        atol_delta = 1e-5
        entries = { (d['phi'], d['alpha'], d['y']): d for d in artifact if all(k in d for k in ['phi','alpha','y','rho','Ub','delta_ud'])}
        matched = 0
        total = len(gold)
        for key, g in gold.items():
            a = entries.get(key)
            if a is None:
                continue
            ok = True
            if g['rho'] is None and a['rho'] is not None:
                ok = False
            elif g['rho'] is not None:
                if a['rho'] is None or abs(a['rho'] - g['rho']) > rho_abs + 1e-9:
                    ok = False
            if g['Ub'] is None and a['Ub'] is not None:
                ok = False
            elif g['Ub'] is not None:
                if a['Ub'] is None:
                    ok = False
                else:
                    err = abs(a['Ub'] - g['Ub'])
                    if err > max(atol_ub, g['Ub'] * ub_rel):
                        ok = False
            if g['delta_ud'] is None and a['delta_ud'] is not None:
                ok = False
            elif g['delta_ud'] is not None:
                if a['delta_ud'] is None:
                    ok = False
                else:
                    err = abs(a['delta_ud'] - g['delta_ud'])
                    if err > max(atol_delta, g['delta_ud'] * delta_abs):
                        ok = False
            if ok:
                matched += 1
        field_score = matched / total if total > 0 else 0.0
        series = {}
        for d in entries.values():
            phi = d['phi']; alpha = d['alpha']; y = d['y']; Ub = d.get('Ub')
            if Ub is None:
                continue
            series.setdefault((phi, alpha), []).append((y, Ub))
        monotonic_ok = True
        for pts in series.values():
            pts.sort(key=lambda p: p[0])
            for i in range(len(pts)-1):
                if pts[i][1] < pts[i+1][1] - 1e-9:
                    monotonic_ok = False
                    break
            if not monotonic_ok:
                break
        bonus = 1.0 if monotonic_ok else 0.0
        return field_score * 0.9 + bonus * 0.1


_SCORERS = {
    'step03_compute_results': score_0,
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
