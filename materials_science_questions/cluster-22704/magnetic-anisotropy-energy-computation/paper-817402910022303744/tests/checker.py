import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='mae_check') ===
def score_0(artifact, step, ctx):
        gold = step['details']['gold_values']
        tol = step['details']['tol_absolute']
        # build lookup from artifact rows
        reported = {}
        for row in artifact:
            sys = row.get('system', '').strip()
            try:
                mae = float(row['MAE_MJpm3'])
            except (KeyError, ValueError):
                continue
            reported[sys] = mae

        # 1. absolute tolerance per system
        sys_names = gold.keys()
        sys_scores = []
        for sys in sys_names:
            if sys not in reported:
                sys_scores.append(0.0)
                continue
            diff = abs(reported[sys] - gold[sys])
            # full credit if within tol, zero otherwise
            sys_scores.append(1.0 if diff <= tol else 0.0)
        avg_sys = sum(sys_scores) / max(len(sys_scores), 1)

        # 2. monotonic decrease along Co series
        co_order = ['Fe5PB2','Fe0.8Co0.2','Fe0.6Co0.4','Fe0.4Co0.6','Fe0.2Co0.8','Co5PB2']
        trend_ok = True
        for i in range(len(co_order)-1):
            sys_a, sys_b = co_order[i], co_order[i+1]
            if sys_a not in reported or sys_b not in reported:
                trend_ok = False
                break
            if reported[sys_b] > reported[sys_a] + tol:  # allow a small upward fluctuation
                trend_ok = False
                break
        trend_score = 1.0 if trend_ok else 0.0

        # 3. doping enhancement (doped MAE must be >= gold_undoped + min_enh)
        undoped_gold = gold['Fe5PB2']
        min_enh = step['details']['doping_enhancement_min']
        doped_ok = True
        for sys in ['Fe0.95W0.05', 'Fe0.95Re0.05']:
            if sys not in reported:
                doped_ok = False
                break
            if reported[sys] < undoped_gold + min_enh:
                doped_ok = False
                break
        doping_score = 1.0 if doped_ok else 0.0

        # weighted total
        w_sys = step['details']['weight_systems']
        w_trend = step['details']['weight_trend']
        w_doping = step['details']['weight_doping']
        total = w_sys * avg_sys + w_trend * trend_score + w_doping * doping_score
        # ensure return is a float [0,1]
        total = max(0.0, min(1.0, total))
        return total


_SCORERS = {
    'mae_check': score_0,
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
