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
    import json
    ref_data = spec.get('reference_data', {})
    table = ref_data.get('table', {})
    tol_abs = ref_data['tolerances']['absorption_edge_eV']
    tol_peak = ref_data['tolerances']['first_strong_peak_eV']
    min_diff = ref_data['trend_min_diff']
    trends = ref_data['trend_configs']
    return {'table': table, 'tol_abs': tol_abs, 'tol_peak': tol_peak, 'min_diff': min_diff, 'trends': trends}


# === block: score_0 (check id='optical_conductivity') ===
def score_0(artifact, step, ctx):
    rows = {}
    try:
        for row in artifact:
            cfg = row.get('configuration', '').strip().lower()
            if cfg:
                try:
                    edge = float(row['absorption_edge_eV'])
                    peak = float(row['first_strong_peak_eV'])
                    rows[cfg] = {'abs_edge': edge, 'peak': peak}
                except (ValueError, KeyError):
                    pass
    except Exception:
        return 0.0
    ref = ctx['table']
    tol_abs = ctx['tol_abs']
    tol_peak = ctx['tol_peak']
    min_diff = ctx['min_diff']
    trends = ctx['trends']
    # value accuracy (8 entries, each 0.05)
    value_score = 0.0
    for cfg, gold in ref.items():
        if cfg in rows:
            if abs(rows[cfg]['abs_edge'] - gold['absorption_edge_eV']) <= tol_abs and abs(rows[cfg]['peak'] - gold['first_strong_peak_eV']) <= tol_peak:
                value_score += 0.05
    value_score = min(value_score, 0.4)
    # trend 1: absorption edge of vac_co > no_vac by >= min_diff
    trend1 = 0.0
    no_vac_cfg = trends['no_vac_config']
    vac_co_cfg = trends['vac_co_config']
    if no_vac_cfg in rows and vac_co_cfg in rows:
        if rows[vac_co_cfg]['abs_edge'] - rows[no_vac_cfg]['abs_edge'] >= min_diff:
            trend1 = 0.3
    # trend 2: first strong peak of vac_ti < vac_co by >= min_diff
    trend2 = 0.0
    vac_ti_cfg = trends['vac_ti_config']
    if vac_ti_cfg in rows and vac_co_cfg in rows:
        if rows[vac_co_cfg]['peak'] - rows[vac_ti_cfg]['peak'] >= min_diff:
            trend2 = 0.3
    return value_score + trend1 + trend2


_SCORERS = {
    'optical_conductivity': score_0,
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
