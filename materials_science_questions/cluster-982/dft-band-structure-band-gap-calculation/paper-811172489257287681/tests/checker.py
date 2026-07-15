import os
import json
import csv

# === author imports / helpers ===
import csv, collections


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
    for s in spec.get('steps', []):
        ctx[s['id']] = s.get('thresholds', {})
    return ctx


# === block: score_0 (check id='kappa_audit') ===
def score_0(artifact, step, ctx):
    def score(rows, step, ctx):
        kappa_max = float(step.get('thresholds', {}).get('kappa_max', 5.0))
        targets = {'ZrSe2': None, 'HfSe2': None}
        for row in rows:
            mat = str(row.get('material', '')).strip()
            try:
                temp = float(row.get('temperature_K', 0.0))
            except (TypeError, ValueError):
                continue
            if temp == 300.0 and mat in targets:
                try:
                    targets[mat] = float(row.get('kappa_l_W_mK', None))
                except (TypeError, ValueError):
                    continue
        if targets['ZrSe2'] is None or targets['HfSe2'] is None:
            return 0.0
        c1 = targets['ZrSe2'] < kappa_max
        c2 = targets['HfSe2'] < kappa_max
        c3 = targets['ZrSe2'] < targets['HfSe2']
        return (c1 + c2 + c3) / 3.0


# === block: score_1 (check id='ZT_audit') ===
def score_1(artifact, step, ctx):
    def score(rows, step, ctx):
        ZT_min = float(step.get('thresholds', {}).get('ZT_min', 0.5))
        max_zt = collections.defaultdict(float)
        for row in rows:
            mat = str(row.get('material', '')).strip()
            ctype = str(row.get('carrier_type', '')).strip()
            try:
                zt = float(row.get('ZT', 0.0))
            except (TypeError, ValueError):
                continue
            key = (mat, ctype)
            if zt > max_zt[key]:
                max_zt[key] = zt
        conditions_passed = 0
        total_conditions = 0
        for mat in ['ZrSe2', 'HfSe2']:
            for ctype in ['p-type', 'n-type']:
                key = (mat, ctype)
                if key in max_zt:
                    total_conditions += 1
                    if max_zt[key] > ZT_min:
                        conditions_passed += 1
        for mat in ['ZrSe2', 'HfSe2']:
            key_p = (mat, 'p-type')
            key_n = (mat, 'n-type')
            if key_p in max_zt and key_n in max_zt:
                total_conditions += 1
                if max_zt[key_n] > max_zt[key_p]:
                    conditions_passed += 1
        if total_conditions == 0:
            return 0.0
        return conditions_passed / total_conditions


_SCORERS = {
    'kappa_audit': score_0,
    'ZT_audit': score_1,
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
