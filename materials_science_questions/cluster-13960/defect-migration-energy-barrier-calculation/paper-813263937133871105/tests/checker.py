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


# === block: score_0 (check id='compile_csv') ===
def score_0(artifact, step, ctx):
        params = step.get('params', {})
        gold = params.get('gold_values', {})
        C2_paper = params.get('C2_paper', 7.81)
        weights = params.get('sub_weights', {})
        w_def_fe = weights.get('def_fe', 0.1)
        w_mag = weights.get('mag', 0.02)
        w_bar_fe = weights.get('bar_fe', 0.04)
        w_bar_empty = weights.get('bar_mag_empty', 0.01)
        w_C3ltC1 = weights.get('trend_C3_lt_C1', 0.02)
        w_N1ltB1 = weights.get('trend_N1_lt_B1', 0.02)
        w_CC1ltC1plusC2 = weights.get('trend_CC1_lt_C1plusC2', 0.03)
        w_mig_le = weights.get('threshold_mig_le_2', 0.02)
        w_SWform_ge = weights.get('threshold_SWform_ge_5', 0.02)
        w_SWheal_le = weights.get('threshold_SWheal_le_2', 0.02)

        if not isinstance(artifact, list):
            return 0.0

        rows_by_defect = {}
        for row in artifact:
            label = row.get('defect', '').strip()
            fe_str = row.get('formation_energy', '').strip()
            mm_str = row.get('total_magnetic_moment', '').strip()
            fe = float(fe_str) if fe_str != '' else None
            mm = float(mm_str) if mm_str != '' else None
            rows_by_defect[label] = (fe, mm)

        total = 0.0

        for label in ['C1','C3','N1','B1','C5','CC1']:
            entry = gold.get(label)
            if entry is None:
                continue
            if label in rows_by_defect:
                fe_agent, mm_agent = rows_by_defect[label]
                if fe_agent is not None:
                    tol = entry.get('tol_fe', 0.3)
                    if abs(fe_agent - entry['formation_energy']) <= tol:
                        total += w_def_fe
                if mm_agent is not None and 'total_magnetic_moment' in entry:
                    if abs(mm_agent - entry['total_magnetic_moment']) <= 0.5:
                        total += w_mag

        for label in ['C1_N1','SW1N_formation','SW1N_healing']:
            entry = gold.get(label)
            if entry is None:
                continue
            if label in rows_by_defect:
                fe_agent, mm_agent = rows_by_defect[label]
                if fe_agent is not None:
                    tol = entry.get('tol_fe', 0.5)
                    if abs(fe_agent - entry['formation_energy']) <= tol:
                        total += w_bar_fe
                if mm_agent is None:
                    total += w_bar_empty

        if 'C3' in rows_by_defect and 'C1' in rows_by_defect:
            fe_C3 = rows_by_defect['C3'][0]
            fe_C1 = rows_by_defect['C1'][0]
            if fe_C3 is not None and fe_C1 is not None and fe_C3 < fe_C1:
                total += w_C3ltC1

        if 'N1' in rows_by_defect and 'B1' in rows_by_defect:
            fe_N1 = rows_by_defect['N1'][0]
            fe_B1 = rows_by_defect['B1'][0]
            if fe_N1 is not None and fe_B1 is not None and fe_N1 < fe_B1:
                total += w_N1ltB1

        if 'CC1' in rows_by_defect and 'C1' in rows_by_defect:
            fe_CC1 = rows_by_defect['CC1'][0]
            fe_C1 = rows_by_defect['C1'][0]
            if fe_CC1 is not None and fe_C1 is not None:
                if fe_CC1 < fe_C1 + C2_paper:
                    total += w_CC1ltC1plusC2

        if 'C1_N1' in rows_by_defect:
            fe_mig = rows_by_defect['C1_N1'][0]
            if fe_mig is not None and fe_mig <= 2.0:
                total += w_mig_le

        if 'SW1N_formation' in rows_by_defect:
            fe_swf = rows_by_defect['SW1N_formation'][0]
            if fe_swf is not None and fe_swf >= 5.0:
                total += w_SWform_ge

        if 'SW1N_healing' in rows_by_defect:
            fe_swh = rows_by_defect['SW1N_healing'][0]
            if fe_swh is not None and fe_swh <= 2.0:
                total += w_SWheal_le

        return min(total, 1.0)


_SCORERS = {
    'compile_csv': score_0,
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
