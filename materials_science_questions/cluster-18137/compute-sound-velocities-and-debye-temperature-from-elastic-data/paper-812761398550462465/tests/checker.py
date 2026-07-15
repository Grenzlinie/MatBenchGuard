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


# === block: score_0 (check id='value_check') ===
def score_0(artifact, step, ctx):
    def _to_float(val, default=None):
        try:
            return float(val)
        except (TypeError, ValueError):
            return default

    gold_rows = step.get('gold_rows', [])
    tol = step.get('tolerance_pcts', {})
    numeric_fields = ['a0_A','c0_A','C11_GPa','C33_GPa','C44_GPa','C12_GPa','C13_GPa','B_GPa','G_GPa','E_GPa','sigma','G_B_ratio','vt_ms','vl_ms','vm_ms','ThetaD_K']
    gold_by_sys = {r['system']: r for r in gold_rows}
    total, passed = 0, 0
    for row in artifact:
        sys = row.get('system')
        if sys not in gold_by_sys:
            continue
        g = gold_by_sys[sys]
        for field in numeric_fields:
            gv = _to_float(g.get(field))
            av = _to_float(row.get(field))
            if gv is None or av is None:
                total += 1
                continue
            t = tol.get(field, {})
            if isinstance(t, dict) and 'abs' in t:
                ok = abs(av - gv) <= float(t['abs']) + 1e-9
            else:
                pct = float(t.get('pct', 10))
                if abs(gv) < 1e-9:
                    ok = abs(av - gv) <= 0.01
                else:
                    ok = abs(av - gv) / abs(gv) <= pct / 100.0 + 1e-9
            total += 1
            if ok:
                passed += 1
    score = passed / total if total else 0.0


# === block: score_1 (check id='trend_check') ===
def score_1(artifact, step, ctx):
    pristine = {}
    for row in artifact:
        if row.get('doping_type') == 'none':
            pristine[row['host']] = row
    if 'TAC' not in pristine or 'TSC' not in pristine:
        score = 0.0
    else:
        checks = []
        for row in artifact:
            dt = row.get('doping_type')
            host = row.get('host')
            if dt == 'substitutional_Ti1':
                pref = pristine[host]
                for mod in ['B_GPa','G_GPa','E_GPa']:
                    pv = float(pref[mod])
                    rv = float(row[mod])
                    checks.append(abs(rv - pv) <= 0.10 * pv + 1e-9)
            elif dt == 'interstitial_c-ATi2':
                pref = pristine[host]
                for mod in ['B_GPa','G_GPa','E_GPa']:
                    pv = float(pref[mod])
                    rv = float(row[mod])
                    checks.append(rv <= pv + 1e-9)
        # magnetic moment checks
        for row in artifact:
            sys = row.get('system')
            mag = float(row.get('Mag_muB', 0))
            if row.get('doping_type') == 'interstitial_c-ATi2' and sys in ['Hfi_TAC', 'Zri_TAC']:
                checks.append(mag > 0.5)
            elif row.get('doping_type') == 'interstitial_c-ATi2':
                checks.append(mag < 0.1)
            else:
                checks.append(mag < 0.1)
        score = sum(1 for c in checks if c) / len(checks) if checks else 0.0


_SCORERS = {
    'value_check': score_0,
    'trend_check': score_1,
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
