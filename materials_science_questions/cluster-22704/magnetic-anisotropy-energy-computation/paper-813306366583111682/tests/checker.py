import os
import json
import csv

# === author imports / helpers ===
import math
from typing import Dict, Any, List, Tuple


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
    step = spec['steps'][0]
    gold_mae = step.get('gold_mae', {})
    return {'gold_mae': gold_mae}


# === block: score_0 (check id='step06') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        entries = {}
        for item in artifact:
            key = (item['system'], item['geometry_state'], item['electric_field'])
            entries[key] = item
        # 1. relaxation increases MAE
        c1 = 0
        co_unrel = entries.get(('pure_Co', 'unrelaxed', 0))
        co_rel = entries.get(('pure_Co', 'relaxed', 0))
        if co_unrel and co_rel and co_rel['MAE'] - co_unrel['MAE'] > 0.05:
            c1 += 1
        copt_unrel = entries.get(('Co_Pt', 'unrelaxed', 0))
        copt_rel = entries.get(('Co_Pt', 'relaxed', 0))
        if copt_unrel and copt_rel and copt_rel['MAE'] - copt_unrel['MAE'] > 0.05:
            c1 += 1
        score_relax = (c1 / 2) * 0.3
        # 2. monotonic field dependence (more negative -> higher MAE)
        fields_order = [-1.0, -0.5, 0.0, 0.5, 1.0]
        mae_vals = []
        for f in fields_order:
            item = entries.get(('pure_Co', 'relaxed', f))
            if item is None:
                mae_vals = None
                break
            mae_vals.append(item['MAE'])
        score_mono = 0.0
        if mae_vals is not None:
            violations = 0
            for i in range(len(mae_vals) - 1):
                if mae_vals[i] < mae_vals[i + 1] - 1e-3:
                    violations += 1
            if violations <= 1:
                score_mono = 0.3
        # 3. easy-axis orientation (relaxed should be out-of-plane, theta <= 10 deg)
        orient_ok = 0
        if co_rel and co_rel.get('easy_theta', 99) <= 10:
            orient_ok += 1
        if copt_rel and copt_rel.get('easy_theta', 99) <= 10:
            orient_ok += 1
        score_orient = (orient_ok / 2) * 0.2
        # 4. absolute MAE values within ±1 meV of paper gold
        gold_mae = ctx.get('gold_mae', {})
        total_cond = len(gold_mae)
        matched = 0
        for key_str, expected in gold_mae.items():
            sys, geom, field_str = key_str.split('|')
            field_val = float(field_str)
            key = (sys, geom, field_val)
            item = entries.get(key)
            if item and abs(item['MAE'] - expected) <= 1.0:
                matched += 1
        score_abs = (matched / total_cond) * 0.2
        total = score_relax + score_mono + score_orient + score_abs
        return min(total, 1.0)


_SCORERS = {
    'step06': score_0,
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
