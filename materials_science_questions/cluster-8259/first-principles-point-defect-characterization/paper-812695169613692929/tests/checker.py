import os
import json
import csv

# === author imports / helpers ===
def field_score(value, gold, tol):
    if value is None:
        return 0.0
    diff = abs(value - gold)
    if diff <= tol:
        return 1.0
    rel = diff / max(abs(gold), 1e-6)
    return max(0.0, 1.0 - (diff - tol) / (tol + abs(gold) * 0.5))


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


# === block: score_0 (check id='properties_check') ===
def score_0(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold_list = step['config']['gold']
        tolerances = step['config']['tolerances']
        gold_map = {g['defect']: g for g in gold_list}
        if not isinstance(artifact, list):
            return 0.0
        agent_map = {}
        for entry in artifact:
            if not isinstance(entry, dict):
                continue
            d = entry.get('defect')
            if d in gold_map:
                agent_map[d] = entry
        scores = []
        for d, gold in gold_map.items():
            ag = agent_map.get(d)
            if ag is None:
                scores.append(0.0)
                continue
            fe_score = field_score(ag.get('formation_energy'), gold['formation_energy'], tolerances['formation_energy'])
            bg_score = field_score(ag.get('band_gap'), gold['band_gap'], tolerances['band_gap'])
            mm_score = field_score(ag.get('magnetic_moment'), gold['magnetic_moment'], tolerances['magnetic_moment'])
            scores.append((fe_score + bg_score + mm_score) / 3.0)
        main_score = sum(scores) / len(scores) if scores else 0.0

        def get_fe(name):
            entry = agent_map.get(name)
            return entry['formation_energy'] if entry and 'formation_energy' in entry else None
        sw_fe = [v for v in (get_fe('SW(55|77)-1'), get_fe('SW(55|77)-2')) if v is not None]
        sv_fe = get_fe('SV(5|9)')
        dv_fe = [v for v in (get_fe('DV(5|8|5)-1'), get_fe('DV(555|777)'), get_fe('DV(5555|6|7777)'), get_fe('DV(5|8|5)-2')) if v is not None]
        order_ok = True
        if sv_fe is not None:
            for fe in sw_fe:
                if fe > sv_fe:
                    order_ok = False
            for fe in dv_fe:
                if sv_fe > fe:
                    order_ok = False
        order_score = 1.0 if order_ok else 0.0

        mag_ok = True
        for d in gold_map:
            if d in ('pristine', 'SV(5|9)'):
                continue
            entry = agent_map.get(d)
            if entry and 'magnetic_moment' in entry:
                if abs(entry['magnetic_moment']) > 1e-6:
                    mag_ok = False
        mag_score = 1.0 if mag_ok else 0.0

        return round(main_score * 0.7 + order_score * 0.15 + mag_score * 0.15, 6)


# === block: score_1 (check id='currents_check') ===
def score_1(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold_list = step['config']['gold']
        tol = step['config']['tolerances']['current']
        gold_map = {g['defect']: g for g in gold_list}
        if not isinstance(artifact, list):
            return 0.0
        agent_map = {}
        for entry in artifact:
            if not isinstance(entry, dict):
                continue
            d = entry.get('defect')
            if d in gold_map:
                agent_map[d] = entry
        scores = []
        for d, gold in gold_map.items():
            ag = agent_map.get(d)
            if ag is None:
                scores.append(0.0)
                continue
            zz_score = field_score(ag.get('current_zigzag'), gold['current_zigzag'], tol)
            ac_score = field_score(ag.get('current_armchair'), gold['current_armchair'], tol)
            scores.append((zz_score + ac_score) / 2.0)
        return round(sum(scores) / len(scores), 6) if scores else 0.0


_SCORERS = {
    'properties_check': score_0,
    'currents_check': score_1,
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
