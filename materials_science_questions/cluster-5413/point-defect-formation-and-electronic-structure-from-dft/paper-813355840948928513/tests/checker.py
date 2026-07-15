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


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import json
        def _safe_float(v):
            try:
                return float(v)
            except (ValueError, TypeError):
                return None
        if not isinstance(artifact, dict):
            return 0.0
        anhydrous = _safe_float(artifact.get('anhydrous_band_gap'))
        free = artifact.get('free_proton_band_gaps')
        if not isinstance(free, dict):
            free = {}
        gold = step.get('gold', {}) if isinstance(step, dict) else {}
        anhydrous_gold_entry = gold.get('anhydrous_band_gap')
        if not isinstance(anhydrous_gold_entry, dict):
            anhydrous_gold_entry = {}
        fp_gold_entry = gold.get('free_proton_band_gaps')
        if not isinstance(fp_gold_entry, dict):
            fp_gold_entry = {}
        tol_an = _safe_float(anhydrous_gold_entry.get('tolerance_abs', 0.2))
        if tol_an is None:
            tol_an = 0.2
        tol_fp = 0.2
        an_pass = 0
        gold_val = _safe_float(anhydrous_gold_entry.get('value'))
        if anhydrous is not None and gold_val is not None:
            if abs(anhydrous - gold_val) <= tol_an:
                an_pass = 1
        fp_pass = {'[100]': 0, '[010]': 0, '[001]': 0}
        for key in ['[100]', '[010]', '[001]']:
            val = _safe_float(free.get(key))
            if val is not None:
                entry = fp_gold_entry.get(key)
                if isinstance(entry, dict):
                    gold_val_fp = _safe_float(entry.get('value'))
                    if gold_val_fp is not None:
                        tol = _safe_float(entry.get('tolerance_abs', tol_fp))
                        if tol is None:
                            tol = tol_fp
                        if abs(val - gold_val_fp) <= tol:
                            fp_pass[key] = 1
        order_pass = 0
        if all(fp_pass.values()):
            val001 = _safe_float(free.get('[001]'))
            val100 = _safe_float(free.get('[100]'))
            val010 = _safe_float(free.get('[010]'))
            if None not in (val001, val100, val010):
                if val001 < val100 and val001 < val010:
                    order_pass = 1
        abs_weight = 0.95
        per_abs_weight = abs_weight / 4.0
        order_weight = 0.05
        total = an_pass * per_abs_weight + sum(fp_pass.values()) * per_abs_weight + order_pass * order_weight
        return min(max(total, 0.0), 1.0)


_SCORERS = {
    's1': score_0,
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
