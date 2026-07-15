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
    steps = spec.get('steps', [])
    gold_rows = []
    tolerances = {}
    acc_weight = 0.8
    trend_weight = 0.2
    for step in steps:
        if step.get('id') == 'factors_check':
            gold_rows = step.get('gold', [])
            tolerances = step.get('tolerances', {})
            acc_weight = step.get('accuracy_weight', 0.8)
            trend_weight = step.get('trend_weight', 0.2)
            break
    return {'gold_rows': gold_rows, 'tolerances': tolerances, 'accuracy_weight': acc_weight, 'trend_weight': trend_weight}


# === block: score_0 (check id='factors_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    cols = {'T', 'A_N', 'M_N', 'A_P', 'M_P'}
    if not all(col in artifact[0] for col in cols):
        return 0.0
    agent_rows = {}
    for row in artifact:
        try:
            t = int(row['T'])
            agent_rows[t] = row
        except (ValueError, KeyError):
            continue
    gold_rows = ctx['gold_rows']
    tolerances = ctx['tolerances']
    acc_weight = float(ctx['accuracy_weight'])
    trend_weight = float(ctx['trend_weight'])

    # accuracy per-factor
    factor_keys = ['A_N', 'M_N', 'A_P', 'M_P']
    rel_tols = {
        'A_N': tolerances.get('A_N_rel', 0.10),
        'M_N': tolerances.get('M_N_rel', 0.25),
        'A_P': tolerances.get('A_P_rel', 0.05),
        'M_P': tolerances.get('M_P_rel', 0.05)
    }
    eps = 1e-6
    n_vals = 0
    acc_sum = 0.0
    for g in gold_rows:
        T = g['T']
        if T not in agent_rows:
            continue
        row = agent_rows[T]
        for key in factor_keys:
            if key not in row:
                continue
            try:
                val = float(row[key])
            except (ValueError, TypeError):
                continue
            gold_val = float(g[key])
            rel_err = abs(val - gold_val) / (gold_val * rel_tols[key] + eps)
            factor_score = max(0.0, 1.0 - rel_err)
            acc_sum += factor_score
            n_vals += 1
    if n_vals == 0:
        return 0.0
    accuracy_score = acc_sum / n_vals

    # trend score
    temp_sorted = sorted(gold_rows, key=lambda x: x['T'])
    electron_A = [agent_rows[g['T']]['A_N'] for g in temp_sorted if g['T'] in agent_rows and 'A_N' in agent_rows[g['T']]]
    electron_M = [agent_rows[g['T']]['M_N'] for g in temp_sorted if g['T'] in agent_rows and 'M_N' in agent_rows[g['T']]]
    electron_A_valid = len(electron_A) > 1
    electron_M_valid = len(electron_M) > 1
    mono_A = 0
    if electron_A_valid:
        pairs = len(electron_A) - 1
        good = sum(1 for i in range(pairs) if float(electron_A[i+1]) >= float(electron_A[i]) - 1e-6)
        mono_A = good / max(1, pairs) if pairs > 0 else 1.0
    mono_M = 0
    if electron_M_valid:
        pairs = len(electron_M) - 1
        good = sum(1 for i in range(pairs) if float(electron_M[i+1]) >= float(electron_M[i]) - 1e-6)
        mono_M = good / max(1, pairs) if pairs > 0 else 1.0
    if electron_A_valid and electron_M_valid:
        electron_mono_score = (mono_A + mono_M) / 2.0
    elif electron_A_valid:
        electron_mono_score = mono_A
    elif electron_M_valid:
        electron_mono_score = mono_M
    else:
        electron_mono_score = 0.0
    # hole near-unity: count fraction within generous bounds
    hole_vals = []
    for g in gold_rows:
        T = g['T']
        if T not in agent_rows:
            continue
        row = agent_rows[T]
        for key in ['A_P', 'M_P']:
            if key in row:
                try:
                    hole_vals.append((key, float(row[key])))
                except (ValueError, TypeError):
                    continue
    hole_ok = 0
    for key, val in hole_vals:
        if key == 'A_P' and 0.9 <= val <= 1.2:
            hole_ok += 1
        elif key == 'M_P' and 0.8 <= val <= 1.5:
            hole_ok += 1
    hole_score = hole_ok / max(1, len(hole_vals)) if hole_vals else 0.0

    if electron_A_valid or electron_M_valid:
        trend_score = 0.6 * electron_mono_score + 0.4 * hole_score
    else:
        trend_score = hole_score

    final = acc_weight * accuracy_score + trend_weight * trend_score
    return max(0.0, min(1.0, final))


_SCORERS = {
    'factors_check': score_0,
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
