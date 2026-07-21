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


# === block: score_0 (check id='elastic_constants_check') ===
def score_0(artifact, step, ctx):
        # defensive: missing/unreadable artifact
        if artifact is None or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        # parse rows safely
        rows = {}
        for r in artifact:
            try:
                mode = r.get('mode', '').strip().lower() if r.get('mode') else ''
                kappa_str = r.get('kappa_K')
                if not mode or kappa_str is None:
                    continue
                rows[mode] = float(kappa_str)
            except (ValueError, TypeError):
                continue
        gold = step['gold']
        tol = gold['tolerance_rel']
        tir_val = rows.get('tir')
        allen_val = rows.get('allen')
        if tir_val is None or allen_val is None:
            return 0.0
        def within(val, target, rel_tol):
            if target == 0:
                return abs(val) < 1e-12
            return abs(val - target) / abs(target) <= rel_tol
        score = 0.0
        if within(tir_val, gold['TIR'], tol):
            score += 0.5
        if within(allen_val, gold['Allen'], tol):
            score += 0.5
        return score


# === block: score_1 (check id='tir_phase_results_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        # locate T=0 row
        t0_rows = [r for r in artifact if float(r['T_K']) == 0.0]
        if not t0_rows:
            t0_rows = sorted(artifact, key=lambda r: float(r['T_K']))[:1]
        if not t0_rows:
            return 0.0
        t0 = t0_rows[0]
        delta0 = float(t0['delta_over_a'])
        Jz0 = float(t0['Jz_avg'])
        delta_score = 1.0
        if gold['delta_t0'] != 0:
            err_ratio = abs(delta0 - gold['delta_t0']) / abs(gold['delta_t0'])
            if err_ratio > gold['tolerance_rel_delta']:
                delta_score = max(0.0, 1.0 - (err_ratio - gold['tolerance_rel_delta']) / (2 * gold['tolerance_rel_delta']))
        Jz_score = 1.0
        Jz_diff = abs(Jz0 - gold['Jz_t0'])
        if Jz_diff > gold['tolerance_abs_Jz']:
            Jz_score = max(0.0, 1.0 - (Jz_diff - gold['tolerance_abs_Jz']) / (2 * gold['tolerance_abs_Jz']))
        # high-T paramagnetic check
        highT_rows = [r for r in artifact if float(r['T_K']) >= 32.0]
        if not highT_rows:
            highT_rows = sorted(artifact, key=lambda r: float(r['T_K']))[-1:]
        delta_high = [float(r['delta_over_a']) for r in highT_rows]
        Jz_high = [float(r['Jz_avg']) for r in highT_rows]
        delta_zero_ok = all(abs(d) < 1e-6 for d in delta_high)
        Jz_zero_ok = all(abs(j) < 1e-6 for j in Jz_high)
        highT_score = (0.5 if delta_zero_ok else 0.0) + (0.5 if Jz_zero_ok else 0.0)
        total = 0.5 * delta_score + 0.3 * Jz_score + 0.2 * highT_score
        return min(max(total, 0.0), 1.0)


_SCORERS = {
    'elastic_constants_check': score_0,
    'tir_phase_results_check': score_1,
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
