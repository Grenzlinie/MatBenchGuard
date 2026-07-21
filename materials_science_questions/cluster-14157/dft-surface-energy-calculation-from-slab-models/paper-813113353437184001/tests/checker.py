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
    def prepare(outputs_dir, spec):
        ctx = {}
        for step in spec.get('steps', []):
            ctx[step['id']] = {
                'gold': step.get('gold'),
                'tolerance_abs': step.get('tolerance_abs', 0.1),
                'trend_check': step.get('trend_check')
            }
        return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        step_ctx = ctx.get(step['id'], {})
        gold = step_ctx.get('gold', {})
        tol = step_ctx.get('tolerance_abs', 0.3)
        trend_check = step_ctx.get('trend_check', {})
        trend_w = trend_check.get('weight_in_step', 0.3)
        # Row accuracy
        correct = 0
        total = 0
        agent_vals = {}
        for row in artifact:
            metal = row.get('metal')
            cov = row.get('coverage_ML')
            val = float(row.get('delta_E_f_eV_per_Sn', 0.0))
            # Store for trend
            try:
                cov_float = float(cov)
                agent_vals[(metal, cov_float)] = val
            except:
                pass
            target = gold.get(metal, {}).get(str(cov))
            if target is not None:
                if abs(val - target) <= tol:
                    correct += 1
                total += 1
        row_acc = correct / total if total > 0 else 0.0
        # Trend check: Ru > Ni > Pt at each coverage 0.25, 0.5, 0.75
        covs = [0.25, 0.5, 0.75]
        metals_order = ['Ru', 'Ni', 'Pt']
        trend_ok = 0
        trend_total = 0
        for cov in covs:
            vals = []
            valid = True
            for m in metals_order:
                v = agent_vals.get((m, cov))
                if v is None:
                    valid = False
                    break
                vals.append(v)
            if valid and len(vals) == 3:
                trend_total += 1
                # Check Ru > Ni > Pt
                if vals[0] > vals[1] > vals[2]:
                    trend_ok += 1
        trend_acc = trend_ok / trend_total if trend_total > 0 else 0.0
        acc_w = 1.0 - trend_w
        return row_acc * acc_w + trend_acc * trend_w


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        step_ctx = ctx.get(step['id'], {})
        gold = step_ctx.get('gold', {})
        tol = step_ctx.get('tolerance_abs', 0.5)
        trend_check = step_ctx.get('trend_check', {})
        trend_w = trend_check.get('weight_in_step', 0.3)
        correct = 0
        total = 0
        agent_vals = {}
        for row in artifact:
            metal = row.get('metal')
            cov = row.get('coverage_ML')
            val = float(row.get('delta_E_seg_eV_per_Sn', 0.0))
            try:
                cov_float = float(cov)
                agent_vals[(metal, cov_float)] = val
            except:
                pass
            target = gold.get(metal, {}).get(str(cov))
            if target is not None:
                if abs(val - target) <= tol:
                    correct += 1
                total += 1
        row_acc = correct / total if total > 0 else 0.0
        covs = [0.25, 0.5, 0.75]
        metals_order = ['Ru', 'Ni', 'Pt']  # expected Ru < Ni < Pt (more negative < less negative)
        trend_ok = 0
        trend_total = 0
        for cov in covs:
            vals = []
            valid = True
            for m in metals_order:
                v = agent_vals.get((m, cov))
                if v is None:
                    valid = False
                    break
                vals.append(v)
            if valid and len(vals) == 3:
                trend_total += 1
                # Check Ru < Ni < Pt
                if vals[0] < vals[1] < vals[2]:
                    trend_ok += 1
        trend_acc = trend_ok / trend_total if trend_total > 0 else 0.0
        acc_w = 1.0 - trend_w
        return row_acc * acc_w + trend_acc * trend_w


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
