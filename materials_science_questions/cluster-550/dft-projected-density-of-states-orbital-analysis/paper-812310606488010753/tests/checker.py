import os
import json
import csv

# === author imports / helpers ===
import math


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
    return {}   # no shared preprocessing needed; gold is accessed per step from spec


# === block: score_0 (check id='step_01_structural') ===
def score_0(artifact, step, ctx):
    import math

    gold_list = step.get('gold', [])
    tolerances = step.get('tolerances', {})
    if not isinstance(artifact, list):
        return 0.0
    gold_map = {g['composition_x']: g for g in gold_list}
    score_sum = 0.0
    count = 0
    for entry in artifact:
        x = entry.get('composition_x')
        if x not in gold_map:
            continue
        g = gold_map[x]
        for field, tol in tolerances.items():
            val = entry.get(field)
            ref = g.get(field)
            if val is None or ref is None:
                continue
            if isinstance(tol, dict):
                if field == 'B0_GPa':
                    rel = tol.get('relative', 0.1)
                    abs_fallback = tol.get('absolute_fallback', 20)
                    if abs(val - ref) <= abs_fallback:
                        ok = True
                    else:
                        if ref != 0:
                            ok = abs(val - ref) / abs(ref) <= rel
                        else:
                            ok = abs(val) < 1e-6
                else:
                    ok = True
            else:
                if tol is not None:
                    ok = abs(val - ref) <= tol
                else:
                    ok = abs(val - ref) <= 1e-6
            if ok:
                score_sum += 1.0
            count += 1
    if count == 0:
        return 0.0
    return min(1.0, score_sum / count)


# === block: score_1 (check id='step_02_electronic') ===
def score_1(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold_list = step.get('gold', [])
        tolerance = step.get('tolerances', {}).get('N_EF_states_per_Ry', 5.0)
        if not isinstance(artifact, list):
            return 0.0
        gold_map = {g['composition_x']: g for g in gold_list}
        total = len(gold_list)
        if total == 0:
            return 0.0
        correct = 0
        for entry in artifact:
            x = entry.get('composition_x')
            if x not in gold_map:
                continue
            ref = gold_map[x].get('N_EF_states_per_Ry')
            val = entry.get('N_EF_states_per_Ry')
            if val is None or ref is None:
                continue
            if abs(val - ref) <= tolerance:
                correct += 1
        return correct / total


# === block: score_2 (check id='step_03_thermal') ===
def score_2(artifact, step, ctx):
    import math

    def check_monotonic(arr, increasing):
        for i in range(len(arr)-1):
            if increasing:
                if arr[i+1] < arr[i] - 1e-9:
                    return False
            else:
                if arr[i+1] > arr[i] + 1e-9:
                    return False
        return True

    def score(artifact, step, ctx):
        gold_obj = step.get('gold', {})
        gold_comps = gold_obj.get('compositions', [])
        tolerances = step.get('tolerances', {})
        if not isinstance(artifact, dict) or 'compositions' not in artifact:
            return 0.0
        agent_comps = artifact['compositions']
        if not isinstance(agent_comps, list):
            return 0.0
        gold_by_x = {c['x']: c for c in gold_comps}
        # value accuracy
        fields = ['lattice_param_A', 'bulk_modulus_GPa', 'thermal_expansion_1e-5_per_K',
                  'gruneisen_param', 'heat_capacity_J_molK', 'debye_temp_K']
        total_value_points = 0
        value_ok = 0
        trend_score = 0.0
        trend_count = 0
        # collect endpoints for global ordering
        endpoint_a = {}
        endpoint_B = {}
        for agent_comp in agent_comps:
            x = agent_comp.get('x')
            if x is None or x not in gold_by_x:
                continue
            gold_data = gold_by_x[x]['thermal_data']
            agent_data = agent_comp.get('thermal_data')
            if not isinstance(agent_data, dict):
                continue
            for field in fields:
                gold_arr = gold_data.get(field, [])
                agent_arr = agent_data.get(field, [])
                if not gold_arr or not agent_arr or len(gold_arr) != len(agent_arr):
                    continue
                tol = tolerances.get(field, {})
                for i, ref in enumerate(gold_arr):
                    val = agent_arr[i]
                    if val is None:
                        continue
                    if isinstance(tol, dict):
                        if 'absolute' in tol:
                            ok = abs(val - ref) <= tol['absolute']
                        elif 'relative' in tol:
                            rel = tol['relative']
                            if ref != 0:
                                ok = abs(val - ref) / abs(ref) <= rel
                            else:
                                ok = abs(val) < 1e-6
                        else:
                            ok = False
                    else:
                        ok = abs(val - ref) <= (tol if tol is not None else 1e-6)
                    if ok:
                        value_ok += 1
                    total_value_points += 1
            # trends (excluding thermal expansion, which is not monotonic in the paper)
            latt = agent_data.get('lattice_param_A')
            if latt and len(latt)==6:
                if check_monotonic(latt, increasing=True):
                    trend_score += 1
                trend_count += 1
            bul = agent_data.get('bulk_modulus_GPa')
            if bul and len(bul)==6:
                if check_monotonic(bul, increasing=False):
                    trend_score += 1
                trend_count += 1
            cv = agent_data.get('heat_capacity_J_molK')
            if cv and len(cv)==6:
                if check_monotonic(cv, increasing=True):
                    trend_score += 1
                trend_count += 1
            debye = agent_data.get('debye_temp_K')
            if debye and len(debye)==6:
                if check_monotonic(debye, increasing=False):
                    trend_score += 1
                trend_count += 1
            # grab endpoints for ordering
            if x in (0.0, 1.0):
                if latt and len(latt)>0:
                    endpoint_a[x] = latt[0]
                if bul and len(bul)>0:
                    endpoint_B[x] = bul[0]
        # global ordering check
        if endpoint_a.get(0.0) is not None and endpoint_a.get(1.0) is not None:
            if endpoint_a[0.0] > endpoint_a[1.0]:
                trend_score += 1
            trend_count += 1
        if endpoint_B.get(1.0) is not None and endpoint_B.get(0.0) is not None:
            if endpoint_B[1.0] > endpoint_B[0.0]:
                trend_score += 1
            trend_count += 1
        value_score = value_ok / total_value_points if total_value_points>0 else 0.0
        trend_s = trend_score / trend_count if trend_count>0 else 0.0
        # combine: 70% value, 30% trend
        return 0.7 * value_score + 0.3 * trend_s


_SCORERS = {
    'step_01_structural': score_0,
    'step_02_electronic': score_1,
    'step_03_thermal': score_2,
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
