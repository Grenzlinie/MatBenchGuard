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
    return {'gold_moments': {'Co_Ti': {'0': 0.93, '-2': 0.99}, 'Co_Ti+V_O': {'+2': 1.89, '0': 0.95}}, 'moment_tol': 0.25}


# === block: score_0 (check id='defect_results_check') ===
def score_0(artifact, step, ctx):
    data = artifact
    ctx_data = ctx or {}
    gold_moments = ctx_data.get('gold_moments', {})
    moment_tol = ctx_data.get('moment_tol', 0.25)
    score_moment = 0.0
    total_moments = 0
    if 'magnetic_moments' in data:
        mm = data['magnetic_moments']
        for defect, states in gold_moments.items():
            if defect not in mm:
                total_moments += len(states)
                continue
            for charge, expected in states.items():
                agent_val = mm[defect].get(charge, None)
                total_moments += 1
                if agent_val is not None and isinstance(agent_val, (int, float)) and abs(agent_val - expected) <= moment_tol:
                    score_moment += 1.0
        if total_moments > 0:
            score_moment = score_moment / total_moments
    else:
        score_moment = 0.0
    score_fmafm = 0.0
    if 'FM_AFM_difference' in data and 'Co_Ti-Co_Ti_neutral' in data['FM_AFM_difference']:
        val = data['FM_AFM_difference']['Co_Ti-Co_Ti_neutral']
        if isinstance(val, (int, float)) and val <= -0.05:
            score_fmafm = 1.0
    pair_passed = 0
    pair_attempted = 0
    if 'pair_energies' in data:
        pe = data['pair_energies']
        # neutral Co_Ti pair: clustering (minimum separation energy should be smallest)
        if 'Co_Ti-Co_Ti_neutral' in pe:
            pair_attempted += 1
            neut = pe['Co_Ti-Co_Ti_neutral']
            try:
                items = [(float(k), v) for k, v in neut.items() if isinstance(v, (int, float))]
                if len(items) >= 2:
                    min_item = min(items, key=lambda x: x[0])
                    max_item = max(items, key=lambda x: x[0])
                    if min_item[1] <= max_item[1]:
                        pair_passed += 1
            except (ValueError, TypeError):
                pass
        if 'Co_Ti-Co_Ti_charged' in pe:
            pair_attempted += 1
            ch = pe['Co_Ti-Co_Ti_charged']
            try:
                items = [(float(k), v) for k, v in ch.items() if isinstance(v, (int, float))]
                if len(items) >= 2:
                    min_item = min(items, key=lambda x: x[0])
                    max_item = max(items, key=lambda x: x[0])
                    if min_item[1] >= max_item[1]:
                        pair_passed += 1
            except (ValueError, TypeError):
                pass
        if 'Co_Ti+V_O_neutral' in pe:
            pair_attempted += 1
            comp = pe['Co_Ti+V_O_neutral']
            try:
                items = [(float(k), v) for k, v in comp.items() if isinstance(v, (int, float))]
                if len(items) >= 2:
                    min_item = min(items, key=lambda x: x[0])
                    max_item = max(items, key=lambda x: x[0])
                    if min_item[1] <= max_item[1]:
                        pair_passed += 1
            except (ValueError, TypeError):
                pass
    score_pairs = (pair_passed / max(1, pair_attempted)) if pair_attempted > 0 else 0.0
    score_form = 0.0
    if 'formation_energies' in data:
        fe = data['formation_energies']
        co_int_vals = []
        other_vals = []
        for defect, states in fe.items():
            for charge, val in states.items():
                if isinstance(val, (int, float)):
                    if defect == 'Co_int':
                        co_int_vals.append(val)
                    else:
                        other_vals.append(val)
        if co_int_vals and other_vals and max(co_int_vals) > max(other_vals):
            score_form = 1.0
    return 0.25 * score_moment + 0.2 * score_fmafm + 0.3 * score_pairs + 0.25 * score_form


_SCORERS = {
    'defect_results_check': score_0,
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
