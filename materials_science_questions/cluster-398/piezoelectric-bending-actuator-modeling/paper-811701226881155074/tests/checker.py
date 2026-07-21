import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    gold = spec.get('hidden_gold', {})
    return {'gold_sparam': gold.get('sc_s11_s12', {}),
            'gold_conv': gold.get('convergence_table', {}).get('gold_rows', [])}


# === block: score_0 (check id='sc_s11_s12_check') ===
def score_0(artifact, step, ctx):
    tol = step.get('tolerance_abs', 0.01)
    gold = ctx['gold_sparam']
    gold_freqs = gold.get('frequencies', [])
    gold_s11 = gold.get('S11_mag', [])
    gold_s12 = gold.get('S12_mag', [])
    if not artifact or len(artifact) == 0:
        return 0.0
    agent_dict = {float(row['frequency']): (float(row['S11_mag']), float(row['S12_mag'])) for row in artifact}
    row_scores = []
    for f, g11, g12 in zip(gold_freqs, gold_s11, gold_s12):
        agent_vals = agent_dict.get(f)
        if agent_vals is None:
            row_scores.append(0.0)
            continue
        a11, a12 = agent_vals
        diff = max(abs(a11 - g11), abs(a12 - g12))
        if diff <= tol:
            row_scores.append(1.0)
        elif diff <= 2 * tol:
            row_scores.append(1.0 - (diff - tol) / tol)
        else:
            row_scores.append(0.0)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


# === block: score_1 (check id='convergence_table_check') ===
def score_1(artifact, step, ctx):
    gold_rows = ctx['gold_conv']
    if not artifact or len(artifact) < 6:
        return 0.0
    agent_by_order = {}
    for row in artifact:
        try:
            o = int(row['order'])
            agent_by_order[o] = {
                'unknowns': int(row['unknowns']),
                'memory': float(row['memory_MB']),
                'cpu': float(row['cpu_time_min']),
                's11': float(row['rel_error_S11']),
                's12': float(row['rel_error_S12'])
            }
        except (ValueError, KeyError):
            continue
    error_scores_s11 = []
    error_scores_s12 = []
    unknowns_ok = True
    for g in gold_rows:
        o = g['order']
        a = agent_by_order.get(o)
        if a is None:
            return 0.0
        if a['unknowns'] != g['unknowns']:
            unknowns_ok = False
        # rel_error scoring: directional, lower is better
        def err_score(agent_val, gold_val):
            if gold_val == 0:
                return 1.0 if agent_val <= 1e-10 else 0.0
            ratio = agent_val / gold_val
            if ratio <= 1.0:
                return 1.0
            elif ratio <= 2.0:
                return 2.0 - ratio
            else:
                return 0.0
        error_scores_s11.append(err_score(a['s11'], g['rel_error_S11']))
        error_scores_s12.append(err_score(a['s12'], g['rel_error_S12']))
    avg_s11 = sum(error_scores_s11) / len(error_scores_s11)
    avg_s12 = sum(error_scores_s12) / len(error_scores_s12)
    # monotonic decrease check
    orders_sorted = sorted(agent_by_order.keys())
    s11_seq = [agent_by_order[o]['s11'] for o in orders_sorted]
    s12_seq = [agent_by_order[o]['s12'] for o in orders_sorted]
    mono_s11 = all(s11_seq[i] >= s11_seq[i+1] for i in range(len(s11_seq)-1))
    mono_s12 = all(s12_seq[i] >= s12_seq[i+1] for i in range(len(s12_seq)-1))
    mono_score = (1.0 if mono_s11 else 0.0) + (1.0 if mono_s12 else 0.0)
    mono_score /= 2.0
    # memory/cpu loose check (within factor 2)
    mem_ok, cpu_ok = True, True
    for g in gold_rows:
        a = agent_by_order[g['order']]
        if not (0.2 * g['memory_MB'] <= a['memory'] <= 5.0 * g['memory_MB']):
            mem_ok = False
        if not (0.2 * g['cpu_time_min'] <= a['cpu'] <= 5.0 * g['cpu_time_min']):
            cpu_ok = False
    mem_score = 1.0 if mem_ok else 0.0
    cpu_score = 1.0 if cpu_ok else 0.0
    unknowns_score = 1.0 if unknowns_ok else 0.0
    # combine sub-scores with weights
    final = (avg_s11 * 0.3 + avg_s12 * 0.3 + mono_score * 0.15 + unknowns_score * 0.05 + mem_score * 0.1 + cpu_score * 0.1)
    return max(0.0, min(1.0, final))


_SCORERS = {
    'sc_s11_s12_check': score_0,
    'convergence_table_check': score_1,
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
