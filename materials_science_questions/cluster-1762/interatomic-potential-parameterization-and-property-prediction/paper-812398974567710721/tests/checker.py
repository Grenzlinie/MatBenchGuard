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
    for step in spec.get('steps', []):
        if 'hidden_gold' in step:
            ctx[step['id']] = step['hidden_gold']
    return ctx


# === block: score_0 (check id='step_fig4') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        hidden = ctx[step['id']]
        tol = hidden.get('barrier_tolerance_ev', 0.01)
        target = hidden.get('barrier_expected_ev', 0.0571)
        cond = hidden.get('barrier_condition', {})

        rows = artifact
        if not rows:
            return 0.0

        def _float(v):
            if v is None or v == '':
                return 0.0
            try:
                return float(v)
            except (ValueError, TypeError):
                return 0.0

        total = len(rows)

        # non‑negative check
        nonneg = sum(1 for r in rows if _float(r.get('relative_energy_eV')) >= -1e-6)
        nonneg_score = nonneg / total

        # zero‑in‑group check
        groups = {}
        for r in rows:
            key = (r.get('face',''), r.get('mo_location',''))
            groups.setdefault(key, []).append(_float(r.get('relative_energy_eV')))
        zero_groups = sum(1 for vals in groups.values() if any(v <= 1e-5 for v in vals))
        total_groups = max(1, len(groups))
        zero_score = zero_groups / total_groups

        # barrier check
        barrier_score = 0.0
        for r in rows:
            if (r.get('face') == cond.get('face') and
                r.get('mo_location') == cond.get('mo_location') and
                r.get('al_proximity') == cond.get('al_proximity')):
                val = _float(r.get('relative_energy_eV'))
                diff = abs(val - target)
                if diff <= tol:
                    barrier_score = 1.0
                else:
                    barrier_score = max(0.0, 1.0 - (diff - tol) / tol)
                break

        return 0.2 * zero_score + 0.3 * nonneg_score + 0.5 * barrier_score


# === block: score_1 (check id='step_fig5') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        total = len(rows)

        # reference row (1, O) must be ~0
        ref_found = False
        for r in rows:
            if str(r.get('row_number','')).strip() == '1' and r.get('column_label','').strip() == 'O':
                if float(r.get('relative_energy_eV', 0)) <= 1e-5:
                    ref_found = True
                break
        ref_score = 1.0 if ref_found else 0.0

        # trend: for rows 2‑5, subsurface (1b) energy > overlayer (O) energy
        passes = 0
        for rn in range(2, 6):
            rn_str = str(rn)
            o_val = None
            ib_val = None
            for r in rows:
                if str(r.get('row_number','')).strip() == rn_str:
                    col = r.get('column_label','').strip()
                    if col == 'O':
                        o_val = float(r.get('relative_energy_eV', 0))
                    elif col == '1b':
                        ib_val = float(r.get('relative_energy_eV', 0))
            if o_val is not None and ib_val is not None and (ib_val - o_val) > 1e-8:
                passes += 1
        trend_score = passes / 4.0 if passes >= 0 else 0.0

        # non‑negative check
        nonneg = sum(1 for r in rows if float(r.get('relative_energy_eV', 0)) >= -1e-6)
        nonneg_score = nonneg / total if total > 0 else 0.0

        return 0.4 * ref_score + 0.4 * trend_score + 0.2 * nonneg_score


_SCORERS = {
    'step_fig4': score_0,
    'step_fig5': score_1,
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
