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
    import os, csv

    gold = spec.get('gold_moduli', {})
    fp = os.path.join(outputs_dir, 'axial_moduli_predictions.csv')
    if not os.path.exists(fp):
        return {'mape_mt': float('inf'), 'mape_sc': float('inf'), 'mape_ht': float('inf')}
    try:
        with open(fp, newline='') as f:
            rows = list(csv.DictReader(f))
    except Exception:
        return {'mape_mt': float('inf'), 'mape_sc': float('inf'), 'mape_ht': float('inf')}
    sys_rows = {}
    for row in rows:
        sys_rows[row.get('system', '').strip()] = row
    errors = {'mt': [], 'sc': [], 'ht': []}
    for sys_name, gold_val in gold.items():
        if sys_name not in sys_rows:
            return {'mape_mt': float('inf'), 'mape_sc': float('inf'), 'mape_ht': float('inf')}
        row = sys_rows[sys_name]
        try:
            mt = float(row.get('mori_tanaka_E', 'nan'))
            sc = float(row.get('self_consistent_E', 'nan'))
            ht = float(row.get('halpin_tsai_E', 'nan'))
        except ValueError:
            return {'mape_mt': float('inf'), 'mape_sc': float('inf'), 'mape_ht': float('inf')}
        errors['mt'].append(abs(mt - gold_val) / gold_val * 100)
        errors['sc'].append(abs(sc - gold_val) / gold_val * 100)
        errors['ht'].append(abs(ht - gold_val) / gold_val * 100)
    def mean(lst):
        return sum(lst)/len(lst) if lst else float('inf')
    return {
        'mape_mt': mean(errors['mt']),
        'mape_sc': mean(errors['sc']),
        'mape_ht': mean(errors['ht'])
    }


# === block: score_0 (check id='sc_best') ===
def score_0(artifact, step, ctx):
    # Gold reference axial moduli at 0 K from Table 3 (hidden)
    gold = {
        "Sys1": 135.0,
        "Sys2": 101.0,
        "Sys3": 94.5,
        "Sys4": 96.3,
        "Sys5": 65.7,
        "Sys6": 60.3,
        "Sys7": 37.5,
        "Sys8": 40.3
    }
    if artifact is None:
        return 0.0
    # Build lookup by system
    sys_rows = {}
    for row in artifact:
        sys_rows[row.get("system", "").strip()] = row
    errors = {"mt": [], "sc": [], "ht": []}
    for sys_name, gold_val in gold.items():
        if sys_name not in sys_rows:
            return 0.0
        row = sys_rows[sys_name]
        try:
            mt = float(row.get("mori_tanaka_E", "nan"))
            sc = float(row.get("self_consistent_E", "nan"))
            ht = float(row.get("halpin_tsai_E", "nan"))
        except (ValueError, TypeError):
            return 0.0
        errors["mt"].append(abs(mt - gold_val) / gold_val * 100)
        errors["sc"].append(abs(sc - gold_val) / gold_val * 100)
        errors["ht"].append(abs(ht - gold_val) / gold_val * 100)

    def safe_mean(lst):
        return sum(lst) / len(lst) if lst else float("inf")

    mape_mt = safe_mean(errors["mt"])
    mape_sc = safe_mean(errors["sc"])
    mape_ht = safe_mean(errors["ht"])

    if mape_sc < mape_mt and mape_sc < mape_ht:
        return 1.0
    elif mape_sc < mape_mt or mape_sc < mape_ht:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='ht_better_than_mt') ===
def score_1(artifact, step, ctx):
    mape_ht = ctx.get('mape_ht', float('inf'))
    mape_mt = ctx.get('mape_mt', float('inf'))
    if mape_ht < mape_mt:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'sc_best': score_0,
    'ht_better_than_mt': score_1,
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
