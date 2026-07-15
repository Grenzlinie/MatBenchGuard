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


# === block: score_0 (check id='check_results') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            if not isinstance(artifact, list):
                return 0.0
            entries = {}
            for obj in artifact:
                key = (obj.get('metal'), obj.get('face'))
                entries[key] = obj
            gold = step.get('gold_values', {})
            tol_h = gold.get('tolerance_hbonds', 0.05)
            tol_angle = gold.get('tolerance_angle', 5.0)
            droplet_metals = ['Pd', 'Pt', 'Al']
            metals = ['Ni','Cu','Pd','Pt','Al','Au','Ag','Pb']
            total = 0
            passed = 0

            # Compute trend_threshold dynamically from droplet within values if available
            within_values_droplet = gold.get('paper_within_100_droplet', {})
            if within_values_droplet:
                trend_th = min(within_values_droplet.values()) - 0.001
            else:
                trend_th = gold.get('trend_threshold', 3.0)
            trend_second_max = gold.get('trend_second_max', 0.6)
            trend_diff = gold.get('trend_diff', 0.5)

            # Paper second_layer (100) values
            second_values = gold.get('paper_second_layer_100', {})
            for metal, expected in second_values.items():
                key = (metal, '100')
                if key in entries:
                    total += 1
                    val = entries[key].get('monolayer_second_layer_Hbonds')
                    if val is not None and isinstance(val, (int, float)) and abs(val - expected) <= tol_h:
                        passed += 1

            # Paper within_monolayer for droplet metals on (100)
            for metal, expected in within_values_droplet.items():
                key = (metal, '100')
                if key in entries:
                    total += 1
                    val = entries[key].get('within_monolayer_Hbonds')
                    if val is not None and isinstance(val, (int, float)) and abs(val - expected) <= tol_h:
                        passed += 1

            # Contact angle for droplet metals
            contact_values = gold.get('paper_contact_angle', {})
            for metal, expected in contact_values.items():
                key = (metal, '100')
                if key in entries:
                    total += 1
                    val = entries[key].get('contact_angle')
                    if val is not None and isinstance(val, (int, float)) and abs(val - expected) <= tol_angle:
                        passed += 1

            # Trend: droplet metals must have within >= trend_th and second <= trend_second_max
            for metal in droplet_metals:
                key = (metal, '100')
                if key in entries:
                    w = entries[key].get('within_monolayer_Hbonds')
                    s = entries[key].get('monolayer_second_layer_Hbonds')
                    if w is not None and isinstance(w, (int, float)):
                        total += 1
                        if w >= trend_th:
                            passed += 1
                    if s is not None and isinstance(s, (int, float)):
                        total += 1
                        if s <= trend_second_max:
                            passed += 1

            # Trend: non-droplet (100) metals must have within < trend_th OR second > trend_second_max
            non_droplet = [m for m in metals if m not in droplet_metals]
            for metal in non_droplet:
                key = (metal, '100')
                if key in entries:
                    total += 1
                    w = entries[key].get('within_monolayer_Hbonds')
                    s = entries[key].get('monolayer_second_layer_Hbonds')
                    if w is not None and isinstance(w, (int, float)) and s is not None and isinstance(s, (int, float)):
                        if w < trend_th or s > trend_second_max:
                            passed += 1

            # Trend: (110) and (111) within must be less than (100) within - trend_diff
            for metal in metals:
                key100 = (metal, '100')
                if key100 not in entries:
                    continue
                w100 = entries[key100].get('within_monolayer_Hbonds')
                if w100 is None or not isinstance(w100, (int, float)):
                    continue
                for face in ['110', '111']:
                    key = (metal, face)
                    if key in entries:
                        total += 1
                        w = entries[key].get('within_monolayer_Hbonds')
                        if w is not None and isinstance(w, (int, float)) and w <= w100 - trend_diff:
                            passed += 1

            # Check that contact_angle is null for all non-droplet cases (all faces except droplet (100))
            for metal in metals:
                for face in ['100','110','111']:
                    if metal in droplet_metals and face == '100':
                        continue
                    key = (metal, face)
                    if key in entries:
                        total += 1
                        ca = entries[key].get('contact_angle')
                        if ca is None:
                            passed += 1

            if total == 0:
                return 0.0
            return passed / total
        except Exception:
            return 0.0


_SCORERS = {
    'check_results': score_0,
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
