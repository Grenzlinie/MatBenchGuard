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


# === block: score_0 (check id='step_02_large_u_phase_boundaries') ===
def score_0(artifact, step, ctx):
    artifact_dict = artifact  # already loaded as dict from json
    if not isinstance(artifact_dict, dict):
        return 0.0
    pcoi_val = artifact_dict.get('PCOI_to_DMI_Vp_over_tb1')
    dmi_val = artifact_dict.get('DMI_to_PCOI_prime_Vp_over_tb1')
    if pcoi_val is None or dmi_val is None:
        return 0.0
    exp_pcoi = step.get('expected_PCOI_to_DMI_Vp', 1.3)
    exp_dmi = step.get('expected_DMI_to_PCOI_prime_Vp', 1.7)
    tol = step.get('tolerance', 0.1)
    diff1 = abs(pcoi_val - exp_pcoi)
    diff2 = abs(dmi_val - exp_dmi)
    score1 = 1.0 if diff1 <= tol else 0.0
    score2 = 1.0 if diff2 <= tol else 0.0
    return 0.5 * score1 + 0.5 * score2


# === block: score_1 (check id='step_03_charge_structure_factors') ===
def score_1(artifact, step, ctx):
    artifact_dict = artifact
    if not isinstance(artifact_dict, dict):
        return 0.0
    high = step.get('high_threshold', 0.5)
    low = step.get('low_threshold', 0.2)
    phases = ['PCOI', 'PCOI_prime', 'NPCOI', 'DMI']
    conditions = {
        'PCOI':   [('N_CD_qpipi', '>', high), ('N_CD_q00', '<', low), ('N_qpipi', '<', low)],
        'PCOI_prime': [('N_CD_q00', '>', high), ('N_CD_qpipi', '<', low), ('N_qpipi', '<', low)],
        'NPCOI':  [('N_qpipi', '>', high), ('N_CD_q00', '<', low), ('N_CD_qpipi', '<', low)],
        'DMI':    [('N_CD_q00', '<', low), ('N_CD_qpipi', '<', low), ('N_qpipi', '<', low)]
    }
    passed = 0
    for ph in phases:
        data = artifact_dict.get(ph)
        if not isinstance(data, dict):
            continue
        phase_ok = True
        for field, op, threshold in conditions[ph]:
            val = data.get(field)
            if val is None:
                phase_ok = False
                break
            if op == '>' and not (val > threshold):
                phase_ok = False
                break
            if op == '<' and not (val < threshold):
                phase_ok = False
                break
        if phase_ok:
            passed += 1
    return passed / len(phases)


# === block: score_2 (check id='step_04_com_density_profile') ===
def score_2(artifact, step, ctx):
    rows = artifact   # list of dicts from CSV
    if not isinstance(rows, list) or len(rows) != 12:
        return 0.0
    rich = step.get('rich_indices', [0,1,3,4,6,7,9,10])
    poor = step.get('poor_indices', [2,5,8,11])
    rich_th = step.get('rich_density_threshold', 1.5)
    poor_th = step.get('poor_density_threshold', 1.0)
    sub_map = {}
    for row in rows:
        if 'sublattice' not in row or 'density_c' not in row or 'density_f' not in row:
            return 0.0
        sub = int(row['sublattice'])
        sub_map[sub] = (float(row['density_c']), float(row['density_f']))
    total_checks = 0
    passed_checks = 0
    for i in rich:
        if i not in sub_map:
            return 0.0
        dc, df = sub_map[i]
        total_checks += 2
        if dc > rich_th:
            passed_checks += 1
        if df > rich_th:
            passed_checks += 1
    for i in poor:
        if i not in sub_map:
            return 0.0
        dc, df = sub_map[i]
        total_checks += 2
        if dc < poor_th:
            passed_checks += 1
        if df < poor_th:
            passed_checks += 1
    return passed_checks / total_checks if total_checks > 0 else 0.0


_SCORERS = {
    'step_02_large_u_phase_boundaries': score_0,
    'step_03_charge_structure_factors': score_1,
    'step_04_com_density_profile': score_2,
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
