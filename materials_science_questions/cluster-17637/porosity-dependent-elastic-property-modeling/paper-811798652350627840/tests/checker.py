import os
import json
import csv

# === author imports / helpers ===
import csv, math
from collections import defaultdict


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
    import json
    with open('/tests/grading_spec.json') as f:
        spec = json.load(f)
    steps = spec.get('steps', [])
    step = steps[0] if steps else {}
    gold_points = step.get('gold', {}).get('points', [])
    return {'gold_points': gold_points}


# === block: score_0 (check id='step_epi_pred') ===
def score_0(artifact, step, ctx):
    import csv, math
    from collections import defaultdict

    rows = artifact if artifact else []
    def parse_row(r):
        try:
            return {k: float(r[k]) if k != 'case_id' else r[k] for k in r}
        except (ValueError, TypeError):
            return None
    rows = [parse_row(r) for r in rows]
    rows = [r for r in rows if r is not None]
    if not rows:
        return 0.0

    def rel_err(ref, val):
        if abs(ref) < 1e-12:
            return abs(val)
        return abs(val - ref) / abs(ref)

    def score_point(ref, val, tol):
        if ref is None or val is None:
            return None
        err = rel_err(ref, val)
        if err <= tol:
            return 1.0
        elif err >= 2*tol:
            return 0.0
        else:
            return 1.0 - (err - tol) / tol

    gold_points = ctx.get('gold_points', [])

    # Build lookup by (porosity, particle, k1, k2) -> row
    lookup = {}
    for r in rows:
        key = (round(r['porosity_alpha_p'], 6), round(r['particle_alpha_s'], 6), round(r['k1'], 6), round(r['k2'], 6))
        lookup[key] = r

    E_scores = []
    G_scores = []
    for gp in gold_points:
        key = (gp['porosity'], gp['particle'], gp['k1'], gp['k2'])
        row = lookup.get(key)
        if row is None:
            E_scores.append(0.0)
            if gp.get('G_ref') is not None:
                G_scores.append(0.0)
            continue
        e = row.get('E_GPa')
        g = row.get('G_GPa')
        es = score_point(gp.get('E_ref'), e, gp.get('tol_E', 0.1))
        if es is not None:
            E_scores.append(es)
        gs = score_point(gp.get('G_ref'), g, gp.get('tol_G', 0.1))
        if gs is not None:
            G_scores.append(gs)

    E_score = sum(E_scores) / len(E_scores) if E_scores else 1.0
    G_score = sum(G_scores) / len(G_scores) if G_scores else 1.0

    # Structural checks
    struct_score = 1.0
    checks = []
    # 1) Spherical porous monotonic decrease
    porous_rows = [r for r in rows if r['k1'] == 1.0 and r['k2'] == 1.0 and r['particle_alpha_s'] == 0.0 and r['porosity_alpha_p'] > 0]
    porous_rows.sort(key=lambda r: r['porosity_alpha_p'])
    mono_ok = all(porous_rows[i]['E_GPa'] >= porous_rows[i+1]['E_GPa'] - 1e-9 for i in range(len(porous_rows)-1))
    checks.append(1.0 if mono_ok else 0.0)

    # 2) Dense spherical monotonic increase
    dense_rows = [r for r in rows if r['k1'] == 1.0 and r['k2'] == 1.0 and r['porosity_alpha_p'] == 0.0 and r['particle_alpha_s'] >= 0]
    dense_rows.sort(key=lambda r: r['particle_alpha_s'])
    dense_ok = all(dense_rows[i]['E_GPa'] <= dense_rows[i+1]['E_GPa'] + 1e-9 for i in range(len(dense_rows)-1))
    checks.append(1.0 if dense_ok else 0.0)

    # 3) Oblate > spherical at alpha_s=0.1, alpha_p=0.6
    spherical_row = lookup.get((0.6, 0.1, 1.0, 1.0))
    oblate_row = lookup.get((0.6, 0.1, 1000.0, 1000.0))
    if spherical_row and oblate_row:
        enhance_ok = oblate_row['E_GPa'] > spherical_row['E_GPa']
        checks.append(1.0 if enhance_ok else 0.0)
    else:
        checks.append(0.0)

    struct_score = sum(checks) / len(checks) if checks else 1.0

    # Combine weights
    w_E, w_G, w_struct = 0.7, 0.2, 0.1
    # Adjust if G not scored
    if not G_scores:
        w_E = 0.8
        w_G = 0.0
        w_struct = 0.2
    return w_E * E_score + w_G * G_score + w_struct * struct_score


_SCORERS = {
    'step_epi_pred': score_0,
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
