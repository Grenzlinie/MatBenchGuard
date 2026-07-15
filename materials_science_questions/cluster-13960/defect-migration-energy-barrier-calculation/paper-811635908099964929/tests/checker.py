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


# === block: score_0 (check id='migration_barriers') ===
def score_0(artifact, step, ctx):
    import csv

    def parse_csv_to_dict(artifact):
        """artifact is list of rows; return dict mapping defect_type -> barrier_eV"""
        mapping = {}
        for row in artifact:
            dtype = row.get('defect_type', '').strip()
            try:
                barrier = float(row.get('barrier_eV', ''))
            except (ValueError, TypeError):
                continue
            if dtype:
                mapping[dtype] = barrier
        return mapping

    expected_types = {'V_U', 'V_UO', 'V_UO2', 'V_U2', 'V_U2O'}
    order = ['V_U2', 'V_U2O', 'V_UO', 'V_UO2', 'V_U']  # required increasing order

    mapping = parse_csv_to_dict(artifact)

    # 1. presence of all required types (0.1)
    types_present = expected_types.issubset(mapping.keys())
    score_presence = 1.0 if types_present else 0.0

    # 2. all barriers positive (0.1)
    all_positive = all(v > 0 for v in mapping.values()) if mapping else False
    score_positive = 1.0 if all_positive else 0.0

    # 3. ordering (0.4)
    vals = [mapping.get(t, None) for t in order]
    ordering_ok = all(v is not None for v in vals) and all(vals[i] < vals[i+1] for i in range(len(vals)-1))
    score_order = 1.0 if ordering_ok else 0.0

    # 4. V_U2 within 1.0 eV of 2.4 (0.2)
    v_u2 = mapping.get('V_U2', None)
    v_u2_in_range = (v_u2 is not None) and (1.4 <= v_u2 <= 3.4)
    score_v_u2 = 1.0 if v_u2_in_range else 0.0

    # 5. V_U2O within 1.0 eV of 2.4 (0.2)
    v_u2o = mapping.get('V_U2O', None)
    v_u2o_in_range = (v_u2o is not None) and (1.4 <= v_u2o <= 3.4)
    score_v_u2o = 1.0 if v_u2o_in_range else 0.0

    total = 0.1*score_presence + 0.1*score_positive + 0.4*score_order + 0.2*score_v_u2 + 0.2*score_v_u2o
    return min(1.0, max(0.0, total))


_SCORERS = {
    'migration_barriers': score_0,
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
